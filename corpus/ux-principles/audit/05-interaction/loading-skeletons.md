---
name: Loading — Skeleton Shapes Match Real Content Layout
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 400-500
related: [corpus/ux-principles/audit/10-performance/skeleton-quality.md, corpus/ux-principles/audit/10-performance/cls-target.md, corpus/ux-principles/audit/05-interaction/empty-states.md]
---

# Loading — Skeleton Shapes Match Real Content Layout

## What it is

When content is loading, show a skeleton (gray rectangles in the shape of the content that's coming) — not a generic spinner. The skeleton shapes should approximate the dimensions, position, and structure of the real content. When real content arrives, it slides into the same space the skeleton occupied, with no layout shift.

A skeleton signals "content is loading here, in this shape" — much more informative than a spinner that signals "wait."

## Why it matters

Spinners produce a feeling of "the system is doing something, I have no idea what or how long." Skeletons produce "the system is loading my dashboard, I can see where the cards will be." Skeletons also prevent CLS (Cumulative Layout Shift) — when real content arrives, it doesn't push other elements around.

Even better: skeletons make perceived performance feel faster. Users wait less anxiously when they can see the shape of what's coming.

## How to apply

1. **Match dimensions of real content.** A card that will be 280×180px → skeleton at 280×180px. Heading text that will be 32px tall → skeleton at 32px tall.
2. **Use a subtle shimmer animation.** A linear gradient that animates left-to-right tells the user "this is loading, not just empty."
   ```css
   .skeleton {
     background: linear-gradient(90deg, #eee 25%, #f5f5f5 50%, #eee 75%);
     background-size: 200% 100%;
     animation: shimmer 1.5s infinite;
   }
   @keyframes shimmer {
     0% { background-position: 200% 0; }
     100% { background-position: -200% 0; }
   }
   ```
3. **Skeleton color appropriate to mode.** Light mode: `#eee` to `#f5f5f5`. Dark mode: `#1f1f1f` to `#2a2a2a`.
4. **Don't show skeletons for sub-100ms loads.** Flash of skeleton looks broken. Use `setTimeout(showSkeleton, 100)` to delay.

## Examples

- **GOOD:** A list of 5 cards loading — show 5 skeleton cards with the same dimensions and the same internal structure (avatar circle, title bar, body lines).
- **BAD:** A spinner in the center of the viewport while a complex dashboard loads. User sees a void with a spinner, then the page snaps in.
- **GOOD:** Facebook / LinkedIn news feed loading skeleton — gray boxes shaped like posts. Users know what's coming.
- **BAD:** A blank page with a centered "Loading..." text. Generic, unhelpful.

## Related entries

- `corpus/ux-principles/audit/10-performance/skeleton-quality.md`
- `corpus/ux-principles/audit/10-performance/cls-target.md`
- `corpus/ux-principles/audit/05-interaction/empty-states.md`

## Anti-patterns

- Generic spinners for content that takes >300ms to load. Use skeletons.
- Skeleton shapes that don't match real content — small skeleton cards, then real cards 3x bigger jump in.
