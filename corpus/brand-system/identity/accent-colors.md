---
name: Accent Colors
domain: brand-system
source_skill: graphic-design
entry_type: resource
length_target: 300-800
related: [corpus/brand-system/identity/color-palette.md, corpus/brand-system/identity/color-anti-patterns.md, corpus/brand-system/identity/palette.yaml, corpus/brand-system/identity/neural-architect-overview.md]
---

# Accent Colors

## What it is
A single accent color is selected per project from a tight technical palette: electric blue, emerald green, or amber. The accent is reserved for interactive elements, data highlights, and the load-bearing node in a diagram. It is never used for decoration, never used in pairs, and never used as a fill color across multiple elements at the same time.

**The three accents:**
- **Electric blue** — the default "data" accent. Use for technology and AI-architecture content.
- **Emerald green** — the "growth/health" accent. Use for metrics, audience growth, or positive deltas.
- **Amber** — the "warning/attention" accent. Use for risk, gaps, or "the thing most people miss."

## Why it matters
The Neural Architect identity has a narrow base palette (near-black, dark gray, white, muted gray) so a single color choice can carry meaning. When every diagram has one and only one colored element, that color becomes the answer the viewer was looking for. Spread the accent across multiple elements and it becomes decoration — the visual argument collapses.

## How to apply
- **One accent per project.** A talk deck, a blog post, a campaign — pick once and hold it across the whole asset set. Switching mid-deck reads as a Canva mistake.
- **Reserve it for the load-bearing element.** The synthesis node in the five-step flow. The "context layer" side of the RAG-vs-Context-Layer comparison. The single data point that makes the argument.
- **Use sparingly.** A single diagram should have at most one accent-colored element, two if there's an explicit comparison being made (e.g., before/after).
- **Pair with the base palette only.** Never accent-on-accent. Never accent-as-background.

## Examples
1. **Five-step context flow diagram.** Electric blue on the "Synthesis" node only — the other four stages stay in white/gray. Viewer's eye lands on synthesis as the differentiator.
2. **Audience growth flywheel post.** Emerald green on the arrow connecting "shipping evidence" to "audience growth" — the load-bearing causal claim of the visual.
3. **"What most people get wrong about RAG" carousel.** Amber on the gap between RAG and Context Layer — the visual highlights the missing work.

## Related entries
- `corpus/brand-system/identity/color-palette.md` — the base palette this accent sits on top of
- `corpus/brand-system/identity/color-anti-patterns.md` — colors that disqualify themselves as accents
- `corpus/brand-system/identity/palette.yaml` — machine-readable accent definitions
- `corpus/brand-system/diagrams/five-step-context-flow.md` — example of one-accent placement

## Anti-patterns
- Using all three accents in the same asset because "the categories deserve different colors." Categories are encoded by position, label, and shape — color is reserved for emphasis.
- Picking a fourth accent (red, pink, purple) because the project "feels different." If the project doesn't fit blue/green/amber, the message is probably off-brand — not the palette.
