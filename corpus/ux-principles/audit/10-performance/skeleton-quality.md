---
name: Skeleton Quality — Match Real Layout, Subtle Shimmer
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/05-interaction/loading-skeletons.md, corpus/ux-principles/audit/10-performance/cls-target.md]
---

# Skeleton Quality

## What it is
Skeleton screens (loading placeholders) must (a) match the *shape* of the real content they're replacing — same number of rows, similar widths, similar element placement — and (b) animate with a subtle shimmer to communicate liveness. Generic gray rectangles in random arrangements feel cheap and cause CLS when real content swaps in.

## Why it matters
A high-quality skeleton makes the wait feel intentional and shorter. The user's eye traces the same shape it will land on when content arrives, so the swap is invisible — no layout shift, no re-orientation. A bad skeleton creates *two* moments of failure: first the wrong shape registers as broken, then the swap-in causes visual jank. The shimmer animation tells the user "we're working," distinguishing loading from frozen.

## How to apply
- Match real content: 3 rows of skeleton if there will be 3 rows of content. Avatar circle if there's an avatar. Title bar of approximately the right width.
- Don't try to be exactly accurate (different real content widths) — use a few standard widths (60%, 80%, 100%) randomly assigned, plus a small jitter so it doesn't feel mechanical.
- Use neutral background color (`#E5E7EB` light / `#27272A` dark), not pure gray. Subtle.
- Shimmer animation:
  ```css
  @keyframes shimmer {
    from { background-position: -200% 0; }
    to { background-position: 200% 0; }
  }
  .skeleton {
    background: linear-gradient(90deg, #E5E7EB 0%, #F3F4F6 50%, #E5E7EB 100%);
    background-size: 200% 100%;
    animation: shimmer 1.6s infinite linear;
    border-radius: 4px;
  }
  ```
- Respect `prefers-reduced-motion` — replace shimmer with a static opacity pulse or no animation.
- Skeleton should appear only after a delay (e.g., 100–200ms) — if data is cached, you don't want the skeleton flash.
- For lists: render N=4–6 skeleton items, not N=20. Enough to communicate "list coming," not enough to look exhaustive.

## Examples (BAD vs. GOOD pairs)

BAD: a single full-width gray bar with no animation, sitting where a complex card grid will load. When real content arrives, the layout reflows by 600px and CLS spikes.

GOOD: a 3-card skeleton matching the future grid, each with a 4:3 image rectangle, a 60%-width title bar, two 100%/80% description lines, all shimmering at 1.6s — when real content arrives, only the colors and text fill in.

## Related entries
- `corpus/ux-principles/audit/05-interaction/loading-skeletons.md` — interaction-state version.
- `corpus/ux-principles/audit/10-performance/cls-target.md` — bad skeletons cause CLS.

## Anti-patterns
- Generic Lottie animation "Loading..." when a skeleton would match the real layout.
- Spinner with no skeleton — okay for actions, bad for content surfaces.
- Skeletons that take longer than the real content would have — over-engineered.
