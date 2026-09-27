---
name: docker-compose-review
description: Review Docker Compose files for service wiring, ports, volumes, and runtime safety.
disable-model-invocation: true
---

# Docker Compose Review

## Purpose
- Review Compose files for service wiring, ports, volumes, and runtime safety.

## When to use
- You need a bounded review of `docker-compose.yml` or a Compose override file.
- The task is about service topology, env wiring, mounts, networks, or startup order.
- You want a review-first pass before changing a Compose stack.

## When not to use
- The task needs a deeper security review of privilege or exposure.
- A narrower active skill already covers the exact request.
- The work is unrelated to Compose runtime behavior.

## Read first
- `AGENTS.md`
- `README.md`
- The target Compose file and any override files
- Related Dockerfile, CI, or deployment docs

## Operating rules
- Prefer the smallest safe diff.
- Keep secrets out of environment files and inline values.
- Separate review findings from fix recommendations.
- Call out mount, network, and restart-policy risks.

## Required inputs
- Target repo and Compose file path
- Expected services or workflow
- Constraints on ports, volumes, secrets, or startup order

## Codex workflow
1. Read the authoritative files first.
2. Inspect service definitions and referenced files.
3. Narrow scope to the smallest useful slice.
4. Verify the Compose model or a targeted lint/check.
5. Report risks, assumptions, and any unverified areas clearly.

## Expected output
- A concise review or patch recommendation.
- The exact Compose files inspected.
- Any safety, portability, or startup-order concerns.

## Output contract
- State whether the Compose file is acceptable as-is or needs a change.
- List the concrete issue or the exact fix.
- Include the verification command used or recommended.

## Validation guidance
- The Compose file parses cleanly.
- Referenced service names, ports, and volumes are consistent.
- No secret material is introduced.

## Rollback guidance
- Revert the Compose change if startup or service wiring breaks.
- Restore the previous service image or volume mapping if the new one is unstable.

## Verification
- The answer identifies the file(s) reviewed.
- The answer separates evidence from inference.
- Validation is run or the missing step is stated clearly.

## Safety boundaries
- Do not add unnecessary privileges.
- Do not bake secrets into Compose files.
- Do not broaden scope into deployment automation.

## Related skills
- `docker-patterns`
- `docker-compose-security-review`
- `verification-loop`

## Source attribution
- Adapted from local Docker review patterns and bounded repository review guidance.

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
