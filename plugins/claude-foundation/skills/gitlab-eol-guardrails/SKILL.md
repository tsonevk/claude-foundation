---
name: gitlab-eol-guardrails
description: Use when a GitLab repository needs LF line-ending guardrails for scripts or config files, especially when Web UI edits or pasted content can introduce CRLF (^M), and when the repo uses a shared CI include for versioning or release jobs.
disable-model-invocation: true
---

# GitLab EOL Guardrails

## Overview

Apply a repo-local line-ending policy and a local GitLab CI validation job that detects `CRLF`, normalizes tracked files to `LF`, pushes a follow-up commit, and stops the stale pipeline so the next pipeline runs on the corrected commit.

Use this skill for repositories that:
- are edited through GitLab Web UI or receive pasted content
- contain shell, Python, Perl, YAML, config, or extensionless operational scripts
- include shared CI templates for versioning or release
- need to avoid `^M` in Unix/Linux files without redesigning the pipeline

## Workflow

1. Inspect the repository first.
   Check:
   - `.gitattributes`
   - `.editorconfig`
   - `.gitlab-ci.yml`
   - top-level script directories
   - current tracked files with `CRLF`

2. Standardize the repo on `LF`.
   Add or update:
   - `.gitattributes` with `text eol=lf` for Unix/Linux file types
   - explicit `text eol=lf` rules for extensionless operational directories
   - Windows-only exceptions for `*.bat`, `*.cmd`, and `*.ps1`
   - binary exclusions where relevant

3. Add `.editorconfig`.
   Use:
   - `end_of_line = lf`
   - `insert_final_newline = true`
   - `trim_trailing_whitespace = true`
   - `crlf` only for Windows-only file types

4. Keep EOL validation local to the consuming repo.
   If the repo includes a shared CI template for versioning or release, add the `validate:eol` job in the repo-local `.gitlab-ci.yml`, not in the shared template, unless all consumers already declare the stage.

5. Add a local `validate` stage and `validate:eol` job.
   The preferred behavior is:
   - scan tracked files for `CRLF`
   - normalize them to `LF`
   - commit and push a follow-up commit to the same branch
   - exit non-zero after push so the old pipeline stops
   - let the next pipeline continue on the corrected commit

6. Preserve current behavior outside line endings.
   Do not redesign the release flow. Keep shared includes intact.

## Preferred CI Pattern

Use a repo-local `validate:eol` job before `version`, `metadata`, or `release`.

Requirements:
- install `git` and `sed`
- configure Git identity in CI
- require `GITLAB_PUSH_TOKEN` with `write_repository`
- push back to `HEAD:${CI_COMMIT_REF_NAME}`

Important behavior:
- Do not try to continue the same pipeline after auto-push.
- The current pipeline is tied to the old commit SHA.
- Push the normalization commit, then stop the current pipeline so a fresh one runs.

## Repo Adaptation Rules

- Match the repository's branch rule such as `main` or `master`.
- Mirror the repo's actual top-level operational directories in `.gitattributes`.
- Keep the shared include unchanged if it already owns version/metadata/release jobs.
- If the current goal is to validate the auto-fix path, do not pre-normalize the known `CRLF` offender before the first test push.

## Validation

After changes:
- parse `.gitlab-ci.yml` as YAML
- inspect `git ls-files --eol` for representative files
- run `git grep -I -l "$(printf '\r')" -- .` to identify current offenders

Expected outcome:
- policy files are in place
- local CI owns `validate:eol`
- next push either passes cleanly or auto-fixes and re-runs on a fresh pipeline

## Rollback

Rollback by reverting:
- `.gitattributes`
- `.editorconfig`
- repo-local `validate:eol` job and `validate` stage in `.gitlab-ci.yml`

Do not change shared CI templates unless the change is safe for every consumer.
