---
name: podman-rootless-service
description: Review or configure rootless Podman service wiring, user units, and socket activation.
disable-model-invocation: true
---

# Podman Rootless Service

## Purpose
- Review or configure rootless Podman service wiring, user units, and socket activation.

## When to use
- The task touches a rootless Podman service, socket, or user unit.
- You need a bounded review of service activation, env, or volume behavior.
- You want a safer, least-privilege Podman service workflow.

## When not to use
- The task needs a deeper security review of rootless Podman exposure.
- A narrower active Podman skill already covers the exact request.
- The request is unrelated to service wiring or activation.

## Read first
- `AGENTS.md`
- `README.md`
- The Podman unit file, socket file, or service wrapper
- Any systemd user docs or container launch scripts

## Operating rules
- Prefer rootless operation and least privilege.
- Keep service, socket, and container concerns separate.
- Call out storage, network, and permission assumptions.
- Avoid hidden host coupling.

## Required inputs
- Target repo or host path
- The unit, socket, or launch file in scope
- Constraints on user identity, volumes, or networking

## Codex workflow
1. Read the authoritative files first.
2. Inspect the service wiring and referenced launch inputs.
3. Narrow scope to the smallest useful slice.
4. Verify the unit or a targeted check relevant to the change.
5. Report risks, assumptions, and any unverified areas clearly.

## Expected output
- A concise service review or patch recommendation.
- The exact unit files or launch artifacts inspected.
- Any portability, permission, or activation concerns.

## Output contract
- State whether the Podman service is acceptable as-is or needs a change.
- List the concrete issue or the exact fix.
- Include the verification command used or recommended.

## Validation guidance
- The unit or socket file parses cleanly.
- Rootless activation and paths are explicit.
- No unnecessary privileges are introduced.

## Rollback guidance
- Revert the unit or socket change if activation breaks.
- Restore the previous user unit or launch path if the new one is unstable.

## Verification
- The answer identifies the file(s) reviewed.
- The answer separates evidence from inference.
- Validation is run or the missing step is stated clearly.

## Safety boundaries
- Do not add rootful privileges by default.
- Do not bake secrets into unit files or service commands.
- Do not broaden scope into host reconfiguration.

## Related skills
- `podman-rootless-security-review`
- `docker-patterns`
- `verification-loop`

## Source attribution
- Adapted from local container service and least-privilege review patterns.

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
