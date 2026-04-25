---
name: Touch Targets ≥ 44px on All Interactive Elements
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 400-500
related: [corpus/ux-principles/principles/mobile-same-rules-higher-stakes.md, corpus/ux-principles/audit/06-responsive/touch-targets-mobile-44.md, corpus/ux-principles/audit/05-interaction/cursor-pointer.md]
---

# Touch Targets ≥ 44px on All Interactive Elements

## What it is

Every tappable element — button, link, icon button, form field — must be at least 44×44 pixels. This is Apple's Human Interface Guidelines minimum and aligns with Material Design and WCAG 2.5.5 (Target Size Level AAA at 44×44, Level AA at 24×24).

This applies to the touch target, not necessarily the visible element. A small icon (16×16) in a button with 14px padding has a 44×44 touch target. Visible decoration can be smaller; the hit area cannot.

## Why it matters

A finger pad is roughly 10mm wide. Smaller targets produce mistaps — the user hits the wrong link, the wrong icon, the X button instead of the menu. Mistaps are especially frustrating because the user knows they aimed correctly; the interface punished them for having normal-sized fingers.

This is a hard requirement on mobile. On desktop with mouse, smaller targets are tolerable but still risky for fine motor control.

## How to apply

1. **Set minimum size on interactive elements:**
   ```css
   button, a, [role="button"] {
     min-width: 44px;
     min-height: 44px;
   }
   ```
2. **Or use padding to expand the hit area** without changing visual size:
   ```css
   .icon-button {
     padding: 14px;  /* 16px icon + 14px padding × 2 = 44px */
   }
   ```
3. **Audit:** select all interactive elements and check `getBoundingClientRect()` — width and height ≥ 44.
4. **Spacing between targets matters too** — 8px minimum between adjacent targets to prevent overlap.
5. **Inline links** in body text are a partial exception (they inherit text height), but if the link is the primary action, expand it.

## Examples

- **GOOD:** A close button that's 16×16 visually but has 14px padding for a 44×44 hit area.
- **BAD:** Three icon buttons in a row, each 24×24 with 4px gap. Mistaps guaranteed.
- **GOOD:** A "Buy now" button at 48×200px. Finger lands cleanly anywhere on it.
- **BAD:** A 12×12 social media icon as a tappable link. Almost impossible to hit on mobile.

## Related entries

- `corpus/ux-principles/principles/mobile-same-rules-higher-stakes.md`
- `corpus/ux-principles/audit/06-responsive/touch-targets-mobile-44.md`
- `corpus/ux-principles/audit/05-interaction/cursor-pointer.md`

## Anti-patterns

- Cramming icon toolbars at 24×24 to fit more icons. Use a grid view or a menu instead.
- Tiny text links inside body copy as the only path to a key action. Make the action a button.
