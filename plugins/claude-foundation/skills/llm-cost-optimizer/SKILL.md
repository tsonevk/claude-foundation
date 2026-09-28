---
name: llm-cost-optimizer
description: Reduce Claude Code token and model costs with measured prompt, routing, context, and validation changes.
disable-model-invocation: true
---

# LLM Cost Optimizer

## Purpose
Keep Claude Code efficient without degrading correctness, evidence quality, or safety.

## When to use
- Model/token spend or latency is too high.
- Prompt or context size is growing.
- Routing/subagent behavior appears heavier than the task needs.
- You need a cheaper/faster path backed by evidence.

## Workflow
1. Identify the measurable cost driver.
2. Trim redundant prompt/context first.
3. Prefer direct scoped work over unnecessary meta-routing or fan-out.
4. Simplify model/routing choices only when quality remains sufficient.
5. Recheck quality and validation against the cheaper path.
6. Record the tradeoff clearly.

## Output contract
- Cost driver
- Safer cheaper option
- Quality tradeoff
- Verification suggestion

## Safety boundaries
- Do not optimize cost by dropping required evidence or validation.
- Do not assume the cheapest model is correct for every task.
- Do not change production/runtime routing without explicit approval.
