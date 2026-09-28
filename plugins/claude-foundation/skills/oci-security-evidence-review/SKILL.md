---
name: oci-security-evidence-review
description: Review OCI evidence artifacts, control mappings, and operational logs for security assurance.
---

# OCI Security Evidence Review

## Workflow
1. Define the security/control question and evidence scope.
2. Review existing exported OCI evidence, audit/control artifacts, and operational logs without exposing secrets/private payloads.
3. Verify provenance, timestamp/freshness, scope, and completeness before drawing conclusions.
4. Separate missing evidence from failed controls.
5. Report evidence-backed gaps and the smallest next collection/review step.

## Output contract
- Scope/control question
- Evidence reviewed
- Findings/gaps
- Confidence
- Next safe step

## Safety boundaries
- Read-only.
- No IAM/security/cloud mutation.
- No secret or private log payload exposure.
