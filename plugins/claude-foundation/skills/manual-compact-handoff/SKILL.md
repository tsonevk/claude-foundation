---
name: manual-compact-handoff
description: Use when a long-running Claude Code repository task needs durable, compact state for a future session without rereading the whole repository.
disable-model-invocation: true
---

# Manual Compact Handoff

## Purpose
Keep substantial work resumable with a small durable state handoff.

## When to use
- A long-running repo task will continue in another session.
- The project already uses compact handoff files.
- The user explicitly asks for persistent project state.

## Workflow
1. Read project authority and existing handoff files first.
2. Reuse existing files when present.
3. Create new handoff files only when project policy expects them, work is genuinely long-running, or the user explicitly requested durable handoff state.
4. Record only current goal, repo state, files changed, decisions, next safe step, risks/blockers, and verification status.
5. Do not scan the whole repository unless the task requires it.

## Safety boundaries
- Do not broaden scope.
- Do not create handoff bureaucracy in every repository.
