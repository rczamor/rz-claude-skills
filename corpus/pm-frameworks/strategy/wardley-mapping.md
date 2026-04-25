---
name: Wardley Mapping
domain: pm-frameworks
source_skill: research
entry_type: framework
length_target: 700
related: [corpus/pm-frameworks/thinkers/wardley-simon.md, corpus/pm-frameworks/strategy/cynefin-framework.md, corpus/pm-frameworks/strategy/seven-powers.md, corpus/pm-frameworks/strategy/blue-ocean.md]
---

# Wardley Mapping

## What it is

Simon Wardley's strategic mapping technique developed at Canonical and refined through his "Wardley Maps" series. A two-dimensional map of a value chain:

- **Y-axis: Visibility.** User-facing components at the top; underlying infrastructure at the bottom. Visibility traces what the user actually experiences vs. what's invisible to them.
- **X-axis: Evolution.** Four stages — **Genesis** (novel, custom-built), **Custom-Built** (one-off, project-based), **Product** (standardized, often commodified), **Commodity/Utility** (undifferentiated, utility-like). Components move left-to-right over time as they mature.

Each component sits at a specific position. The map then shows: (a) what the value chain looks like today, (b) where each component is in its evolution, and (c) what predictable moves (yours, competitors', the market's) follow.

From Wardley's *Wardley Maps* (Medium series, 2018; Creative Commons book).

## Why it matters

Most strategy is positional ("we're #2 in the market") or directional ("we're going to win on speed"). Wardley Mapping is **situational** — it tells you what kind of move is appropriate given where you sit. A startup competing on Genesis innovation should not behave like an incumbent commoditizing a Product. The wrong move at the wrong stage destroys value even if executed perfectly.

The framework's distinctive contributions:
- **Climatic patterns:** predictable evolution (commodities don't go back to genesis; visibility flows downward over time).
- **Doctrines:** universally good practices (focus on user needs; use appropriate methods).
- **Gameplay:** competitive moves that depend on the map (counter-positioning, exploiting inertia, weaponizing open source).

For AI products, Wardley Mapping is exceptionally clarifying because AI's value chain is mid-evolution. Foundation models are commoditizing rapidly (moving right). Application-layer differentiation is in early Product stage. Context architecture and evals are in Custom-Built / Genesis. Knowing where each component sits determines whether to build, buy, or partner — and what your defensibility actually is.

## How to apply

1. **Anchor on user need.** What is the user trying to accomplish? Place the user at the top.
2. **Map the value chain downward.** What components does the user experience? What components support those? Iterate until you reach commodity infrastructure (electricity, IP, etc.).
3. **Position each component on the evolution axis.** Genesis (novel, custom)? Custom-built (one-off)? Product (standardized)? Commodity (undifferentiated)?
4. **Identify movements.** Which components are about to evolve (move right)? Which competitive forces accelerate the movement?
5. **Choose gameplay.** Build on emerging utilities; counter-position against incumbents stuck in older stages; exploit competitor inertia.
6. **Pair with doctrine.** Even with great mapping, focus on user needs and use appropriate methods (agile for genesis, lean for product, six-sigma for commodity).

## Examples

1. **Suzy Decision Engine map.** User need: defensible answer to a stakeholder question. Top: study results (Product — standardized format). Below: methodology recommendation (Custom-Built moving toward Product). Below that: study templates (Product). Below: model-based recommendation engine (Genesis/Custom-Built). Below: foundation models (Commodity rapidly). Below: compute (Commodity utility). The map reveals that defensibility lives in the Custom-Built / Genesis layers (methodology + recommendation engine), not in the model itself. Strategy: deepen the Custom-Built layer; treat foundation models as utilities; don't try to differentiate on the commodity.
2. **Helm Labs map.** User need: explain variance to the board. Top: variance narrative (Genesis — nobody does this well). Below: GL data integration (Product). Below: ledger systems (Commodity for most CFOs). The Genesis position at the top is the differentiation; the strategic move is to stay in Genesis longer than competitors by deepening proprietary methodology.

## Related entries

- `corpus/pm-frameworks/thinkers/wardley-simon.md` — Wardley's broader work
- `corpus/pm-frameworks/strategy/cynefin-framework.md` — paired situational-strategy framework (Snowden)
- `corpus/pm-frameworks/strategy/seven-powers.md` — Helmer's powers complement Wardley's evolution stages
- `corpus/pm-frameworks/strategy/blue-ocean.md` — blue oceans often live in Genesis or early Custom-Built
- `corpus/pm-frameworks/ai-product-pm/context-architecture-as-strategy.md` — context architecture's Wardley position

## Anti-patterns

- **Map-as-static-artifact.** Drawing the map once for an offsite, framing it on a wall, never updating. The map's value comes from situational use — it should be redrawn as the value chain evolves.
- **Wrong-stage-method.** Applying agile to a commodity (over-engineered) or six-sigma to a genesis effort (premature optimization). Wardley's doctrine of "appropriate method" is half the value of the map; ignoring it produces good maps with bad execution.
