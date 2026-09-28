---
name: terraform-state-backend-review
description: Review Terraform state backend, locking, workspaces, tfstate secrets, import, move, and state rm risk.
---

# Terraform State and Backend Review

## Workflow
1. Read project backend/workspace configuration and state-management documentation; do not print state secrets.
2. Review backend durability, locking, workspace/environment separation, encryption/access, and recovery assumptions.
3. Treat import/move/rm/replace-provider and backend migration as state mutations requiring explicit approval.
4. Verify proposed state operations against current config/resource addresses before recommending execution.
5. Provide backup/rollback/recovery requirements.

## Output contract
- Backend/workspace scope
- Findings
- State-operation risk
- Preconditions
- Rollback/recovery plan

## Safety boundaries
- No state mutation, backend migration, or cloud apply without explicit approval.
- Never expose tfstate secrets or credentials.
