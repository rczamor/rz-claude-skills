---
name: Responsive Images (srcset / sizes / containment)
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/10-performance/image-optimization.md, corpus/ux-principles/audit/10-performance/lcp-target.md]
---

# Responsive Images

## What it is
Images must adapt to viewport size and device pixel ratio. Use `srcset` and `sizes` so the browser picks the right asset, set explicit `width` and `height` so layout doesn't shift, and apply CSS containment for above-the-fold images that drive LCP.

## Why it matters
Serving a 2400px hero to a 375px iPhone wastes 5–10× the bytes, ruins LCP, and crushes data-capped users. Conversely, scaling a 400px image up to 1440px is blurry. Without explicit dimensions, the layout shifts as images load (CLS penalty). Responsive images are the single biggest performance lever on most marketing sites.

## How to apply
- Use `<img srcset="hero-400.jpg 400w, hero-800.jpg 800w, hero-1600.jpg 1600w" sizes="(max-width: 600px) 100vw, 50vw" width="800" height="450" alt="...">` — sizes describes layout, srcset provides candidates.
- For art-direction (different *crop* per breakpoint, not just different size), use `<picture>` with `<source media="(max-width: 600px)">`.
- Always set `width` and `height` attributes (or `aspect-ratio` in CSS) — reserves space and prevents CLS.
- Use modern formats — WebP or AVIF — with fallback. Modern build tools generate these automatically.
- Lazy-load below-the-fold: `loading="lazy"`. Eager-load LCP image: `fetchpriority="high"`.

## Examples (BAD vs. GOOD pairs)

BAD:
```html
<img src="/hero.png" alt="hero">
<!-- one 2400px PNG served to every device, no dimensions, CLS guaranteed -->
```

GOOD:
```html
<img
  src="/hero-800.webp"
  srcset="/hero-400.webp 400w, /hero-800.webp 800w, /hero-1600.webp 1600w"
  sizes="(max-width: 600px) 100vw, 800px"
  width="800"
  height="450"
  fetchpriority="high"
  alt="Product dashboard showing live metrics">
```

## Related entries
- `corpus/ux-principles/audit/10-performance/image-optimization.md` — the perf-side rule.
- `corpus/ux-principles/audit/10-performance/lcp-target.md` — why this rolls up to LCP.

## Anti-patterns
- One 4K PNG used everywhere "because it's only one file."
- `<img>` without `width`/`height` — every image causes a layout shift on load.
- `loading="lazy"` on the LCP image — delays the very element you're being scored on.
