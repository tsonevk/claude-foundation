---
name: oci-evidence-collector
description: Use this skill when preparing readonly OCI CLI evidence collection commands or scripts for AI-assisted diagnostics and handoff, including deterministic inventory and state capture that can be shared, replayed, or attached to a report, especially IPSec, DRG, VCN, route table, security list, load balancer, and compartment/region troubleshooting.
---

# OCI Evidence Collector

## Workflow
1. Confirm tenancy/profile context only conceptually; never read or expose protected credential files.
2. Define region/compartment/resource scope and the diagnostic question.
3. Collect deterministic read-only OCI state only for relevant resources.
4. Prefer structured JSON/query output suitable for replay/comparison; redact secrets and unnecessary identifiers where required.
5. Preserve command, scope, timestamp, and evidence provenance.
6. Do not mutate OCI state.

## Output contract
- Scope
- Read-only commands/evidence paths
- Deterministic fields captured
- Gaps/errors
- Next diagnostic step

## Safety boundaries
- Read-only OCI operations only.
- No IAM/network/resource mutation.
- Never expose OCI config keys, tokens, or private material.
