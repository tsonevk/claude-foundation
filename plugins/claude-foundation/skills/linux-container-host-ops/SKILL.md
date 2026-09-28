---
name: linux-container-host-ops
description: Review Linux host-side container operations, storage, networking, and service support.
disable-model-invocation: true
---

# Linux Container Host Ops

## Purpose
- Review Linux host-side container operations, storage, networking, and service support.

## When to use
- The task is about the host that runs containers, not the container app itself.
- You need bounded host-side guidance for container runtime support or triage.
- You want a defensive, evidence-first operating review.

## When not to use
- The task is purely inside the container image or Compose file.
- A narrower runtime or CI skill already fits better.
- The request needs destructive host changes.

## Read first
- `AGENTS.md`
- `README.md`
- Host service, runtime, or storage files in scope
- Any logs or health checks for the container host

## Operating rules
- Prefer read-only host inspection first.
- Keep host, runtime, and application layers separate.
- Call out cgroup, storage, network, and permission assumptions.
- Avoid hidden coupling to a single host setup.

## Required inputs
- Target host or repo path
- The host-side runtime or service in scope
- Constraints on storage, networking, or user identity

## Codex workflow
1. Read the authoritative files first.
2. Identify the host-side container support path.
3. Narrow scope to the smallest useful slice.
4. Verify the result with a targeted host or config check.
5. Report risks, assumptions, and any unverified areas clearly.

## Expected output
- A concise host operations review or patch recommendation.
- The exact host files or logs inspected.
- Any portability or service-support concerns.

## Output contract
- State whether the host-side setup is acceptable as-is or needs a change.
- List the concrete issue or the exact fix.
- Include the verification command used or recommended.

## Validation guidance
- The host-side service or config is explicit.
- Runtime, storage, and networking assumptions are visible.
- Any proposed fix is bounded and testable.

## Rollback guidance
- Revert the host-side change if service support breaks.
- Restore the prior runtime or storage setting if the new one is unstable.

## Verification
- The answer identifies the host evidence reviewed.
- The answer separates evidence from inference.
- Validation is run or the missing step is stated clearly.

## Safety boundaries
- Do not recommend destructive host cleanup without confirmation.
- Do not assume privileged access unless stated.
- Do not broaden into full host redesign.

## Related skills
- `linux-ci-parity`
- `container-runtime-diagnostics`
- `verification-loop`

## Source attribution
- Adapted from local Linux host parity and container runtime review patterns.

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
