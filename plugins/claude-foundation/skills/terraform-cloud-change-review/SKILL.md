---
name: terraform-cloud-change-review
description: "Review Terraform cloud changes for destructive actions, drift, and rollback safety before apply."
disable-model-invocation: true
---

# Terraform Cloud Change Review

## Purpose
- Review Terraform cloud changes for destructive actions, drift, and rollback safety before apply.

## When to use
- The task is a Terraform plan, diff, or proposed cloud change review.
- You need to assess risk before approving an apply.

## When not to use
- The task is a live apply without a prior plan.
- A narrower provider-specific skill already covers the exact change set.

## Read first
- Terraform configuration, plan output, and any state notes.
- Existing drift, maintenance, or rollback documentation.
- Provider docs for the affected resources when needed.

## Operating rules
- Inspect before changing.
- Prefer read-only evidence first.
- State assumptions clearly.
- Separate evidence from inference.
- Keep review focused on the smallest plan slice.

## Required inputs
- Terraform plan or equivalent diff.
- Target workspace, environment, and cloud scope.
- Any existing rollback or maintenance constraints.

## Codex workflow
1. Read the plan and config first.
2. Identify destructive, replacement, or drift-related actions.
3. Map the change to the minimum impacted cloud scope.
4. Check rollback feasibility and blast radius.
5. Report the safe approve, amend, or stop decision.

## Expected output
- A concise plan review with risk notes.
- The destructive or drift-sensitive actions found.
- A minimal safe recommendation.

## Output contract
- Name the plan, workspace, or scope reviewed.
- Separate evidence from inference.
- Include rollback considerations for risky changes.

## Validation guidance
- Review the plan before any apply.
- Compare the plan to the intended change and rollback path.
- If files changed, run the repo's own lint/tests if present; otherwise state that no validator is available.

## Rollback guidance
- Prefer a prior plan, state backup, or provider rollback path.
- If rollback is unclear, flag the change as higher risk.

## Verification
- The plan or diff matches the reported cloud scope.
- The answer identifies destructive or replacement actions clearly.

## Safety boundaries
- Read-only first.
- No destructive cloud commands without explicit approval.
- No secret output.
- Respect account, region, and workspace scope.

## Related skills
- `cloud-cost-risk-review`
- `oci-operations-review`
- `aws-operations-review`
- `security-review`

## Source attribution
- No exact upstream match.
- Closest local defensive context: `auditing-terraform-infrastructure-for-security`.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- For cloud changes, inspect plan before apply.
- Do not promise hidden async work or detached execution.
- No open-ended shell access.
- No secrets handling beyond detection and redaction guidance.