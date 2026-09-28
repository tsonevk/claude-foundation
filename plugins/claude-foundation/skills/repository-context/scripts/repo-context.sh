#!/usr/bin/env bash
# repo-context.sh - bounded, pinned Repomix wrapper for the repository-context skill.
# ---------------------------------------------------------------------------
# Wraps `npx repomix@<PINNED_VERSION>` with a small, explicit flag surface so
# repository context packaging stays reproducible and reviewable.
#
# Guarantees:
#   - Pinned tool version (never @latest).
#   - No global npm install (uses `npx`, downloads to the npx cache only).
#   - No secrets, no home-directory-specific committed path.
#   - No production/runtime dependency.
#   - No auto-upload, no auto-commit (Repomix only ever writes a local file).
#   - No arbitrary shell passthrough: only a fixed, documented flag set is
#     accepted and forwarded as argv (never through eval/sh -c).
#   - Fails safely with a clear, actionable message when Node.js is missing.
#   - POSIX/Linux-compatible: no hardcoded Windows paths, tools resolved
#     from PATH only.
#
# Usage:
#   repo-context.sh [--mode full|compress] [--include GLOB] [--ignore GLOB]
#                    [--style xml|markdown|json|plain] [--output PATH]
#                    [--no-security-check] [--dir PATH] [-h|--help]
#
# Examples:
#   repo-context.sh --mode compress --dir . --output /tmp/context.md
#   repo-context.sh --mode full --include "src/**" --ignore "**/*.test.*" \
#                    --output /tmp/context.xml
# ---------------------------------------------------------------------------
set -euo pipefail

PINNED_VERSION="1.18.0"
PROG="$(basename "$0")"

MODE="compress"
INCLUDE=""
IGNORE=""
STYLE="xml"
OUTPUT=""
NO_SECURITY_CHECK="0"
TARGET_DIR="."

usage() {
  cat <<EOF
$PROG - bounded Repomix wrapper (pinned repomix@${PINNED_VERSION}, requires Node.js >= 22)

Usage: $PROG [options]

Options:
  --mode full|compress     full = complete file contents (default: compress)
                           compress = Tree-sitter signature-only extraction
  --include GLOB           glob of files to include (repeatable-safe: pass a
                            comma-separated list, e.g. "src/**,docs/**")
  --ignore GLOB             glob of files to exclude, same comma-separated form
  --style xml|markdown|json|plain   output style (default: xml)
  --output PATH             local output file path (default: repomix-output.<ext>
                             in the current directory; never a git-tracked path
                             you did not choose explicitly)
  --no-security-check       disable Repomix's built-in Secretlint-backed check.
                             Only use this after you have verified project
                             exclusions cover sensitive material yourself.
  --dir PATH                repository directory to pack (default: .)
  -h, --help                 show this help and exit

This wrapper never packages a fixed deny-list of sensitive paths regardless of
other flags: .env, .env.*, credentials, tokens, *.pem/*.key/*.p12/*.pfx,
id_rsa/id_ed25519, ~/.aws, ~/.oci, ~/.kube, *.tfstate*, ansible vault files,
databases, logs, and prior repomix-output artifacts.
EOF
}

FIXED_IGNORE="**/.env,**/.env.*,**/*credentials*,**/*.pem,**/*.key,**/*.p12,**/*.pfx,**/id_rsa,**/id_ed25519,**/.aws/**,**/.oci/**,**/.kube/**,**/*.tfstate*,**/*.tfstate,**/vault.yml,**/*.log,**/repomix-output.*"

while [ $# -gt 0 ]; do
  case "$1" in
    --mode) MODE="${2:-}"; shift 2 ;;
    --include) INCLUDE="${2:-}"; shift 2 ;;
    --ignore) IGNORE="${2:-}"; shift 2 ;;
    --style) STYLE="${2:-}"; shift 2 ;;
    --output) OUTPUT="${2:-}"; shift 2 ;;
    --no-security-check) NO_SECURITY_CHECK="1"; shift ;;
    --dir) TARGET_DIR="${2:-}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *)
      echo "ERROR: unrecognized argument '$1'" >&2
      echo "This wrapper accepts a fixed flag set only (no arbitrary passthrough)." >&2
      usage >&2
      exit 1
      ;;
  esac
done

case "$MODE" in
  full|compress) ;;
  *)
    echo "ERROR: --mode must be 'full' or 'compress' (got '$MODE')" >&2
    exit 1
    ;;
esac

case "$STYLE" in
  xml|markdown|json|plain) ;;
  *)
    echo "ERROR: --style must be one of xml|markdown|json|plain (got '$STYLE')" >&2
    exit 1
    ;;
esac

if ! command -v node >/dev/null 2>&1; then
  echo "ERROR: Node.js was not found on PATH. repo-context.sh requires Node.js >= 22" >&2
  echo "        to run 'npx repomix@${PINNED_VERSION}'. Install Node.js and retry." >&2
  exit 1
fi

if ! command -v npx >/dev/null 2>&1; then
  echo "ERROR: npx was not found on PATH (expected alongside a Node.js >= 22 install)." >&2
  exit 1
fi

ARGS=(--style "$STYLE")
if [ "$MODE" = "compress" ]; then
  ARGS+=(--compress)
fi
if [ -n "$INCLUDE" ]; then
  ARGS+=(--include "$INCLUDE")
fi

COMBINED_IGNORE="$FIXED_IGNORE"
if [ -n "$IGNORE" ]; then
  COMBINED_IGNORE="${FIXED_IGNORE},${IGNORE}"
fi
ARGS+=(--ignore "$COMBINED_IGNORE")

if [ -n "$OUTPUT" ]; then
  ARGS+=(--output "$OUTPUT")
fi
if [ "$NO_SECURITY_CHECK" = "1" ]; then
  ARGS+=(--no-security-check)
  echo "WARNING: --no-security-check disables Repomix's Secretlint-backed scan." >&2
  echo "         Confirm project exclusions cover sensitive material yourself." >&2
fi

echo "==> npx --yes repomix@${PINNED_VERSION} ${ARGS[*]} \"${TARGET_DIR}\"" >&2
exec npx --yes "repomix@${PINNED_VERSION}" "${ARGS[@]}" "$TARGET_DIR"
