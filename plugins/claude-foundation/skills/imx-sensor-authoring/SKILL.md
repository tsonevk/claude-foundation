---
name: imx-sensor-authoring
description: Use this skill when creating, reviewing, or improving iMX sysadm sensors, including ksh scripts, metadata blocks, enable hooks, schedules, recipients, exit codes, and runtime logs.
disable-model-invocation: true
---

# iMX Sensor Authoring

## Purpose

Use this skill to create or improve iMX sensors in the standard sysadm sensor framework.

Use it when the user asks to:

- create a new sensor
- review a sensor
- add metadata to a sensor
- add enable/disable handling
- prepare sensor rollout instructions
- convert an operational check into a sensor
- align a sensor with iMX conventions

## Default language and style

- Use English for code, comments, metadata, and documentation intended for repositories.
- Use `ksh` for sensor scripts unless the repository uses a different shell convention.
- Keep scripts bounded, readable, and operator-friendly.
- Do not use Bash-only features unless explicitly allowed.

## Standard locations

Sensor scripts:

```sh
$IMX_HOME/sysadm/sensors
```

Sensor configs:

```sh
$IMX_CLT/config/sysadm/sensors
```

Runtime enable/disable marker:

```sh
$IMX_SCRIPT/sysadm/sensors/<sensor_name>.enabled
```

Logs:

```sh
$IMX_TMP
```

## Standard exit codes

Use these exit codes consistently:

```text
0   OK
1   ERROR / alert condition
114 SKIPPED / not applicable / disabled / missing prerequisite
```

Do not invent additional exit codes unless an existing repo convention requires them.

## Sensor metadata block

Each new sensor should include a clear metadata block near the top.

Template:

```ksh
# SENSOR_NAME="<sensor_name>"
# SENSOR_DESCRIPTION="<short operational description>"
# SENSOR_DEFAULT_SCHEDULE="<schedule_key>"
# SENSOR_DEFAULT_RECIPIENTS="<recipient_group_or_email>"
# SENSOR_EXIT_OK=0
# SENSOR_EXIT_ERROR=1
# SENSOR_EXIT_SKIPPED=114
# SENSOR_OWNER="sysadm"
# SENSOR_MODE="readonly"
```

Use schedule keys that match the existing schedule matrix when available, for example:

```text
hourly
daily
weekly
monthly
```

## Script structure

Preferred structure:

```ksh
#!/bin/ksh

SENSOR_NAME="<sensor_name>"
LOG_FILE="${IMX_TMP}/${SENSOR_NAME}_$(date +%Y%m%d_%H%M%S).log"

print_msg() {
  print -- "$(date '+%Y-%m-%d %H:%M:%S') [$SENSOR_NAME] $*"
}

finish_ok() {
  print_msg "OK: $*"
  exit 0
}

finish_error() {
  print_msg "ERROR: $*"
  exit 1
}

finish_skipped() {
  print_msg "SKIPPED: $*"
  exit 114
}

# prerequisite checks
# bounded readonly checks
# summary
```

## Authoring rules

Do:

- check prerequisites explicitly
- write useful logs to `$IMX_TMP`
- keep checks readonly
- quote variables
- use bounded command paths or existing iMX helpers where available
- return clear status
- include exact evidence in output
- make the sensor safe to run repeatedly

Avoid:

- deleting files
- changing configs
- restarting services
- killing processes
- relying on interactive input
- hardcoding client-specific paths when variables exist
- silent failures
- generic shell execution
- unbounded `find /`
- noisy output without summary

## Output format

Sensor output should include:

```text
Sensor:
Status:
Evidence:
Details:
Log:
```

## Promotion checklist

Before marking a sensor runnable:

- syntax check if possible
- verify required variables
- verify exit codes
- verify log file path
- verify no mutation commands
- verify no hardcoded environment-specific paths
- verify metadata block
- verify enable marker behavior if implemented
- add rollout notes if needed

## Typical sensors

Examples of sensor types:

- filesystem
- paging
- forms
- batches
- doc_server
- mail_in
- mail_out
- extranet
- foreign_key_missing_index
- java_certs_extranet
- applsign_cert_check

## Final response style

When asked to create a sensor, provide:

1. exact script
2. install path
3. enable/disable command
4. test command
5. expected output
6. rollback/removal step

Keep code comments in English.

