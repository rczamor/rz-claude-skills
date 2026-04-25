---
name: Image Optimization (lazy, dimensions, WebP/AVIF)
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/06-responsive/responsive-images.md, corpus/ux-principles/audit/10-performance/lcp-target.md, corpus/ux-principles/audit/10-performance/cls-target.md]
---

# Image Optimization

## What it is
Every image must have: `loading="lazy"` for below-the-fold, explicit `width`/`height` attributes, and a modern format (WebP or AVIF with PNG/JPG fallback). Above-the-fold / LCP images additionally need `fetchpriority="high"` and should be preloaded. Together these three controls usually cut image bytes by 60–80% and prevent layout shift.

## Why it matters
Images are the single largest performance lever on most sites — often 70%+ of total page weight. PNG / JPG defaults blow through bandwidth budgets; WebP cuts ~30% off JPG, AVIF cuts ~50%. Missing dimensions cause CLS. Eager-loading every below-the-fold image kills LCP by hogging the network. Three small habits collapse the entire image perf problem.

## How to apply
- **Lazy loading** — `loading="lazy"` on every below-the-fold `<img>`. Browsers handle the rest. Above-the-fold / LCP image gets `fetchpriority="high"` and *not* lazy.
- **Dimensions** — `width` and `height` attributes on every image (HTML attrs, not just CSS). Reserves space, prevents CLS.
- **Format** — serve WebP or AVIF. Most modern build pipelines (Next.js Image, Astro, etc.) handle this automatically. For raw HTML, use `<picture>` with `<source type="image/avif">`, `<source type="image/webp">`, then `<img>` fallback.
- **Decoding** — `decoding="async"` for non-LCP images so decode doesn't block main thread.
- **Compression** — quality 75–80% for photos (visually identical to 100%, half the bytes). Tools: `sharp`, `squoosh`, `imagemin`.
- **Don't ship 4× retina** — at viewport sizes 4× DPR images are wasted bytes; 2× is plenty.

## Examples (BAD vs. GOOD pairs)

BAD:
```html
<img src="/hero.png" alt="hero">
<img src="/feature1.png" alt="feature one">
<img src="/feature2.png" alt="feature two">
<!-- 3MB of PNGs, all eager-loaded, no dimensions -->
```

GOOD:
```html
<!-- LCP / hero -->
<img src="/hero.webp" width="800" height="450" alt="..." fetchpriority="high">

<!-- below-the-fold -->
<picture>
  <source srcset="/feat1.avif" type="image/avif">
  <source srcset="/feat1.webp" type="image/webp">
  <img src="/feat1.jpg" width="600" height="400" loading="lazy" decoding="async" alt="...">
</picture>
```

Or via Next.js Image:
```jsx
<Image src="/feat1.png" width={600} height={400} alt="..." />
{/* Auto: lazy by default, AVIF/WebP, srcset, decoding=async */}
```

## Related entries
- `corpus/ux-principles/audit/06-responsive/responsive-images.md` — srcset/sizes companion.
- `corpus/ux-principles/audit/10-performance/lcp-target.md` — biggest LCP lever.
- `corpus/ux-principles/audit/10-performance/cls-target.md` — dimensions = CLS prevention.

## Anti-patterns
- `loading="lazy"` on the LCP image — kills LCP.
- 4MB PNG hero "for fidelity" — WebP at 75% is visually indistinguishable.
- No dimensions, "we'll let CSS size them" — guarantees CLS.
