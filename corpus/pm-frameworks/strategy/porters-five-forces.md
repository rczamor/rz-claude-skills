---
name: Porter's Five Forces
domain: pm-frameworks
source_skill: research
entry_type: framework
length_target: 600
related: [corpus/pm-frameworks/thinkers/porter-michael.md, corpus/pm-frameworks/strategy/seven-powers.md, corpus/pm-frameworks/strategy/competitive-analysis.md, corpus/pm-frameworks/strategy/blue-ocean.md]
---

# Porter's Five Forces

## What it is

Michael Porter's industry-structure analysis framework (Harvard Business Review, 1979; *Competitive Strategy*, 1980). An industry's profit potential is determined by five competitive forces:

1. **Threat of new entrants.** How easy is it for new firms to enter? Barriers (capital, regulation, network effects, brand) reduce the threat.
2. **Bargaining power of suppliers.** Concentrated suppliers with unique inputs extract more margin. Fragmented commodity suppliers have low power.
3. **Bargaining power of buyers.** Concentrated buyers (large customers) or commodity products give buyers leverage.
4. **Threat of substitutes.** Different products that satisfy the same need. Coffee shops compete with energy drinks for the "afternoon focus" job; their substitution threat caps coffee-shop pricing.
5. **Industry rivalry.** Intensity of competition among existing firms. High rivalry compresses margins.

The five forces shape the **industry's** profit potential. A firm's strategy then aims to find a defensible position within (or to reshape) those forces.

## Why it matters

Porter's framework is the bedrock of strategic analysis. It's been criticized (slow-moving, less applicable to platform businesses) and supplemented (Helmer's 7 Powers, Blue Ocean) — but never replaced. The five forces remain the standard lens for "is this an attractive industry to compete in?"

For PMs, Porter's contribution is the recognition that **industry structure** matters at least as much as company execution. A great team in a structurally bad industry (low entry barriers, concentrated buyers, many substitutes, intense rivalry) will struggle. A mediocre team in a structurally good industry (high barriers, fragmented buyers, no substitutes, low rivalry) will print money. Strategy is partly about industry selection.

For AI products, the five forces analysis is unsettling: AI applications have low entry barriers (foundation models are accessible), buyers are increasingly sophisticated, substitutes proliferate (every category has 20 AI startups), and rivalry is intense. The industry structure is unfavorable to most participants. The implication: most AI startups must reshape the structure (network effects, switching costs, counter-positioning) or accept commodity returns.

## How to apply

1. **Define the industry boundary.** Too broad ("software") and the analysis is meaningless; too narrow ("AI-recommended studies for CPG analysts") and you miss substitutes.
2. **Score each force.** High / medium / low. Provide evidence — concentration ratios, switching costs, observed buyer behavior, substitute usage.
3. **Identify the dominant forces.** Usually one or two forces dominate the industry's economics. In SaaS, often buyer power and rivalry. In semiconductors, supplier power and entry barriers.
4. **Map your firm's position relative to the dominant forces.** Where do you have leverage? Where are you exposed?
5. **Strategy chooses one of three:**
   - **Cost leadership** within the industry structure.
   - **Differentiation** that mutes the dominant forces.
   - **Niche focus** that escapes the worst force exposure.

## Examples

1. **Suzy Decision Engine industry analysis.** Industry: enterprise consumer-intelligence platforms. Threat of entry: medium (capital to build platform, but tooling is improving). Buyer power: high (large enterprises consolidate spend). Substitutes: high (legacy survey tools, in-house research, consumer-research consultancies). Rivalry: medium-high. Strategy: differentiate via Insights pillar's defensibility (process power); avoid head-to-head price competition with legacy survey tools; target Fortune 1000 buyers where switching costs are highest.
2. **Helm Labs industry analysis.** Industry: PE-portfolio close-and-reporting software. Threat of entry: low (PE relationships are hard to replicate). Buyer power: medium (concentrated PE firms but many portfolio companies per fund). Substitutes: high (Excel, in-house spreadsheet templates, audit firm services). Rivalry: low (no AI-native incumbent yet). Strategy: niche focus on the close-narrative segment, exploit the structural opening before AI-native competitors arrive.

## Related entries

- `corpus/pm-frameworks/thinkers/porter-michael.md` — Porter's broader work
- `corpus/pm-frameworks/strategy/seven-powers.md` — Helmer's update to Porter
- `corpus/pm-frameworks/strategy/competitive-analysis.md` — operational competitor work
- `corpus/pm-frameworks/strategy/blue-ocean.md` — strategy of escaping force dominance

## Anti-patterns

- **Industry boundary fudging.** Drawing the industry boundary to make your firm look favorable. "Our industry" defined to exclude the largest substitutes is self-deception.
- **Static analysis.** Treating the five forces as fixed. Industries evolve; AI is reshaping force dynamics in real time. Re-analyze annually at minimum.
