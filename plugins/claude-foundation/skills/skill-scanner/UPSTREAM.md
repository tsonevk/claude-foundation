# Upstream provenance

This local `skill-scanner` is behaviorally adapted from:

- Repository: `getsentry/skills`
- Upstream path: `skills/skill-scanner/`
- Reviewed repository revision: `24fdb833b9e67670a027e3b482189100a69ff7f9`
- Reviewed `SKILL.md` blob: `29260cd69218761ade855517961ed1c9c8bd49d9`
- Reviewed `scripts/scan_skill.py` blob: `14aaa7b059c659ea5c2719fa266f19641dfd9d3d`
- License: Apache-2.0
- Copyright: 2025 Functional Software, Inc. dba Sentry

## Local changes

The local implementation is intentionally not a byte-for-byte vendor copy.

- Removed the `uv` and PyYAML runtime requirement; scanner uses Python standard library only.
- Scans supported text/script files recursively instead of only immediate `references/` and `scripts/` children.
- Redacts matched secrets before JSON output.
- Keeps scanning read-only; candidate code is never executed by the scanner.
- Keeps deterministic pattern matches separate from agent-level intent review.
- Preserves the local repositories' own skill lifecycle, routing, and safety rules.

The upstream implementation and its documentation remain the authoritative reference for Sentry's version. This local adaptation is maintained independently.
