---
name: security-scan
description: Do a narrow scan for secrets, risky settings, and exposed attack surface in repo files.
---

# Security Scan

## Workflow
1. Read project security exclusions and define a bounded repository/path scope.
2. Use existing deterministic scanners/checks first; do not install new tools automatically.
3. Inspect only findings/hotspots that justify model review.
4. Never open protected secret files merely because a scanner references them.
5. Report real findings, false-positive uncertainty, and missing coverage separately.

## Output contract
- Scope/tools
- Findings
- False-positive/coverage notes
- Recommended next step

## Safety boundaries
- Read-only by default.
- No secret contents in output.
- No automatic remediation, dependency installation, or production action.
