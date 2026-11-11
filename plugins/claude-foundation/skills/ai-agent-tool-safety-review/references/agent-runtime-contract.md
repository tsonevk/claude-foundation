# Claude Agent Runtime Contract

Use this reference when a Claude workflow moves beyond ordinary direct repository work into recurring/autonomous execution, MCP/tool gateways, isolated writes, or external actions.

## Contract

Define before execution:

1. **Objective and authority**
   - operator and success criteria
   - authoritative project/runtime sources
   - untrusted inputs that must not become instructions

2. **Capability boundary**
   - allowed tools and targets
   - read/write level
   - denied actions
   - input/output validation
   - timeout, retry, or budget limits when relevant

3. **Execution boundary**
   - reasoning only
   - read-only tools
   - isolated workspace/worktree write
   - draft external action
   - explicitly approved external write
   - reviewed low-risk automation

4. **Evidence boundary**
   - use runtime-native events when available
   - preserve enough evidence to identify important tool calls, targets, results, verification, approval state, and outcome
   - never invent run/session/event identifiers that the runtime does not expose

5. **Approval boundary**
   - Claude must not self-approve production mutation, destructive action, deployment, IAM/policy changes, credential/certificate rotation, DB writes/migrations, whole-instance lifecycle actions, privileged host/container mutation, broad shell/SSH execution, or widening its own permissions

6. **Verification and stop policy**
   - objective pass/fail checks where feasible
   - bounded retry count
   - stop/escalate when authorization, evidence, or verification is unclear
   - external disable/rollback path for mutations

## Tool gateway pattern

Prefer:

```text
Claude
  |
  v
Tool / MCP gateway
  |
  +-- authentication
  +-- authorization
  +-- target allowlist
  +-- schema validation
  +-- timeout / rate limit
  +-- output filtering / redaction
  +-- audit evidence
  +-- disable path
  |
  v
Bounded tool
  |
  v
Target system
```

Prefer semantic capabilities such as:

- read pipeline state
- read deployment evidence
- list scoped cloud resources
- read workload events
- read a bounded log source
- validate configuration
- create a draft artifact

Treat generic shell/SSH execution, arbitrary HTTP, generic database interfaces, broad filesystem mutation, admin/IAM mutation, and unrestricted target selection as higher risk.

Prompt text is guidance, not enforcement. Use Claude Code permissions/hooks/tool restrictions plus target-system authorization and policy where deterministic enforcement is possible.

## Isolation rule

A worktree, isolated workspace, container, or dedicated runner may be an execution boundary.

A production host, live cloud tenancy, live cluster, shared runtime, or production database is a live target, not a sandbox.

## Evidence rule

Durable run evidence is justified for recurring automation, external writes, production-adjacent diagnostics, MCP/tool execution with material side effects, or security-sensitive workflows.

Do not create run records for ordinary direct repository edits.
