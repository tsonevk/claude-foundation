---
name: oci-networking-diagnostics
description: Diagnose OCI VCN, subnet, route table, security list, NSG, DRG, LPG, VPN, and hybrid networking issues with read-only evidence.
---

# OCI Networking Diagnostics

## Workflow
1. Confirm source, destination, region/compartment, protocol/port, and expected path.
2. Collect only relevant read-only evidence for VCN/subnet, route tables, NSGs/security lists, gateways/DRG/LPG, load balancers, IPSec/BGP/static routes, and DNS where applicable.
3. Trace forward and return paths separately.
4. Distinguish route, security, VPN/BGP, LB, DNS, and host/application evidence.
5. Report the first supported failure boundary and the next safe evidence check.

## Output contract
- Path/scope
- OCI evidence reviewed
- Diagnosis and confidence
- Unknowns
- Next safe action

## Safety boundaries
- Read-only by default.
- No route/security/IAM/VPN/cloud mutation without explicit approval.
- No secret/private key material.
