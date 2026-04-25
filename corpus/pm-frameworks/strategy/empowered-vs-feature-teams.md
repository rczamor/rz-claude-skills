---
name: Empowered vs Feature Teams
domain: pm-frameworks
source_skill: product-management
entry_type: framework
length_target: 600
related: [corpus/pm-frameworks/thinkers/cagan-marty.md, corpus/pm-frameworks/strategy/product-operating-model.md, corpus/pm-frameworks/strategy/trust-barrier.md, corpus/pm-frameworks/discovery/continuous-discovery-habits.md]
---

# Empowered vs Feature Teams

## What it is

Marty Cagan's distinction between two operating models for product teams:

- **Feature teams** are given features (or projects, or releases) to ship. They're measured on output: did the feature ship on time? Did it match the spec? The PM is effectively a project manager translating stakeholder requests into tickets.
- **Empowered teams** are given **problems** to solve and outcomes to achieve. They discover the right solution through customer research, prototyping, and assumption testing. They're measured on outcomes: did engagement improve? Did churn drop? The PM is a product strategist owning the problem.

Same headcount; same engineers, designers, PMs. Radically different output and engagement.

From Cagan's *Empowered* (2020).

## Why it matters

The distinction explains most of the variance in product team performance. Feature teams ship more features but produce less value because the features are dictated, not discovered. Empowered teams ship fewer features but each one has been validated against customer evidence — the hit rate is higher.

The distinction also explains team retention. Strong PMs, designers, and engineers don't stay at feature-team companies — they get bored and leave. Cagan's empirical claim, supported by SVPG's two decades of practice, is that empowerment and talent quality are tightly correlated.

For AI products specifically, the empowerment model is more important, not less. AI compresses execution time, which raises the premium on judgment about what to build. Feature teams in AI shops produce a stream of capability demos that don't compound into product. Empowered teams produce fewer launches that compound into a defensible product.

## How to apply

1. **Audit team assignments.** Are teams given features ("ship the AI recommendations panel by Q3") or problems ("increase weekly active analysts; the strategy bet is recommendations")? The phrasing reveals everything.
2. **Test the PM's authority.** Can the PM choose not to build a feature in their problem space if discovery shows it's the wrong solution? In a feature team, no. In an empowered team, yes — that's the empowerment.
3. **Provide strategic context.** Empowered teams need rich context: vision, strategy, target customers, business constraints. Without context, empowerment becomes anarchy. Cagan: "context replaces control."
4. **Hold teams accountable for outcomes.** Output (features shipped) is operational hygiene. Outcomes (metrics moved) are the contract.
5. **Earn the trust to empower.** See `trust-barrier.md` — empowerment is granted, not declared. Most failed transformations skip this.

## Examples

1. **Suzy Insights team transition.** Pre-transition: team given a quarterly feature list ("ship recommendations, ship templates, ship briefings"). Post-transition: team given an outcome ("increase analyst weekly active rate") with strategic context (the bets) and authority to choose the solution. Within two quarters, the team killed two of the original features and built a different one that moved the outcome. Same people, different operating model.
2. **Anti-pattern (industry).** A "transformation" that renames feature teams "empowered teams" but preserves the feature-list assignment and output-only metrics. Nothing changes except vocabulary; the talent that joined for empowerment leaves within six months.

## Related entries

- `corpus/pm-frameworks/thinkers/cagan-marty.md` — Cagan's broader practice
- `corpus/pm-frameworks/strategy/product-operating-model.md` — the surrounding system
- `corpus/pm-frameworks/strategy/trust-barrier.md` — the prerequisite for empowerment
- `corpus/pm-frameworks/discovery/continuous-discovery-habits.md` — empowered teams require continuous discovery to function

## Anti-patterns

- **Empowerment-in-name.** Calling teams "empowered" without removing the feature mandate. The naming change makes the failure harder to diagnose.
- **Empowerment-without-context.** Telling teams to "figure it out" without providing vision, strategy, customer context, or business constraints. The teams thrash; leadership concludes empowerment doesn't work; the model gets blamed when the missing piece was strategic context.
