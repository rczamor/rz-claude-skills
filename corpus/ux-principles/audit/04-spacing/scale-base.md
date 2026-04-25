---
name: Spacing Scale — 4px or 8px Base, Not Arbitrary Values
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/04-spacing/grid-consistent.md, corpus/ux-principles/audit/04-spacing/rhythm.md, corpus/ux-principles/audit/02-typography/scale-ratio.md]
---

# Spacing Scale — 4px or 8px Base, Not Arbitrary Values

## What it is

All spacing in a product — margins, padding, gaps, gutters — should derive from a base unit (commonly 4px or 8px) and use only multiples of it. A 4px base gives you: 4, 8, 12, 16, 24, 32, 48, 64, 96. An 8px base gives: 8, 16, 24, 32, 48, 64. No `padding: 13px` or `margin: 27px`.

This is a hard rule. Arbitrary values are the single most common source of visual inconsistency.

## Why it matters

When all spacing is on a system, related elements naturally relate to each other (their padding and margins are factors of the same unit). When spacing is arbitrary, elements have subtle misalignments — a 13px gap here, a 16px gap there — that the eye reads as sloppy without articulating why.

The base unit also makes the system extensible. Designers and devs don't pick "what number sounds good"; they pick the next step on the scale.

## How to apply

1. **Choose 4px or 8px base.** 4px is more granular (good for tight UI); 8px is more opinionated (good for marketing).
2. **Define spacing tokens:**
   ```css
   --space-1: 0.25rem;  /* 4px */
   --space-2: 0.5rem;   /* 8px */
   --space-3: 0.75rem;  /* 12px */
   --space-4: 1rem;     /* 16px */
   --space-6: 1.5rem;   /* 24px */
   --space-8: 2rem;     /* 32px */
   --space-12: 3rem;    /* 48px */
   --space-16: 4rem;    /* 64px */
   ```
3. **Use only token values.** No raw `13px` or `27px`.
4. **Tailwind enforces this** by default — utilities map to the scale.
5. **Audit:** scan all `padding` / `margin` / `gap` values for off-scale numbers.

## Examples

- **GOOD:** A card with `padding: 24px`, items inside spaced by `gap: 16px`, between cards `gap: 32px`. All on the 8px scale.
- **BAD:** A card with `padding: 23px`, items at `gap: 18px`, between cards `gap: 31px`. Off-scale, looks accidental.
- **GOOD:** Tailwind's spacing utilities — `p-4`, `gap-6`, `mt-12`. Always on scale.
- **BAD:** Inline styles with `padding: 13.5px;` because that's what looked right at the moment.

## Related entries

- `corpus/ux-principles/audit/04-spacing/grid-consistent.md`
- `corpus/ux-principles/audit/04-spacing/rhythm.md`
- `corpus/ux-principles/audit/02-typography/scale-ratio.md`

## Anti-patterns

- Eyeballing spacing in browser DevTools by tweaking pixel values. Use the scale.
- Mixing 4px and 8px bases — pick one, commit.
