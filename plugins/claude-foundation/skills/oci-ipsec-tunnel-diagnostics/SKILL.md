---
name: oci-ipsec-tunnel-diagnostics
description: "Diagnose OCI IPSec tunnel state, IKE/BGP/static routing drift, and evidence for read-only investigations."
disable-model-invocation: true
---

# OCI IPSec Tunnel Diagnostics

## Purpose
- Diagnose OCI IPSec tunnel state, IKE/BGP/static routing drift, and evidence for read-only investigations.

## When to use
- The issue involves OCI IPSec tunnel status, routing, or tunnel drift.
- You need a read-only evidence bundle before any change proposal.

## When not to use
- The task asks for tunnel restart, rekey, or other live mutation.
- A generic OCI network review is sufficient and tunnel detail is not needed.

## Read first
- OCI CLI help for IPSec connection and tunnel commands.
- Existing tunnel, DRG, route, and CPE evidence.
- Any timestamps or observed outage details.

## Operating rules
- Inspect before changing.
- Prefer read-only evidence first.
- State assumptions clearly.
- Separate evidence from inference.
- Keep to the affected connection and tunnel set only.

## Required inputs
- Compartment and region scope.
- IPSec connection OCID or CPE reference when available.
- Observed symptom, timestamps, and any routing expectations.

## Codex workflow
1. Read existing evidence and topology first.
2. Collect connection, tunnel, DRG, and route state.
3. Compare the observed state to the expected path.
4. Identify tunnel drift or missing evidence.
5. Report the smallest credible fault domain.

## Expected output
- A concise tunnel diagnosis.
- The evidence collected and the commands used.
- Any missing evidence or next questions.

## Output contract
- Name the connection or tunnel scope reviewed.
- Separate evidence from inference.
- Do not present a mutation plan as a completed fix.

## Validation guidance
- Use targeted `oci network ip-sec-connection` and `ip-sec-tunnel` reads only.
- Confirm the evidence matches the reported tunnel state.
- If files changed, run the repo's own lint/tests if present; otherwise state that no validator is available.

## Rollback guidance
- No mutation by default, so no rollback is expected.
- If a fix is later proposed, keep the smallest reversible recovery path.

## Verification
- The tunnel and routing evidence exists for the reported scope.
- The answer distinguishes current state from inferred cause.

## Safety boundaries
- Read-only first.
- No destructive OCI tunnel or routing commands without explicit approval.
- No secret output.
- Respect compartment, region, and home-region scope.

## Related skills
- `oci-networking-diagnostics`
- `oci-operations-review`
- `oci-security-evidence-review`

## Source attribution
- No exact upstream match.
- Closest local defensive context: `oci-evidence-collector` and `oci-network-security-review`.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- For repo work, obey `AGENTS.md` first.
- For OCI diagnostics, default to read-only evidence collection and deterministic reporting.
- Do not promise hidden async work or detached execution.
- No open-ended shell access.
- No secrets handling beyond detection and redaction guidance.