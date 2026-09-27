---
name: eight-rule-architecture
description: Apply the reusable 8-rule working architecture for non-trivial repo tasks, with caution, surgical edits, read-before-write, checkpoints, context discipline, and loud failure reporting.
disable-model-invocation: true
---

# Eight-Rule Working Architecture

## Purpose

Provide a compact reusable operating contract for non-trivial repo work.

Use this skill to keep repo changes cautious, small, verifiable, and easy to hand off.

## When to use

- A task requires code, config, docs, repo, or workflow changes.
- A task spans multiple files or has meaningful risk.
- You need disciplined checkpointing for a growing session.
- The current repo work would benefit from an explicit read-before-write loop.

## When not to use

- The task is a trivial one-line answer with no repo changes.
- A closer project `AGENTS.md` provides a stricter task-specific workflow.
- The user explicitly asks for fast exploratory brainstorming without implementation.

## Required inputs

- The nearest applicable `CLAUDE.md` / `AGENTS.md`
- The repo path or task summary
- The files likely to change
- Any relevant tests, configs, or docs already named by the user

## The 8 rules

### 1. Think before editing

State the goal and assumptions before changing files.

If the existing structure is unclear, stop and surface the uncertainty.

Push back when a simpler safe approach exists.

### 2. Simplicity first

Implement the minimum safe change that solves the task.

Do not add speculative features.

Do not create abstractions for one-off code.

### 3. Surgical changes

Touch only files required for the task.

Do not reformat, rename, or clean up adjacent code unless the task requires it.

Match existing style and naming.

### 4. Goal-driven execution

Define success criteria before editing.

Iterate toward verified success rather than blindly following a checklist.

### 5. Context budgets are real

Keep reads narrow and task-focused.

Do not re-read the whole repo when a few authoritative files are enough.

If context grows too large, create or update compact handoff notes and continue from them.

### 6. Read before write

Before code changes, inspect the relevant:

- exports or interfaces
- immediate callers
- shared utilities
- config
- tests
- project docs and instructions

Do not invent filesystem layouts, commands, or conventions.

### 7. Checkpoint after significant steps

After each significant step, summarize:

- what changed
- what is verified
- what remains
- the next safe step

For large repo work, update these files when present:

- `docs/activeContext.md`
- `docs/currentTask.md`
- `docs/decision-log.md`

### 8. Fail loud

Do not say `completed` if anything was skipped silently.

Do not say `tests pass` if any relevant test was skipped.

Separate verified facts from assumptions and residual risk.

## Workflow

1. Read the closest applicable `CLAUDE.md` / `AGENTS.md` first.
2. Read only task-relevant docs and files.
3. Define success criteria and likely files to change.
4. Make the smallest safe edit.
5. Run the narrowest meaningful verification.
6. Check for unintended file changes.
7. Report facts, skipped checks, risks, and next safe step.

## Output contract

For repo work, final output must include:

- summary
- files changed
- verification run
- skipped checks, if any
- risks or uncertainty
- next safe step, if relevant

## Verification

A correct use of this skill should show:

- no unrelated files changed
- at least one relevant check run, or an explicit reason why no check could run
- no hidden skipped work
- a clear difference between facts and assumptions

## Safety boundaries

- Do not use this skill to override project-specific authority.
- Do not broaden runtime, network, filesystem, or deployment authority unless explicitly requested and verified.
- Do not perform destructive operations without explicit approval.
- Do not hide failed or unavailable checks.

## Related skills

- `strategic-compact`
- `search-first`
- `verification-loop`
- `manual-compact-handoff`
- `skill-bank-router`

## Source attribution

Adapted from the reusable 8-rule working architecture pattern.

## Local policy overrides

- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- For iMX work, use iMX-native ksh and Oracle context; whole-instance stop requires explicit reconfirmation.
- For OCI diagnostics, default to read-only evidence collection and deterministic reporting.
- Do not promise hidden async work or detached execution.
