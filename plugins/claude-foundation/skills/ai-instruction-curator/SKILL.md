---
name: ai-instruction-curator
description: Convert raw internet advice, posts, or AI workflow notes into durable, reusable project guidance without bloat.
disable-model-invocation: true
---

# Skill: AI Instruction Curator

## Purpose

Convert raw internet advice, posts, prompt tips, or AI workflow notes into durable reusable project guidance.

## Input

Raw instruction candidates, usually from:

- `inbox/instruction-candidates.md`
- user-provided articles or posts
- AI workflow notes
- lessons learned from previous tasks

## Decision filter

Keep an instruction only if it is:

- durable: likely useful for months
- actionable: changes assistant or Codex behavior
- scoped: has clear trigger conditions
- testable: can be verified
- non-duplicated: does not repeat existing guidance

## Classification

Classify each accepted rule as one of:

- global skill
- project-specific rule
- task-specific template
- evaluator or checklist item

## Promotion rules

Prefer updating an existing skill or checklist over creating a new one.

Do not copy full articles.

Do not preserve motivational wording.

Do not add generic advice without a trigger.

## Output contract

When curating instructions, report:

- accepted rules
- ignored rules and why
- files changed
- verification performed
- risks or follow-up suggestions
