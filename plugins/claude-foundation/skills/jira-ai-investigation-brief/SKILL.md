---
name: jira-ai-investigation-brief
description: Use this skill when converting Jira/Atlassian tasks into structured AI investigation briefs, DevOps analysis plans, colleague handoff instructions, and evidence collection checklists.
disable-model-invocation: true
---

# Jira AI Investigation Brief

## Purpose

Use this skill to turn Jira tasks into actionable investigation briefs.

Use it when the user asks:

- analyze this Jira task
- prepare AI investigation
- make colleague instructions
- what evidence is needed
- break this task into steps
- create prompt for AI/Codex
- create DevOps investigation plan

## Input types

Accept:

- Jira text
- screenshots
- copied comments
- acceptance criteria
- logs
- links
- partial notes
- user summary

If a link is inaccessible, work from the provided text and say what is missing.

## Standard brief structure

Use:

```text
Problem:
Business / operational impact:
Known facts:
Unknowns:
Assumptions:
Evidence needed:
Readonly checks:
Possible root causes:
Risk:
Proposed next action:
Colleague handoff:
AI/Codex prompt:
Definition of done:
```

## DevOps evidence checklist

Depending on topic, include relevant evidence:

- hostnames
- environment
- timestamps
- logs
- config files
- exact commands
- before/after state
- affected users
- recent changes
- network path
- security rules
- service status
- pipeline/job output
- rollback constraints

## Colleague handoff format

Use:

```text
Please check:
Please run:
Please return:
Do not change:
Escalate if:
```

## AI/Codex prompt format

When generating a prompt for Codex, include:

```text
Use the harness-driven-coding skill.

Task:
Context:
Files to inspect:
Rules:
Expected changes:
Verification:
Commit/push:
Return:
```

## Risk classification

Use:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

Explain why.

## Final response style

Be structured and practical.

Use tables when comparing options.

Avoid vague advice.

The goal is to make the Jira task executable by a colleague or AI agent.

