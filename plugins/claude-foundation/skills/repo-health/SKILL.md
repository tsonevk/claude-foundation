---
name: repo-health
description: Run a periodic, read-only, deterministic-first repository maintainability health check to find growth, churn, complexity hotspots, and development-speed risks without broad LLM scanning or automatic refactoring.
disable-model-invocation: true
---

# Repository Health

## Purpose

Keep growing repositories fast to understand and change.

This skill is a periodic maintainability check, not a normal pre-change step. It uses deterministic
repository metadata first, then spends model context only on the few hotspots that justify inspection.

Core rule:

> Never spend model tokens discovering mechanically what deterministic tools can determine first.

## When to use

Use manually when one or more are true:

- repository work is getting noticeably slower;
- the codebase has grown substantially;
- several major features have landed since the last health review;
- the same modules are repeatedly touched;
- files or functions are becoming difficult to navigate;
- the user explicitly asks for repo health, maintainability, complexity, code growth, or development-speed review.

A reasonable cadence is after roughly 5-10 substantial feature merges, not after every commit.

## Do not use

- for a tiny local edit;
- as an automatic hook on every task;
- as a replacement for normal task-scoped testing;
- as a reason to refactor unrelated code;
- to run Repomix or broad multi-agent review by default.

## Authority

1. Read the closest project `CLAUDE.md` / `AGENTS.md` first.
2. Project-native architecture, tests, validation commands, and operational rules are authoritative.
3. Existing `docs/activeContext.md`, `docs/currentTask.md`, and `docs/decision-log.md` should be used when present.
4. This skill reports health risks; it does not authorize changes.

## Default workflow

### 1. Keep orientation narrow

Read only:

- project governance;
- compact context/handoff files when present;
- package/build/test metadata needed to understand repository type.

Do not read the repository source tree into model context.

### 2. Run deterministic triage first

Run the bundled read-only scanner against the repository root:

```bash
python3 <repo-health-skill-dir>/scripts/repo_health.py --repo . --top 10
```

Use the current Python interpreter on platforms where `python3` is not the command name.

The scanner:

- uses only tracked Git files;
- counts source size without printing source code;
- reports largest source files;
- measures recent Git churn;
- identifies size × churn hotspots;
- performs lightweight Python AST function hotspot detection when Python is present;
- reports optional static-analysis tools already available;
- redacts sensitive-looking tracked paths;
- modifies nothing.

Do not install tools to satisfy this scan.

### 3. Inspect only justified hotspots

After deterministic triage:

- inspect at most the top 1-3 hotspots by default;
- prefer a file that is both large and frequently changed over a merely large stable file;
- inspect immediate callers/tests only when needed to understand the hotspot;
- expand scope only when evidence requires it.

Do not perform full-repository LLM review.

### 4. Use existing analyzers selectively

If the repository already has configured tools, use only those relevant to a reported hotspot.

Examples:

- Python: `ruff`, `radon`, `vulture`, focused `pytest`;
- JavaScript/TypeScript: configured `eslint`, `tsc`, focused test command;
- Terraform: existing formatting/validation/lint commands;
- Ansible: existing `ansible-lint` or syntax checks.

Rules:

- do not install missing analyzers;
- do not run every available analyzer;
- do not run a full slow test suite merely to complete this health review;
- prefer repository-native commands over generic guesses;
- record unavailable checks instead of compensating with broad model reading.

### 5. Separate health findings from refactoring

This skill is read-only by default.

For a real hotspot, recommend one of:

- leave as-is;
- monitor;
- simplify a bounded recently changed area with `code-simplifier`;
- schedule an explicit refactor task;
- improve architecture/context documentation so future sessions navigate faster.

Never refactor automatically.

## Findings to consider

Prioritize evidence for:

- oversized/high-churn modules;
- oversized or branch-heavy functions;
- duplicated implementation patterns confirmed by targeted inspection or existing tooling;
- dead code confirmed by configured tooling or call-site evidence;
- dependency creep;
- repeated repository rediscovery caused by missing architecture/context guidance;
- slow or overly broad validation loops;
- architectural boundaries that force unrelated files to change together.

Do not report style preference as maintainability risk.

## Verdict

Return exactly one primary verdict:

- `HEALTHY` — no meaningful development-speed risk found;
- `WATCH` — growth or hotspots exist but do not justify refactoring yet;
- `REFACTOR_RECOMMENDED` — evidence shows one or more bounded areas are materially increasing change cost;
- `INSUFFICIENT_EVIDENCE` — repository/tool evidence is not enough for a grounded conclusion.

## Output contract

Keep the report short:

1. **Verdict**
2. **Repository signal** — source file/LOC scale and dominant languages
3. **Top hotspots** — maximum 5
4. **Why they matter** — size/churn/complexity evidence
5. **Development-speed risks** — maximum 3
6. **Recommended action** — maximum 3 bounded actions
7. **Do not touch** — areas intentionally left alone
8. **Checks used** — deterministic tools/commands only

Do not paste large source excerpts, full file inventories, or raw analyzer output.

## Token and latency guardrails

- No Repomix by default.
- No broad repository dump.
- No subagent fan-out by default.
- No full-tree source reading by the model.
- No repeated reading of files already summarized in project context.
- No more than 3 hotspot source files opened initially.
- Prefer deterministic summaries over raw logs.
- Stop when evidence is sufficient for the verdict.

## Safety boundaries

- Read-only unless the user separately approves implementation.
- No dependency installation.
- No generated-file cleanup.
- No automatic commits or pushes.
- No production/runtime actions.
- Never print secret contents.
- Respect project-specific must-not-touch paths.

## Related skills

- `search-first` — authoritative task-scoped discovery;
- `repo-intake-scan` — first contact with an unfamiliar repository;
- `codebase-onboarding` — minimal initial repository orientation;
- `repository-context` — bounded Repomix packaging only when repo-wide context is genuinely needed;
- `context-budget-audit` — Claude/Codex harness and instruction-context bloat;
- `code-simplifier` — bounded behavior-preserving simplification after a hotspot is explicitly selected;
- `verification-loop` — validate any later approved implementation.
