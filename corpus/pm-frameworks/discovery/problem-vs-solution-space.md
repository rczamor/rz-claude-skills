---
name: Problem Space vs Solution Space
domain: pm-frameworks
source_skill: product-management
entry_type: concept
length_target: 500
related: [corpus/pm-frameworks/discovery/opportunity-solution-trees.md, corpus/pm-frameworks/discovery/jobs-to-be-done.md, corpus/pm-frameworks/thinkers/doshi-shreyas.md, corpus/pm-frameworks/discovery/customer-development.md]
---

# Problem Space vs Solution Space

## What it is

A foundational distinction in product discovery: the **problem space** is the world of customer needs, pains, jobs to be done, and underserved outcomes. The **solution space** is the world of features, products, and implementations. They are disjoint domains.

A customer problem ("I can't tell which study to run when stakeholders ask for 'consumer perspective'") lives in problem space. Any number of solutions could address it (recommendations, templates, an analyst training program, a stakeholder briefing tool). The solution space is open until a problem is well-understood; the problem space is closed by customer reality.

The discipline: discovery operates in problem space. Move to solution space only after the problem space is sufficiently mapped.

## Why it matters

Most product teams jump to solution space immediately and never come back. The roadmap is a list of features; the OKRs are feature-shipped counts; the PRDs describe interfaces. None of those artifacts contain a customer problem. The result is the build trap: a roadmap of solutions disconnected from any specific problem.

The cost is asymmetric. A wrong solution to a real problem can be replaced. A correct solution to a phantom problem cannot — there's no problem for it to map to. Most "the feature shipped but nobody used it" outcomes are phantom-problem failures.

For AI products, the temptation is sharper. The model can build solutions in minutes. So the constraint moves from build capacity to problem clarity. Without disciplined problem-space work, AI teams ship a stream of solutions that don't attach to anything.

## How to apply

- **Phrase opportunities in problem-space language.** "Customers can't ___" or "When ___ happens, customers ___." Never "Customers need a feature for ___."
- **Apply the noun test.** If the opportunity contains a feature noun (dashboard, panel, recommendation engine), it has slipped into solution space. Rewrite it.
- **Generate multiple solutions per problem.** If you can name only one solution, the problem isn't understood. Diversity in solutions is a marker of problem clarity.
- **Defer solution discussion** during interviews. When customers propose solutions ("you should add X"), ask what would happen if X existed and what they're working around now.

## Examples

1. **Suzy: Solution space slip.** "Build a results-summary panel" is a solution. The problem space version: "Analysts can't quickly tell whether a study's results will satisfy the original stakeholder question." Multiple solutions become visible: an automated summary, a stakeholder-question matcher, a confidence indicator on existing results, an analyst checklist.
2. **Office hours framing.** Riché's question "should I invest in a context-architecture white paper?" is solution-space. The problem-space version: "Prospective design partners can't tell what makes my approach to context different — what's my distinctiveness signal?" Now the white paper is one of several candidates (a benchmark study, a case study from Suzy, a podcast appearance).

## Related entries

- `corpus/pm-frameworks/discovery/opportunity-solution-trees.md` — OSTs operationalize the distinction
- `corpus/pm-frameworks/discovery/jobs-to-be-done.md` — JTBD is a problem-space discipline
- `corpus/pm-frameworks/thinkers/doshi-shreyas.md` — Doshi's bias-for-building is the symptom
- `corpus/pm-frameworks/discovery/customer-development.md` — Blank's problem interviews stay in problem space

## Anti-patterns

- **Solution disguised in problem language.** "Customers need better recommendations" is a solution wearing problem clothing. Ask: better than what? what does "better" mean here? — and the actual problem emerges.
- **Retrofitting problems to solutions.** Building first, then asking "what problem does this solve?" The problem statement that emerges is rationalization, not discovery.
