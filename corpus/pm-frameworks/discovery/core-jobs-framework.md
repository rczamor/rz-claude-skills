---
name: Core Jobs Framework (Jobs-Pains-Gains)
domain: pm-frameworks
source_skill: research
entry_type: framework
length_target: 500
related: [corpus/pm-frameworks/discovery/jobs-to-be-done.md, corpus/pm-frameworks/thinkers/christensen-clayton.md, corpus/pm-frameworks/discovery/empathy-mapping.md]
---

# Core Jobs Framework (Jobs-Pains-Gains)

## What it is

An operational variant of JTBD popularized by Intercom and Strategyzer (Osterwalder's Value Proposition Canvas) that decomposes a customer's job into three components:

- **Jobs:** what the customer is trying to get done (functional, emotional, social).
- **Pains:** undesired outcomes, obstacles, and risks the customer encounters while doing the job.
- **Gains:** desired outcomes, benefits, and aspirations the customer wants from doing the job successfully.

A product earns its hire by being a **pain reliever** for specific pains and a **gain creator** for specific gains. This produces a value-proposition fit map: each pain pairs with a relief mechanism; each gain pairs with a creation mechanism.

From Osterwalder, Pigneur, Bernarda, Smith, *Value Proposition Design* (2014), and Intercom's "Jobs to be Done" handbook (2016).

## Why it matters

Pure JTBD describes the job; jobs-pains-gains describes the experience of doing the job. That second layer is where most product opportunities live. Pains tell you what to remove; gains tell you what to amplify. The framework also produces a clean test for value proposition: every claim in your messaging should map to a specific pain you relieve or gain you create. If a claim doesn't map, it's noise.

For AI products, jobs-pains-gains is especially clarifying because AI relieves a specific class of pains (cognitive load, time-on-task, expertise gaps) and creates a specific class of gains (speed, scale, accessibility). Knowing which pain or gain you're targeting prevents AI feature drift.

## How to apply

1. **List the customer's jobs** — functional, emotional, social. Limit to 3–5 per persona; more dilutes focus.
2. **For each job, list pains and gains.** Pains: what goes wrong, what slows them down, what worries them, what they avoid. Gains: what success looks like, what they aspire to, what would surprise them positively.
3. **Rank by importance.** Not all pains/gains are equal. Underserved high-importance pains/gains are the opportunity space.
4. **Map your product's pain relievers and gain creators.** Each feature must map to at least one pain or gain. Features without mapping are candidates for deprecation.
5. **Audit messaging.** Every value-proposition claim should be a stated pain reliever or gain creator. Claims without mapping are slogans.

## Examples

1. **Suzy Insights.** Job: "answer a stakeholder question with consumer evidence in time." Pains: stakeholder asks vague questions; analyst guesses wrong methodology; results arrive after the meeting. Gains: confidence the answer is defensible; reusable templates; faster turnaround. AI-recommended studies are a pain reliever for the methodology pain, not a gain creator — that distinction shapes the messaging.
2. **Helm Labs.** Job: "give the board confidence in close numbers." Pains: explanations of variances are ad hoc, audit asks recur, board asks the same question every quarter. Gains: predictable narratives, faster close, reusable analyses. The product is positioned around the recurring-question pain, which CFOs feel viscerally.

## Related entries

- `corpus/pm-frameworks/discovery/jobs-to-be-done.md` — the parent framework
- `corpus/pm-frameworks/thinkers/christensen-clayton.md` — JTBD origin
- `corpus/pm-frameworks/discovery/empathy-mapping.md` — adjacent customer-research artifact

## Anti-patterns

- **Pain inflation.** Listing every annoyance as a "pain" until the list has 40 items, none of which are urgent enough to drive a purchase. Rank ruthlessly.
- **Confusing features with gain creators.** "Dashboard view" isn't a gain creator; the gain it creates ("see all my numbers in one place without exporting") is.
