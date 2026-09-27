# Claude Foundation

Private, version-controlled Claude plugin foundation for the user's Claude Code, VS Code, Claude Desktop, Cowork, and related agent workflows.

## Repository role

This repository is the **source of truth** for `claude-foundation`.

It is intentionally private.

The plugin provides:
- 168 skills;
- 10 focused agents;
- 6 slash commands;
- automatic/context-driven capability routing;
- DevOps, OCI, Linux, iMX, Kubernetes, Ansible, Terraform, CI/CD, security, agent-runtime and repository-governance workflows.

## Runtime model

```text
private GitHub: tsonevk/claude-foundation
                  |
                  | source of truth
                  |
        +---------+------------------+
        |                            |
        v                            v
local clone/runtime             packaged plugin
~/.claude/claude-foundation     Claude Desktop / Cowork
        |                            |
        v                            v
Claude Code / VS Code           personal "Your plugins"
```

The local Claude Code marketplace is **not** replaced by the Desktop/Cowork installation.

Do not remove the local `ktsonev-local` marketplace until a replacement runtime has been independently validated.

## Privacy / Team account boundary

The repository and plugin are private personal tooling.

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

Claude Code can keep using the local marketplace runtime while this GitHub repository remains the version-controlled source.

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

Run the repository checks after plugin changes:

```bash
python3 scripts/check_description_collisions.py --top 25
python3 scripts/check_manifest_consistency.py --check
python3 scripts/check_related_refs.py
python3 scripts/generate_skill_index.py --check
```

## Migration status

The original embedded copy currently exists in `tsonevk/claude` for compatibility.

Migration policy:
1. populate and validate this standalone repository;
2. point the local runtime at this repository/clone;
3. validate Claude Code / VS Code;
4. validate Desktop/Cowork packaged installation;
5. only then remove or deprecate the embedded copy in `tsonevk/claude`.

Do not perform step 5 prematurely.
