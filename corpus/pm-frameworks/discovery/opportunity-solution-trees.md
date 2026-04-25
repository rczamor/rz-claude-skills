---
name: Opportunity Solution Trees
domain: pm-frameworks
source_skill: product-management
entry_type: framework
length_target: 700
related: [corpus/pm-frameworks/discovery/continuous-discovery-habits.md, corpus/pm-frameworks/thinkers/torres-teresa.md, corpus/pm-frameworks/prioritization/opportunity-tree-ranking.md, corpus/pm-frameworks/discovery/problem-vs-solution-space.md]
---

# Opportunity Solution Trees

## What it is

Teresa Torres' visual discovery framework for connecting customer needs to solution bets. The structure is a four-layer tree:

1. **Desired outcome** at the root — the product outcome the team is accountable for.
2. **Opportunity space** in the middle — customer needs, pain points, and desires surfaced through interviews. Framed as customer language, not internal solutions.
3. **Solutions** below opportunities — multiple bets per opportunity.
4. **Assumption tests** at the leaves — small experiments designed to invalidate the riskiest desirability, viability, feasibility, or usability assumption behind each solution.

Built and updated continuously as a product trio (PM, designer, engineer) interviews customers and runs assumption tests.

## Why it matters

Most teams jump from outcome straight to solutions, skipping the opportunity layer. That's the build trap encoded as a tree. Forcing every solution to attach to a named customer opportunity (and every opportunity to a measurable outcome) produces a defensible chain of reasoning: leadership can see why this solution, why this opportunity, why this outcome. It also enables the "compare and contrast" mindset Torres prescribes — instead of asking "should we build this?" you ask "of these solutions for this opportunity, which is most promising?" From Torres, *Continuous Discovery Habits* (2021).

For AI products specifically: opportunities don't change as fast as model capabilities. Anchoring discovery on durable customer needs prevents the model-of-the-month roadmap thrash.

## How to apply

1. **Anchor on a product outcome.** Not a business outcome (revenue, retention) but a behavioral outcome the team can directly influence (e.g. "increase weekly active analysts running insights queries").
2. **Populate the opportunity space from interviews.** Each opportunity is a verbatim or near-verbatim customer statement of need. Group, deduplicate, and structure into parent/child opportunities.
3. **Pick one opportunity to focus on.** Limit WIP. Working on five opportunities at once means none get tested.
4. **Generate 3–5 candidate solutions** per opportunity. Diverge before converging — explicitly include solutions you don't favor to avoid confirmation bias.
5. **Identify the riskiest assumption** for each solution: desirability (will customers want it?), viability (is it good for the business?), feasibility (can we build it?), usability (can users figure it out?).
6. **Design assumption tests** that could invalidate the riskiest assumption fast and cheap. A landing-page test, a Wizard-of-Oz prototype, an unmoderated study.

## Examples

1. **Suzy Decision Engine.** Outcome: "increase Insights pillar weekly active enterprise users." Opportunity: "Analysts can't tell which study to run first when stakeholders ask for 'consumer perspective.'" Solutions: smart study templates, an AI-recommended-study queue, a stakeholder briefing generator. Riskiest assumption on the AI queue: desirability — would analysts trust AI study recommendations? Test: prototype five recommendations against historical study selections and review with five senior analysts.
2. **Helm Labs ICP discovery.** Outcome: "convert pre-launch pipeline into design partners." Opportunity: "PE-backed CFOs say their close process is opaque to the board but can't define what 'transparent' means." Three solutions, each with a desirability test designed to run inside a 30-minute discovery call.

## Related entries

- `corpus/pm-frameworks/discovery/continuous-discovery-habits.md` — the cadence that keeps OSTs alive
- `corpus/pm-frameworks/thinkers/torres-teresa.md` — Torres' broader practice
- `corpus/pm-frameworks/prioritization/opportunity-tree-ranking.md` — using OSTs as a prioritization device
- `corpus/pm-frameworks/discovery/problem-vs-solution-space.md` — the conceptual move OSTs operationalize
- `corpus/pm-frameworks/ai-product-pm/evals-framework.md` — assumption tests in non-deterministic systems

## Anti-patterns

- **Solution dressed as an opportunity.** "Users need a recommendations panel" is a solution. The opportunity is whatever pain a recommendations panel addresses. If the opportunity contains a feature noun, rewrite it.
- **Tree-as-roadmap-decoration.** Building the tree once for a planning offsite, then never updating it. OSTs are working artifacts, not deliverables; if they aren't redrawn weekly they have stopped functioning.
