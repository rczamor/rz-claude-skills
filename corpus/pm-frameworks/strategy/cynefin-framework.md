---
name: Cynefin Framework
domain: pm-frameworks
source_skill: research
entry_type: framework
length_target: 700
related: [corpus/pm-frameworks/thinkers/snowden-dave.md, corpus/pm-frameworks/strategy/wardley-mapping.md, corpus/pm-frameworks/lifecycle/lean-startup.md, corpus/pm-frameworks/prioritization/pre-mortems.md]
---

# Cynefin Framework

## What it is

Dave Snowden's sense-making framework (originally published in *Harvard Business Review*, 2007: "A Leader's Framework for Decision Making") for matching the type of problem to the type of decision-making approach. Five domains:

1. **Clear (formerly Simple/Obvious).** Cause-and-effect known to all. Best practices apply. Sense → categorize → respond. (Routine ops; well-understood compliance.)
2. **Complicated.** Cause-and-effect knowable through analysis. Good practices apply. Sense → analyze → respond. (Engineering systems; financial models.)
3. **Complex.** Cause-and-effect only knowable in retrospect. Emergent practices. Probe → sense → respond. (Markets, customer behavior, organizational change.)
4. **Chaotic.** No discernible cause-and-effect. Novel practices required. Act → sense → respond. (Crises, emergencies.)
5. **Disorder.** You don't know which domain you're in. The most dangerous state — usually you act according to your default domain (often Clear or Complicated) regardless of actual fit.

The framework is **descriptive of the problem**, not prescriptive of the solution. Different domains require different toolkits.

## Why it matters

Most strategic mistakes come from treating a complex problem as if it were complicated, or vice versa. Treating market discovery as complicated (research it thoroughly, then execute) misses that markets are complex (you must probe to learn). Treating an engineering system as complex (probe first) wastes time when analysis would suffice.

For PMs, Cynefin clarifies which kind of move applies:
- **Discovery work is Complex.** You can't analyze your way to PMF; you probe (build minimum experiments), sense (read signals), respond (iterate).
- **Delivery work is often Complicated.** Engineering execution against a known specification benefits from analysis.
- **Compliance and table-stakes are Clear.** Apply the best practice; don't over-think.
- **Crises (production outage, security breach) are Chaotic.** Act first, analyze later.

For AI products, Cynefin is especially useful because AI products span multiple domains simultaneously. Model behavior is Complex (emergent, requires probing — this is why evals matter). Inference infrastructure is Complicated (analyzable). Safety guardrails are Clear (apply the best practice). Hallucination crises are Chaotic. A single AI product team needs all four toolkits.

## How to apply

1. **Diagnose the domain** before choosing the approach. Ask: is cause-and-effect known? Knowable? Emergent? Absent?
2. **Match toolkit to domain:**
   - Clear: SOPs, checklists, automation.
   - Complicated: experts, analysis, modeling.
   - Complex: experiments, MVPs, probes; multiple parallel bets.
   - Chaotic: command-and-control short-term action; transition to Complex once stability returns.
3. **Watch for misclassification.** The most common error is treating Complex problems as Complicated. The symptom: extensive analysis followed by confident execution that produces unexpected results.
4. **Use Disorder as a flag.** If the team can't agree which domain a problem is in, that's diagnostic — work on the framing before acting.

## Examples

1. **Suzy: AI-recommendation rollout.** The recommendation engine itself is Complex (emergent behavior; requires probing via evals and A/B tests). The deployment infrastructure is Complicated (analyzable). The audit-trail compliance is Clear (apply the SOC 2 best practice). When a model regression causes hallucinated study recommendations in production, that's Chaotic — act first (rollback), then transition to Complex (probe what went wrong).
2. **Helm Labs: PE-backed CFO discovery.** Treating CFO discovery as Complicated (run a thorough analysis, then sell) failed in early conversations. Reframing as Complex (run weekly probes, sense the response, adjust the next probe) produced the $3.25M pipeline. The framework didn't tell Riché what to build; it told him which decision-making mode to use.

## Related entries

- `corpus/pm-frameworks/thinkers/snowden-dave.md` — Snowden's broader work
- `corpus/pm-frameworks/strategy/wardley-mapping.md` — paired situational-strategy framework
- `corpus/pm-frameworks/lifecycle/lean-startup.md` — Lean Startup is a Complex-domain method
- `corpus/pm-frameworks/prioritization/pre-mortems.md` — pre-mortems are a Complex-domain probe

## Anti-patterns

- **Complicated-treated-as-complex.** Endless probing on a problem that could have been analyzed (e.g. running A/B tests on UI choices that have well-established design heuristics). Wastes capacity.
- **Complex-treated-as-complicated.** Building a 12-month roadmap based on initial customer-discovery analysis, then executing without probes. By month three the analysis is stale; by month six the product is wrong.
