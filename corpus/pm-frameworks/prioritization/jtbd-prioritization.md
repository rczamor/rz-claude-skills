---
name: JTBD Prioritization
domain: pm-frameworks
source_skill: research
entry_type: framework
length_target: 500
related: [corpus/pm-frameworks/discovery/jobs-to-be-done.md, corpus/pm-frameworks/discovery/core-jobs-framework.md, corpus/pm-frameworks/thinkers/christensen-clayton.md]
---

# JTBD Prioritization

## What it is

Prioritizing roadmap initiatives by the importance and current satisfaction of customer **jobs**, not by the appeal of features. Two coordinated rankings:

1. **Job importance:** how critical is the job to the customer's progress (1–10)?
2. **Job satisfaction:** how well are current solutions (yours and competitors') performing on that job (1–10)?

The opportunity score for each job: **Importance + max(Importance − Satisfaction, 0)** (Tony Ulwick's Outcome-Driven Innovation formula).

Jobs with high importance and low satisfaction are **underserved** — the highest-ROI place to invest. Jobs with high importance and high satisfaction are **served** — investing here yields diminishing returns. Jobs with low importance are deprioritized regardless of satisfaction.

## Why it matters

Feature-level prioritization measures the wrong thing. Whether to build "AI-recommended studies" depends entirely on which job it serves and how underserved that job is. Two teams with identical roadmaps can be making opposite-quality decisions if they've identified different jobs.

JTBD prioritization elevates the prioritization to the job layer, where competitive context lives. Your competitor isn't the team building similar features; it's whatever the customer is currently hiring for the same job. If incumbent solutions already satisfy a job (high satisfaction), you can't differentiate on it. If incumbent solutions fail (low satisfaction), even modest improvement creates outsized value.

For AI products, JTBD prioritization is especially clarifying. The temptation is to build wherever AI capability is novel; JTBD redirects to wherever an underserved job exists that AI capability can newly serve. The first lens optimizes capability output; the second optimizes customer value capture.

## How to apply

1. **Identify the customer's jobs** via JTBD interviews (functional, emotional, social).
2. **Survey importance and satisfaction** across a representative customer sample. Both metrics on a 1–10 scale, per job.
3. **Calculate opportunity scores.** Underserved jobs (importance > satisfaction by a margin) are the priority.
4. **Sort the roadmap by opportunity score.** Features get justified by the underserved job they address.
5. **Recheck periodically.** As you ship and as competitors move, satisfaction levels change. The opportunity landscape evolves.

## Examples

1. **Suzy Insights jobs ranking.** Survey of 200 analysts. Job: "frame the right methodology for an ambiguous stakeholder question." Importance 9, satisfaction 4 — opportunity score 14. Job: "schedule a recurring tracker." Importance 6, satisfaction 8 — opportunity score 6. Even though tracker scheduling is well-loved (high satisfaction), the underserved methodology-framing job dominates the prioritization and reshapes Q3.
2. **JTBD prioritization at Helm Labs.** Among five candidate jobs, "explain a variance to the board on 24 hours' notice" scored highest opportunity (importance 10, satisfaction 3). The roadmap pivoted toward instant variance narratives — not because the feature was novel, but because the job was the most underserved.

## Related entries

- `corpus/pm-frameworks/discovery/jobs-to-be-done.md` — the parent framework
- `corpus/pm-frameworks/discovery/core-jobs-framework.md` — pains and gains as job-decomposition
- `corpus/pm-frameworks/thinkers/christensen-clayton.md` — JTBD origin

## Anti-patterns

- **Feature-level reasoning dressed as JTBD.** Listing features and labeling them "jobs." A real job is a customer-progress goal in customer language; "AI summarization" is a feature.
- **Satisfaction inflation.** Customers report high satisfaction with their current workarounds because they've forgotten how painful the workaround is. Probe with behavioral questions ("walk me through the last time you did this"), not preference questions.
