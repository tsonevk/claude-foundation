---
name: oci-iam-policy-review
description: "Review OCI IAM policies, dynamic groups, and compartment scope for least-privilege and operational safety."
disable-model-invocation: true
---

# OCI IAM Policy Review

## Purpose
- Review OCI IAM policies, dynamic groups, and compartment scope for least-privilege and operational safety.

## When to use
- The question is about OCI access control or permission scope.
- You need a bounded IAM review before any policy change.

## When not to use
- The task is a live policy rollout without confirmation.
- A broader OCI ops review is enough and IAM is not the main issue.

## Read first
- OCI IAM policy docs and any existing policy exports.
- Dynamic group definitions and compartment layout.
- OCI CLI help for read-only IAM queries.

## Operating rules
- Inspect before changing.
- Prefer read-only evidence first.
- State assumptions clearly.
- Separate evidence from inference.
- Keep scope to the minimum policy or compartment slice.

## Required inputs
- Tenancy, compartment, and region scope.
- Policy text or exported IAM state when available.
- The access question or least-privilege concern.

## Codex workflow
1. Read the IAM evidence first.
2. Map principals, compartments, and allowed actions.
3. Identify overbroad grants or missing boundaries.
4. Compare policy intent to observed scope.
5. Report the smallest safe adjustment path.

## Expected output
- A concise IAM review summary.
- The policies, groups, or compartments inspected.
- The least-privilege gaps or confirmations.

## Output contract
- Name the IAM scope reviewed.
- Separate evidence from inference.
- Keep recommendations minimal and defensive.

## Validation guidance
- Use targeted `oci iam ... get|list` commands only.
- Verify the policy text or exports before concluding.
- If files changed, run the repo's own lint/tests if present; otherwise state that no validator is available.

## Rollback guidance
- No mutation by default, so no rollback is expected.
- If a policy change is proposed, keep the previous policy text available.

## Verification
- The relevant IAM objects exist and match the scope.
- The answer distinguishes current grants from inferred intent.

## Safety boundaries
- Read-only first.
- No destructive IAM commands without explicit approval.
- No secret output.
- Respect tenancy, compartment, and region scope.

## Related skills
- `oci-operations-review`
- `oci-networking-diagnostics`
- `oci-vault-key-rotation-review`
- `oci-evidence-collector`

## Source attribution
- No exact upstream match.
- Closest local defensive context: `oci-security-evidence-review`.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- For OCI diagnostics, default to read-only evidence collection and deterministic reporting.
- Do not promise hidden async work or detached execution.
- No open-ended shell access.
- No secrets handling beyond detection and redaction guidance.