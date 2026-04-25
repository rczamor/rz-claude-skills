---
name: Uniform Bubbly Border-Radius (AI Slop)
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/04-spacing/border-radius-hierarchy.md, corpus/brand-system/identity/imagery-anti-patterns.md]
---

# Uniform Bubbly Border-Radius

## What it is
The same large border-radius applied to every element on the page — buttons, cards, inputs, images, modals, even icons. `rounded-2xl` on everything. The visual identity of every Vercel-clone landing page generated since 2023. Without radius hierarchy, nothing feels nested, contained, or distinct — the whole page becomes a soft blur.

## Why it matters
Border-radius is a hierarchy signal. Larger radius = larger element = outer container. Smaller radius = nested or interactive element. When everything has the same radius, the visual logic collapses. It also fights the inner-radius formula (`audit/04-spacing/inner-radius-formula.md`): `inner = outer - gap` produces nested elements that look correctly seated. Uniform radius produces nested elements that look pasted on top.

## How to apply
- Establish a **radius scale** as design tokens, typically 4 steps:
  - `--radius-sm: 4px` — tags, badges, small UI controls.
  - `--radius-md: 8px` — buttons, inputs, small cards.
  - `--radius-lg: 12px` — cards, modals.
  - `--radius-xl: 16–24px` — hero blocks, full-bleed wrappers.
- Apply the **inner-radius formula** for nested elements: `inner-radius = outer-radius - gap`. A 24px outer card with 8px padding contains a 16px-radius inner element.
- Some elements should have **no radius** (sharp corners): tables, code blocks, large editorial blocks. Reserved square corners create contrast with rounded interactive elements.
- Avoid `rounded-full` on cards (only icons / avatars / chips).
- Audit: count the unique border-radius values used across the codebase. If it's only 1–2 values, you have the slop. If it's 8+ values, you have chaos. The right number is 3–5.

## Examples (BAD vs. GOOD pairs)

BAD:
```html
<div class="rounded-2xl">         <!-- card -->
  <button class="rounded-2xl">    <!-- button same radius as parent -->
  <input class="rounded-2xl">     <!-- input same radius -->
  <img class="rounded-2xl">       <!-- image same radius -->
</div>
```

GOOD:
```html
<div class="rounded-2xl">         <!-- 24px outer card -->
  <button class="rounded-md">     <!-- 8px button -->
  <input class="rounded-md">      <!-- 8px input -->
  <img class="rounded-lg">        <!-- 12px image, sized between button and card -->
</div>
```

## Related entries
- `corpus/ux-principles/audit/04-spacing/border-radius-hierarchy.md` — the hierarchy version of this rule.
- `corpus/ux-principles/audit/04-spacing/inner-radius-formula.md` — the math.
- `corpus/brand-system/identity/imagery-anti-patterns.md` — broader catalog.

## Anti-patterns
- `--radius: 16px` as the only token in the system.
- "Bubbly" 24px+ radius on data tables — looks like a candy app.
- Pill-shaped (`rounded-full`) buttons next to pill-shaped cards next to pill-shaped images.
