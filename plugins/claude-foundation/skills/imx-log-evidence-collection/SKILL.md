---
name: imx-log-evidence-collection
description: Collect and summarize iMX log evidence with minimal, redaction-safe scope.
disable-model-invocation: true
---

# iMX Log Evidence Collection

## Purpose
- Collect and summarize iMX log evidence with minimal, redaction-safe scope.

## When to use
- The task asks for a small evidence bundle before deeper iMX diagnostics.
- You need logs, report output, or runtime excerpts from an iMX incident.
- The work should stay read-only and reproducible.

## When not to use
- The request needs sensor review, CMS review, or start/stop guardrails.
- The user wants live mutation or broad incident response.
- The task is already covered by a narrower iMX review skill.

## Read first
- `AGENTS.md`
- `README.md`
- The incident note or handoff in scope
- Relevant iMX log locations and report output

## Operating rules
- Prefer minimal evidence sets.
- Redact secrets, keys, certificates, and private logs.
- Keep time windows explicit.
- Use iMX-native paths and commands provided by the repo context.

## Required inputs
- Target iMX instance, module, or host
- The symptom or question
- The desired time range

## Codex workflow
1. Read the authoritative files first.
2. Identify the log and report sources in scope.
3. Collect the smallest useful evidence set.
4. Redact sensitive material before summarizing.
5. Report what the evidence shows and what remains unknown.

## Expected output
- A concise evidence bundle summary.
- The exact log sources reviewed.
- Any redaction or retention note.

## Output contract
- State what was collected and why.
- List the evidence sources and time window.
- Separate evidence from inference.

## Validation guidance
- Confirm the evidence sources match the requested symptom.
- Confirm sensitive content is redacted.
- If files changed, run the repo validation scripts.

## Rollback guidance
- This skill is read-only; rollback applies only to later changes.

## Verification
- The answer identifies the collected evidence.
- The answer states any remaining gaps.

## Safety boundaries
- No secret exposure.
- No whole-instance stop/restart/shutdown without explicit reconfirmation.
- No destructive cleanup.

## Related skills
- `imx-ops-readonly-diagnostic`
- `imx-runtime-log-triage`
- `imx-security-evidence-review`
- `imx-enterprise-app-runtime-review`

## Source attribution
- Adapted from local iMX evidence-first and log triage patterns.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- Prefer iMX-native workflows and read-only evidence first.
- Do not promise hidden async work or detached execution.
- No self-remediation outside explicit approval.
