#!/usr/bin/env python3
"""Run trigger evaluation for a skill description.

Each query runs in an isolated temporary project. The child Claude process
receives only an explicit environment allowlist; API keys, tokens, passwords,
and unrelated CI variables are not inherited.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import select
import shutil
import subprocess
import sys
import tempfile
import time
import uuid
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

from scripts.utils import parse_skill_md


_CHILD_ENV_ALLOWLIST = (
    "PATH",
    "HOME",
    "USER",
    "LOGNAME",
    "SHELL",
    "LANG",
    "LC_ALL",
    "LC_CTYPE",
    "TERM",
    "COLORTERM",
    "NO_COLOR",
    "TMPDIR",
    "TMP",
    "TEMP",
    "XDG_CONFIG_HOME",
    "XDG_CACHE_HOME",
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "NO_PROXY",
    "http_proxy",
    "https_proxy",
    "no_proxy",
    "SSL_CERT_FILE",
    "SSL_CERT_DIR",
    "REQUESTS_CA_BUNDLE",
    "NODE_EXTRA_CA_CERTS",
    "SYSTEMROOT",
    "COMSPEC",
    "PATHEXT",
    "APPDATA",
    "LOCALAPPDATA",
    "USERPROFILE",
)


def build_claude_env() -> dict[str, str]:
    """Return the minimal non-secret environment required by the Claude CLI."""
    env: dict[str, str] = {}
    for name in _CHILD_ENV_ALLOWLIST:
        value = os.environ.get(name)
        if value:
            env[name] = value
    return env


def resolve_claude_binary(env: dict[str, str]) -> str:
    """Resolve Claude from the allowlisted PATH and fail closed if unavailable."""
    binary = shutil.which("claude", path=env.get("PATH"))
    if not binary:
        raise RuntimeError("claude executable was not found on the allowlisted PATH")
    return binary


def _safe_skill_name(skill_name: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9_-]+", "-", skill_name).strip("-")
    return (normalized or "skill")[:80]


def _terminate_process(process: subprocess.Popen[bytes]) -> None:
    """Stop the child process, escalating only if graceful termination stalls."""
    if process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(timeout=2)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=2)


def run_single_query(
    query: str,
    skill_name: str,
    skill_description: str,
    timeout: int,
    model: str | None = None,
) -> bool:
    """Run one trigger query in an isolated temporary Claude project."""
    unique_id = uuid.uuid4().hex[:8]
    clean_name = f"{_safe_skill_name(skill_name)}-skill-{unique_id}"
    env = build_claude_env()
    claude_binary = resolve_claude_binary(env)

    with tempfile.TemporaryDirectory(prefix="skill-trigger-eval-") as temp_dir:
        isolated_root = Path(temp_dir)
        project_commands_dir = isolated_root / ".claude" / "commands"
        project_commands_dir.mkdir(parents=True, exist_ok=True)
        command_file = project_commands_dir / f"{clean_name}.md"

        indented_desc = "\n  ".join(skill_description.split("\n"))
        command_file.write_text(
            "---\n"
            "description: |\n"
            f"  {indented_desc}\n"
            "---\n\n"
            f"# {skill_name}\n\n"
            f"This skill handles: {skill_description}\n",
            encoding="utf-8",
        )

        cmd = [
            claude_binary,
            "-p",
            query,
            "--output-format",
            "stream-json",
            "--verbose",
            "--include-partial-messages",
        ]
        if model:
            cmd.extend(["--model", model])

        process = subprocess.Popen(
            cmd,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            cwd=isolated_root,
            env=env,
            shell=False,
        )

        triggered = False
        start_time = time.monotonic()
        buffer = ""
        pending_tool_name: str | None = None
        accumulated_json = ""

        try:
            if process.stdout is None:
                raise RuntimeError("claude subprocess stdout was not captured")

            while time.monotonic() - start_time < timeout:
                if process.poll() is not None:
                    remaining = process.stdout.read()
                    if remaining:
                        buffer += remaining.decode("utf-8", errors="replace")
                    break

                ready, _, _ = select.select([process.stdout], [], [], 1.0)
                if not ready:
                    continue

                chunk = os.read(process.stdout.fileno(), 8192)
                if not chunk:
                    break
                buffer += chunk.decode("utf-8", errors="replace")

                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    line = line.strip()
                    if not line:
                        continue

                    try:
                        event = json.loads(line)
                    except json.JSONDecodeError:
                        continue

                    if event.get("type") == "stream_event":
                        stream_event = event.get("event", {})
                        event_type = stream_event.get("type", "")

                        if event_type == "content_block_start":
                            content_block = stream_event.get("content_block", {})
                            if content_block.get("type") != "tool_use":
                                continue
                            tool_name = content_block.get("name", "")
                            if tool_name not in ("Skill", "Read"):
                                return False
                            pending_tool_name = tool_name
                            accumulated_json = ""

                        elif event_type == "content_block_delta" and pending_tool_name:
                            delta = stream_event.get("delta", {})
                            if delta.get("type") == "input_json_delta":
                                accumulated_json += delta.get("partial_json", "")
                                if clean_name in accumulated_json:
                                    return True

                        elif event_type in ("content_block_stop", "message_stop"):
                            if pending_tool_name:
                                return clean_name in accumulated_json
                            if event_type == "message_stop":
                                return False

                    elif event.get("type") == "assistant":
                        message = event.get("message", {})
                        for content_item in message.get("content", []):
                            if content_item.get("type") != "tool_use":
                                continue
                            tool_name = content_item.get("name", "")
                            tool_input = content_item.get("input", {})
                            if tool_name == "Skill" and clean_name in tool_input.get("skill", ""):
                                triggered = True
                            elif tool_name == "Read" and clean_name in tool_input.get("file_path", ""):
                                triggered = True
                            return triggered

                    elif event.get("type") == "result":
                        return triggered
        finally:
            _terminate_process(process)

        return triggered


def run_eval(
    eval_set: list[dict],
    skill_name: str,
    description: str,
    num_workers: int,
    timeout: int,
    runs_per_query: int = 1,
    trigger_threshold: float = 0.5,
    model: str | None = None,
) -> dict:
    """Run the full eval set and return aggregate trigger results."""
    results: list[dict] = []

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        future_to_info = {}
        for item in eval_set:
            for run_idx in range(runs_per_query):
                future = executor.submit(
                    run_single_query,
                    item["query"],
                    skill_name,
                    description,
                    timeout,
                    model,
                )
                future_to_info[future] = (item, run_idx)

        query_triggers: dict[str, list[bool]] = {}
        query_items: dict[str, dict] = {}
        for future in as_completed(future_to_info):
            item, _ = future_to_info[future]
            query = item["query"]
            query_items[query] = item
            query_triggers.setdefault(query, [])
            try:
                query_triggers[query].append(future.result())
            except Exception as exc:
                print(f"Warning: query failed: {exc}", file=sys.stderr)
                query_triggers[query].append(False)

    for query, triggers in query_triggers.items():
        item = query_items[query]
        trigger_rate = sum(triggers) / len(triggers)
        should_trigger = item["should_trigger"]
        did_pass = (
            trigger_rate >= trigger_threshold
            if should_trigger
            else trigger_rate < trigger_threshold
        )
        results.append(
            {
                "query": query,
                "should_trigger": should_trigger,
                "trigger_rate": trigger_rate,
                "triggers": sum(triggers),
                "runs": len(triggers),
                "pass": did_pass,
            }
        )

    passed = sum(1 for result in results if result["pass"])
    total = len(results)
    return {
        "skill_name": skill_name,
        "description": description,
        "results": results,
        "summary": {
            "total": total,
            "passed": passed,
            "failed": total - passed,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run trigger evaluation for a skill description"
    )
    parser.add_argument("--eval-set", required=True, help="Path to eval set JSON file")
    parser.add_argument("--skill-path", required=True, help="Path to skill directory")
    parser.add_argument("--description", default=None, help="Override description to test")
    parser.add_argument("--num-workers", type=int, default=10, help="Number of parallel workers")
    parser.add_argument("--timeout", type=int, default=30, help="Timeout per query in seconds")
    parser.add_argument("--runs-per-query", type=int, default=3, help="Number of runs per query")
    parser.add_argument("--trigger-threshold", type=float, default=0.5, help="Trigger rate threshold")
    parser.add_argument("--model", default=None, help="Model to use for claude -p")
    parser.add_argument("--verbose", action="store_true", help="Print progress to stderr")
    args = parser.parse_args()

    eval_set = json.loads(Path(args.eval_set).read_text(encoding="utf-8"))
    skill_path = Path(args.skill_path)
    if not (skill_path / "SKILL.md").exists():
        print(f"Error: No SKILL.md found at {skill_path}", file=sys.stderr)
        raise SystemExit(1)

    name, original_description, _ = parse_skill_md(skill_path)
    description = args.description or original_description

    if args.verbose:
        print(f"Evaluating: {description}", file=sys.stderr)

    output = run_eval(
        eval_set=eval_set,
        skill_name=name,
        description=description,
        num_workers=args.num_workers,
        timeout=args.timeout,
        runs_per_query=args.runs_per_query,
        trigger_threshold=args.trigger_threshold,
        model=args.model,
    )

    if args.verbose:
        summary = output["summary"]
        print(f"Results: {summary['passed']}/{summary['total']} passed", file=sys.stderr)
        for result in output["results"]:
            status = "PASS" if result["pass"] else "FAIL"
            rate = f"{result['triggers']}/{result['runs']}"
            print(
                f"  [{status}] rate={rate} expected={result['should_trigger']}: "
                f"{result['query'][:70]}",
                file=sys.stderr,
            )

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
