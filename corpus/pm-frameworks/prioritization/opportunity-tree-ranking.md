---
name: Opportunity Tree Ranking
domain: pm-frameworks
source_skill: product-management
entry_type: pattern
length_target: 400
related: [corpus/pm-frameworks/discovery/opportunity-solution-trees.md, corpus/pm-frameworks/thinkers/torres-teresa.md, corpus/pm-frameworks/discovery/continuous-discovery-habits.md]
---

# Opportunity Tree Ranking

## What it is

Using a Teresa Torres Opportunity Solution Tree as a prioritization device, not just a discovery artifact. The pattern:

1. The tree's structure (outcome → opportunities → solutions → assumption tests) makes the prioritization layer-explicit.
2. **At the opportunity layer**, rank opportunities by importance to the outcome and confidence in their existence. Choose one to focus on (Torres' "limit WIP" principle).
3. **At the solution layer**, generate multiple solutions for the chosen opportunity and rank them — but the choice is "compare and contrast among solutions for this opportunity," not "should we build this solution at all."
4. **At the assumption-test layer**, rank tests by riskiness reduced per dollar spent. Test the most-uncertain assumption first.

The pattern shifts prioritization from feature-list ranking to multi-layer decision-tree pruning.

## Why it matters

A flat feature-list prioritization ranks apples against oranges — different features address different problems and aren't directly comparable. Tree-based ranking forces same-layer comparisons: opportunities only ranked against opportunities; solutions only ranked among solutions for a chosen opportunity. Comparability becomes structural, not vibes-based.

It also makes the conversation traceable. When leadership asks "why this feature?" the answer chain is: "It's the highest-confidence solution for this opportunity, which is the highest-importance opportunity for this outcome."

## How to apply

- **Build the tree** through continuous discovery (see `opportunity-solution-trees.md`).
- **At each layer, rank explicitly.** Opportunities by importance + confidence; solutions by desirability + viability + feasibility + usability; assumption tests by risk-per-dollar.
- **Prune ruthlessly.** Lower-ranked opportunities aren't "later" — they're parked until the focus opportunity is resolved.
- **Re-rank when discovery surfaces new evidence.** New customer interviews shift importance scores; failed assumption tests prune branches.

## Examples

1. **Suzy: opportunity-layer prioritization.** Outcome: "increase weekly active analysts." Five opportunities surfaced; opportunity #2 ("analysts can't tell which study to run") rated highest (mentioned by 14 of 20 interviewees). Three solutions ranked at the next layer; the AI-recommendation solution chosen for desirability testing.
2. **Anti-pattern.** A team building five solutions across five opportunities simultaneously. Nothing converges; the tree has no focus; discovery produces opinions, not learning.

## Related entries

- `corpus/pm-frameworks/discovery/opportunity-solution-trees.md` — the tree itself
- `corpus/pm-frameworks/thinkers/torres-teresa.md` — Torres' broader practice
- `corpus/pm-frameworks/discovery/continuous-discovery-habits.md` — the cadence that updates the tree

## Anti-patterns

- **Cross-layer comparison.** Ranking solutions for opportunity A against solutions for opportunity B. The comparison is incoherent; you're choosing between different problems disguised as choosing between solutions.
- **Frozen tree.** Treating the tree as a planning artifact, not a working document. Without continuous updates, the prioritization staleness compounds.
