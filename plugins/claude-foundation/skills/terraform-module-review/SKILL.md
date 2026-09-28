---
name: terraform-module-review
description: "Review Terraform module structure, variables, outputs, providers, locals, and reuse safely."
disable-model-invocation: true
---

# Terraform Module Review

## Purpose
- Review Terraform module structure, variables, outputs, providers, locals, and reuse safely.

## When to use
- The task is about module layout, inputs, outputs, or composition.
- You need to review a module before using or publishing it.

## When not to use
- The issue is mainly plan safety or change risk.
- A provider version or state backend review is a better fit.

## Read first
- The module files and any calling root module.
- Variable, output, provider, and local definitions.
- Any module docs or examples in the repo.

## Operating rules
- Inspect before changing.
- Prefer read-only review first.
- State assumptions.
- Separate evidence from inference.
- Keep scope to one module and its direct callers.

## Required inputs
- Module path or repository path.
- The consumer or intended use case.
- Any expected inputs, outputs, or invariants.

## Codex workflow
1. Read the module structure and inputs first.
2. Trace variable flow, outputs, and provider assumptions.
3. Check reuse, naming, and coupling boundaries.
4. Identify the smallest structural issue or drift.
5. Report facts and the safest next step.

## Expected output
- A concise module review.
- The files and consumers inspected.
- Any structure or interface gaps.

## Output contract
- Name the module scope reviewed.
- Separate evidence from inference.
- Keep recommendations minimal and reusable.

## Validation guidance
- Use `terraform fmt`, `terraform validate`, or a read-only plan when appropriate.
- Confirm the module path and callers before concluding.
- If files changed, run the repo's own lint/tests if present; otherwise state that no validator is available.

## Rollback guidance
- No mutation by default, so rollback is usually not needed.
- If a change is proposed, keep the previous module interface available.

## Verification
- The module structure matches the reported scope.
- The answer distinguishes confirmed behavior from inference.

## Safety boundaries
- Read-only first.
- No destructive cloud commands without explicit approval.
- No secret output.
- Respect module reuse boundaries and provider scope.

## Related skills
- `terraform-plan-safety-review`
- `terraform-state-backend-review`
- `terraform-provider-versioning`
- `auditing-terraform-infrastructure-for-security`

## Source attribution
- No exact upstream match.
- Closest local defensive context: `auditing-terraform-infrastructure-for-security`.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- For cloud changes, inspect plan before apply.
- Treat tfstate as sensitive.
- Do not promise hidden async work or detached execution.
- No open-ended shell access.
- No secrets handling beyond detection and redaction guidance.