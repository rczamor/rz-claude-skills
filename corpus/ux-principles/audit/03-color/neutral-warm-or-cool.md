---
name: Neutral Palette — Warm OR Cool Consistently, Not Mixed
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/03-color/palette-coherent.md, corpus/brand-system/identity/]
---

# Neutral Palette — Warm OR Cool Consistently, Not Mixed

## What it is

The neutral grays in your palette should be either warm (slight yellow or red tint, e.g., `#F5F4F2`, `#37352F`) or cool (slight blue tint, e.g., `#F8FAFC`, `#1E293B`) — but consistently one or the other across the product. Mixing warm and cool grays makes the design feel inconsistent in ways users sense without being able to articulate.

Pure neutral grays (`#888`, `#CCC`) are technically neither, but they pair acceptably with either warm or cool palettes. The failure mode is using `#F5F4F2` (warm) in one component and `#F8FAFC` (cool) in another.

## Why it matters

Warm grays carry a different emotional register from cool grays — warm feels approachable, organic, brand-y; cool feels precise, technical, modern. Mixing the two within a single product creates subtle dissonance. Most users won't say "the grays clash," but they'll feel something is off.

Notion uses warm grays. Linear uses cool grays. Both are coherent because they pick a side and commit.

## How to apply

1. **Pick warm or cool** for the neutral scale at the start of the design system.
2. **Define tokens consistently:** every gray-50 through gray-950 follows the same temperature.
3. **Use HSL to make temperature explicit:** warm grays have hue ~30-50, cool grays have hue ~210-220.
4. **Audit:** sample several "gray" colors across the product. If some are warm and some cool, fix.

## Examples

- **GOOD (cool palette):** `#F8FAFC`, `#E2E8F0`, `#94A3B8`, `#475569`, `#1E293B`. All have a slight blue undertone. Tailwind's `slate` scale.
- **GOOD (warm palette):** `#FAFAF9`, `#E7E5E4`, `#A8A29E`, `#57534E`, `#1C1917`. All warm. Tailwind's `stone` scale.
- **BAD:** Mixing `slate-100` (cool) with `stone-900` (warm) in the same component. Discordant.
- **GOOD:** Notion's UI — every gray has a warm cream undertone. Cohesive even when subtle.

## Related entries

- `corpus/ux-principles/audit/03-color/palette-coherent.md`
- `corpus/brand-system/identity/`

## Anti-patterns

- "We just used the default gray scale" — without checking whether it matches the rest of the palette.
- Mixing Tailwind's `gray`, `slate`, `zinc`, `neutral`, and `stone` arbitrarily because "they're all gray." They're not — different temperatures.
