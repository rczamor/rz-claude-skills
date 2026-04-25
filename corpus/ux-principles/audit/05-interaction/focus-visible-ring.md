---
name: focus-visible Ring — Never outline:none Without Replacement
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 400-500
related: [corpus/ux-principles/audit/05-interaction/hover-state.md, corpus/ux-principles/audit/03-color/wcag-aa-contrast.md]
---

# focus-visible Ring — Never outline:none Without Replacement

## What it is

Every interactive element must have a visible focus indicator when focused via keyboard. The browser provides this by default (`outline: 1px auto`), but most designers consider the default ugly and remove it with `outline: none`. **Removing the outline without providing a replacement is a critical accessibility failure** — keyboard users can't tell where focus is.

The fix: use `:focus-visible` (which only activates on keyboard focus, not mouse click) and apply a deliberate, designed focus ring.

## Why it matters

Keyboard navigation is essential for:

- Users with motor impairments (can't use a mouse precisely)
- Screen reader users (navigate by Tab)
- Power users (Tab is faster than mouse for forms)
- Anyone whose mouse has died

Without a visible focus indicator, these users are navigating blind. They Tab through the page and have no idea which element is selected. WCAG 2.1 requires a focus indicator (Success Criterion 2.4.7).

## How to apply

1. **Use `:focus-visible`, not `:focus`.** `focus-visible` only triggers for keyboard focus, so mouse clicks don't show the ring.
2. **Design a deliberate focus style:**
   ```css
   *:focus-visible {
     outline: 2px solid var(--color-focus);
     outline-offset: 2px;
   }
   ```
   Or with box-shadow for more flexibility:
   ```css
   *:focus-visible {
     outline: none;
     box-shadow: 0 0 0 2px var(--color-focus);
   }
   ```
3. **Make sure the focus color has 3:1 contrast against adjacent colors** (UI component requirement).
4. **Never `outline: 0` or `outline: none` globally** without a replacement. If you must remove it, replace immediately.
5. **Audit:** Tab through the page. Can you see where focus is at every step? If no, fix.

## Examples

- **GOOD CSS:**
  ```css
  button:focus-visible {
    outline: 2px solid #3B82F6;
    outline-offset: 2px;
  }
  ```
- **BAD:**
  ```css
  *:focus { outline: none; }
  ```
  No replacement. Keyboard users navigate invisibly.
- **GOOD:** Stripe's docs — Tab through, every focused element has a visible blue ring.
- **BAD:** A "polished" SaaS app where every element has `outline: none` because the designer found it ugly. Keyboard navigation completely broken.

## Related entries

- `corpus/ux-principles/audit/05-interaction/hover-state.md`
- `corpus/ux-principles/audit/03-color/wcag-aa-contrast.md`

## Anti-patterns

- `*:focus { outline: none; }` reset. Worst-in-class accessibility hostile pattern.
- Setting focus styles that match the hover style — no distinction means keyboard users can't tell what's focused vs. just hovered.
