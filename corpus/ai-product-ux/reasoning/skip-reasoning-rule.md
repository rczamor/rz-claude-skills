---
name: Skip-Reasoning Rule
domain: ai-product-ux
source_skill: product-design
entry_type: rule
length_target: 500
related: [corpus/ai-product-ux/patterns/reasoning-transparency.md, corpus/ai-product-ux/reasoning/sidebar-pattern.md, corpus/ai-product-ux/reasoning/show-the-work-rule.md, corpus/ai-product-ux/confidence/expressing-uncertainty.md]
---

# Skip-Reasoning Rule

## What it is
A rule. Users may skip reasoning by default — but the product must never auto-collapse the reasoning when uncertainty is high. Low-confidence outputs require the reasoning to be visible; the user shouldn't have to find it. High-confidence outputs allow the reasoning to stay collapsed unless the user opens it.

## Why it matters
Power users hate friction. A product that forces reasoning open on every output trains users to ignore it. Equally, a product that always collapses reasoning hides the warrant exactly when the user needs it most — when the output is uncertain. The rule operationalizes the trade-off: skip is the default for known-good outputs; visible-by-default for hedged or uncertain outputs. The product reads the room.

## How to apply
1. **Default sidebar state per output, not per session.** Same sidebar opens collapsed for a known-good output and expanded for an uncertain one.
2. **Tie the default to the confidence band.** Known good → collapsed. Hedged → collapsed but with a one-line teaser. Uncertain → expanded.
3. **Persist the user's choice within an output, not across.** If the user collapses an uncertain output's reasoning, respect that — but the next uncertain output gets expanded again.
4. **Never auto-collapse mid-stream.** If the reasoning is rendering and the user is reading, don't snap it shut.

## Examples
1. **Context Layer Demo's auto-expand on hedged outputs.** When the synthesis is hedged or uncertain, the reasoning sidebar auto-expands. When the synthesis is known-good, it collapses with a "see reasoning" affordance. Users find this calibrated rather than naggy.
2. **Anthropic Claude's extended thinking pattern.** Thinking blocks are collapsed by default for routine outputs and expanded for complex ones. Same calibration, different surface.

## Related entries
- `corpus/ai-product-ux/patterns/reasoning-transparency.md` — parent pattern
- `corpus/ai-product-ux/reasoning/sidebar-pattern.md` — the surface this rule governs
- `corpus/ai-product-ux/reasoning/show-the-work-rule.md` — the complementary rule
- `corpus/ai-product-ux/confidence/expressing-uncertainty.md` — the bands that drive the default

## Anti-patterns
- **Always-expanded reasoning.** Every output ships with a wall of reasoning. Users learn to ignore it.
- **Always-collapsed reasoning.** The reasoning is hidden for every output, including hallucinations and hedges. Users miss the warrant when they need it most.
