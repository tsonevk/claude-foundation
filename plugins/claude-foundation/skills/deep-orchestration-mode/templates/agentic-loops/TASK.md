# Loop Task

## Goal

<Describe the recurring or goal-driven task in one sentence.>

## Expected outputs

Each accepted run should produce or update:

- `<output-path>`
- `<state-path>`
- an up-to-date Facts block in `PROGRESS.md` (exact values, secrets redacted)

## Scope

The loop may:

- inspect `<allowed-inputs>`
- write `<allowed-output-files>`
- update `<state-path>`

The loop must not:

- modify source files unless explicitly approved
- delete, rename, or move files
- push branches or merge pull requests
- post messages or update external systems
- mutate production, cloud, cluster, database, or iMX runtime state
- read, copy, summarize, or expose secrets, keys, certificates, tokens, private logs, or sensitive account data

## Trigger

- Type: <manual | interval | file-change | PR | CI | goal-condition>
- Cadence or condition: <describe exactly>
- First run mode: manual

## Stop condition

The loop is accepted only when:

- required output exists
- state file is updated
- verification checklist passes
- no forbidden files or external systems were modified

## Human review gate

Human review is required when:

- verification fails twice
- the same blocker appears in two consecutive runs
- the loop needs a higher permission level
- any destructive, production-impacting, external-write, or sensitive-data action seems necessary
