# Agentic Loop Readiness Checklist

Use this before creating or enabling a recurring, scheduled, polling, or goal-driven agent loop.

## Candidate fit

- [ ] The task repeats or benefits from goal-driven continuation.
- [ ] The task benefits from state from previous runs.
- [ ] The first useful version can produce a report, draft, or state update without high-risk writes.
- [ ] The expected output is small enough to review repeatedly.
- [ ] The loop reduces cognitive load instead of creating a noisy report stream.

## Context

- [ ] Repo authority files are known.
- [ ] Required input files, logs, issues, CI results, or docs are identified.
- [ ] State file is defined.
- [ ] Output path is defined.
- [ ] Sensitive paths and data classes are denied.

## Verification

- [ ] Required output sections are defined.
- [ ] A checker-only verification pass exists.
- [ ] Pass/fail criteria are objective enough to apply repeatedly.
- [ ] Validation commands are project-native or the narrowest safe substitute.
- [ ] Failed verification is written to state.

## Permission boundary

- [ ] First version is read-heavy and write-light.
- [ ] Allowed files are explicit.
- [ ] Denied files and denied external actions are explicit.
- [ ] Source edits require explicit approval.
- [ ] External writes require explicit approval.
- [ ] Production, cloud, cluster, database, iMX runtime, or destructive actions require explicit confirmation.
- [ ] Secrets, keys, certificates, tokens, private logs, and sensitive account data are not read or exposed.

## Stop and escalation

- [ ] Maximum attempts per run are defined.
- [ ] Repeated blockers escalate instead of retrying forever.
- [ ] Human review is required for higher permissions.
- [ ] Human review is required after repeated verification failure.
- [ ] A rollback or discard path exists for generated output.

## Scheduling gate

- [ ] Manual run has succeeded more than once.
- [ ] Output stayed concise and useful.
- [ ] State stayed compact and accurate.
- [ ] Verification caught failures clearly.
- [ ] Cadence matches how often new information appears.
- [ ] There is a reviewed scheduler or task runner if the loop must run outside the current interactive session.

## Decision

- [ ] APPROVE MANUAL LOOP ONLY
- [ ] APPROVE SCHEDULED LOOP
- [ ] NEEDS REDESIGN
- [ ] REJECT AS TOO RISKY OR TOO NOISY
