# Tool Gateway Pattern

Use this reference when Claude reaches external systems through MCP or another tool gateway.

## Principle

Keep reasoning in the model and enforce authentication, authorization, target scope, schemas, limits, and disable controls in deterministic infrastructure.

## Preferred flow

```text
Claude / agent
      |
      v
tool / MCP gateway
      |
      +-- authentication
      +-- authorization
      +-- target allowlist
      +-- schema validation
      +-- timeout / rate limit
      +-- output filtering / redaction
      +-- audit evidence
      +-- external disable path
      |
      v
bounded semantic tool
      |
      v
target system
```

## Design rules

- Prefer semantic tools over generic shell, SSH, arbitrary HTTP, generic database, or broad admin interfaces.
- Separate read and write capabilities.
- Scope repositories, namespaces, compartments, hosts, clusters, environments, and resource classes outside the model when practical.
- Use typed inputs, allowlists, size limits, and timeouts.
- Keep credentials outside model-visible tool output.
- Record enough runtime-native evidence to reconstruct important actions.
- Preserve a human-controlled revoke/disable path.

## Write pattern

```text
agent -> proposed action -> external approval -> bounded write tool -> verification
```

Prompt text alone is not sufficient enforcement for high-risk capabilities.
