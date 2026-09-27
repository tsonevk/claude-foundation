---
name: cloud-cost-risk-review
description: "Review cloud cost risk from idle, oversized, unattached, or duplicated resources with a read-first lens."
disable-model-invocation: true
---

# Cloud Cost Risk Review

## Purpose
- Review cloud cost risk from idle, oversized, unattached, or duplicated resources with a read-first lens.

## When to use
- The task is about cost exposure or resource efficiency.
- You need a bounded risk review before proposing cleanup.

## When not to use
- The task asks for destructive cleanup without approval.
- A provider-specific operations skill is more appropriate.

## Read first
- Cost, usage, inventory, and tagging evidence.
- Any budget or chargeback notes.
- Existing rollback or retention rules.

## Operating rules
- Inspect before changing.
- Prefer read-only evidence first.
- State assumptions clearly.
- Separate evidence from inference.
- Keep recommendations small and reversible.

## Required inputs
- Cloud account or tenancy scope.
- Resource inventory, billing, or usage evidence when available.
- The cost-risk question or target optimization area.

## Codex workflow
1. Read cost and inventory evidence first.
2. Identify idle, oversized, unattached, or duplicated resources.
3. Estimate risk and likely savings.
4. Check for retention or rollback constraints.
5. Report a minimal safe action list.

## Expected output
- A concise cost-risk summary.
- The likely waste or exposure areas.
- A reversible recommendation set.

## Output contract
- Name the cloud scope reviewed.
- Separate measured evidence from inference.
- Avoid unsupported savings claims.

## Validation guidance
- Use read-only billing or inventory data only.
- Confirm the resources and scope before concluding.
- If files changed, run the repo's own lint/tests if present; otherwise state that no validator is available.

## Rollback guidance
- Prefer delete-free, tag-only, or stop-start-safe recommendations.
- If cleanup is proposed, keep restore steps explicit.

## Verification
- The evidence supports the cited cost-risk issue.
- The answer distinguishes confirmed waste from estimate.

## Safety boundaries
- Read-only first.
- No destructive cleanup without explicit approval.
- No secret output.
- Respect account, region, and project scope.

## Related skills
- `terraform-cloud-change-review`
- `oci-operations-review`
- `aws-operations-review`
- `auditing-cloud-with-cis-benchmarks`

## Source attribution
- No exact upstream match.
- Closest local defensive context: `auditing-cloud-with-cis-benchmarks` and `analyzing-cloud-storage-access-patterns`.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- No destructive cloud commands without explicit approval.
- Do not promise hidden async work or detached execution.
- No open-ended shell access.
- No secrets handling beyond detection and redaction guidance.