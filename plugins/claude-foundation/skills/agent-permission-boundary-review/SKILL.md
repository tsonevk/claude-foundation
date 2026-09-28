---
name: agent-permission-boundary-review
description: Review Claude agent permissions, tool scopes, and data boundaries before deployment or reuse.
disable-model-invocation: true
---

# Agent Permission Boundary Review

## Purpose
Review agent permissions and data/tool boundaries with least privilege and explicit mutation gates.

## When to use
- Designing or reusing a Claude agent with tools or private context.
- Reviewing read/write/shell/cloud/external-action boundaries.

## Workflow
1. Read authoritative project policy and agent/tool definitions.
2. Map tools to purpose, input scope, side effects, and required approval.
3. Prefer read-only and deny-by-default capabilities.
4. Identify overbroad permissions, missing auditability, or unsafe data exposure.
5. Validate the smallest proposed control change.

## Output contract
- Scope and risk tier
- Allowed/denied tools
- Approval gates
- Evidence and findings
- Residual risks
- Next safe action

## Safety boundaries
- Read-only first.
- No production or external mutation without explicit approval.
- No secrets in prompts, logs, scripts, or repositories.
