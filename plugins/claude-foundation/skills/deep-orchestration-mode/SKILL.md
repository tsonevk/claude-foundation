---
name: deep-orchestration-mode
description: Use a bounded scout-plan-slice-verify workflow for genuinely large, ambiguous, high-risk, explicitly parallelizable, recurring, or goal-driven Claude Code tasks.
disable-model-invocation: true
---

# Deep Orchestration Mode

## Purpose
Provide a bounded workflow when a normal direct task is not enough. It is not a default preamble for ordinary repository work.

## When to use
- Large architecture/security/repository work with unclear blast radius.
- Explicitly requested parallel/subagent review where tracks are independent.
- Recurring, scheduled, polling, stateful, or goal-driven agent workflow design.

## When not to use
- Clear scoped edits, simple diagnostics, formatting, or one-file changes.
- Work that a narrower skill already covers.
- Any situation where fan-out/coordination costs more than it helps.

## Default execution model
Stay single-threaded by default:
1. scout only the relevant authority/source
2. map the smallest task slice
3. implement if approved
4. verify
5. challenge residual risk
6. hand off concise state only when durable state is actually needed

## Optional subagents
Use subagents only when explicitly requested or when a bounded read-only side investigation would materially protect the parent context. Keep fan-out small (normally 1-3), one level deep, with disjoint scopes and distilled evidence. The parent thread owns synthesis and final edits.

## Recurring/goal-driven loops
A safe loop defines trigger, authoritative context, capability boundary, execution boundary, one bounded action, runtime-native events/evidence when justified, deterministic verification, compact state update when needed, stop/retry/escalation policy, and human approval boundary.

Start manual, read-heavy, and write-light. Before autonomous writes, define the real workspace/branch/worktree/container/runner boundary. Schedule or widen permissions only after useful manual runs and explicit approval. For tool-driven runtime work, apply `ai-agent-tool-safety-review`.

## Safety boundaries
- No unbounded agent spawning, recursion, token use, or repository reading.
- No production/cloud/DB/whole-instance mutation without explicit approval.
- No detached work claims without a real scheduler/automation.
- No live production target should be described as a sandbox without an actual isolation boundary.
- No durable audit claim unless the runtime records the corresponding evidence.
