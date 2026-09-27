---
name: claude-plugin-authoring
description: Author, structure, and maintain a local Claude Code plugin — marketplace registration, plugin.json, skills, agents, skills-preload binding, skill-vs-agent decision criteria, legacy commands migration, auto-discovery, namespace scoping, and idempotent install.sh bootstrap.
---

# Claude Code Plugin Authoring

## Purpose

Create and maintain a local Claude Code plugin: a versioned, self-contained library of skills,
subagents, and slash commands — auto-discovered by Claude Code without any manual registration.

## Directory structure

```
<plugin-root>/                          ← local marketplace root (any name)
  .claude-plugin/
    marketplace.json                    ← declares available plugins in this marketplace
  plugins/<plugin-name>/                ← one plugin
    .claude-plugin/
      plugin.json                       ← plugin identity and version
    skills/<skill-name>/
      SKILL.md                          ← loaded on demand via Skill tool
    agents/<agent-name>.md              ← subagent definitions
    commands/<command-name>.md          ← slash commands (/command-name)
```

## marketplace.json

```json
{
  "plugins": [
    {
      "name": "<plugin-name>",
      "source": "./plugins/<plugin-name>"
    }
  ]
}
```

- `name` must match the directory under `plugins/` exactly.
- `source` is relative to the marketplace root directory.

## plugin.json

```json
{
  "name": "<plugin-name>",
  "displayName": "<Human Name>",
  "version": "1.0.0",
  "description": "One-line description shown in /plugin list."
}
```

- `name` must match `marketplace.json` entry and `plugins/<name>` directory.
- Bump `version` on any functional change (skills/agents/commands added, modified).

## settings.json registration

```json
{
  "extraKnownMarketplaces": {
    "<marketplace-id>": {
      "source": {
        "source": "directory",
        "path": "/absolute/path/to/<plugin-root>"
      }
    }
  },
  "enabledPlugins": {
    "<plugin-name>@<marketplace-id>": true
  }
}
```

- `path` must be absolute. Use `$HOME`-relative value for portability; fix at clone time via `install.sh`.
- `<marketplace-id>` is an arbitrary key (e.g. `ktsonev-local`).
- After adding: run `/plugin marketplace add <path>` + `/plugin install <name>@<marketplace-id>` or `/reload-plugins`.

## Skills (SKILL.md)

```markdown
---
name: my-skill-name
description: One sentence — verbs an agent would type: "review", "audit", "collect". Used for auto-load matching.
---

# Skill heading

Body: workflow steps, rules, output contract, verification.
```

- Auto-discovered: place `SKILL.md` in any `skills/<name>/` directory — no registration needed.
- Invoked via Skill tool: `Skill({ skill: "claude-foundation:my-skill-name" })`.
- Loaded into the main context window on demand; keep bodies focused.
- `name:` in frontmatter becomes the namespace suffix: `<plugin-name>:<name>`.

## Agents (.md files)

```markdown
---
name: my-agent
description: One sentence used by Claude Code for auto-routing. Be specific about trigger scenarios.
model: inherit
effort: medium
color: purple
---

Agent system prompt body here.
```

**Supported frontmatter fields:**

| Field | Purpose |
|-------|---------|
| `name` (req) | Unique ID; filename need not match |
| `description` (req) | Auto-routing trigger — state "Use when..." explicitly |
| `tools` | Allowlist (e.g. `Read, Grep, Glob, Bash`); inherits all if omitted |
| `disallowedTools` | Denylist, applied before `tools` is resolved |
| `model` | `sonnet` / `opus` / `haiku` / `fable` / full ID / `inherit` (default) |
| `effort` | `low` / `medium` / `high` / `xhigh` / `max` |
| `maxTurns` | Cap on agentic turns before the agent stops |
| `skills` | Preload full skill content at agent startup (see next section) |
| `memory` | Persistent agent memory scope: `user` / `project` / `local` |
| `background` | Always run as a background task |
| `isolation` | `worktree` — run in a temporary git worktree, isolated from parent |
| `color` | Display color (`red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink`, `cyan`) |

**Still silently ignored in plugin agents (do NOT add):** `hooks`, `mcpServers`, `permissionMode`.
These fields are valid in project-scoped agent files but are rejected/ignored in plugin agents.
Adding them causes no error but also no effect — a common source of confusion.

- Auto-discovered from `agents/*.md`.
- Referenced as `claude-foundation:<name>` in CLAUDE.md routing tables.
- Invoked via Agent tool: `Agent({ subagent_type: "claude-foundation:my-agent" })`.
- Keep agents as focused workers; synthesis and safety review stays in the parent thread.

## Binding skills to agents (`skills:` preload)

Do not duplicate skill content into an agent's system prompt. Keep the skill as the
knowledge layer and preload it into the agent:

```markdown
---
name: iac-reviewer
skills:
  - terraform-plan-safety-review
  - ansible-idempotency-safety
  - kubernetes-manifest-review
---
```

The agent starts with those skill bodies already in its context — one source of truth,
no drift between skill and agent prompt. When domain knowledge changes, edit the skill
once; every agent that preloads it picks up the change.

## Skill vs agent decision criteria

- **Keep as a SKILL** when the content is procedural knowledge, a checklist, reference
  material, or anything that needs the main conversation's context — a subagent gets a
  fresh context with NO conversation history, so session-analysis skills can never be agents.
- **Make an AGENT** when the task produces verbose intermediate output (log dumps, big
  JSON, many file reads) that would bloat main context, is self-contained with a
  summarizable result, or needs its own tool restrictions / model / effort.
- **Usually the right move is both**: the skill holds the knowledge, the agent preloads
  it via `skills:` and does the isolated work.

## Commands (.md files) — LEGACY

Custom commands have been merged into skills: `skills/deploy/SKILL.md` → `/deploy` works
identically to `commands/deploy.md` → `/deploy`. Existing `commands/*.md` files keep
working, but author new slash commands as skills.

```markdown
---
description: One sentence. Shown in /commands list.
---

Command body — instructions Claude executes when the slash command is invoked.
```

- File name becomes the slash command: `commands/my-workflow.md` → `/my-workflow`.
- Auto-discovered from `commands/*.md`.
- No name frontmatter needed — the filename IS the name.
- For new work, prefer `skills/<name>/SKILL.md` — same slash-command behavior, and the
  skill can also be auto-loaded by description matching.

## Auto-discovery rules

All three types (skills, agents, commands) are discovered automatically by Claude Code:
- No plugin.json entries required per item.
- No import/export syntax.
- Adding a new `SKILL.md`, agent `.md`, or command `.md` takes effect after `/reload-plugins` or restart.

## Namespace scoping

Always reference skills and agents with the full scoped name to avoid ambiguity:

```
claude-foundation:skill-name      ← skill invocation
claude-foundation:agent-name      ← agent routing
/command-name                     ← slash command (no namespace prefix)
```

In CLAUDE.md, list all agent routes as `plugin-name:agent-name` — bare names are ambiguous
when multiple plugins or built-in agent types are present.

## Idempotent install.sh

The `path` in `settings.json` must be absolute, but the committed value is machine-specific.
Use an `install.sh` that rewrites it at clone time:

```bash
#!/usr/bin/env bash
set -euo pipefail

CLAUDE_DIR="${HOME}/.claude"
MARKETPLACE_DIR="${CLAUDE_DIR}/<plugin-root>"

# Rewrite the absolute marketplace path for this machine
python3 - <<PY
import json, pathlib

cfg = pathlib.Path("${CLAUDE_DIR}/settings.json")
data = json.loads(cfg.read_text())
mkts = data.setdefault("extraKnownMarketplaces", {})
entry = mkts.setdefault("<marketplace-id>", {"source": {}})
entry["source"] = {"source": "directory", "path": "${MARKETPLACE_DIR}"}
cfg.write_text(json.dumps(data, indent=2) + "\n")
print(f"Marketplace path set to {MARKETPLACE_DIR}")
PY

claude plugin install <plugin-name>@<marketplace-id> 2>/dev/null || true
echo "Done. Run /reload-plugins or restart Claude Code."
```

Make it idempotent: running it twice must produce the same state.

## Verification

After install:

```bash
# In Claude Code:
/plugin           # → <plugin-name> shows as installed/enabled
/agents           # → lists your plugin agents
/commands         # → lists your plugin commands
# Invoke a skill:
Skill({ skill: "claude-foundation:my-skill-name" })
```

Check `plugins/installed_plugins.json` for `installedAt` timestamp confirming install.

## .gitignore allowlist pattern

When the plugin lives inside a tracked repo, use an allowlist `.gitignore` so runtime
files Claude Code writes (sessions, projects, cache) are never accidentally committed:

```gitignore
# Ignore everything by default
/*

# Re-include only tracked content
!.gitignore
!CLAUDE.md
!settings.json
!install.sh
!<plugin-root>/
```

Then add `!` re-include lines for each new tracked file or directory.

## Common mistakes

- **Wrong path type in settings.json**: `path` must be absolute, not `~/` (tilde is not expanded by JSON parsers).
- **Marketplace not reloaded**: new skills/agents appear only after `/reload-plugins` or Claude Code restart.
- **Agent fields not supported in plugins**: `hooks`, `mcpServers`, `permissionMode` silently do nothing in plugin agents.
- **Bare agent names in CLAUDE.md**: always use `plugin-name:agent-name`; bare names match built-in agent types first.
- **`name:` mismatch**: `marketplace.json` plugin name, `plugin.json` name, and `plugins/<name>/` directory must all be identical strings.
- **Duplicating skill content into an agent prompt** instead of using `skills:` preload — the two copies drift; edit-once semantics are lost.
- **Authoring new slash commands in `commands/`** — legacy path; use `skills/<name>/SKILL.md` instead.
