---
name: CLS < 0.1 (No Visible Layout Shifts During Load)
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/10-performance/lcp-target.md, corpus/ux-principles/audit/06-responsive/responsive-images.md, corpus/evaluation-frameworks/review-sections/07-performance.md]
---

# CLS < 0.1

## What it is
**Cumulative Layout Shift < 0.1** — no visible jank, jumps, or content reflow as the page loads. CLS measures the unexpected movement of visible elements during page lifetime. Google's "Good" threshold is 0.1; the "Poor" threshold is 0.25. Below 0.1 the page feels solid; above it the page feels broken even if it's fast.

## Why it matters
CLS captures the misery moment when the user is about to tap a button and the layout shifts, sending them to the wrong tap target. It's the most viscerally annoying performance failure — even users who can't articulate "your CLS is 0.32" know that the page "felt off." Common offenders: images without dimensions, web fonts without size-adjust, late-loading ads or banners pushing content down.

## How to apply
- **Always set `width` and `height`** (or `aspect-ratio` in CSS) on every `<img>`, `<video>`, `<iframe>`. Reserves space; prevents shift on load.
- **Reserve space for dynamic content** — if a banner / cookie notice / ad will appear, render its container at full dimensions before the content arrives, even if empty.
- **Web fonts** — use `font-display: swap` plus `size-adjust`, `ascent-override`, `descent-override`, and `line-gap-override` (or use a font with a metrics-matched fallback) to prevent the text-jump when the custom font loads.
- **Skeleton screens** must match the layout of the real content (`audit/10-performance/skeleton-quality.md`) — wrong-shaped skeletons cause shift on swap-in.
- **Inserted content** — never insert content above the fold after first paint unless it's user-initiated (e.g., user taps "show more" — that's expected motion).
- Measure with DevTools → Performance Insights → Layout Shifts; in production via CrUX or Vercel Speed Insights.

## Examples (BAD vs. GOOD pairs)

BAD:
```html
<img src="/hero.png" alt="hero">
<!-- no width/height, layout shifts when image loads -->

<div id="banner-slot"></div>
<!-- empty until JS inserts a 60px banner; everything below jumps -->
```

GOOD:
```html
<img src="/hero.webp" width="800" height="450" alt="hero">
<!-- aspect ratio preserved; no shift on load -->

<div id="banner-slot" style="min-height: 60px"></div>
<!-- space reserved before banner inserts -->
```

For fonts:
```css
@font-face {
  font-family: 'Söhne';
  src: url(/fonts/sohne.woff2) format('woff2');
  font-display: swap;
  size-adjust: 102%;
  ascent-override: 90%;
  descent-override: 22%;
}
```

## Related entries
- `corpus/ux-principles/audit/10-performance/lcp-target.md` — sibling Core Web Vital.
- `corpus/ux-principles/audit/06-responsive/responsive-images.md` — image dimensions = CLS prevention.
- `corpus/evaluation-frameworks/review-sections/07-performance.md` — broader perf review.

## Anti-patterns
- Images without dimensions "because we'll set them later."
- Late-loading hero text that swaps in after the LCP image, jumping the layout.
- Cookie banner that pushes content down 80px after first paint.
