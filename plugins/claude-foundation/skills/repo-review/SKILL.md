---
name: repo-review
description: Review a repository before changing it so you do not duplicate, overwrite, or fight existing structure.
---

# Repo Review

## Purpose
Review enough repository structure to preserve existing architecture before a non-trivial change.

## Use when
- The repository or target area is unfamiliar.
- The requested change could overlap existing structure.

## Do not use when
- The target and local pattern are already known.
- The task is a tiny obvious edit.

## Minimal inspection
- closest `CLAUDE.md` / `AGENTS.md`
- relevant README/context only if needed
- existing target config/source/tests
- recent git status

Stop when the source of truth and smallest change are clear.

## Review questions
- What is authoritative?
- What must be preserved?
- What is the smallest useful change?
- How will it be verified?

## Output contract
- Existing structure found
- Changes made/proposed
- Files changed
- Verification
- Risks/assumptions
