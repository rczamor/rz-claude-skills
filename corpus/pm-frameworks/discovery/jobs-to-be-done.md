---
name: Jobs to Be Done
domain: pm-frameworks
source_skill: research
entry_type: framework
length_target: 700
related: [corpus/pm-frameworks/thinkers/christensen-clayton.md, corpus/pm-frameworks/discovery/core-jobs-framework.md, corpus/pm-frameworks/prioritization/jtbd-prioritization.md, corpus/pm-frameworks/discovery/problem-vs-solution-space.md]
---

# Jobs to Be Done

## What it is

A theory and method developed by Clayton Christensen and collaborators (Bob Moesta, Tony Ulwick, Alan Klement) that holds: customers don't buy products — they "hire" products to make progress on a job they're trying to get done in a specific situation. The job has functional, emotional, and social dimensions, all of which the chosen product must address better than alternatives, or the customer will "fire" it.

A canonical job statement form: **"When [situation], I want to [motivation], so I can [expected outcome]."**

From Christensen, Hall, Dillon, and Duncan, *Competing Against Luck* (2016). Tony Ulwick's *Outcome-Driven Innovation* (1990s onward) is the parallel, more quantitative tradition.

## Why it matters

JTBD reframes competition. Your competitor isn't the company with the similar feature set; it's whatever the customer is currently hiring for the same job — including non-consumption (doing nothing). Christensen's milkshake study is the canonical illustration: a fast-food milkshake competed not with other milkshakes but with bagels, bananas, and donuts as a "morning commute, one-handed, non-boring breakfast" hire.

For AI products, JTBD is especially powerful because users hire AI for jobs that older products couldn't address (synthesis, reasoning under ambiguity, content generation). The functional job often masks the emotional job: "help me draft this email" frequently means "remove my anxiety about how to start." Building only for the functional layer leaves the actual hire criterion unaddressed.

## How to apply

1. **Interview customers about a recent purchase or switch** using the "switch interview" structure: first thought, passive looking, active looking, deciding event. The discontinuity of switching reveals the job.
2. **Identify functional, emotional, and social dimensions.** What is the user literally trying to accomplish? How do they want to feel? How do they want to be perceived?
3. **Write the job statement** in canonical form. Test it: does it explain why the customer fired their previous solution and hired yours?
4. **Map competing alternatives** including non-consumption. Customers always have alternatives; if you don't know what they're firing, you don't understand the job.
5. **Identify the desired outcomes** (Ulwick's contribution) — measurable success criteria the customer uses to judge any solution. Rank by importance and current satisfaction. Underserved outcomes (high importance, low satisfaction) are the opportunity space.

## Examples

1. **Suzy Decision Engine.** The functional job: "answer a stakeholder question with consumer evidence in time for the meeting." The emotional job: "feel confident the answer will hold up under scrutiny." The social job: "be perceived as the analyst who delivers, not the analyst who pushes back on timelines." Solutions optimizing only the functional layer (faster studies) miss the emotional layer (confidence) — and confidence is what determines re-hire.
2. **Riché's office hours.** Job: "When I'm stuck on a technical decision and can't trust my own loop, I want to think alongside someone whose judgment I respect, so I can leave with an action and unblock the team." This reveals office hours competes with peer Slack DMs and mentor 1:1s, not with consultants.

## Related entries

- `corpus/pm-frameworks/thinkers/christensen-clayton.md` — Christensen's broader theory of disruption
- `corpus/pm-frameworks/discovery/core-jobs-framework.md` — Intercom's operational variant
- `corpus/pm-frameworks/prioritization/jtbd-prioritization.md` — using job importance to prioritize
- `corpus/pm-frameworks/discovery/problem-vs-solution-space.md` — JTBD as problem-space discipline
- `corpus/pm-frameworks/strategy/blue-ocean.md` — JTBD as input to category creation

## Anti-patterns

- **Persona substitution.** "Marketing managers want X" is a persona statement, not a job statement. Personas describe who; jobs describe what they're trying to make progress on. The same persona has dozens of jobs.
- **Feature-as-job.** "The job is to share dashboards" — that's a feature. The job behind it might be "make our team's results visible to leadership without me having to defend them in a meeting."
