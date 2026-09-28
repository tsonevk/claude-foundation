---
name: oci-operations-review
description: Review OCI resource layout, tenancy scope, compartments, and regions with a read-first operations lens.
---

# OCI Operations Review

## Workflow
1. Confirm the operational question plus region/compartment/resource scope.
2. Read existing inventory/evidence first and collect only necessary read-only OCI state.
3. Separate current observed state from intended design or stale notes.
4. Identify the smallest operational gap or follow-up domain review.
5. Report evidence, unknowns, and the next safe action.

## Output contract
- OCI scope
- Evidence
- Findings
- Unknowns
- Next safe action

## Safety boundaries
- Read-only first.
- No OCI mutation, IAM change, or credential access without explicit approval.
