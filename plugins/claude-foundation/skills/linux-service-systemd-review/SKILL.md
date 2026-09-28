---
name: linux-service-systemd-review
description: Review systemd units, failed services, journalctl evidence, and timer safety.
disable-model-invocation: true
---

# Linux Service and Systemd Review

## Workflow
1. Confirm host/environment and exact unit/timer scope.
2. Inspect unit/drop-ins, dependencies, status, and targeted journal evidence read-only.
3. Separate observed failure state from restart/enable assumptions.
4. Identify the smallest unit, ordering, environment, or timer issue.
5. Propose validation and rollback before any mutation.

## Safety boundaries
- No production-impacting restart/enable/disable without explicit approval.
- Do not apply generic systemd lifecycle guidance to iMX whole-instance operations.
