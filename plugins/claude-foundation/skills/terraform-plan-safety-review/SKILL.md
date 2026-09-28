---
name: terraform-plan-safety-review
description: Review Terraform plan/apply safety, replacements, destroys, lifecycle, dependencies, drift, and rollback.
---

# Terraform Plan Safety Review

## Workflow
1. Read project Terraform authority, backend/workspace context, changed config, and plan evidence.
2. Identify creates/updates/replacements/destroys, sensitive resources, dependency cascades, and lifecycle changes.
3. Distinguish intended change from drift and provider-generated noise.
4. Call out blast radius and rollback/import/state implications.
5. Prefer `fmt -check`, `validate`, and reviewed `plan` evidence; stop before apply.

## Output contract
- Workspace/scope
- Plan summary
- Destructive/replacement risks
- Drift/unknowns
- GO / CONDITIONAL GO / NO-GO recommendation for apply review

## Safety boundaries
- No `apply`, `destroy`, state mutation, or cloud mutation without explicit approval.
- No secret/state content exposure.
