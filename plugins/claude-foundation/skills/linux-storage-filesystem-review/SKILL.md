---
name: linux-storage-filesystem-review
description: Review disks, LVM, filesystems, mounts, fstab, inode, and capacity risk.
disable-model-invocation: true
---

# Linux Storage and Filesystem Review

## Purpose
- Review disks, partitions, LVM, filesystems, mounts, and capacity risk safely.

## When to use
- The task reviews disk, partition, LVM, or filesystem state.
- You need to inspect mounts, `fstab`, inode use, or swap layout.
- A full filesystem or resize-risk question needs a read-first review.
- Storage symptoms need evidence before mutation is considered.

## When not to use
- The task asks for destructive disk, LVM, or filesystem mutation without approval.
- The issue is cloud volume assignment and an OCI or AWS storage skill is primary.
- The issue is Kubernetes PVC-specific and Kubernetes storage review is primary.
- The task does not involve host storage state.

## Read first
- `AGENTS.md`
- `README.md`
- The host, runbook, or change request in scope
- Any current mount, disk, or filesystem evidence

## Operating rules
- Inspect before changing.
- Prefer read-only inspection of disk and filesystem state first.
- Keep the scope to the affected host and mount point.
- Call out filesystem type, mount options, and capacity assumptions.
- Do not expose secrets or private file content.

## Required inputs
- Target host or environment
- The mount, disk, or filesystem in scope
- The risk or change question being reviewed

## Codex workflow
1. Read the storage scope and current state first.
2. Inspect disks, mounts, filesystem usage, and LVM layers.
3. Check for inode, capacity, or mount-option risk.
4. Identify any resize, rollback, or backup need.
5. Report the smallest safe next step.

## Expected output
- A short storage review.
- The exact disks, mounts, or filesystems inspected.
- Any capacity or mutation risk.

## Output contract
- State whether the storage state is acceptable, constrained, or risky.
- List the evidence reviewed.
- Separate evidence from inference.

## Validation guidance
- Confirm the mount, filesystem, or device path matches the issue.
- Confirm resize or mutation risk is explicit.
- If files changed, run the repo's own lint/tests if present; otherwise state that no validator is available.

## Rollback guidance
- Preserve backup or snapshot evidence before any storage change.
- Revert the smallest mount or filesystem change if the result is unstable.

## Verification
- The answer names the storage evidence reviewed.
- The answer identifies whether a follow-up resize or rollback is needed.

## Safety boundaries
- No destructive storage mutation without explicit approval.
- No hidden data-loss assumptions.
- No secret disclosure.

## Related skills
- `linux-system-diagnostics-review`
- `linux-networking-diagnostics`
- `rhel-oracle-linux-ops-review`
- `linux-container-host-ops`

## Source attribution
- Adapted from local host operations patterns and non-destructive storage review practice.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- Before large tasks, create or update `docs/activeContext.md`, `docs/currentTask.md`, and `docs/decision-log.md`.
- For repo work, obey `AGENTS.md` first.
- Prefer read-only evidence commands before any fix.
- Do not promise hidden async work or detached execution.
- No secrets handling beyond detection and redaction guidance.
- No self-remediation outside an explicit, scoped approval.