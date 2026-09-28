---
name: agent-hook-guardrails
description: Decide whether a repeated rule belongs in project guidance, a Claude Code hook, a repo-local check, or CI.
---

# Agent Hook Guardrails

## Purpose
Place repeated rules at the cheapest reliable enforcement layer without bloating prompts.

## When to use
- A rule repeats across tasks or repositories.
- The rule may be deterministic and machine-checkable.
- You need to choose between guidance, hook, script, staged check, or CI.

## Decision rule
- Human judgment, authority, scope, and approval rules stay in `CLAUDE.md` / `AGENTS.md`.
- Small deterministic prevention can use a Claude Code hook.
- Reusable deterministic checks belong in repo-local scripts when humans and CI should run them.
- Release gates belong in CI.

## Workflow
1. Classify the rule as judgment-heavy or deterministic.
2. Choose the narrowest enforcement surface.
3. Keep hook commands local, short, timeout-bounded, and reviewable.
4. Prefer `PreToolUse` when a dangerous side effect must be prevented before execution.
5. Verify lifecycle-event support against `docs/CLAUDE_CODE_COMPATIBILITY.md` before wiring anything beyond the existing baseline.
6. Document rollback/disable behavior.

## Output contract
- Recommended placement
- Reason
- Minimal hook/script/check shape when appropriate
- Validation and rollback

## Safety boundaries
- No secrets, network side effects, destructive commands, or production actions from hooks.
- No new global hook without explicit approval.
- Deterministic enforcement must not broaden permissions.
