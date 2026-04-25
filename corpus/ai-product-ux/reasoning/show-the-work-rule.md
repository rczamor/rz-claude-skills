---
name: Show-the-Work Rule
domain: ai-product-ux
source_skill: product-design
entry_type: rule
length_target: 500
related: [corpus/ai-product-ux/patterns/reasoning-transparency.md, corpus/ai-product-ux/reasoning/sidebar-pattern.md, corpus/ai-product-ux/reasoning/reasoning-vs-output.md, corpus/ai-product-ux/reasoning/skip-reasoning-rule.md]
---

# Show-the-Work Rule

## What it is
A rule. Reasoning shown is reasoning that can be challenged by the user. The corollary: reasoning hidden is reasoning the product is asking the user to take on faith. Every visible reasoning step is an invitation to disagree, correct, or refine. Every hidden step is an act of authority.

## Why it matters
Faith doesn't scale. A user can extend faith for one or two outputs; by the tenth, they want to verify. A product that hides reasoning forces the user into a binary: trust everything or distrust everything. A product that shows reasoning lets the user trust granularly — accept this step, question that one, override another. Granular trust is durable; binary trust is brittle.

## How to apply
1. **Every step in the reasoning sidebar is a click target.** Click to see the inputs, the alternatives, the rationale.
2. **Provide a "this is wrong" affordance per step.** When the user spots a bad step, they should be able to flag it without leaving the surface. The flag becomes correction data.
3. **Never display reasoning the user cannot challenge.** A step that says "the model decided X" with no further depth is decoration. Either show the depth or remove the step.
4. **The reasoning must match the output.** If the displayed reasoning would not actually produce the displayed output, the user catches the mismatch and trust collapses. Generated reasoning ≠ displayed reasoning is the worst failure mode.

## Examples
1. **Context Layer Demo's per-step "challenge this" button.** Each step in the reasoning sidebar carries a "this looks wrong" affordance. The flag opens a correction interface scoped to that step. The user's challenge becomes the next iteration's input.
2. **Anthropic's "show your work" emphasis in Constitutional AI.** The principle that the model should explain its reasoning *and* be willing to be questioned about it — operationalized as a UI pattern.

## Related entries
- `corpus/ai-product-ux/patterns/reasoning-transparency.md` — parent pattern
- `corpus/ai-product-ux/reasoning/sidebar-pattern.md` — the canonical UI
- `corpus/ai-product-ux/reasoning/reasoning-vs-output.md` — the conceptual basis
- `corpus/ai-product-ux/reasoning/skip-reasoning-rule.md` — the complementary rule

## Anti-patterns
- **Read-only reasoning.** Showing the steps but offering no way to challenge them. The display becomes pedagogy, not product.
- **Sanitized reasoning.** Cleaning up the actual chain into a presentable summary. The user catches the gap between the polished display and the messy reality and stops trusting the surface.
