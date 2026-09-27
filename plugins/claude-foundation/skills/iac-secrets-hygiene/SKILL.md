---
name: iac-secrets-hygiene
description: "Review IaC secrets leakage across Terraform, Ansible, vars, tfvars, state, logs, and CI artifacts."
disable-model-invocation: true
---

# IaC Secrets Hygiene

## Purpose
- Review IaC secrets leakage across Terraform, Ansible, vars, tfvars, state, logs, and CI artifacts.

## When to use
- The task is about secrets exposure in infrastructure code or deployment artifacts.
- You need a broad IaC secret review across tools and pipeline output.

## When not to use
- The issue is only in one tool and a narrower secret skill is enough.
- The task is about runtime application secrets, not IaC materials.

## Read first
- Terraform, Ansible, and variable files in scope.
- State, logs, artifacts, and CI outputs that may contain secrets.
- Existing secret-handling or redaction guidance.

## Operating rules
- Inspect before changing.
- Prefer read-only review first.
- State assumptions.
- Separate evidence from inference.
- Keep all secret handling redacted and scoped.

## Required inputs
- IaC repository path or file set.
- The secret source or output path.
- Any existing redaction or rotation expectations.

## Codex workflow
1. Read the secret-bearing IaC files and outputs first.
2. Check variables, tfvars, state, logs, and artifacts for leakage.
3. Identify the smallest safe hardening step.
4. Note any rotation or remediation requirement separately.
5. Report facts only; do not print secret material.

## Expected output
- A concise IaC secrets review.
- The secret-bearing files or outputs inspected.
- Any exposure or handling gaps.

## Output contract
- Name the IaC scope reviewed.
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
- `ansible-secrets-hygiene`
- `container-secrets-hygiene`
- `ansible-ci-validation`
- `iac-ci-pipeline-review`

## Source attribution
- No exact upstream match.
- Closest local defensive context: `security-scan` and the existing secret-hygiene skills.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- Treat tfstate as sensitive.
- Do not promise hidden async work or detached execution.
- No open-ended shell access.
- No secrets handling beyond detection and redaction guidance.