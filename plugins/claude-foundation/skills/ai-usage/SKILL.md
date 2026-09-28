---
name: ai-usage
description: Analyze local Claude Code token usage and cost estimates with ccusage; workstation-local developer observability only, not billing authority or production telemetry.
---

# AI Usage

## Purpose
Answer Claude Code usage/token/cost questions from local session records using ccusage. Results are local estimates, not provider billing authority.

## When to use
- Claude Code daily/weekly/monthly/session usage questions.
- Per-project/instance usage breakdowns.
- A development session felt expensive and the user wants evidence.

## When not to use
- Production/application telemetry.
- Provider invoice reconciliation.
- Cross-machine/team aggregation.

## Required inputs
- Time grain: daily, weekly, monthly, or session-level.
- Human-readable vs JSON output.
- Whether per-instance/project breakdown is needed.
- Pinned ccusage version: `ccusage@20.0.19`.

## Workflow
1. Confirm the requested time grain/scope.
2. Use the pinned wrapper or equivalent pinned command, for example:

```bash
npx ccusage@20.0.19 daily
npx ccusage@20.0.19 weekly
npx ccusage@20.0.19 monthly
npx ccusage@20.0.19 claude daily --instances
npx ccusage@20.0.19 daily --json
```

3. Present results with scope/time grain clearly labeled.
4. State that cost figures are estimates from local Claude Code records.
5. Do not commit or persist raw usage/session history in tracked paths.

## Output contract
- Scope/time grain
- Exact pinned command
- Usage/cost summary with estimate caveat
- Confirmation that raw local history was not committed/shared

## Safety boundaries
- Local developer observability only.
- No persistence of session history into repositories.
- No cross-project exposure of local usage data.
- No bare `@latest` in reusable automation.
