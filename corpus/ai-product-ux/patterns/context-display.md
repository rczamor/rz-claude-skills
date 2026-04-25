---
name: Context Display
domain: ai-product-ux
source_skill: product-design
entry_type: pattern
length_target: 700
related: [corpus/ai-product-ux/context/sources-panel.md, corpus/ai-product-ux/context/correction-interface.md, corpus/ai-product-ux/context/context-quality-display.md, corpus/ai-product-ux/context/audit-log.md, corpus/ai-product-ux/context/context-as-product-surface.md, corpus/voice/hook-data-is-not-context.md, corpus/pm-frameworks/ai-product-pm/five-step-context-generation.md, corpus/brand-system/diagrams/five-step-context-flow.md]
---

# Context Display

## What it is
Context display is the AI UX pattern of showing users what context the AI is using to make decisions — the sources retrieved, the data considered, the quality scores, the goal alignment. Users should be able to see, audit, and correct the context that informs AI decisions, not just the outputs. This pattern is the load-bearing UX expression of Riché's thesis: data is not context, and context is what makes AI useful.

## Why it matters
Most AI products display only the output. The context that produced the output is invisible — buried in retrieval logs and prompt scaffolding. When the output is wrong, the user has no surface to diagnose or correct. They can only retry with a different prompt and hope. Context display turns the invisible into the actionable. When users can see the context, they can fix it; when they can fix it, the AI improves with use; when the AI improves with use, the product compounds. This is what separates a wrapper from a system.

## How to apply
1. **Show the sources.** A panel of clickable, inspectable sources informing the answer is the minimum bar. (See `sources-panel.md`.)
2. **Surface quality scores.** Freshness, consistency, completeness, goal-alignment — the four dimensions of context quality from the five-step framework.
3. **Allow correction.** Users edit, remove, or re-rank context. The corrections feed back into future generations.
4. **Maintain an audit log.** What context was used at each decision point — recoverable and attestable. Enterprise buyers require this.

## Examples
1. **Context Layer Demo's center stage.** The demo's primary surface is not the AI output — it is the context. Sources, quality scores, the five-step flow, and the synthesis sit side by side. The output is a consequence of the context, and the user can intervene at any step.
2. **Suzy Decision Engine's research panel transparency.** Every insight surfaces the underlying research-panel respondents, their consistency, and the goal alignment to the buyer's brief. Enterprise customers can audit any insight back to its data.
3. **Perplexity's source citations.** A baseline implementation — every answer carries inline citations the user can click through. Minimal context display, but it works.

## Related entries
- `corpus/ai-product-ux/context/sources-panel.md` — the canonical UI
- `corpus/ai-product-ux/context/correction-interface.md` — letting users intervene
- `corpus/ai-product-ux/context/context-quality-display.md` — the four-dimension score
- `corpus/ai-product-ux/context/audit-log.md` — the enterprise requirement
- `corpus/ai-product-ux/context/context-as-product-surface.md` — context is the product, not a debug panel
- `corpus/voice/hook-data-is-not-context.md` — the thesis
- `corpus/pm-frameworks/ai-product-pm/five-step-context-generation.md` — the framework being displayed
- `corpus/brand-system/diagrams/five-step-context-flow.md` — the visual companion

## Anti-patterns
- **Context behind a "debug" toggle.** Treating context as developer-only metadata. The user is the one who knows what context is missing — surface it for them.
- **Read-only context.** Showing the context but not letting the user correct it. Half the value is the feedback loop.
