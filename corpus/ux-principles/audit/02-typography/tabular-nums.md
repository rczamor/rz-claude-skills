---
name: font-variant-numeric — tabular-nums on Number Columns
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/02-typography/scale-ratio.md, corpus/ux-principles/audit/04-spacing/grid-consistent.md]
---

# font-variant-numeric — tabular-nums on Number Columns

## What it is

By default, most fonts render digits with proportional widths — the "1" is narrower than the "8". This looks fine in prose but breaks columns of numbers: rows don't line up vertically, and figures feel uneven. Setting `font-variant-numeric: tabular-nums;` forces every digit to occupy the same width, making numbers in tables, financial reports, and dashboards align cleanly.

## Why it matters

A table of dollar amounts where digits don't line up vertically reads as amateurish. Users mentally re-align as they scan, slowing comprehension. Stocks, prices, metrics, scores — anywhere users compare numerical values vertically — benefits from tabular figures. The fix is a single CSS line; not applying it is just neglect.

## How to apply

1. **CSS on number columns:**
   ```css
   .num-col, td.numeric, .metric-value {
     font-variant-numeric: tabular-nums;
   }
   ```
2. **Tailwind:** `tabular-nums` utility class.
3. **Apply to:** stock tickers, dashboards, financial tables, leaderboards, anywhere numbers stack vertically.
4. **Don't apply globally** — proportional figures look better in prose.

## Examples

- **GOOD (tabular):**
  ```
  $1,234.56
  $   89.10
  $   12.34
  ```
  Decimal points align.
- **BAD (proportional):**
  ```
  $1,234.56
  $89.10
  $12.34
  ```
  Decimals scattered.
- **GOOD:** Stripe Dashboard's revenue tables use tabular-nums; columns line up perfectly.
- **BAD:** A finance app's transaction list with proportional digits — eye has to re-align constantly.

## Related entries

- `corpus/ux-principles/audit/02-typography/scale-ratio.md`
- `corpus/ux-principles/audit/04-spacing/grid-consistent.md`

## Anti-patterns

- Using proportional figures in a financial dashboard. Users notice without knowing why it bothers them.
- Applying tabular-nums globally to body text. Prose looks slightly worse.
