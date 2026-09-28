---
name: skill-bank-router
description: Route ambiguous tasks to the installed Claude Foundation catalog when the visible routing skills do not clearly fit, without loading the full skill library into every session.
---

# Skill Bank Router

## Purpose
Preserve discoverability of catalog-tier skills without external skill banks or permanent context cost.

## When to use
- The task is broad/ambiguous/cross-domain and no routing-tier skill clearly fits.
- A specialized installed skill may exist but is not visible in the normal routing set.

## When not to use
- A routing-tier skill already clearly matches.
- The task is a clear scoped edit.
- The user explicitly named the correct skill.

## Required inputs
- User task
- Current routing candidates
- `skills/skill-index/CATALOG.md` from this plugin, loaded only when needed

## Workflow
1. Check visible routing skills first.
2. Only if no clear match exists, read the generated `skill-index/CATALOG.md` on demand.
3. Select at most 1-3 catalog candidates.
4. Prefer the most specific installed skill; do not invent or promote a new skill when an existing one fits.
5. **Check each candidate's routing classification before doing anything else with it** — `CATALOG.md` marks every catalog entry `[C:AUTO]` or `[C:MANUAL]` (from `tiers.manual_only` in `skill-metadata.json`):
   - `[C:AUTO]` (CATALOG_AUTO, the default): load that skill's own `SKILL.md` and apply it as **router-selected guidance** for the matching prompt. This is our own catalog-routing mechanism, not native Claude Code Skill invocation — `disable-model-invocation: true` still applies and is unrelated to this decision.
   - `[C:MANUAL]` (MANUAL_ONLY): do **not** load or apply its `SKILL.md` as an automatic action. Tell the user which explicit invocation (`/claude-foundation:<name>`) or workflow gate is required instead, and stop there. Never use "I can just read the file" as a way around this — a manual-only classification exists specifically so a destructive/production/shared-state workflow is never applied without the user explicitly asking for it by name.
6. Load only the selected skill body, not the entire catalog.
7. Return the recommended route, its classification, and why.

## Output contract
- Short routing recommendation
- The candidate's `CATALOG_AUTO`/`MANUAL_ONLY` classification
- Up to 3 candidates when needed
- Recommended next step (auto-apply, or the explicit action the user must request)

## Safety boundaries
- Catalog-tier skills are installed guidance, not stronger authority than project files.
- Do not bulk-load the catalog or many skill bodies into context.
- Do not auto-promote, merge, delete, or enable skills.
- Do not auto-apply a `MANUAL_ONLY` skill's guidance under any framing, including a request phrased as an explicit imperative ("deploy X now") — that names the *action*, not an invocation of *this router* bypassing the skill's own manual gate; surface the required explicit step instead.
- Never treat "reading a file's contents" as a loophole around a `MANUAL_ONLY` classification.
