---
name: imx-enterprise-app-runtime-review
description: Review iMX enterprise application runtime evidence for Oracle DB, WebLogic, Tomcat, and HTTPD without changing state.
---

# iMX Enterprise Application Runtime Review

## Workflow
1. Read iMX/project authority and identify the exact layer: Oracle DB, WebLogic, Tomcat, HTTPD, or their integration path.
2. Inspect existing configuration, process/status evidence, logs, listeners, and dependencies read-only.
3. Trace the request/runtime path instead of assuming generic service names or paths.
4. Separate confirmed evidence from likely application, middleware, DB, or network causes.
5. Recommend the narrowest next diagnostic or config change.

## Output contract
- Runtime layer/scope
- Evidence reviewed
- Findings and remaining unknowns
- Next safe action
- Validation/rollback for any proposed edit

## Safety boundaries
- iMX/Oracle-native context only; do not invent paths or lifecycle commands.
- No whole-instance lifecycle action, DB write, or production mutation without explicit approval.
- No secrets/private log payloads.
