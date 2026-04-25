---
name: Hallucination Handoff
domain: ai-product-ux
source_skill: research
entry_type: pattern
length_target: 600
related: [corpus/ai-product-ux/patterns/graceful-degradation.md, corpus/ai-product-ux/failure/design-the-failure-first.md, corpus/ai-product-ux/failure/error-recovery-paths.md, corpus/ai-product-ux/confidence/expressing-uncertainty.md, corpus/ai-product-ux/context/sources-panel.md]
---

# Hallucination Handoff

## What it is
A pattern for the moment a hallucination is detected — by groundedness check, citation mismatch, contradiction with retrieved sources, or user flag. Instead of failing or retrying, the product hands off gracefully: "Let me hand this back to the source data." The user is given the underlying retrieved context directly and invited to read it themselves. The pattern adapts public AI UX canon — Anthropic's Constitutional AI emphasis on refusing rather than fabricating, Google PAIR's "show retrieval" guidance, OpenAI's grounded-generation patterns — into a product affordance.

## Why it matters
Hallucinations are the single largest trust killer in AI products. A user who catches one confident hallucination remembers it longer than ten correct outputs. The cost is asymmetric. The handoff pattern converts the hallucination from a credibility loss into a procedural step: the AI noticed it couldn't ground the answer and routed the user to the data that *can* ground it. The product looks more honest after a handoff than after a fluent-but-wrong synthesis.

## How to apply
1. **Detect groundedness before display.** Check that the synthesis matches the retrieved sources (citation overlap, entity match, contradiction scan). If groundedness fails, do not display the synthesis.
2. **Surface the sources, not an apology.** "We couldn't ground a confident synthesis on this — here are the sources we pulled. Review directly." The handoff is the answer.
3. **Make the handoff feel intentional, not catastrophic.** This is not an error. It's a routing decision. Visual treatment should match the rest of the product.
4. **Log the handoff for eval.** Every handoff is a calibration signal. Track which prompts trigger handoffs and use them to improve grounding.

## Examples
1. **Context Layer Demo's "review the sources directly" mode.** When the five-step quality check fails groundedness, the demo skips the synthesis card entirely and surfaces the retrieved sources with the prompt: "We couldn't ground a confident synthesis. Here's what we found." Users routinely report this as a feature, not a failure.
2. **Suzy Decision Engine's panel-data fallback.** When the automated insight cannot be grounded in the underlying research-panel responses with sufficient consistency, the system routes the user to the raw panel data with a clear "review directly" framing. Buyers see this as evidence of integrity.
3. **Perplexity's "I don't know" path.** When the model can't ground an answer, the product surfaces search results directly. A public reference implementation.

## Related entries
- `corpus/ai-product-ux/patterns/graceful-degradation.md` — parent pattern
- `corpus/ai-product-ux/failure/design-the-failure-first.md` — the operating rule
- `corpus/ai-product-ux/failure/error-recovery-paths.md` — handoff is the "fall back to human/data" path
- `corpus/ai-product-ux/confidence/expressing-uncertainty.md` — the uncertain-band's UI affordance
- `corpus/ai-product-ux/context/sources-panel.md` — the surface the handoff routes to

## Anti-patterns
- **Apologetic handoff.** "Sorry, AI couldn't answer — here's some stuff." The framing turns a useful routing into a confession of failure.
- **No detection layer.** Surfacing every synthesis without a groundedness check, then asking users to flag hallucinations after the fact. By the time they flag, trust is already gone.
