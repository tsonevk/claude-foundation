---
name: mcp-server-patterns
description: Use authoritative MCP config, registry, and transport patterns for server and client work.
disable-model-invocation: true
---

# MCP Server Patterns

## Workflow
1. Read the repository's MCP registry/config/schema/tests first; they are authoritative.
2. Keep tool descriptions mutually distinguishable and input/output schemas explicit.
3. Separate protocol/transport errors from tool-execution errors.
4. Make side effects, idempotency, permissions, limits, and approval requirements explicit per tool.
5. Prefer small typed tools over broad shell-like capabilities.
6. Validate with repository-native schema/tests.
