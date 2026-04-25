---
name: Mobile Layout Makes Design Sense
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/principles/mobile-same-rules-higher-stakes.md, corpus/ai-product-ux/, corpus/ux-principles/audit/06-responsive/nav-collapse-pattern.md]
---

# Mobile Layout Makes Design Sense

## What it is
Mobile layout makes *design* sense — not just stacked desktop columns. The mobile view should be authored as a first-class composition: thumb-zone aware, vertical-rhythm sound, with elements re-prioritized for the smaller canvas. A 3-column desktop grid that becomes a 1-column stack with no other change is a port, not a design.

## Why it matters
Mobile is over half of most product traffic. A pure column-stack pushes the most important content below 4–6 screens of scroll, buries primary CTAs under decorative cards, and ignores that thumbs reach the bottom-third of the screen most easily. Layout-as-an-afterthought is the loudest "we didn't design for mobile" signal — users feel it before they can name it.

## How to apply
- Re-author the hierarchy on mobile, don't just collapse columns. The primary CTA should be reachable in one thumb-stretch.
- Above-the-fold on mobile should pass the 3-second test (`audit/01-hierarchy/above-fold-3-second.md`) on a 375px-wide canvas, not just on desktop.
- Convert horizontal feature grids into either compact cards, a horizontal-scroll carousel with a clear hint, or a single-column with tighter spacing — never the same desktop card stretched edge-to-edge.
- Bottom navigation, sticky primary actions, or floating action buttons go where the thumb already is — not at the top of the viewport.
- Test on real device, not browser devtools alone. Things look different at 60Hz scroll on iOS than they do in Chrome's responsive panel.

## Examples (BAD vs. GOOD pairs)

BAD — desktop port:
```css
.feature-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }
@media (max-width: 768px) { .feature-grid { grid-template-columns: 1fr; } } /* 3 huge stacked cards, primary CTA buried */
```

GOOD — re-authored:
```css
.feature-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }
@media (max-width: 768px) {
  .feature-grid { display: flex; overflow-x: auto; scroll-snap-type: x mandatory; gap: 12px; padding-inline: 16px; }
  .feature-grid > * { flex: 0 0 80%; scroll-snap-align: start; }
}
```

## Related entries
- `corpus/ux-principles/principles/mobile-same-rules-higher-stakes.md` — the umbrella principle.
- `corpus/ux-principles/audit/06-responsive/nav-collapse-pattern.md` — picking hamburger vs. bottom nav.
- `corpus/ai-product-ux/` — AI surfaces on mobile have stricter density tolerance.

## Anti-patterns
- "Responsive" = `@media (max-width: 768px) { grid-template-columns: 1fr; }` and nothing else.
- Hiding entire blocks on mobile with `display: none` instead of redesigning them.
- Treating the desktop layout as the canonical truth and mobile as a degraded copy.
