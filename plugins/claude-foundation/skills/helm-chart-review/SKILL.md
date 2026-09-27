---
name: helm-chart-review
description: Review Helm charts, values, templates, and rendered output for safe defaults and release risk.
disable-model-invocation: true
---

# Helm Chart Review

## Purpose
- Review Helm charts for safe defaults, coherent templates, and release-readiness before install or upgrade.

## When to use
- The task involves `Chart.yaml`, `values.yaml`, templates, helpers, hooks, or rendered chart output.
- You need to validate upgrade or rollback risk.
- You need to review chart-generated manifests before deployment.

## When not to use
- Raw Kubernetes manifests are primary and no chart exists.
- The task is only container image review.
- The task asks to deploy or upgrade live releases without approval.

## Read first
- `AGENTS.md`
- `README.md`
- `skills/USAGE.md`
- `skills/registry.yaml`
- The chart, values files, and rendered output in scope

## Operating rules
- Inspect before changing.
- Prefer read-only review first.
- State assumptions.
- Separate evidence from inference.
- Keep scope to the smallest useful release, namespace, or values slice.
- Do not expose secrets.

## Required inputs
- Chart path or rendered output path.
- Values files or override inputs.
- Target release and namespace.
- Any deployment or rollback constraints already in scope.

## Codex workflow
1. Read the chart and values first.
2. Render the chart or inspect generated output if needed.
3. Check templates, helpers, hooks, and safe defaults.
4. Review secret handling, release naming, and upgrade/rollback risk.
5. Compare rendered manifests to the intended workload shape.
6. Report the smallest safe follow-up.

## Expected output
- A concise chart review verdict.
- The chart files and rendered output reviewed.
- The risks in values, templates, hooks, or release behavior.
- The next safe action.

## Output contract
- State whether the chart is safe enough for the current slice.
- List the concrete chart concerns or confirm the absence of blockers.
- Distinguish facts from interpretation.

## Validation guidance
- Prefer `helm lint`, `helm template`, and `helm diff` when available.
- Prefer manifest validation on rendered output when the repo already uses it.
- Confirm the rendered output matches the intended release shape.

## Rollback guidance
- Revert the chart or values change if the rendered output is unstable or unsafe.
- Narrow the review to one chart or one values file at a time.

## Verification
- The chart files exist and match the scope.
- The answer names the chart validation used.
- The answer separates evidence from inference.

## Safety boundaries
- No install, upgrade, rollback, or delete guidance without explicit approval.
- No secret values in output.
- No production-impacting mutation.

## Related skills
- `kubernetes-manifest-review`
- `kubernetes-policy-and-access-review`
- `kubernetes-cluster-operations-review`
- `docker-to-kubernetes-migration`

## Source attribution
- Adapted from the parked `securing-helm-chart-deployments` source and local Kubernetes manifest review patterns.

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
