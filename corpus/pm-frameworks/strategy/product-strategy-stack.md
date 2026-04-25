---
name: Product Strategy Stack (Rekhi)
domain: pm-frameworks
source_skill: product-management
entry_type: framework
length_target: 500
related: [corpus/pm-frameworks/thinkers/rekhi-sachin.md, corpus/pm-frameworks/strategy/product-vision-strategy.md, corpus/pm-frameworks/metrics/okrs.md]
---

# Product Strategy Stack (Rekhi)

## What it is

Sachin Rekhi's hierarchical model for company-to-team strategic alignment. Five layers, each tracing to the layer above:

1. **Company Mission.** Why the company exists (years/decades).
2. **Company Strategy.** How the company will win in its market over the medium term.
3. **Product Strategy.** Which products and product capabilities advance the company strategy.
4. **Product Roadmap.** The specific initiatives the product strategy implies, sequenced.
5. **Product Goals.** Quarterly/monthly outcomes that the roadmap is intended to produce, owned by teams.

Each layer answers a "why" question for the layer below it. The discipline: every product goal traces upward through the stack to the company mission.

From Rekhi's writing on Notejoy and his Reforge teaching.

## Why it matters

Most companies have all five layers but they don't connect. The mission is on the website; the strategy is in a board deck nobody references; the product strategy is whatever the head of product believes this month; the roadmap is shaped by stakeholder demands; the team goals are output metrics disconnected from any of the above. The stack collapses into "ship the things on the list" with no traceability.

Rekhi's stack is the antidote: every team goal must answer "how does this advance the product strategy, which advances the company strategy, which advances the mission?" If the chain breaks, you've found the disconnect.

For AI products, the stack matters because AI shifts the layers at different speeds. Mission stays stable; company strategy may shift annually; product strategy may shift quarterly as model capabilities evolve; roadmap shifts monthly. Without the stack, the team can't tell which shift is responding to which signal.

## How to apply

1. **Articulate each layer in writing.** Mission and company strategy from leadership; product strategy from the head of product; roadmap and goals from the team.
2. **Audit the connections.** For each product goal, trace upward: which roadmap initiative does it support? Which product strategy bet does that roadmap serve? Which company strategy does that bet advance? Which mission does that strategy realize? Breaks in the chain are the diagnosis.
3. **Update on the right cadence per layer.** Mission rarely; company strategy annually; product strategy quarterly; roadmap monthly; goals quarterly with monthly check-ins.
4. **Use it for stakeholder conversations.** When stakeholders push features, ask: which strategy bet does this serve? If they can't answer, the request is an output without a why.

## Examples

1. **Suzy stack.** Mission: every consumer-facing decision grounded in real-time consumer truth. Company strategy: enterprise platform for ongoing consumer intelligence. Product strategy (Q3): Insights pillar deepens analyst confidence as the wedge. Roadmap: AI-recommended studies, methodology coaching, briefing summaries. Goals: weekly active analysts, study completion rate, stakeholder satisfaction.
2. **Helm Labs stack.** Mission: PE portfolio CFOs have audit-grade close visibility on demand. Strategy: variance-explanation automation as the entry product. Product strategy: instant board-narrative generation. Roadmap: variance pipeline, narrative templates, audit-trail integration. Goals: pilot conversion rate, narrative-generation accuracy, time-to-board-pack.

## Related entries

- `corpus/pm-frameworks/thinkers/rekhi-sachin.md` — Rekhi's broader practice
- `corpus/pm-frameworks/strategy/product-vision-strategy.md` — Cagan's vision/strategy compatible with the stack
- `corpus/pm-frameworks/metrics/okrs.md` — OKRs are the typical instrument for the goals layer

## Anti-patterns

- **Stack-as-decoration.** All five layers exist as artifacts but the connections are missing. The chain doesn't trace; the goals don't reflect the strategy; the roadmap doesn't reflect the goals.
- **Skipping the product-strategy layer.** Many companies have mission, company strategy, roadmap, and goals — but no product strategy in between. The roadmap then becomes politically negotiated rather than strategically derived.
