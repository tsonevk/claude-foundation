---
name: context-budget-audit
description: Use when Claude Code sessions feel bloated and you want to audit global/project instructions, routing skills, subagent use, and tool-output patterns for avoidable context overhead.
---

# Context Budget Audit

## Purpose
Reduce context, latency, and token waste without reducing correctness or safety.

## When to use
- Sessions become long, repetitive, or slow.
- Claude repeatedly rereads the same repository areas.
- Many routing/meta skills are eligible at once.
- Subagents or large tool outputs are used more often than the task requires.
- The user explicitly asks for context, token, latency, or routing-efficiency review.

## Do not use
- For a normal scoped code/config task.
- When the issue is clearly a code bug rather than harness overhead.
- As an automatic preflight on every session.

## Audit targets
- `~/.claude/CLAUDE.md`
- `~/.claude/settings.json`
- `claude-foundation/plugins/claude-foundation/skill-metadata.json`
- routing-tier skill descriptions and overlapping triggers
- project `CLAUDE.md` / `AGENTS.md` and compact handoff files when relevant
- repeated broad searches, repository rereads, subagent fan-out, Repomix use, and oversized tool output

## Workflow
1. Measure deterministic facts first: routing count, description sizes, repeated trigger overlap, and obvious duplicated guidance.
2. Review only the highest-cost instruction/routing candidates.
3. Identify unnecessary rereads, meta-routing, fan-out, or context packaging.
4. Prefer smaller trigger descriptions, direct-work defaults, and on-demand catalog skills.
5. Do not reduce validation, evidence, security boundaries, or project authority merely to save tokens.

## Output contract
- Summary
- Heaviest context/routing components
- Overlap findings
- Top 3 practical savings
- Proposed skill changes for human review
- Proposed global/project instruction changes for human review

## Safety boundaries
- Read-only by default.
- Do not disable or remove skills automatically.
- Do not optimize cost by dropping required evidence or safety checks.
