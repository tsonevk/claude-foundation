---
name: portfolio-bucket-rebalance
description: Use this skill when reviewing or correcting portfolio buckets, Google Sheets formulas, dashboard weights, asset classifications, and rebalance suggestions for the user's EUR-focused portfolio.
disable-model-invocation: true
---

# Portfolio Bucket Rebalance

## Purpose

Use this skill for portfolio bucket review and rebalancing.

Use it when the user asks:

- "do some stocks need to be rearranged"
- "change bucket"
- "update Dashboard"
- "formulas for columns"
- "why Core is too large"
- "positions extended/reduced"
- "copy-paste table for Google Sheets"
- "portfolio allocation looks wrong"

## Source of truth

When the user provides screenshots or sheet data, treat the Dashboard/current visible table as the source of truth unless they specify another tab.

Do not touch dividend tabs unless explicitly requested.

User prefers dividends to remain as personal historical records in the same main sheet.

## Default buckets

Use these buckets unless the current sheet defines others:

```text
AI Core
AI Satellite
Defensive
Financial
Energy Hedge
Tactical / Leveraged
Dividend / Income
Cash
Watchlist
```

## High-level target framework

Use cautiously as guidance, not as hard law:

```text
AI Core: 55–65%
AI Satellite: 5–10%
Defensive: 15–25%
Financial: 5–10%
Energy Hedge: 3–6%
Tactical / Leveraged: reduce toward 0 over time
```

If the user's current framework differs in the sheet, follow the sheet and report the mismatch.

## Formula guidance

Common formulas:

Weight per asset:

```excel
=IFERROR(G4/SUM($G$4:$G$38),"")
```

Bucket total weight:

```excel
=IFERROR(SUMIF($I$4:$I$38,I4,$G$4:$G$38)/SUM($G$4:$G$38),"")
```

When formulas look wrong, check:

- absolute ranges
- asset value column
- bucket column
- hidden rows
- duplicated labels
- rows outside formula range
- text-formatted numbers
- currency symbols
- decimal separators
- percent formatting

## Output tables

For bucket changes:

```text
Asset | Old Bucket | New Bucket | Reason
```

For position action:

```text
Asset | Current Bucket | Current Weight | Target Role | Action | Reason
```

For formula fixes:

```text
Column | Row | Formula | Purpose
```

## Rebalance rules

Suggest reduce/extend based on:

- overweight core
- too much leveraged exposure
- position below minimum useful size
- high conviction core candidates
- concentration risk
- upcoming earnings
- current technical structure
- monthly DCA budget
- user risk preference

Do not recommend adding before checking live price when market-sensitive.

## Leverage rule

For leveraged ETPs:

- avoid adding before earnings
- avoid adding on first spike
- reduce/trim when exposure becomes too large
- prefer partial trim over full exit when underlying long-term thesis remains good
- define stop/stop-limit levels when swing planning is involved

## Final response style

Use Bulgarian unless the user asks otherwise.

Be table-first.

Make outputs easy to paste into Excel or Google Sheets.

Explicitly say when analysis is formula-only and not live-price-based.

