---
name: Monthly LinkedIn Audits — Notion DB Schema
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: resource
length_target: 400-700
related: [corpus/linkedin-audit/methodology/report-assembly.md, corpus/linkedin-audit/methodology/task-issuance.md, corpus/linkedin-audit/methodology/slack-notification.md]
---

# Monthly LinkedIn Audits — Notion DB Schema

## What it is
The Notion database that holds one page per monthly audit. Database ID `9ccff092811d479891a684c402e6da91`, data source ID `d5206b14-756d-422d-b54b-74d57560e321`. Lives under Brand → Audits (page `356ac0ea4f6580278a7ac7be039b8987`). One page per first-Sunday-of-month audit run, named `LinkedIn Audit — {Month YYYY}`.

## Properties

| Property | Type | Description |
|---|---|---|
| Audit | title | `LinkedIn Audit — {Month YYYY}` (e.g., `LinkedIn Audit — May 2026`) |
| Audit Date | date | First Sunday of the month after the audited period |
| Period Start | date | First day of the audited 30-day window |
| Period End | date | Last day of the audited 30-day window |
| Overall Status | select (Green / Yellow / Red) | Headline traffic light per `report-assembly.md` rules |
| Posts Published | number | Count of posts in the period |
| Total Impressions | number | Period total |
| Engagement Rate | number | Engagements ÷ Impressions; period avg, 2 decimals (display as % if formatted) |
| Avg Impressions Per Post | number | Period average |
| Net Follower Growth | number | Period total new followers |
| Total Followers EOP | number | At period end |
| ICP Match Pct | number | Senior + Director + CXO + Owner combined seniority share |
| Top Format | select (Hot Take / Signal / Deep Dive / Framework / Story) | Best-performing format by impressions |
| Top Domain | select (Context Intelligence / PM / Leadership / Intersection) | Best-performing domain by impressions |
| Domain Mix Drift | select (On-target / CI under / PM over / Leadership over / Other) | Drift vs the 50/30/20 target |
| Gate 1 Impressions | checkbox | 5,000+ avg sustained 8 weeks |
| Gate 2 Engagement | checkbox | 3%+ sustained 8 weeks |
| Gate 3 ICP Quality | checkbox | Manual confirmation |
| Gate 4 Waitlist | checkbox | 200+ signups |
| Linear Tasks Issued | rich_text | Comma-separated TRZ-### IDs |
| Deep Dive Candidates | rich_text | Comma-separated post URLs (Top 5 per `DEEP_DIVE_CRITERION`) |

Total: 21 properties.

## Page body structure

The body, when assembled by `report-assembly.md` Step 7, contains these sections in order:

1. **Headline** — emoji + 1-line verdict
2. **Period Summary** — bullet list of key numbers
3. **Pillar Findings** — P1-P6 sections with status emoji + narrated findings
4. **Master Tracker Highlights** — Top 5 Compounders, Late Bloomers, Format Decay Observation
5. **Deep Dive Candidates** — 5 URLs with selecting metric and 1-line context
6. **Newsletter Gate Check** — 4 gates with current status + trajectory
7. **Voice Drift Sample** — 4 random posts graded against Fatal Fifteen
8. **Linear Tasks Issued** — TRZ-### IDs with task titles

## Why it matters

Each month's audit lives in its own page. The properties enable cross-month queries (which months were Red? which months hit Gate 2? which Format dominated Q1?) without parsing page bodies. The page body is the long-form narrative; the properties are the queryable index.

The Audit (title) format is locked: `LinkedIn Audit — {Month YYYY}`. This makes pages sortable by name and unambiguous when referenced. Don't reformat.

## How properties get populated

Per `methodology/report-assembly.md` Step 7:

- `Audit Date`: today's date when the audit runs
- `Period Start` / `Period End`: from `parsed_export.period_start` / `period_end`
- `Overall Status`: computed per the headline rules
- `Posts Published`, `Total Impressions`, `Avg Impressions Per Post`, `Net Follower Growth`, `Total Followers EOP`: from Master Tracker Monthly Summary row written in Step 3
- `Engagement Rate`: computed in Step 2 (sum engagements / sum impressions)
- `ICP Match Pct`: computed in Step 4 P2 (Senior + Director + CXO + Owner from demographics)
- `Top Format`, `Top Domain`: from Master Tracker Monthly Summary
- `Domain Mix Drift`: derived from comparing actual mix vs `DOMAIN_BALANCE_TARGET`
- 4 Gate checkboxes: per Step 6 newsletter gate computation
- `Linear Tasks Issued`: filled in Step 9 after Step 8 returns TRZ-### IDs (comma-separated)
- `Deep Dive Candidates`: filled in Step 5 (comma-separated URLs)

## Cross-month queries

Multi-month retrospectives are common:
- "Show all months where Overall Status was Red" — filter on Overall Status = "Red"
- "Show months where Gate 2 was checked" — filter on Gate 2 Engagement = true
- "Compare CI Top Domain frequency over last 6 months" — group by Top Domain over Audit Date range
- "Months with ICP Match Pct < 50%" — filter on ICP Match Pct < 0.50 (or 50 depending on display format)

Quarterly retrospectives (per `rz-quarterly-review`) read the most-recent 3 months and summarize trend.

## Examples

1. **Standard page.** `Audit = "LinkedIn Audit — May 2026"`, Audit Date 2026-06-07, Period Start/End 2026-05-05/2026-06-04, Overall Status Yellow, Posts Published 18, Engagement Rate 0.012 (1.2%), Top Format Deep Dive, Top Domain PM, Domain Mix Drift "CI under", Gate 1-4 all unchecked, Linear Tasks Issued "TRZ-145, TRZ-146", Deep Dive Candidates 5 URLs comma-separated.
2. **Red page (parse failure).** Most properties null or 0; Overall Status Red; Linear Tasks Issued = "TRZ-150"; body contains the parse anomaly description.
3. **Gate-met page.** Gate 2 Engagement = true (sustained 3%+ over 8 weeks). Narrative celebrates milestone.

## Related entries
- `corpus/linkedin-audit/methodology/report-assembly.md` — populates this page
- `corpus/linkedin-audit/methodology/task-issuance.md` — fills `Linear Tasks Issued`
- `corpus/linkedin-audit/methodology/slack-notification.md` — uses `Audit` + `Overall Status` + page URL for the Slack post

## Anti-patterns
- Renaming the title format. `LinkedIn Audit — {Month YYYY}` is the queryable key.
- Writing partial pages. The atomic-per-page-create rule means all properties + all body sections at once.
- Editing a prior month's page after creation. Append-only time series; corrections go to next month's narrative.
- Adding properties without updating this schema entry + the SKILL.md + report-assembly.md. The contract is documented; drift breaks downstream tooling.
