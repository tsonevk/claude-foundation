---
name: code-simplifier
description: Simplify recently changed or explicitly requested code while preserving behavior, APIs, schemas, deployment semantics, security boundaries, and repository conventions. Use after an implementation or when the user explicitly asks for simplification/refactoring; keep scope bounded and validate after changes.
disable-model-invocation: true
---

# Code Simplifier

Use this skill to reduce unnecessary complexity in a bounded change without changing what the software does.

## Authority

1. Follow the closest project `CLAUDE.md`, `AGENTS.md`, repository documentation, tests, schemas, and existing code conventions.
2. Preserve externally visible behavior unless the user explicitly requests a behavior change.
3. Do not redesign architecture, migrate frameworks/tooling, or broaden scope just because a different design looks cleaner.
4. Keep permissions, security controls, deployment behavior, data formats, APIs, CLI contracts, and operational semantics unchanged.

## Scope

Prefer one of these scopes:

- files changed in the current task or branch;
- code explicitly named by the user;
- the smallest supporting area needed to simplify those changes safely.

Do not sweep unrelated files or perform repository-wide cleanup unless explicitly requested.

## Workflow

1. Read the governing instructions and inspect the current diff or requested code.
2. Identify complexity that is real rather than stylistic preference: duplicated logic, needless indirection, avoidable nesting, dead branches, confusing naming, repeated conditionals, unnecessary wrappers, or over-general abstractions.
3. Establish behavior that must remain invariant from tests, interfaces, schemas, documentation, and call sites.
4. Make the smallest simplification that improves readability or maintainability.
5. Preserve comments that explain non-obvious constraints; remove only comments that became misleading or merely restate obvious code.
6. Run the narrowest relevant validation first, then the repository-required checks for the touched area.
7. Review the resulting diff for accidental scope growth or behavior changes.

## Rules

- Prefer clarity over fewer lines.
- Prefer existing project idioms over generic style advice.
- Do not collapse code if the compact form is harder to debug or operate.
- Do not introduce a new abstraction unless it removes demonstrated duplication or complexity.
- Do not replace explicit domain logic with clever metaprogramming.
- Do not change public names, configuration keys, serialization formats, database schemas, network contracts, exit codes, or error semantics without explicit approval.
- Do not weaken validation, logging, auditability, rollback paths, or security controls for concision.
- For infrastructure code, preserve idempotency, resource identity, lifecycle semantics, and plan/apply behavior.
- For shell/ops code, preserve quoting, exit-status handling, environment assumptions, and failure behavior.
- For Python/JS/Java and other application code, preserve interfaces and observable side effects.

## Stop Conditions

Stop and report instead of simplifying when:

- required behavior is ambiguous;
- simplification would need an API/schema/architecture change;
- tests or authoritative documentation conflict;
- the requested change would remove a security, validation, observability, or rollback safeguard;
- the simplification cannot be validated with available evidence.

## Output

Report concisely:

1. **Simplified:** what changed and why it is simpler.
2. **Behavior preserved:** the key invariants kept unchanged.
3. **Validation:** exact checks run and their result.
4. **Residual complexity:** anything intentionally left as-is and why.
