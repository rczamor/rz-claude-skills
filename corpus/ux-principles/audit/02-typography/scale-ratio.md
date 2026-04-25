---
name: Scale Ratio — 1.25 (Major Third) or 1.333 (Perfect Fourth)
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/02-typography/no-skipped-heading-levels.md, corpus/ux-principles/audit/04-spacing/scale-base.md]
---

# Scale Ratio — 1.25 (Major Third) or 1.333 (Perfect Fourth)

## What it is

Type scales should follow a consistent ratio between sizes. The two most common ratios are:

- **1.25 (major third)** — gentle, suited to dense interfaces and dashboards.
- **1.333 (perfect fourth)** — more dramatic, suited to marketing pages and editorial layouts.

Starting from a base body size (e.g., 16px), each step is the previous size × ratio. With 1.25: 16, 20, 25, 31, 39, 49, 61. With 1.333: 16, 21, 28, 38, 51, 68.

Arbitrary sizes (`14px, 17px, 19px, 24px, 28px`) signal that no scale was chosen.

## Why it matters

A scale enforces hierarchy. The eye recognizes proportional relationships even when it can't articulate them — sizes that follow a ratio look "right," and sizes picked one-off look chaotic. A scale also gives designers fewer decisions to make: pick the next step up, not "what number sounds good."

## How to apply

1. **Pick a ratio.** 1.25 for dense apps, 1.333 for marketing.
2. **Base on body size (typically 16px).**
3. **Snap all sizes to scale steps.** No off-scale values.
4. **Define tokens** — `--text-xs`, `--text-sm`, `--text-base`, `--text-lg`, `--text-xl`, `--text-2xl`, `--text-3xl`, etc.
5. **Audit:** list all `font-size` values used. If they don't snap to a ratio, the scale is broken.

## Examples

- **GOOD (1.25 scale):** body 16, large body 20, h3 25, h2 31, h1 39, hero 49.
- **GOOD (1.333 scale):** body 16, h4 21, h3 28, h2 38, h1 51, hero 68.
- **BAD:** body 16, h3 18, h2 22, h1 30 — no consistent ratio, looks accidental.
- **GOOD CSS tokens:**
  ```css
  --text-base: 1rem;
  --text-lg: 1.25rem;
  --text-xl: 1.5625rem;  /* 1.25^2 */
  --text-2xl: 1.953rem;  /* 1.25^3 */
  ```

## Related entries

- `corpus/ux-principles/audit/02-typography/no-skipped-heading-levels.md`
- `corpus/ux-principles/audit/04-spacing/scale-base.md` — same idea applied to spacing

## Anti-patterns

- "We just picked sizes that looked good." That's the no-scale path; the page will feel inconsistent.
- Using two ratios simultaneously (1.25 in some places, 1.333 in others). Pick one.
