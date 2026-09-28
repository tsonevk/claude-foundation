---
name: session-skill-harvester
description: Scan the current session for reusable patterns, workflows, and non-obvious knowledge that could become skills. Always ends with a yes/no recommendation on whether to create a new skill. Use after any substantive session, or when the user asks "anything to add as a skill?", "skill suggestions", "harvest skills".
disable-model-invocation: true
---

# Session Skill Harvester

## Purpose

Scan the current conversation for knowledge worth capturing as a reusable skill.
Always produce a concrete recommendation — YES (with a draft name + scope) or NO.

## What qualifies as a skill candidate

A good candidate is knowledge that:

- Required trial and error or non-obvious discovery to produce
- Is NOT derivable from reading the project README or official docs
- Would save a future agent time if it didn't have to re-derive it
- Is **repeatable**: the same workflow will likely occur again
- Is **scoped**: can be described in one sentence and fits in one SKILL.md

Reject a candidate if:
- It is already covered by an existing `claude-foundation:*` skill (check by name and description)
- It is one-time migration/rename work with no recurring application
- It is purely project-specific (belongs in a project `CLAUDE.md`, not a global skill)
- It is already documented in official Claude Code / tool docs

## Scan process

1. **Identify repeated manual steps** — anything the user had to explain, correct, or repeat across the session
2. **Identify non-obvious discoveries** — gotchas, silent failures, missing-from-docs behavior, field combinations that don't work
3. **Identify new workflows** — multi-step procedures that were assembled from scratch and will recur
4. **Check against existing skills** — list the existing `claude-foundation:*` skills and discard any candidate that is already covered
5. **Score each candidate**:
   - HIGH: non-obvious + recurring + not in docs + generalizable beyond this repo
   - MEDIUM: useful but narrower scope or partially covered elsewhere
   - LOW: interesting but one-off or too project-specific

## Output format

```
## Skill harvest — [session topic]

### Candidates

| # | Name (proposed) | What it captures | Score |
|---|----------------|-----------------|-------|
| 1 | `some-skill-name` | One sentence | HIGH / MEDIUM / LOW |
| 2 | `another-skill` | One sentence | MEDIUM |

### Recommendation

**YES** — create [skill-name]: [one sentence on what gap it fills and why it qualifies]

  OR

**NO** — nothing new to extract: [one sentence why — already covered / too narrow / one-off]

---
> Is there anything from this session that could be added as a skill, or not?
```

Always end with the `> Is there anything...` line verbatim — even when the answer is NO.

## Rules

- Maximum 3 candidates per scan. If more qualify, pick the 3 highest-scored.
- Do not suggest skills that duplicate `harness-driven-coding`, `eight-rule-architecture`,
  `verification-loop`, `search-first`, `claude-plugin-authoring`, `claude-code-settings-hardening`,
  or other meta-workflow skills already in the plugin unless the new one is meaningfully narrower.
- If the session produced zero qualifying candidates, output the NO branch and still end with the question.
- Keep the recommendation to 1–2 sentences. This is a triage output, not a design doc.
- If the user says YES to a candidate, proceed to write the SKILL.md using `claude-foundation:claude-plugin-authoring` as the authoring guide.
