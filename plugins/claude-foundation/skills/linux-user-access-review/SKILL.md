---
name: linux-user-access-review
description: Review Linux users, groups, sudo, SSH, permissions, and least privilege safely.
disable-model-invocation: true
---

# Linux User and Access Review

## Purpose
- Review Linux users, groups, sudo, SSH, permissions, and least privilege safely.

## When to use
- The task reviews users, groups, sudoers, or SSH access.
- You need to inspect ownership, permissions, umask, or service users.
- The issue is locked, expired, or denied access on a Linux host.
- A safe access change needs a read-first review.

## When not to use
- The task asks to expose private keys or passwords.
- The task requests broad privilege escalation without justification.
- The issue is IAM or cloud identity only.
- The request is not about Linux host access.

## Read first
- `AGENTS.md`
- `README.md`
- The target host, user, or access scope
- Any ownership, sudo, or SSH evidence already available

## Operating rules
- Inspect before changing.
- Prefer read-only access review first.
- Keep the user, group, host, and file scope explicit.
- Separate confirmed access state from assumed intent.
- Do not expose secrets or sensitive auth material.

## Required inputs
- Target user, host, or group
- The access or permission question
- Any approval or maintenance constraint

## Codex workflow
1. Read the access scope and current state first.
2. Inspect users, groups, sudoers, SSH, and permissions evidence.
3. Check whether ownership or umask is part of the issue.
4. Identify the smallest safe access change or follow-up.
5. Report the access risk and next step clearly.

## Expected output
- A concise access review.
- The users, groups, sudo, or SSH evidence reviewed.
- Any least-privilege concern or safe next step.

## Output contract
- State whether the access state is acceptable, constrained, or risky.
- List the exact access evidence used.
- Separate evidence from inference.

## Validation guidance
- Confirm the target user, host, and permission scope are explicit.
- Confirm any access change is bounded and reversible.
- If files changed, run the repo's own lint/tests if present; otherwise state that no validator is available.

## Rollback guidance
- Preserve the prior sudo, SSH, ownership, or permission state.
- Revert the smallest access change if it breaks the workflow.

## Verification
- The answer names the access evidence reviewed.
- The answer identifies whether a safer least-privilege path exists.

## Safety boundaries
- No secret exposure.
- No broad privilege escalation without justification.
- No production-impacting access mutation by default.

## Related skills
- `linux-system-diagnostics-review`
- `linux-service-systemd-review`
- `linux-selinux-firewall-review`
- `ansible-linux-ops-guardrails`

## Source attribution
- Adapted from local Linux access review patterns and least-privilege guidance.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- Before large tasks, create or update `docs/activeContext.md`, `docs/currentTask.md`, and `docs/decision-log.md`.
- For repo work, obey `AGENTS.md` first.
- Prefer read-only evidence commands before any fix.
- Do not promise hidden async work or detached execution.
- No secrets handling beyond detection and redaction guidance.
- No self-remediation outside an explicit, scoped approval.