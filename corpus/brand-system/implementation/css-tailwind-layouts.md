---
name: CSS / Tailwind Layouts
domain: brand-system
source_skill: graphic-design
entry_type: pattern
length_target: 300-500
related: [corpus/brand-system/implementation/svg-for-diagrams.md, corpus/brand-system/implementation/react-interactive.md, corpus/brand-system/identity/palette.yaml, corpus/brand-system/social/corner-treatment.md]
---

# CSS / Tailwind Layouts

## What it is
For layout-based visuals — comparison tables, card grids, framework displays — use CSS / Tailwind rather than authoring as a single SVG. CSS layouts are easier to make responsive, easier to update content in, and integrate naturally with the rest of richezamor.com. Use this pattern when the visual is mostly typography and rectangles arranged in a grid.

## Why it matters
SVG is the right tool for diagrams (curves, transformations, custom shapes). CSS is the right tool for grids (cards arranged in rows, comparison tables, framework matrices). Trying to render a 4-card framework grid as a single SVG produces a brittle artifact that's hard to update; rendering it with CSS Grid + Tailwind classes produces a component that scales, re-themes, and accepts content changes without touching path data.

## How to apply
- **Use Tailwind utility classes** for spacing, typography, and color. The brand palette lives in `tailwind.config.js` as semantic tokens (`bg-primary`, `text-primary`, `accent-blue`).
- **CSS Grid for card layouts.** A 2x2 framework grid: `grid grid-cols-2 gap-6`. A 4-up row: `grid grid-cols-4 gap-4`.
- **Flexbox for in-card composition.** Inside each card, use `flex flex-col gap-3` to stack the icon, label, and definition.
- **Apply corner radius via Tailwind.** `rounded-md` (6px) for buttons, `rounded-lg` (8px) for cards, `rounded` (4px) for code panels.
- **Type stack via Tailwind.** `font-sans` (Inter), `font-mono` (JetBrains Mono). Configure both in `tailwind.config.js` so they apply everywhere consistently.
- **Reuse component classes.** Build a small set of reusable component classes (`card`, `code-panel`, `stage-container`) so the same visual treatment applies across every page.

## Examples
1. **Context Quality Framework as a CSS grid.** Four cards in a 2x2 grid, each card with a Tailwind class set: `bg-secondary rounded-lg p-6 flex flex-col gap-3`. Inside: an SVG icon, the dimension name in `font-sans font-semibold text-2xl`, the diagnostic question in `font-mono text-sm text-muted`.
2. **RAG vs. Context Layer comparison table.** CSS Grid with two columns; each row is a flex container with the comparison cells. Checkmarks rendered as monospace glyphs in JetBrains Mono.
3. **Speaker one-sheet on richezamor.com.** Tailwind layout with hero section, talk listings (cards in a grid), social proof (logos in a row). Each section uses the consistent palette and type stack.

## Related entries
- `corpus/brand-system/implementation/svg-for-diagrams.md` — sibling pattern for true diagrams
- `corpus/brand-system/implementation/react-interactive.md` — when interactivity is needed on top of CSS layout
- `corpus/brand-system/identity/palette.yaml` — the values that map to Tailwind tokens
- `corpus/brand-system/social/corner-treatment.md` — Tailwind radius utilities

## Anti-patterns
- Inline styles for one-off colors. Always reference the palette tokens — otherwise re-theming is an engineering project.
- Mixing utility classes and custom CSS for the same component. Pick one approach per component and stay consistent.
