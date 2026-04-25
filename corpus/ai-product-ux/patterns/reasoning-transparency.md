---
name: Reasoning Transparency
domain: ai-product-ux
source_skill: product-design
entry_type: pattern
length_target: 700
related: [corpus/ai-product-ux/reasoning/sidebar-pattern.md, corpus/ai-product-ux/reasoning/show-the-work-rule.md, corpus/ai-product-ux/patterns/confidence-indicators.md, corpus/voice/hook-data-is-not-context.md, corpus/pm-frameworks/ai-product-pm/non-determinism.md]
---

# Reasoning Transparency

## What it is
Reasoning transparency is the AI UX pattern of showing users *why* the AI made a decision, not just *what* it decided. The output is the claim; the reasoning is the warrant. When a user can inspect the chain of inference — the sources pulled, the steps followed, the trade-offs weighed — they trust the system enough to act on it. Without it, every output is a black box that demands either blind faith or independent verification, and most users choose verification.

## Why it matters
AI is non-deterministic. A user who sees output X today and X' tomorrow on the same prompt will lose trust unless the reasoning explains why X and X' both fit. Reasoning transparency converts model variance from a defect into a legible feature. It also creates the audit surface that enterprise buyers require — the same buyers Riché's Suzy Decision Engine and Context Layer Demo target. Hide the reasoning and the AI looks like a magic trick. Show the reasoning and it looks like a colleague who can be questioned, refined, and corrected.

## How to apply
1. **Default to a reasoning sidebar** — collapsible, scrollable, time-stamped. The Context Layer Demo uses one to expose the five-step context flow at each decision point.
2. **Reasoning shown is reasoning that can be challenged.** Surface enough that a user can disagree with a step, not so much that they tune out.
3. **Pair every output with its warrant.** A claim without a warrant looks confident; a claim with one looks accountable.
4. **Never auto-collapse when uncertainty is high.** If confidence is low, the reasoning is the product.

## Examples
1. **Context Layer Demo reasoning sidebar.** When the demo synthesizes a recommendation, the right panel shows: which of the five context steps fired, what data was retrieved, what was filtered, and the prompt that went to the model. Users can replay any decision.
2. **Suzy Decision Engine launch.** Six-week transformation across 350+ enterprise customers required reasoning transparency at every recommendation — buyers would not approve autonomous insights without a visible chain back to the underlying research panel data.
3. **GitHub Copilot's "Why this suggestion?"** is a minimal reasoning surface — even a one-line warrant raises trust above zero.

## Related entries
- `corpus/ai-product-ux/reasoning/sidebar-pattern.md` — the canonical UI implementation
- `corpus/ai-product-ux/reasoning/show-the-work-rule.md` — the operating rule
- `corpus/ai-product-ux/patterns/confidence-indicators.md` — pairs with reasoning to calibrate trust
- `corpus/voice/hook-data-is-not-context.md` — the thesis this pattern demonstrates
- `corpus/pm-frameworks/ai-product-pm/non-determinism.md` — the constraint that makes reasoning transparency load-bearing

## Anti-patterns
- **Pretty disclosure that hides the work.** A "Show details" link that reveals a paraphrased summary, not the actual chain, is theater.
- **Too much reasoning.** Dumping the full prompt + retrieved chunks teaches the user nothing; it just shifts the cognitive load. Curate the reasoning the way you'd curate a chart axis — keep what supports the decision, drop what doesn't.
