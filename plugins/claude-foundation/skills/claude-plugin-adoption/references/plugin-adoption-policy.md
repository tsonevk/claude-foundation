# Claude Code Plugin Adoption Policy

This policy controls how community Claude Code plugins, marketplaces, agent packs, and skill packs are evaluated and adopted.

## Position

Use community plugins as a source of patterns first. Direct installation is the exception, not the default.

## Why

Claude Code plugins can affect local files, prompts, commands, agents, tools, shell execution, git workflows, and sometimes deployment paths. A plugin that saves a few minutes can also create supply-chain risk or make the workflow impossible to reproduce later.

## Adoption levels

| Level | Meaning | Allowed by default |
| --- | --- | --- |
| Reference | Read and extract ideas only | Yes |
| Adapt | Copy selected docs/prompts/commands locally | Yes, after review |
| Pilot | Test in scratch branch or disposable repo | Yes, with guardrails |
| Install | Install plugin into a real project | Explicit approval only |
| Trust | Allow plugin to run privileged workflows | Explicit approval only |

## Evaluation checklist

Before adoption, confirm:

- The source repository is visible and inspectable.
- The plugin has a clear manifest.
- Commands, agents, skills, and scripts are understandable.
- There are no hidden install scripts or shell profile changes.
- There is no automatic deploy, push, or credential access.
- The plugin does not duplicate existing project rules.
- The plugin can be removed cleanly.
- The value is greater than the token/context cost.

## Project fit checklist

For each project, check:

- Does this match the current stack?
- Does it respect existing architecture?
- Does it use the project's test tools?
- Does it preserve the current CI/CD flow?
- Does it avoid production-impacting actions?
- Does it produce smaller, safer changes?

## Security guardrails

Never allow an unreviewed plugin to:

- read secrets, private keys, tokens, certs, or credential stores
- write shell startup files
- modify git remotes or credentials
- push to remote repositories
- deploy to production
- create broad network-facing services
- install opaque binaries
- change MCP/tool permissions silently

## Recommended workflow

1. Run an evaluation.
2. Decide `REJECT`, `ADAPT`, `PILOT`, or `INSTALL`.
3. If useful, adapt only the smallest local subset.
4. Pilot on a reversible task.
5. Promote only after the result is measurable and reproducible.

## Current marketplace view

For broad community plugin marketplaces, start with low-risk workflow value:

- docs loading
- quality/testing
- security review
- lifecycle planning

Do not start with large full-stack bundles, payment/auth integrations, model routing, or deployment automation unless the project explicitly needs them.
