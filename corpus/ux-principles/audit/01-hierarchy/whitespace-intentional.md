---
name: Whitespace Is Intentional, Not Leftover
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/04-spacing/rhythm.md, corpus/ux-principles/audit/01-hierarchy/info-density-appropriate.md]
---

# Whitespace Is Intentional, Not Leftover

## What it is

Whitespace (negative space, the empty area between elements) should be a design decision, not the accidental gap left when nothing got placed there. Intentional whitespace creates rhythm, signals grouping, lets the eye rest, and elevates the items it surrounds. Leftover whitespace looks like a layout bug — uneven gaps, awkward stretches between unrelated elements, weird empty corners.

The test: would you notice if the whitespace got 20% smaller or larger? If yes, it's intentional. If no, it's leftover.

## Why it matters

Whitespace is one of the most powerful tools in design — it's how you signal "these things go together" and "this is the most important thing here." But it only works when it's deliberate. Inconsistent whitespace tells the user nothing useful and makes the page look unfinished. Worse, it makes the rest of the design look unfinished by association.

## How to apply

1. **Use a spacing scale (4px or 8px base).** Every gap is a multiple of the base unit. No `margin-top: 23px` arbitrary values.
2. **Tighter spacing within groups, looser spacing between groups.** Related items use the smaller scale (8px, 16px). Section breaks use the larger scale (48px, 64px, 96px).
3. **Generous whitespace around the most important element.** A primary CTA isolated by space draws more attention than the same CTA surrounded by clutter.
4. **Audit empty stretches.** Any large empty area should be there for a reason — breathing room, emphasis, separation. If it's just there because nothing else was, fix it.

## Examples

- **GOOD:** A pricing card with `padding: 32px`, items inside spaced by `16px`, between cards `24px`. Rhythm is consistent, intentional.
- **BAD:** A form where some field gaps are 12px, others 18px, others 8px — no system, just whatever the developer typed.
- **GOOD:** Apple product page — massive whitespace around the product image, signaling "this is the hero." Whitespace is the design.
- **BAD:** A dashboard where one column has 200px of empty space below it because the developer didn't shrink the container after deleting widgets.

## Related entries

- `corpus/ux-principles/audit/04-spacing/rhythm.md`
- `corpus/ux-principles/audit/01-hierarchy/info-density-appropriate.md`

## Anti-patterns

- Adding random `<br>` or `<div style="height: 50px"></div>` to "fix" spacing. Use the spacing system.
- Filling whitespace with decorative content because empty space "looks unfinished." Empty space looks finished when it's intentional.
