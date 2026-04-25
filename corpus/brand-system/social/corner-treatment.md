---
name: Corner Treatment
domain: brand-system
source_skill: graphic-design
entry_type: rule
length_target: 300-500
related: [corpus/brand-system/identity/imagery-style.md, corpus/brand-system/identity/neural-architect-overview.md, corpus/brand-system/implementation/svg-for-diagrams.md, corpus/brand-system/implementation/css-tailwind-layouts.md]
---

# Corner Treatment

## What it is
Containers, cards, code panels, and any rectangular shape in a Riché visual asset use a slight border radius — between **4px and 8px**. Never fully rounded (pill-shaped). Never sharp (zero radius). The slight radius reads as intentional and matches the IDE-tool aesthetic; full pills read as consumer-app; sharp corners read as utilitarian/wireframe.

**Specific values:**
- **Cards and containers:** 8px
- **Buttons and pills:** 6px
- **Code panels:** 4px (slightly tighter, matches IDE conventions)
- **Hero containers (large):** 8px

## Why it matters
Corner radius is one of the smallest visual choices that compounds across an asset set. Consistent radius = consistent identity. The 4–8px range was chosen because it sits in the same neighborhood as VS Code, Linear, Vercel, and most modern developer tools. Going larger (12px+) drifts toward consumer SaaS. Going to zero drifts toward 90s-era wireframes. The narrow band keeps every asset in the same visual neighborhood.

## How to apply
- **Default cards: 8px.** Use for diagram containers, comparison cards, framework cells.
- **Buttons: 6px.** Slightly tighter than cards so they read as interactive but still in-system.
- **Code panels: 4px.** Tighter still — matches IDE syntax-highlighter conventions.
- **Never fully rounded.** No `border-radius: 50%` on rectangular elements. No pill-shaped buttons. The only fully rounded elements should be circles by intent (e.g., flywheel diagram nodes).
- **Match across components.** All cards in a deck should use the same radius. All code panels should use the same radius. Mixing radii in the same asset reads as inconsistent.

## Examples
1. **Five-Step Context Flow diagram.** Each of the five stage containers uses 8px corner radius. The arrows between them are flat (no radius — they're paths, not shapes).
2. **Code snippet on a slide.** 4px radius on the outer panel. The snippet inside has no corner treatment of its own — it's just text.
3. **LinkedIn carousel cover slide.** Background `#1a1a1a`, no corner radius (full bleed). A small attribution badge in the corner uses 6px.

## Related entries
- `corpus/brand-system/identity/imagery-style.md` — the geometric vocabulary radius is part of
- `corpus/brand-system/identity/neural-architect-overview.md` — why the dev-tool neighborhood matters
- `corpus/brand-system/implementation/svg-for-diagrams.md` — applying radius in SVG output
- `corpus/brand-system/implementation/css-tailwind-layouts.md` — applying radius in Tailwind (`rounded-md` ≈ 6px, `rounded-lg` ≈ 8px)

## Anti-patterns
- Pill buttons (`rounded-full`). Reads as consumer SaaS, breaks the dev-tool neighborhood.
- Sharp zero-radius corners across a whole asset. Reads as wireframe, not finished design.
