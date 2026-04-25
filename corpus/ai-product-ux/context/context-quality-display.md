---
name: Context Quality Display
domain: ai-product-ux
source_skill: product-design
entry_type: template
length_target: 600
related: [corpus/ai-product-ux/patterns/context-display.md, corpus/ai-product-ux/context/sources-panel.md, corpus/ai-product-ux/context/correction-interface.md, corpus/pm-frameworks/ai-product-pm/five-step-context-generation.md, corpus/voice/hook-data-is-not-context.md]
---

# Context Quality Display

## What it is
A template UI for surfacing the four context-quality dimensions from the five-step framework: **freshness** (how recent), **consistency** (how much sources agree), **completeness** (how much of the question is covered), **goal-alignment** (how well the context matches the user's intent). Each dimension gets a score; the scores live near the synthesis they produced. Quality display turns "context" from a vibe into a measured input.

## Why it matters
Users intuit that some answers are better-grounded than others. Without quality scores, they have to read every source to figure out which. With scores, they can scan and act. The four dimensions are not arbitrary — each surfaces a distinct failure mode. Stale freshness flags an outdated answer; low consistency flags contradicting sources; low completeness flags coverage gaps; weak goal-alignment flags retrieval drift. Together, they are the diagnostic panel for context health.

## How to apply
1. **Display all four, always.** A single "context score" averages away the diagnostic value. Users need to see which dimension is weak.
2. **Map each dimension to a simple scale (e.g. 0–100 or three-band).** Match the visual encoding from `confidence/visual-encoding.md`.
3. **Make each score clickable to the contributing sources.** Click freshness → see retrieval dates. Click consistency → see the disagreement. The score is an entry point, not a verdict.
4. **Surface the weakest dimension as the headline.** "Consistency low — sources disagree on Q3 vs Q4." That's the actionable finding.
5. **Never hide low scores.** A 30/100 freshness score must be visible; surfacing it builds trust faster than hiding it.

## Examples
1. **Context Layer Demo's four-quadrant quality readout.** Above every synthesis sits a four-quadrant chip: Fresh / Consistent / Complete / Aligned. Each quadrant fills based on the score. A weak quadrant is the user's next click.
2. **Suzy Decision Engine's panel-quality readout.** Each automated insight surfaces sample size (completeness), inter-respondent agreement (consistency), recency of fielding (freshness), and brief-alignment score (goal-alignment). Buyers use the four scores to decide whether to ship the insight.

## Related entries
- `corpus/ai-product-ux/patterns/context-display.md` — parent pattern
- `corpus/ai-product-ux/context/sources-panel.md` — the underlying sources the scores summarize
- `corpus/ai-product-ux/context/correction-interface.md` — what users do when scores are weak
- `corpus/pm-frameworks/ai-product-pm/five-step-context-generation.md` — where the four dimensions come from
- `corpus/voice/hook-data-is-not-context.md` — the thesis the scores operationalize

## Anti-patterns
- **Single composite score.** "Context quality: 84." The number flatters but tells the user nothing actionable.
- **Quality scores with no click-through.** A pretty chart that doesn't let the user diagnose. The display became decoration.
