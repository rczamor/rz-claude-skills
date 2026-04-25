---
name: RICE Scoring
domain: pm-frameworks
source_skill: research
entry_type: framework
length_target: 500
related: [corpus/pm-frameworks/prioritization/ice-scoring.md, corpus/pm-frameworks/prioritization/gem-prioritization.md, corpus/pm-frameworks/prioritization/wsjf.md]
---

# RICE Scoring

## What it is

A four-factor scoring formula introduced by Sean McBride at Intercom (2016) for ranking product initiatives:

**RICE = (Reach × Impact × Confidence) / Effort**

- **Reach:** how many users (or events) per time period the initiative will affect. Use real numbers (e.g. "8,000 users per quarter").
- **Impact:** estimated effect on the target metric per user reached. Often coded on a 5-point scale (3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal).
- **Confidence:** the team's confidence in the Reach and Impact estimates. Coded as a percentage (100% = high confidence, 80% = medium, 50% = low).
- **Effort:** total person-months required (PM, design, engineering combined).

The result is a comparable score across initiatives in the planning cycle.

## Why it matters

RICE makes prioritization assumptions explicit. Each input is a defensible estimate that can be challenged and revised. Reach forces the team to size the audience honestly; Impact forces a per-user-effect hypothesis; Confidence captures uncertainty; Effort prevents large-budget initiatives from monopolizing the roadmap on raw enthusiasm. The dividing structure (impact divided by effort) approximates ROI.

The framework is most useful when comparing initiatives within a similar metric domain. It breaks down comparing an engagement initiative to a compliance initiative — the metrics aren't commensurable.

## How to apply

1. **Define the time period** Reach is measured over (typically a quarter). Be consistent across all initiatives in the comparison.
2. **Estimate Reach** using real product data, not aspiration. Pull cohort sizes, funnel volumes, or feature-touch counts from analytics.
3. **Score Impact** against the target metric the team is accountable for. Don't mix metrics — prioritize within one.
4. **Set Confidence honestly.** Most teams default 80–100%; in practice, well-grounded confidence is rarely above 70% for new initiatives. Lower confidence numbers are a feature, not a bug.
5. **Estimate Effort in person-months.** Combine PM, design, and engineering. Round generously; effort estimates are systematically low.
6. **Calculate, rank, sanity-check.** If the top-ranked initiative is one nobody wanted, audit the inputs — usually Reach or Confidence is inflated.

## Examples

1. **Suzy quarterly planning.** Initiative A: in-app onboarding redesign. Reach: 3,000 new analysts/quarter. Impact: 2 (high — likely lifts activation 15%). Confidence: 70% (one A/B test on a precursor). Effort: 4 person-months. RICE = (3000 × 2 × 0.7) / 4 = 1,050. Initiative B: AI-recommended-studies. Reach: 8,000 active analysts. Impact: 2. Confidence: 40% (no test data, model quality unknown). Effort: 6 person-months. RICE = (8000 × 2 × 0.4) / 6 = 1,067. Roughly tied, but the confidence gap suggests sequencing A first to build evidence, then B.
2. **Cargo-cult RICE.** A team scoring everything as Reach=10000, Impact=3, Confidence=100%, Effort=1, producing identical scores. The framework was filled in but not applied.

## Related entries

- `corpus/pm-frameworks/prioritization/ice-scoring.md` — simpler three-factor variant
- `corpus/pm-frameworks/prioritization/gem-prioritization.md` — multi-axis alternative
- `corpus/pm-frameworks/prioritization/wsjf.md` — SAFe analog with risk and time-criticality factors

## Anti-patterns

- **Confidence inflation.** Defaulting Confidence to 100%. The variable's purpose is to deflate scores when evidence is thin; setting it to 1 collapses RICE into Reach × Impact / Effort.
- **Reach defined as TAM.** Reach is users-per-time-period actually affected — not "everyone who could theoretically be affected." TAM-as-Reach inflates everything proportionally and the rank order becomes meaningless.
