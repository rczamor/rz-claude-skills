---
name: Master Tracker Update
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: pattern
length_target: 500-900
related: [corpus/linkedin-audit/databases/master-tracker-sheet-schema.md, corpus/linkedin-audit/methodology/export-parsing.md, corpus/linkedin-audit/views/compounders.md, corpus/linkedin-audit/views/late-bloomers.md]
---

# Master Tracker Update

## What it is
Step 3 of the audit. Takes the parsed export from Step 2 and writes it into the Master Tracker Google Sheet (six tabs documented in `databases/master-tracker-sheet-schema.md`). The tracker is the longitudinal spine — without it the audit only knows this month's data; with it the audit can compute MoM deltas, decay curves, and compounder/late-bloomer status.

## Why it matters
The single 30-day export is a snapshot. Compounder analysis (which posts keep accumulating impressions month-over-month?), late-bloomer analysis (which posts re-entered top performers >30 days after publish?), and format decay curves (how fast does each format lose relevance?) all require the time series. The tracker is the time series.

The update is **append-only for snapshots, upsert for posts** — past months are immutable; only the most-recent month's snapshot is being added; existing posts get their `Latest Snapshot *` fields updated.

## How to apply

### 1. Upsert Posts Master

For each post in the union of `top_posts_by_engagements` and `top_posts_by_impressions`:

1. Compute `activity_id` by parsing `urn:li:activity:NNN` from the URL.
2. Look up by URL in Posts Master.
3. If found:
   - Update `Latest Snapshot Month` = current month
   - Update `Latest Snapshot Impressions` = max(impressions across both top-posts lists for this URL, this period)
   - Update `Latest Snapshot Engagements` = max(engagements across both top-posts lists for this URL, this period)
   - Recompute `Decay Status` per the formula in `databases/master-tracker-sheet-schema.md`
4. If not found:
   - Create new row with all "First Snapshot" fields populated for this period
   - Lookup Format and Domain in Content Topics DB (`CONTENT_TOPICS_DB_ID`) by URL match. If found, populate. If not, leave blank and append URL to the `Unclassified Posts` log (a section at the bottom of the tracker for manual cleanup).
   - Set `Latest Snapshot *` fields = `First Snapshot *` (same period for first appearance)

### 2. Append Snapshots rows

For each post in the upsert above:
- Append one row to `Snapshots` tab: `{Post URL, Snapshot Month: YYYY-MM, Period Start, Period End, Impressions, Engagements}`.
- The MoM delta formulas (`MoM Impression Delta`, `MoM Engagement Delta`) self-compute against the prior `Snapshots` row for the same URL.

**Append-only discipline:** never modify or delete past Snapshots rows. The time series is the time series; if a row is wrong, surface it as a P2 anomaly, don't rewrite history.

### 3. Append Monthly Summary row

One new row to `Monthly Summary` for this audit's month:
- `Month` = YYYY-MM derived from Period End
- `Posts Published` = count of posts with publish_date in [Period Start, Period End] (NOT the same as TOP POSTS rows — TOP POSTS includes older late-bloomers; "Posts Published" is the cadence metric)
- `Total Impressions`, `Total Engagements` = period totals from DISCOVERY
- `Engagement Rate` = computed via formula referencing this row
- `Avg Impressions/Post` = computed via formula
- `Top Format by Impressions`, `Top Domain by Impressions` = computed via QUERY against this period's Snapshots joined to Posts Master
- `New Followers` = sum of daily_followers for the period
- `Total Followers (EOP)` = manual capture (not in export); pulled from prior month's tracker + this period's growth, OR captured by Riché in the LinkedIn UI and entered (preferred for accuracy)
- `ICP Match % (Senior+)` = Senior + Director + CXO + Owner pct from DEMOGRAPHICS

### 4. Refresh views

Compounders, Late Bloomers, and Format Decay Curves are formula-driven. After Steps 1-3, no manual recompute is needed — the formulas re-evaluate when the underlying data changes. Verify: open each view, confirm row counts match the new data state.

### 5. Surface tracker anomalies

If anomalies were detected:
- New posts not found in Content Topics DB → flag count and post URLs as P1 finding under P3 ("`{N}` posts unclassified — tag in Content Topics DB before next audit")
- Posts in current TOP POSTS that were Decay-Status="Plateaued" last month → "late bloomer revival" candidates; flag in narrative
- Posts older than 365 days appearing in TOP POSTS → unusually long tail; flag for narrative

## First-run handling

If `Posts Master` is empty (first audit ever):
- Every post in this period's TOP POSTS is treated as "new" — all First Snapshot fields = current period
- No MoM deltas can be computed; Snapshots will start populating from this run forward
- Note in the audit narrative: "First-run audit; no MoM deltas available. Trend analysis begins next month."

## Examples
1. **Standard month.** May 2026. 47 posts in TOP POSTS Engagement union with TOP POSTS Impressions. 12 are new, 35 are upserts. 47 Snapshots rows appended. Monthly Summary: 1 row added. Compounders view auto-populates: 8 posts with positive MoM delta. Late Bloomers view: 3 posts. Tracker anomalies: 4 new posts not yet in Content Topics DB; flagged for P3.
2. **First-run.** April 2026. Posts Master is empty. 31 posts in TOP POSTS union. All 31 treated as new with First Snapshot = April. No MoM deltas. Audit narrative notes the first-run state.
3. **Decay status transition.** Post `urn:li:activity:7412...` was Active last month (positive MoM delta). This month, no longer in TOP POSTS by either ranking. Status flips to Plateaued. Will count toward `late bloomer revival` candidates if it ever re-enters.

## Related entries
- `corpus/linkedin-audit/databases/master-tracker-sheet-schema.md` — defines the tabs and columns this step writes to
- `corpus/linkedin-audit/methodology/export-parsing.md` — Step 2, source of the data this step writes
- `corpus/linkedin-audit/views/compounders.md` — view that consumes the updated Snapshots
- `corpus/linkedin-audit/views/late-bloomers.md` — view that consumes the updated Posts Master

## Anti-patterns
- Modifying or deleting past Snapshots rows. Append-only. Past data is the truth as of when it was captured; rewrites destroy the time series.
- Computing Total Followers (EOP) by summing daily new-followers without baseline. Drift accumulates; capture the absolute count from LinkedIn UI quarterly to recalibrate.
- Treating "post not in Content Topics DB" as a fatal error. It's a soft error — flag as P1 for cleanup, don't halt.
- Refreshing formulas manually. They auto-compute; manual recompute often introduces errors.
