# Upstream provenance

- Source repository: `getsentry/skills`
- Source skill: `skills/code-simplifier/SKILL.md`
- Reviewed upstream revision: `24fdb833b9e67670a027e3b482189100a69ff7f9`
- Reviewed upstream blob: `a8c66eb86aa4902814a28192055acef2322257f9`
- Adoption model: behaviorally adapted, not copied verbatim
- Local intent: language-neutral, bounded simplification that follows project `CLAUDE.md` / `AGENTS.md` and preserves operational/security semantics
- Reviewed: 2026-08-19

## Local adaptations

The local version intentionally removes Sentry- and frontend-specific style preferences. It does not impose React/TypeScript conventions on Python, shell, infrastructure, Java, or other repositories. It narrows default scope to recently changed or explicitly requested code and treats APIs, schemas, deployment behavior, permissions, security boundaries, observability, and rollback semantics as invariants unless explicitly changed by the user.
