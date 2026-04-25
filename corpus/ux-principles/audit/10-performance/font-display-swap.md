---
name: `font-display: swap` + Preconnect to CDN
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/10-performance/no-fout.md, corpus/ux-principles/audit/10-performance/lcp-target.md]
---

# `font-display: swap` and Preconnect

## What it is
Custom web fonts must use `font-display: swap` (or `optional`) so text renders immediately in a fallback font and swaps to the custom font when ready — never blocked while waiting. Pair with `<link rel="preconnect">` to the font CDN so the TLS handshake completes early.

## Why it matters
The default `font-display: auto` produces FOIT (Flash of Invisible Text): text is hidden until the font loads, sometimes 1–3 seconds. Users see a blank page, can't read content, and bounce. `swap` shows fallback text immediately, then swaps when the custom font arrives — text is always visible. Preconnect saves ~100–300ms by warming up the connection to the font CDN before the font request fires.

## How to apply
- Every `@font-face` rule must declare `font-display`:
  ```css
  @font-face {
    font-family: 'Söhne';
    src: url('/fonts/sohne.woff2') format('woff2');
    font-display: swap;          /* shows fallback, swaps when ready */
    font-weight: 100 900;        /* variable font range */
  }
  ```
- Choose between:
  - `swap` — always swap, even late. Best UX for marketing copy.
  - `optional` — swap only if font loads in <100ms; otherwise stays on fallback. Best for product UI where the swap itself is jarring.
  - `block` (≈3s invisible) — never use this.
- Preconnect to font CDN in `<head>`:
  ```html
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  ```
  (`crossorigin` matters for fonts.)
- For self-hosted fonts on the same origin: `<link rel="preload" as="font" type="font/woff2" href="/fonts/sohne.woff2" crossorigin>`.
- Pair with metrics-matched fallback (size-adjust / ascent-override) to prevent CLS on swap (`audit/10-performance/cls-target.md`).

## Examples (BAD vs. GOOD pairs)

BAD:
```css
@font-face { font-family: 'Söhne'; src: url(...) format('woff2'); }
/* defaults to font-display: auto → FOIT for 1–3s */
```

GOOD:
```html
<head>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="font" type="font/woff2" href="/fonts/sohne.woff2" crossorigin>
</head>
```
```css
@font-face {
  font-family: 'Söhne';
  src: url('/fonts/sohne.woff2') format('woff2');
  font-display: swap;
  size-adjust: 102%;
}
```

## Related entries
- `corpus/ux-principles/audit/10-performance/no-fout.md` — preventing visible flash.
- `corpus/ux-principles/audit/10-performance/lcp-target.md` — fonts are part of the LCP critical path.

## Anti-patterns
- `font-display: block` — same as default; produces FOIT.
- Forgetting `crossorigin` on preconnect / preload for fonts — silently fails.
- Loading 8 font weights when you use 2 — bytes on the critical path.
