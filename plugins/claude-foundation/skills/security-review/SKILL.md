---
name: security-review
description: Review code, configs, prompts, or docs for security issues before commit or release.
---

# Security Review

## Workflow
1. Read project security/authority guidance and define the exact changed or requested surface.
2. Review trust boundaries, input validation, authn/authz, secrets, command/file/network access, dependency/supply-chain impact, and unsafe defaults relevant to that surface.
3. Prioritize exploitable or material findings over generic hardening advice.
4. Cite evidence and distinguish confirmed findings from hypotheses.
5. Recommend the smallest verifiable remediation.

## Output contract
- Scope
- Findings ordered by severity
- Evidence
- Remediation
- Validation / residual risk

## Safety boundaries
- Defensive review only.
- No secret exposure or offensive exploitation workflow.
- No production mutation without explicit approval.
