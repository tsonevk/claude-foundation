---
name: linux-package-patching-review
description: Review dnf, yum, rpm, repos, patch windows, and reboot risk safely.
disable-model-invocation: true
---

# Linux Package and Patching Review

## Purpose
- Review package, repository, kernel, subscription, and reboot-risk workflows safely.

## When to use
- The task reviews `dnf`, `yum`, `rpm`, repository, or package-lock behavior.
- You need to assess kernel update or patch-window risk.
- RHEL subscription or Oracle Linux ULN/public-yum context matters.
- You need a safe update history or rollback review before patching.

## When not to use
- The task is application dependency management only.
- The task is Ansible patching and `ansible-linux-ops-guardrails` is primary.
- The task asks to run upgrade immediately without scope and approval.
- The task needs broad OS mutation beyond a read-first review.

## Read first
- `AGENTS.md`
- `README.md`
- Repo, host, or runbook notes for package policy
- Any update history, repo config, or maintenance window details

## Operating rules
- Inspect before changing.
- Prefer read-only package and repo review first.
- Separate installed-state evidence from proposed update behavior.
- Treat kernel and reboot impact as first-class risk.
- Do not expose secrets or repo credentials.

## Required inputs
- Target host or environment
- Package, repo, or patching objective
- Approval and reboot constraints

## Codex workflow
1. Read package and repo metadata first.
2. Check installed packages, repos, and locks.
3. Review kernel, subscription, and reboot risk.
4. Identify a safe patch window or rollback need.
5. Report the smallest safe next step.

## Expected output
- A concise patching review.
- The package, repo, or kernel evidence reviewed.
- Any reboot or rollback concern.

## Output contract
- State whether patching is low risk, risky, or blocked.
- List the exact package or repo evidence used.
- Separate evidence from inference.

## Validation guidance
- Confirm the package manager, repository, and OS family match the evidence.
- Confirm the reboot impact is explicit.
- If files changed, run the repo's own lint/tests if present; otherwise state that no validator is available.

## Rollback guidance
- Preserve the prior repo config or package state before changes.
- Keep rollback steps explicit if a patch is proposed.

## Verification
- The answer names the package or repo state reviewed.
- The answer identifies reboot or rollback risk clearly.

## Safety boundaries
- No update/upgrade execution without explicit approval.
- No production-impacting package mutation by default.
- No secret disclosure.

## Related skills
- `linux-system-diagnostics-review`
- `linux-service-systemd-review`
- `rhel-oracle-linux-ops-review`
- `ansible-linux-ops-guardrails`

## Source attribution
- Adapted from local host operations review patterns and Linux package safety conventions.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- Before large tasks, create or update `docs/activeContext.md`, `docs/currentTask.md`, and `docs/decision-log.md`.
- For repo work, obey `AGENTS.md` first.
- Prefer read-only evidence commands before any fix.
- Do not promise hidden async work or detached execution.
- No secrets handling beyond detection and redaction guidance.
- No self-remediation outside an explicit, scoped approval.