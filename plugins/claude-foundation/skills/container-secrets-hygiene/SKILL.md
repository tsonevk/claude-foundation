---
name: container-secrets-hygiene
description: Review container workflows for secret handling, exposure, and leakage risks.
disable-model-invocation: true
---

# Container Secrets Hygiene

## Purpose
- Review container workflows for secret handling, exposure, and leakage risks.

## When to use
- The task touches environment variables, secret files, or build-time secret handling.
- You need a bounded review of container secret exposure or leakage.
- You want defensive guidance before changing a container or pipeline.

## When not to use
- The task is a broad secret-management redesign.
- A narrower active security skill already fits better.
- The request is unrelated to container secret flow.

## Read first
- `AGENTS.md`
- `README.md`
- The Dockerfile, Compose file, or pipeline file in scope
- Any secret-related docs or environment files

## Operating rules
- Keep secrets out of images, logs, and committed files.
- Prefer runtime injection over baked-in values.
- Call out secret scope, lifetime, and rotation assumptions.
- Separate evidence from remediation advice.

## Required inputs
- Target repo and file path
- The secret path or environment variable in question
- Constraints on runtime injection or rotation

## Codex workflow
1. Read the authoritative files first.
2. Trace where the secret enters, flows, and exits the container path.
3. Narrow scope to the smallest useful slice.
4. Verify the result with a targeted check or review.
5. Report risks, assumptions, and any unverified areas clearly.

## Expected output
- A concise review or patch recommendation.
- The exact files or secret paths inspected.
- The leak or exposure risk, if any.

## Output contract
- State whether the secret handling is acceptable as-is or needs a change.
- List the concrete issue or the exact fix.
- Include the verification command used or recommended.

## Validation guidance
- No secret material is introduced into tracked files or images.
- The secret flow is explicit and limited.
- Any change remains compatible with least privilege.

## Rollback guidance
- Revert the container or pipeline change if secret handling worsens.
- Restore the previous injection method if the new one is unstable.

## Verification
- The answer identifies the file(s) reviewed.
- The answer separates evidence from inference.
- Validation is run or the missing step is stated clearly.

## Safety boundaries
- Do not print or copy secret values.
- Do not recommend unsafe secret storage.
- Do not broaden scope into secret rotation policy.

## Related skills
- `security-scan`
- `security-review`
- `container-vulnerability-scanning`

## Source attribution
- Adapted from local container review and secret-handling guardrail patterns.

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
