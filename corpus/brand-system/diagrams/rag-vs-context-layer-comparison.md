---
name: RAG vs. Context Layer Comparison Diagram
domain: brand-system
source_skill: graphic-design
entry_type: template
length_target: 600-800
related: [corpus/brand-system/diagrams/five-step-context-flow.md, corpus/brand-system/diagrams/context-quality-framework.md, corpus/voice/hook-data-is-not-context.md, corpus/brand-system/identity/imagery-style.md]
---

# RAG vs. Context Layer Comparison Diagram

## What it is
A side-by-side visual that makes the Context Layer argument by contrast. **Left side: typical RAG** — Chunk → Embed → Store → Retrieve, rendered as a simple four-step pipeline with minimal transformation between steps. **Right side: Context Layer** — the full five-step flow (Curation, Synthesis, Consolidation, Prioritization, Intelligent Storage), rendered with visible transformation at each stage.

The visual gap between the two sides is the argument. The right side should look richer, more sophisticated, more intentional. The viewer should see the difference before reading any label.

## Why it matters
Most of the audience already has a mental model of RAG. The Context Layer is the thing they don't have a model for yet. Trying to define the Context Layer from scratch requires too much prose. Putting RAG and Context Layer side by side lets the audience use what they already know as the anchor — and the visual asymmetry does the explaining. This is the comparison diagram that shows up in talk decks when Riché needs to land the differentiation in 30 seconds.

## How to apply
Build the side-by-side in this structure:

1. **Two columns, equal width.** Header on each side: "TYPICAL RAG" (left) and "CONTEXT LAYER" (right) in JetBrains Mono 14pt, all caps, `#a0a0a0`.
2. **Left column — RAG pipeline.** Four containers stacked vertically: Chunk → Embed → Store → Retrieve. Containers are equal-sized, simple rectangles, white stroke. Arrows between them are flat unidirectional (pipeline-feel). No transformation glyphs inside. The whole left side reads as flat and mechanical.
3. **Right column — Context Layer.** Five containers stacked vertically: Curation → Synthesis → Consolidation → Prioritization → Intelligent Storage. Each container has a transformation glyph inside (the same iconography from the five-step flow diagram). Arrows between stages show transformation (thicker after each stage, or inline transformation icons). The Synthesis stage carries the project's accent color.
4. **The visual gap is the argument.** Don't add a divider line between the columns. Don't add labels saying "more sophisticated." Let the structural difference do the work.
5. **One-line caption at the bottom.** A single line in Inter Medium 14pt: "Both retrieve. Only one curates, synthesizes, consolidates, prioritizes." (Or a similar one-liner from Riché's voice.)

**Format variants:**
- **Slide format (16:9)**: Two columns side-by-side, headers at top, caption at bottom.
- **Social square (1080x1080)**: Same structure, slightly compressed vertically.
- **LinkedIn landscape (1200x627)**: Compress to two compact columns with shorter labels.

## Examples
1. **Conference talk "Beyond RAG" slide.** Full 16:9 dark slide. Left column: 4-stage RAG pipeline in flat white. Right column: 5-stage Context Layer with electric-blue Synthesis node and transformation glyphs throughout. Caption: "Retrieval is not enough."
2. **LinkedIn post hero image (1200x627).** Compact two-column format. RAG side fits on left third, Context Layer fits on middle third, right third is the caption + "richezamor" attribution.
3. **Blog post inline diagram.** SVG embedded mid-post. Same structure but rendered in the surrounding article's text scale so it reads as an integrated diagram, not a pasted graphic.

## Related entries
- `corpus/brand-system/diagrams/five-step-context-flow.md` — the right-side structure in detail
- `corpus/brand-system/diagrams/context-quality-framework.md` — the third diagram in the trio
- `corpus/voice/hook-data-is-not-context.md` — the verbal hook this diagram supports
- `corpus/brand-system/identity/imagery-style.md` — the geometric vocabulary

## Anti-patterns
- Making the RAG side look "bad" through visual treatment (red strikethrough, sad faces, broken arrows). The argument is structural — RAG works, it's just incomplete. Don't strawman it visually.
- Adding a "winner" label or a checkmark on the Context Layer side. The audience reads condescension. The structural difference is the argument.
- Rendering both sides with identical step counts to "make them look balanced." The unequal step count is the point.
