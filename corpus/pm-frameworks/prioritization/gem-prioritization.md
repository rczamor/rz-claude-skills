---
name: GEM Prioritization
domain: pm-frameworks
source_skill: product-management
entry_type: framework
length_target: 600
related: [corpus/pm-frameworks/thinkers/biddle-gibson.md, corpus/pm-frameworks/strategy/dhm-model.md, corpus/pm-frameworks/prioritization/rice-scoring.md, corpus/pm-frameworks/metrics/consumer-science.md]
---

# GEM Prioritization

## What it is

Gibson Biddle's three-axis scoring framework for product initiatives — score each candidate initiative on its expected impact on:

- **Growth (G):** acquisition of new users; expansion to new segments; viral or paid reach.
- **Engagement (E):** depth and frequency of existing-user behavior; activation of dormant users; habit formation.
- **Monetization (M):** revenue from existing users; conversion of free to paid; expansion ARPA; pricing leverage.

Each initiative receives a G, E, and M score (often 1–5). Roadmap construction balances the three: an all-G roadmap acquires users who don't engage; an all-E roadmap deepens use without paying for itself; an all-M roadmap optimizes the existing base into churn.

Developed by Biddle during his time at Netflix and Chegg; taught in his "Ask Gib" sessions and Reforge courses.

## Why it matters

Most prioritization frameworks (RICE, ICE) collapse impact into a single dimension. GEM resists that compression. A growth initiative and a monetization initiative are different *kinds* of bets with different risk profiles, time horizons, and downstream effects. Scoring on one impact axis hides those distinctions; scoring on three keeps them visible.

GEM also surfaces strategic imbalance early. A team optimizing only on M (because revenue is the loudest stakeholder demand) can be redirected before the engagement debt compounds into churn. A team optimizing only on G (because the board funds it) can be redirected before the engagement and monetization gaps make the growth unsustainable.

For AI products, GEM is especially useful because the three axes have different AI-economic dynamics: growth (often viral via AI demos) can outpace monetization (constrained by inference costs), creating a compounding loss if the team doesn't rebalance.

## How to apply

1. **List candidate initiatives** for the planning cycle. Aim for 8–15; smaller lists hide tradeoffs.
2. **Score each on G, E, and M** (1–5 each). Use evidence (cohort data, A/B test results, comparable benchmarks) to ground scores.
3. **Plot the portfolio.** What's the G/E/M mix? Is the team over-indexed on one axis?
4. **Sequence with intentional balance.** Each quarter, choose initiatives that collectively move all three axes (unless strategy explicitly de-prioritizes one — e.g. a startup pre-monetization).
5. **Pair with consumer science** (Biddle's other framework): each initiative should have a hypothesis, an experiment, and a data plan.

## Examples

1. **Suzy roadmap balancing.** Five Q-priority initiatives scored on GEM revealed four high-M initiatives and zero high-E. The team was about to optimize a base they were also failing to engage. Rebalancing inserted one high-E initiative (in-app analyst onboarding flow) — which then improved M-conversion downstream.
2. **Netflix (per Biddle's teaching).** "Profiles" feature scored high E (personalization deepens usage), modest G (drove some household-account expansion), low M (didn't change subscription pricing). High-E investment justified despite low immediate M, because it raised retention, which raises lifetime M.

## Related entries

- `corpus/pm-frameworks/thinkers/biddle-gibson.md` — Biddle's broader practice
- `corpus/pm-frameworks/strategy/dhm-model.md` — DHM is the strategy lens; GEM is the execution lens
- `corpus/pm-frameworks/prioritization/rice-scoring.md` — collapsed-axis alternative
- `corpus/pm-frameworks/metrics/consumer-science.md` — paired hypothesis discipline
- `corpus/pm-frameworks/metrics/aarrr-funnel.md` — GEM aligns with funnel stages

## Anti-patterns

- **Score inflation.** Every initiative scored 5/5/5. The rubric is compromised; rescore against a baseline initiative everyone agrees is moderate.
- **Treating GEM as exhaustive.** GEM is a balance check, not the whole strategy. An initiative that scores low on all three but is required for compliance, defensibility, or platform debt still belongs on the roadmap — captured separately, not scored away.
