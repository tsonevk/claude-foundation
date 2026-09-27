---
name: gitlab-container-pipeline
description: Review or shape GitLab CI jobs that build, scan, or publish container images.
disable-model-invocation: true
---

# GitLab Container Pipeline

## Purpose
- Review or shape GitLab CI jobs that build, scan, or publish container images.

## When to use
- The task touches `.gitlab-ci.yml` or a GitLab container job.
- You need a bounded pipeline change for build, scan, or publish steps.
- You want Linux-runner-friendly container job guidance.

## When not to use
- The task is not GitLab CI work.
- A narrower active CI or container skill already fits better.
- The request needs broad pipeline redesign or release automation.

## Read first
- `AGENTS.md`
- `README.md`
- The relevant `.gitlab-ci.yml` and job scripts
- Any container image, scan, or registry docs

## Operating rules
- Prefer pinned images and tools.
- Keep build, scan, and publish stages explicit.
- Preserve runner compatibility and shell portability.
- Call out any secret, auth, or registry assumption.

## Required inputs
- Target repo and pipeline file path
- The job name or stage in scope
- Constraints on runners, registry access, or artifacts

## Codex workflow
1. Read the authoritative files first.
2. Inspect the job, image, and script paths it uses.
3. Narrow scope to the smallest useful slice.
4. Verify the YAML or a targeted pipeline check.
5. Report risks, assumptions, and any unverified areas clearly.

## Expected output
- A concise pipeline recommendation or patch.
- The exact GitLab files and jobs inspected.
- Any portability, auth, or image-tag concerns.

## Output contract
- State whether the job is acceptable as-is or needs a change.
- List the concrete issue or the exact fix.
- Include the validation command used or recommended.

## Validation guidance
- The GitLab YAML parses cleanly.
- Container job images and scripts are pinned or explicit.
- Linux runner behavior is considered.

## Rollback guidance
- Revert the pipeline change if the job stops working.
- Restore the prior image or stage wiring if the new one is unstable.

## Verification
- The answer identifies the file(s) reviewed.
- The answer separates evidence from inference.
- Validation is run or the missing step is stated clearly.

## Safety boundaries
- Do not assume privileged Docker-in-Docker is available.
- Do not introduce secret exposure in pipeline logs.
- Do not broaden scope into deployment orchestration.

## Related skills
- `ci-cd-pipeline-builder`
- `gitlab-ci-trivy-daemonless`
- `linux-ci-parity`

## Source attribution
- Adapted from local GitLab CI and container delivery patterns.

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
