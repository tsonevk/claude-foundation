#!/usr/bin/env python3
"""Validate the standalone Claude Foundation repository layout.

Standard-library-only and read-only.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
PLUGIN_DIR = ROOT / "plugins" / "claude-foundation"
PLUGIN_MANIFEST = PLUGIN_DIR / ".claude-plugin" / "plugin.json"

FORBIDDEN_NAMES = {
    ".credentials.json",
    "sessions",
    "session-env",
    "state",
    "telemetry",
    "shell-snapshots",
    "file-history",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_json(path: Path) -> dict:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def main() -> int:
    marketplace = read_json(MARKETPLACE)
    plugin = read_json(PLUGIN_MANIFEST)

    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or len(plugins) != 1:
        fail("marketplace must contain exactly one plugin entry")

    entry = plugins[0]
    if entry.get("name") != plugin.get("name"):
        fail("marketplace plugin name does not match plugin.json")

    source = entry.get("source")
    if not isinstance(source, str):
        fail("marketplace plugin source is missing")
    resolved_source = (ROOT / source).resolve()
    if resolved_source != PLUGIN_DIR.resolve():
        fail("marketplace source must resolve to plugins/claude-foundation")

    if plugin.get("name") != "claude-foundation":
        fail("plugin name must be claude-foundation")

    skills_dir = PLUGIN_DIR / "skills"
    agents_dir = PLUGIN_DIR / "agents"
    commands_dir = PLUGIN_DIR / "commands"

    skill_count = sum(1 for p in skills_dir.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())
    agent_count = len(list(agents_dir.glob("*.md")))
    command_count = len(list(commands_dir.glob("*.md")))

    forbidden = []
    for path in ROOT.rglob("*"):
        if path.name in FORBIDDEN_NAMES:
            forbidden.append(str(path.relative_to(ROOT)))
    if forbidden:
        fail("forbidden runtime/private paths found: " + ", ".join(forbidden))

    print(f"marketplace: {marketplace.get('name')}")
    print(f"plugin: {plugin.get('name')} v{plugin.get('version')}")
    print(f"skills: {skill_count}")
    print(f"agents: {agent_count}")
    print(f"commands: {command_count}")
    print("standalone repository validation: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
