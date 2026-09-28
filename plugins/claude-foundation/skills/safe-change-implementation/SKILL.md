---
name: safe-change-implementation
description: Use when the user asks for a minimal-risk code or configuration change that should preserve existing behavior as much as possible. Do not use when a full redesign is explicitly requested.
disable-model-invocation: true
---

Implement the smallest correct change with clear validation and rollback.

## Goals
- Minimize unintended behavior changes.
- Keep diffs easy to review.
- Preserve current behavior unless a change in behavior is explicitly requested.

## When to use
- The user asks for a small fix.
- The repository is sensitive, legacy, or operational.
- The request says "small changes", "safe", "minimal", "do not break current flow", or equivalent.

## Do not use when
- The user explicitly wants a redesign, refactor, or architecture overhaul.
- The current structure is unusable and a larger rewrite is clearly required.

## Steps
1. Inspect the current structure before editing.
2. Identify the smallest file set that can solve the problem.
3. Preserve current interfaces, filenames, and defaults where possible.
4. Prefer config-based extension over hardcoded changes.
5. Add or adjust only the smallest relevant validation.
6. Report:
   - what changed
   - what was deliberately not changed
   - what still remains unverified

## Output format
Always include:
- target files
- exact changes
- validation commands
- rollback approach
- open risks or assumptions

## Quality bar
- Favor minimal patch size.
- Avoid opportunistic unrelated cleanup unless it blocks the change.
- If a larger redesign is objectively better, mention it separately but still deliver the safe option first.
