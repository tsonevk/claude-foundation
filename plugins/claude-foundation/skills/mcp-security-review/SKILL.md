---
name: mcp-security-review
description: Review MCP server and connector exposure, permissions, and tool boundaries.
disable-model-invocation: true
---

# MCP Security Review

## Workflow
1. Read authoritative MCP server/tool registry, schemas, auth model, transport config, and tests.
2. Map each tool to data accessed, side effects, permission scope, validation, and auditability.
3. Check prompt/tool injection boundaries, untrusted inputs, secret exposure, overbroad filesystem/network/shell access, and external writes.
4. Prefer deny-by-default, typed inputs, narrow outputs, and explicit approval gates.
5. Recommend the smallest verifiable control improvement.

## Safety boundaries
- No secret material in prompts/logs.
- No permission widening or external mutation without explicit approval.
