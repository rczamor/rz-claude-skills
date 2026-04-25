---
name: Implementation Alternatives (Step 0C-bis)
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: template
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/01-classification-instinct.md, corpus/evaluation-frameworks/step-0/premise-challenge.md, corpus/pm-frameworks/strategy/]
---

# Implementation Alternatives (Step 0C-bis)

## What it is
A mandatory step in every CEO plan review. Before mode selection, before Section 1, the reviewer must produce 2-3 distinct implementation approaches and recommend one. This is NOT optional — every plan must consider alternatives. The minimal-viable and ideal-architecture approaches have **equal weight**: don't default to "minimal" just because it's smaller, and don't default to "ideal" because it sounds more rigorous. Recommend whichever best serves the user's goal.

## The required format
```
APPROACH A: [Name]
  Summary: [1-2 sentences]
  Effort:  [S/M/L/XL]
  Risk:    [Low/Med/High]
  Pros:    [2-3 bullets]
  Cons:    [2-3 bullets]
  Reuses:  [existing code/patterns leveraged]

APPROACH B: [Name]
  ...

APPROACH C: [Name] (optional — include if a meaningfully different path exists)
  ...
```

Then:
```
RECOMMENDATION: Choose [X] because [one-line reason mapped to engineering preferences].
```

## The rules
- **At least 2 approaches required.** 3 preferred for non-trivial plans.
- **One approach must be the "minimal viable"** (fewest files, smallest diff).
- **One approach must be the "ideal architecture"** (best long-term trajectory).
- **These two have equal weight.** If the right answer is a rewrite, say so. If the right answer is the smallest possible patch, say so.
- If only one approach exists, **explain concretely why alternatives were eliminated**. "There's only one way to do this" is rarely true; surface the eliminated paths.
- Do NOT proceed to mode selection (0F) without user approval of the chosen approach.

## How to use the format
1. Read the plan. Sketch the approach the plan implies (often that becomes Approach A or B).
2. Generate the **minimal viable** approach. Forced exercise: if the team had 4 hours and one engineer, what would they ship? That's minimal viable.
3. Generate the **ideal architecture** approach. Forced exercise: if the team had unlimited time and the right people, what would they build? That's ideal.
4. If a meaningfully different third path exists (different vendor, different paradigm, different abstraction level), include it.
5. Map the trade-offs honestly. Don't bias the framing toward your preferred recommendation.
6. Recommend with a one-line reason. The reason must map to a stated engineering preference (speed-to-ship, long-term simplicity, code reuse, observability), not to vibes.

## Why "equal weight" matters
The default reviewer bias is toward "minimal viable" because it's safer-looking. But sometimes the right answer is the rewrite. Other times the bias goes the other way — toward the ambitious architecture because it sounds more rigorous. The equal-weight rule defends against both biases. Recommend whichever approach the user's goal actually requires.

## Required output format
The 2-3 approach blocks above, plus the RECOMMENDATION line. Presented to the user via AskUserQuestion (with the preamble's AskUserQuestion format), since these approaches differ in coverage (minimal vs. ideal), so completeness scoring applies.

## Why it matters
Plans that bypass alternatives default to whatever the author wrote first. The first approach that comes to mind is rarely the best one. Forcing 2-3 alternatives produces 2-3 chances to find the right answer. The discipline is unglamorous (the second and third approach are often clearly worse, which is fine — the goal is contrast, not all candidates being viable). Doing it consistently is what separates plans that survive contact from plans that pivot mid-implementation.

## Examples
1. **Plan adds a notification system**. Approach A (minimal): cron job that polls a table. Approach B (ideal): event-driven publisher with webhook endpoints. Approach C (vendor): use Twilio/SendGrid. Trade-offs surfaced; recommendation maps to user's actual goal.
2. **Plan introduces a new API**. Approach A: extend existing REST endpoints. Approach B: build a parallel GraphQL surface. Approach C: keep REST, add GraphQL only for one specific use case. Recommendation depends on whether the user prioritizes API consistency or query flexibility.
3. **Single-approach plan defended**. Plan to migrate database vendor. Often "we'll use Postgres" is the only viable approach given the constraints. The format demands explaining why MySQL, SQLite, and others were eliminated. The eliminated paths sometimes surface a constraint that hadn't been named.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/01-classification-instinct.md` — alternatives generation is how you avoid one-way doors by accident
- `corpus/evaluation-frameworks/step-0/premise-challenge.md` — premise challenge generates the alternatives this step structures
- `corpus/pm-frameworks/strategy/` — strategic options thinking lives here

## Anti-patterns
- Generating alternatives the reviewer doesn't believe in. The contrast is the value, but the alternatives must be plausibly defensible. Strawmen waste the user's time.
- Skipping the recommendation. The format demands a recommendation with a reason — abdicating the recommendation to the user is not the reviewer's job.
