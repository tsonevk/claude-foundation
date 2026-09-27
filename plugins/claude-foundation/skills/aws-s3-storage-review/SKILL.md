---
name: aws-s3-storage-review
description: "Review AWS S3 bucket policy, public access, encryption, lifecycle, replication, and logging settings."
disable-model-invocation: true
---

# AWS S3 Storage Review

## Purpose
- Review AWS S3 bucket policy, public access, encryption, lifecycle, replication, and logging settings.

## When to use
- The task is about S3 access, exposure, retention, or data protection.
- You need a bounded storage review before any remediation.

## When not to use
- The task asks for destructive cleanup without approval.
- A broader AWS networking or IAM review already covers the issue.

## Read first
- S3 bucket policy, public access block, and encryption state.
- Lifecycle, replication, and logging settings.
- AWS CLI help for the specific read-only commands.

## Operating rules
- Inspect before changing.
- Prefer read-only evidence first.
- State assumptions clearly.
- Separate evidence from inference.
- Keep recommendations small and reversible.

## Required inputs
- Account, region, and profile scope.
- Bucket names or ARNs when available.
- The access, protection, or retention question.

## Codex workflow
1. Read bucket state and evidence first.
2. Check public access, policy, encryption, and logging settings.
3. Compare observed state to the expected protection level.
4. Identify the smallest safe corrective path.
5. Report the risk and any rollback concern.

## Expected output
- A concise S3 storage review.
- The bucket state and controls inspected.
- The exposure or protection gaps found.

## Output contract
- Name the bucket scope reviewed.
- Separate evidence from inference.
- Keep any proposed changes minimal and defensive.

## Validation guidance
- Use targeted `aws s3api ...` commands only.
- Confirm the bucket settings before concluding.
- If files changed, run the repo's own lint/tests if present; otherwise state that no validator is available.

## Rollback guidance
- Prefer reversible control changes over deletes.
- If retention or replication is involved, document the restore path first.

## Verification
- The bucket settings match the cited issue.
- The answer distinguishes confirmed risk from estimate.

## Safety boundaries
- Read-only first.
- No destructive AWS commands without explicit approval.
- No secret, token, or key output.
- Respect account, region, and profile scope.

## Related skills
- `aws-operations-review`
- `aws-iam-policy-review`
- `aws-networking-review`
- `auditing-aws-s3-bucket-permissions`

## Source attribution
- No exact upstream match.
- Closest local defensive context: `auditing-aws-s3-bucket-permissions` and `analyzing-cloud-storage-access-patterns`.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- For AWS diagnostics, default to read-only evidence collection and deterministic reporting.
- Do not promise hidden async work or detached execution.
- No open-ended shell access.
- No secrets handling beyond detection and redaction guidance.