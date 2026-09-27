---
name: bootstrap-ai-native-project
description: Bootstrap or audit a repository's AI-assisted development governance — initialize project conventions, review whether CLAUDE.md/AGENTS.md/rules/skills/hooks are structured correctly, and add an intent/spec/plan/review lifecycle where size and risk justify it. Use when setting up a new project's standard Claude workflow or auditing an existing one for governance drift; not for an ordinary code change in an already-governed repo.
disable-model-invocation: true
---

# Bootstrap AI-native project

## Purpose

Set up, or audit, a repository's AI-assisted development governance: an
intent → spec → plan → implementation → review lifecycle, clear
ownership of "who updates which doc," and a sane split between
always-on instructions, on-demand skills, and deterministic enforcement.

This is a method, not a template to copy verbatim. It carries no
project-specific application, cloud, or infrastructure detail — that
lives in the target repository itself. Never blindly copy another
project's structure (including this plugin's own home repository); only
the shape of the governance process is reusable, not any domain content.

This skill is catalog-tier and carries `disable-model-invocation: true`:
Claude Code itself will not put its description in resident context or
natively auto-invoke it, and `/claude-foundation:bootstrap-ai-native-project`
remains the explicit manual path. Separately, it is classified
`CATALOG_AUTO` in `skill-metadata.json`'s `tiers.manual_only` (absent from
that list = the documented default), which means `skill-bank-router`/
`skill-index` MAY discover it via `CATALOG.md` and load/apply this file as
**router-selected guidance** for a matching prompt — a custom mechanism
this plugin owns, not native Claude Code Skill invocation. That is a safe
default here because this skill only establishes/audits governance and
always preserves explicit human approval for destructive or
production-affecting actions. Do not flip `disable-model-invocation` to
"fix" routing, and do not move this skill to `tiers.manual_only` without a
concrete reason — router-selected guidance is the intended path.

## When to use

- Initializing governance for a repository, or bootstrapping a new
  software project's standard development conventions.
- Setting up a new project using the normal Claude Code workflow, or
  preparing an existing repository for Claude Code.
- Auditing whether `CLAUDE.md`, `AGENTS.md`, `.claude/rules`, skills, or
  hooks are structured correctly, or whether repository instructions and
  documentation are organized the intended way.
- Adding intent/spec/plan governance, or reviewing/fixing documentation
  that can silently go stale.
- "Make this project follow our standard development governance" or
  equivalent asks about project/governance structure itself.

## When not to use

- The repository already has an equivalent, working governance model —
  audit it instead of replacing it (see Inspect first).
- An ordinary code change, bug fix, or feature edit in an
  already-governed repository — this skill is about the governance
  structure itself, not routine development work.
- A single trivial edit needs no governance ceremony at all.

## Inspect first

1. Read whatever the repo already has: `AGENTS.md`, `CLAUDE.md`,
   `README.md`, any current-task/active-context/decision-log-shaped
   files, `.claude/rules/*`, `.claude/skills/*`, `.claude/agents/*`,
   `.claude/settings.json`, `CONTRIBUTING.md`, ADR directories.
2. Determine what already exists functionally, even under a different
   name (a `decisions/` folder instead of `decision-log.md`, `docs/adr/`
   instead of `spec/`). Never create a second source of truth for
   something an existing document already owns.
3. Gauge size/risk: lines of code, contributor count, whether the
   project touches production infrastructure/credentials/user data,
   whether CI already exists, whether lifecycle stages already exist
   informally (issues as intent, PR descriptions as spec).

## Scale to the project

| Signal | Recommended structure |
|---|---|
| Small/trivial (script, prototype, one contributor, no production exposure) | A short "how we work" section in one file. No `intent/`/`spec/`/`plan/`, no `REVIEW.md` — say so explicitly rather than over-building; recommend adding them only if the project grows. |
| Medium (small team, some production exposure, existing CI) | A canonical contract file with safety/architecture invariants; a lightweight `intent/`+`plan/` for non-trivial changes (spec folded into intent); a short `REVIEW.md`; a current-state handoff file. |
| Larger/production-critical (multiple contributors, real security/compliance stakes) | Full `intent/` → `spec/` → `plan/` → `REVIEW.md` chain (below); a documentation-ownership rule; deterministic guardrails for the highest-value invariants; current-task/active-context/decision-log-equivalent handoff files. |

State which tier was assessed and why, so the recommendation is
falsifiable rather than a fixed template.

## The lifecycle (when justified)

`intent → spec → plan → implementation/tests → review → merge/release →
feedback/new intent`

- **intent** (why): problem, desired outcome, affected users/systems,
  constraints, risks/open questions, status/owner.
- **spec** (what): approved behavior, requirements, interfaces/data
  implications, security constraints, edge cases, acceptance criteria,
  unresolved concerns.
- **plan** (how): files/components expected to change, implementation
  order, rejected alternatives where material, risks/blast radius,
  validation/tests, rollback where applicable. If implementation
  diverges materially from an approved plan, update the plan (and spec,
  if approved behavior changed) in the same change.
- **review**: a concise `REVIEW.md` — correctness/regressions, security/
  trust boundaries, compliance with intent/spec/plan when present,
  architectural invariants, test/evidence sufficiency, stale/
  contradictory docs, whether instruction files need synchronization.
  Reference canonical policy sources; do not duplicate them.

Do not create these directories with placeholder/fake content merely to
have them exist — create them when the first real non-trivial change
needs one, with a short README/template per directory. Preserve any
existing current-state handoff file and decision-rationale log: `plan/`
captures intended-how, not current execution state or historical
rationale; those stay in their existing homes.

## Documentation synchronization ownership

For any repository with more than one persistent doc, establish (in one
rule file, not scattered prose):

1. What each document owns (the specific facts it is authoritative for).
2. Whether it's authoritative, derived, historical, operational, or
   temporary.
3. What kind of change makes it stale.
4. Which workflow step is responsible for updating it.
5. Whether staleness is deterministically checkable (a path/reference
   that must resolve, a generated file that must match its generator)
   or requires human/agent judgment.
6. Whether it duplicates or contradicts another document — if so,
   collapse to one authoritative source.

Recommend a deterministic check only when it expresses a real invariant
with low false-positive risk (a generated file must match its source, a
link must resolve). Never recommend timestamp-only or semantic-guessing
checks — they produce more noise than signal.

## Instruction-layer placement

- **Canonical/tool-neutral repo contract** (e.g. `AGENTS.md`): hard
  invariants — safety, architecture, security boundaries — that hold
  regardless of which coding agent is used.
- **Tool-specific adapter** (e.g. `CLAUDE.md`): short, always-on
  operational context for one tool — commands, environment quirks,
  recurring-mistake notes. Must not restate the canonical contract.
- **Modular/path-specific rules** (`.claude/rules/*.md`): scoped
  persistent instructions that would clutter the top-level files.
- **Skills**: repeatable procedures or reference knowledge invoked on
  demand, not needed every session.
- **Subagents**: isolated specialist work only when genuinely useful;
  do not default to broad/nested fan-out.
- **Hooks/permissions**: deterministic enforcement — an actual check —
  not another place to restate policy in prose.

Never move existing content between these layers for aesthetics alone;
move it only when doing so clearly reduces duplication or contradiction
without changing its meaning.

## Deterministic guardrails

Evaluate whether an existing IMPORTANT safety rule is currently prose
that should be enforceable (secrets/`.env` exposure, destructive git
commands, dangerous filesystem deletion, bypassing validation,
production/deployment actions). Recommend a hook/permission only when
the condition is objectively detectable, false positives are
acceptably low, and it will not break existing developer workflows.
Otherwise document the control as "recommended, not implemented" and
say why, rather than adding an LLM-judgment-based hook for a hard
security invariant.

## Tests, evidence, and human gates

Require tests/validation proportional to the project — not a
heavyweight suite on a trivial repo, and not "no tests" for a
production-impacting one. Treat an existing CI gate as authoritative
over local-only validation. Regardless of project size, preserve
explicit human/operator approval for destructive actions, production
deployment, credential rotation, schema/infra changes, and anything
affecting shared state — this skill must never let an agent bypass
those gates by default. Auto-memory (or any equivalent session-recall
feature) must never become a project's source of truth; a repository's
own version-controlled documents always win. Do not require MCP, agent
teams, plugins, subagents, or hooks without a concrete need.

## Output of this skill

1. A short inventory of what already exists and what it functionally
   covers.
2. The recommended tier (small/medium/large) with justification.
3. Only the artifacts justified by that tier — created or proposed, not
   both by default; ask before creating if the repo has active
   maintainers who haven't been consulted.
4. A documentation-ownership table sized to the number of persistent
   docs actually present.
5. Any deterministic guardrail recommended, and any deliberately not
   added, with the reason why.
6. An explicit note of what was intentionally NOT done (e.g. "no
   `intent/`/`spec/`/`plan/` — this repo is small enough that a short
   section covers it; revisit if the team grows").
