---
name: interaction-intake-contract
description: Classify ambiguous, high-risk, production-impacting, cross-domain, or genuinely multi-step requests before acting; define the target, success criteria, approval boundary, and next safe mode without adding ceremony to clear scoped tasks.
---

# Interaction Intake Contract

## Purpose
Use a compact execution contract only when ambiguity or risk makes immediate action unsafe or wasteful.

## Use when
- The requested target or outcome is ambiguous.
- The next action could be destructive, production-impacting, costly, or security-sensitive.
- The task crosses multiple systems or repositories and the authority boundary is unclear.
- The user asks for recurring/scheduled automation or a workflow with external side effects.
- A genuinely multi-step task needs explicit success criteria and approval boundaries before work begins.

## Do not use when
- The request is clear, scoped, and local.
- The target file/module/repo and desired outcome are explicit.
- The task is a normal bug fix, small feature, config edit, or review whose project docs can resolve context.
- A more specific skill already defines the needed workflow.

For a clear scoped repository task, read project authority, inspect the target, act, validate, and report. Do not emit a meta-contract first.

## Request modes
Choose exactly one primary mode only when this skill is triggered:

| Mode | Default action |
| --- | --- |
| `answer` | Explain/recommend only. |
| `observe` | Read/search only. |
| `analyze` | Gather evidence and assess. |
| `propose_patch` | Provide exact patch/change plan without editing. |
| `approved_edit` | Inspect, make the smallest scoped change, validate. |
| `review` | Findings first with evidence and missing verification. |
| `automation` | Define trigger/schedule/condition, task, safety, stop/escalation. |

## Compact intake
When needed, state only:
- Mode
- Target
- Success criteria
- Boundary / approval gate
- Likely specific skill or agent if obvious

Keep it to 3-5 bullets. Ask only blocking questions, maximum 3. If repository inspection can answer the question safely, inspect instead of asking the user to repeat context.

## Evidence discipline
Separate verified facts, inference, assumptions, and recommendations when the distinction affects correctness.
For edits, report files changed and validation performed. If validation cannot run, state why.

## Approval boundaries
Standing safe actions include read/search/list, git status/diff/log, static checks, syntax checks, dry-runs, and tests that do not mutate production/external state.

Explicit approval is required for production deploy/restart/reboot/shutdown, migrations, DB writes, IAM/policy changes, credential rotation, Terraform apply/destroy, live Kubernetes apply, destructive shell actions, whole-instance iMX lifecycle actions, or other externally visible mutations not already explicitly requested.

## Workflow
1. Contract only if ambiguity/risk justifies it.
2. Inspect authoritative context.
3. Act within the boundary.
4. Verify with the smallest meaningful checks.
5. Handoff evidence, risks, rollback where relevant, and next safe action.

## Related skills
- `harness-driven-coding`
- `search-first`
- `verification-loop`
- `deep-orchestration-mode`
