---
name: RAG vs. Context Layer Interfaces
domain: ai-product-ux
source_skill: product-design
entry_type: pattern
length_target: 700
related: [corpus/ai-product-ux/patterns/context-display.md, corpus/voice/hook-data-is-not-context.md, corpus/pm-frameworks/ai-product-pm/five-step-context-generation.md, corpus/brand-system/diagrams/five-step-context-flow.md, corpus/ai-product-ux/context/context-as-product-surface.md]
---

# RAG vs. Context Layer Interfaces

## What it is
This pattern is the visual demonstration of the difference between raw retrieval (RAG: pull chunks, stuff into prompt, hope for the best) and synthesized context (the five-step Context Layer: retrieve, filter, score, align to goal, synthesize). Side-by-side views, before/after comparisons, or progressive enhancement that walks the user through each of the five steps. The interface itself is an argument — the user *sees* why context beats data.

## Why it matters
Riché's thesis — "data is not context" — is abstract until someone shows them. Most AI buyers think they are buying RAG when they are actually buying a chunk-stuffer. The RAG-vs-context interface makes the difference visceral: same query, same source corpus, two outputs. One is generic and shallow; the other is specific and load-bearing. Once a buyer sees the comparison, the question changes from "should we add AI?" to "why isn't our AI doing the second one?" This is the pattern that closes deals for the Context Layer Engine.

## How to apply
1. **Lock the inputs.** Same query, same corpus. Variance must come from the context-generation step, not from prompt engineering on either side.
2. **Show both outputs simultaneously.** Side-by-side. Don't make the user toggle and remember.
3. **Walk the five steps as the user scrolls.** Step 1 (retrieve) is identical in both. Step 2 (filter) starts to diverge. By step 5 (synthesize), the gap is obvious.
4. **End with the corrected output.** The user should leave the comparison with a working artifact, not just a debate.

## Examples
1. **Context Layer Demo's "vs RAG" mode.** Toggle that splits the screen: left pane shows what a stock RAG pipeline would return; right pane shows the five-step synthesis. Same prompt, same docs. The two outputs are visually adjacent so the buyer cannot miss the gap.
2. **Conference talk arc visual.** The five-step context flow diagram (in `corpus/brand-system/diagrams/`) is the printed companion to this interactive pattern — same argument, different medium.
3. **Anthropic's tool-use comparison demos.** The pattern of "here's the model alone, here's the model with tools" is the same shape applied to a different axis.

## Related entries
- `corpus/ai-product-ux/patterns/context-display.md` — the core pattern this builds on
- `corpus/voice/hook-data-is-not-context.md` — the thesis
- `corpus/pm-frameworks/ai-product-pm/five-step-context-generation.md` — the framework being demonstrated
- `corpus/brand-system/diagrams/five-step-context-flow.md` — the static diagram counterpart
- `corpus/ai-product-ux/context/context-as-product-surface.md` — why this is product, not pedagogy

## Anti-patterns
- **Cherry-picked comparisons.** Using a query the RAG side can't handle and the Context Layer side aces. Buyers smell it. Pick a query both sides can attempt and let the quality difference speak.
- **Pedagogy without product.** A "how it works" page that explains the difference but doesn't let the user run their own query through both. The interactive comparison is the persuasion; the explainer alone is forgettable.
