---
description: Run a controlled pilot plan for a Claude Code plugin idea without trusting the full external plugin.
---

Use this command to test a plugin idea without trusting the full external plugin.

## Pilot rules

1. Use `claude-foundation:claude-plugin-adoption`.
2. Use a scratch branch or disposable test repository.
3. Pin all external source references to a commit SHA.
4. Copy only the minimum docs, commands, or skill content needed for the pilot.
5. Disable or remove:
   - deployment commands
   - credential handling
   - git push automation
   - shell hooks
   - broad MCP/tool configuration
6. Run the pilot on a small, reversible task.
7. Capture results in a short decision note.

## Pilot result template

```md
# Plugin Pilot Result

Plugin:
Source:
Pinned commit:
Date:
Project:

## Goal

## What Was Tested

## What Worked

## What Failed Or Added Noise

## Security Review

## Token/Context Cost

## Decision

Verdict: INSTALL | ADAPT | REJECT

## Next Action
```

## Recommended first pilots

- Documentation loading and source-grounded analysis
- Quality/testing checklists
- Security review prompts
- Project lifecycle planning templates

Avoid piloting payment, auth, deployment, model-routing, or credential-heavy plugins until the low-risk workflow plugins prove useful.
