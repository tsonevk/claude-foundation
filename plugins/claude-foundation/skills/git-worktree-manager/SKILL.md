---
name: git-worktree-manager
description: Use git worktrees for isolated parallel work without branch collisions or dirty-state confusion.
disable-model-invocation: true
---

# Git Worktree Manager

## Workflow
1. Confirm base branch, repository state, task slice, and target path.
2. Create a dedicated worktree only when isolation or parallelism has real value.
3. Keep each worktree on its own branch/scope.
4. Avoid touching the main checkout when isolation is the reason for using a worktree.
5. Remove the worktree after the slice is safely integrated or abandoned.

## Output contract
- Base branch
- Worktree path/branch
- Purpose
- Cleanup expectation
- Safety notes

## Safety boundaries
- Do not use worktrees to hide unrelated edits.
- Do not create them for routine single-slice work.
- No branch deletion, reset, or push without explicit authorization where required.
