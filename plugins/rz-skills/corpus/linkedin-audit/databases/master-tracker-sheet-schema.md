---
name: Master Tracker — Google Sheet Schema (6 tabs)
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: resource
length_target: 600-1000
related: [corpus/linkedin-audit/methodology/master-tracker-update.md, corpus/linkedin-audit/views/compounders.md, corpus/linkedin-audit/views/late-bloomers.md, corpus/linkedin-audit/views/format-decay-curves.md]
---

# Master Tracker — Google Sheet Schema (6 tabs)

## What it is
The Google Sheets file that holds the longitudinal LinkedIn post performance data. Path: `Brand > LinkedIn Archive > _Content Analytics > _LinkedIn_Post_Performance_Master.xlsx`. File ID stored in the `MASTER_TRACKER_FILE_ID` constant in SKILL.md.

This is the only persistent data store the audit owns (Notion holds the audit pages; Drive holds the raw exports; the Master Tracker holds the post-by-post time series that links them).

**Setup status:** the Sheet structure with 6 tabs, formulas, and views requires manual setup by Riché. The audit skill consumes the sheet but does not create it. See "Manual setup" section below.

## The 6 tabs

### Tab 1: `Posts Master`
One row per post. Primary key: Post URL.

| Column | Type | Source / formula |
|---|---|---|
| Post URL | text | LinkedIn export TOP POSTS |
| Activity ID | text | Parsed from URL: `urn:li:activity:NNN` |
| Publish Date | date | LinkedIn export |
| Format | select | Hot Take / Signal / Deep Dive / Framework / Story (from Content Topics DB or manual tag) |
| Domain | select | Context Intelligence / PM / Leadership / Intersection (from Content Topics DB or manual tag) |
| First Snapshot Month | text | First YYYY-MM the post appeared in any export |
| First Snapshot Impressions | number | Impressions at first appearance |
| First Snapshot Engagements | number | Engagements at first appearance |
| Latest Snapshot Month | text | Most recent YYYY-MM the post appeared |
| Latest Snapshot Impressions | number | Impressions at latest appearance |
| Latest Snapshot Engagements | number | Engagements at latest appearance |
| Lifetime Impressions | formula | `=SUMIF(Snapshots!A:A, A2, Snapshots!E:E)` (sum impressions in Snapshots where URL matches) |
| Lifetime Engagements | formula | `=SUMIF(Snapshots!A:A, A2, Snapshots!F:F)` |
| Days Since Publish | formula | `=TODAY() - C2` |
| Decay Status | formula | `=IF(Latest Snapshot Month appears in last 2 audit months, "Active", IF(post newly entered TOP POSTS this month AND Days Since Publish > 30, "Late Bloomer", "Plateaued"))` |

The Decay Status formula is described in plain language above; the implementation is a nested IF or a script function in the Sheet.

### Tab 2: `Snapshots`
Append-only time-series. One row per (post, month) pair.

| Column | Type |
|---|---|
| Post URL | text |
| Snapshot Month | text (YYYY-MM) |
| Period Start | date |
| Period End | date |
| Impressions | number |
| Engagements | number |
| MoM Impression Delta | formula `=Impressions - <prior-month-row-for-this-URL>.Impressions` (or 0 if first snapshot) |
| MoM Engagement Delta | formula similar |
| Days Since Publish at Snapshot | formula `=Period End - <Posts Master>.Publish Date` |

The MoM formulas can be implemented via INDEX/MATCH against the prior-month row for the same URL; example formula provided in the manual-setup section.

### Tab 3: `Monthly Summary`
One row per audited month.

| Column | Type | Source |
|---|---|---|
| Month | text (YYYY-MM) | from period |
| Posts Published | number | period count |
| Total Impressions | number | period sum |
| Total Engagements | number | period sum |
| Engagement Rate | formula | `=Total Engagements / Total Impressions` |
| Avg Impressions/Post | formula | `=Total Impressions / Posts Published` |
| Top Format by Impressions | formula | `=QUERY` against Snapshots × Posts Master Format |
| Top Domain by Impressions | formula | similar |
| New Followers | number | period sum from FOLLOWERS |
| Total Followers (EOP) | number | manual entry from LinkedIn UI |
| ICP Match % (Senior+) | number | from DEMOGRAPHICS |

### Tab 4: `Compounders`
Auto-computed view per `corpus/linkedin-audit/views/compounders.md`. Pulls from Snapshots × Posts Master.

### Tab 5: `Late Bloomers`
Auto-computed view per `corpus/linkedin-audit/views/late-bloomers.md`. Filters Posts Master where Decay Status = "Late Bloomer".

### Tab 6: `Format Decay Curves`
Auto-computed pivot per `corpus/linkedin-audit/views/format-decay-curves.md`. Pivots Snapshots by Format × Days bucket, values = avg impressions.

## Manual setup (Riché creates this once)

The audit skill consumes the tracker but does not build it. Riché creates the sheet via:

1. **Create file.** New Google Sheets file at `Brand > LinkedIn Archive > _Content Analytics/`. Name: `_LinkedIn_Post_Performance_Master`.
2. **Create tabs.** 6 tabs with names exactly: `Posts Master`, `Snapshots`, `Monthly Summary`, `Compounders`, `Late Bloomers`, `Format Decay Curves`.
3. **Add column headers** per the schema above. Match exactly — the audit reads columns by header name.
4. **Add the formula columns** in Posts Master:
   - Lifetime Impressions: `=SUMIF(Snapshots!A:A, A2, Snapshots!E:E)`
   - Lifetime Engagements: `=SUMIF(Snapshots!A:A, A2, Snapshots!F:F)`
   - Days Since Publish: `=TODAY() - C2`
   - Decay Status: implement as a nested IF or a custom function (a Google Apps Script function may be cleaner)
5. **Add formula columns in Snapshots:**
   - MoM Impression Delta: `=E2 - IFERROR(INDEX(E:E, MATCH(1, (A:A=A2)*(B:B<B2), 0)), 0)` (array formula; pulls prior month for same URL)
   - MoM Engagement Delta: similar with column F
   - Days Since Publish at Snapshot: `=D2 - VLOOKUP(A2, Posts_Master!A:C, 3, FALSE)`
6. **Add Monthly Summary formulas** — Engagement Rate, Avg Impressions/Post, Top Format/Domain QUERYs.
7. **Set up the auto-views** in Tabs 4-6:
   - Compounders: QUERY filter on Snapshots
   - Late Bloomers: QUERY filter on Posts Master
   - Format Decay Curves: pivot table on Snapshots × Posts Master
8. **Capture file ID** from the Drive URL and populate `MASTER_TRACKER_FILE_ID` in `rz-linkedin-audit/SKILL.md` Constants block.

## How the audit consumes the tracker

Per `methodology/master-tracker-update.md`:

- **Read** Posts Master, Snapshots, Monthly Summary at Bootstrap (Step 1)
- **Upsert** Posts Master rows in Step 3 (new posts → insert; existing posts → update Latest Snapshot fields + recompute Decay Status)
- **Append** Snapshots rows for each (post, this-month) pair in Step 3
- **Append** one Monthly Summary row in Step 3
- **Read** Compounders, Late Bloomers, Format Decay Curves views in Step 7 for narrative

The append-only discipline is critical: never modify or delete past Snapshots rows. The time series is the time series; if a row is wrong, surface it as a P2 anomaly, don't rewrite history.

## Examples

1. **Standard month.** Posts Master grows by 12 new posts (35 upserts). Snapshots gets 47 new rows appended. Monthly Summary gets 1 row appended. Views auto-refresh.
2. **First-run.** Posts Master starts empty. All 31 posts in May export are new. Snapshots gets 31 rows. Monthly Summary: 1 row. Views show 0 compounders (no prior data), 0 late bloomers (no prior data), Format Decay Curves data sparse.
3. **Sheet structure missing.** Bootstrap fails because Posts Master tab has no rows or the columns differ from spec. Halts with: "Bootstrap failed: Master Tracker structure mismatch. Verify against `master-tracker-sheet-schema.md`."

## Related entries
- `corpus/linkedin-audit/methodology/master-tracker-update.md` — Step 3 protocol
- `corpus/linkedin-audit/views/compounders.md` — Tab 4
- `corpus/linkedin-audit/views/late-bloomers.md` — Tab 5
- `corpus/linkedin-audit/views/format-decay-curves.md` — Tab 6

## Anti-patterns

- Modifying past Snapshots rows. Append-only.
- Renaming tabs. The audit reads by tab name; renames break it.
- Storing the tracker outside the documented Drive path. Move = file ID changes = SKILL.md needs updating.
- Treating the tracker as the source of truth for posts not in TOP POSTS. Posts that never appeared in TOP POSTS aren't in the tracker; that's by design (the export is the data; the tracker is the time series of the export).
