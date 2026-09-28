---
name: imx-orchestration-tower-review
description: Review iMX Orchestration Tower jobs, schedules, and execution evidence safely.
disable-model-invocation: true
---

# iMX Orchestration Tower Review

## Purpose
- Review iMX Orchestration Tower jobs, schedules, and execution evidence safely.

## When to use
- The task reviews Orchestration Tower definitions, schedules, job runs, or execution drift.
- You need to understand orchestration dependencies before a change or release.
- The question is about orchestration evidence rather than execution.

## When not to use
- The user wants live orchestration changes without approval.
- The issue is only general runtime triage or CMS config.
- The task requires destructive mutation or production-impacting actions.

## Read first
- `AGENTS.md`
- `README.md`
- The orchestration note, handoff, or job record in scope
- Any run log or job output already provided by the repo context

## Operating rules
- Use iMX-native orchestration context.
- Treat schedules, job parameters, and execution logs as evidence.
- Do not invent job names or target hosts.
- Keep review scope to the smallest useful orchestration slice.

## Required inputs
- The job, schedule, or orchestration item in scope
- The symptom or review question
- Any known maintenance or execution window

## Codex workflow
1. Read the authoritative files first.
2. Identify the orchestration surface in scope.
3. Review job parameters, schedule state, and execution evidence.
4. Note dependencies and failure exposure.
5. Report the safe next step or blocker.

## Expected output
- A concise orchestration review.
- The job and schedule evidence reviewed.
- Any execution risk or follow-up.

## Output contract
- State whether the orchestration state is acceptable, constrained, or risky.
- List the exact evidence reviewed.
- Separate evidence from inference.

## Validation guidance
- Confirm the job name and schedule are explicit.
- Confirm the execution window or run id is explicit.
- If files changed, run the repo validation scripts.

## Rollback guidance
- Preserve the prior schedule or job definition before any later change.
- Revert the smallest orchestration step if a later change fails.

## Verification
- The answer names the orchestration evidence reviewed.
- The answer identifies the next safe step.

## Safety boundaries
- No live orchestration mutation without explicit approval.
- No secret exposure.
- No whole-instance stop/restart/shutdown without explicit reconfirmation.

## Related skills
- `imx-deployment-release-review`
- `imx-enterprise-app-runtime-review`
- `imx-ops-readonly-diagnostic`

## Source attribution
- Adapted from local iMX release and execution review patterns.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- Prefer iMX-native workflows and read-only evidence first.
- Do not promise hidden async work or detached execution.
- No self-remediation outside explicit approval.
