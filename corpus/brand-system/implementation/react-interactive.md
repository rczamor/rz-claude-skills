---
name: React Interactive Visualizations
domain: brand-system
source_skill: graphic-design
entry_type: pattern
length_target: 300-500
related: [corpus/brand-system/implementation/svg-for-diagrams.md, corpus/brand-system/implementation/css-tailwind-layouts.md, corpus/brand-system/implementation/2x-export-retina.md, corpus/brand-system/diagrams/context-quality-framework.md]
---

# React Interactive Visualizations

## What it is
For visualizations on richezamor.com that benefit from interactivity — hover states, plot-your-own-system tools, animated reveals, click-through walkthroughs — use React components. The component renders the visual, owns its state, and exports a static fallback (SVG or PNG) for environments that can't run JavaScript.

## Why it matters
A static diagram is the right tool for a LinkedIn post (no interaction layer exists). On the website, where the audience can engage, an interactive version is a stronger experience: the user can plot their own system on the Context Quality Framework radar, hover the Five-Step Flow to see expanded descriptions, or animate the RAG vs. Context Layer comparison to see the difference build. Interactivity also produces shareable artifacts: a screenshot of "my system on the framework" becomes user-generated content.

## How to apply
- **Build the component once.** Each canonical diagram (Five-Step Flow, Context Quality Framework, Flywheel) is a single React component, parameterized by the data it displays.
- **State for interaction, not for content.** The component's state holds hover/active/animated state. The content (stage names, dimension labels) is passed as props.
- **Animate sparingly.** Animations support the argument (revealing transformation between stages); they don't decorate. No bouncy spring animations, no parallax — those clash with the technical aesthetic.
- **Export a static version.** Every interactive component has a `export-static.tsx` (or equivalent) that renders the same visual without state — used for fallback, OG images, and slides.
- **Use the design tokens.** Palette and type stack live in shared tokens; the component imports them rather than hardcoding.
- **Server-rendered first paint.** Use Next.js / SSR so the static visual renders on initial load; interactivity hydrates progressively.

## Examples
1. **Interactive Context Quality Framework on richezamor.com.** User can drag points on a 4-axis radar to plot their own system. The component computes the polygon and shows which dimensions are weak. Static fallback: a sample plot exported as SVG.
2. **Hover-revealing Five-Step Context Flow.** Each stage container expands to show a longer description on hover. Static fallback: the standard diagram with all labels visible.
3. **Animated RAG vs. Context Layer build.** On scroll-into-view, the comparison animates: RAG side fills first, then Context Layer side, showing each transformation glyph one by one. Static fallback: the final state.

## Related entries
- `corpus/brand-system/implementation/svg-for-diagrams.md` — the SVG layer the React component renders
- `corpus/brand-system/implementation/css-tailwind-layouts.md` — CSS layout sibling
- `corpus/brand-system/implementation/2x-export-retina.md` — exporting React-rendered visuals to static images
- `corpus/brand-system/diagrams/context-quality-framework.md` — the canonical framework that benefits most from interactivity

## Anti-patterns
- Building interactive visuals with no static fallback. Slides, social posts, and email previews all need the static export. If there's no fallback, the component can't ship anywhere except the website.
- Decorative animations that don't reinforce the argument (parallax, sparkle effects). Cut them. The visual is the argument; the animation is the argument unfolding.
