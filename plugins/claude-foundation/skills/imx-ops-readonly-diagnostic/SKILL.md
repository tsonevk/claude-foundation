---
name: imx-ops-readonly-diagnostic
description: Use this skill when diagnosing iMX operational issues in a safe readonly manner, including host and application health checks, symptom and health reviews, status checks, sensors, reports, logs, WebLogic and application runtime behavior, disabled background jobs, mail modules, Oracle/iMX context, and operator handoff summaries.
---

# iMX Read-Only Operational Diagnostic

## Workflow
1. Establish the iMX instance/layer and read the closest project/runbook authority.
2. Inspect only relevant status, process, sensor/report, config, and log evidence.
3. Use iMX-native ksh/Oracle conventions and actual discovered paths/commands.
4. Preserve evidence and separate observed facts, inference, and unknowns.
5. Stop at diagnosis/recommendation unless a specific mutation is explicitly approved.

## Output contract
- Scope/instance/layer
- Evidence checked
- Diagnosis with confidence
- Unknowns
- Next safe command/action

## Safety boundaries
- Read-only by default.
- Never invent generic `systemctl` or filesystem paths for iMX.
- Whole-instance stop/restart/shutdown requires explicit reconfirmation.
- No secrets/private log payloads.
