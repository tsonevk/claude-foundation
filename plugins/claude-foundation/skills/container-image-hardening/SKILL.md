---
name: container-image-hardening
description: Review container image layers, package sets, runtime identity, and provenance controls for hardening opportunities.
---

# Container Image Hardening

## Workflow
1. Read project authority, Dockerfile/build definition, base image, package sources, and CI scan/signing path.
2. Inspect build/runtime separation, packages, user/privileges, secrets, provenance, and unnecessary layers.
3. Prioritize concrete high-impact risks over style preferences.
4. Recommend the smallest behavior-preserving hardening change.
5. Validate with existing build/lint/scan tooling; do not install new tools automatically.

## Output contract
- Evidence reviewed
- Hardening findings
- Minimal recommended change
- Validation
- Residual risk

## Safety boundaries
- No secrets in layers/build args/logs.
- No unnecessary privileges.
- No automatic runtime/deployment mutation.
