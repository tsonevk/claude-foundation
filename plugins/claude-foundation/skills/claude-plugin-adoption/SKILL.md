---
name: claude-plugin-adoption
description: Evaluate, adapt, or pilot Claude Code plugins, marketplaces, agent packs, and skill packs before adoption. Use when a task mentions Claude plugins, plugin marketplaces, external skill packs, agent packs, or installing/adapting third-party Claude Code workflow tools.
---

# Claude Plugin Adoption

## Purpose

Evaluate whether a third-party Claude Code plugin, marketplace, agent pack, or skill pack should be rejected, adapted locally, piloted, or installed.

Prefer small local adaptations over broad installs. This keeps `~/.claude` self-contained and avoids runtime dependencies on external agent-policy, coding-assistant, or marketplace repositories.

## Default stance

Third-party plugins are untrusted until reviewed. They may still be useful as design references even when they are not safe to install.

Use community plugins as:

1. research input
2. local adaptation candidates
3. controlled pilots
4. direct installs only after explicit approval

## Decision labels

- `REJECT`: not useful, stale, too risky, or duplicates local guidance
- `ADAPT`: useful ideas, but copy only selected local docs/prompts/commands
- `PILOT`: worth testing in a scratch branch or disposable repository
- `INSTALL`: safe and valuable enough for project-level installation after approval

## Review steps

1. Identify the plugin source, intended project, and requested outcome.
2. Inspect visible source files before recommending install.
3. List plugin components:
   - commands
   - agents
   - skills
   - docs/templates
   - scripts
   - MCP/tool configuration
4. Classify risk:
   - `LOW`: documentation, prompts, static templates
   - `MEDIUM`: file edits, test execution, local checks
   - `HIGH`: shell execution, network access, credentials, git push, deploy, package install, MCP/tool permission changes
5. Compare against local project authority and existing architecture.
6. Prefer the smallest reversible local implementation.

## Adoption levels

| Level | Meaning | Default |
| --- | --- | --- |
| Reference | Read and extract ideas only | Allowed |
| Adapt | Copy selected docs/prompts/commands locally | Allowed after review |
| Pilot | Test in scratch branch or disposable repo | Allowed with guardrails |
| Install | Install plugin into a real project | Explicit approval only |
| Trust | Allow privileged workflow execution | Explicit approval only |

## Good first candidates

Start with low-risk workflow value:

- documentation/source loading
- repository review checklists
- quality/testing workflows
- security review prompts
- lifecycle planning templates

## Poor first candidates

Avoid early adoption of:

- production deployment automation
- credential management
- payment/auth workflows
- model-routing services
- broad full-stack scaffolding
- plugins that install binaries or packages
- plugins that silently add MCP servers or tool permissions

## Hard stops

Do not install or run a third-party plugin when it:

- requests secrets or credentials without a clear need
- modifies shell startup files
- changes git remotes, hooks, or credentials
- performs deployment by default
- downloads opaque binaries
- requires broad network or filesystem access without justification
- changes MCP/tool permissions silently

## Output format

```md
## Verdict

REJECT | ADAPT | PILOT | INSTALL

## Why

## Keep

## Avoid

## Risk

LOW | MEDIUM | HIGH

## Required Approval

## Minimal Next Step
```

## References

Read `references/plugin-adoption-policy.md` when the task asks for a broader policy, install guardrails, or repeatable rollout process.
