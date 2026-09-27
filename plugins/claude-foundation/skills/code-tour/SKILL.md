---
name: code-tour
description: Create a guided repository tour from minimal verified context and selected file lines.
disable-model-invocation: true
---

# Code Tour

## Purpose
- Help Codex produce a guided tour of a repository or selected subsystem.
- Keep tours useful for onboarding, handoff, review, and future implementation planning.

## When to use
- The user wants a repository walkthrough, onboarding tour, architecture tour, PR tour, or RCA-style tour.
- A guided narrative would help explain how a subsystem fits together.
- The task needs a structured path through a codebase without broad scanning.

## When not to use
- The user only needs a short summary.
- The repository is already fully familiar.
- The task is a direct implementation or edit request, not a walkthrough.
- The user explicitly wants a full repository audit or exhaustive index.

## Required inputs
- Target repository path or selected subsystem.
- User goal for the tour.
- Observed files and verified line references.
- Any project `AGENTS.md` or local context files that govern the repository.

## Codex workflow
1. Confirm the repo root and read `AGENTS.md` first.
2. Read `README.md` and any `docs/activeContext.md`, `docs/currentTask.md`, or `docs/decision-log.md` files if present.
3. Inspect only the minimum package, build, or test metadata needed to orient the tour.
4. Read targeted files that support the story.
5. Verify file paths and line numbers before using them.
6. Separate observed facts from architectural inference and from uncertainty.
7. Produce a tour that follows a clear narrative from orientation to core path to closing.

## Output contract
- Short tour title and audience.
- Observed files and verified anchors.
- High-level architecture or flow, clearly labeled as inferred when needed.
- Risks, assumptions, and uncertainty.
- Suggested next reading or next step.
- No file edits during tour creation.

## Verification
- All cited file paths exist.
- All cited line numbers were verified from the file contents.
- The tour starts from real repository context, not guesses.
- The output distinguishes observed facts from inference.

## Safety boundaries
- Do not scan the whole repository by default.
- Do not modify files while producing the tour.
- Do not infer authority from docs alone.
- Do not fabricate file paths, line numbers, or architecture.
- Do not treat the tour as a runtime contract.

## Related skills
- `codebase-onboarding`
- `repo-intake-scan`
- `documentation-lookup`
- `verification-loop`
- `search-first`

## Source attribution
- Adapted from the upstream `claude-skills` `code-tour` skill.
- Rewritten for Codex to emphasize minimal verified reading and narrative repository tours.

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
