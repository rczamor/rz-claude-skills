---
name: Inversion Reflex (Munger)
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: concept
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/02-paranoid-scanning.md, corpus/evaluation-frameworks/review-sections/01-architecture.md, corpus/evaluation-frameworks/review-sections/02-error-rescue-map.md]
---

# Inversion Reflex (Munger)

## What it is
For every "how do we win?" also ask "what would make us fail?" Charlie Munger's inversion: solve hard problems by asking the inverse first. If you want to find smart investments, list every way to lose money and avoid those. If you want a feature to succeed, list every way it could fail at scale and design those failures out before you write code. Inversion does not replace forward-thinking — it is a forcing function that surfaces the failure modes a forward-only review will miss.

## Why it matters
Forward-thinking generates plans. Inverted thinking generates rescue plans, threat models, and edge cases. A plan reviewed only forward will pass — looks coherent, ships on time, hits the metric on the happy path. A plan reviewed with inversion produces the error & rescue map, the data-flow shadow paths, the deploy-rollback tree. The 10x CEO does both as one move: every "we will" gets paired with "and if this fails, we will."

## How to apply
1. After reading a plan's stated objective, write the inverse on the next line: "What would have to be true for this to fail spectacularly?"
2. Generate at least 5 failure modes per major component: technical (crash, leak, timeout), operational (runbook missing, alert silent), product (user doesn't understand, user understands and doesn't care), strategic (competitor ships first, market shifts).
3. For each failure mode, ask: does the plan account for it? If no, decide: design it in, plan a rescue, or accept the risk explicitly.
4. Inversion is a generator, not a gate. Use it to find what to scrutinize harder — not to reject every plan that has unresolved failure modes.

## Examples
1. **API integration plan**: "How do we make this work?" Forward answer: handle 2xx responses, parse JSON, store result. Inverted: what if the API returns a 200 with malformed JSON, a 500 with a 30-second timeout, a 429 with no retry-after header, a payload twice the documented size? Now design Section 2's rescue map.
2. **Onboarding redesign**: "How do users complete it faster?" Inverted: how do we make users abandon mid-flow? Surface: too many fields, no progress indicator, blocking validation, mobile keyboard occluding inputs. Now design the protections.
3. **Pricing change**: "How do we increase revenue?" Inverted: how do existing customers learn about this and rage-quit? Surface: surprise email, no grandfathering, no migration window. Now plan the comms.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/02-paranoid-scanning.md` — scanning supplies the failure-mode candidates
- `corpus/evaluation-frameworks/review-sections/01-architecture.md` — Section 1 explicitly demands "what breaks first under 10x load?"
- `corpus/evaluation-frameworks/review-sections/02-error-rescue-map.md` — Section 2 IS inversion made into a deliverable

## Anti-patterns
- Inverting performatively (listing 30 failure modes, none of which are weighted or addressed). Inversion has to produce decisions, not anxiety.
- Stopping at one inverse. The first failure mode that comes to mind is rarely the one that kills you.
