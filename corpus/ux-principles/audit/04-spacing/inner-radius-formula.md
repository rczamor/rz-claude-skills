---
name: Inner Radius Formula — Inner = Outer - Gap (Nested Elements)
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/04-spacing/border-radius-hierarchy.md]
---

# Inner Radius Formula — Inner = Outer - Gap (Nested Elements)

## What it is

When one rounded element is nested inside another (a card inside a panel, a button inside a card), the inner element's border-radius should equal the outer's radius minus the gap between them. The formula: `inner_radius = outer_radius - gap`.

Why: this keeps the curves visually concentric. If outer is 16px radius and there's an 8px gap, the inner should be 8px radius. The two arcs share a center, looking intentional. If both are 16px, the gap looks wider at corners than along edges — a small but noticeable visual bug.

## Why it matters

Concentric curves look polished; non-concentric curves look amateurish. Most teams don't notice this until it's pointed out, then they notice it everywhere. It's the kind of detail that separates "designed" products from "assembled" ones.

## How to apply

1. **Outer container:** define its radius (e.g., 16px) and inner padding (e.g., 8px).
2. **Inner element radius:** `inner = outer - padding` = 16 - 8 = 8px.
3. **As CSS variables:**
   ```css
   .card {
     --card-radius: 16px;
     --card-padding: 8px;
     border-radius: var(--card-radius);
     padding: var(--card-padding);
   }
   .card .inner {
     border-radius: calc(var(--card-radius) - var(--card-padding));
   }
   ```
4. **Audit:** anywhere a rounded element nests inside another rounded element, check the formula.

## Examples

- **GOOD:** Card with `border-radius: 16px; padding: 8px;` containing a nested image with `border-radius: 8px`. Curves concentric, looks intentional.
- **BAD:** Same card and image, both with `border-radius: 16px`. The image's corners look "tight" at the corners while the card's corners look "loose" — inconsistent visual gap.
- **GOOD:** iOS app icons in a folder — outer folder radius matches inner icon radius with the right gap. Apple obsessively maintains this.
- **BAD:** A button at `border-radius: 8px` inside a card at `border-radius: 8px` with `padding: 16px`. Should be inner radius `0` (or smaller).

## Related entries

- `corpus/ux-principles/audit/04-spacing/border-radius-hierarchy.md`

## Anti-patterns

- Applying the same radius to nested elements regardless of nesting. Common cargo-cult mistake.
- "It's close enough." It's not — the eye picks up non-concentric curves immediately, even at small sizes.
