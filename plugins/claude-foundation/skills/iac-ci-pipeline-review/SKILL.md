---
name: iac-ci-pipeline-review
description: "Review GitLab or Jenkins IaC validation pipelines, artifacts, plan retention, approvals, and protected variables."
disable-model-invocation: true
---

# IaC CI Pipeline Review

## Purpose
- Review GitLab or Jenkins IaC validation pipelines, artifacts, plan retention, approvals, and protected variables.

## When to use
- The task is about CI gates for Terraform or Ansible infrastructure changes.
- You need to review validation, approval, or artifact handling before rollout.

## When not to use
- The issue is only local syntax or module structure.
- A narrower tool-specific CI review is already sufficient.

## Read first
- CI config, job definitions, and artifact retention rules.
- Any plan publication, approval, or protected variable settings.
- The Terraform or Ansible files the pipeline validates.

## Operating rules
- Inspect before changing.
- Prefer read-only review first.
- State assumptions.
- Separate evidence from inference.
- Keep CI validation minimal and reproducible.

## Required inputs
- CI platform and pipeline files.
- The IaC content being validated.
- Any approval, artifact, or retention constraints.

## Codex workflow
1. Read the CI jobs and IaC inputs first.
2. Check validation, approval, and artifact handling.
3. Verify protected variables and secret boundaries.
4. Identify missing gates or risky retention behavior.
5. Report the smallest safe improvement.

## Expected output
- A concise IaC pipeline review.
- The jobs, artifacts, and protections inspected.
- Any missing gates or exposure risks.

## Output contract
- Name the CI and IaC scope reviewed.
- Separate evidence from inference.
- Keep recommendations minimal and defensive.

## Validation guidance
- Confirm the CI files and artifact settings before concluding.
- Prefer read-only validation checks when possible.
- If files changed, run the repo's own lint/tests if present; otherwise state that no validator is available.

## Rollback guidance
- Preserve the prior job, approval, or artifact settings.
- If a change is proposed, keep a rollback path for the pipeline config.

## Verification
- The CI controls match the cited IaC scope.
- The answer distinguishes confirmed behavior from inference.

## Safety boundaries
- Read-only first.
- No production-impacting execution without explicit confirmation.
- No secret output.
- Prefer Linux/GitLab runner compatibility.

## Related skills
- `ansible-ci-validation`
- `terraform-plan-safety-review`
- `terraform-state-backend-review`
- `iac-secrets-hygiene`

## Source attribution
- No exact upstream match.
- Closest local defensive context: `building-devsecops-pipeline-with-gitlab-ci` and `verification-loop`.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- Do not promise hidden async work or detached execution.
- No open-ended shell access.
- No secrets handling beyond detection and redaction guidance.