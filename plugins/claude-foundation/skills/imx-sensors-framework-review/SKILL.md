---
name: imx-sensors-framework-review
description: Review iMX sensors, reports, and runtime enablement safely.
disable-model-invocation: true
---

# iMX Sensors Framework Review

## Purpose
- Review iMX sensors, reports, and runtime enablement safely.

## When to use
- The task reviews sensor definitions, sensor output, or sensor runtime state.
- You need to inspect `imxstatus`, `batchreport`, `interfacereport`, or `sensors desc`.
- The question is about sensor enablement or sensor config drift.

## When not to use
- The task is only general log triage.
- The request needs live mutation without explicit approval.
- The issue is better handled by a broader read-only iMX diagnostics review.

## Read first
- `AGENTS.md`
- `README.md`
- Sensor docs, reports, or handoff notes in scope
- The sensor config and runtime paths provided by the user context

## Operating rules
- Use iMX-native paths and the repo-provided context.
- Do not invent sensor locations.
- Treat sensor enable/disable state as sensitive runtime state.
- Keep the scope to the smallest useful sensor set.

## Required inputs
- Sensor name, report name, or runtime path
- The symptom or review question
- Any known instance or module context

## Codex workflow
1. Read the authoritative files first.
2. Identify the sensor or report scope.
3. Review sensor definitions, config, and runtime state.
4. Compare enabled versus expected state.
5. Report the findings and the safest next step.

## Expected output
- A concise sensor framework review.
- The sensor and report evidence reviewed.
- Any configuration or enablement drift.

## Output contract
- State whether the sensor state is acceptable, constrained, or risky.
- List the exact sensor evidence reviewed.
- Separate evidence from inference.

## Validation guidance
- Confirm the sensor names and paths match the repo context.
- Confirm runtime enablement and report output are explicit.
- If files changed, run the repo validation scripts.

## Rollback guidance
- Restore the prior sensor enablement state if a later change breaks reviewability.

## Verification
- The answer names the sensor evidence reviewed.
- The answer identifies whether a narrower follow-up is needed.

## Safety boundaries
- No secret exposure.
- No whole-instance stop/restart/shutdown without explicit reconfirmation.
- No destructive runtime changes.

## Related skills
- `imx-ops-readonly-diagnostic`
- `imx-log-evidence-collection`
- `imx-start-stop-guardrails`
- `imx-deployment-release-review`

## Source attribution
- Adapted from local iMX sensor and report review patterns.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- Prefer iMX-native workflows and read-only evidence first.
- Do not promise hidden async work or detached execution.
- No self-remediation outside explicit approval.
