# Reusable Loop Prompt

Use deep-orchestration-mode loop adapter.

## Goal

<Describe the recurring or goal-driven task.>

## Rules

- Read repo authority first.
- Read `TASK.md`, `PROGRESS.md`, `LOOP_INSTRUCTIONS.md`, and `VERIFY.md` before acting.
- Keep the first run manual unless scheduling has already been explicitly approved.
- Inspect only the allowed inputs.
- Write only the approved output files.
- Update `PROGRESS.md` before stopping.
- Run the checker phase from `VERIFY.md` before reporting completion.
- Stop if human review is required.

## Denied actions

Do not:

- delete, rename, or move files
- modify source files unless explicitly approved
- send messages or update external systems
- push branches or merge pull requests
- deploy
- mutate production, cloud, cluster, database, or iMX runtime state
- read, copy, summarize, or expose secrets, keys, certificates, tokens, private logs, or sensitive account data

## Output

Return:

- What changed or was reviewed
- Output files changed
- State update summary
- Verification result
- Risks or untested areas
- Human review needs
- Next safe action
