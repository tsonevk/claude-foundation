---
name: kubernetes-policy-and-access-review
description: Review Kubernetes RBAC, service accounts, pod security, and admission policy for least privilege and safety.
disable-model-invocation: true
---

# Kubernetes Policy and Access Review

## Purpose
- Review Kubernetes access, identity, and pod security posture for least privilege and safe admission behavior.

## When to use
- The task involves RBAC, service accounts, roles, bindings, Pod Security, or admission policy.
- You need to review securityContext, privileged pod risk, or policy engine coverage.
- You want a policy review that complements RBAC auditing without turning into offensive testing.

## When not to use
- The task is only audit-log analysis.
- The task requests privilege escalation testing or policy bypass.
- The task is only a static manifest review with no access or policy focus.

## Read first
- `AGENTS.md`
- `README.md`
- `skills/USAGE.md`
- `skills/registry.yaml`
- The RBAC, service account, securityContext, or admission policy material in scope

## Operating rules
- Inspect before changing.
- Prefer read-only review first.
- State assumptions.
- Separate evidence from inference.
- Keep scope to the smallest useful namespace, role, or workload slice.
- Do not expose secrets.

## Required inputs
- RBAC manifests or cluster evidence.
- Service account, namespace, or workload names.
- Admission policy or Pod Security references, if any.
- Approval boundary for any remediation.

## Codex workflow
1. Read the relevant access and pod security objects first.
2. Check Roles, ClusterRoles, RoleBindings, and ClusterRoleBindings.
3. Review service accounts, automount behavior, and privilege paths.
4. Check securityContext, Pod Security Standards, and admission policy alignment.
5. Recommend the smallest safe policy adjustment or next check.
6. Stop before any bypass or mutation unless explicitly approved.

## Expected output
- A concise policy and access verdict.
- The exact RBAC and security objects reviewed.
- The privilege or policy risks found.
- The next safe action.

## Output contract
- State whether the access and pod security posture is acceptable for the current slice.
- List the concrete privilege paths or controls examined.
- Distinguish facts from interpretation.

## Validation guidance
- Prefer `kubectl auth can-i`, RBAC manifest review, and read-only policy inspection.
- Prefer dry-run or audit-style policy checks when the repo already uses them.
- Confirm the review matches the intended namespace or workload slice.

## Rollback guidance
- If a policy change is too broad, revert to the previous least-privilege baseline.
- Narrow the review to one namespace, service account, or workload at a time.

## Verification
- The reviewed policy objects exist and match the scope.
- The answer names the privilege or admission controls checked.
- The answer separates evidence from inference.

## Safety boundaries
- No privilege-escalation testing.
- No control bypass.
- No secret values in output.
- No production-impacting mutation.

## Related skills
- `auditing-kubernetes-cluster-rbac`
- `kubernetes-manifest-review`
- `kubernetes-cluster-operations-review`
- `helm-chart-review`
- `security-review`

## Source attribution
- Adapted from parked Kubernetes RBAC, Pod Security, and privilege-detection sources.

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
