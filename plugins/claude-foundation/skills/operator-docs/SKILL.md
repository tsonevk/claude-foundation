---
name: operator-docs
description: Write or simplify short, clear operator-facing installation guides, runbooks, Wiki/MediaWiki pages and README procedures. Use automatically for documentation creation and rewrites, not for documentation lookup, code simplification or audits.
---

# Operator Docs

## Purpose
Write for an operator who needs to complete a task safely, not for an auditor reading every implementation detail. Use plain, natural English in technical artifacts.

## Scope and authority
- Read the closest project instructions, existing procedure, scripts and configuration that establish the actual steps.
- Keep the requested document format (Markdown, MediaWiki, etc.), naming conventions and working commands.
- Use only verified paths, variables, commands, prerequisites and expected results. Do not invent a successful test or an approved environment.
- Keep the canonical technical runbook as the source of truth. For a quick guide, link to it rather than copying its entire explanation.

## Writing rules
- Start with one sentence explaining the outcome and the minimum prerequisites.
- Use short, numbered steps in execution order.
- For each step: **Action -> command -> expected result**. Omit a part only when it adds no value.
- Make copied commands independently understandable: define required variables and helpers, or link explicitly to the exact setup step that defines them.
- Prefer short sentences, direct verbs and familiar terms; preserve precise technical identifiers.
- Remove repeated warnings, speculative edge cases, long architecture discussions, audit narratives and information the operator does not need to follow this procedure.
- Keep troubleshooting short and limited to common or observed failures; put advanced diagnostics in the canonical runbook.
- Preserve mandatory approvals, security checks, STOP conditions, non-production restrictions, validation and scoped rollback where applicable. State each at the point where it matters instead of repeating it everywhere.
- Never include credentials, private keys or secret values in examples. Preserve safe handling instructions without expanding them into unrelated policy text.
- Do not add requirements, checkpoints or hypothetical safeguards that are absent from the verified process just to make the document look comprehensive.

## Rewrite workflow
1. Identify the audience and the requested document type (quick guide versus full operational runbook).
2. Extract the verified execution sequence, dependencies, approval gates and success criteria.
3. Rewrite for the operator; move optional detail to a link or a clearly separate troubleshooting section.
4. Compare the result with the original: no missing required command, prerequisite, safety gate or validation step.
5. Check command order, defined variables, copy/paste usability, formatting and factual accuracy.

## Output
Return the edited document and a brief note of significant changes or unresolved facts. Do not add a separate technical audit unless requested. Document-writing does not authorize executing deployment commands.
