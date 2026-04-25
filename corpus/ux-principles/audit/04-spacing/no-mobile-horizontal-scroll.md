---
name: No Horizontal Scroll on Mobile
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/06-responsive/no-horizontal-scroll.md, corpus/ux-principles/principles/mobile-same-rules-higher-stakes.md]
---

# No Horizontal Scroll on Mobile

## What it is

On mobile viewports (≤768px), the page should never scroll horizontally. The user should be able to scroll vertically only. Horizontal scroll on mobile happens when an element is wider than the viewport — most often: an image without `max-width: 100%`, a `min-width` set somewhere, a pre/code block, or an overflowing flex/grid container.

## Why it matters

Horizontal scroll on mobile is one of the most disorienting UX failures. The user swipes vertically, the page jerks horizontally, content disappears off-screen, and the user loses their place. It signals "we didn't test on mobile" and drains the goodwill reservoir instantly.

## How to apply

1. **Audit:** load the page on a 375px viewport (Chrome DevTools mobile emulation). Try to scroll horizontally. If the page moves, find the offender.
2. **Common fixes:**
   ```css
   img, video { max-width: 100%; height: auto; }
   pre, code { overflow-x: auto; max-width: 100%; }
   .container { overflow-x: hidden; }
   ```
3. **Don't use `overflow-x: hidden` on the body** to "fix" it — that masks the underlying bug. Find what's overflowing and constrain it.
4. **Test responsive breakpoints individually.** Sometimes the issue only appears at 320px or 375px.

## Examples

- **GOOD:** Body fits within 375px viewport. All images, code blocks, tables either fit or scroll within their container.
- **BAD:** A blog post with a 600px-wide image. On mobile, page scrolls horizontally to reveal it.
- **GOOD:** A wide table in `<div style="overflow-x: auto;">` — table can scroll horizontally inside its container, page does not.
- **BAD:** A flex container with no wrapping that pushes its children off-screen on mobile.

## Related entries

- `corpus/ux-principles/audit/06-responsive/no-horizontal-scroll.md` — the all-viewport version
- `corpus/ux-principles/principles/mobile-same-rules-higher-stakes.md`

## Anti-patterns

- Setting `overflow-x: hidden` on the body to silence the symptom. Bug is still there.
- Hardcoded `min-width` values on layouts that need to be responsive.
