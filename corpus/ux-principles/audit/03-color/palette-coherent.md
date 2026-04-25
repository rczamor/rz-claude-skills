---
name: Palette Coherent — ≤12 Unique Non-Gray Colors
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/03-color/semantic-colors.md, corpus/ux-principles/audit/03-color/neutral-warm-or-cool.md, corpus/brand-system/identity/]
---

# Palette Coherent — ≤12 Unique Non-Gray Colors

## What it is

A coherent palette uses ≤12 distinct non-gray colors across the entire product. Gray scales are excluded from the count (you typically need 8-12 grays for shadows, borders, backgrounds, text). The 12-color cap covers brand colors, semantic colors (success, error, warning, info), and any accent or category colors.

More than 12 distinct colors and the palette starts to feel undisciplined — the eye can't recognize a system, and the product reads as a collection of one-off decisions rather than a cohesive whole.

## Why it matters

Color is a primary identity carrier. A tight palette reads as confident; a sprawling palette reads as random. Beyond identity, a tight palette also makes hierarchy clearer: when colors are scarce, the colors that do appear carry more weight.

This rule is operationalized via DOM scanning — extract all `color` and `background-color` values, deduplicate, exclude grays, count. >12 = flag.

## How to apply

1. **Audit:** in DevTools, run a script to extract all colors and count unique non-gray values.
2. **If > 12:** consolidate. Find duplicates that are nearly identical (`#3B82F6` and `#3D83F8`) and merge.
3. **Define tokens.** Every color in the product should map to a named token (`--color-primary`, `--color-success`, `--color-warning`).
4. **Don't hardcode hex values in components.** They drift from the system.

## Examples

- **GOOD:** A SaaS palette: 1 primary, 1 secondary, 4 semantic (success/error/warning/info), 4 accents, plus 8 grays. ~10 non-gray colors, well under cap.
- **BAD:** A landing page that ends up with 30+ colors because every section had a different "feel" and the team never reconciled.
- **GOOD:** Stripe's palette — primary blurple, semantic greens/reds/yellows, neutral grays. Tight and identifiable.
- **BAD:** A dashboard where each chart picks colors freely — by the time you have 8 charts, you have 40 colors.

## Related entries

- `corpus/ux-principles/audit/03-color/semantic-colors.md`
- `corpus/ux-principles/audit/03-color/neutral-warm-or-cool.md`
- `corpus/brand-system/identity/`

## Anti-patterns

- Defining the brand palette as "any color the marketing team likes."
- Using direct hex values in CSS instead of tokens — colors drift over time.
