---
name: cms-safe-mutation-boundary
description: Use this skill when designing or implementing bounded CMS mutation flows, especially readonly inspect, dry-run plan, explicit approval, precondition checks, approved mutation, audit trail, and rollback notes.
disable-model-invocation: true
---

# CMS Safe Mutation Boundary

## Purpose

Use this skill for CMS or iMX lifecycle changes that cross from readonly inspection into controlled mutation.

Use it when the user asks to:

- add a CMS mutation tool
- set a CMS variable
- deploy config
- compare configs
- create approval gates
- define mutation audit flow
- add dry-run planning before a change
- strengthen safety boundaries

## Core lifecycle

All mutation-class flows should follow this lifecycle:

```text
readonly inspect
→ dry-run plan
→ explicit approval gate
→ precondition validation
→ approved mutation
→ audit record
→ verification
→ rollback/recovery notes
```

Never jump directly from user intent to mutation.

## Action classes

Use explicit action classes:

```text
readonly
dry_run
approved_mutation
```

Each tool/action should clearly declare its action class.

Readonly actions must not mutate state.

Dry-run actions must produce a plan without applying it.

Approved mutations must require explicit approval evidence.

## Mutation approval

Approved mutation requires:

```text
target:
intended value/change:
dry-run plan id or summary:
preconditions:
approval token or explicit user confirmation:
audit destination:
rollback/recovery note:
```

Do not treat vague user intent as approval for a high-impact mutation.

## Preconditions

Before mutation, validate:

- target exists
- current state matches expectation
- requested change is bounded
- user has provided exact target
- dry-run plan matches mutation target
- risk class is acceptable
- rollback/recovery note exists
- audit destination is available

If preconditions fail, return a normal tool error result, not a hidden mutation attempt.

## Audit record

Mutation audit should include:

```text
timestamp_utc:
operator:
tool/action:
target:
before:
requested_after:
actual_after:
dry_run_plan:
approval:
preconditions:
result:
rollback_note:
```

## Output model

For tool-style outputs, prefer:

```json
{
  "action_class": "approved_mutation",
  "target": "...",
  "status": "applied",
  "audit_ref": "...",
  "verification": "...",
  "rollback_note": "..."
}
```

For failures:

```json
{
  "action_class": "approved_mutation",
  "is_error": true,
  "status": "blocked",
  "reason": "...",
  "failed_precondition": "..."
}
```

## Forbidden shortcuts

Do not:

- hide mutation behind a readonly name
- perform mutation during dry-run
- skip approval because the change is "small"
- use generic shell execution for mutation
- broaden allowlists silently
- mutate multiple targets when one was requested
- omit audit records
- omit verification

## Repo implementation guidance

When implementing in code:

- keep handlers bounded
- validate config at startup when applicable
- keep route allowlists explicit
- update registries/contracts together
- add tests for blocked mutation and successful approved mutation
- preserve protocol error boundaries
- use structured tool results for tool-level errors

## Final response style

When proposing a mutation flow, always include:

```text
Readonly inspect:
Dry-run plan:
Approval gate:
Preconditions:
Mutation:
Audit:
Verification:
Rollback:
```

