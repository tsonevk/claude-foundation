---
name: strategic-compact
description: Compress a complex request into a small actionable Claude Code brief with scope, risks, authoritative context, and verification.
disable-model-invocation: true
---

# Strategic Compact

## Purpose
Turn a broad request into the smallest execution brief that preserves correctness, scope, and verification.

## When to use
- The request is broad, ambiguous, or genuinely multi-step.
- A small execution slice must be defined before implementation.
- The user wants execution rather than brainstorming.

## When not to use
- The task is already a clear scoped edit.
- Project docs already define the exact procedure.
- The user asked for a long-form strategy memo.

## Required inputs
- Goal
- Target repo/system
- Constraints and exclusions
- Authoritative project docs or prior decisions when relevant

## Workflow
1. Read the closest project authority first.
2. Restate the job in one sentence.
3. Name only the files/surfaces likely required.
4. Define the smallest useful change.
5. Define the verification gate and residual risks.

Do not create handoff files merely because the task is large. Reuse them when present; create them only when project policy, long-running work, or an explicit user request justifies durable state.

## Output contract
- One compact brief
- Scope boundary
- Minimal action plan
- Verification gate
- Residual risks

## Safety boundaries
- No unrelated cleanup.
- No invented project policy.
- No hidden assumptions where uncertainty affects correctness.
