---
name: container-runtime-diagnostics
description: Diagnose container runtime behavior from logs, mounts, health checks, launch definitions, and host evidence.
---

# Container Runtime Diagnostics

## Workflow
1. Read project authority, container definition/launch path, and only relevant logs/events/health checks.
2. Trace launch input to runtime state.
3. Separate host, image, and orchestration evidence.
4. Isolate the narrowest proven or likely failure point.
5. Propose the next safe diagnostic step or bounded fix.

## Output contract
- Observed failure mode
- Evidence
- Proven vs inferred cause
- Next safe step
- Validation/rollback if a fix is proposed

## Safety boundaries
- Read-only first.
- No destructive cleanup or privileged host action without explicit approval.
- Do not broaden into deployment redesign.
