---
name: terraform-provider-versioning
description: "Review Terraform provider versions, lock file safety, upgrade safety, and OpenTofu compatibility."
disable-model-invocation: true
---

# Terraform Provider Versioning

## Purpose
- Review Terraform provider versions, lock file safety, upgrade safety, and OpenTofu compatibility.

## When to use
- The task is about provider pinning, upgrades, or lock file changes.
- You need to evaluate compatibility before changing versions.

## When not to use
- The issue is mainly plan safety or state backend behavior.
- Another Terraform review skill already covers the exact risk.

## Read first
- `required_providers`, provider constraints, and lock file state.
- Release notes or compatibility notes for the providers involved.
- Any workspace or OpenTofu compatibility guidance.

## Operating rules
- Inspect before changing.
- Prefer read-only review first.
- State assumptions.
- Separate evidence from inference.
- Keep scope to provider versioning and compatibility only.

## Required inputs
- Terraform root or module path.
- Provider names and current version constraints.
- Any OpenTofu or upgrade constraints.

## Codex workflow
1. Read provider constraints and lock file state first.
2. Compare current and target versions.
3. Check upgrade risk and compatibility expectations.
4. Identify the smallest safe pin or bump.
5. Report facts and the safest next step.

## Expected output
- A concise provider version review.
- The provider constraints and lock file state inspected.
- Any upgrade or compatibility risks.

## Output contract
- Name the provider scope reviewed.
- Separate evidence from inference.
- Avoid claims that ignore lock file behavior.

## Validation guidance
- Confirm provider constraints and lock file state before concluding.
- Use `terraform init -lockfile=readonly` or similar read-only checks when appropriate.
- If files changed, run the repo's own lint/tests if present; otherwise state that no validator is available.

## Rollback guidance
- Preserve the previous lock file and provider constraint state.
- If an upgrade is proposed, keep the downgrade path explicit.

## Verification
- The provider versions and lock file state match the cited scope.
- The answer distinguishes confirmed compatibility from inference.

## Safety boundaries
- Read-only first.
- No destructive cloud commands without explicit approval.
- No secret output.
- Respect provider, module, and workspace scope.

## Related skills
- `terraform-module-review`
- `terraform-state-backend-review`
- `terraform-plan-safety-review`
- `iac-secrets-hygiene`

## Source attribution
- No exact upstream match.
- Closest local defensive context: `auditing-terraform-infrastructure-for-security`.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- For cloud changes, inspect plan before apply.
- Treat tfstate as sensitive.
- Do not promise hidden async work or detached execution.
- No open-ended shell access.
- No secrets handling beyond detection and redaction guidance.