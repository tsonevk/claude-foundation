---
name: prompt-quality
description: Turn vague AI requests into reliable, testable work instructions with explicit job, relevant context, output contract, and verification.
---

# Prompt Quality Gate

## Purpose
Turn vague requests into reliable instructions without bloating prompts.

## Core rule
Do not optimize for clever wording. Optimize for:
1. clear job definition
2. relevant context
3. explicit output
4. testable result

## Required preflight
Identify only what materially affects execution:

### Job
- What exactly must be done?
- What does done look like?

### Context
- What repo/file facts, constraints, examples, or prior decisions matter?
- What is already available in project docs and should not be repeated in the prompt?
- What is unknown and actually blocking?

### Output
- What format is required?

### Test
- What command/check proves the result?

## Anti-patterns
Avoid:
- motivational role-play filler
- restating project documentation in every prompt
- copying long posts/articles
- untestable rules
- duplicated instructions across global/project/task layers
- asking the user for context that repository files can supply

## Compact mode
For Claude Code prompts, prefer:

`Define goal -> add only task-specific context/constraints -> require project-doc read -> define success/verification -> state approval boundaries.`
