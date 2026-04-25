---
name: Safe Area Insets — env(safe-area-inset-*) for Notch Devices
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/06-responsive/no-user-scalable-no.md, corpus/ux-principles/principles/mobile-same-rules-higher-stakes.md]
---

# Safe Area Insets — env(safe-area-inset-*) for Notch Devices

## What it is

Modern phones (iPhone X+ with notch, Android with punch-hole or rounded corners) reserve part of the screen for system UI. CSS provides `env(safe-area-inset-top)`, `env(safe-area-inset-right)`, `env(safe-area-inset-bottom)`, `env(safe-area-inset-left)` — values representing how much padding is needed to avoid system UI obstruction.

Sticky headers, bottom nav bars, fixed toolbars — anything pinned to the edge of the screen — must respect these insets, or it ends up obscured by the notch, home indicator, or rounded corner.

## Why it matters

A bottom nav bar that ignores safe-area-inset-bottom on iPhone X+ has its tap targets partially hidden behind the home indicator. A sticky header that ignores safe-area-inset-top can be partially obscured by the notch. Users adapt and tap awkwardly, but it's a polish failure that signals the team didn't test on real devices.

## How to apply

1. **Required meta tag:**
   ```html
   <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
   ```
   The `viewport-fit=cover` is what enables safe-area-inset to actually return values.
2. **Apply to fixed elements:**
   ```css
   .bottom-nav {
     padding-bottom: env(safe-area-inset-bottom);
   }
   .sticky-header {
     padding-top: env(safe-area-inset-top);
   }
   ```
3. **Combine with existing padding:**
   ```css
   padding-bottom: max(16px, env(safe-area-inset-bottom));
   ```
4. **Test on actual notched devices** or via Chrome DevTools' device emulation with notch simulation.

## Examples

- **GOOD:** A bottom tab bar with `padding-bottom: env(safe-area-inset-bottom);` — sits above the home indicator, fully tappable.
- **BAD:** A bottom nav with `padding-bottom: 16px;` only. On iPhone X+, the bottom 8px of the nav is behind the home indicator.
- **GOOD:** A full-screen modal that respects insets on all four sides for landscape orientation on notched devices.
- **BAD:** A sticky banner at top with no `padding-top: env(safe-area-inset-top)`. On a notched phone, banner content can be clipped by the notch.

## Related entries

- `corpus/ux-principles/audit/06-responsive/no-user-scalable-no.md`
- `corpus/ux-principles/principles/mobile-same-rules-higher-stakes.md`

## Anti-patterns

- Forgetting `viewport-fit=cover` and wondering why `env(safe-area-inset-*)` returns 0.
- Hardcoding bottom padding to "an amount that looks right on iPhone X" without using the env variable.
