---
name: Product Vision and Strategy
domain: pm-frameworks
source_skill: product-management
entry_type: framework
length_target: 600
related: [corpus/pm-frameworks/thinkers/cagan-marty.md, corpus/pm-frameworks/strategy/product-strategy-stack.md, corpus/pm-frameworks/strategy/empowered-vs-feature-teams.md, corpus/pm-frameworks/strategy/product-operating-model.md]
---

# Product Vision and Strategy

## What it is

Marty Cagan's distinction between two distinct strategic artifacts:

- **Product Vision:** spans **years** (3–10). Customer-centric, inspiring, evocative. Describes the future world the product is creating. Not a roadmap; a destination. Stable — changes only when the company itself fundamentally pivots.
- **Product Strategy:** updated **quarterly**. Specific. Identifies focus areas, strategic insights about customer/market/technology, and the bets the company is making to advance toward the vision. Concrete enough that team objectives flow directly from it.

Team objectives (OKRs, outcomes) flow from strategy; strategy flows from vision. Each layer should trace cleanly to the layer above.

From Cagan's *Inspired* (2017), *Empowered* (2020), and SVPG materials.

## Why it matters

Most companies confuse vision and strategy, with three failure modes:
1. **Vision-as-strategy.** "We want to democratize X" — beautiful but unactionable. No team can decide what to build next from a vision alone.
2. **Strategy-as-vision.** "Q3 strategy: ship the analytics dashboard." Tactical, time-bound, no destination — the team executes but doesn't know why.
3. **No connection between layers.** Vision in a frame on the wall; strategy in a Notion doc nobody reads; team OKRs disconnected from both.

Cagan's separation forces both: a stable destination *and* a quarterly bet on how to get closer. The combination produces empowered teams (problems to solve, not features to ship) without devolving into chaos (everyone has the same destination in mind).

For AI products, this distinction is especially load-bearing. Model capabilities shift quarterly — strategy must respond. Customer outcomes shift slowly — vision should not. Confusing the two causes either thrash (changing vision every quarter) or stagnation (refusing to update strategy when the model landscape shifts).

## How to apply

1. **Author the vision.** Customer-centric (the customer's future state, not the company's). Years out. Specific enough to be evocative, abstract enough to outlive any one product. Test: would this still apply if the product were redesigned ground-up?
2. **Author the quarterly strategy.** Three components: focus areas (where will we invest?), strategic insights (what do we believe about customers/market/tech?), and bets (what specific things will we try?).
3. **Map team objectives to strategy.** Every team OKR or outcome should trace to a strategy bet. If it doesn't, either the strategy is incomplete or the team is freelancing.
4. **Re-author strategy quarterly.** The cadence is non-negotiable. If your strategy doc hasn't been touched in two quarters, you don't have one.
5. **Test the vision rarely.** Vision changes are existential events, not routine ones. If you change the vision more than once every two years, it wasn't a vision.

## Examples

1. **Suzy Decision Engine.** Vision (years): a world where every consumer-facing decision is grounded in a real-time view of what people think, feel, and need. Quarterly strategy (Q3): focus area is the Insights pillar; strategic insight is that analyst confidence (not speed) determines re-engagement; bets include AI-recommended studies, methodology coaching, and stakeholder briefing summaries. Team OKRs flow from those bets.
2. **Helm Labs.** Vision: PE portfolio CFOs have audit-grade close visibility on demand. Strategy at launch: focus area is variance-explanation automation; strategic insight is that audit firms are the actual buying influencers, not CFOs alone; bets include a dual-relationship sales motion and a variance-narrative generator.

## Related entries

- `corpus/pm-frameworks/thinkers/cagan-marty.md` — Cagan's broader practice
- `corpus/pm-frameworks/strategy/product-strategy-stack.md` — Rekhi's mission/strategy/product-strategy/roadmap stack (compatible)
- `corpus/pm-frameworks/strategy/empowered-vs-feature-teams.md` — empowered teams need strategic context
- `corpus/pm-frameworks/strategy/product-operating-model.md` — Cagan's surrounding system

## Anti-patterns

- **Vision-strategy collapse.** A single document called "the strategy" that's actually trying to be both vision and quarterly strategy. It's too vague to act on and too specific to outlast the quarter.
- **Roadmap-as-strategy.** Treating the feature roadmap as the strategy. A roadmap is an output of strategy, not a substitute for it. If asked "what's our strategy?" and the team points at the roadmap, the strategy doesn't exist.
