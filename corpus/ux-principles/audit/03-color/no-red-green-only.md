---
name: No Red/Green Only Combinations — 8% of Men Have Red-Green Deficiency
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/03-color/no-color-only-encoding.md, corpus/ux-principles/audit/03-color/semantic-colors.md]
---

# No Red/Green Only Combinations — 8% of Men Have Red-Green Deficiency

## What it is

Approximately 8% of men and 0.5% of women have red-green color vision deficiency (deuteranopia or protanopia). For them, red and green look nearly identical — both render as a similar muddy yellow-brown. Any UI that depends on distinguishing red from green without additional cues is invisible to ~1 in 12 men.

Common offenders: stock charts (red down / green up), pass/fail badges (red X / green check using color only), form validation (red border / green border without icons or text).

## Why it matters

This is one of the most common accessibility failures because the red-green convention is deeply ingrained — green = good, red = bad — and designers rarely test grayscale or simulated color blindness. The fix is universal: pair the color with a non-color cue.

## How to apply

1. **Always pair red/green with a redundant cue:**
   - Stock arrows: ▲ for up, ▼ for down (in addition to color).
   - Pass/fail: ✓ for pass, ✗ for fail.
   - Form validation: error icon + text, success checkmark + text.
2. **Test in grayscale.** Chrome DevTools → Rendering → Emulate vision deficiencies → Achromatopsia.
3. **Test deuteranopia / protanopia** specifically — the simulator shows what red-green deficient users see.
4. **Avoid putting red and green directly adjacent** as the only distinguishers. They merge.

## Examples

- **GOOD:** Stock ticker showing `▲ +2.5%` in green and `▼ -1.2%` in red. Color helps; the arrows do the work.
- **BAD:** Stock ticker showing `+2.5%` (green) and `-1.2%` (red), no arrows. Red-green deficient users see two identical-looking percentages.
- **GOOD:** GitHub PR file diff: `+` for added lines (green), `-` for removed (red). The character does the work, color reinforces.
- **BAD:** A heatmap that only uses red-to-green gradient with no labels. Users with deficiency see uniform noise.

## Related entries

- `corpus/ux-principles/audit/03-color/no-color-only-encoding.md`
- `corpus/ux-principles/audit/03-color/semantic-colors.md`

## Anti-patterns

- "It's a stock chart, everyone knows red is down." Not for ~1 in 12 men.
- Using red and green simultaneously as the only differentiator on charts, badges, or status pills.
