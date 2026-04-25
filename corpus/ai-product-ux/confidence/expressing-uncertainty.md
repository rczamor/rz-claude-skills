---
name: Expressing Uncertainty
domain: ai-product-ux
source_skill: research
entry_type: pattern
length_target: 600
related: [corpus/ai-product-ux/patterns/confidence-indicators.md, corpus/ai-product-ux/confidence/visual-encoding.md, corpus/ai-product-ux/confidence/textual-encoding.md, corpus/ai-product-ux/confidence/calibration-anti-patterns.md, corpus/ai-product-ux/failure/hallucination-handoff.md]
---

# Expressing Uncertainty

## What it is
A three-level taxonomy for AI uncertainty, each with a distinct UI affordance: **known good** (assertive output, full UI weight), **hedged** (qualified output, lighter visual weight, user prompted to verify), **uncertain** (explicit "I don't know" with handoff to source data or human). The taxonomy adapts public AI UX canon — Anthropic's Constitutional AI emphasis on honest uncertainty, Google PAIR's "calibrate trust" guideline, OpenAI's "show your work" pattern — into a product-shippable shape.

## Why it matters
The source skill describes a binary: "high confidence vs. uncertain." Real models produce a gradient, and the middle band — hedged — is where most outputs live and where the most damage gets done. A hedged output displayed as known-good is a confident hallucination; a hedged output displayed as uncertain is a useful answer thrown away. Distinct UI affordances for each band let the product preserve the value of hedged outputs without inflating their authority.

## How to apply
1. **Known good** — full visual weight, assertive language, no caveat. Display only when eval-measured precision exceeds the agreed threshold.
2. **Hedged** — same content, lighter visual treatment (~70% opacity, soft border), qualifying language ("This is likely..."), and a one-click "verify" affordance that surfaces the underlying sources.
3. **Uncertain** — minimal output, explicit "I don't have enough to answer this," with a handoff path: "Here's the source data we pulled — review directly." The handoff is the product, not the failure.
4. **Never compress hedged into known good.** The temptation is real (the output looks better confident); the cost is calibration debt that compounds.

## Examples
1. **Context Layer Demo's three states.** Same recommendation surface, three visual modes. Known good shows the synthesis as the headline. Hedged shows the synthesis with sources surfaced inline. Uncertain hides the synthesis entirely and surfaces the raw sources with a "we couldn't synthesize — review directly" note.
2. **Anthropic Claude's hedging registers.** "X." (assertive) / "I think X, but verify." (hedged) / "I don't have enough information to answer." (uncertain). The pattern this entry generalizes.
3. **Perplexity's "I don't know" path.** When the model can't ground an answer, the product surfaces the search results directly rather than fabricating. A working public example of the uncertain-band handoff.

## Related entries
- `corpus/ai-product-ux/patterns/confidence-indicators.md` — parent pattern
- `corpus/ai-product-ux/confidence/visual-encoding.md` — the visual scale this maps to
- `corpus/ai-product-ux/confidence/textual-encoding.md` — the language register for each band
- `corpus/ai-product-ux/confidence/calibration-anti-patterns.md` — how the three-band system breaks
- `corpus/ai-product-ux/failure/hallucination-handoff.md` — the uncertain-band handoff in detail

## Anti-patterns
- **Two-band collapse.** Treating hedged as known good (over-confident) or as uncertain (under-utilized). The middle band carries most of the product's value; collapsing it costs more than either extreme.
- **Hedging by default.** Every output is hedged "to be safe." Users learn that hedging means nothing and stop reading the qualifier.
