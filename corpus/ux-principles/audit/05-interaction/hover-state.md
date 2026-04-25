---
name: Hover State on All Interactive Elements
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/05-interaction/cursor-pointer.md, corpus/ux-principles/audit/05-interaction/focus-visible-ring.md, corpus/ux-principles/principles/billboard-design-overview.md]
---

# Hover State on All Interactive Elements

## What it is

Every interactive element — button, link, card, dropdown trigger, icon button, clickable row — must have a visible hover state. The hover state confirms to the user "this is interactive." It is not the only signal of interactivity (see `billboard-design-overview` for why hover alone is insufficient on mobile), but on desktop it's a basic affordance.

Hover states should be subtle — color shift, slight elevation, underline appearing — not dramatic.

## Why it matters

Without hover states, the user can't confirm an element is clickable until they actually click. They hover, see no response, and assume it's static. They click anyway, sometimes correctly, sometimes not — but the experience feels unresponsive.

Hover is also the primary way desktop users explore — moving the cursor across the page builds a mental map of what's interactive. Static elements feel dead.

## How to apply

1. **Add `:hover` styles to every interactive element:**
   ```css
   .button:hover { background: var(--color-primary-darker); }
   .card:hover { box-shadow: var(--shadow-md); transform: translateY(-1px); }
   a:hover { color: var(--color-primary-darker); text-decoration: underline; }
   ```
2. **Keep changes subtle.** Color darken/lighten by 5-10%, slight elevation, an underline appearing. Not full-color flashes.
3. **Don't rely on hover alone for discoverability** — especially on mobile, where hover doesn't exist. The element should already look clickable.
4. **Audit:** mouse over every interactive element on the page. Does each respond? If not, add hover style.

## Examples

- **GOOD:** A button that darkens by 8% on hover. Confirms interactivity, doesn't startle.
- **BAD:** A "Click here" text link with no underline, no color change, no hover state. Looks like body text.
- **GOOD:** A card row that gets a subtle background color on hover (`background: var(--color-surface-hover)`), telling the user "this row is clickable."
- **BAD:** A clickable card that has no hover state and an `onClick` handler that requires the user to know it's clickable.

## Related entries

- `corpus/ux-principles/audit/05-interaction/cursor-pointer.md`
- `corpus/ux-principles/audit/05-interaction/focus-visible-ring.md`
- `corpus/ux-principles/principles/billboard-design-overview.md`

## Anti-patterns

- Using only `cursor: pointer` and no visual hover. Cursor change is too subtle on its own.
- Hover effects so dramatic they distract — full background flips, scale jumps, animations.
