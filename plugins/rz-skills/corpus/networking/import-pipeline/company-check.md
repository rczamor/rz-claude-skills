---
name: Company Check
domain: networking
source_skill: networking
entry_type: pattern
length_target: 300-500
related: [corpus/networking/import-pipeline/relevance-scan.md, corpus/networking/import-pipeline/fit-score.md]
---

# Company Check

## What it is
A short pass on the contact's company LinkedIn page to capture the structural facts that inform fit score and (if the profile lacks signals) the company-based opener fallback. Used by both networking import skills.

## Why it matters
A profile without company context produces a fit score with no anchor. A Head of Product at a 50-person Series A AI company is a different signal than a Head of Product at a 5,000-person enterprise SaaS shop. The check takes 30 seconds and removes that ambiguity.

The company check is also the fallback opener source. When the profile has no recent activity, the company news is what the warm opener references.

## How to apply

**Open the company LinkedIn page.** Capture three things:

1. **Headcount bucket.** Use LinkedIn's published range: 1-10, 11-50, 51-200, 201-500, 501-1000, 1001-5000, 5000+.
2. **Most recent funding round.** Stage and date if visible in the About section or recent posts (e.g., "Series B, Mar 2025"). Skip if not visible.
3. **Pinned news from the last 90 days.** Product launches, leadership changes, major announcements. Capture the headline and date.

If any field is unavailable (private company, incomplete profile), record `unknown` rather than guessing.

**Output shape (used by both skills):**
```
company: { name, headcount_bucket, funding_stage, funding_date, recent_news }
```

This object stays in run memory; only the headcount and funding stage flow into the fit score. Recent news flows into the company-based opener fallback.

## Examples
1. **AI startup, recently funded.** Company headcount 51-200, Series B raised 2 months ago, recent news is a product launch in beta. Strong company-side signal regardless of profile activity.
2. **Mature SaaS, no recent news.** Company headcount 501-1000, last funding round was Series D from 2021, no pinned news in 90 days. Lower urgency context.
3. **Private/unknown company.** LinkedIn page exists but has no published headcount or funding info. All three fields recorded as `unknown`. Fit score relies entirely on profile signals and title.

## Related entries
- `corpus/networking/import-pipeline/relevance-scan.md` precedes this step
- `corpus/networking/import-pipeline/fit-score.md` consumes the headcount + funding stage

## Anti-patterns
- Spending more than 60 seconds per company. The check is structural, not deep research.
- Reading the company's About blurb and summarizing it. Capture the structural facts only; ignore marketing copy.
- Inferring funding stage from headcount. If the round is not visible, record `unknown`.
