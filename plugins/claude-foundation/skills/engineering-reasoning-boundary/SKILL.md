---
name: engineering-reasoning-boundary
description: Preserve human engineering judgment on high-consequence work by switching from AI-first execution to reasoning-first analysis before mutation.
---

# Engineering Reasoning Boundary

## Purpose

Use AI aggressively for execution without silently outsourcing the engineering judgment that defines safety, causality, and system boundaries.

## Default modes

### AI-first execution

Use for clear, low-risk, reversible work such as:
- repository search and codebase navigation
- boilerplate and pattern-following implementation
- documentation synchronization
- test generation
- bounded refactoring
- formatting and repetitive configuration work

Default flow:

```text
inspect -> implement -> narrow verification -> done
```

### Reasoning-first engineering

Use before implementation when the task involves meaningful operational, security, data-integrity, or architectural risk, especially:
- production incidents or production-impacting changes
- IAM, permissions, secrets, or trust boundaries
- networking, routing, DNS, certificates, or service dependencies
- database migrations, writes, transactions, retries, or idempotency
- Kubernetes/Terraform/Ansible changes with live blast radius
- destructive operations
- architecture decisions that create durable coupling
- distributed-system failure handling

Before proposing or executing a mutation, reconstruct the minimum engineering model:

```text
Goal:
Invariant:
Known facts:
Causal hypothesis:
Failure model:
Safest minimal change:
Validation / falsification:
Rollback:
```

Keep this compact. Do not turn it into ceremony.

## Causality rule

For incidents, distinguish:
- initiating cause
- amplifier
- downstream symptom

Establish event ordering from evidence where possible. Do not infer root cause merely from the loudest or most correlated metric.

Ask what changed first and what observation would falsify the current hypothesis.

## Retry and side-effect rule

Treat timeout as an unknown outcome, not proof that an operation failed.

Before adding retries to a mutating external operation, establish whether it is idempotent or protected by an idempotency key, deduplication mechanism, transaction boundary, or equivalent invariant.

## Challenge mode

When the user or repository already provides a hypothesis, prefer challenging it over replacing it silently:

1. Identify evidence for and against.
2. Try to falsify the hypothesis.
3. Name assumptions.
4. Separate observed facts from inference.
5. Recommend the smallest reversible action that tests the model.

## Human ownership boundary

AI may own:
- search
- implementation
- repetitive execution
- verification
- evidence collection
- documentation

Human judgment remains explicit for:
- intent
- risk tolerance
- invariants
- architecture boundaries
- production-impact decisions
- destructive actions

This does not require user confirmation for every high-risk analysis step. Continue autonomously through read-only investigation and reversible preparation. Respect the repository's existing explicit approval boundary before impactful execution.

## Output contract

For reasoning-first work, include only the parts that materially affect the decision:
- invariant or safety property
- causal/failure model
- key assumptions or uncertainty
- smallest safe next action
- validation and rollback when mutation is proposed

## Safety boundaries

- Read before mutation.
- Prefer evidence over plausible narratives.
- Prefer small reversible changes.
- Do not treat green tests as proof that business invariants are preserved.
- Do not broaden a bounded task into architecture work without evidence that it is necessary.
- Existing project-local safety, production, iMX, and approval rules override this skill.
