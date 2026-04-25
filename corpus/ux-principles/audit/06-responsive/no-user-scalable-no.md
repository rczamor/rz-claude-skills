---
name: Never Disable User Zoom (`user-scalable=no`)
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/06-responsive/text-readable-no-zoom.md, corpus/ux-principles/audit/02-typography/body-min-16px.md]
---

# No `user-scalable=no` or `maximum-scale=1`

## What it is
The viewport meta tag must not block user pinch-zoom. `user-scalable=no`, `maximum-scale=1`, or `maximum-scale=1.0` all disable accessibility zoom. The correct meta is simply: `<meta name="viewport" content="width=device-width, initial-scale=1">`.

## Why it matters
Pinch-zoom is a baseline accessibility affordance — users with low vision rely on it constantly. WCAG 2.1 SC 1.4.4 explicitly requires that text can be resized up to 200% without loss of content or function. Apple, Google, and every screen-reader vendor flag `user-scalable=no` as an accessibility violation. There is no "design reason" worth disabling this — it tells users with vision impairments "you are not welcome here."

## How to apply
- Search the codebase for `user-scalable`, `maximum-scale`, `minimum-scale`. Any hit other than the default = remove.
- The correct viewport meta:
  ```html
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  ```
  `viewport-fit=cover` enables `env(safe-area-inset-*)` for notch devices.
- If your concern is "users will zoom and break the layout," the fix is making your layout robust to zoom — not blocking zoom.
- If iOS auto-zooms on input focus, fix the *input font-size to 16px* (see related entry) — don't suppress zoom globally.

## Examples (BAD vs. GOOD pairs)

BAD:
```html
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
```

GOOD:
```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

## Related entries
- `corpus/ux-principles/audit/06-responsive/text-readable-no-zoom.md` — the right fix for iOS auto-zoom.
- `corpus/ux-principles/audit/02-typography/body-min-16px.md` — minimum body size.

## Anti-patterns
- Copy-pasting a viewport meta from a 2014 boilerplate that locks zoom "for native feel."
- Locking zoom on a "pinch gesture conflicts with our canvas" — solve the gesture conflict differently (e.g., scope canvas to its own touch region).
- Adding `user-scalable=no` "to stop iOS auto-zoom on form focus" — wrong fix, see related rule.
