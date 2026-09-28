---
name: aws-networking-review
description: "Review AWS VPC networking, subnets, route tables, security groups, NACLs, VPN, and Transit Gateway state."
disable-model-invocation: true
---

# AWS Networking Review

## Purpose
- Review AWS VPC networking, subnets, route tables, security groups, NACLs, VPN, and Transit Gateway state.

## When to use
- The problem is about AWS connectivity, exposure, routing, or segmentation.
- You need evidence before suggesting a network change.

## When not to use
- The task is a live network mutation or destructive recovery.
- A narrower AWS S3 or IAM review already covers the issue.

## Read first
- AWS networking docs and CLI help for the specific commands.
- Existing route, security, and attachment evidence.
- Any incident notes or topology diagrams.

## Operating rules
- Inspect before changing.
- Prefer read-only evidence first.
- State assumptions clearly.
- Separate evidence from inference.
- Keep scope to the minimum affected network segment.

## Required inputs
- Account, region, and profile scope.
- VPC, subnet, route table, or address filters when available.
- The observed symptom, path, or exposure question.

## Codex workflow
1. Read topology and evidence first.
2. Trace the smallest relevant network path.
3. Collect read-only route, security, and attachment state.
4. Compare observed state to the intended design.
5. Report the narrowest likely fault domain.

## Expected output
- A concise AWS network diagnosis.
- The state and evidence reviewed.
- The likely fault domain and remaining gaps.

## Output contract
- Name the AWS network scope reviewed.
- Separate evidence from inference.
- Avoid remediation steps that assume mutation.

## Validation guidance
- Use targeted `aws ec2 ... describe` commands only.
- Confirm routes, security, and attachments with current evidence.
- If files changed, run the repo's own lint/tests if present; otherwise state that no validator is available.

## Rollback guidance
- No mutation by default, so no rollback is expected.
- If a fix is proposed, keep a reversible fallback and document it.

## Verification
- The relevant network artifacts exist and match the symptom scope.
- The answer identifies what was confirmed versus inferred.

## Safety boundaries
- Read-only first.
- No destructive AWS network commands without explicit approval.
- No secret output.
- Respect account, region, and profile scope.

## Related skills
- `aws-operations-review`
- `aws-iam-policy-review`
- `aws-s3-storage-review`
- `cloud-cost-risk-review`

## Source attribution
- No exact upstream match.
- Closest local defensive context: `auditing-cloud-with-cis-benchmarks`.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- For AWS diagnostics, default to read-only evidence collection and deterministic reporting.
- Do not promise hidden async work or detached execution.
- No open-ended shell access.
- No secrets handling beyond detection and redaction guidance.