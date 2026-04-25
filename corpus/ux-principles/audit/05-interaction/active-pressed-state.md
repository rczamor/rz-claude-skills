---
name: Active / Pressed State — Depth or Color Shift on Press
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/05-interaction/hover-state.md, corpus/ux-principles/audit/05-interaction/focus-visible-ring.md]
---

# Active / Pressed State — Depth or Color Shift on Press

## What it is

When a user clicks/taps an interactive element, it should provide immediate visual feedback during the press: a slight color darkening, a small scale-down (`transform: scale(0.98)`), or both. The CSS pseudo-class is `:active`. This is the "I felt your tap" signal.

Without an active state, clicks feel laggy or unconfirmed — the user isn't sure if their tap registered until the action completes (which may take milliseconds or seconds). With an active state, every tap feels solid.

## Why it matters

Tactile feedback is what makes physical buttons satisfying. Software buttons that don't replicate this feel "soft" and unresponsive. The active state is especially critical on touch devices, where there's no hover state to confirm interactivity — the press itself becomes the entire feedback loop.

## How to apply

1. **CSS:**
   ```css
   button:active {
     background: var(--color-primary-pressed);
     transform: translateY(1px);
   }
   ```
   Or with scale:
   ```css
   button:active {
     transform: scale(0.98);
     filter: brightness(0.92);
   }
   ```
2. **Keep duration tight.** Active state lasts only as long as the press, so transitions should be near-instant or very short (~50ms).
3. **Combine with hover.** Hover → slightly darker; active → noticeably darker. Three states: rest → hover → active.
4. **Audit:** click/tap every interactive element. Is there a visible "I felt that" response?

## Examples

- **GOOD:** A primary button that darkens by 15% and pushes 1px down on `:active`. Tactile.
- **BAD:** A flat button that looks identical when pressed. Feels broken.
- **GOOD:** iOS-style button: scale down to 0.95 on press, return on release. Highly tactile.
- **BAD:** A button with a 500ms transition on `:active` so the press effect lags noticeably behind the click.

## Related entries

- `corpus/ux-principles/audit/05-interaction/hover-state.md`
- `corpus/ux-principles/audit/05-interaction/focus-visible-ring.md`

## Anti-patterns

- Forgetting `:active` and shipping without tactile feedback. Especially obvious on mobile.
- Active states that are too dramatic — full color flips, large scale changes that feel overwrought.
