---
name: ansible-secrets-hygiene
description: "Review Ansible Vault, secret vars, no_log usage, logs, artifacts, and credential handling safely."
disable-model-invocation: true
---

# Ansible Secrets Hygiene

## Purpose
- Review Ansible Vault, secret vars, no_log usage, logs, artifacts, and credential handling safely.

## When to use
- The task is about secrets in Ansible variables, Vault, or logs.
- You need to confirm secrets are not exposed in output, artifacts, or templates.

## When not to use
- The issue is only playbook syntax or host targeting.
- A generic secret-scan task is enough and Ansible is not involved.

## Read first
- Vault usage, variable files, and task output settings.
- Any logs, artifacts, or CI output that may contain credentials.
- Existing secret-handling conventions in the repo.

## Operating rules
- Inspect before changing.
- Prefer read-only review first.
- State assumptions.
- Separate evidence from inference.
- Keep secret handling scoped and redacted.

## Required inputs
- Playbook or role path.
- The secret source or output path.
- Any existing redaction or rotation expectations.

## Codex workflow
1. Read the secret sources and output paths first.
2. Check Vault, `no_log`, and template exposure risk.
3. Inspect logs and artifacts for credential leakage.
4. Identify the smallest safe remediation or hardening step.
5. Report facts and redaction needs only.

## Expected output
- A concise Ansible secrets review.
- The secret-bearing files or outputs inspected.
- Any exposure or handling gaps.

## Output contract
- Name the Ansible scope reviewed.
- Separate evidence from inference.
- Do not print secret material or credentials.

## Validation guidance
- Confirm secret paths and output controls before concluding.
- Use read-only checks only.
- If files changed, run the repo's own lint/tests if present; otherwise state that no validator is available.

## Rollback guidance
- No mutation by default, so rollback is usually not needed.
- If a change is proposed, keep the prior secret-handling pattern available.

## Verification
- The evidence supports the exposure or protection finding.
- The answer omits secret content and distinguishes fact from inference.

## Safety boundaries
- Read-only first.
- No secret, token, private key, certificate, or Vault password output.
- No production-impacting execution without explicit confirmation.
- Preserve least privilege and redaction.

## Related skills
- `ansible-playbook-review`
- `ansible-role-review`
- `ansible-ci-validation`
- `iac-secrets-hygiene`

## Source attribution
- No exact upstream match.
- Closest local defensive context: `security-scan`.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- For RHEL/Oracle Linux Ansible work, avoid assumptions that break package or service conventions.
- Do not promise hidden async work or detached execution.
- No open-ended shell access.
- No secrets handling beyond detection and redaction guidance.