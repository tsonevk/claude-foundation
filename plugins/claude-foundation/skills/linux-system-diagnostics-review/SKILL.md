---
name: linux-system-diagnostics-review
description: Review Linux host health, load, memory, processes, logs, and incident-style diagnostics.
disable-model-invocation: true
---

# Linux System Diagnostics Review

## Workflow
1. Confirm host, symptom, and time window.
2. Collect the smallest useful read-only evidence for load/CPU, memory, processes, kernel, timers, packages, and logs.
3. Classify the likely domain and hand off to a narrower service/network/storage/access skill when justified.
4. Preserve evidence and separate confirmed facts from inference.
5. Report the safest next check or bounded fix.

## Safety boundaries
- No destructive remediation or production-impacting action without explicit approval.
- No secrets/private log payloads.
