# Loop Instructions

You are running a bounded agentic loop.

## Before you start

1. Read `TASK.md`.
2. Read `PROGRESS.md`.
3. Read `VERIFY.md`.
4. Inspect only the allowed inputs named in `TASK.md`.
5. Identify what changed, what is incomplete, and what needs human review.

## What you should do

Write or update the approved output file:

- `<output-path>`

The output must include:

- Summary
- Inputs reviewed
- Meaningful changes or findings
- Blockers or unresolved questions
- Recommended next action

After writing the output, update `PROGRESS.md` with:

- Date of this run
- Trigger
- Summary of what happened
- Files or systems reviewed
- Output produced
- Verification result
- What the next run should do
- Anything that needs human review

## Safety rules

- Do not delete files.
- Do not rename files.
- Do not move files.
- Do not modify source files unless explicitly approved.
- Do not send messages.
- Do not open or update external tickets.
- Do not push branches or merge pull requests.
- Do not deploy.
- Do not mutate production, cloud, cluster, database, or iMX runtime state.
- Do not read, copy, summarize, or expose secrets, keys, certificates, tokens, private logs, or sensitive account data.
- Only write to the files allowed by `TASK.md`.
- If an action is not clearly allowed, stop and mark human review required.

## Scheduled run policy

When this loop runs on a schedule or interval:

- If there are meaningful changes, write a concise output.
- If there are no meaningful changes, write a short no-change note.
- If human review is needed, mark it clearly in `PROGRESS.md`.
- If the same blocker appears in two consecutive runs, stop retrying and escalate.
- If verification fails twice, stop and mark the run as not accepted.
- Keep scheduled outputs short unless something important changed.
- Do not create extra files unless explicitly allowed.

## Failure policy

If verification fails:

1. If the failure is a missing required section in the output, fix it once.
2. If `PROGRESS.md` was not updated, update it once.
3. If a forbidden file was modified or a forbidden external action occurred, stop immediately and report it.
4. If the same check fails twice, stop and mark human review required.

## Iteration limits

- Maximum automatic correction attempts per run: 1
- Maximum permission level for first version: draft output only
- Maximum default output length: concise report unless the task explicitly requires detail

## Completion rule

The loop run is complete only when:

- approved output exists
- `PROGRESS.md` is updated
- `VERIFY.md` checklist passes
- no forbidden paths or external systems were modified
- risks and human review items are recorded
