---
name: Proxy Skepticism (Bezos Day 1)
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: concept
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/02-paranoid-scanning.md, corpus/evaluation-frameworks/step-0/premise-challenge.md, corpus/evaluation-frameworks/review-sections/08-observability.md]
---

# Proxy Skepticism (Bezos Day 1)

## What it is
Are our metrics still serving users, or have they become self-referential? Bezos's "Day 1 vs. Day 2" letter named the disease: process becomes a proxy for outcome, metrics become a proxy for the thing they once measured, and the company optimizes the proxy at the expense of the underlying value. Proxy skepticism is the discipline of asking, on every plan and every metric, "is this the thing, or is it a stand-in for the thing that we've stopped checking?"

## Why it matters
Plans love proxies. They quantify, they show progress, they fit on a slide. But a plan that succeeds against its proxy and fails against the real outcome is a worse plan than one that fails the proxy and asks the right next question. The 10x CEO treats every metric as guilty until it can show it still tracks the real thing.

## How to apply
1. For every metric in the plan, ask: "Could we hit this metric in a way that hurts the user / business?" If yes — flag the metric as proxy-vulnerable.
2. Ask: "When was the last time we checked that this metric still correlates with the outcome we care about?" If "never" or "long ago" — invest in the validation, not just the metric.
3. Look for process worship: meetings, reviews, signoffs that exist to demonstrate process rather than to improve outcome. Subtract them.
4. Pair every quantitative target with a qualitative check: read the comments, watch the session, talk to the user. Numbers are summaries; the truth is in the source.

## Examples
1. **DAU as success metric**: but DAU is up because of an in-app prompt that nudges users to open the app daily for no reason. Proxy is hit; user value is unchanged or worse.
2. **PRs merged per week**: but engineers fragment work into tiny PRs to game the metric. Throughput on paper, throughput in reality flat.
3. **Onboarding completion rate**: but completion is up because a step was removed that was actually catching invalid signups. Now activation is up; retention is down.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/02-paranoid-scanning.md` — paranoid scanning is what catches proxy drift early
- `corpus/evaluation-frameworks/step-0/premise-challenge.md` — premise challenge directly asks the proxy question
- `corpus/evaluation-frameworks/review-sections/08-observability.md` — Section 8 picks the metrics that need this scrutiny

## Anti-patterns
- Defending a metric because "we've always tracked it." History is not validity.
- Adding a second metric to compensate for a flawed first metric. Two flawed metrics do not average to truth.
