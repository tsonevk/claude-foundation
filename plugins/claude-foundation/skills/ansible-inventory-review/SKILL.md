---
name: ansible-inventory-review
description: "Review Ansible inventory, group_vars, host_vars, environment separation, and host targeting."
disable-model-invocation: true
---

# Ansible Inventory Review

## Purpose
- Review Ansible inventory, group_vars, host_vars, environment separation, and host targeting.

## When to use
- The task is about host selection, inventory layout, or variable scoping.
- You need to verify environment boundaries before execution.

## When not to use
- The issue is primarily playbook task flow or role structure.
- A narrower playbook or role review is enough.

## Read first
- Inventory files and any `group_vars` or `host_vars`.
- Environment-specific inventory overlays.
- Host targeting notes or execution commands.

## Operating rules
- Inspect before changing.
- Prefer read-only review first.
- State assumptions.
- Separate evidence from inference.
- Keep scope to the smallest inventory slice.

## Required inputs
- Inventory path or repository path.
- Target environment or host group.
- The question about targeting, separation, or variable scope.

## Codex workflow
1. Read inventory and variable sources first.
2. Trace host, group, and environment boundaries.
3. Check `group_vars` and `host_vars` precedence.
4. Identify the smallest likely mismatch or risk.
5. Report facts and any remaining ambiguity.

## Expected output
- A concise inventory review.
- The host, group, and variable sources inspected.
- Any targeting or separation gaps.

## Output contract
- Name the inventory scope reviewed.
- Separate evidence from inference.
- Keep recommendations minimal and operational.

## Validation guidance
- Confirm the inventory files and variable directories exist.
- Use a read-only `ansible-inventory` check if helpful.
- If files changed, run the repo's own lint/tests if present; otherwise state that no validator is available.

## Rollback guidance
- No mutation by default, so rollback is usually not needed.
- If a change is proposed, keep the previous inventory layout available.

## Verification
- The host targeting and variable scope match the reported environment.
- The answer distinguishes confirmed behavior from inference.

## Safety boundaries
- Read-only first.
- No production-impacting execution without explicit confirmation.
- No secret output.
- Respect environment separation and host scope.

## Related skills
- `ansible-playbook-review`
- `ansible-role-review`
- `ansible-idempotency-safety`
- `ansible-secrets-hygiene`

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