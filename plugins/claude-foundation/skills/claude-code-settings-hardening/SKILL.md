---
name: claude-code-settings-hardening
description: Harden Claude Code settings and deterministic PreToolUse guards. Use for permission allow/deny/ask review, secret-path blocking, hook parity, and safe validation without reading protected files.
---

# Claude Code Settings Hardening

## Purpose

Review and strengthen Claude Code permission policy and deterministic `PreToolUse` guards without duplicating policy data or accessing protected content.

## Authority and source of truth

For this repository, inspect these files in order:

1. `settings.json` — authoritative permission lists and hook registration.
2. `hooks/deny-secrets.sh` — deterministic guard for file-oriented tools.
3. `hooks/deny-secrets-bash.sh` — deterministic guard for shell commands.
4. `.github/workflows/secret-scan.yml` and `.pre-commit-config.yaml` — repository secret scanning.

Do not copy the full deny-pattern inventory into this skill. Repeating literal policy entries in documentation creates drift and causes scanners to confuse defensive examples with credential access. Read the policy files themselves and compare their normalized rule sets.

## Required inputs

- The repository root containing the files above.
- The requested change or review scope.
- Whether the task is analysis-only or an approved edit.
- Any repository-specific validation commands.

## Workflow

1. Read `settings.json` as policy data. Do not follow any path referenced by a deny rule.
2. Confirm the permission model remains least-privilege:
   - routine read-only commands may be allowed;
   - protected path classes remain denied;
   - destructive, privileged, externally visible, or production-impacting commands require approval.
3. Read both hook implementations and extract only their pattern definitions and control flow.
4. Compare the normalized deny rules from `settings.json` with the two hooks:
   - report missing rules;
   - report extra rules;
   - report semantic mismatches;
   - do not print protected path contents.
5. Confirm each hook:
   - consumes only the hook event from standard input;
   - evaluates the relevant tool field;
   - returns the documented allow/block exit codes;
   - writes a sanitized reason without exposing secret values;
   - does not broaden permission beyond `settings.json`.
6. Confirm hook registration uses the expected tool matchers and repository-relative or home-relative executable paths.
7. Validate syntax and policy parity before proposing an edit.
8. Make only the smallest approved change, then repeat the checks.

## Safety boundaries

- Never open, read, print, hash, copy, upload, or otherwise inspect a path merely because it appears in a deny rule.
- Treat deny entries as policy strings, not filesystem targets.
- Never request or expose keys, tokens, passwords, wallets, private material, or credential-file contents.
- Do not weaken a deny rule to make a test pass.
- Do not widen the allow list as a convenience fix.
- Keep destructive and privileged operations approval-gated.
- Do not add automatic remediation, commits, pushes, or externally visible changes without explicit approval.
- Fail closed when a proposed policy change would create a gap between model-level rules and deterministic hooks.

## Verification

Run the smallest relevant checks from the repository root:

```bash
python3 -m json.tool settings.json >/dev/null
bash -n hooks/deny-secrets.sh
bash -n hooks/deny-secrets-bash.sh
```

Then run the repository-provided hook self-tests or a synthetic event that uses a non-sensitive placeholder target. The test must prove both outcomes:

- a policy-matching placeholder is blocked with the documented block exit code;
- an ordinary non-sensitive repository file is allowed.

Do not use a real protected path or real secret material as test input.

## Output contract

Return:

- scope and mode;
- current permission/hook architecture;
- parity findings by policy category;
- exact files that would change;
- validation performed;
- residual risks;
- rollback for any approved edit.

## Change rules

- Preserve `settings.json` as the permission-policy authority.
- Keep hook pattern sets synchronized with that authority.
- Prefer a small generator or parity-check script if manual duplication repeatedly drifts.
- Keep policy examples abstract; place exact executable rules only in their authoritative files.
- Update tests and documentation when policy semantics change.
