---
name: Section 10 — Long-Term Trajectory Review
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: template
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/09-temporal-depth.md, corpus/evaluation-frameworks/cognitive-patterns/01-classification-instinct.md, corpus/evaluation-frameworks/step-0/dream-state-mapping.md]
---

# Section 10 — Long-Term Trajectory Review

## What it is
Section 10 zooms out from the present plan to its position on a 12-month arc. It evaluates technical debt introduced (code, operational, testing, documentation), path dependency (does this make future changes harder?), knowledge concentration (sufficient documentation for a new engineer?), reversibility (rated 1-5: 1 = one-way door, 5 = easily reversible), ecosystem fit, and answers "the 1-year question" — read this plan as a new engineer in 12 months. Is it obvious?

## What it evaluates
- Technical debt introduced — code debt, operational debt, testing debt, documentation debt
- Path dependency — does this make future changes harder?
- Knowledge concentration — documentation sufficient for a new engineer?
- Reversibility — rate 1-5: 1 = one-way door, 5 = easily reversible
- Ecosystem fit — aligns with Rails/JS ecosystem direction?
- The 1-year question — read this plan as a new engineer in 12 months. Is it obvious?

## Required output format
A debt ledger and a reversibility rating:
```
  DEBT TYPE        | LEVEL | RATIONALE
  -----------------|-------|--------------------------------------
  Code             | Med   | Adds parallel implementation; can be unified later
  Operational      | Low   | Standard runbook; no new on-call complexity
  Testing          | Med   | E2E coverage gap on retry path
  Documentation    | High  | New concept, no architecture doc yet

  REVERSIBILITY: 3/5 — schema changes are reversible within 1 release; data backfill is one-way.
```

Plus the 1-year question answered explicitly:
```
  Q: A new engineer reads this in 12 months. Is it obvious?
  A: Mostly. The auth flow is documented; the rate-limiting rationale is not.
     Add a comment in `RateLimiter` explaining the 60-rps choice and the alternative considered.
```

## Mode-specific additions
**EXPANSION and SELECTIVE EXPANSION**:
- What comes after this ships? Phase 2? Phase 3? Does the architecture support that trajectory?
- Platform potential — does this create capabilities other features can leverage?
- (SELECTIVE EXPANSION only) Retrospective: were the right cherry-picks accepted? Did any rejected expansions turn out to be load-bearing for the accepted ones?

## Rules in force
- **STOP. AskUserQuestion once per issue.** Do NOT batch. Recommend + WHY. If no issues or fix is obvious, state what you'll do and move on — don't waste a question. Do NOT proceed until user responds.
- **Do NOT make any code changes. Review only.**

## Why it matters
Plans that pass every other section can still fail Section 10. A correctly-implemented, well-tested, observable feature can still create path dependency that paints the team into a corner 9 months from now. Section 10 forces the long view: the 1-year question is the closest a plan review gets to time-travel. The reversibility rating is the closest the review gets to giving the team a quantitative handle on "how much should I pad my confidence?"

## Examples
1. **Plan picks a vendor for a critical service**: Section 10 reversibility rating is 1 (one-way door). The plan needs the same level of due diligence as a hire.
2. **Plan adds a new pattern that conflicts with existing patterns**: Section 10 surfaces the path dependency — every future feature that touches this surface will inherit the conflict.
3. **Plan is coherent but undocumented**: Section 10's 1-year question answers "no, a new engineer would be lost." Add the doc; the cost is hours, the value compounds for years.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/09-temporal-depth.md` — pattern 9 IS Section 10's underlying instinct
- `corpus/evaluation-frameworks/cognitive-patterns/01-classification-instinct.md` — Section 10's reversibility rating IS classification operationalized
- `corpus/evaluation-frameworks/step-0/dream-state-mapping.md` — Section 10 closes the loop on Step 0's dream-state delta

## Anti-patterns
- Reversibility theater: rating every plan a 4 or 5 because it "feels" reversible. Many features that look reversible are not — schema changes, customer expectations, brand promises.
- Treating documentation as "polish." It is the most leveraged investment in Section 10. The plan that documents itself ages well.
