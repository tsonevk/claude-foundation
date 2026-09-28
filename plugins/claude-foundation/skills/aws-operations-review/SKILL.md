---
name: aws-operations-review
description: Review AWS account and resource layout with a read-first operations lens.
disable-model-invocation: true
---

# AWS Operations Review

## Workflow
1. Confirm account, region, profile, and resource scope.
2. Read authoritative inventory/incident evidence.
3. Collect only the smallest needed read-only AWS state.
4. Compare observed state with the question or expected layout.
5. Report verified facts, unknowns, and the next safe diagnostic step.

## Safety boundaries
- Read-only first.
- No destructive or mutating AWS command without explicit approval.
- No secret/token/key output.
