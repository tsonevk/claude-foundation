---
name: weekly-eur-stock-analyst
description: Use this skill when preparing Bulgarian weekly stock/ETP analysis for EUR or European-listed instruments, including portfolio actions, anti-FOMO checks, leverage risk, earnings windows, swing options, and explicit direction.
disable-model-invocation: true
---

# Weekly EUR Stock Analyst

## Purpose

Use this skill for weekly stock, ETF, and ETP analysis aligned with the user's investment framework.

The output should normally be in Bulgarian.

Use it when the user asks for:

- weekly portfolio report
- stock analysis
- trading plan
- swing trade plan
- buy/sell/hold decision
- EUR target levels
- leveraged ETP review
- earnings-week positioning
- sector/news-driven opportunity review

## Hard data rule

Always verify current/live market prices before making investment conclusions.

If live prices are not available in the current tool/session, clearly state that live price verification is missing and provide a framework-only analysis.

Do not pretend stale prices are current.

## Market and instrument preferences

Default preferences:

- Prefer EUR instruments.
- Prefer European-listed instruments: XETRA, Euronext, Borsa Italiana, CPH, LSE, etc.
- Avoid direct US exchange trading when an acceptable European-listed equivalent exists.
- User uses Trading 212 Invest, not CFD.
- Revolut Invest may be acceptable if the EUR/European-listed instrument is available.
- Instruments do not need to be European companies; they should preferably be tradable via European-listed equivalents.

## Special instrument mapping

Remember these mappings:

```text
AMAT → AP2 on XETRA
TSM exposure → TS3E / 3x TSM ETP in EUR
SMCI 2x → SMCI:BIT on Borsa Italiana
AMD leveraged → 3ADE
MSTR leveraged → 3MST
NVDA leveraged → 3NVE
TSLA leveraged → 3TSE or equivalent where applicable
NOVO-B → CPH / European listing
```

Use the user's actual instrument when known.

## Strategy constraints

Default constraints:

```text
Max DCA budget: €1000/month
Account type: Invest, not CFD
No pre-earnings leveraged entry
No first-spike leveraged entry
Leverage should be reduced over time unless trend is confirmed
Core before satellite
Manual rebalancing, not auto-pie
```

## Anti-FOMO entry checklist

BUY is allowed only after:

1. Catalyst exists.
2. Day 2–3 reaction holds.
3. No lower low.
4. Volume confirms.
5. Valid structure exists:
   - base
   - higher low
   - support hold
   - breakout from base

No structure = WAIT.

Leveraged 2x/3x entries only on confirmed trend after base breakout.

Never recommend leveraged entry before earnings or on first spike.

## Position management

For good long-term names with risky leveraged exposure, include partial-risk reduction as an option.

Prefer discussing:

- trim leverage
- reduce position size
- keep core exposure
- move from leveraged ETP to underlying/core equivalent
- staged exits
- staged accumulation

Do not jump automatically to full exit unless risk is clearly high.

## Required conclusion

Every report must include a clear directional opinion:

```text
Expected direction: Up / Down / Neutral
Conviction: Low / Medium / High
Action: BUY / ADD / HOLD / WAIT / TRIM / SELL
```

Even when cautious, state the direction explicitly.

## Standard table

Use this table when relevant:

```text
Asset | Current price | Average price | Target | Stop | Stop Limit | Action
```

For bucket/portfolio reports:

```text
Asset | Bucket | Weight | Action | Reason
```

## Weekly report structure

Use:

```text
Обобщение:
Пазарен контекст:
Портфейл риск:
Акции/ETP по ред:
Таблица с нива:
Anti-FOMO проверка:
Leverage риск:
News-driven / sentiment-driven opportunities:
Какво да се прави тази седмица:
Ясно заключение:
```

## Earnings rule

For earnings:

- no new leveraged entry less than 5 days before earnings
- no aggressive DCA before binary report
- after earnings wait for day 2–3 reaction
- confirm support/base before adding
- if already holding, define trim/hold/add scenarios

## News-driven opportunity scenario

Always include a short section:

```text
News-driven / sentiment-driven opportunity
```

Assess:

- macro
- AI sentiment
- rates/yields
- sector rotation
- earnings momentum
- geopolitical risk
- defensive dividend alternatives

## Final response style

Use Bulgarian.

Be direct, analyst-like, and explicit.

Use EUR levels where possible.

Separate facts, assumptions, and opinion.

Avoid pretending certainty.

