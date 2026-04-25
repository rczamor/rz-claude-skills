---
name: `system-ui` as PRIMARY Display Font (AI Slop)
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/02-typography/blacklisted-fonts.md, corpus/ux-principles/audit/02-typography/generic-font-flag.md, corpus/brand-system/identity/imagery-anti-patterns.md]
---

# `system-ui` / `-apple-system` as Primary Display Font

## What it is
Using `font-family: system-ui, -apple-system, sans-serif` as the **PRIMARY display or body font** of a marketing or product page. This is the "I gave up on typography" signal — the developer-default font stack adopted because no real type decision was made. Fine for code blocks and admin tools; fatal for any page that aspires to brand identity. **Pick a real typeface.**

## Why it matters
`system-ui` isn't a typeface — it's a fallback chain that resolves to whatever the OS happens to ship that year (San Francisco on Mac, Segoe UI on Windows, Roboto on Android). Your brand looks different on every device, your hierarchy doesn't translate, and most importantly, you're saying *"we didn't pick a font."* Real brands pick a typeface — Inter, Söhne, Aeonik, Suisse Int'l, Mona Sans, an editorial serif, anything intentional. The choice carries personality. `system-ui` carries none.

## How to apply
- Audit `font-family` declarations. If the primary heading or body family is `system-ui`, `-apple-system`, `BlinkMacSystemFont`, or `sans-serif`, that's the slop.
- Acceptable uses of system stack:
  - Code blocks (use `ui-monospace` or `Menlo, Consolas`).
  - Admin / internal tools where brand isn't a goal.
  - As the *fallback* in a font stack: `font-family: 'Aeonik', system-ui, sans-serif`.
- Replace with a real chosen typeface:
  - Free / open-source — Inter, Geist, Manrope (cautiously — see generic-font-flag), Public Sans, IBM Plex.
  - Paid — Söhne, Aeonik, Suisse Int'l, ABC Diatype, Söhne Mono, Tiempos.
  - Variable — modern variable fonts give you weight + width + optical-size from one file.
- Pair display + text: a distinctive display face for headings, a clean text face for body (1.5x line-height, 16px+).

## Examples (BAD vs. GOOD pairs)

BAD:
```css
body, h1, h2, h3 {
  font-family: system-ui, -apple-system, sans-serif;
}
```

GOOD:
```css
:root {
  --font-display: 'Söhne', 'Inter', system-ui, sans-serif;
  --font-text: 'Söhne', 'Inter', system-ui, sans-serif;
  --font-mono: 'Söhne Mono', ui-monospace, monospace;
}
h1, h2, h3 { font-family: var(--font-display); font-feature-settings: 'ss01'; }
body { font-family: var(--font-text); }
```

## Related entries
- `corpus/ux-principles/audit/02-typography/blacklisted-fonts.md` — what *not* to pick.
- `corpus/ux-principles/audit/02-typography/generic-font-flag.md` — even named fonts can be generic.
- `corpus/brand-system/identity/imagery-anti-patterns.md` — broader anti-pattern catalog.

## Anti-patterns
- Believing system-ui is "performant by default" — modern font-loading with `font-display: swap` and preload is a near-zero cost.
- Using system-ui "to match the OS aesthetic" — only Apple gets to do that, and only in their products.
- Picking system-ui because "the design isn't ready yet" — the design will never be ready. Ship a real font.
