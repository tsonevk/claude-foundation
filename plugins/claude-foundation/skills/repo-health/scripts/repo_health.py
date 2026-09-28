#!/usr/bin/env python3
"""Dependency-free, read-only repository health triage."""

from __future__ import annotations

import argparse
import ast
import collections
import shutil
import subprocess
import sys
from pathlib import Path


CODE_EXTS = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".java", ".go", ".rs",
    ".c", ".cc", ".cpp", ".h", ".hpp", ".sh", ".bash", ".ksh",
    ".ps1", ".tf", ".hcl", ".sql", ".rb", ".php",
}

SKIP_DIRS = {
    ".git", ".venv", "venv", "node_modules", "vendor", "dist", "build",
    "coverage", ".next", ".terraform", ".tox", ".mypy_cache",
    ".pytest_cache", "__pycache__", "target",
}

SENSITIVE = (
    ".env",
    "secret",
    "credential",
    "token",
    "private_key",
    "private-key",
)

OPTIONAL = (
    "ruff",
    "radon",
    "vulture",
    "eslint",
    "tsc",
    "tflint",
    "terraform",
    "ansible-lint",
    "pytest",
)


def git(repo: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )

    if proc.returncode:
        raise RuntimeError(proc.stderr.strip() or "git command failed")

    return proc.stdout


def repo_root(path: Path) -> Path:
    return Path(
        git(path, "rev-parse", "--show-toplevel").strip()
    ).resolve()


def sensitive(path: str) -> bool:
    value = path.lower()
    return any(marker in value for marker in SENSITIVE)


def skipped(path: str) -> bool:
    return any(part in SKIP_DIRS for part in Path(path).parts)


def tracked(repo: Path) -> list[str]:
    proc = subprocess.run(
        ["git", "-C", str(repo), "ls-files", "-z"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    if proc.returncode:
        raise RuntimeError(
            proc.stderr.decode("utf-8", "replace").strip()
        )

    return [
        item.decode("utf-8", "replace")
        for item in proc.stdout.split(b"\0")
        if item
    ]


def count_lines(path: Path) -> int:
    with path.open("rb") as handle:
        return sum(1 for _ in handle)


def source_stats(
    repo: Path,
    paths: list[str],
) -> tuple[list[dict], int, int]:

    rows = []
    skipped_count = 0
    redacted = 0

    for rel in paths:
        if sensitive(rel):
            redacted += 1
            continue

        if skipped(rel):
            skipped_count += 1
            continue

        ext = Path(rel).suffix.lower()

        if ext not in CODE_EXTS:
            continue

        full = repo / rel

        if not full.is_file():
            continue

        try:
            size = full.stat().st_size

            if size > 5 * 1024 * 1024:
                continue

            rows.append(
                {
                    "path": rel,
                    "ext": ext,
                    "loc": count_lines(full),
                }
            )
        except OSError:
            pass

    return rows, skipped_count, redacted


def churn(
    repo: Path,
    days: int,
) -> collections.Counter:

    output = git(
        repo,
        "log",
        "--no-merges",
        f"--since={days}.days",
        "-n",
        "500",
        "--name-only",
        "--format=",
    )

    counts = collections.Counter()

    for rel in output.splitlines():
        rel = rel.strip()

        if not rel or sensitive(rel) or skipped(rel):
            continue

        if Path(rel).suffix.lower() in CODE_EXTS:
            counts[rel] += 1

    return counts


def python_hotspots(
    repo: Path,
    rows: list[dict],
) -> list[tuple]:

    branch_types = (
        ast.If,
        ast.For,
        ast.AsyncFor,
        ast.While,
        ast.Try,
        ast.BoolOp,
        ast.IfExp,
        ast.Match,
        ast.comprehension,
    )

    found = []

    for row in rows:
        if row["ext"] != ".py":
            continue

        try:
            tree = ast.parse(
                (repo / row["path"]).read_text(
                    encoding="utf-8",
                    errors="replace",
                )
            )
        except (OSError, SyntaxError):
            continue

        for node in ast.walk(tree):
            if not isinstance(
                node,
                (ast.FunctionDef, ast.AsyncFunctionDef),
            ):
                continue

            end = getattr(
                node,
                "end_lineno",
                node.lineno,
            )

            loc = max(
                1,
                end - node.lineno + 1,
            )

            branches = sum(
                isinstance(item, branch_types)
                for item in ast.walk(node)
            )

            if loc >= 80 or branches >= 12:
                found.append(
                    (
                        loc + branches * 5,
                        loc,
                        branches,
                        row["path"],
                        node.name,
                    )
                )

    return sorted(
        found,
        reverse=True,
    )


def report(
    repo: Path,
    rows: list[dict],
    skipped_count: int,
    redacted: int,
    churn_counts: collections.Counter,
    days: int,
    top: int,
) -> None:

    languages = collections.defaultdict(
        lambda: [0, 0]
    )

    for row in rows:
        languages[row["ext"]][0] += 1
        languages[row["ext"]][1] += row["loc"]

    changed = sum(
        bool(line.strip())
        for line in git(
            repo,
            "status",
            "--porcelain",
        ).splitlines()
    )

    tools = [
        name
        for name in OPTIONAL
        if shutil.which(name)
    ]

    print("REPO_HEALTH_SCAN")
    print(f"root: {repo}")
    print(f"source_files: {len(rows)}")
    print(
        f"source_loc: "
        f"{sum(item['loc'] for item in rows)}"
    )
    print(f"working_tree_entries: {changed}")
    print(
        "generated_or_vendor_paths_skipped: "
        f"{skipped_count}"
    )
    print(
        "sensitive_looking_paths_redacted: "
        f"{redacted}"
    )
    print(
        "optional_tools_available: "
        f"{', '.join(tools) if tools else 'none'}"
    )

    print("\nLANGUAGES")

    for ext, (files, loc) in sorted(
        languages.items(),
        key=lambda item: -item[1][1],
    )[:top]:
        print(
            f"{ext}: files={files} loc={loc}"
        )

    print("\nLARGEST_SOURCE_FILES")

    for row in sorted(
        rows,
        key=lambda item: (
            -item["loc"],
            item["path"],
        ),
    )[:top]:
        print(
            f"{row['loc']:6d} loc  "
            f"{row['path']}"
        )

    print(
        f"\nCHURN_LAST_{days}_DAYS"
    )

    for path, touches in churn_counts.most_common(top):
        print(
            f"{touches:6d} touches  {path}"
        )

    by_path = {
        row["path"]: row
        for row in rows
    }

    hotspots = []

    for path, row in by_path.items():
        touches = churn_counts.get(
            path,
            0,
        )

        score = (
            min(row["loc"] / 500.0, 4.0)
            + min(touches / 5.0, 4.0)
        )

        if score >= 2.0:
            hotspots.append(
                (
                    score,
                    row["loc"],
                    touches,
                    path,
                )
            )

    print("\nSIZE_X_CHURN_HOTSPOTS")

    for score, loc, touches, path in sorted(
        hotspots,
        reverse=True,
    )[:top]:
        print(
            f"score={score:4.2f} "
            f"loc={loc:5d} "
            f"touches={touches:3d}  "
            f"{path}"
        )

    functions = python_hotspots(
        repo,
        rows,
    )

    print("\nPYTHON_FUNCTION_HOTSPOTS")

    if functions:
        for _, loc, branches, path, name in functions[:top]:
            print(
                f"loc={loc:4d} "
                f"branches={branches:3d}  "
                f"{path}:{name}"
            )
    else:
        print("none")

    severe_files = sum(
        row["loc"] >= 1200
        for row in rows
    )

    severe_functions = sum(
        loc >= 150 or branches >= 20
        for _, loc, branches, _, _ in functions
    )

    severe_hotspots = sum(
        score >= 5.0
        for score, *_ in hotspots
    )

    if (
        severe_files
        or severe_functions
        or severe_hotspots
    ):
        verdict = "REFACTOR_RECOMMENDED"

    elif (
        any(row["loc"] >= 800 for row in rows)
        or hotspots
    ):
        verdict = "WATCH"

    else:
        verdict = "HEALTHY"

    print("\nVERDICT")
    print(verdict)
    print(
        "note: deterministic triage only; "
        "inspect only top hotspots before "
        "proposing changes"
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Read-only repository health scan"
        )
    )

    parser.add_argument(
        "--repo",
        default=".",
    )

    parser.add_argument(
        "--top",
        type=int,
        default=10,
    )

    parser.add_argument(
        "--churn-days",
        type=int,
        default=90,
    )

    args = parser.parse_args()

    try:
        root = repo_root(
            Path(args.repo).resolve()
        )

        rows, skipped_count, redacted = source_stats(
            root,
            tracked(root),
        )

        counts = churn(
            root,
            max(1, args.churn_days),
        )

        report(
            root,
            rows,
            skipped_count,
            redacted,
            counts,
            max(1, args.churn_days),
            max(1, args.top),
        )

        return 0

    except (OSError, RuntimeError) as exc:
        print(
            f"repo-health: {exc}",
            file=sys.stderr,
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
