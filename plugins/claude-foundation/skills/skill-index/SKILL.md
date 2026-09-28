---
name: skill-index
description: Search the full claude-foundation catalog for a task, including catalog-tier skills that are installed but not listed in context. Use manually when you need catalog discovery beyond the visible routing set.
disable-model-invocation: true
---

# Skill index

The plugin ships a large skill catalog. Routing-tier skills are listed in context; catalog-tier skills are installed and runnable but deliberately invisible to keep per-session context small.

## Steps
1. Read `${CLAUDE_SKILL_DIR}/CATALOG.md`.
2. Pick the most specific match for the task; prefer one skill over several.
3. Check its classification marker: `[C:AUTO]` (CATALOG_AUTO) may be read and
   applied inline as router-selected guidance for the matching prompt;
   `[C:MANUAL]` (MANUAL_ONLY) must NOT be applied automatically — tell the
   user to invoke `/claude-foundation:<name>` explicitly instead, and stop.
4. If nothing matches, continue without stretching an unrelated skill onto the task.

Applying a `CATALOG_AUTO` skill's guidance this way is our own catalog-routing
mechanism, not native Claude Code Skill invocation — `disable-model-invocation:
true` still applies to every catalog-tier skill and is unrelated to whether
this router may act on it.

## Rules
- Never invent a skill name.
- Project authority remains stronger than catalog guidance.
- `CATALOG.md` is generated; regenerate it with `python3 scripts/generate_skill_index.py --write` after tier/description changes.
- Never use "I can just read the file" to bypass a `MANUAL_ONLY` classification.
