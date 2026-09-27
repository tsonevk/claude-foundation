---
name: agentic-qa-evidence-loop
description: Run a budget-aware post-change QA evidence loop with compact default validation, scenario setup, artifact capture, and pass/fail reporting.
disable-model-invocation: true
---

# Agentic QA Evidence Loop

## Purpose
- Run a bounded post-change QA loop that turns a code change into a repeatable scenario, safe validation commands, minimal evidence, and a clear pass/fail summary.

## When to use
- After a non-trivial code, config, or workflow change.
- When the task needs more than implementation and should end with evidence-backed validation.
- When the repo has project-native validation commands or artifact conventions worth reusing.

## When not to use
- The task is a trivial one-line edit.
- The request is purely exploratory or advisory.
- A stricter project-specific QA, release, or verification contract already governs the exact slice.

## Required inputs
- The changed files or diff summary.
- The repo root and any project-local validation entrypoints.
- Runtime and approval constraints for the target system.
- Any known artifact or docs conventions already used by the repo.

## Codex workflow
1. Inspect changed files first and identify the scope of the change.
2. Classify the change type as CLI, UI, infrastructure, docs, tests, iMX, OCI, Ansible, or container.
3. Pick a QA depth mode before reading more than needed.
4. Read only the files allowed by the chosen depth mode.
5. Prefer existing project validation commands, then choose the smallest safe checks.
6. Prefer Linux, WSL, or GitLab-compatible validation over Windows-only validation.
7. For UI work, prefer Playwright or browser evidence when available and safe.
8. For infrastructure work, prefer dry-run, check mode, mock, plan, or sandbox validation.
9. Create or update a QA scenario under `docs/qa-scenarios/` only when the repo has `docs/` and the depth mode warrants it.
10. Collect evidence under `artifacts/qa/<timestamp>/` only when the repo already uses `artifacts/` and the depth mode warrants it.
11. Summarize the scenario, commands, evidence, pass/fail, risks, and next safe action.
12. If validation fails, propose the smallest safe fix or draft a PR-ready follow-up.

## QA depth modes

### MICRO
- Use for typo-only, comments-only, markdown-only, or tiny config-only changes.
- Do not create a full QA scenario.
- Only provide a 3-5 line validation checklist.
- Do not read unrelated files.

### COMPACT
- Default mode for most tasks.
- Inspect only changed files, directly referenced docs, and directly related tests or validation scripts.
- Create a short QA note in the final answer.
- Do not create large evidence folders unless the repo already has a QA or artifacts convention.
- Run only cheap, targeted validation commands.

### STANDARD
- Use for non-trivial code, infra, Ansible, OCI, Docker, MCP, or UI changes.
- Create or update one focused QA scenario when useful.
- Run project-native validation.
- Collect minimal evidence: command output summary, changed files, pass/fail result, risks, and next safe action.

### DEEP
- Use only when explicitly requested by the user with `QA_DEPTH=deep` or the phrase `run deep QA`.
- May include browser, computer-use, webVNC, or Playwright-style checks when available.
- May collect screenshots, videos, JUnit reports, and larger logs.
- Must still avoid secrets and production-impacting actions.

## Token budget rules
- Never read the whole repository unless the user explicitly requests a full audit.
- Start with `git status --short`, `git diff --name-only`, and `git diff --stat`.
- Prefer changed files over broad discovery.
- Maximum default file reads:
  - MICRO: 3 files
  - COMPACT: 8 files
  - STANDARD: 15 files
  - DEEP: 30 files unless explicitly extended by the user
- Maximum default validation loops:
  - MICRO: 0 auto-fix loops
  - COMPACT: 1 auto-fix loop
  - STANDARD: 1 auto-fix loop
  - DEEP: 2 auto-fix loops
- After the loop limit is reached, stop and report the remaining issue instead of continuing.
- Do not generate long prose evidence.
- Do not paste full logs unless the failure requires it.
- Summarize logs and include file paths instead.
- Keep final QA summaries concise and structured.

## Trigger phrases and overrides
- Default behavior: use COMPACT unless the task is clearly tiny or clearly risky.
- Force MICRO with `QA_DEPTH=micro`.
- Force COMPACT with `QA_DEPTH=compact`.
- Force STANDARD with `QA_DEPTH=standard`.
- Force DEEP with `QA_DEPTH=deep`.
- Disable the QA loop with `QA_SKIP=true`.
- Request validation only with `QA_ONLY=true`.

## Output contract
- What changed.
- QA mode used.
- Commands run.
- Pass/fail status.
- Evidence files or summaries created.
- Risks and untested areas.
- Next safe action.

## Verification
- The scenario matches the changed files and change type.
- The validation commands are project-native or the narrowest safe substitute.
- Evidence is separated from interpretation.
- The response states what passed, what failed, and what still needs confirmation.

## Safety boundaries
- No production changes.
- No real OCI mutation unless explicitly requested.
- No iMX whole-instance stop, restart, or shutdown.
- No secret, token, or certificate exposure.
- No automatic merge to `main` or `master`.
- No browser actions involving banking, broker trading, or sensitive personal accounts.
- All destructive actions require explicit human confirmation.
- Use Playwright or browser validation only when available and safe.
- Use Codex Computer Use only when it is available and allowed.
- Use webVNC or crabbox-style remote evidence runners only as future optional integrations.
- Use MCP tools only through approved configured servers.

## Related skills
- `verification-loop`
- `search-first`
- `safe-change-implementation`
- `ai-output-evaluation-review`
- `ci-cd-pipeline-builder`
- `gitlab-mr-security-validation`

## Source attribution
- Adapted from local verification, search-first, QA review, and evidence-handling patterns in the shared catalog.
- No exact upstream match.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- Before large tasks, create or update `docs/activeContext.md`, `docs/currentTask.md`, and `docs/decision-log.md`.
- For repo work, obey `AGENTS.md` first.
- For iMX work, use iMX-native ksh and Oracle context; avoid generic `sudo` or `systemctl` guidance; whole-instance stop requires explicit reconfirmation.
- For OCI diagnostics, default to read-only evidence collection and deterministic reporting.
- For MCP repos, registry, config, policy files, and tests are authoritative; skills are only guidance.
- Do not promise hidden async work or detached execution.
- No open-ended shell access.
- No secrets handling beyond detection and redaction guidance.
- No self-remediation outside an explicit, scoped approval.
