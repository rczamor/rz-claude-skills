---
name: P1 — Reach & Velocity
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: rule
length_target: 400-700
related: [corpus/linkedin-audit/methodology/pillar-analysis.md, corpus/linkedin-audit/methodology/export-parsing.md, corpus/growth/channels/linkedin-cadence.md, corpus/growth/playbook/budget-allocation.md]
---

# P1 — Reach & Velocity

## Purpose
Measures whether Riché is publishing at the cadence target (5x/week = ~22 posts/month) and whether reach is holding or compounding. Also surfaces export-integrity issues (parse anomalies fire here as P0 — Reach & Velocity is the first pillar evaluated and bears the responsibility of refusing to proceed if the data isn't trustworthy).

## Inputs
- `parsed_export.totals` — period total impressions, members reached
- `parsed_export.daily` — daily impressions + engagements time series
- `parsed_export.daily_followers` — daily new-follower count
- `parsed_export.parse_anomalies` — any anomalies surfaced in Step 2
- Master Tracker `Monthly Summary` rows (last 6 months) for trend context

## Metrics computed

| Metric | Formula | Target |
|---|---|---|
| Posts published | count posts with publish_date in [Period Start, Period End] | 22 (5x/week × 4.4 weeks) |
| Total impressions | sum from DISCOVERY | grow MoM |
| Avg impressions/post | total_impressions / posts_published | grow MoM |
| Net follower growth | sum daily new-followers | grow MoM |
| Profile views | NOT IN EXPORT | (deferred) |
| Cadence held | posts_published / 22 | ≥ 0.80 |
| Reach trend | (this_month_impressions - last_month) / last_month | ≥ 0 |

Profile views are explicitly out of scope (not in the export); a future enhancement could pull them via a separate workflow.

## Severity rules

| Condition | Severity | Headline pattern |
|---|---|---|
| `parse_anomalies` non-empty (export schema changed or truncated) | **P0** | "Export parse failure: {anomaly}. Pillars degraded; re-export required." |
| Posts published <50% of target (<11) OR impressions dropped >50% MoM | **P0** | "Cadence collapsed: {N} posts vs 22 target." OR "Impressions down {N}% MoM." |
| Posts published 50-80% of target (11-17) OR impressions down 20-50% MoM | **P1** | "Cadence below target: {N} posts (target 22)." OR "Impressions down {N}% MoM." |
| Posts published 80-100% (18-22) | **P2** | "Cadence at {N} posts (target 22) — flexible week." |
| Everything within target ranges | (no finding) | — |

## Headline format for findings

```
{severity}: {headline}

Evidence:
- Posts published: {N} (target 22, {pct}% of target)
- Total impressions: {N} (MoM {Δ%})
- Avg impressions/post: {N} (MoM {Δ%})
- Net follower growth: +{N} (MoM {Δ%})
- {parse anomaly description if applicable}

Action:
{recommended-action specific to the cause}
```

## Action recommendations

The action paired with each fired finding should be specific:

- **Cadence collapse (P0):** "Re-establish Sunday batch session (`corpus/growth/playbook/batch-writing-sunday.md`); pre-write 2 weeks ahead."
- **Cadence below target (P1):** "Recover one missing post category in next week's batch (Mon hot take or Wed deep dive most often the gap)."
- **Impressions drop (P0/P1):** "Run engagement-drop diagnostic per `corpus/growth/diagnostics/engagement-drop-diagnostic.md`. Don't pivot strategy; observe 2 weeks first."
- **Parse anomaly (P0):** "Update `corpus/linkedin-audit/methodology/export-parsing.md` for the new schema before next audit."

## Examples

1. **Healthy month.** 23 posts, total impressions 18,400 (up 12% MoM), avg 800/post, +85 followers (steady). No findings; pillar shows P2 baseline only in narrative ("Cadence at 23 posts, 105% of target").
2. **Cadence below target (P1).** Travel month: 16 posts (73% of target). Impressions held flat (down 4% MoM). P1 fires: "Cadence below target: 16 posts vs 22." Action: recover 2 missing Wed deep dives in next batch.
3. **Cadence collapse + impressions drop (P0).** Heavy interview prep month: 9 posts (41% of target), impressions down 38%. P0 fires both: cadence + impressions. 1 task issued (most severe — impressions diagnostic).
4. **Parse anomaly (P0).** LinkedIn changed TOP POSTS columns. `parse_anomalies = ["TOP POSTS schema: 4 cols, expected 3"]`. P0 fires: "Export parse failure: TOP POSTS schema changed. Pillars degraded; re-export required." Halts task issuance for affected pillars.

## Related entries
- `corpus/linkedin-audit/methodology/pillar-analysis.md` — runs this pillar in order
- `corpus/linkedin-audit/methodology/export-parsing.md` — Step 2; parse anomalies surface here
- `corpus/growth/channels/linkedin-cadence.md` — defines the 5x/week target this pillar verifies
- `corpus/growth/playbook/budget-allocation.md` — explains why cadence is the binding constraint

## Anti-patterns

- Inflating P1 severity when posts are slightly below target. 80-100% is acceptable variance; reserve P1 for actual gaps.
- Treating an in-quarter algo change as a cadence problem. Cadence held but reach dropped → run the engagement-drop diagnostic, don't blame the operator.
- Suppressing parse anomalies to keep the audit "clean." Anomalies are P0 by design; clean reports built on bad data are worse than honest red ones.
