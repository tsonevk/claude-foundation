---
description: Evaluate a Claude Code plugin, marketplace, skill pack, or agent pack before local adoption.
---

Use this command when reviewing a Claude Code plugin, marketplace, skill pack, or agent pack before adoption.

## Input

Provide one or more of:

- plugin repository URL
- marketplace URL
- plugin name
- local plugin path
- intended project or workflow

## Process

1. Use `claude-foundation:claude-plugin-adoption`.
2. Inspect the source before recommending install.
3. Identify what the plugin adds:
   - slash commands
   - agents
   - skills
   - MCP/tool config
   - shell hooks or scripts
   - documentation/templates
4. Classify risk:
   - `LOW`: docs, prompts, static templates only
   - `MEDIUM`: commands that edit files or run local checks
   - `HIGH`: shell execution, network access, credentials, git push, deploy, package installation, MCP/tool changes
5. Check fit for the current project:
   - existing architecture
   - test strategy
   - CI/CD flow
   - security boundaries
   - token/context cost
6. Prefer adaptation over direct install when the plugin is broad, young, unpinned, or not project-specific.

## Output

Return:

- Verdict: `INSTALL`, `ADAPT`, `PILOT`, or `REJECT`
- Useful parts to keep
- Parts to avoid
- Security concerns
- Required approval before install or execution
- Minimal local implementation plan

## Hard stops

Do not install or run a third-party plugin when it:

- requests secrets or credentials without a clear need
- modifies shell startup files
- changes git remotes, hooks, or credentials
- performs deployment by default
- downloads opaque binaries
- requires broad network or filesystem access without justification
