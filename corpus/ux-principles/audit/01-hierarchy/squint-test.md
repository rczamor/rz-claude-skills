---
name: Squint Test — Hierarchy Still Visible When Blurred
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/principles/users-scan-not-read.md, corpus/ux-principles/audit/01-hierarchy/clear-focal-point.md, corpus/ux-principles/audit/01-hierarchy/visual-noise.md]
---

# Squint Test — Hierarchy Still Visible When Blurred

## What it is

The squint test: blur the page (literally squint, or apply a CSS `filter: blur(4px)` in DevTools). Without being able to read any text, can you still identify:

- The primary CTA
- The major sections
- The navigation
- Where to start reading

If yes, the visual hierarchy is doing its job. If everything blurs into uniform mush, the hierarchy depends entirely on text content — and scanning users won't read the text.

## Why it matters

Users scan, not read. The first pass over a page is essentially a blurred view — the eye perceives shapes, colors, and contrast before it parses any words. If the hierarchy disappears under a blur, it disappears under a scan. The squint test is a fast operationalization of "would a scanning user understand this page?"

## How to apply

1. **Apply blur in DevTools** — select the body, set `filter: blur(4px)` in styles, observe what survives.
2. **Or just squint** — defocus your eyes until the text is illegible.
3. **Look for:**
   - The primary CTA: still visible as a high-contrast colored shape?
   - Major sections: still distinguishable as separate blocks?
   - Navigation: still locatable as a horizontal or vertical strip?
4. **If hierarchy disappears,** strengthen contrast: increase size differential, use color/weight, add whitespace separation.

## Examples

- **GOOD:** A pricing page where the "Most popular" tier card still clearly stands out under blur — bigger, bordered, colored. Hierarchy survives.
- **BAD:** Three identical pricing cards with text-only differentiation. Under blur, they're three identical rectangles.
- **GOOD:** Linear's interface under blur — sidebar visible as a darker column, primary content clearly framed, CTA buttons high-contrast.
- **BAD:** A page with everything in `#666` text on `#FFF` background, all same size. Under blur, it's a uniform gray field.

## Related entries

- `corpus/ux-principles/principles/users-scan-not-read.md`
- `corpus/ux-principles/audit/01-hierarchy/clear-focal-point.md`
- `corpus/ux-principles/audit/01-hierarchy/visual-noise.md`

## Anti-patterns

- Building hierarchy purely with font weight. Weight contrast helps but isn't enough — color, size, and whitespace must also distinguish.
- Treating the squint test as optional polish. It's a fast diagnostic; run it on every page.
