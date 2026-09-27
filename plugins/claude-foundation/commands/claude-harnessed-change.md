---
description: Turn the current coding or repo request into a bounded harness-driven change plan, then execute only the approved minimal safe scope.
---

Goal: Turn the current coding or repo request into a bounded harness-driven change plan, then execute only the approved minimal safe scope.

Inspect first (no edits):

1. Read the project `CLAUDE.md` / `AGENTS.md`.
2. Read `docs/activeContext.md`, `docs/currentTask.md`, `docs/decision-log.md` if present.
3. Read the target file(s) and any directly related tests, CI jobs, or configs.
4. State what was found and what remains unknown.

Define the harness:

- **Target:** file(s) and specific location of the change
- **Success criteria:** observable outcome that proves correctness
- **Expected files changed:** complete list (flag surprises)
- **Validation commands:** ordered cheapest-first
- **Rollback path:** `git checkout -- <file>` or equivalent
- **Risks:** what could break or is out of scope
- **Iteration cap:** max 3 attempts before stopping and reporting

Constraints:

- Do not edit until the harness is defined.
- Do not touch files outside the expected-files list.
- Do not read, edit, or print secret or credential files.
- Do not deploy, restart, or apply to production without explicit per-action confirmation.
- Do not claim success without evidence from a validation command.

Implement:

- Make the smallest change that satisfies the success criteria.
- One logical change per step.

Validate:

- Run validation commands cheapest-first.
- Stop at first clear failure; revert and report.

Final response:

- Files changed
- Validation commands run and results
- What was not verified and why
- Risks and open questions
- Rollback command
- Next safe action
