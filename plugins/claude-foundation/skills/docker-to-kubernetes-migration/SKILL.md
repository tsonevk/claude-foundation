---
name: docker-to-kubernetes-migration
description: Review Docker or Compose workloads for a bounded migration path to Kubernetes.
disable-model-invocation: true
---

# Docker to Kubernetes Migration

## Purpose
- Review Docker or Compose workloads for a bounded migration path to Kubernetes.

## When to use
- You need a small, practical mapping from Docker to Kubernetes concepts.
- The task is about migration planning, not full cluster administration.
- You want to preserve app behavior while changing the runtime substrate.

## When not to use
- The task is a Kubernetes cluster security review.
- A narrower Docker or Kubernetes skill already fits better.
- The request is a live migration with production rollout already approved.

## Read first
- `AGENTS.md`
- `README.md`
- The Dockerfile or Compose file being migrated
- Any Kubernetes manifests or cluster constraints already in scope

## Operating rules
- Preserve observable runtime behavior first.
- Keep the migration bounded to one thin slice.
- Call out config, storage, and networking changes explicitly.
- Separate mapping advice from cluster-specific actions.

## Required inputs
- Source Docker or Compose artifact
- Target Kubernetes constraints or manifest path
- Constraints on storage, ports, secrets, or rollout

## Codex workflow
1. Read the authoritative files first.
2. Map the existing runtime shape to Kubernetes primitives.
3. Narrow scope to the smallest useful slice.
4. Verify the manifest, translation, or migration note.
5. Report risks, assumptions, and any unverified areas clearly.

## Expected output
- A concise migration plan or patch recommendation.
- The exact source and target artifacts inspected.
- Any behavior, storage, or rollout gaps.

## Output contract
- State the migration target and whether the slice is ready.
- List the concrete mapping or the exact fix.
- Include the verification command used or recommended.

## Validation guidance
- The target manifest reflects the source runtime shape.
- Storage, ports, and env mapping are explicit.
- Any rollout assumption is clearly stated.

## Rollback guidance
- Revert the translation if the target behavior diverges.
- Restore the previous manifest or runtime shape if the new one is unstable.

## Verification
- The answer identifies the source and target artifacts reviewed.
- The answer separates evidence from inference.
- Validation is run or the missing step is stated clearly.

## Safety boundaries
- Do not assume cluster-wide privileges.
- Do not broaden scope into deployment orchestration without approval.
- Do not hide unsupported runtime differences.

## Related skills
- `docker-patterns`
- `auditing-kubernetes-cluster-rbac`
- `ci-cd-pipeline-builder`

## Source attribution
- Adapted from local container review patterns and Kubernetes review guidance.

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
