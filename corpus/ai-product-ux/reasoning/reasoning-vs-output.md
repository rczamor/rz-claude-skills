---
name: Reasoning vs. Output
domain: ai-product-ux
source_skill: product-design
entry_type: concept
length_target: 600
related: [corpus/ai-product-ux/patterns/reasoning-transparency.md, corpus/ai-product-ux/reasoning/sidebar-pattern.md, corpus/ai-product-ux/reasoning/show-the-work-rule.md, corpus/ai-product-ux/reasoning/skip-reasoning-rule.md, corpus/pm-frameworks/ai-product-pm/non-determinism.md]
---

# Reasoning vs. Output

## What it is
A concept. The output of an AI is a **claim**. The reasoning is the **warrant** for that claim. Users need both to act. A claim without a warrant is an assertion that demands faith; a warrant without a claim is process without product. Designing AI products means designing claim and warrant together — and giving them parity in the interface.

## Why it matters
Most AI products design for the claim and treat the warrant as optional. The result is a polished output that the user cannot interrogate. When the claim is right, the user accepts on faith; when the claim is wrong, the user has no idea why and can't course-correct. Treating reasoning as a peer to output — not a footnote — restores the user's ability to think with the AI rather than around it.

## How to apply
1. **Design the warrant alongside the claim.** Wireframes show both surfaces simultaneously. If the warrant doesn't fit, the layout is wrong.
2. **Allocate review time equally.** If the team spends 10x longer polishing the answer than the reasoning, the imbalance ships.
3. **Use the same vocabulary in both.** If the claim says "Q3 launch is recommended," the reasoning shouldn't say "the temporal decision tree converged on a Q3 outcome." The warrant must read in the same register as the claim.
4. **Test both surfaces with users.** "Does the claim feel decisive?" and "Does the reasoning feel inspectable?" are separate questions with separate answers.

## Examples
1. **Context Layer Demo's parity.** The synthesis card and the reasoning sidebar share visual weight, typography, and motion. Neither is subordinate. The user can spend their attention on either without feeling they are leaving the product.
2. **Suzy Decision Engine's insight + provenance pairing.** The insight card and the underlying panel-data view are presented as a pair. Buyers don't experience one as the answer and the other as the receipt — they experience both as the product.
3. **Counter-example: most LLM chat UIs.** The output dominates; the reasoning (when shown at all) is a smaller, grayer, more cramped surface. The hierarchy implies "the answer is what matters; the reasoning is for nerds." Riché's products refuse this hierarchy.

## Related entries
- `corpus/ai-product-ux/patterns/reasoning-transparency.md` — parent pattern
- `corpus/ai-product-ux/reasoning/sidebar-pattern.md` — the canonical UI
- `corpus/ai-product-ux/reasoning/show-the-work-rule.md` — the operating rule
- `corpus/ai-product-ux/reasoning/skip-reasoning-rule.md` — the user's right to skip
- `corpus/pm-frameworks/ai-product-pm/non-determinism.md` — why warrant matters more than in deterministic products

## Anti-patterns
- **Output-first design.** The claim gets a beautiful card; the warrant gets a tooltip. The hierarchy is the message.
- **Warrant-first design.** The reasoning is the show; the answer is buried. Useful for technical demos, useless for users who came for an answer.
