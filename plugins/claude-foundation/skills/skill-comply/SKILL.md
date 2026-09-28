---
name: skill-comply
description: Check a Claude Foundation skill or instruction file against local format, lifecycle, routing, and safety rules.
disable-model-invocation: true
---

# Skill Comply

## Purpose
Make skill reviews mechanical enough to catch format, lifecycle, source, trigger, routing, and policy drift early.

## When to use
- Drafting or updating a skill file.
- Checking required sections, routing metadata, or banned patterns.
- Running a small compliance gate before publishing or promoting a skill.

## When not to use
- Pure content ideation.
- A stronger repository-native validator already covers the requested check.
- Deep domain judgment is the main task.

## Required inputs
- Skill path or candidate content.
- Intended trigger/operator.
- Local authoring/validation rules.
- Source attribution when relevant.

## Workflow
1. Check frontmatter for `name` and a short trigger-focused `description`.
2. Check required sections and lifecycle/routing metadata.
3. Check that the skill is narrow, reusable, and non-duplicative.
4. Check source attribution/adaptation notes when applicable.
5. Scan for unsafe runtime guidance, secrets, permission-evasion language, and stale external dependencies.
6. Confirm project authority remains stronger than generic skill guidance.
7. Confirm the output contract is testable.
8. Report pass/fail with minimal fixes.

## Output contract
- Compliance verdict
- Lifecycle/routing recommendation
- Missing/invalid sections
- Trigger/description quality
- Safety/authority findings
- Minimal remediation list

## Safety boundaries
- Do not rewrite content silently.
- Do not promote unreviewed third-party material directly into active guidance.
- Do not auto-enable/disable/remove skills.
- Required human approvals and project-specific rules remain mandatory.
