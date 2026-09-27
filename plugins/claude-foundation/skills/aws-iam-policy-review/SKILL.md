---
name: aws-iam-policy-review
description: Review AWS IAM roles, policies, users, and trust relationships for least privilege and safe scope.
disable-model-invocation: true
---

# AWS IAM Policy Review

## Workflow
1. Confirm account/profile scope and read exported policy/trust evidence.
2. Map principals, actions, resources, conditions, trust, and permission boundaries.
3. Identify overbroad grants or missing constraints.
4. Separate current grants from inferred intent.
5. Recommend the smallest least-privilege adjustment; use read-only AWS queries for validation.

## Output contract
- IAM scope reviewed
- Evidence and findings
- Least-privilege gap or confirmation
- Validation
- Safe next step

## Safety boundaries
- Read-only first.
- No IAM mutation without explicit approval.
- No secret/token/key output.
