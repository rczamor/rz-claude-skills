---
name: Context Quality Framework Diagram
domain: brand-system
source_skill: graphic-design
entry_type: template
length_target: 500-700
related: [corpus/brand-system/diagrams/five-step-context-flow.md, corpus/brand-system/diagrams/rag-vs-context-layer-comparison.md, corpus/voice/hook-data-is-not-context.md, corpus/brand-system/identity/imagery-style.md, corpus/evaluation-frameworks/]
---

# Context Quality Framework Diagram

## What it is
The visual that names the four dimensions context must satisfy to be useful for a model:

1. **Freshness** — is it current?
2. **Consistency** — does it align with other context provided?
3. **Completeness** — does it cover the decision space?
4. **Goal-alignment** — is it relevant to the current task?

Unlike the five-step flow (which describes the process) and the RAG comparison (which contrasts approaches), this diagram describes the **output quality** — the dimensions you grade context on. It's the rubric.

## Why it matters
Without quality dimensions, "context" is a vague aspiration. With four named dimensions, it becomes something an audience can evaluate, debug, and improve. This diagram is the framework that shows up when Riché needs to give the audience a tool to take home — at the end of a talk, in a "framework" carousel, on the website's methodology page. The four dimensions also become hashtags for individual posts: a single post can dive deep on Freshness alone and reference the broader framework.

## How to apply
Pick the rendering that fits the use case. All three renderings show the **same four dimensions** — only the visual structure changes.

### Rendering option 1: Radar chart
- Four-axis radar (one axis per dimension).
- Each axis labeled in JetBrains Mono 12pt: `FRESHNESS / CONSISTENCY / COMPLETENESS / GOAL-ALIGNMENT`.
- Plot a current state (filled polygon in muted gray) and a target state (outlined polygon in the project accent).
- Use when comparing two systems, or showing improvement over time.

### Rendering option 2: 2x2 matrix
- Two axes, two dimensions paired: e.g., Freshness × Goal-alignment, with Consistency and Completeness as separate annotations.
- Quadrants labeled with concrete examples ("stale-but-relevant", "fresh-but-off-task", etc.).
- Use when the audience needs to locate specific failure modes in their own systems.

### Rendering option 3: Card-based layout
- Four cards in a 2x2 grid (or four-up row for landscape).
- Each card: dimension name (Inter SemiBold 24pt), one-line definition (Inter 16pt), one diagnostic question (JetBrains Mono 14pt italic).
- Use as a teaching aid — when the audience needs to learn what each dimension means before applying them.

**Common rules across all three renderings:**
- Apply the accent rule. One dimension can be highlighted with the project accent if it's the focus of a specific post; otherwise all four sit in the white/gray base.
- Stage labels in monospace, definitions in sans.
- No decorative shading inside the chart area — the data shape is the visual.

## Examples
1. **Conference talk closing slide.** Card-based 2x2 layout. Four dimensions, each card with the diagnostic question ("Freshness: was this generated more than X minutes ago?"). The audience leaves with the rubric.
2. **LinkedIn post on context drift.** Radar chart rendering, two polygons overlaid: a "before" state with weak Freshness, and an "after" state where Freshness is restored. Single-image visual argument.
3. **richezamor.com methodology page.** Interactive 2x2 matrix where the audience can plot their own system and see which dimensions are weakest.

## Related entries
- `corpus/brand-system/diagrams/five-step-context-flow.md` — the process diagram this rubric grades
- `corpus/brand-system/diagrams/rag-vs-context-layer-comparison.md` — the third visual in the trio
- `corpus/voice/hook-data-is-not-context.md` — the hook this framework operationalizes
- `corpus/brand-system/identity/imagery-style.md` — geometric vocabulary
- `corpus/evaluation-frameworks/` — related evaluation rubrics this framework slots into

## Anti-patterns
- Adding a fifth dimension because "we discovered another one." The four-dimension framework is calibrated to be memorable. If a fifth idea matters, it folds into one of the existing four or becomes a separate framework.
- Rendering the radar chart with all four axes maxed out as the "ideal." That tells the audience the goal is "do everything perfectly" — useless. Show realistic tradeoffs.
