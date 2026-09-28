---
name: ansible-idempotency-safety
description: "Review Ansible idempotency, changed_when, failed_when, check_mode, handlers, and repeatability."
disable-model-invocation: true
---

# Ansible Idempotency Safety

## Purpose
- Review Ansible idempotency, changed_when, failed_when, check_mode, handlers, and repeatability.

## When to use
- The task is about whether a playbook or role is safe to rerun.
- You need to verify change reporting, handler triggers, or check-mode behavior.

## When not to use
- The issue is only inventory selection or role layout.
- A broader playbook review already covers the same behavior.

## Read first
- The tasks, handlers, and any custom conditions.
- Existing check-mode or dry-run notes.
- Any test output or prior run logs.

## Operating rules
- Inspect before changing.
- Prefer read-only review first.
- State assumptions.
- Separate evidence from inference.
- Focus on repeatability and correct change reporting.

## Required inputs
- Playbook or role path.
- The behavior that should be idempotent.
- Any observed non-idempotent run results.

## Codex workflow
1. Read the task flow and handler conditions first.
2. Check `changed_when`, `failed_when`, and `check_mode` usage.
3. Identify repeatability risks and handler misfires.
4. Compare behavior to the intended rerun outcome.
5. Report the smallest safe fix path.

## Expected output
- A concise idempotency review.
- The tasks or handlers inspected.
- Any repeatability or reporting gaps.

## Output contract
- Name the playbook or role scope reviewed.
- Separate evidence from inference.
- Avoid claiming idempotency without repeat-run evidence.

## Validation guidance
- Use read-only rerun or check-mode checks when appropriate.
- Confirm the reported change behavior with evidence.
- If files changed, run the repo's own lint/tests if present; otherwise state that no validator is available.

## Rollback guidance
- No mutation by default, so rollback is usually not needed.
- If a change is proposed, preserve the previous handler and condition logic.

## Verification
- The rerun or check-mode behavior matches the cited result.
- The answer distinguishes confirmed behavior from inference.

## Safety boundaries
- Read-only first.
- No production-impacting execution without explicit confirmation.
- No secret output.
- Respect handler side effects and repeatability scope.

## Related skills
- `ansible-playbook-review`
- `ansible-role-review`
- `ansible-inventory-review`
- `ansible-ci-validation`
- `ansible-idempotent-change-check` — verifies current state before editing to avoid no-op/duplicate changes; this skill reviews idempotency constructs in playbooks/roles.

## Source attribution
- No exact upstream match.
- Closest local defensive context: `verification-loop`.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- For RHEL/Oracle Linux Ansible work, avoid assumptions that break package or service conventions.
- Do not promise hidden async work or detached execution.
- No open-ended shell access.
- No secrets handling beyond detection and redaction guidance.