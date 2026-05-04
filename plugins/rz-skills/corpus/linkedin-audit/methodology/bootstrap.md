---
name: Bootstrap
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: pattern
length_target: 400-700
related: [corpus/linkedin-audit/methodology/export-parsing.md, corpus/linkedin-audit/methodology/master-tracker-update.md, corpus/linkedin-audit/databases/master-tracker-sheet-schema.md]
---

# Bootstrap

## What it is
The first step of every monthly audit run. Verifies environmental readiness, locates the export to audit, reads prior-state baselines, and initializes the per-pillar findings buffer. Bootstrap fails loudly — if any required input is missing, the run halts with a single explicit message rather than producing a partial audit.

## Why it matters
Bootstrap is the only step that's allowed to refuse to run. Once data parsing starts (Step 2), the audit commits to producing a page; partial audits corrupt the time series. Catching missing connectors, missing exports, or stale master tracker data before parsing protects the integrity of every downstream output (Notion page, Linear tasks, Slack post).

## How to apply

**1. Verify MCP connectors.** Reach a no-op endpoint on each:
- Notion (`notion-fetch` on `NOTION_LINKEDIN_AUDIT_DB_ID`)
- Linear (`list_teams` filtered to `LINEAR_TEAM_ID`)
- Slack (search `#brand` for any post)
- Google Drive (`search_files` rooted at `Brand > LinkedIn Archive > _Content Analytics`)

If any fails, halt with: `Bootstrap failed: {connector} unreachable. {next-action}.`

**2. Locate the latest export and the diff baseline.**
- Search `_Content Analytics > export/` for files named `Content_*_RichéZamor*` sorted by file end-date in name (filename pattern: `Content_{YYYY-MM-DD}_{YYYY-MM-DD}_RichéZamor`).
- Latest export = highest end-date. This is the audited window.
- Diff baseline = the export immediately prior. If only one export exists, baseline = none; first audit runs without MoM deltas (per `master-tracker-update.md` first-run handling).

**3. Read Master Tracker state.**
- Open file at `MASTER_TRACKER_FILE_ID`.
- Read tabs: `Posts Master`, `Snapshots`, `Monthly Summary`. Cache row counts and most-recent month for parity-check after Step 3 update.

**4. Read mapping data.**
- Content Topics DB (`CONTENT_TOPICS_DB_ID`): pull rows where the URL appears in this period's TOP POSTS so we have Format + Domain assignments ready.
- Competitors DB (`COMPETITORS_DB_ID`): pull rows where Tier is `Direct` or `Aspirational` for P5 benchmarking.

**5. Initialize findings buffer.**
- Create an in-memory dict: `{p1: [], p2: [], p3: [], p4: [], p5: [], p6: []}`.
- Each finding will be appended as `{severity: P0|P1|P2, headline: str, evidence: str, action: str}`.

**6. Compute period metadata.**
- `Period Start` = export start date
- `Period End` = export end date
- `Audit Date` = today (or the next first-Sunday if running ahead of cadence)
- `Title` = `LinkedIn Audit — {Month YYYY}` where Month YYYY is derived from `Period End`.

## Bootstrap failure modes

| Failure | Detection | Action |
|---|---|---|
| MCP unreachable | Connector check fails | Halt with explicit connector name |
| No exports in Drive folder | search returns 0 files | Halt; tell Riché to drop the export |
| Master Tracker missing | `MASTER_TRACKER_FILE_ID` doesn't resolve | Halt; tell Riché to create per `master-tracker-sheet-schema.md` |
| Master Tracker has no `Posts Master` tab | tab list missing | Halt; tracker setup incomplete |
| Latest export is older than 35 days | end-date in name >35 days ago | Warn, don't halt; tell Riché the export is stale |
| Latest export = previous month's (no new export) | end-date matches prior audit's Period End | Halt; nothing new to audit |

## Examples
1. **Standard run.** First Sunday of June 2026. Bootstrap finds `Content_2026-05-05_2026-06-04_RichéZamor` as latest, `Content_2026-04-04_2026-05-04_RichéZamor` as baseline. All connectors reachable. Master Tracker has 47 rows in Posts Master. Buffer initialized. Proceeds to Step 2.
2. **First-run.** First audit ever. Only `Content_2026-04-04_2026-05-04_RichéZamor` exists. No baseline. Bootstrap proceeds with `baseline = none`; Step 3 will populate Posts Master from scratch.
3. **Failed run (export missing).** Riché forgot to drop the June export. Bootstrap halts: `Bootstrap failed: no Content_* file with end-date in last 7 days at Brand > LinkedIn Archive > _Content Analytics > export/. Re-run after dropping the export.` Riché drops the export, re-runs, succeeds.

## Related entries
- `corpus/linkedin-audit/methodology/export-parsing.md` — Step 2, consumes the export located here
- `corpus/linkedin-audit/methodology/master-tracker-update.md` — Step 3, writes to the tracker read here
- `corpus/linkedin-audit/databases/master-tracker-sheet-schema.md` — defines the tabs Bootstrap reads
- `corpus/growth/playbook/linkedin-monthly-dump-workflow.md` — the upstream workflow Riché runs to populate the export folder

## Anti-patterns
- Proceeding when the export is stale. A 6-week-old export means the audit covers the wrong window; either Riché skipped a month or the workflow broke. Don't paper over it.
- Skipping the diff baseline read because "this is the first run anyway." First-run handling is explicit; the absence of baseline is a state, not a default.
- Initializing the buffer with placeholder findings. Empty dicts only; pillars decide what to add.
