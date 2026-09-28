---
name: rhel-oracle-linux-ops-review
description: Review Red Hat Enterprise Linux and Oracle Linux lifecycle, repos, subscriptions, kernels, and patch conventions.
---

# RHEL and Oracle Linux Ops Review

## Workflow
1. Confirm host/environment, OS release, kernel family, and operational question.
2. Inspect release/kernel, yum/dnf repositories, ULN/subscription, module streams, and patch/reboot evidence read-only.
3. Keep RHEL vs Oracle Linux and RHCK vs UEK differences explicit.
4. Identify lifecycle/support/patch implications without guessing from generic Linux behavior.
5. Report the smallest safe next step and reboot impact when relevant.

## Output contract
- OS/kernel/repo scope
- Evidence
- Lifecycle/patch finding
- Reboot/support risk
- Next safe action

## Safety boundaries
- No OS-wide/package/repo mutation or reboot without explicit approval.
- No registration credential exposure.
