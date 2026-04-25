---
name: Alignment Consistent — Nothing Floats Outside the Grid
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/04-spacing/grid-consistent.md, corpus/ux-principles/audit/04-spacing/rhythm.md]
---

# Alignment Consistent — Nothing Floats Outside the Grid

## What it is

Every element on the page should align to the established grid (vertical alignment to columns, horizontal alignment to baselines and rows). Nothing floats — no element is positioned arbitrarily, breaking the grid. If one card is 4px to the left of the others, that's an alignment break.

Alignment includes: left edges of stacked cards, baselines of adjacent text blocks, top edges of side-by-side elements, and so on.

## Why it matters

The eye is extraordinarily sensitive to misalignment. A card 2px out of alignment from its neighbors reads as a bug, not a design choice. Even more striking: misalignment in one component makes the entire page feel unfinished — the user may not pinpoint the offending element, but the overall impression suffers.

## How to apply

1. **Use a grid system** (CSS Grid, flexbox with consistent gaps). Don't position elements with absolute positioning or arbitrary margins.
2. **Snap to whole pixels and grid lines.** No `margin-left: 2.5px;` to nudge things into place.
3. **Audit visually.** Lay a vertical line down the page (DevTools' rulers, or a screenshot with a guide). Do all major edges align?
4. **Use baseline alignment for text-heavy layouts.** Adjacent paragraphs should share baselines.

## Examples

- **GOOD:** A list of cards with `display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px;`. Every card aligned identically.
- **BAD:** Three cards positioned with absolute coordinates — one is `top: 100px`, another `top: 102px`. 2px misalignment, sloppy.
- **GOOD:** Form labels and inputs using a grid where every label-input pair starts at the same column. Eye flows down the form effortlessly.
- **BAD:** A form where some labels are above the inputs and some are to the left, creating jagged edges.

## Related entries

- `corpus/ux-principles/audit/04-spacing/grid-consistent.md`
- `corpus/ux-principles/audit/04-spacing/rhythm.md`

## Anti-patterns

- Using `margin-left: 7px` to nudge an element into "looking right" — fix the underlying alignment, don't fudge.
- Positioning everything with absolute positioning to "have full control." That's how you lose alignment fastest.
