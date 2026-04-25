---
name: Border-Radius Hierarchy — Not Uniform Bubbly Radius on Everything
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/04-spacing/inner-radius-formula.md, corpus/ux-principles/audit/09-ai-slop/uniform-bubbly-radius.md]
---

# Border-Radius Hierarchy — Not Uniform Bubbly Radius on Everything

## What it is

Border-radius should follow a hierarchy: small for inputs and buttons (4-8px), medium for cards and panels (8-12px), larger for feature blocks (16-24px) where appropriate. Pills are special-case (50% / fully rounded). Different element types call for different radii.

Applying the same large radius (e.g., `border-radius: 16px`) to every element — buttons, inputs, cards, modals, images — produces the "bubbly" SaaS template look. It is the most common AI-generated design tell.

## Why it matters

Radius carries visual hierarchy like size and weight. A button with a large radius and a card with a large radius and an image with a large radius produces a uniform "everything's a soft blob" feel. Differentiated radii make the system more legible: small radius = small element, larger radius = larger element, no radius = sharp.

## How to apply

1. **Define a radius scale:**
   - `--radius-sm: 4px;` (small inputs, badges)
   - `--radius-md: 8px;` (buttons, cards)
   - `--radius-lg: 12px;` (panels)
   - `--radius-xl: 24px;` (hero containers, feature blocks)
   - `--radius-full: 9999px;` (pills, avatars)
2. **Don't use the same radius everywhere.** A button at 8px, a card at 12px, an image at 4px is fine.
3. **Match radius to element size.** Tiny buttons get 4px; large cards get 12-16px. A 24px radius on a 32px button looks comically bubbly.
4. **Or: use no radius.** Sharp corners are a deliberate choice and look distinctive (Linear, Stripe).

## Examples

- **GOOD:** Inputs `4px`, buttons `8px`, cards `12px`, images `8px`. Hierarchy.
- **BAD:** Everything at `border-radius: 16px;` — buttons, inputs, cards, images. The "bubbly SaaS" look.
- **GOOD:** Linear's UI — minimal radius (`4px`) on most things; signals precision.
- **BAD:** A landing page with `border-radius: 24px` on every element — pills feel correct, but cards look like jellybeans.

## Related entries

- `corpus/ux-principles/audit/04-spacing/inner-radius-formula.md`
- `corpus/ux-principles/audit/09-ai-slop/uniform-bubbly-radius.md` — the AI slop version

## Anti-patterns

- Uniform `border-radius` token applied to every element via global CSS reset. Indicates no hierarchy thinking.
- Using huge radii to "feel friendly." Friendly is a personality, not a 24px corner.
