---
name: imx-ops-runbook
description: Use when the task involves iMX operational management, reports, sensors, CMS variables, scheduling, log locations, or start/stop flows across Intranet, AD, and Extranet layers. Do not use for generic Linux work unrelated to iMX.
---

# iMX Operations Runbook

## Workflow
1. Confirm the iMX layer/instance and read its existing runbook/config authority.
2. Discover real paths, variables, scripts, schedules, sensor/report wiring, and logs before proposing commands.
3. Prefer iMX-native ksh and Oracle context; do not substitute generic Linux service management.
4. For changes, preserve current state, make the smallest reversible edit, and validate the exact operational path.
5. Keep start/stop flows explicit about component vs whole-instance impact.

## Output contract
- iMX scope
- Discovered authoritative paths/commands
- Procedure or finding
- Validation
- Rollback / approval gate

## Safety boundaries
- Whole-instance stop/restart/shutdown requires explicit reconfirmation.
- No invented paths/commands.
- No secrets or production mutation beyond the explicitly approved action.
