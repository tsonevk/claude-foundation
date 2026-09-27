---
name: container-log-weekly-archive
description: Use when a containerized service writes many small log or temp files to a bind-mounted host directory and inode pressure must be reduced with container-side cleanup, weekly period-bounded archives, and delete-after-success retention.
disable-model-invocation: true
---

Reduce inode pressure from container log trees by keeping cleanup and archive work inside the container, selecting one closed weekly window at a time, and deleting originals only after archive validation succeeds.

## When to use
- A bind-mounted log directory contains thousands of small files or per-request directories.
- Host-side cleanup is unreliable because files are owned by the container user.
- Daily cleanup already exists, but a weekly archive of older periods is needed.
- The user wants archives kept for a longer retention period while removing loose files immediately after successful packing.

## Core rules
- Prefer `docker exec -u 0` or an equivalent container-root path for archive and delete work when host permissions are limited.
- Keep daily cleanup and weekly archive behavior in the same script if the job already runs daily.
- Archive exactly one closed time window per run. Do not archive "everything older than N days".
- Exclude the archive output directory from normal compression and prune passes.
- Delete originals only after:
  - archive command exits successfully
  - archive file exists
  - archive file is non-empty
  - archive listing or validation succeeds

## Preferred workflow
1. Inspect the current cleanup script, scheduler, and bind-mounted log directory.
2. Confirm whether the host user can traverse and compress the container-created files.
3. If not, keep all heavy operations inside the container.
4. Identify the inode source:
   - rotated logs
   - temp files
   - per-request directories
5. Keep daily cleanup focused on recent temp files and stale directories.
6. Add a weekly archive branch that:
   - runs only on the chosen weekday or when forced
   - selects the closed 7-day window that is 7-13 days old
   - writes archives to a dedicated `archive/` directory
   - removes packed originals only after validation
7. Add a longer retention rule for weekly archives, such as 6 months.
8. Update ignore rules so runtime archives are not committed.

## Date-window guidance
- Prefer computing the archive window on the host and passing it into the container as environment variables.
- This avoids relying on limited BusyBox `date` implementations inside minimal containers.
- A good default weekly window is:
  - start: 13 days ago
  - end: 7 days ago
- This captures the previous fully closed 7-day block when the script runs on Sunday.

## Implementation notes
- If the log tree uses date-prefixed directory names, prefer prefix-based grouping over `mtime` alone.
- If rotated logs use date suffixes, include only the files that match the same weekly window.
- Exclude `archive/` from:
  - gzip rotation passes
  - temp-file cleanup
  - empty-directory pruning
- If the script currently chmods the whole tree every run, flag that as potentially expensive and revisit separately.

## Validation checklist
- `bash -n` or shell syntax validation passes.
- A non-destructive candidate count can be produced for the next weekly archive window.
- The script logs:
  - whether weekly mode ran
  - selected window
  - number of archive candidates
  - archive path created
  - number of originals deleted
  - number of expired archives pruned
- Verify that archive retention is longer than daily loose-file retention.

## Output checklist
- target files
- exact changes
- validation commands
- rollback approach
- open risks or assumptions
