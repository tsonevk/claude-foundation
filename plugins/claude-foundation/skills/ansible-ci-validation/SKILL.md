---
name: ansible-ci-validation
description: "Validate Ansible with ansible-lint, syntax-check, check mode, molecule, and CI gating safely."
disable-model-invocation: true
---

# Ansible CI Validation

## Purpose
- Validate Ansible with ansible-lint, syntax-check, check mode, molecule, and CI gating safely.

## When to use
- The task is about CI validation for Ansible content.
- You need to decide what to run locally versus in GitLab or another CI system.

## When not to use
- The issue is only playbook logic or inventory scope.
- A narrower review skill already covers the problem.

## Read first
- Playbook, role, and inventory paths.
- Existing CI config and any current Ansible validation commands.
- Any molecule scenarios or lint rules in the repo.

## Operating rules
- Inspect before changing.
- Prefer read-only review first.
- State assumptions.
- Separate evidence from inference.
- Keep CI validation small and reproducible.

## Required inputs
- The Ansible content to validate.
- The CI environment or runner constraints.
- Any known lint, syntax, or molecule expectations.

## Codex workflow
1. Read the Ansible files and CI setup first.
2. Choose the smallest useful validation commands.
3. Check lint, syntax, check mode, and molecule fit.
4. Identify missing or flaky gates.
5. Report the safe validation plan and gaps.

## Expected output
- A concise CI validation recommendation.
- The commands or gates to run.
- Any missing validation coverage.

## Output contract
- Name the Ansible scope and CI context reviewed.
- Separate evidence from inference.
- Avoid promising execution you have not run.

## Validation guidance
- Prefer `ansible-lint`, `ansible-playbook --syntax-check`, `--check`, and `molecule` where appropriate.
- Confirm runner compatibility before suggesting CI changes.
- If files changed, run the repo's own lint/tests if present; otherwise state that no validator is available.

## Rollback guidance
- No mutation by default, so rollback is usually not needed.
- If a CI change is proposed, keep the previous job or gate available.

## Verification
- The validation commands or gates match the reported Ansible scope.
- The answer distinguishes confirmed checks from inference.

## Safety boundaries
- Read-only first.
- No production-impacting execution without explicit confirmation.
- No secret output.
- Prefer Linux/GitLab runner compatibility.

## Related skills
- `ansible-playbook-review`
- `ansible-role-review`
- `ansible-inventory-review`
- `ansible-idempotency-safety`

## Source attribution
- No exact upstream match.
- Closest local defensive context: `linux-ci-parity` and `verification-loop`.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- For RHEL/Oracle Linux Ansible work, avoid assumptions that break package or service conventions.
- Do not promise hidden async work or detached execution.
- No open-ended shell access.
- No secrets handling beyond detection and redaction guidance.