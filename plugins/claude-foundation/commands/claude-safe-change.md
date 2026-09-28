---
description: Make the smallest safe additive change for the requested task, with verification and a clean summary.
---

Goal: Make the smallest safe additive change needed for the requested task.

Before editing:

1. Read the project `CLAUDE.md` / `AGENTS.md`.
2. Read relevant `docs/currentTask.md`, `docs/activeContext.md`, and `docs/decision-log.md` if present.
3. Inspect existing files before creating new ones.

Constraints:

- Do not overwrite project-specific authority.
- Do not add generic shell or runtime authority unless explicitly requested.
- Do not commit secrets, local scratch files, or generated noise.
- Prefer docs, tests, or config-only changes when a runtime change is not required.

Verification:

- Run available lightweight checks.
- If a check is unavailable, state why.
- Review `git diff --check` and `git status --short`.

Commit (only if asked):

- Commit only relevant files with a concise message.
- Push to the active branch only when instructed.

Final response:

- Summary
- Files changed
- Verification
- Risks or assumptions
- Commit SHA (if committed)
