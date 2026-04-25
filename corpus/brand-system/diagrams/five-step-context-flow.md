---
name: Five-Step Context Flow Diagram
domain: brand-system
source_skill: graphic-design
entry_type: template
length_target: 600-800
related: [corpus/brand-system/diagrams/rag-vs-context-layer-comparison.md, corpus/brand-system/diagrams/context-quality-framework.md, corpus/voice/hook-data-is-not-context.md, corpus/brand-system/identity/imagery-style.md, corpus/brand-system/identity/accent-colors.md]
---

# Five-Step Context Flow Diagram

## What it is
The canonical visual for Riché's central thesis: context generation is not a pipeline, it's an active process. Five distinct stages — **Curation, Synthesis, Consolidation, Prioritization, Intelligent Storage** — each rendered as a labeled container with visible transformation between input and output. The arrows between stages suggest transformation, not passive flow.

This is **not** a left-to-right pipeline of equal-weight boxes. The visual structure is the argument: each stage is doing different work, and the diagram shows that work happening.

## Why it matters
The five-step flow is the visual that makes the verbal hook ("Data is not context") legible. When someone reads the post, the diagram is the proof. When someone sees the diagram in a feed without context, the structure alone communicates that something more sophisticated than RAG is being described. This diagram shows up in conference talks, LinkedIn posts, the website, slide decks, and recruiter pitch materials — it's the most-reused visual in the brand. Getting the structure right once means every reuse compounds the recognition.

## How to apply
Build the diagram in this exact structure:

1. **Five distinct stages, each in its own visual container.** Containers are rectangles (rounded corners, 4–8px radius — see `corpus/brand-system/social/corner-treatment.md`). Equal width, equal height, equal spacing.
2. **Show transformation at each stage.** The input glyph entering a stage looks different from the output glyph leaving it. A simple way to encode this: a small icon inside each container showing what the stage does (a filter for Curation, a merge for Synthesis, a dedup for Consolidation, a ranking for Prioritization, a database/vector for Storage).
3. **Iconography or visual metaphors that distinguish active processing from data movement.** A stage is doing work — show the work as a glyph, not as a name plate.
4. **Arrows that suggest transformation.** Use arrows with a slight thickness change (input thinner, output thicker) or with a small inline transformation icon. A flat unidirectional arrow looks like passive flow; a transformational arrow says "the data was changed."
5. **Label each stage with a one-line description.** Stage name in Inter Medium 16pt; one-line "what happens here" in JetBrains Mono 12pt below it. Example: "CURATION / select sources by relevance + freshness."
6. **Apply the accent rule.** One accent color (typically electric blue) on the load-bearing stage — usually Synthesis, since it's the differentiator from RAG. Other four stages stay in white/gray.

**Layout options:**
- **Horizontal row** — five stages left-to-right. Default for slides (16:9).
- **Three-up grid with two-up below** — for portrait social formats (1080x1080).
- **Vertical stack** — for mobile-first reading and long blog headers.

## Examples
1. **LinkedIn carousel slide 3 of 7.** Five rectangles in a horizontal row on `#0a0a0a` background. Each rectangle has a 2px white stroke, a small icon centered, the stage name in Inter Medium 16pt below the icon, and a one-line mono caption beneath. Synthesis stage has electric-blue stroke and electric-blue icon. "richezamor" attribution lower-right at 60% opacity.
2. **Conference talk slide.** Same five stages but enlarged for projection — containers 2x larger, 48pt stage names, a 1-second build animation per stage so the speaker can talk through each one.
3. **richezamor.com hero diagram.** React component rendering the five stages with subtle hover state on each — hovering reveals an expanded description. Static export at 2x retina for fallback.

## Related entries
- `corpus/brand-system/diagrams/rag-vs-context-layer-comparison.md` — uses this five-step structure on the right side
- `corpus/brand-system/diagrams/context-quality-framework.md` — the complementary "quality dimensions" visual
- `corpus/voice/hook-data-is-not-context.md` — the verbal claim the diagram proves
- `corpus/brand-system/identity/imagery-style.md` — the geometric vocabulary this diagram uses
- `corpus/brand-system/identity/accent-colors.md` — why one stage gets the accent

## Anti-patterns
- Rendering the five stages as identical boxes connected by identical arrows. That collapses to a generic pipeline diagram and loses the "active process" argument.
- Adding decorative icons that don't encode the work happening at each stage. If the icon is just "a sparkle" or "a circle," cut it.
- Coloring all five stages with five different accents. The accent goes on one stage only — the differentiator.
