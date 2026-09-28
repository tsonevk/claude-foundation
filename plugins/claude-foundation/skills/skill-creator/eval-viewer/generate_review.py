#!/usr/bin/env python3
"""Generate and serve a review page for skill-evaluation results.

The viewer is local-only. It never terminates an existing process to claim a
port: if the requested loopback port is unavailable, it binds an ephemeral
loopback port instead. Use --static for a standalone HTML artifact.
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import re
import sys
import webbrowser
from functools import partial
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Any


METADATA_FILES = {"transcript.md", "user_notes.md", "metrics.json"}
TEXT_EXTENSIONS = {
    ".txt",
    ".md",
    ".json",
    ".csv",
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".yaml",
    ".yml",
    ".xml",
    ".html",
    ".css",
    ".sh",
    ".rb",
    ".go",
    ".rs",
    ".java",
    ".c",
    ".cpp",
    ".h",
    ".hpp",
    ".sql",
    ".r",
    ".toml",
}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}
MIME_OVERRIDES = {
    ".svg": "image/svg+xml",
    ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
}


def get_mime_type(path: Path) -> str:
    extension = path.suffix.lower()
    if extension in MIME_OVERRIDES:
        return MIME_OVERRIDES[extension]
    mime, _ = mimetypes.guess_type(str(path))
    return mime or "application/octet-stream"


def _read_json(path: Path) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def find_runs(workspace: Path) -> list[dict[str, Any]]:
    """Find directories containing an outputs/ directory."""
    runs: list[dict[str, Any]] = []
    _find_runs_recursive(workspace, workspace, runs)
    runs.sort(key=lambda item: (item.get("eval_id", float("inf")), item["id"]))
    return runs


def _find_runs_recursive(
    root: Path,
    current: Path,
    runs: list[dict[str, Any]],
) -> None:
    if not current.is_dir():
        return

    if (current / "outputs").is_dir():
        run = build_run(root, current)
        if run:
            runs.append(run)
        return

    skip = {"node_modules", ".git", "__pycache__", "skill", "inputs"}
    try:
        children = sorted(current.iterdir())
    except OSError:
        return
    for child in children:
        if child.is_dir() and child.name not in skip:
            _find_runs_recursive(root, child, runs)


def _find_task_and_eval_id(run_dir: Path) -> tuple[str, Any | None]:
    task_text = ""
    eval_id: Any | None = None

    for candidate in (
        run_dir / "eval_metadata.json",
        run_dir.parent / "eval_metadata.json",
    ):
        metadata = _read_json(candidate)
        if isinstance(metadata, dict):
            task_text = str(metadata.get("prompt") or "")
            eval_id = metadata.get("eval_id")
            if task_text:
                return task_text, eval_id

    for candidate in (
        run_dir / "transcript.md",
        run_dir / "outputs" / "transcript.md",
    ):
        try:
            text = candidate.read_text(encoding="utf-8")
        except OSError:
            continue
        match = re.search(r"## Eval Prompt\n\n([\s\S]*?)(?=\n##|$)", text)
        if match:
            return match.group(1).strip(), eval_id

    return "(No prompt found)", eval_id


def _load_grading(run_dir: Path) -> Any | None:
    for candidate in (
        run_dir / "grading.json",
        run_dir.parent / "grading.json",
    ):
        grading = _read_json(candidate)
        if grading:
            return grading
    return None


def build_run(root: Path, run_dir: Path) -> dict[str, Any] | None:
    """Build one viewer run from metadata, outputs, and grading."""
    outputs_dir = run_dir / "outputs"
    if not outputs_dir.is_dir():
        return None

    task_text, eval_id = _find_task_and_eval_id(run_dir)
    output_files: list[dict[str, Any]] = []
    try:
        children = sorted(outputs_dir.iterdir())
    except OSError:
        children = []
    for path in children:
        if path.is_file() and path.name not in METADATA_FILES:
            output_files.append(embed_file(path))

    run_id = str(run_dir.relative_to(root)).replace("/", "-").replace("\\", "-")
    return {
        "id": run_id,
        "prompt": task_text,
        "eval_id": eval_id,
        "outputs": output_files,
        "grading": _load_grading(run_dir),
    }


def _read_bytes_as_base64(path: Path) -> str | None:
    try:
        return base64.b64encode(path.read_bytes()).decode("ascii")
    except OSError:
        return None


def embed_file(path: Path) -> dict[str, Any]:
    """Return a browser-embeddable representation of one output file."""
    extension = path.suffix.lower()
    mime = get_mime_type(path)

    if extension in TEXT_EXTENSIONS:
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            content = "(Error reading file)"
        return {"name": path.name, "type": "text", "content": content}

    encoded = _read_bytes_as_base64(path)
    if encoded is None:
        return {
            "name": path.name,
            "type": "error",
            "content": "(Error reading file)",
        }

    if extension in IMAGE_EXTENSIONS:
        return {
            "name": path.name,
            "type": "image",
            "mime": mime,
            "data_uri": f"data:{mime};base64,{encoded}",
        }
    if extension == ".pdf":
        return {
            "name": path.name,
            "type": "pdf",
            "data_uri": f"data:{mime};base64,{encoded}",
        }
    if extension == ".xlsx":
        return {"name": path.name, "type": "xlsx", "data_b64": encoded}
    return {
        "name": path.name,
        "type": "binary",
        "mime": mime,
        "data_uri": f"data:{mime};base64,{encoded}",
    }


def load_previous_iteration(workspace: Path) -> dict[str, dict[str, Any]]:
    """Load previous feedback and outputs keyed by run id."""
    result: dict[str, dict[str, Any]] = {}
    feedback_map: dict[str, str] = {}

    feedback_data = _read_json(workspace / "feedback.json")
    if isinstance(feedback_data, dict):
        reviews = feedback_data.get("reviews", [])
        if isinstance(reviews, list):
            for review in reviews:
                if not isinstance(review, dict):
                    continue
                run_id = str(review.get("run_id") or "")
                feedback = str(review.get("feedback") or "").strip()
                if run_id and feedback:
                    feedback_map[run_id] = feedback

    for run in find_runs(workspace):
        result[run["id"]] = {
            "feedback": feedback_map.get(run["id"], ""),
            "outputs": run.get("outputs", []),
        }

    for run_id, feedback in feedback_map.items():
        result.setdefault(run_id, {"feedback": feedback, "outputs": []})
    return result


def generate_html(
    runs: list[dict[str, Any]],
    skill_name: str,
    previous: dict[str, dict[str, Any]] | None = None,
    benchmark: dict[str, Any] | None = None,
) -> str:
    """Generate a standalone HTML document from the existing viewer template."""
    template_path = Path(__file__).parent / "viewer.html"
    template = template_path.read_text(encoding="utf-8")

    previous_feedback: dict[str, str] = {}
    previous_outputs: dict[str, list[dict[str, Any]]] = {}
    for run_id, data in (previous or {}).items():
        feedback = str(data.get("feedback") or "")
        outputs = data.get("outputs")
        if feedback:
            previous_feedback[run_id] = feedback
        if isinstance(outputs, list) and outputs:
            previous_outputs[run_id] = outputs

    embedded: dict[str, Any] = {
        "skill_name": skill_name,
        "runs": runs,
        "previous_feedback": previous_feedback,
        "previous_outputs": previous_outputs,
    }
    if benchmark is not None:
        embedded["benchmark"] = benchmark

    return template.replace(
        "/*__EMBEDDED_DATA__*/",
        f"const EMBEDDED_DATA = {json.dumps(embedded)};",
    )


class ReviewHandler(BaseHTTPRequestHandler):
    """Serve the viewer and save review feedback inside the workspace."""

    def __init__(
        self,
        workspace: Path,
        skill_name: str,
        feedback_path: Path,
        previous: dict[str, dict[str, Any]],
        benchmark_path: Path | None,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        self.workspace = workspace
        self.skill_name = skill_name
        self.feedback_path = feedback_path
        self.previous = previous
        self.benchmark_path = benchmark_path
        super().__init__(*args, **kwargs)

    def _send_bytes(
        self,
        status: int,
        content_type: str,
        content: bytes,
    ) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self) -> None:
        if self.path in {"/", "/index.html"}:
            benchmark = (
                _read_json(self.benchmark_path)
                if self.benchmark_path is not None
                else None
            )
            if not isinstance(benchmark, dict):
                benchmark = None
            html = generate_html(
                find_runs(self.workspace),
                self.skill_name,
                self.previous,
                benchmark,
            )
            self._send_bytes(200, "text/html; charset=utf-8", html.encode("utf-8"))
            return

        if self.path == "/api/feedback":
            try:
                data = self.feedback_path.read_bytes()
            except OSError:
                data = b"{}"
            self._send_bytes(200, "application/json", data)
            return

        self.send_error(404)

    def do_POST(self) -> None:
        if self.path != "/api/feedback":
            self.send_error(404)
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            length = 0
        if length < 0 or length > 5_000_000:
            self._send_bytes(
                413,
                "application/json",
                b'{"error":"feedback payload too large"}',
            )
            return

        body = self.rfile.read(length)
        try:
            data = json.loads(body)
            if not isinstance(data, dict) or not isinstance(data.get("reviews"), list):
                raise ValueError("Expected JSON object with a reviews list")
            self.feedback_path.write_text(
                json.dumps(data, indent=2) + "\n",
                encoding="utf-8",
            )
        except (json.JSONDecodeError, OSError, ValueError) as exc:
            response = json.dumps({"error": str(exc)}).encode("utf-8")
            self._send_bytes(400, "application/json", response)
            return

        self._send_bytes(200, "application/json", b'{"ok":true}')

    def log_message(self, format: str, *args: object) -> None:
        pass


def create_server(
    requested_port: int,
    handler: Any,
) -> tuple[HTTPServer, int, bool]:
    """Bind the requested loopback port or fall back to an ephemeral port."""
    if requested_port < 0 or requested_port > 65535:
        raise ValueError("port must be between 0 and 65535")

    try:
        server = HTTPServer(("127.0.0.1", requested_port), handler)
        return server, int(server.server_address[1]), False
    except OSError:
        if requested_port == 0:
            raise
        server = HTTPServer(("127.0.0.1", 0), handler)
        return server, int(server.server_address[1]), True


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate and serve eval review")
    parser.add_argument("workspace", type=Path, help="Workspace directory")
    parser.add_argument(
        "--port",
        "-p",
        type=int,
        default=3117,
        help="Preferred loopback port; falls back safely if occupied",
    )
    parser.add_argument("--skill-name", "-n", default=None)
    parser.add_argument("--previous-workspace", type=Path, default=None)
    parser.add_argument("--benchmark", type=Path, default=None)
    parser.add_argument(
        "--static",
        "-s",
        type=Path,
        default=None,
        help="Write standalone HTML instead of starting a server",
    )
    args = parser.parse_args()

    workspace = args.workspace.resolve()
    if not workspace.is_dir():
        print(f"Error: {workspace} is not a directory", file=sys.stderr)
        raise SystemExit(1)

    runs = find_runs(workspace)
    if not runs:
        print(f"No runs found in {workspace}", file=sys.stderr)
        raise SystemExit(1)

    skill_name = args.skill_name or workspace.name.replace("-workspace", "")
    feedback_path = workspace / "feedback.json"
    previous = (
        load_previous_iteration(args.previous_workspace.resolve())
        if args.previous_workspace
        else {}
    )
    benchmark_path = args.benchmark.resolve() if args.benchmark else None
    benchmark = (
        _read_json(benchmark_path)
        if benchmark_path is not None
        else None
    )
    if not isinstance(benchmark, dict):
        benchmark = None

    if args.static:
        html = generate_html(runs, skill_name, previous, benchmark)
        args.static.parent.mkdir(parents=True, exist_ok=True)
        args.static.write_text(html, encoding="utf-8")
        print(f"\n  Static viewer written to: {args.static}\n")
        return

    handler = partial(
        ReviewHandler,
        workspace,
        skill_name,
        feedback_path,
        previous,
        benchmark_path,
    )
    try:
        server, port, used_fallback = create_server(args.port, handler)
    except (OSError, ValueError) as exc:
        print(f"Error: unable to start loopback viewer: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    url = f"http://localhost:{port}"
    print("\n  Eval Viewer")
    print("  --------------------------------")
    print(f"  URL:       {url}")
    print(f"  Workspace: {workspace}")
    print(f"  Feedback:  {feedback_path}")
    if used_fallback:
        print(f"  Port:      requested {args.port}; using {port} because it was occupied")
    if previous:
        print(f"  Previous:  {args.previous_workspace} ({len(previous)} runs)")
    if benchmark_path:
        print(f"  Benchmark: {benchmark_path}")
    print("\n  Press Ctrl+C to stop.\n")

    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
