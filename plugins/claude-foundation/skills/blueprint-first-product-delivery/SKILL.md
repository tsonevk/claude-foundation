---
name: blueprint-first-product-delivery
description: Deliver a new app, dashboard, API, DevOps tool, MCP or agent gateway, or another major feature slice using a compact blueprint-first model with checked-in blueprint and implementation-plan docs. Use when the job is product-shaped and needs a thin verified vertical slice instead of ad hoc implementation.
disable-model-invocation: true
---

# Blueprint-first Product Delivery

## Purpose

Use a compact, reusable delivery model for product-shaped work without bloating global instructions.

Read these policy docs before drafting or revising the slice plan:

- `docs/product-delivery/product-delivery-policy.md`
- `docs/product-delivery/repo-collaboration-policy.md`

## When to use

- You are starting a new app, dashboard, API, DevOps tool, or internal platform feature.
- You are shaping a new MCP server, MCP gateway, or agent gateway.
- You are implementing a major feature slice that needs product docs before broad coding.
- The project needs a thin verified vertical slice instead of open-ended architecture work.

## When not to use

- The task is already a single obvious code edit.
- The repository already has a tighter project-local product workflow that should win.
- The work is only a bug fix, refactor, or small docs patch with no product-shaping component.

## Required inputs

- Product or slice goal
- Target repository and runtime target
- Authority files to inspect first
- Explicit constraints, exclusions, and trust boundaries

## Codex workflow

1. Read the project's authority files first.
2. Read `docs/product-delivery/product-delivery-policy.md` and `docs/product-delivery/repo-collaboration-policy.md`.
3. Define the smallest useful product slice in one sentence.
4. Create or update `docs/project/BLUEPRINT.md` and `docs/project/IMPLEMENTATION_PLAN.md` when the project needs them.
5. Build the thinnest usable vertical slice that satisfies the current plan.
6. Keep README, API, and operations docs aligned only where the slice actually changes operator behavior.
7. Update project-local handoff or status docs after the slice when the repo uses them.
8. Verify the slice before calling it done.

## Output contract

- A compact product slice brief
- Updated blueprint and implementation-plan docs when applicable
- Minimal implementation changes for the current slice
- Clear verification results
- Residual risks and next safe action

## Verification

- The project goal and current slice can be stated clearly.
- The change surface matches the implementation plan.
- The first usable slice is verified with the smallest relevant checks.
- Durable rules stayed in `AGENTS.md` and live progress stayed in project docs.

## Safety boundaries

- Do not turn `AGENTS.md` into a project plan or progress log.
- Do not invent product requirements that the repo or user did not provide.
- Do not let shared policy docs override project-local authority.
- Do not broaden the slice to speculative architecture or unrelated cleanup.

## Related skills

- `strategic-compact`
- `verification-loop`
- `repo-intake-scan`

## Source attribution

- Adapted from the existing local blueprint-first workflow draft in `~/.agents`.
- Shaped to match the compact instruction and authority model used across the shared Codex skill catalog.

## Local policy overrides

- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey the active project's `AGENTS.md` first.
- Keep shared guidance in `~/.agents` compact and reference-driven.
- Treat `BLUEPRINT.md` and `IMPLEMENTATION_PLAN.md` as project docs, not global policy.
- Do not promise hidden async work or detached execution.
- No secrets handling beyond detection and redaction guidance.
