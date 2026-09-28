---
name: prompt-governance
description: Review reusable Claude Code prompts, skills, and instruction files for clarity, safety, trigger quality, authority boundaries, and testability.
---

# Prompt Governance

## Purpose
Keep reusable Claude Code prompts and skills short, scoped, reviewable, and non-duplicative.

## When to use
- Writing or revising reusable prompts, skills, or instruction docs.
- Deciding whether guidance belongs globally, in a project file, a skill, checklist, template, or reference doc.
- Reviewing trigger overlap, authority leakage, or untestable instructions.

## When not to use
- One-off task execution.
- A clear scoped prompt that already has goal, context, output, and verification.
- Deterministic behavior that belongs in code/tests/hooks/CI instead of prose.

## Prompt shape
For a substantial Claude Code execution prompt, include only what is not already durable in project docs:
1. Goal.
2. Target repository/path when ambiguity exists.
3. Task-specific constraints/exclusions.
4. Expected outcome/change.
5. Verification or success criteria.
6. Explicit commit/push/deploy instructions only when desired.

Normally do not restate architecture, standard tests, project conventions, or current state that the repo already documents.

## Workflow
1. Check job, context, output, and verification.
2. Remove vague/redundant/authority-expanding language.
3. Keep triggers short and specific.
4. Prefer updating an existing reusable artifact over creating a duplicate.
5. Keep project-specific authority in project files.
6. Verify the result can be reused without importing runtime authority or unnecessary context.

## Decision filter
Keep an instruction only if it is durable, actionable, scoped, testable, non-duplicated, and safe to reuse.

## Output contract
- Improved prompt/skill or review note
- Accepted vs removed rules
- Trigger clarity assessment
- Safety/authority concerns
- Recommended classification/location

## Safety boundaries
- Do not copy long external material into active prompts/skills.
- Do not weaken project authority or approval boundaries for brevity.
- Do not automatically create persistent handoff docs in projects that do not need them.
