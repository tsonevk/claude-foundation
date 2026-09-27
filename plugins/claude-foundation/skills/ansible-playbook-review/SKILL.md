---
name: ansible-playbook-review
description: Review Ansible playbooks, tasks, handlers, vars, templates, and execution safety with a read-first operations lens.
---

# Ansible Playbook Review

## Workflow
1. Read project authority, the target playbook, referenced roles/vars/templates, inventory scope, and execution notes.
2. Trace task order, handlers, variable use, host targeting, and side effects.
3. Separate verified behavior from inference.
4. Identify the smallest correctness, idempotency, or safety issue.
5. Use `ansible-playbook --syntax-check` and other project-native read-only validation when appropriate.

## Output contract
- Scope/files reviewed
- Findings and evidence
- Host/execution risk
- Validation performed
- Smallest safe next step

## Safety boundaries
- Read-only first.
- No production-impacting run without explicit confirmation.
- No secret output.
