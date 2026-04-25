---
name: Design the Failure First
domain: ai-product-ux
source_skill: product-design
entry_type: rule
length_target: 600
related: [corpus/ai-product-ux/patterns/graceful-degradation.md, corpus/ai-product-ux/failure/error-recovery-paths.md, corpus/ai-product-ux/failure/timeout-and-rate-limit-ux.md, corpus/ai-product-ux/failure/hallucination-handoff.md, corpus/pm-frameworks/ai-product-pm/non-determinism.md, corpus/ux-principles/audit/05-interaction]
---

# Design the Failure First

## What it is
A rule. Before designing the success state of any AI product surface, design the failure state. The failure state is the test of the product. An AI product without a designed failure state is an unfinished product — regardless of how polished the happy path looks.

## Why it matters
Models fail. They time out, return empty, hallucinate, hit rate limits, lose context, contradict themselves. The variance is permanent. Teams who design success first and bolt on failure handling later end up with happy-path products that fall apart in production — and enterprise buyers who probe the failure path on day one walk away. Designing failure first inverts the priority and forces a design that can ship.

## How to apply
1. **Storyboard failures before successes.** Sketch what the user sees when (a) the model returns nothing, (b) it returns garbage, (c) it never returns, (d) it returns something plausible but wrong. Four storyboards before any happy-path comp.
2. **Make the failure surface the test for the success surface.** If the failure surface is incoherent, the success surface is fragile. Refactor.
3. **Apply the rule recursively.** Every component that calls a model needs its own failure design. The component-level failure compounds the product-level failure if not handled locally.
4. **Review the failure surface with the same intensity as the success surface.** Most teams design success in 5 days and failure in 5 minutes. Invert that ratio.

## Examples
1. **Context Layer Demo timeout fallback.** Designed before the happy-path synthesis. When synthesis fails, the demo surfaces the raw retrieved sources with a clear handoff: "We couldn't synthesize — here's the underlying context." The success path inherited its structure from the failure path.
2. **Suzy Decision Engine's research-panel handoff.** Built before the automated insight generator. When the automated insight cannot meet the confidence threshold, the user is routed to the underlying panel data — degraded, but still useful. Designing the handoff first made the success path's confidence bar credible.

## Related entries
- `corpus/ai-product-ux/patterns/graceful-degradation.md` — the parent pattern
- `corpus/ai-product-ux/failure/error-recovery-paths.md` — the three-path template
- `corpus/ai-product-ux/failure/timeout-and-rate-limit-ux.md` — model-API-specific failures
- `corpus/ai-product-ux/failure/hallucination-handoff.md` — the detected-error path
- `corpus/pm-frameworks/ai-product-pm/non-determinism.md` — why this rule is load-bearing
- `corpus/ux-principles/audit/05-interaction` — general failure-state UX

## Anti-patterns
- **Happy-path-first design reviews.** The team spends 80% of review time on the success state and rubber-stamps the error state. The error state ships untested and breaks on first contact with production.
- **Generic error toast as the failure state.** "Something went wrong" with a retry button is not a designed failure — it's the absence of one.
