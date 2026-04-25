---
name: Talk Structure Template
domain: brand-system
source_skill: graphic-design
entry_type: template
length_target: 600-800
related: [corpus/content-system/format-talk-abstract.md, corpus/growth/speaking/, corpus/brand-system/presentation/one-idea-per-slide.md, corpus/brand-system/presentation/code-and-architecture-anchors.md, corpus/voice/]
---

# Talk Structure Template

## What it is
A six-step arc for any conference talk, keynote, or pitch presentation Riché delivers. Each step has a specific job and a specific position in the talk. Following the structure produces talks that have a strong opening, a clear thesis, credible evidence, and a takeaway the audience can use the next day.

**The six steps:**

1. **Opening — a specific moment or failure.** Not "today I'll talk about..." Open with a concrete moment: a deploy that went wrong, a meeting where the question revealed the gap, a bug that surfaced the architectural mistake. The opening is a story beat, not an agenda slide.

2. **The problem — what most people get wrong.** Name the misconception. The audience has a mental model; the talk's job is to show why that model breaks. This is the "you think it's X, but actually..." moment.

3. **The thesis — Riché's alternative framing.** State the new model in one sentence. This is the headline of the talk — the line that should land on a slide alone, in Inter Bold 64pt, with nothing else.

4. **The evidence — proof points, architecture, demos.** Show the work. Architecture diagrams, code snippets, real metrics, demos. This is the longest section and the most slides — 60% of the deck.

5. **The framework — what the audience can take home.** Distill the thesis into a tool the audience can use Monday morning. The Context Quality Framework, the Five-Step Flow, a checklist, a decision tree. The framework is the giveaway.

6. **The close — one clear takeaway, stated directly.** Not "thank you" and not "questions?" Close with a single sentence the audience leaves with. Stated as an imperative or a clear claim, not a question.

## Why it matters
This structure compresses to a 5-minute lightning talk and expands to a 45-minute keynote. It maps to Riché's content system (hook → tension → evidence → framework → CTA), so a talk and a long-form post share the same skeleton. It also produces talks that record well — each section is self-contained, which means the talk can be excerpted into clips, shorts, and post drafts without re-engineering. The structure is also what conference programmers expect from a strong abstract: when the abstract reflects this arc, acceptance rates rise.

## How to apply
- **Time allocation for a 20-minute talk.** Opening: 1 min. Problem: 2 min. Thesis: 1 min. Evidence: 11 min. Framework: 3 min. Close: 1 min. Buffer: 1 min.
- **Slide allocation for a 20-minute talk (25–35 slides total).** Opening: 1–2 slides. Problem: 2–3 slides. Thesis: 1 slide (the hero). Evidence: 18–22 slides. Framework: 3–5 slides. Close: 1 slide.
- **Write the close first.** The takeaway you want the audience to leave with should drive every choice upstream. Decide the close, then build the framework that produces it, then the evidence that supports the framework, then the thesis, then the problem, then the opening.
- **The opening should reference the close.** A talk that opens with "I deployed broken context to production" and closes with "ship the rubric before you ship the model" is a complete arc. The bookends connect.
- **Cross-reference content.** The talk's framework slide is the same diagram that goes in the LinkedIn post and on the website methodology page. Don't redesign per medium; reuse and stay coherent.

## Examples
1. **"Beyond RAG" 20-minute talk.** Opening: a story about a context-drift incident in production. Problem: "Most teams treat RAG as the finish line." Thesis: "Retrieval is the first step, not the last." Evidence: architecture walkthrough of the five-step flow with code snippets. Framework: Context Quality Framework with the four dimensions. Close: "Grade your context before you grade your model."
2. **"Context Is a Product Surface" 10-minute lightning.** Same arc, compressed. Opening: 30 seconds. Problem: 1 minute. Thesis: 30 seconds. Evidence: 6 minutes (cut to two strong proof points). Framework: 1 minute. Close: 30 seconds.
3. **45-minute keynote.** Same arc, expanded. Evidence section becomes a deeper architecture tour with a live demo; framework gets a 5-minute walkthrough; close takes 2 minutes to land the imperative.

## Related entries
- `corpus/content-system/format-talk-abstract.md` — the abstract format that maps to this arc
- `corpus/growth/speaking/` — the speaking strategy this template feeds
- `corpus/brand-system/presentation/one-idea-per-slide.md` — slide-level rule that holds this structure together
- `corpus/brand-system/presentation/code-and-architecture-anchors.md` — what fills the evidence section
- `corpus/voice/` — the verbal style across all six sections

## Anti-patterns
- Opening with the agenda slide. The audience knows you're giving a talk. Open with the moment.
- Skipping the framework section because "the evidence speaks for itself." Evidence without a framework is a war story. The framework is what makes the audience feel they got something to take home.
- Closing with "any questions?" Close with the takeaway. Then take questions.
