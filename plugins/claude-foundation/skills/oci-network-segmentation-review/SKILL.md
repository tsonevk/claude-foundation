---
name: oci-network-segmentation-review
description: Use this skill when reviewing OCI VCN/subnet/security-list/route-table designs for PROD/NON-PROD segregation, including Terraform export analysis, CIDR split impact, security list reorganization, and colleague handoff instructions.
disable-model-invocation: true
---

# OCI Network Segmentation Review

## Purpose

Use this skill to review OCI network segmentation proposals.

Primary use case:

- split existing shared subnets into PROD and NON-PROD
- review security lists and route tables
- classify changes as safe/risky/migration-required
- prepare instructions for colleagues
- analyze Terraform exports or OCI CLI evidence

## Target policy model

Default target model:

```text
PROD → NON-PROD: allowed when operationally required
NON-PROD → PROD: denied by default
```

Load balancer VCNs are excluded from the core PROD/NON-PROD split enforcement, but must be reviewed for east-west trust leakage.

Default security list goal:

```text
Default security list should be minimal, preferably PMTUD ICMP-only.
Do not use default security list as the real policy layer.
```

Preferred baseline:

```text
Subnets + security lists
```

Do not switch to an NSG-first model unless explicitly requested.

## Common review inputs

Accept and analyze:

- Terraform exports
- OCI CLI JSON evidence
- screenshots
- manual rule lists
- subnet CIDRs
- route table attachments
- security list attachments
- load balancer topology
- client/region structure

Common export path pattern:

```text
configs/<client>/<region>/core.tf
```

## Review dimensions

Evaluate:

1. CIDR feasibility
2. subnet split impact
3. existing VM private IP placement
4. route table reuse
5. security list reuse
6. default security list usage
7. asymmetric trust
8. LB VCN trust leakage
9. DNS labels
10. DHCP option consistency
11. rollback complexity
12. migration sequencing
13. colleague handoff clarity

## CIDR split impact

When shrinking a subnet, always consider:

- existing private IPs outside the new CIDR
- secondary VNICs
- reserved IPs
- load balancer IPs
- DNS labels
- route table and security list attachments
- OCI restrictions on subnet CIDR modification
- whether recreate/migrate is safer than in-place change

Example:

```text
Existing: 10.8.247.0/24
Candidate PROD: 10.8.247.0/25
Candidate NON-PROD: 10.8.247.128/25
```

Check whether existing VMs have IPs that remain inside the intended subnet.

Rebooting a VM does not magically move it into a new subnet. If the subnet CIDR is changed or recreated, resource attachment and IP placement must be validated.

## Change classification

Classify each proposed change:

```text
SAFE
LOW RISK
MEDIUM RISK
HIGH RISK
REQUIRES MIGRATION
REQUIRES CLIENT CONFIRMATION
BLOCKED
```

For each classification include:

```text
Reason:
Evidence:
Required precheck:
Rollback:
```

## Security list rule review

For each rule identify:

```text
Direction:
Protocol:
Source/Destination:
Port:
Purpose:
Environment impact:
Keep / Move / Split / Remove:
Risk:
```

Avoid vague "allow all" unless clearly bounded to trusted internal ranges and justified.

## Recommended output format

Use this structure:

```text
Verdict:
Target model:
Current problem:
Proposed design:
Change classification:
Prechecks:
Implementation sequence:
Rollback:
Colleague instructions:
Open questions:
```

## Colleague handoff

For colleague instructions, make them direct and safe:

```text
Please create:
Please attach:
Please remove only after validation:
Do not delete:
Validate with:
Rollback by:
Evidence to return:
```

## Hard rules

- Do not recommend deleting old resources before validation.
- Always prepare rollback first for VM migration.
- Keep old boot/data volumes until final validation.
- Do not assume LB VCNs are safe just because they are excluded from core split.
- Do not claim security is enforced unless the actual security list/route table attachment supports it.
- Prefer concrete CIDRs and rule tables.

## Final response style

Be pragmatic and explicit.

Use tables for rules and classifications.

For risky changes, state the risk clearly.

