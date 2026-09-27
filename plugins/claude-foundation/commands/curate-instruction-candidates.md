---
description: Extract durable, reusable AI-working rules from instruction candidates and file them in the smallest correct place.
---

Read:

1. `~/.agents/inbox/instruction-candidates.md` (or a candidates file named in the task)
2. `~/.claude/skills/` and `~/.agents/skills/`
3. Any project `checklists/`
4. The project `CLAUDE.md` / `AGENTS.md`

Goal: Extract only durable, reusable AI-working rules from the instruction candidates.

- Do not copy full posts. Do not add motivational text. Do not duplicate existing rules.

For each candidate idea:

- decide whether it is useful
- classify it as global, project-specific, task-specific, or evaluator
- add it to the smallest correct place
- include trigger conditions
- include a verification or checklist item if applicable

Prefer updating existing skills over creating new ones.

Output:

- summary of accepted rules
- ignored rules and why
- files changed
- verification performed
- risks or follow-up suggestions
