# Agentic Loop Templates

These templates are bundled with `claude-foundation:deep-orchestration-mode`.

Copy them into a project repo only after reading the repo's `CLAUDE.md`, `AGENTS.md`, README, handoff docs, tests, and runtime constraints.

They are designed for safe recurring or goal-driven agent work:

1. Trigger
2. Context
3. Action
4. Verification
5. State update
6. Stop, retry once, or escalate

## Files

- `TASK.md` - stable loop goal, scope, and outputs.
- `PROGRESS.md` - compact loop state between runs.
- `LOOP_INSTRUCTIONS.md` - operating procedure and safety rules.
- `VERIFY.md` - checker-only verification pass.
- `loop.md` - reusable prompt shape for a manual or scheduled loop run.

## Safe default

Start with read-heavy and write-light loops:

- allowed: inspect, summarize, draft, write approved output files, update state
- denied by default: source edits, external posts, ticket mutation, branch push, deploy, cloud mutation, production mutation, secret handling

Scheduling is not the first step. Run the loop manually until it is useful, compact, and consistently verifiable.
