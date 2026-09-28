# Loop Verification

Run this as a checker-only pass. Do not modify files during verification unless explicitly instructed after reporting failures.

## Required files

- [ ] `TASK.md` exists.
- [ ] `PROGRESS.md` exists.
- [ ] `LOOP_INSTRUCTIONS.md` exists.
- [ ] Approved output file exists.

## Required output sections

The approved output file includes:

- [ ] Summary
- [ ] Inputs reviewed
- [ ] Meaningful changes or findings
- [ ] Blockers or unresolved questions
- [ ] Recommended next action

## State update

`PROGRESS.md` includes:

- [ ] Date of current run
- [ ] Trigger
- [ ] Summary
- [ ] Files or systems reviewed
- [ ] Output produced
- [ ] Verification result
- [ ] Next run guidance
- [ ] Human review status
- [ ] Facts block present; values copied exactly from evidence
- [ ] No value replaced by an approximation
- [ ] No secret, token, key, or private payload recorded as a fact value

## Safety boundary

- [ ] Only approved files were modified.
- [ ] No source files were modified without approval.
- [ ] No files were deleted, renamed, or moved.
- [ ] No branch was pushed or merged.
- [ ] No external message, ticket, or public comment was sent.
- [ ] No production, cloud, cluster, database, or iMX runtime state was mutated.
- [ ] No secrets, keys, certificates, tokens, private logs, or sensitive account data were read or exposed.

## Decision

Return one of:

- ACCEPTED: all required checks passed.
- NOT ACCEPTED: one or more checks failed.
- HUMAN REVIEW REQUIRED: action is outside the approved permission level or risk boundary.

## Report format

```text
Verification result: <ACCEPTED | NOT ACCEPTED | HUMAN REVIEW REQUIRED>

Passed:
- <check>

Failed:
- <check>

Files modified:
- <path or none>

Human review required:
- <yes/no and reason>
```
