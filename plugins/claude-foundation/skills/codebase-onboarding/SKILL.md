---
name: codebase-onboarding
description: Guide a minimal first-pass repository onboarding and context scan without broad, unnecessary reading.
---

# Codebase Onboarding

## Purpose
Understand an unfamiliar repository quickly with the smallest useful map of authority, structure, risks, and validation entrypoints.

## When to use
- First contact with a repository.
- The task needs orientation before implementation.
- The user asks for a practical repository overview.

## When not to use
- The repository is already familiar.
- The task is a clear local edit.
- Deep architecture analysis is explicitly requested instead.

## Workflow
1. Confirm the repo root.
2. Read the closest `CLAUDE.md` / `AGENTS.md` first.
3. Read `README.md` only as needed.
4. Reuse `docs/activeContext.md`, `docs/currentTask.md`, and `docs/decision-log.md` when they exist.
5. Inspect package/build/test metadata only enough to find validation entrypoints.
6. Target only files relevant to the user's task.
7. Stop when the repository map is sufficient.

Do not create handoff files as part of onboarding unless project policy or the user explicitly asks for persistent state.

## Output contract
- Repository purpose
- Key directories/surfaces
- Source-of-truth files
- High-risk/must-not-touch areas
- Validation entrypoints
- Open questions that matter
- Next files to inspect for the actual task

## Safety boundaries
- Read-only during onboarding.
- No broad repository dump or Repomix by default.
- Project authority wins over generic guidance.
