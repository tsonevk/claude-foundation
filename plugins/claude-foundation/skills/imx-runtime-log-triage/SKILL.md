---
name: imx-runtime-log-triage
description: Triage iMX runtime logs to isolate incidents without mutating production state.
---

# iMX Runtime Log Triage

## Workflow
1. Confirm instance/layer, symptom, and time window.
2. Use project/iMX documentation to locate the relevant logs; do not guess paths.
3. Read the smallest relevant excerpts and correlate timestamps across middleware/application/DB/network layers when needed.
4. Redact secrets/private payloads and distinguish primary errors from follow-on noise.
5. Return the likely failure boundary and next safe evidence check.

## Output contract
- Scope/time window
- Logs/evidence reviewed
- Key correlated events
- Likely failure boundary
- Next safe action

## Safety boundaries
- Read-only.
- No broad log dumps or secret/private payload exposure.
- No restart or runtime mutation without explicit approval.
