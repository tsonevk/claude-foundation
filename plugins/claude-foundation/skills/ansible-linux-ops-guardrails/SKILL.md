---
name: ansible-linux-ops-guardrails
description: "Review Ansible-driven Linux, RHEL, and Oracle Linux package, service, file, cron, user, SELinux, and system operations safely."
disable-model-invocation: true
---

# Ansible Linux Ops Guardrails

## Purpose
- Review Ansible-driven Linux, RHEL, and Oracle Linux package, service, file, cron, user, SELinux, and system operations safely.

## When to use
- The task touches Linux host operations through Ansible.
- You need guardrails for package, service, or SELinux management before running anything.

## When not to use
- The issue is only playbook syntax or inventory targeting.
- A narrower playbook or role review is enough.

## Read first
- The playbook, role, and target host scope.
- Existing host docs or runbooks.
- Any package, service, SELinux, or cron expectations.

## Operating rules
- Inspect before changing.
- Prefer read-only review first.
- State assumptions.
- Separate evidence from inference.
- Keep host scope tight and explicit.

## Required inputs
- Target hosts, inventory, and environment.
- The Linux operation being managed.
- Any maintenance window or rollback note.

## Codex workflow
1. Read the target scope and host expectations first.
2. Check package, service, file, user, cron, and SELinux actions.
3. Verify the playbook is safe for the target distribution.
4. Identify host-impacting steps and recovery needs.
5. Report facts and the smallest safe next step.

## Expected output
- A concise host-ops review.
- The host operations inspected.
- Any safety or rollback gaps.

## Output contract
- Name the host scope reviewed.
- Separate evidence from inference.
- Avoid guidance that assumes destructive execution.

## Validation guidance
- Use read-only checks or syntax checks before any execution.
- Confirm the target distribution and inventory scope.
- If files changed, run the repo's own lint/tests if present; otherwise state that no validator is available.

## Rollback guidance
- Preserve prior package, service, file, or SELinux state notes.
- If a change is proposed, keep the smallest reversible path explicit.

## Verification
- The host operations match the reported distribution and scope.
- The answer distinguishes confirmed behavior from inference.

## Safety boundaries
- Read-only first.
- No production-impacting execution without explicit confirmation.
- No secret output.
- Respect RHEL and Oracle Linux package/service conventions.

## Related skills
- `ansible-playbook-review`
- `ansible-role-review`
- `ansible-inventory-review`
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