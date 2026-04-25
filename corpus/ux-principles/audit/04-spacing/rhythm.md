---
name: Rhythm — Related Items Closer, Distinct Sections Farther
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/04-spacing/scale-base.md, corpus/ux-principles/audit/04-spacing/alignment-consistent.md, corpus/ux-principles/audit/01-hierarchy/whitespace-intentional.md]
---

# Rhythm — Related Items Closer, Distinct Sections Farther

## What it is

The Gestalt principle of proximity in CSS form: related items should be visually closer together; distinct sections should be visually farther apart. The spacing between elements communicates their relationship — closer = "these belong together," farther = "these are separate concepts."

A form field's label should be tight against the field (8px). The next field's label-and-input pair should sit farther from the previous (24-32px). The form section break should be even farther (48-64px).

## Why it matters

Without rhythm, the page reads as a flat list of elements with no implied groupings. Users have to mentally parse what relates to what, slowing comprehension. With rhythm, the structure is immediately legible: scanning users pick up groupings in milliseconds.

Rhythm is also what distinguishes "tight" from "cramped" and "spacious" from "sparse." Both pairs use whitespace, but rhythmic whitespace conveys structure; arrhythmic whitespace just looks random.

## How to apply

1. **Tight spacing within groups:** 4-8px between label and field, 8px between bullet items.
2. **Medium spacing between siblings in a list:** 16-24px between cards in a stack.
3. **Larger spacing between sections:** 48-96px between major sections of a page.
4. **Be ruthless with consistency.** All groups within a list should use the same intra-group spacing.
5. **Audit:** does the spacing between any two elements make sense given their relationship?

## Examples

- **GOOD:** A form with `gap: 8px` between label and input, `gap: 24px` between fields, `gap: 64px` between form sections. Three rhythm levels.
- **BAD:** A form with arbitrary gaps — 12px between everything. Reads as a uniform list, no implied structure.
- **GOOD:** A blog post with `gap: 16px` between paragraphs, `margin-top: 48px` before headings. Clear sections, comfortable reading.
- **BAD:** A blog post with `margin-top: 16px` everywhere — paragraphs and headings same distance apart, structure invisible.

## Related entries

- `corpus/ux-principles/audit/04-spacing/scale-base.md`
- `corpus/ux-principles/audit/04-spacing/alignment-consistent.md`
- `corpus/ux-principles/audit/01-hierarchy/whitespace-intentional.md`

## Anti-patterns

- One spacing value used everywhere. Loses all hierarchy.
- Spacing scaled by importance instead of relationship. ("This section is important so it gets more space.") Importance = visual weight; relationship = spacing.
