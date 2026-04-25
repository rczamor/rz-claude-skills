---
name: Section 9 — Deployment & Rollout Review
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: template
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/01-classification-instinct.md, corpus/evaluation-frameworks/review-sections/01-architecture.md, corpus/evaluation-frameworks/review-sections/10-long-term-trajectory.md]
---

# Section 9 — Deployment & Rollout Review

## What it is
Deployments are not atomic — plan for partial states, rollbacks, and feature flags. Section 9 evaluates migration safety (backward-compatible? zero-downtime? table locks?), feature-flag posture, rollout sequencing (migrate first, deploy second), explicit step-by-step rollback, deploy-time risk window (old and new code running simultaneously), environment parity, post-deploy verification checklist, and smoke tests.

## What it evaluates
- Migration safety — for every new DB migration: backward-compatible? Zero-downtime? Table locks?
- Feature flags — should any part be behind a feature flag?
- Rollout order — correct sequence: migrate first, deploy second?
- Rollback plan — explicit step-by-step
- Deploy-time risk window — old code and new code running simultaneously, what breaks?
- Environment parity — tested in staging?
- Post-deploy verification checklist — first 5 minutes? First hour?
- Smoke tests — what automated checks should run immediately post-deploy?

## Required output format
A deployment sequence diagram + a rollback flowchart:

```
  DEPLOYMENT SEQUENCE:
    1. Migration runs (backfill column with default; backward-compatible)
    2. Deploy new code (reads old + new column path; behind feature flag)
    3. Toggle flag to 5% of traffic
    4. Smoke tests run; metrics watched for 1h
    5. Ramp to 50%, then 100%
    6. Drop old column in next migration

  ROLLBACK FLOWCHART:
    If feature error rate > 2% in first hour:
      -> Toggle flag off (immediate)
      -> Investigate; fix; redeploy
    If migration cannot be reversed:
      -> Forward-fix only; no schema rollback
```

Plus the post-deploy checklist:
```
  FIRST 5 MIN  | FIRST HOUR
  -------------|---------------------------
  Health green | Error rate stable
  Logs flowing | New metric trending up
  Smoke tests  | No alert noise
```

## Mode-specific addition
**EXPANSION and SELECTIVE EXPANSION**: also evaluate what deploy infrastructure would make shipping this feature routine. (For SELECTIVE EXPANSION, assess whether accepted cherry-picks change the deployment risk profile.)

## Rules in force
- **STOP. AskUserQuestion once per issue.** Do NOT batch. Recommend + WHY. If no issues or fix is obvious, state what you'll do and move on — don't waste a question. Do NOT proceed until user responds.
- **Do NOT make any code changes. Review only.**

## Why it matters
Most production incidents do not come from the code being wrong — they come from the deploy being wrong. A correct codepath behind a wrong rollout sequence produces an outage. Section 9 is the section that makes the deploy a designed artifact, not a YOLO. The deploy-time risk window question is particularly load-bearing: old and new code coexist for minutes to hours during every deploy, and plans that ignore the window break in subtle ways.

## Examples
1. **Migration that adds NOT NULL column**: plan ships migration + code together. Section 9 surfaces — old code won't insert the new column; deploy window will fail. Fix: add column nullable, backfill, then add NOT NULL in a later migration.
2. **Feature flag plan**: plan ships behind a flag with no rollout sequence. Section 9 demands: 5% → 50% → 100% with metrics watched at each stage; what gets ramped, what gets paused.
3. **No rollback plan**: plan says "we'll rollback if needed." Section 9 demands the explicit steps: which command, who runs it, how long it takes, what's the verification.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/01-classification-instinct.md` — deploy plans inherit the one-way/two-way classification
- `corpus/evaluation-frameworks/review-sections/01-architecture.md` — Section 1's rollback posture sub-bullet seeds Section 9
- `corpus/evaluation-frameworks/review-sections/10-long-term-trajectory.md` — Section 10's reversibility rating compounds with Section 9's rollback plan

## Anti-patterns
- Treating "deploy on Friday afternoon" as a strategy. Section 9's risk-window analysis exists to prevent this.
- Skipping the rollback flowchart because "we have feature flags." Flags don't rollback migrations or backfilled data.
