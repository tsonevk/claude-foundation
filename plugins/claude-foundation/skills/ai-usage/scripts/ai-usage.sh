#!/usr/bin/env bash
# ai-usage.sh - bounded, pinned ccusage wrapper for the ai-usage skill.
# ---------------------------------------------------------------------------
# Wraps `npx ccusage@<PINNED_VERSION>` with a small, explicit flag surface for
# workstation-local Claude Code / Codex coding-agent usage observability.
#
# Guarantees:
#   - Pinned tool version (never @latest).
#   - No global npm install (uses `npx`, downloads to the npx cache only).
#   - No secrets, no home-directory-specific committed path.
#   - No production/runtime dependency; local developer observability only.
#   - No auto-upload, no auto-commit of usage reports or history.
#   - No arbitrary shell passthrough: only a fixed, documented flag set is
#     accepted and forwarded as argv (never through eval/sh -c).
#   - Fails safely with a clear, actionable message when Node.js is missing.
#   - POSIX/Linux-compatible: no hardcoded Windows paths, tools resolved
#     from PATH only.
#
# Usage:
#   ai-usage.sh --source claude|codex --report daily|weekly|monthly [--json]
#               [--instances] [-h|--help]
#
# Examples:
#   ai-usage.sh --source claude --report daily
#   ai-usage.sh --source claude --report daily --instances
#   ai-usage.sh --source codex  --report daily
#   ai-usage.sh --source claude --report monthly --json
# ---------------------------------------------------------------------------
set -euo pipefail

PINNED_VERSION="20.0.19"
PROG="$(basename "$0")"

SOURCE=""
REPORT=""
JSON="0"
INSTANCES="0"

usage() {
  cat <<EOF
$PROG - bounded ccusage wrapper (pinned ccusage@${PINNED_VERSION})

Usage: $PROG --source claude|codex --report daily|weekly|monthly [options]

Options:
  --source claude|codex   coding agent whose local usage records to read
                           (required)
  --report daily|weekly|monthly   report time grain (required)
  --json                   emit machine-readable JSON instead of a table
  --instances               per-project/instance breakdown (Claude Code only)
  -h, --help                show this help and exit

This is workstation-local developer observability only: it reads local
coding-agent session logs already on this machine and reports estimated
token usage / cost. It is NOT project governance, application telemetry,
a billing authority, or production monitoring. Codex usage requires local
Codex CLI session logs to already exist on this machine and is documented
upstream as an experimental data source. Figures are estimates, not
authoritative provider invoices. Reports are never committed or uploaded
by this wrapper.
EOF
}

while [ $# -gt 0 ]; do
  case "$1" in
    --source) SOURCE="${2:-}"; shift 2 ;;
    --report) REPORT="${2:-}"; shift 2 ;;
    --json) JSON="1"; shift ;;
    --instances) INSTANCES="1"; shift ;;
    -h|--help) usage; exit 0 ;;
    *)
      echo "ERROR: unrecognized argument '$1'" >&2
      echo "This wrapper accepts a fixed flag set only (no arbitrary passthrough)." >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [ -z "$SOURCE" ] || [ -z "$REPORT" ]; then
  echo "ERROR: --source and --report are both required." >&2
  usage >&2
  exit 1
fi

case "$SOURCE" in
  claude|codex) ;;
  *)
    echo "ERROR: --source must be 'claude' or 'codex' (got '$SOURCE')" >&2
    exit 1
    ;;
esac

case "$REPORT" in
  daily|weekly|monthly) ;;
  *)
    echo "ERROR: --report must be one of daily|weekly|monthly (got '$REPORT')" >&2
    exit 1
    ;;
esac

if [ "$INSTANCES" = "1" ] && [ "$SOURCE" != "claude" ]; then
  echo "ERROR: --instances is only supported for --source claude." >&2
  exit 1
fi

if ! command -v node >/dev/null 2>&1; then
  echo "ERROR: Node.js was not found on PATH. ai-usage.sh requires Node.js to run" >&2
  echo "        'npx ccusage@${PINNED_VERSION}'. Install Node.js and retry." >&2
  exit 1
fi

if ! command -v npx >/dev/null 2>&1; then
  echo "ERROR: npx was not found on PATH (expected alongside a Node.js install)." >&2
  exit 1
fi

if [ "$SOURCE" = "codex" ]; then
  ARGS=(codex "$REPORT")
else
  ARGS=(claude "$REPORT")
fi

if [ "$INSTANCES" = "1" ]; then
  ARGS+=(--instances)
fi
if [ "$JSON" = "1" ]; then
  ARGS+=(--json)
fi

echo "==> npx --yes ccusage@${PINNED_VERSION} ${ARGS[*]}" >&2
echo "NOTE: figures are local estimates from on-disk session records, not authoritative billing." >&2
exec npx --yes "ccusage@${PINNED_VERSION}" "${ARGS[@]}"
