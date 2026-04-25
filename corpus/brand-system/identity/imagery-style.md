---
name: Imagery Style
domain: brand-system
source_skill: graphic-design
entry_type: rule
length_target: 300-800
related: [corpus/brand-system/identity/imagery-anti-patterns.md, corpus/brand-system/identity/neural-architect-overview.md, corpus/brand-system/diagrams/five-step-context-flow.md, corpus/brand-system/social/diagrams-over-abstract.md, corpus/brand-system/implementation/svg-for-diagrams.md]
---

# Imagery Style

## What it is
Riché's visual content is architectural, structural, and systems-oriented. The default visual vocabulary is node-and-edge diagrams, layer visualizations, and flow diagrams — clean geometric shapes rendered with consistent stroke widths. Imagery exists to encode an argument, not to decorate a post.

**The on-brand vocabulary:**
- Node-and-edge diagrams (with directional or transformational arrows)
- Layer visualizations (stacked rectangles showing system architecture)
- Flow diagrams (left-to-right or circular, with each stage as a labeled container)
- 2x2 matrices, radar charts, comparison tables
- Code snippets as visual anchors
- Geometric shapes with intentional spacing

## Why it matters
The imagery style is what makes Riché's content recognizable in a feed before the caption is read. It is also what separates a practitioner brand from a "talker about AI" brand. A node-and-edge diagram says "I built this." A glowing brain says "I have opinions about AI." The audience Riché is building toward — operators, builders, technical PMs — reads visual style as a credibility signal long before they read prose.

## How to apply
- **Default to a diagram.** When a post or slide needs visual weight, the first move is "what's the diagram for this argument?" — not "what stock illustration matches this vibe?"
- **Geometric, not organic.** Rectangles, circles, lines. No hand-drawn squiggles, no watercolor textures, no rounded blobs.
- **Consistent stroke widths.** One stroke weight per asset (typically 1.5px or 2px). Mixing stroke widths reads as inconsistent rather than emphatic.
- **Iconography from a single library.** Pick one icon set per project (Lucide, Phosphor, Heroicons) and stay in it. Never mix sets in a single asset.
- **Negative space carries weight.** Leave room around nodes and labels — density makes diagrams feel like systems, but cramped density makes them feel like clutter.

## Examples
1. **Five-stage context flow.** Five labeled rectangles, transformation arrows between them, monospace stage names, accent on the load-bearing stage. No background imagery, no decorative shapes.
2. **Layered architecture diagram on the website.** Three stacked containers labeled "Curation Layer / Synthesis Layer / Storage Layer," each with an icon and a one-line description, all geometric.
3. **Comparison table on LinkedIn.** Two columns ("RAG / Context Layer"), checkmarks and X-marks rendered as monospace glyphs, no decorative shading.

## Related entries
- `corpus/brand-system/identity/imagery-anti-patterns.md` — what's banned from the imagery vocabulary
- `corpus/brand-system/diagrams/five-step-context-flow.md` — concrete example of the on-brand structure
- `corpus/brand-system/social/diagrams-over-abstract.md` — applying the rule to social assets
- `corpus/brand-system/implementation/svg-for-diagrams.md` — how to render this style cleanly

## Anti-patterns
- Reaching for a stock illustration when a diagram would do. If the argument can be drawn as a system, draw it as a system.
- Mixing illustration styles within a single asset (geometric + isometric + hand-drawn). Pick one vocabulary and hold it.
