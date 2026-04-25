---
name: Dark Mode — Surfaces Use Elevation, Not Just Lightness Inversion
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 400-500
related: [corpus/ux-principles/audit/03-color/dark-mode-text-off-white.md, corpus/ux-principles/audit/03-color/dark-mode-accent-desaturated.md, corpus/ux-principles/audit/03-color/color-scheme-html.md]
---

# Dark Mode — Surfaces Use Elevation, Not Just Lightness Inversion

## What it is

In dark mode, surfaces should be differentiated by elevation — lighter colors indicate higher elevation, darker colors indicate the base. This inverts the "shadow as elevation" pattern of light mode (where shadows imply elevation) into "lighter surface = higher elevation."

Critically, this does NOT mean inverting the entire palette: white → black, gray-100 → gray-900, etc. Pure inversion produces washed-out interfaces with no clear hierarchy. Material Design's dark theme spec is the canonical reference: base surface ~`#121212`, elevation +1 ~`#1E1E1E`, +2 ~`#222`, +3 ~`#252525`, etc.

## Why it matters

A dark mode that just inverts lightness produces uniform-looking dark screens with no visible elevation. Cards, modals, and floating elements lose their separation from the page. Users can't tell what's clickable, what's content, what's chrome.

Real dark modes use a layered surface system — each level slightly lighter than the one below — to create perceived depth without shadows (which don't show on dark backgrounds).

## How to apply

1. **Define a surface scale** in dark mode:
   - `--surface-base: #121212;` (page background)
   - `--surface-1: #1E1E1E;` (cards)
   - `--surface-2: #232323;` (elevated cards, modals)
   - `--surface-3: #2A2A2A;` (popovers, tooltips)
2. **Use these tokens** instead of inverting light-mode colors.
3. **Don't use pure black `#000`.** It's too harsh, eats shadows, and looks "off." Material Design recommends `#121212` as the darkest surface.
4. **Don't use pure white `#FFFFFF` text** on dark surfaces (see `dark-mode-text-off-white`).

## Examples

- **GOOD:** Stripe Dashboard dark mode — page `#0A0A0A`, cards lift to `#1A1A1A`, modals to `#262626`. Clear depth.
- **BAD:** A site that toggles dark mode by inverting every color literally. Cards are now `#FFF` → `#000` text on `#000` page → invisible borders.
- **GOOD:** Tailwind's docs dark mode — base near-black, surfaces step up in lightness, accents desaturated.
- **BAD:** A "dark mode" that's actually `#222` everywhere with no elevation tokens. Everything feels flat.

## Related entries

- `corpus/ux-principles/audit/03-color/dark-mode-text-off-white.md`
- `corpus/ux-principles/audit/03-color/dark-mode-accent-desaturated.md`
- `corpus/ux-principles/audit/03-color/color-scheme-html.md`

## Anti-patterns

- Designing dark mode by inverting hex values automatically (CSS `filter: invert()`). Produces images-inverted, weird-tinted nightmare.
- Using pure black `#000` as the base. Too harsh, no room for elevation lower.
