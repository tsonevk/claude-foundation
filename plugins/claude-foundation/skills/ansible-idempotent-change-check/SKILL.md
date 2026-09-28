---
name: ansible-idempotent-change-check
description: Verify current Ansible state before editing or reinstalling. Use when working on roles, playbooks, inventories, group vars, handlers, or package/service tasks and you need to confirm whether the requested change is already present before making a diff.
disable-model-invocation: true
---

# Ansible Idempotent Change Check

## Overview

Inspect first, change only when drift exists, and keep the result idempotent. Use this skill to avoid rewriting files, reinstalling packages, or reapplying handlers when the repository or target host already matches the requested state.

## Workflow

1. Identify the exact target state.
2. Inspect the current repo or host state first.
3. Compare current state to target state.
4. If the requested state is already present, stop and report that no change is needed.
5. If drift exists, make the smallest safe additive change.
6. Validate only the touched Ansible surface.
7. Document rollback only for the new delta.

## Change Rules

- Do not reinstall packages, restart services, or rewrite files if the desired state is already present.
- Prefer inventory, task, and variable inspection before editing role logic.
- Preserve existing behavior unless the user explicitly asks for a change.
- Keep edits minimal and reversible.
- If validation shows the target state already exists, say so and stop.

## Validation

- Run the smallest relevant Ansible or lint check after a real change.
- Report what was already correct, what was changed, and what remains unverified.
- Include rollback notes only for the files or tasks that actually changed.

## Related skills
- `ansible-idempotency-safety` — reviews idempotency constructs (changed_when, failed_when, check_mode, handlers) in playbooks/roles; this skill verifies current state before editing to avoid no-op or duplicate changes.
