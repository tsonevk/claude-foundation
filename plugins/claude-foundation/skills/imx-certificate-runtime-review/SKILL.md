---
name: imx-certificate-runtime-review
description: Review iMX certificate runtime state, expiry, trust, and binding evidence safely.
disable-model-invocation: true
---

# iMX Certificate Runtime Review

## Purpose
- Review iMX certificate runtime state, expiry, trust, and binding evidence safely.

## When to use
- The task inspects cert expiry, truststores, keystores, or runtime binding evidence.
- You need to review certificate-related runtime risk before release or rotation.
- The question is about certificate state rather than secret management or live rotation.

## When not to use
- The user wants secret material exposed or exported.
- The task needs live rotation or mutation without approval.
- The issue is only generic app runtime triage or deployment review.

## Read first
- `AGENTS.md`
- `README.md`
- The certificate note, trust report, or handoff in scope
- Any runtime binding or expiry evidence already provided

## Operating rules
- Use iMX-native Oracle context and app-layer terminology.
- Do not print private keys, passwords, or secret values.
- Keep expiry, trust, and binding concerns separate.
- Prefer read-only evidence over assumptions.

## Required inputs
- The certificate, truststore, or runtime endpoint in scope
- The review question or expiry concern
- Any known service or maintenance window

## Codex workflow
1. Read the authoritative files first.
2. Identify the certificate surface in scope.
3. Review expiry, chain, and runtime binding evidence.
4. Check whether trust or hostname assumptions are explicit.
5. Report the safe next step or rotation risk.

## Expected output
- A concise certificate runtime review.
- The certificate evidence reviewed.
- Any expiry, trust, or binding risk.

## Output contract
- State whether the certificate state is acceptable, constrained, or risky.
- List the exact evidence reviewed.
- Separate evidence from inference.

## Validation guidance
- Confirm the cert or trust object is explicit.
- Confirm the runtime endpoint or service is explicit.
- If files changed, run the repo validation scripts.

## Rollback guidance
- Preserve the prior certificate/trust snapshot before any later change.
- Revert the smallest binding change if a later step fails.

## Verification
- The answer names the certificate evidence reviewed.
- The answer identifies the next safe step.

## Safety boundaries
- No secret, key, or wallet exposure.
- No live rotation without explicit approval.
- No whole-instance stop/restart/shutdown without explicit reconfirmation.

## Related skills
- `imx-enterprise-app-runtime-review`
- `imx-cms-config-review`
- `imx-ops-readonly-diagnostic`

## Source attribution
- Adapted from local iMX runtime and certificate review patterns.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- Prefer iMX-native workflows and read-only evidence first.
- Do not promise hidden async work or detached execution.
- No self-remediation outside explicit approval.
