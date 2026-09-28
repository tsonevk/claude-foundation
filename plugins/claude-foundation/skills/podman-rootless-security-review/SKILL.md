---
name: podman-rootless-security-review
description: "Review rootless Podman usage for capability, volume, and network safety."
disable-model-invocation: true
---

# Podman Rootless Security Review

## Purpose
- Review rootless Podman usage for capability, volume, and network safety.

## When to use
- The task matches the skill name and sits in the defensive scope described by the user.
- The work needs a bounded review, triage, or validation pass instead of a broad redesign.

## When not to use
- The task is an offensive, destructive, or unauthorized attack workflow.
- The user wants live mutation without explicit confirmation.
- A narrower active skill already covers the exact request.

## Required inputs
- Target repo, system, or artifact path.
- Relevant evidence, logs, manifests, or config paths.
- Any explicit approval boundary for mutation or rollout.

## Codex workflow
1. Read the authoritative files first.
2. Narrow scope to the smallest useful slice.
3. Preserve evidence before any remediation or refactor.
4. Verify the result against the local validator or a targeted check.
5. Report risks, assumptions, and any unverified areas clearly.

## Output contract
- A concise recommendation, review, or evidence-backed summary.
- The exact files, logs, or artifacts inspected.
- A short list of next safe steps or remaining gaps.

## Verification
- The referenced files exist and match the task scope.
- The answer separates evidence from inference.
- If files changed, run the repo's own lint/tests if present; otherwise confirm a narrower relevant check passes.

## Safety boundaries
- Read-only first.
- No production mutation without explicit confirmation.
- No secrets in prompts, logs, scripts, tickets, or repositories.
- No broad destructive cleanup.
- Preserve evidence before remediation.
- Prefer least privilege.

## Related skills
- `docker-patterns`
- `security-scan`
- `security-review`

## Source attribution
- No exact upstream match. Closest defensive upstream skill: `docker-patterns`.

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