---
name: Export Parsing
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: pattern
length_target: 500-900
related: [corpus/linkedin-audit/methodology/bootstrap.md, corpus/linkedin-audit/methodology/master-tracker-update.md, corpus/linkedin-audit/pillars/p1-reach-velocity.md, corpus/linkedin-audit/pillars/p2-audience-composition.md, corpus/linkedin-audit/pillars/p3-thesis-resonance.md]
---

# Export Parsing

## What it is
Step 2 of the audit. Reads the LinkedIn Creator Analytics 30-day export located by Bootstrap. Parses 5 distinct sections (DISCOVERY, ENGAGEMENT, TOP POSTS, FOLLOWERS, DEMOGRAPHICS) into structured data the pillars can consume. Surfaces parsing anomalies as P0 findings under P1 — schema changes by LinkedIn are uncaught risk that needs to fire loudly.

## Why it matters
The LinkedIn Creator Analytics export is a single Google Sheets file with stacked tables, not separate sheets per section. Tables are separated by blank rows + new headers. Parsing must handle:

- Variable row counts per section (depends on activity in the period)
- Header rows that look like data rows (TOP POSTS has a label row that needs `skiprows=1`)
- Truncated DEMOGRAPHICS section (sits at the very end; some tooling truncates at file size limits)
- Date format ambiguity (`1/2/2026` could be Jan 2 or Feb 1; LinkedIn uses M/D/YYYY US format consistently)
- Posts older than the audit window appearing in TOP POSTS rankings (LinkedIn's "top by engagement" pulls from a 12-month window even though daily metrics are 30-day)

Without explicit handling of each, the audit silently misreads data and makes wrong calls.

## How to apply

The export contains 5 sections in this order:

### Section 1: Overall Performance / DISCOVERY
First two rows of the file. Format:
```
| Overall Performance | {Period Start} - {Period End} |
| Impressions | {N} |
| Members reached | {N} |
```

Extract: `total_impressions`, `members_reached`, `period_label`.

### Section 2: ENGAGEMENT (daily time series)
Header row: `| Date | Impressions | Engagements |`. Then one row per day in the period.

Extract: list of `{date, impressions, engagements}`. Compute weekly rollups by ISO week. Compute period-avg `engagement_rate = sum(engagements) / sum(impressions)`.

### Section 3: TOP POSTS by Engagements
Header row: `| Post URL | Post publish date | Engagements |`. Then up to 50 rows sorted descending.

**Quirk:** Skip the section header row (the "Top posts by Engagements" line itself if present as a row). The actual table header is `| Post URL | Post publish date | Engagements |`.

**Quirk:** Posts can be older than the period — LinkedIn surfaces top performers from a longer window. Extract `publish_date` from the row; flag any post older than `Period Start` as a `late_bloomer_candidate` (per `corpus/linkedin-audit/views/late-bloomers.md`).

Extract: `top_posts_by_engagements = [{url, publish_date, engagements}]`.

### Section 4: TOP POSTS by Impressions
Same shape as Section 3 but ranked by impressions. Up to 50 rows.

Extract: `top_posts_by_impressions = [{url, publish_date, impressions}]`.

Cross-reference Sections 3 and 4: posts in both lists are the strong performers. Posts in Section 4 but not Section 3 are high-reach-low-engagement (often shares of others' content). Posts in Section 3 but not Section 4 are high-engagement-low-reach (often comment threads on Riché's own posts).

### Section 5: FOLLOWERS
Header: `| Date | New followers |`. Daily new-follower count.

**Quirk:** First row may be a label like "Total followers gained" — skip if not date-formatted.

Extract: list of `{date, new_followers}`. Compute `net_follower_growth = sum(new_followers)`. The `total_followers (EOP)` is NOT in the export — has to be captured separately (manual or from the LinkedIn UI) or carried forward from the prior month + net growth.

### Section 6: Top Demographics
Header rows for each subsection: `Job titles`, `Locations`, `Industries`, `Seniority`, `Company size`, `Companies`. Each subsection has 5+ rows of `{Value, Percentage}`.

**Quirk:** This is the LAST section; if the export was truncated mid-file, demographics are missing. Detect: if the file ends without a Companies subsection, mark `demographics_truncated = true` and surface as P0 in P1 ("export incomplete; re-export").

Extract per subsection: ordered list of `{value, percentage}`.

## Output of Step 2

A structured object the pillars consume:

```
parsed_export = {
  period_start, period_end,
  totals: {impressions, members_reached},
  daily: [{date, impressions, engagements}],
  top_posts_by_engagements: [{url, publish_date, engagements}],
  top_posts_by_impressions: [{url, publish_date, impressions}],
  daily_followers: [{date, new_followers}],
  demographics: {
    job_titles: [{value, pct}],
    locations: [{value, pct}],
    industries: [{value, pct}],
    seniority: [{value, pct}],
    company_size: [{value, pct}],
    companies: [{value, pct}]
  },
  parse_anomalies: [string],
  demographics_truncated: bool
}
```

## Examples
1. **Clean parse.** May 2026 export. 5 sections all present, 31 days in ENGAGEMENT, 47 rows in TOP POSTS by Engagements, 50 rows in TOP POSTS by Impressions (capped), 31 rows in FOLLOWERS, 6 demographics subsections. `parse_anomalies = []`. Proceeds.
2. **Late bloomer detected.** TOP POSTS by Engagements row has `publish_date = 2025-10-06` but `Period Start = 2026-04-04`. Flagged as `late_bloomer_candidate`. Surfaces in `views/late-bloomers.md`.
3. **Truncated DEMOGRAPHICS.** File ends at "Top Industries" — no Companies subsection. `demographics_truncated = true`. Surfaces as P0 finding under P1: "Export truncated mid-DEMOGRAPHICS section. Re-export required for P2 to run."
4. **Schema change.** LinkedIn changed the TOP POSTS columns — added a `Reach` column. Parser fails on column count mismatch. Surfaces as P0: "TOP POSTS schema changed (4 cols vs expected 3). Update export-parsing.md before next run." Halts audit.

## Related entries
- `corpus/linkedin-audit/methodology/bootstrap.md` — Step 1, locates the export this step parses
- `corpus/linkedin-audit/methodology/master-tracker-update.md` — Step 3, consumes the parsed output
- `corpus/linkedin-audit/pillars/p1-reach-velocity.md` — uses totals + daily
- `corpus/linkedin-audit/pillars/p2-audience-composition.md` — uses demographics
- `corpus/linkedin-audit/pillars/p3-thesis-resonance.md` — uses top_posts_by_engagements

## Anti-patterns
- Treating "section absent" as "section empty." Absent = parse failure or truncation; empty = legitimate zero activity. Different actions.
- Trusting LinkedIn's date format without explicit format string. Always parse as M/D/YYYY.
- Auto-fixing "Schema changed" without surfacing. The schema change should fire as P0 so the parser gets updated before silent miscounts accumulate.
- Joining TOP POSTS to Posts Master by URL substring match. Use exact URL match; the activity ID inside is the canonical key.
