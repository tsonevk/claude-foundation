---
name: imx-start-stop-guardrails
description: Review iMX start, stop, restart, and shutdown safety with explicit confirmation.
disable-model-invocation: true
---

# iMX Start/Stop Guardrails

## Purpose
- Review iMX start, stop, restart, and shutdown safety with explicit confirmation.

## When to use
- The task touches start or stop scripts for iMX modules or whole instances.
- You need to review restart safety before any operational change.
- The request includes `start_instance.sh`, `Shutdown_iMX.sh`, or module control scripts.

## When not to use
- The user wants a whole-instance stop, restart, or shutdown without reconfirmation.
- The request is generic Linux service control instead of iMX-native control.
- The issue is purely about logs or evidence.

## Read first
- `AGENTS.md`
- `README.md`
- The iMX runbook or module docs in scope
- Any existing start/stop script or change note

## Operating rules
- Use iMX-native scripts and Oracle context.
- Do not use generic `systemctl` controls for iMX application layers.
- Treat whole-instance stop/restart/shutdown as a separate explicit confirmation step.
- Keep module, instance, and DR paths separate.

## Required inputs
- Target iMX instance or module
- The desired action or guardrail question
- Any confirmation or maintenance boundary

## Codex workflow
1. Read the authoritative files first.
2. Identify the exact start/stop surface in scope.
3. Check whether the request is module-local or whole-instance.
4. Verify rollback and recovery assumptions.
5. Report the safest next step and any confirmation requirement.

## Expected output
- A concise safety review.
- The scripts or controls reviewed.
- The confirmation boundary, if any.

## Output contract
- State whether the action is safe, risky, or blocked pending reconfirmation.
- List the exact scripts or evidence used.
- Separate evidence from inference.

## Validation guidance
- Confirm the scope is not broader than the request.
- Confirm whole-instance effects are called out clearly.
- If files changed, run the repo validation scripts.

## Rollback guidance
- Preserve the prior instance state and script path before any later change.
- Revert the smallest control change if it breaks recovery.

## Verification
- The answer names the control surface reviewed.
- The answer states whether explicit reconfirmation is required.

## Safety boundaries
- No whole-instance stop/restart/shutdown without explicit reconfirmation.
- No generic `systemctl` guidance for iMX application layers.
- No destructive or production-impacting action by default.

## Related skills
- `imx-ops-readonly-diagnostic`
- `imx-enterprise-app-runtime-review`
- `imx-deployment-release-review`
- `imx-dr-parity-review`

## Source attribution
- Adapted from local iMX runtime and operational safety patterns.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- Prefer iMX-native workflows and read-only evidence first.
- Do not promise hidden async work or detached execution.
- No self-remediation outside explicit approval.
