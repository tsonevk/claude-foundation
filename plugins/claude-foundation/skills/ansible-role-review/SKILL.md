---
name: ansible-role-review
description: Review Ansible role structure, defaults, vars, tasks, handlers, templates, files, and meta for safe reuse.
---

# Ansible Role Review

## Workflow
1. Read project authority, the role tree/metadata, defaults, vars, tasks, handlers, templates/files, and direct consumers.
2. Trace variable precedence, task flow, handlers, and reuse boundaries.
3. Identify the smallest correctness, idempotency, or portability issue.
4. Validate through project-native lint/syntax checks where available.

## Output contract
- Role scope reviewed
- Evidence-backed findings
- Reuse/safety risks
- Validation
- Smallest safe next step

## Safety boundaries
- Read-only first.
- No production-impacting execution without explicit confirmation.
- No secret output.
