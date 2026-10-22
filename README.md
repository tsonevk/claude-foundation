# Claude Foundation

Public distribution mirror for the version-controlled Claude plugin used by Claude Code, VS Code, Claude Desktop, Cowork, and related agent workflows.

## Repository role

This repository is a **public downstream distribution mirror**, not the source of truth. The canonical private repository is `tsonevk/claude`, where `claude-foundation/` is tracked. Only `.claude-plugin/`, `plugins/`, and `EXCLUDED.md` are synchronized; this mirror's README and validation scripts are maintained separately.

The plugin provides:
- reusable skills, focused agents, and slash commands (see `plugins/claude-foundation/` for the current inventory);
- automatic/context-driven capability routing;
- DevOps, OCI, Linux, iMX, Kubernetes, Ansible, Terraform, CI/CD, security, agent-runtime and repository-governance workflows.

## Runtime model

```text
private canonical: tsonevk/claude (main)
        |                                  |
        v                                  v
local ~/.claude/claude-foundation/   distribution sync
        |                                  |
        v                                  v
Claude Code / VS Code         public tsonevk/claude-foundation
                                           |
                                           v
                                Claude Desktop / Cowork
                                 personal "Your plugins"
```

The local Claude Code marketplace is **not** replaced by the Desktop/Cowork installation.

Do not remove the local `ktsonev-local` marketplace until a replacement runtime has been independently validated.

## Privacy / Team account boundary

This repository is public. Never commit private runtime state or secrets. Account-level plugin installation can remain personal.

When uploading the plugin in a Team Claude account:
- keep it under **Your plugins**;
- keep **Publish to org** disabled;
- do not publish it to the organization;
- do not share it with other users or groups unless explicitly intended.

Marketplace plugins installed from Anthropic/third-party sources are separate from this custom plugin.

## Local Claude Code / VS Code

Recommended local location:

```text
~/.claude/claude-foundation
```

The repository exposes a local marketplace at:

```text
.claude-plugin/marketplace.json
```

Claude Code can keep using the local marketplace runtime while the private `tsonevk/claude` repository remains the version-controlled source.

## Claude Desktop / Cowork

For a private personal installation in a Team account, package and upload only the plugin directory:

```text
plugins/claude-foundation/
```

The archive root must contain:

```text
.claude-plugin/
agents/
commands/
skills/
skill-metadata.json
```

Do **not** archive the parent `~/.claude` directory or any runtime/session state.

Example on Windows PowerShell:

```powershell
$src = "$env:USERPROFILE\.claude\claude-foundation\plugins\claude-foundation"
$dst = "$env:USERPROFILE\Downloads\claude-foundation.zip"

Remove-Item $dst -Force -ErrorAction SilentlyContinue
tar.exe -a -c -f $dst -C $src .
Get-Item $dst
```

Then:

```text
Claude Desktop
-> Customize
-> Plugins
-> Add
-> Upload plugin
-> claude-foundation.zip
```

Keep **Publish to org** off.

## Routing principles

- Natural-language requests are the primary interface.
- Automatically select a relevant skill/plugin/agent from task context when useful.
- Do not require the user to remember slash commands.
- Use one primary capability by default; add another only for a genuinely separate risk or validation need.
- Clear scoped work should execute directly without unnecessary orchestration.
- Workflow depth scales with ambiguity, risk, and blast radius.
- Keep low-risk reversible work AI-first; switch to reasoning-first for high-consequence work by establishing invariants, causal/failure models, falsification, validation, and rollback before mutation.

## Safety

- Project-local `AGENTS.md`, `CLAUDE.md`, current-task and decision documents remain authoritative.
- Read before mutation.
- Prefer small, reversible changes.
- Never expose passwords, tokens, certificates, private keys, SSH credentials, or protected logs.
- Referenced repositories are read-only unless explicitly authorized.
- Production-impacting actions require explicit approval.
- Whole-instance iMX stop/restart/shutdown requires explicit reconfirmation.
- Claude Code may use native SSH where appropriate.
- Claude Desktop/Cowork may use an approved local SSH bridge; SSH credentials remain workstation-managed.

## Validation

Run the standalone repository validation after plugin or marketplace changes:

```bash
python3 scripts/validate_repository.py
```

This verifies the marketplace-to-plugin path, plugin identity, installed skill/agent/command inventory, and that local runtime/private-state paths were not committed.

Deeper skill-routing and catalog checks remain part of the local Claude Code maintenance workflow until they are adapted for this standalone repository.

## Canonical and distribution boundaries

The embedded `claude-foundation/` in private `tsonevk/claude` remains canonical for Claude Code / VS Code. This public repository distributes the approved plugin payload for Claude Desktop / Cowork and other consumers. The canonical repository's publish workflow and its local hooks are separate publication paths; see the canonical README for the current security trade-offs and review gates.

Do not treat this mirror as the implementation source or change local runtime provisioning solely because the mirror exists. Validate each runtime independently before changing its installation.
