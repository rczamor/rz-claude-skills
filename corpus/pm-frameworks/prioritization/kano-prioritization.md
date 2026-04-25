---
name: Kano Prioritization
domain: pm-frameworks
source_skill: research
entry_type: framework
length_target: 500
related: [corpus/pm-frameworks/discovery/kano-model.md, corpus/pm-frameworks/thinkers/kano-noriaki.md, corpus/pm-frameworks/prioritization/moscow.md]
---

# Kano Prioritization

## What it is

Using Noriaki Kano's satisfaction-curve categories to sequence a roadmap. After classifying features into Must-be / One-dimensional / Attractive / Indifferent / Reverse via Kano survey, the prioritization rule is:

1. **Must-bes first.** Their absence loses the deal; their presence doesn't differentiate.
2. **One-dimensionals second.** Linear satisfaction-to-investment relationship; this is where competitive position is built.
3. **Attractive (delighters) third.** Asymmetric upside; differentiation lives here.
4. **Indifferent and Reverse: don't build.** Indifferent features waste capacity; Reverse features actively harm.

The principle: you cannot win on delighters if you've failed on must-bes. Sequencing matters more than feature count.

## Why it matters

Most teams chase delighters because they're more interesting and demo well. But a product with three delighters and one missing must-be loses every deal. Kano-based prioritization forces the unsexy table-stakes work first, then the differentiation work, in that order. It's the discipline-imposed-by-rubric that gut prioritization rarely achieves.

The framework is also temporally explicit: Kano categories drift (today's delighter is tomorrow's must-be). Re-running Kano surveys quarterly keeps the prioritization current as the category matures.

For AI products, the drift is fast. AI summarization was a delighter in early 2023 and a must-be by late 2024. Without Kano-based re-prioritization, teams spend on yesterday's differentiators while today's must-bes go unbuilt.

## How to apply

1. **Run a Kano survey** on candidate features (paired functional/dysfunctional questions, 100+ respondents from target customer set).
2. **Tabulate categories.** Each feature lands in M / O / A / I / R.
3. **Sequence:** M → O → A. Drop I and R from the roadmap.
4. **Within each category, rank by importance/satisfaction gap.** A high-importance, low-satisfaction Must-be is the most urgent feature on the roadmap.
5. **Re-run quarterly** for evolving categories. A feature that was Attractive last year may now be Must-be.

## Examples

1. **Suzy Q2 roadmap.** Kano survey of 60 enterprise analysts: SSO scored Must-be (absent = no deal); audit trail scored One-dimensional (more depth = more satisfaction); AI-recommended studies scored Attractive (delighter). Roadmap sequence: SSO ship gate first (without it, Q2 deals stall), then audit-trail enhancements, then AI recommendations as competitive differentiation.
2. **Cargo-cult Kano.** A team running a Kano survey once, then permanently treating AI-summarization as a delighter even after every competitor shipped it. The category drifted to Must-be; the team kept investing in marginal delight gains while losing deals on the actual must-be (compliance-grade summaries).

## Related entries

- `corpus/pm-frameworks/discovery/kano-model.md` — the categorization framework itself
- `corpus/pm-frameworks/thinkers/kano-noriaki.md` — Kano's original work
- `corpus/pm-frameworks/prioritization/moscow.md` — Must-bes map to MoSCoW Musts

## Anti-patterns

- **Delighter-first sequencing.** Chasing differentiation features while must-bes go unfilled. The product loses deals before the delighters can be experienced.
- **Static categorization.** Treating Kano category as permanent. The drift is the second-most useful signal the framework gives you; ignoring it makes the prioritization stale.
