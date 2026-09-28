---
name: imx-sensor-enable-hook-audit
description: Use when an iMX sensor is unexpectedly reported as DISABLED and you need to audit the enable/disable path, especially `.enabled` hooks, lock files, sensor-specific disable flags, and config-to-env gaps before proposing the smallest safe operational fix.
disable-model-invocation: true
---

Audit iMX sensor enable-hook behavior and explain exactly why a sensor is disabled before changing anything.

## Use This Skill When
- A command such as `sensors <name>` returns `Check enabled [ DISABLED ]` unexpectedly.
- The issue is likely in `sensors.sl`, `${IMX_SCRIPT}/sysadm/sensors/<sensor>.enabled`, or `${IMX_CLT}/lock/sensor_<sensor>.disabled`.
- A sensor should be enabled by default, but runtime variables or config export behavior may be preventing that.
- You need a minimal operational fix with explicit verification and rollback.

## Do Not Use This Skill When
- The sensor is enabled and failing its real checks; then debug the sensor logic itself.
- The problem is generic Linux service monitoring unrelated to iMX sensor flow.
- The user wants a broad redesign of sensor architecture instead of a bounded audit.

## Workflow
1. Reproduce the issue on the target host with the exact operator command.
2. Confirm the runtime context:
   - `IMX_SYSADM`
   - `IMX_CLT`
   - `IMX_SCRIPT`
   - sensor wrapper path such as `type sensors` or `whence sensors`
3. Inspect the sensor file and the shared sourced logic:
   - `${IMX_SYSADM}/sensors/<sensor>`
   - `${IMX_SYSADM}/sensors/sensors.sl`
4. Check the standard disable paths first:
   - `${IMX_CLT}/lock/init.lock`
   - `${IMX_CLT}/lock/shutdown_iMX.lock`
   - `${IMX_CLT}/lock/Stopped_for_maintenance.lock`
   - `${IMX_CLT}/lock/sh_bkg.disable`
   - `${IMX_CLT}/lock/sensor_<sensor>.disabled`
5. Inspect the enable hook if present:
   - `${IMX_SCRIPT}/sysadm/sensors/<sensor>.enabled`
6. Compare what the hook expects against what the runtime actually exports.
7. If the root cause is still unclear, run a shell trace on the sensor and identify the exact line that sets `DISABLED=TRUE` or exits with `114`.
8. Propose the smallest safe fix:
   - host-local config change
   - host-local hook change
   - repo patch only if the source-of-truth is actually in the repository
9. Verify with the real sensor command and report whether the sensor is now enabled and what its real status becomes.

## Key Audit Questions
- Is the sensor disabled by a global lock path or by a sensor-specific hook?
- Does the `.enabled` hook exist and return non-zero?
- Is the hook expecting an environment variable that is unset?
- Is the variable present only in a config file but not exported to the child hook process?
- Is the current behavior host-specific runtime drift or a repo source-of-truth problem?

## Command Pattern
Prefer exact host-local commands and keep them copy-paste ready.

Common checks:
```sh
ssh bron@bron 'ksh -lc "sensors filesystem"'
ssh bron@bron 'ksh -lc "type sensors 2>/dev/null || whence sensors 2>/dev/null || command -v sensors"'
ssh bron@bron 'ksh -lc "sed -n \"1,220p\" $IMX_SYSADM/sensors/filesystem"'
ssh bron@bron 'ksh -lc "sed -n \"1,220p\" $IMX_SYSADM/sensors/sensors.sl"'
ssh bron@bron 'ksh -lc "ls -l $IMX_CLT/lock/sensor_filesystem.disabled $IMX_CLT/lock/init.lock $IMX_CLT/lock/shutdown_iMX.lock $IMX_CLT/lock/Stopped_for_maintenance.lock $IMX_CLT/lock/sh_bkg.disable 2>/dev/null"'
ssh bron@bron 'ksh -lc "ls -l $IMX_SCRIPT/sysadm/sensors/filesystem.enabled; sed -n \"1,220p\" $IMX_SCRIPT/sysadm/sensors/filesystem.enabled"'
ssh bron@bron 'ksh -lc "ksh -x $IMX_SYSADM/sensors/filesystem > /tmp/filesystem_sensor_xtrace.out 2>&1; rc=$?; echo RC=$rc"'
ssh bron@bron 'ksh -lc "grep -n \"DISABLED=TRUE\\|Check enabled\\|status_ko DISABLED\" /tmp/filesystem_sensor_xtrace.out"'
```

## Fix Selection Guidance
- Prefer a host-local config change if the runtime already supports it cleanly.
- Prefer a host-local hook fix if the bug is in the deployed hook behavior.
- Prefer a repo change only when the repository contains the source-of-truth file that generates or deploys the broken hook.
- Avoid broad shared-logic changes in `sensors.sl` unless the issue is clearly systemic across multiple sensors.

## Known Patterns
- `filesystem.enabled` and `sh_pooling_int.enabled` can fall into the same bug class: install defaults say the sensor should default to `TRUE`, but the hook tests only the raw variable and treats unset as disabled.
- For that case, prefer a narrow hook fix that preserves explicit `FALSE` but defaults unset to `TRUE`.

Example patch pattern:
```diff
-execute 3 'test "$SH_POOLING_INT_ENABLED" = "TRUE" ' || RC=1
+execute 3 'test "${SH_POOLING_INT_ENABLED:-TRUE}" = "TRUE" ' || RC=1
```

- `backup.enabled` is different. If a runtime config such as `${IMX_CLT}/config/imx_backup_oci.conf` explicitly exports `BACKUP_SENSOR_ENABLED=` or another non-`TRUE` value, treat that as a config decision first, not as an automatic hook-default bug.
- Before patching a backup hook, verify whether the instance is intentionally leaving backup monitoring disabled because backup is not configured on that host.

## Verification
Always report:
- the exact command used to reproduce
- the exact file and line or condition that caused disable
- the exact command used to verify the fix
- whether the sensor became `ENABLED`
- whether a real underlying `FAILED` state appeared after enablement

## Rollback
Before changing runtime files on a host:
- create a timestamped backup next to the changed file
- keep the rollback command explicit and copy-paste ready

Typical rollback form:
```sh
cp /path/to/file.bak.YYYYMMDDHHMMSS /path/to/file
```

## Output Contract
Always provide:
- summary
- commands
- exact root cause
- target files
- exact changes
- verification
- risks
- rollback

## Quality Bar
- Do not stop at “sensor is disabled”; explain why.
- Distinguish runtime host drift from repository source-of-truth.
- Prefer the smallest reversible fix that restores intended default behavior.
- Call out when enabling the sensor reveals a real operational failure that was previously masked.
