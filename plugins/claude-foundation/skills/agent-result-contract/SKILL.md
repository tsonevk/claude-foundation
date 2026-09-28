---
name: agent-result-contract
description: Apply the shared structured result envelope when subagents, loops, or automation return findings, so the parent thread can aggregate, retry, or escalate without guessing. Use when designing agent output, merging fan-out results, or classifying automation errors.
---

# Agent Result Contract

## Purpose
One canonical result contract for subagents, loops, and automation, with a compact default for routine successful inspections and a full envelope when aggregation, failure handling, or evidence depth requires it.

## When to use
- Designing a subagent, loop, or automation Output section.
- Returning findings from a focused subagent to the parent thread.
- Merging fan-out results in the parent thread.
- Classifying an automation error for retry vs escalation.

## When not to use
- A trivial single-fact answer in the main thread where an envelope adds only noise.

## Required inputs
- The domain result (findings, verdict, or evidence) the agent produced.
- The scope the agent was asked to cover.

## Workflow
1. Emit the domain-specific output first when the task has one (for example GO / CONDITIONAL GO / NO-GO, or a review summary).
2. Use the compact result by default for a routine single-subagent success or empty-success result.
3. Use the full envelope for fan-out aggregation, automation/retry workflows, security or release reviews, conflicting evidence, or any `partial`, `failed`, or `escalate` result.
4. Set `status` honestly: distinguish empty success from failed inspection.
5. Keep evidence distilled; do not return raw logs, broad grep output, or large file dumps when a concise fact and source are sufficient.

## Output contract

### Compact default

Use for routine successful focused inspections:

    status: success
    coverage:
      reviewed: []
      gaps: []
    findings:
      - title: ""
        fact: ""
        source: ""
    confidence: high | medium | low
    next_safe_action: ""

Omit empty optional fields when that makes the result smaller without hiding uncertainty. A successful inspection with no findings is still `status: success` with an empty `findings` list.

### Full envelope

Use when the parent needs deterministic aggregation, deeper evidence, retry/error handling, conflict preservation, or higher-risk review:

    status: success | partial | failed | escalate

    coverage:
      reviewed: []        # files, systems, or scopes actually inspected
      skipped: []         # in-scope items not inspected, with reason
      gaps: []            # known unknowns that limit the conclusion

    evidence:
      - source: ""        # file path, command, log, doc
        location: ""      # line, section, resource id
        observed_at: ""   # timestamp of observation
        fact: ""          # observed fact, subject to the secrets rule

    findings:
      - severity: critical | high | medium | low
        title: ""
        evidence_refs: [] # indexes into evidence
        impact: ""
        recommendation: ""

    error:                # present only when status is partial | failed | escalate
      category: transient | input | validation | permission | tool | conflict
      retryable: true | false
      attempted_actions: []
      missing_context: []

    conflicts: []          # contradicting evidence, preserved rather than averaged
    confidence: high | medium | low
    next_safe_action: ""

## Rules
- "No results found" is `status: success` with empty `findings`. "Inspection failed" is `status: partial|failed` and requires the full envelope with the `error` block.
- Local retry limit is 1-2 attempts; then use `status: escalate` with the full `error` block filled.
- Aggregators carry `coverage.skipped` and `coverage.gaps` into the final synthesis; missing coverage is treated as gaps, never as full coverage.
- Raw command output is evidence input, not the default agent response. Distill it unless exact lines are required.
- Secrets rule: never copy secrets into results; redact and point to the source instead.

## Verification
- Every returned result has `status` and enough `coverage` to show what was actually inspected.
- Routine success uses the compact form unless the full envelope is justified.
- Failures carry the full `error` block; successes with no findings are not mislabeled as failures.

## Safety boundaries
- Never place secrets, tokens, keys, or private log payloads in `fact` or `evidence.fact`; redact and cite the source.
- Do not average or discard conflicts; use the full envelope and preserve contradicting evidence.

## Related skills
- `deep-orchestration-mode`
- `verification-loop`
- `manual-compact-handoff`

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- Keep this contract canonical; do not restate interaction-intake, security, or domain-agent policy here.
