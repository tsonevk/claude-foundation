---
name: skill-stocktake
description: Audit the Claude Foundation skill catalog for overlap, drift, weak scope, stale assumptions, or missing gaps.
disable-model-invocation: true
---

# Skill Stocktake

## Purpose
Keep the installed skill catalog lean, useful, and easy to route.

## When to use
- The catalog has grown materially.
- Several skills were added or changed.
- The user wants keep/improve/merge/retire decisions.

## When not to use
- One small skill changed.
- A normal repo task is in progress.

## Workflow
1. Derive inventory and routing metadata deterministically first.
2. Compare scope and trigger descriptions.
3. Inspect only collision candidates or stale-looking skills.
4. Identify missing high-value gaps.
5. Recommend keep/improve/merge/retire; do not mutate during the audit.
6. For routing-sensitive edits, update/re-run the repository's eval cases and generated consistency checks.

## Repository-maintenance guidance
- Lexical similarity is only candidate evidence.
- Inspect full scope, action mode, safety boundary, precedence, intentional overlaps, and replacement relationships before a merge/retire recommendation.
- Keep delete, merge, rename, and routing-tier changes as proposals until the user approves the exact change.

## Output contract
- Inventory summary
- Verdict table/shortlist
- High-priority changes
- Gap proposals
- Exact follow-up files/checks for approved edits

## Safety boundaries
- Read-only by default.
- Do not enable/disable/remove skills automatically.
- Do not create project handoff files as part of catalog maintenance.
