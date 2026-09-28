---
name: linux-selinux-firewall-review
description: Review SELinux modes, AVCs, firewalld, iptables, and nftables safely.
disable-model-invocation: true
---

# Linux SELinux and Firewall Review

## Purpose
- Review SELinux mode, contexts, denials, and firewall state safely.

## When to use
- The task diagnoses SELinux denials or policy impact on a service.
- You need to review `firewalld`, `firewall-cmd`, `iptables`, or `nftables`.
- A safe policy or firewall change needs read-first review.
- The question is about Linux host policy controls, not cloud security groups.

## When not to use
- The task asks to disable SELinux as a first step.
- The request is broad firewall opening without justification.
- Live policy or firewall mutation is requested without approval.
- The issue is primarily cloud or Kubernetes network policy.

## Read first
- `AGENTS.md`
- `README.md`
- The service, policy, or firewall scope in question
- Recent AVCs, audit evidence, or firewall notes

## Operating rules
- Inspect before changing.
- Prefer read-only policy and firewall review first.
- Keep the rule, port, and service scope explicit.
- Separate AVC evidence from policy assumptions.
- Do not expose secrets or private log content.

## Required inputs
- Target host or environment
- The service or port in scope
- The SELinux or firewall symptom being reviewed

## Codex workflow
1. Read the host policy scope first.
2. Inspect SELinux mode, contexts, AVCs, and firewall state.
3. Identify whether a context fix, rule change, or policy review is needed.
4. Check whether the least-risk path is a label change, rule change, or follow-up.
5. Report the smallest safe next step.

## Expected output
- A concise policy review.
- The SELinux or firewall evidence reviewed.
- Any safe fix, risk, or follow-up.

## Output contract
- State whether the policy state is acceptable, constrained, or risky.
- List the exact SELinux or firewall evidence used.
- Separate evidence from inference.

## Validation guidance
- Confirm the context, AVC, and port/service evidence match the issue.
- Confirm any change path is bounded and reversible.
- If files changed, run the repo's own lint/tests if present; otherwise state that no validator is available.

## Rollback guidance
- Preserve the current label or firewall state before changes.
- Revert the smallest policy or rule change if the service regresses.

## Verification
- The answer names the SELinux or firewall evidence reviewed.
- The answer identifies whether a follow-up policy change is needed.

## Safety boundaries
- No SELinux disablement as a first step.
- No broad firewall opening without justification.
- No live policy mutation without explicit approval.
- No secret disclosure.

## Related skills
- `linux-networking-diagnostics`
- `linux-service-systemd-review`
- `linux-system-diagnostics-review`
- `ansible-linux-ops-guardrails`

## Source attribution
- Adapted from local Linux host policy review patterns and defensive security hygiene.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- Before large tasks, create or update `docs/activeContext.md`, `docs/currentTask.md`, and `docs/decision-log.md`.
- For repo work, obey `AGENTS.md` first.
- Prefer read-only evidence commands before any fix.
- Do not promise hidden async work or detached execution.
- No secrets handling beyond detection and redaction guidance.
- No self-remediation outside an explicit, scoped approval.