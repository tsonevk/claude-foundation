---
name: linux-ci-container-parity
description: Keep container-related GitLab CI changes compatible with Linux runners and shell behavior.
disable-model-invocation: true
---

# Linux CI Container Parity

## Purpose
- Keep container-related GitLab CI changes compatible with Linux runners and shell behavior.

## When to use
- The task touches GitLab CI jobs that build, scan, or publish containers.
- You need shell, path, or runner behavior to match Linux CI.
- The work mixes container tooling with cross-platform validation.

## When not to use
- The task is not CI-related.
- A narrower Linux CI or container skill already fits better.
- The request is a Windows-only local convenience change.

## Read first
- `AGENTS.md`
- `README.md`
- The relevant GitLab CI file and job scripts
- Any Docker, Podman, or scanner config used by the job

## Operating rules
- Treat Linux runner behavior as the source of truth.
- Keep shell resolution and path handling explicit.
- Prefer pinned tools and stable job images.
- Call out any runner or daemon assumption clearly.

## Required inputs
- Target repo and CI file path
- The container job or script in scope
- Constraints on runners, shells, or artifacts

## Codex workflow
1. Read the authoritative files first.
2. Inspect the job, script, and tool resolution path.
3. Narrow scope to the smallest useful slice.
4. Verify the YAML or a targeted Linux-compatible check.
5. Report risks, assumptions, and any unverified areas clearly.

## Expected output
- A concise CI parity recommendation or patch.
- The exact CI files and scripts inspected.
- Any shell, runner, or portability concerns.

## Output contract
- State whether the CI path is acceptable as-is or needs a change.
- List the concrete issue or the exact fix.
- Include the validation command used or recommended.

## Validation guidance
- Linux runner behavior is considered explicitly.
- Tool resolution is portable and pinned where possible.
- The CI file parses cleanly.

## Rollback guidance
- Revert the CI change if Linux runner behavior breaks.
- Restore the prior image or shell path if the new one is unstable.

## Verification
- The answer identifies the file(s) reviewed.
- The answer separates evidence from inference.
- Validation is run or the missing step is stated clearly.

## Safety boundaries
- Do not assume Windows Git Bash paths in CI.
- Do not hide missing Linux dependencies with silent fallbacks.
- Do not broaden scope into pipeline redesign.

## Related skills
- `linux-ci-parity` — general shell/path parity; this skill covers container-job parity specifically.
- `gitlab-container-pipeline`
- `verification-loop`

## Source attribution
- Adapted from local Linux CI parity guidance and container pipeline patterns.

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
