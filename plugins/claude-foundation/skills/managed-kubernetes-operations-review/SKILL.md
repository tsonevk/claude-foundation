---
name: managed-kubernetes-operations-review
description: Review OKE and EKS managed Kubernetes operations, upgrades, and provider integration with read-only evidence.
disable-model-invocation: true
---

# Managed Kubernetes Operations Review

## Purpose
- Review managed Kubernetes operations for OKE and EKS with read-only evidence and provider-aware operational checks.

## When to use
- The task involves OKE, Oracle Kubernetes Engine, EKS, or AWS EKS.
- You need to review node pools, managed node groups, cluster versioning, or provider integrations.
- You need provider-specific evidence for networking, IAM, storage, logging, or monitoring dependencies.

## When not to use
- The task is generic Kubernetes manifest review.
- The task is pure OCI or AWS account review with no Kubernetes layer.
- The task needs live cloud or cluster mutation without approval.

## Read first
- `AGENTS.md`
- `README.md`
- `skills/USAGE.md`
- `skills/registry.yaml`
- The cluster, node pool, IAM, network, and logging evidence in scope

## Operating rules
- Inspect before changing.
- Prefer read-only review first.
- State assumptions.
- Separate evidence from inference.
- Keep scope to the smallest useful cluster, node pool, or managed workload slice.
- Do not expose secrets.

## Required inputs
- Provider name and cluster identifier.
- Node pool or managed node group context.
- Region, compartment, or account scope.
- IAM, network, storage, and monitoring dependencies in scope.

## Codex workflow
1. Read the provider and cluster evidence first.
2. Inspect node pools, managed node groups, and cluster version constraints.
3. Check IAM, networking, storage, and logging integrations.
4. Identify upgrade or dependency risks.
5. Prefer read-only and dry-run style checks.
6. Recommend the smallest safe next action.

## Expected output
- A concise managed-cluster review verdict.
- The provider-specific evidence reviewed.
- The integration or upgrade risks found.
- The next safe action.

## Output contract
- State whether the managed cluster is safe enough for the current slice.
- List the provider-specific control points reviewed.
- Distinguish facts from interpretation.

## Validation guidance
- Prefer provider read-only evidence, cluster describe output, and version checks.
- Prefer cloud-native dry-run, plan, or preview commands when available.
- Confirm the review matches the intended managed cluster and region.

## Rollback guidance
- If an upgrade or node pool change looks risky, stop and return to read-only evidence.
- Narrow the review to one cluster or one node pool at a time.

## Verification
- The managed-cluster evidence reviewed exists and matches the scope.
- The answer names the provider-specific controls used.
- The answer separates evidence from inference.

## Safety boundaries
- No deletes, upgrades, node pool changes, key rotation, or network changes without explicit approval.
- No secret values in output.
- No production-impacting mutation.

## Related skills
- `kubernetes-cluster-operations-review`
- `kubernetes-policy-and-access-review`
- `kubernetes-manifest-review`
- `oci-operations-review`
- `aws-operations-review`

## Source attribution
- Inspired by the parked `securing-kubernetes-on-cloud` source and local OCI/AWS operations review patterns.

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
