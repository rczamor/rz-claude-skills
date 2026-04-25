---
name: SVG for Diagrams
domain: brand-system
source_skill: graphic-design
entry_type: pattern
length_target: 300-500
related: [corpus/brand-system/implementation/css-tailwind-layouts.md, corpus/brand-system/implementation/react-interactive.md, corpus/brand-system/implementation/2x-export-retina.md, corpus/brand-system/identity/imagery-style.md, corpus/brand-system/diagrams/five-step-context-flow.md]
---

# SVG for Diagrams

## What it is
SVG is the default rendering format for all diagrams and icons. Hand-authored or programmatically generated, with clean paths, consistent stroke widths, and the brand palette baked in as variables. SVG scales to any size without quality loss, embeds inline in HTML and Markdown, and exports cleanly to PNG at any resolution.

## Why it matters
A diagram that exists as a flattened PNG can't be edited, can't be re-themed (light mode / dark mode), and can't be made interactive on the website. A diagram that exists as SVG is the source — every other format (slide, social graphic, blog inline) exports from it. One source of truth means one update propagates to every surface where the diagram appears.

## How to apply
- **Author or generate as SVG first.** Even if the final use is a static PNG, build the source as SVG.
- **Consistent stroke width.** Pick one stroke width per diagram (typically `1.5px` or `2px`) and apply it across every path. Mixing strokes reads as inconsistent.
- **Use CSS variables for colors.** Define the palette as CSS custom properties (`--bg-primary: #0a0a0a; --text-primary: #f5f5f5; --accent: #3b82f6;`) and reference them in the SVG fills/strokes. Re-theming becomes a one-variable change.
- **Group with `<g>` and label.** Each logical component (a stage container, an arrow, a label) lives in a named `<g>` group. Easier to edit, easier to animate later if needed.
- **Apply corner radius consistently.** Use `rx="8"` (or 4 for code panels, 6 for buttons) on every rectangle. See `corpus/brand-system/social/corner-treatment.md`.
- **Optimize for size.** Run SVGs through `svgo` before shipping. Removes hidden metadata and shrinks file size.
- **Embed inline for blog posts.** Inline SVG in HTML lets CSS hover states and JavaScript animate the diagram without re-fetching.

## Examples
1. **Five-Step Context Flow as SVG.** Five `<rect>` elements grouped in `<g class="stages">`, transformation `<path>` arrows in `<g class="arrows">`, labels in `<g class="labels">`. Single CSS variable for the accent color. Export size: 1080x1080 PNG for social, inline at any size for the website.
2. **Context Quality Framework radar chart.** SVG with computed polygon coordinates for the four-axis radar. Two polygons (current state, target state) with the accent color on the target.
3. **Geometric monogram favicon.** Single SVG path, exported to PNG at 16x16, 32x32, and 192x192 for the favicon set.

## Related entries
- `corpus/brand-system/implementation/css-tailwind-layouts.md` — sibling pattern for layout-heavy graphics
- `corpus/brand-system/implementation/react-interactive.md` — sibling pattern for the website
- `corpus/brand-system/implementation/2x-export-retina.md` — exporting SVG to PNG correctly
- `corpus/brand-system/identity/imagery-style.md` — the geometric vocabulary
- `corpus/brand-system/diagrams/five-step-context-flow.md` — example of an SVG-authored canonical diagram

## Anti-patterns
- Authoring diagrams in Figma and exporting only as PNG. Loses the editability and the re-theming. Export the SVG too.
- Inconsistent stroke widths across paths in the same diagram (e.g., 1px arrows but 2px containers). Pick one and stick to it.
