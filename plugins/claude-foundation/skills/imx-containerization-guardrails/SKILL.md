---
name: imx-containerization-guardrails
description: Review iMX containerization with strict read-first guardrails and bounded change scope, including Dockerfile, compose, and container runtime config, privilege boundaries, volume mounts, network settings, and evidence-preserving operations for iMX/Oracle workloads.
---

# iMX Containerization Guardrails

## Workflow
1. Read project authority and the exact iMX/Oracle container artifacts in scope.
2. Separate host, iMX runtime, Oracle dependencies, image, compose, mounts, privileges, and network assumptions.
3. Preserve the existing runtime contract and inspect before editing.
4. Prefer least privilege and explicit mounts/networking; flag root/privileged/socket/host coupling.
5. Make only the smallest approved change.
6. Validate with repository-native checks such as `docker compose config`, Dockerfile/build validation, or shell syntax checks.

## Output contract
- Artifacts reviewed
- Runtime/privilege/mount/network findings
- Exact bounded change when needed
- Validation
- Rollback and residual risk

## Safety boundaries
- No generic `systemctl`/`sudo` assumptions for iMX lifecycle.
- Whole-instance iMX stop/restart/shutdown requires explicit reconfirmation.
- No production mutation or secret exposure.
