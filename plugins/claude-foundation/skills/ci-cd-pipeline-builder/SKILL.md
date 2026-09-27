---
name: ci-cd-pipeline-builder
description: Design or update CI/CD pipelines with explicit stages, checks, and deployment gates.
---

# CI/CD Pipeline Builder

## Workflow
1. Read project pipeline authority and existing CI configuration first.
2. Map required stages and existing gates.
3. Make the smallest pipeline change that satisfies the goal.
4. Keep deploy/publish approvals explicit and separate from validation.
5. Validate syntax/config using repository-native checks before any push or rollout.

## Output contract
- Pipeline stages affected
- Minimal change
- Gates/approvals
- Validation performed
- Residual risks

## Safety boundaries
- Do not add silent auto-deploy behavior.
- Do not expose secrets or widen runner permissions.
- Do not deploy or push unless explicitly requested.
