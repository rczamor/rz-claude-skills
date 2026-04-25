---
name: Pre-Mortems
domain: pm-frameworks
source_skill: product-management
entry_type: framework
length_target: 600
related: [corpus/pm-frameworks/thinkers/doshi-shreyas.md, corpus/pm-frameworks/prioritization/lno-framework.md, corpus/pm-frameworks/strategy/empowered-vs-feature-teams.md]
---

# Pre-Mortems

## What it is

A structured exercise developed by psychologist Gary Klein and adopted by Shreyas Doshi as core PM practice: before a major initiative starts, the team imagines that it has already failed — completely, publicly, embarrassingly — and lists the reasons why. Each reason becomes a candidate risk to mitigate before launch.

The framing is critical. Instead of asking "what could go wrong?" (which produces general anxiety), the pre-mortem asks "imagine it's six months from now and this initiative was a disaster — what happened?" The retrospective frame unlocks specific, vivid failure scenarios the team's optimism would otherwise suppress.

Doshi prescribes pre-mortems before PRD finalization, major launches, and architectural decisions.

## Why it matters

Initiatives fail in predictable ways: stakeholder misalignment, key dependency breaks, customer-need mis-specification, technical debt overwhelming velocity, competitive response, regulatory blocker, key-person attrition. Most of these are knowable in advance — but only if you ask. Optimism bias and the planning fallacy systematically blind teams to the most likely failure modes.

Klein's research found that pre-mortems improve the team's ability to identify reasons for outcomes by 30%. Doshi's adaptation pairs the exercise with Doshi's seven biases of product teams — pre-mortems are a structural counterweight to bias-for-building, confirmation bias, and pro-innovation bias.

For AI products specifically, pre-mortems catch the failure modes that AI introduces: model regressions, eval drift, prompt-injection vulnerabilities, context drift, hallucination in high-stakes contexts, inference-cost blow-ups. These are easy to overlook in the excitement of capability; the pre-mortem forces them onto the page.

## How to apply

1. **Time-box 30–45 minutes** with the cross-functional team (PM, design, engineering, plus any critical stakeholders).
2. **Set the failure premise.** "It's [date 6 months from now]. We launched [initiative]. It was a disaster — the worst-case scenario the executive team feared. What happened?"
3. **Silent generation first** (5–10 minutes). Each person writes failure reasons individually. Avoid groupthink in the framing.
4. **Share, cluster, deduplicate.** Group similar reasons. Identify the top 5–8 distinct failure modes.
5. **Score by likelihood and severity.** Likelihood × severity gives a risk rank.
6. **Develop mitigations** for the top 3–5 risks. Each mitigation has an owner and a pre-launch deadline.
7. **Document and revisit.** The pre-mortem document lives in the PRD. Review it 30 and 60 days post-launch — what risks materialized? What did the exercise miss?

## Examples

1. **Suzy Decision Engine launch pre-mortem.** Team imagined launch failure six months out. Top failure modes: (a) enterprise customers couldn't connect existing study templates to new AI-recommended studies — adoption stalled at the recommendation layer; (b) compliance team blocked data flow into eval pipelines two weeks before launch. Mitigations: build a template-import bridge in week 1, run pre-launch compliance review at week 4. Both materialized; both were absorbable because they were anticipated.
2. **Helm Labs pre-launch pre-mortem.** Failure scenarios surfaced: (a) PE-backed CFOs reject the close-software pitch because their portfolio companies' systems are too heterogeneous; (b) audit firm becomes the actual buyer, not the CFO. Mitigation on (a): pre-validate with five CFOs before launch; on (b): explicit auditor-relationship strategy. The auditor-pivot scenario didn't materialize but the validation work strengthened the close-rate.

## Related entries

- `corpus/pm-frameworks/thinkers/doshi-shreyas.md` — Doshi's broader practice
- `corpus/pm-frameworks/prioritization/lno-framework.md` — paired Doshi tool
- `corpus/pm-frameworks/strategy/empowered-vs-feature-teams.md` — pre-mortems require an empowered team to execute on findings

## Anti-patterns

- **Generic failure list.** "Engineering took longer than expected" appears on every pre-mortem. Push for specificity: which engineering decision, why, what's the leading indicator? Generic risks aren't actionable.
- **Pre-mortem as theater.** Running the exercise to satisfy a process requirement, then ignoring the findings. The artifact must drive concrete mitigations with owners and deadlines or it's overhead.
