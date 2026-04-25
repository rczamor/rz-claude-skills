---
name: LCP Target (< 2.0s web apps, < 1.5s informational)
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/evaluation-frameworks/review-sections/07-performance.md, corpus/ux-principles/audit/06-responsive/responsive-images.md, corpus/ux-principles/audit/10-performance/cls-target.md]
---

# Largest Contentful Paint (LCP) Target

## What it is
**LCP < 2.0s for web apps; LCP < 1.5s for informational sites.** Largest Contentful Paint measures the time from navigation start until the largest visible content element (typically the hero image or hero text block) is painted. It is the Core Web Vital that most directly correlates with perceived loading speed, and Google's "Good" threshold is 2.5s — your bar should be more aggressive.

## Why it matters
LCP is the moment the user *believes* the page has loaded. Below ~1.5s feels instant; above ~2.5s users start tab-switching or hitting back. For informational sites (blog, marketing, docs), LCP is the conversion moment — the bar is tighter. For web apps, the user has decided to be there, but every 100ms of LCP costs measurable engagement. Below 2.0s is table stakes; below 1.5s feels premium.

## How to apply
- Identify the LCP element in DevTools → Performance → Performance Insights → LCP. Usually it's the hero image, hero h1, or product screenshot above the fold.
- For LCP images: `fetchpriority="high"`, eager loading, served as WebP/AVIF, sized correctly via srcset/sizes (`audit/06-responsive/responsive-images.md`).
- Preconnect to the image / font CDN: `<link rel="preconnect" href="https://cdn.example.com" crossorigin>`.
- Preload the LCP image: `<link rel="preload" as="image" href="/hero.webp" imagesrcset="..." imagesizes="...">`.
- Critical CSS inline (above-the-fold styles in `<head>`); rest deferred.
- No render-blocking JS in `<head>` — defer or async every script that doesn't need to run before paint.
- Test on slow 4G + mid-tier device (Moto G4 in DevTools throttling), not just on your fiber + M3 MacBook.
- Lighthouse / WebPageTest / RUM data via CrUX or Vercel Speed Insights — measure in production, not just lab.

## Examples (BAD vs. GOOD pairs)

BAD: hero image lazy-loaded behind a font that doesn't render until 2.8s due to FOIT, with two third-party scripts blocking render. LCP = 3.4s on a Moto G4.

GOOD:
```html
<head>
  <link rel="preconnect" href="https://cdn.helmlabs.com" crossorigin>
  <link rel="preload" as="image" href="/hero-800.webp"
        imagesrcset="/hero-400.webp 400w, /hero-800.webp 800w, /hero-1600.webp 1600w"
        imagesizes="(max-width: 600px) 100vw, 800px">
  <style>/* inlined critical CSS */</style>
</head>
<body>
  <img src="/hero-800.webp" srcset="..." fetchpriority="high" width="800" height="450" alt="...">
</body>
```
LCP = 1.3s on the same Moto G4.

## Related entries
- `corpus/evaluation-frameworks/review-sections/07-performance.md` — broader perf review.
- `corpus/ux-principles/audit/06-responsive/responsive-images.md` — image optimization is the biggest LCP lever.
- `corpus/ux-principles/audit/10-performance/cls-target.md` — sibling Core Web Vital.

## Anti-patterns
- Lazy-loading the LCP image with `loading="lazy"` — guarantees a slow LCP.
- Hero animation that delays paint — JS-driven hero entrance kills LCP.
- Optimizing only on fiber — most users aren't on fiber.
