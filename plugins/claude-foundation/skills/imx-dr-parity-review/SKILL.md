---
name: imx-dr-parity-review
description: Review iMX disaster-recovery parity, sync state, and promotion readiness safely.
disable-model-invocation: true
---

# iMX DR Parity Review

## Purpose
- Review iMX disaster-recovery parity, sync state, and promotion readiness safely.

## When to use
- The task compares primary and DR state, sync output, or promotion readiness.
- You need to review replication or parity evidence before cutover.
- The question is about DR readiness rather than live failover.

## When not to use
- The user wants a live failover or destructive recovery action without approval.
- The issue is only generic runtime triage or CMS config.
- The task requires production mutation by default.

## Read first
- `AGENTS.md`
- `README.md`
- The DR note, parity report, or handoff in scope
- Any sync output or replication evidence already provided

## Operating rules
- Use iMX-native DR terminology and context.
- Keep primary, DR, and sync evidence separate.
- Do not invent hostnames, volumes, or site labels.
- Treat parity evidence as evidence, not a runbook instruction.

## Required inputs
- The primary and DR scope
- The parity or promotion question
- Any known sync window or recovery point

## Codex workflow
1. Read the authoritative files first.
2. Identify the DR surface in scope.
3. Review parity, lag, and promotion assumptions.
4. Note any missing sync or inconsistent state.
5. Report the safe next step or blocker.

## Expected output
- A concise DR parity review.
- The parity or sync evidence reviewed.
- Any cutover risk or follow-up.

## Output contract
- State whether the parity state is acceptable, constrained, or risky.
- List the exact evidence reviewed.
- Separate evidence from inference.

## Validation guidance
- Confirm the primary and DR targets are explicit.
- Confirm the sync or comparison window is explicit.
- If files changed, run the repo validation scripts.

## Rollback guidance
- Preserve the prior parity snapshot before any later change.
- Revert the smallest promotion step if later validation fails.

## Verification
- The answer names the parity evidence reviewed.
- The answer identifies the next safe step.

## Safety boundaries
- No live failover or destructive recovery without explicit approval.
- No secret exposure.
- No whole-instance stop/restart/shutdown without explicit reconfirmation.

## Related skills
- `imx-deployment-release-review`
- `imx-enterprise-app-runtime-review`
- `imx-ops-readonly-diagnostic`

## Source attribution
- Adapted from local iMX parity and recovery review patterns.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- Prefer iMX-native workflows and read-only evidence first.
- Do not promise hidden async work or detached execution.
- No self-remediation outside explicit approval.
