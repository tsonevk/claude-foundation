---
name: repo-intake-scan
description: Use when taking over or first inspecting a repository and you need a practical map of boundaries, source-of-truth files, risky areas, validation entrypoints, and reusable ideas.
disable-model-invocation: true
---

Run a lightweight repository intake scan before deeper implementation.

## Goals
- Build a useful mental model fast.
- Separate source of truth from generated or runtime artifacts.
- Find reusable patterns, validation entrypoints, and likely risks.

## When to use
- First contact with a repository.
- Before a major change in an unfamiliar codebase.
- When evaluating whether a repo contains reusable ideas or skills.

## Do not use when
- You already know the repository well.
- The task is a tiny, local edit with obvious scope.

## Intake checklist
- identify whether the target is a repo root or a container directory
- locate `AGENTS.md`, `README`, canonical context files, and major config files
- identify source-of-truth vs generated files
- locate validation commands, tests, hooks, and automation entrypoints
- spot runtime or secret-bearing files that should not be touched casually
- extract reusable patterns worth turning into skills, rules, or templates

## Output format
Return:
- summary
- repository shape
- source-of-truth files
- must-not-touch files
- validation entrypoints
- reusable ideas worth adopting
- `NEW SKILL:` suggestions
- `UPDATE AGENTS.MD:` suggestions

## Quality bar
- Prefer practical boundaries over exhaustive inventories.
- Make recommendations actionable.
- If the path is not the real repo root, say so immediately and rescope.

## Related skills
- Use `project-guidelines-template` when the repository deserves a reusable project-local onboarding or execution skill after the intake scan.
