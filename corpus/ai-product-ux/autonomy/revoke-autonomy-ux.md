---
name: Revoke-Autonomy UX
domain: ai-product-ux
source_skill: research
entry_type: pattern
length_target: 500
related: [corpus/ai-product-ux/patterns/progressive-autonomy.md, corpus/ai-product-ux/autonomy/three-tier-model.md, corpus/ai-product-ux/autonomy/trust-building-pattern.md, corpus/ai-product-ux/failure/error-recovery-paths.md]
---

# Revoke-Autonomy UX

## What it is
A pattern: an easy off-ramp when the AI errs in a higher autonomy tier. One-click drop from autonomous back to confirmed, or from confirmed back to suggested. Restores human-in-the-loop without friction. Adapted from public AI UX canon — Anthropic's emphasis on user controllability in Constitutional AI, Google PAIR's "user is always in control" guideline — into a product-shippable affordance.

## Why it matters
The first error in autonomous mode is the moment of trust collapse. Users either find a one-click revoke (and stay in the product, just at a lower tier) or they find no revoke (and abandon the autonomy entirely, often the product). The asymmetry is huge: a friction-free revoke preserves the relationship; a hidden or multi-step revoke ends it. Designing the revoke path is as important as designing the promotion path — and most products skip it.

## How to apply
1. **One-click, surface-level.** A revoke control in the same surface where the user encounters the error — not buried in settings.
2. **Drop one tier, not all the way.** Autonomous → confirmed is the default revoke. Don't force the user back to suggested unless they choose to.
3. **Preserve corrections.** Revoking autonomy doesn't reset the trust meter to zero. The accept-rate history persists; the user can re-promote later if they choose.
4. **Acknowledge the error inline.** "We auto-completed this and got it wrong. Switching back to confirm-first." The acknowledgment is half the recovery.
5. **Never punish revoke.** No "are you sure" modals, no friction. The whole pattern's value is the lack of friction.

## Examples
1. **Suzy Decision Engine's "pause autonomous insights" toggle.** A single toggle in the workspace header. Click drops all autonomous insight types back to confirmed mode. The accept-rate history is preserved; the user can re-enable later.
2. **Context Layer Demo's per-action revoke chip.** When the demo executes an autonomous action and the user spots an error, a small "switch back to confirm" chip appears next to the action. One click, instant tier drop.
3. **Cursor's "stop agent" button.** The agent-mode equivalent — visible at all times, one-click to stop autonomous execution and return to manual.

## Related entries
- `corpus/ai-product-ux/patterns/progressive-autonomy.md` — parent pattern
- `corpus/ai-product-ux/autonomy/three-tier-model.md` — the framework that makes "drop one tier" meaningful
- `corpus/ai-product-ux/autonomy/trust-building-pattern.md` — the loop this pattern preserves on error
- `corpus/ai-product-ux/failure/error-recovery-paths.md` — the wider error-recovery context

## Anti-patterns
- **Hidden revoke.** Buried in settings two clicks deep. The first error becomes the last interaction.
- **Punitive revoke.** Confirmation modals, multi-step flows, "you'll lose your trust history." All friction is hostile here.
