---
name: cursor:pointer on All Clickable Elements
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/05-interaction/hover-state.md, corpus/ux-principles/audit/05-interaction/disabled-state.md]
---

# cursor:pointer on All Clickable Elements

## What it is

Every clickable element should show `cursor: pointer` on hover. This is the small hand icon that signals "this is interactive." Browsers do this by default for `<a>` tags but not for `<button>`, `<div onClick>`, or other custom interactive elements.

The fix is one line of CSS, but it's commonly forgotten on custom interactive elements.

## Why it matters

The cursor change is a small but expected affordance signal. Users mouse over an element; the cursor turns into a pointer; the user thinks "ah, clickable." Without the cursor change, the user pauses to verify by other means (color, shape) — or doesn't realize it's clickable at all.

This is a polish issue with a one-line fix. There is no excuse to ship without it.

## How to apply

1. **CSS:**
   ```css
   button, a, [role="button"], .clickable {
     cursor: pointer;
   }
   ```
2. **For disabled elements,** use `cursor: not-allowed` instead.
3. **Audit:** mouse over every interactive element. Does the cursor change to a pointer? If no, fix.
4. **Tailwind:** `cursor-pointer` utility class.

## Examples

- **GOOD:**
  ```css
  button { cursor: pointer; }
  ```
  Or in JSX: `<div className="cursor-pointer" onClick={...}>`
- **BAD:** A custom `<div onClick={...}>` styled as a button but with default cursor (text I-beam). Looks broken.
- **GOOD:** A clickable card with `cursor: pointer` — user knows they can click anywhere on it.
- **BAD:** A clickable card without cursor:pointer; user mouses over, sees text-cursor, assumes it's not interactive.

## Related entries

- `corpus/ux-principles/audit/05-interaction/hover-state.md`
- `corpus/ux-principles/audit/05-interaction/disabled-state.md`

## Anti-patterns

- Forgetting cursor:pointer on custom click handlers (`<div onClick>`). Always add it.
- Using cursor:pointer on non-interactive text to "make it feel important." Misleading.
