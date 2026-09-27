---
name: container-supply-chain-security
description: Review container provenance, SBOM, signing, and image trust controls.
disable-model-invocation: true
---

# Container Supply Chain Security

## Purpose
- Review container provenance, SBOM, signing, and image trust controls.

## When to use
- The task touches image provenance, SBOMs, signatures, or registry trust.
- You need a bounded supply-chain review for container artifacts.
- You want to verify trust controls before a release or deployment.

## When not to use
- The task is only about a local Dockerfile or Compose syntax issue.
- A narrower active security skill already covers the exact request.
- The request is unrelated to image trust or provenance.

## Read first
- `AGENTS.md`
- `README.md`
- The image, SBOM, or registry artifact in scope
- Any signing, attestation, or policy docs

## Operating rules
- Prefer verifiable provenance over implicit trust.
- Keep findings separate from remediation steps.
- Call out signing, pinning, and registry trust assumptions.
- Treat SBOM and attestation evidence as first-class inputs.

## Required inputs
- Target image or artifact path
- The trust, SBOM, or signing mechanism in use
- Constraints on registry access or offline validation

## Codex workflow
1. Read the authoritative files first.
2. Trace the artifact from build to registry to runtime.
3. Narrow scope to the smallest useful slice.
4. Verify the trust chain or review the evidence available.
5. Report risks, assumptions, and any unverified areas clearly.

## Expected output
- A concise trust or provenance review.
- The exact artifact or metadata inspected.
- The missing trust control, if any.

## Output contract
- State whether the supply-chain posture is acceptable as-is or needs a change.
- List the concrete issue or the exact fix.
- Include the verification command used or recommended.

## Validation guidance
- The artifact identity is explicit.
- The provenance or signing evidence is traceable.
- The result separates evidence from inference.

## Rollback guidance
- Revert the provenance or registry change if trust checks fail.
- Restore the previous pinning or signing policy if the new one is unstable.

## Verification
- The answer identifies the artifact reviewed.
- The answer separates evidence from inference.
- Validation is run or the missing step is stated clearly.

## Safety boundaries
- Do not fake provenance or signatures.
- Do not broaden into release engineering without approval.
- Do not expose private registry credentials.

## Related skills
- `container-image-hardening`
- `analyzing-sbom-for-supply-chain-vulnerabilities`
- `security-review`

## Source attribution
- Adapted from local container hardening and SBOM-oriented defensive patterns.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- Before large tasks, create or update `docs/activeContext.md`, `docs/currentTask.md`, and `docs/decision-log.md`.
- For repo work, obey `AGENTS.md` first.
- For iMX work, use iMX-native ksh and Oracle context; avoid generic `sudo` or `systemctl` guidance; whole-instance stop requires explicit reconfirmation.
- For OCI diagnostics, default to read-only evidence collection and deterministic reporting.
- For MCP repos, registry, config, policy files, and tests are authoritative; skills are only guidance.
- Do not promise hidden async work or detached execution.
- No open-ended shell access.
- No secrets handling beyond detection and redaction guidance.
- No self-remediation outside an explicit, scoped approval.
