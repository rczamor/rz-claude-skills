---
name: Design for Trust
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: concept
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/16-edge-case-paranoia-design.md, corpus/ux-principles/principles/goodwill-reservoir.md, corpus/evaluation-frameworks/review-sections/11-design-ux-review.md]
---

# Design for Trust

## What it is
Every interface decision either builds or erodes user trust. Pixel-level intentionality about safety, identity, and belonging. The 10x CEO knows that trust is not built by trust badges or "secure" labels — it is built by the consistency, calm, and care visible in every interaction the user has with the product. A misaligned button erodes trust slightly. A confusing error message erodes it more. A surprise fee or a default-on tracking switch erodes it catastrophically.

## Why it matters
Trust is the resource the product spends to keep users. Plans rarely list "trust" as an outcome, because it isn't quantified the way revenue or retention are. But every other metric (retention, referral, willingness-to-pay) is downstream of trust. The 10x CEO reads every plan with a trust lens: which of these decisions is depositing into the trust account? Which is withdrawing? A plan that books a quarterly metric while withdrawing trust is borrowing against the future.

## How to apply
1. For every plan touching the user, ask: does this build or erode trust? Specifically: does it respect the user's time, attention, expectations, and prior relationship with the product?
2. Watch the "small" decisions: default-on toggles, surprise emails, opt-in dark patterns, hidden fees, microcopy that performs friendliness while doing something hostile. These are the trust killers.
3. Match the user's mental model. When the product behaves the way the user expected, trust deposits. When it surprises (in a non-delightful way), trust withdraws.
4. Trust is asymmetric: many small deposits produce slow growth; one large withdrawal produces fast loss. Plan accordingly.

## Examples
1. **Account deletion flow**: a plan that makes deletion easy, confirms once, and shows the user what's being deleted is a trust-builder. A plan that requires emailing support, hides the option in settings, or threatens consequences is a trust-killer that books retention this quarter and loses the relationship for life.
2. **Pricing page**: clear tier comparison, no asterisks, no "contact us" for stated features. Builds trust. The competitor's plan with hidden fees and dark-pattern upsells erodes it.
3. **Error message**: "Something went wrong" — withdraws. "We couldn't save your changes because the network dropped. Your work is preserved here. Try again?" — deposits.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/16-edge-case-paranoia-design.md` — edge cases are where trust is won or lost
- `corpus/ux-principles/principles/goodwill-reservoir.md` — Krug's goodwill reservoir is this concept's UX-principle expression
- `corpus/evaluation-frameworks/review-sections/11-design-ux-review.md` — Section 11's design-intentionality lens includes trust

## Anti-patterns
- Treating trust as a feature ("Add trust badges to checkout"). Trust is a property of the entire interaction, not a label.
- Withdrawing trust to hit a quarterly metric. The metric arrives; the trust does not return. The 10x CEO knows the trade-off and almost always sides with trust.
