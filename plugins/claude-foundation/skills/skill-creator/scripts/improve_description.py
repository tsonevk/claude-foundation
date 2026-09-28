#!/usr/bin/env python3
"""Improve a skill description based on eval results.

Calls the local Claude CLI with an explicit, non-secret environment allowlist.
No API key, token, password, credential, or unrelated CI variable is inherited.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
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


def _call_claude(prompt: str, model: str | None, timeout: int = 300) -> str:
    """Run `claude -p` with the prompt on stdin and return the text response."""
    env = build_claude_env()
    claude_binary = shutil.which("claude", path=env.get("PATH"))
    if not claude_binary:
        raise RuntimeError("claude executable was not found on the allowlisted PATH")

    cmd = [claude_binary, "-p", "--output-format", "text"]
    if model:
        cmd.extend(["--model", model])

    result = subprocess.run(
        cmd,
        input=prompt,
        capture_output=True,
        text=True,
        env=env,
        timeout=timeout,
        shell=False,
        check=False,
    )
    if result.returncode != 0:
        stderr = (result.stderr or "").strip()
        detail = stderr[-1000:] if stderr else "no stderr output"
        raise RuntimeError(f"claude -p exited {result.returncode}: {detail}")
    return result.stdout


def improve_description(
    skill_name: str,
    skill_content: str,
    current_description: str,
    eval_results: dict,
    history: list[dict],
    model: str,
    test_results: dict | None = None,
    log_dir: Path | None = None,
    iteration: int | None = None,
) -> str:
    """Call Claude to improve the description based on eval results."""
    failed_triggers = [
        result
        for result in eval_results["results"]
        if result["should_trigger"] and not result["pass"]
    ]
    false_triggers = [
        result
        for result in eval_results["results"]
        if not result["should_trigger"] and not result["pass"]
    ]

    train_score = (
        f"{eval_results['summary']['passed']}/{eval_results['summary']['total']}"
    )
    if test_results:
        test_score = (
            f"{test_results['summary']['passed']}/{test_results['summary']['total']}"
        )
        scores_summary = f"Train: {train_score}, Test: {test_score}"
    else:
        scores_summary = f"Train: {train_score}"

    prompt = f"""You are optimizing a skill description for a Claude Code skill called "{skill_name}". A "skill" is sort of like a prompt, but with progressive disclosure -- there's a title and description that Claude sees when deciding whether to use the skill, and then if it does use the skill, it reads the .md file which has lots more details and potentially links to other resources in the skill folder like helper files and scripts and additional documentation or examples.

The description appears in Claude's "available_skills" list. When a user sends a query, Claude decides whether to invoke the skill based solely on the title and on this description. Your goal is to write a description that triggers for relevant queries, and doesn't trigger for irrelevant ones.

Here's the current description:
<current_description>
"{current_description}"
</current_description>

Current scores ({scores_summary}):
<scores_summary>
"""
    if failed_triggers:
        prompt += "FAILED TO TRIGGER (should have triggered but didn't):\n"
        for result in failed_triggers:
            prompt += (
                f'  - "{result["query"]}" '
                f'(triggered {result["triggers"]}/{result["runs"]} times)\n'
            )
        prompt += "\n"

    if false_triggers:
        prompt += "FALSE TRIGGERS (triggered but shouldn't have):\n"
        for result in false_triggers:
            prompt += (
                f'  - "{result["query"]}" '
                f'(triggered {result["triggers"]}/{result["runs"]} times)\n'
            )
        prompt += "\n"

    if history:
        prompt += (
            "PREVIOUS ATTEMPTS (do NOT repeat these — try something structurally "
            "different):\n\n"
        )
        for attempt in history:
            train_result = (
                f"{attempt.get('train_passed', attempt.get('passed', 0))}/"
                f"{attempt.get('train_total', attempt.get('total', 0))}"
            )
            test_result = (
                f"{attempt.get('test_passed', '?')}/{attempt.get('test_total', '?')}"
                if attempt.get("test_passed") is not None
                else None
            )
            score_text = f"train={train_result}"
            if test_result:
                score_text += f", test={test_result}"
            prompt += f"<attempt {score_text}>\n"
            prompt += f'Description: "{attempt["description"]}"\n'
            if "results" in attempt:
                prompt += "Train results:\n"
                for result in attempt["results"]:
                    status = "PASS" if result["pass"] else "FAIL"
                    prompt += (
                        f'  [{status}] "{result["query"][:80]}" '
                        f'(triggered {result["triggers"]}/{result["runs"]})\n'
                    )
            if attempt.get("note"):
                prompt += f'Note: {attempt["note"]}\n'
            prompt += "</attempt>\n\n"

    prompt += f"""</scores_summary>

Skill content (for context on what the skill does):
<skill_content>
{skill_content}
</skill_content>

Based on the failures, write a new and improved description that is more likely to trigger correctly. When I say "based on the failures", it's a bit of a tricky line to walk because we don't want to overfit to the specific cases you're seeing. So what I DON'T want you to do is produce an ever-expanding list of specific queries that this skill should or shouldn't trigger for. Instead, try to generalize from the failures to broader categories of user intent and situations where this skill would be useful or not useful. The reason for this is twofold:

1. Avoid overfitting
2. The list might get loooong and it's injected into ALL queries and there might be a lot of skills, so we don't want to blow too much space on any given description.

Concretely, your description should not be more than about 100-200 words, even if that comes at the cost of accuracy. There is a hard limit of 1024 characters — descriptions over that will be truncated, so stay comfortably under it.

Here are some tips that we've found to work well in writing these descriptions:
- The skill should be phrased in the imperative -- "Use this skill for" rather than "this skill does"
- The skill description should focus on the user's intent, what they are trying to achieve, vs. the implementation details of how the skill works.
- The description competes with other skills for Claude's attention — make it distinctive and immediately recognizable.
- If you're getting lots of failures after repeated attempts, change things up. Try different sentence structures or wordings.

I'd encourage you to be creative and mix up the style in different iterations since you'll have multiple opportunities to try different approaches and we'll just grab the highest-scoring one at the end.

Please respond with only the new description text in <new_description> tags, nothing else."""

    text = _call_claude(prompt, model)
    match = re.search(r"<new_description>(.*?)</new_description>", text, re.DOTALL)
    description = match.group(1).strip().strip('"') if match else text.strip().strip('"')

    transcript: dict = {
        "iteration": iteration,
        "prompt": prompt,
        "response": text,
        "parsed_description": description,
        "char_count": len(description),
        "over_limit": len(description) > 1024,
    }

    if len(description) > 1024:
        shorten_prompt = (
            f"{prompt}\n\n---\n\n"
            f"A previous attempt produced this description, which at "
            f"{len(description)} characters is over the 1024-character hard limit:\n\n"
            f'"{description}"\n\n'
            "Rewrite it to be under 1024 characters while keeping the most "
            "important trigger words and intent coverage. Respond with only "
            "the new description in <new_description> tags."
        )
        shorten_text = _call_claude(shorten_prompt, model)
        match = re.search(
            r"<new_description>(.*?)</new_description>", shorten_text, re.DOTALL
        )
        shortened = (
            match.group(1).strip().strip('"')
            if match
            else shorten_text.strip().strip('"')
        )
        transcript["rewrite_prompt"] = shorten_prompt
        transcript["rewrite_response"] = shorten_text
        transcript["rewrite_description"] = shortened
        transcript["rewrite_char_count"] = len(shortened)
        description = shortened

    transcript["final_description"] = description

    if log_dir:
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / f"improve_iter_{iteration or 'unknown'}.json"
        log_file.write_text(json.dumps(transcript, indent=2), encoding="utf-8")

    return description


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Improve a skill description based on eval results"
    )
    parser.add_argument(
        "--eval-results", required=True, help="Path to eval results JSON"
    )
    parser.add_argument("--skill-path", required=True, help="Path to skill directory")
    parser.add_argument("--history", default=None, help="Path to previous attempts JSON")
    parser.add_argument("--model", required=True, help="Model for improvement")
    parser.add_argument("--verbose", action="store_true", help="Print progress to stderr")
    args = parser.parse_args()

    skill_path = Path(args.skill_path)
    if not (skill_path / "SKILL.md").exists():
        print(f"Error: No SKILL.md found at {skill_path}", file=sys.stderr)
        raise SystemExit(1)

    eval_results = json.loads(Path(args.eval_results).read_text(encoding="utf-8"))
    history = (
        json.loads(Path(args.history).read_text(encoding="utf-8"))
        if args.history
        else []
    )

    name, _, content = parse_skill_md(skill_path)
    current_description = eval_results["description"]

    if args.verbose:
        print(f"Current: {current_description}", file=sys.stderr)
        print(
            f"Score: {eval_results['summary']['passed']}/"
            f"{eval_results['summary']['total']}",
            file=sys.stderr,
        )

    new_description = improve_description(
        skill_name=name,
        skill_content=content,
        current_description=current_description,
        eval_results=eval_results,
        history=history,
        model=args.model,
    )

    if args.verbose:
        print(f"Improved: {new_description}", file=sys.stderr)

    output = {
        "description": new_description,
        "history": history
        + [
            {
                "description": current_description,
                "passed": eval_results["summary"]["passed"],
                "failed": eval_results["summary"]["failed"],
                "total": eval_results["summary"]["total"],
                "results": eval_results["results"],
            }
        ],
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
