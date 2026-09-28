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
