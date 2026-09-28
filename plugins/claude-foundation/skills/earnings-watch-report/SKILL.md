---
name: earnings-watch-report
description: Use this skill when creating weekly upcoming earnings reports for the user's watchlist, especially EUR/European-listed instruments, AI/tech/pharma/industrial focus, and Trading 212 Invest planning.
disable-model-invocation: true
---

# Earnings Watch Report

## Purpose

Use this skill for weekly earnings watch reports and upcoming earnings risk planning.

Use it when the user asks:

- weekly earnings update
- earnings calendar
- reports for portfolio/watchlist
- Tuesday 09:00 earnings report
- "stock date comment" table
- upcoming earnings impact

## Default output language

Use Bulgarian unless the user requests English.

## Default watchlist

Use this watchlist unless the user provides a different one:

```text
NVDA
AVGO
MSFT
AMD
AP2
TS3E
NOVO-B
SMCI:BIT
VRT
MU
ASML
SAP
ORCL
MRVL
SOFI
```

Map instruments to EUR/European equivalents where possible.

## Required live-data rule

Earnings dates can change.

Always verify current earnings dates before giving a final report.

If live verification is unavailable, mark the report as framework-only and state that dates require confirmation.

## Standard table

Use:

```text
Stock | Instrument / EU equivalent | Earnings date | Timing | Expected impact | Action comment
```

Optional expanded table:

```text
Stock | Date | Confirmed? | Position? | Risk | Setup | Action
```

## Action rules

Before earnings:

- avoid new leveraged entries
- avoid aggressive DCA less than 5 days before earnings
- define hold/trim/wait plan
- prepare levels, but do not chase first spike

After earnings:

- wait for day 2–3 reaction
- check no lower low
- check volume
- check support/base
- only then consider add/swing

## Impact classification

Use:

```text
High impact
Medium impact
Low impact
Watch only
```

Classify based on:

- position size
- AI/tech relevance
- sector read-through
- leverage exposure
- recent stock move
- macro sensitivity
- guidance importance

## Report structure

Use:

```text
Обобщение:
Най-важни отчети:
Таблица:
Риск за портфейла:
Какво да не се прави:
Какво може да се направи:
След отчетите:
```

## Final response style

Keep it actionable.

Use dates and timing clearly.

Mention uncertainty when earnings dates are unconfirmed.

