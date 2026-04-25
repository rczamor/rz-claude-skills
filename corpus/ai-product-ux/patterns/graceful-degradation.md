---
name: Graceful Degradation
domain: ai-product-ux
source_skill: product-design
entry_type: pattern
length_target: 700
related: [corpus/ai-product-ux/failure/design-the-failure-first.md, corpus/ai-product-ux/failure/error-recovery-paths.md, corpus/ai-product-ux/failure/timeout-and-rate-limit-ux.md, corpus/ai-product-ux/failure/hallucination-handoff.md, corpus/ux-principles/audit/05-interaction]
---

# Graceful Degradation

## What it is
Graceful degradation is the pattern of designing the failure state of an AI product before designing the success state. When the model times out, hallucinates, hits a rate limit, or returns nothing useful, the user experience must remain coherent. The product still works — it just works in a reduced mode that is honest about its limits. An AI product without a designed failure state is an unfinished product.

## Why it matters
Models fail. They time out under load, return empty for edge-case prompts, hallucinate on adversarial input, and rate-limit at peak demand. The variance is not a bug to be eliminated — it is the operating environment. Teams that ship the happy path and bolt on error states later end up with an AI product that feels great on the demo and brittle in production. Buyers (especially enterprise) test the failure path on day one. If it's incoherent, the deal stalls regardless of how good the success path looks.

## How to apply
1. **Storyboard the failure first.** Before you build the success UI, sketch what happens when the model returns nothing, returns garbage, or never returns. The success UI is easy. The failure UI is the work.
2. **Three recovery paths: retry, refine, fall back to human.** Always offer at least one. Often offer all three.
3. **Degrade to a usable surface, not a dead end.** "Sorry, something went wrong" is not graceful. "Here's the source data we pulled — you can review it directly" is graceful.
4. **Time-box every model call.** A spinner that runs forever is a worse failure than a fast no.

## Examples
1. **Context Layer Demo timeout fallback.** When synthesis fails, the demo shows the raw retrieved sources directly with a note: "We couldn't synthesize a recommendation — here's the underlying context. You can review and decide." The user never hits a dead end.
2. **Suzy Decision Engine's research panel handoff.** When an automated insight cannot be generated with sufficient confidence, the system routes the user back to the underlying research panel data — degraded, but still useful. The product never lies about not having an answer.
3. **GitHub Copilot's "no suggestion."** When Copilot has nothing useful, it shows nothing. The IDE keeps working. The failure mode is silence, not a broken UI.

## Related entries
- `corpus/ai-product-ux/failure/design-the-failure-first.md` — the operating rule
- `corpus/ai-product-ux/failure/error-recovery-paths.md` — the three-path template
- `corpus/ai-product-ux/failure/timeout-and-rate-limit-ux.md` — failure modes specific to model APIs
- `corpus/ai-product-ux/failure/hallucination-handoff.md` — the recovery path for detected hallucinations
- `corpus/ux-principles/audit/05-interaction/` — general failure / loading / error UX

## Anti-patterns
- **The eternal spinner.** A loading state with no time-out and no fallback. The user assumes the product is broken.
- **Generic error toast.** "Something went wrong" with a retry button is not graceful — it provides no context, no agency, and no path forward.
