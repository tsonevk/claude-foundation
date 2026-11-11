---
name: verification-loop
description: Run the smallest useful verification sequence after a change and report residual risk clearly.
---

# Verification Loop

## Workflow
1. Identify the exact changed surface and repository-native validation contract.
2. Run the cheapest relevant check first.
3. Escalate only when a cheaper check is inconclusive or risk justifies deeper testing.
4. Confirm only intended files changed.
5. Record what was verified, skipped, or unavailable.
6. End with a readiness verdict.

## Verification depth
- MICRO/COMPACT: main-thread targeted checks only.
- STANDARD: add independent verification only when behavior changed materially and it adds value.
- HIGH-RISK: security/infra/runtime/CI/IaC/permissions changes justify one focused independent read-only review when available.

Do not default to explorer -> coder -> reviewer -> verifier chains for routine work.

## Bounded recovery after a failed check
- Diagnose first. Do not repeat an unchanged deterministic failure; keep repairs inside the approved task boundary.
- If the user has approved iterative repair, use at most five minimal fix/verify attempts per failing slice; stop earlier if evidence is not improving. Retry transient read-only calls narrowly. Report the attempt count.
- No automatic retry of production, destructive, credential, IAM, deployment, DB, privileged host, or external-write actions without explicit approval and verified replay safety.
- Inspect the resulting diff and latest commit before relying on CI. Local green does not mean remote CI is green.
- If red persists, stop with the exact failing check, observations, unverified items, and next safe action.

## Repeat-failure learning (proposal only)
- Trigger only when the same confirmed root cause recurs in two independent tasks or runs; retries within one failing slice do not count.
- Check existing project rules, tests, and prior proposals first. Avoid duplicate rules.
- If a gap remains, suggest **one sanitized candidate**: failure signature, two independent evidence references, confirmed root cause, smallest suitable home (test, script, hook, skill, or project rule), and regression check.
- If the cause or evidence is uncertain, report an investigation need, not a new rule.
- Never auto-edit global/project instructions, skills, hooks, permissions, or other repositories. Changes require separate scoped authorization. Skip this step for one-off/flaky failures and ordinary successful tasks.

## Output contract
- Validation commands/checks
- Results
- Skipped/unavailable checks
- Residual risks
- Readiness verdict

## Safety boundaries
- Do not replace a narrow proof with a broad expensive suite unless needed.
- Do not claim success without evidence.
- Do not create or update handoff files solely because verification ran.
