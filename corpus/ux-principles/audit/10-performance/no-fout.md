---
name: No FOUT — Critical Fonts Preloaded
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/10-performance/font-display-swap.md, corpus/ux-principles/audit/10-performance/cls-target.md]
---

# No FOUT (Flash of Unstyled Text)

## What it is
**FOUT (Flash of Unstyled Text)** is the visible jump when a page renders in the fallback font, then swaps to the custom font mid-view — text reflows, character widths change, line breaks shift. Critical fonts must be preloaded *and* fallback metrics matched to the custom font so the swap is invisible.

## Why it matters
FOUT is the cousin of FOIT. FOIT hides text; FOUT shows it ugly. Both are jarring. With proper preloading, the custom font arrives early enough to render without swap. With proper metrics-matching, even when there's a tiny swap delay, the fallback character dimensions are close enough that no visible reflow happens. Together: text is always visible AND it never jumps.

## How to apply
- **Preload the critical fonts** — typically the body weight and the heading weight. Don't preload all 8 weights; preload 2.
  ```html
  <link rel="preload" as="font" type="font/woff2"
        href="/fonts/sohne-regular.woff2" crossorigin>
  <link rel="preload" as="font" type="font/woff2"
        href="/fonts/sohne-bold.woff2" crossorigin>
  ```
- **Metrics-match the fallback** so character widths line up. Modern way: `size-adjust`, `ascent-override`, `descent-override`, `line-gap-override` on the `@font-face` of the fallback (or use a tool like `fontaine` or `next/font` that does it automatically).
  ```css
  @font-face {
    font-family: 'Söhne-fallback';
    src: local('Arial');
    size-adjust: 102%;
    ascent-override: 90%;
    descent-override: 22%;
    line-gap-override: 0%;
  }
  body { font-family: 'Söhne', 'Söhne-fallback', sans-serif; }
  ```
- **Subset fonts** — if you only use Latin glyphs, ship a Latin subset (5–15KB) instead of the full font (50–200KB).
- **Variable fonts** — ship one variable font file with weight 100–900 instead of 8 separate weights. Saves bytes and lets you use any weight CSS-side.
- **Consider `font-display: optional`** for above-the-fold critical fonts in product UI — if the font hasn't loaded in 100ms, stay on the matched fallback. Avoids the swap entirely.
- Test by throttling network to slow 3G in DevTools — FOUT shows up clearly.

## Examples (BAD vs. GOOD pairs)

BAD: site uses Söhne via `@font-face` with `font-display: swap` and no preload, no metrics match. Hero text renders in Arial at 14px wide, then swaps to Söhne at 13.6px wide — every line breaks differently after swap, page jumps.

GOOD:
```html
<head>
  <link rel="preload" as="font" type="font/woff2" href="/fonts/sohne-regular.woff2" crossorigin>
  <link rel="preload" as="font" type="font/woff2" href="/fonts/sohne-bold.woff2" crossorigin>
</head>
```
```css
@font-face { font-family: 'Söhne'; src: url(...) format('woff2'); font-display: swap; }
@font-face {
  font-family: 'Söhne-fallback';
  src: local('Arial');
  size-adjust: 102%;
  ascent-override: 90%;
}
body { font-family: 'Söhne', 'Söhne-fallback', system-ui, sans-serif; }
```
Result: text renders in metrics-matched Arial → swaps to Söhne with zero visible reflow.

## Related entries
- `corpus/ux-principles/audit/10-performance/font-display-swap.md` — companion rule.
- `corpus/ux-principles/audit/10-performance/cls-target.md` — FOUT is a CLS contributor.

## Anti-patterns
- Preloading every font weight you have (10 of them) — defeats the purpose.
- No fallback metrics match — guarantees visible reflow on swap.
- Using `font-display: block` to hide the FOUT — replaces FOUT with FOIT, worse UX.
