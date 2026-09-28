---
name: search-first
description: Check authoritative repo docs and source files before guessing or improvising; stop as soon as the task has enough grounded context.
---

# Search First

## Purpose
Use targeted evidence before implementation or advice when the source of truth is not already known.

## When to use
- The task touches an unfamiliar repo/module.
- The authoritative file or runtime path is unclear.
- The answer needs repository evidence rather than inference.

## When not to use
- The authoritative target is already known and loaded.
- The task is a trivial scoped edit.
- The user explicitly asks not to search.

## Workflow
1. Read the closest project `CLAUDE.md` / `AGENTS.md`; read `README.md` only when it adds needed context.
2. Reuse existing compact task/context files when present.
3. Find the runtime/config source of truth with targeted search.
4. Read only nearby tests/templates/configs that can affect the requested change.
5. Stop searching as soon as evidence is sufficient.
6. Separate observed facts from inference.

Do not perform a generic repository preflight when the target and required behavior are already explicit.
Do not create context files as part of search.

## Output contract
- Evidence-backed summary
- Authoritative files used
- Remaining unknowns that matter
- Next safe step

## Safety boundaries
- Do not replace evidence with intuition.
- Do not use stale notes over current runtime/source files.
- Do not expand into broad repository scans without evidence that they are needed.
