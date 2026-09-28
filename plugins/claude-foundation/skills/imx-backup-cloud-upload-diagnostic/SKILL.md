---
name: imx-backup-cloud-upload-diagnostic
description: Use this skill when diagnosing iMX backup and cloud upload behavior, including OCI Object Storage uploads, rclone comparison, not_uploaded directories, upload logs, retry staging, and restore/upload instructions.
disable-model-invocation: true
---

# iMX Backup Cloud Upload Diagnostic

## Purpose

Use this skill for iMX backup and cloud upload troubleshooting.

Use it when the user asks about:

- `imx_backup.sh`
- OCI Object Storage upload
- `not_uploaded`
- cloud upload logs
- backup created but not_uploaded directory remains
- retry behavior
- rclone vs OCI CLI
- backup archive structure
- restore/upload instructions
- cosmetic vs real upload failure

## Safety model

Default to readonly diagnostics.

Allowed:

- inspect backup logs
- inspect upload logs
- list backup directories
- list `not_uploaded`
- compare expected vs actual uploaded objects
- prepare cleanup recommendation

Not allowed without explicit approval:

- delete backup artifacts
- delete `not_uploaded` content
- rerun upload with mutation
- modify backup script
- change bucket contents
- change retention policy

## Common paths and files

Typical evidence:

```sh
$IMX_TMP/*cloud_upload*.log
$IMX_TMP/*backup*.log
/not_uploaded
not_uploaded
HowToRestore.txt
HowToUpload.txt
```

Backup directory patterns may include date prefixes:

```text
YYYYMMDD_
YYYYMMDD__cloud_upload.log
```

## OCI CLI upload behavior

When diagnosing OCI CLI bulk upload logs, inspect:

```json
{
  "skipped-objects": [],
  "upload-failures": {},
  "uploaded-objects": {}
}
```

Interpretation:

- `upload-failures` empty usually means upload succeeded.
- `uploaded-objects` lists objects uploaded in that run.
- `skipped-objects` may be acceptable if objects already exist and upload mode skips them.
- A leftover local `not_uploaded` directory can be cosmetic if upload success is proven.
- Do not declare success without checking failures and expected object inventory.

## Diagnostic checklist

1. Identify backup run date.
2. Locate backup log.
3. Locate cloud upload log.
4. Check whether backup archive was created.
5. Check `upload-failures`.
6. Check uploaded object count.
7. Check expected object prefix.
8. Inspect `not_uploaded` contents.
9. Decide:
   - real failed upload
   - partial upload
   - retry staging left behind
   - cosmetic leftover
10. Recommend safe next step.

## Useful commands

Use variable-driven commands:

```sh
RUN_DATE="20260422"
BASE_DIR="${IMX_TMP:-/tmp}"
UPLOAD_LOG="${BASE_DIR}/${RUN_DATE}__cloud_upload.log"

ls -ltr "$BASE_DIR" | grep "$RUN_DATE"
cat "$UPLOAD_LOG"
```

With `jq` if available:

```sh
jq '.["upload-failures"]' "$UPLOAD_LOG"
jq '.["uploaded-objects"] | keys | length' "$UPLOAD_LOG"
jq '.["skipped-objects"] | length' "$UPLOAD_LOG"
```

## rclone comparison guidance

Use rclone when the user is evaluating:

- streaming sync
- lower temporary space usage
- retry-friendly sync
- DR copy/sync
- object listing performance with `--fast-list`

Clarify that multipart upload part size does not split the source file permanently; it only chunks transfer.

## Output format

Use:

```text
Verdict:
Evidence:
Upload status:
not_uploaded interpretation:
Risk:
Safe cleanup option:
Recommended script fix:
Commands to verify:
```

## Script fix guidance

If fixing scripts, prefer:

- only move to `not_uploaded` on upload failure
- remove or mark retry staging after confirmed success
- write clear status file
- preserve logs
- avoid deleting data unless retention rules are explicit
- use idempotent retry behavior

## Final response style

Be careful with data-loss risk.

Never recommend deletion without a verified backup/upload success and explicit user approval.

