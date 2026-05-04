---
name: LinkedIn Monthly Exports — Data Archive + Content Analytics Workflow
domain: growth
source_skill: growth-marketing
entry_type: template
length_target: 600-1000
related: [corpus/growth/playbook/admin-tracking.md, corpus/growth/playbook/strategic-commenting.md, corpus/growth/channels/linkedin-cadence.md, corpus/growth/metrics/segment-proxies-rollup.md, corpus/growth/databases/quarterly-reviews-schema.md]
---

# LinkedIn Monthly Exports — Data Archive + Content Analytics Workflow

## What it is
Riché's monthly ~15-minute workflow for capturing two LinkedIn exports and dropping them into Google Drive at predictable paths. Together, the two exports give a complete picture of LinkedIn outbound activity (data archive) AND inbound engagement received (content analytics). The exports are the data spine for `rz-website-audit` (weekly) and `rz-quarterly-review` (quarterly).

Two exports, one monthly cadence:

1. **LinkedIn Data Archive** — the full data export from LinkedIn's "Get a copy of your data" tool. ~50 CSV files covering outbound activity (Shares, Comments, Reactions given, InstantReposts) plus connection state. **The export is FULL HISTORY each time, not delta.**
2. **LinkedIn Content Analytics** — engagement-received metrics export from LinkedIn's analytics dashboard. Per-day impressions/engagements, per-post performance, new followers per day, and audience demographics. Date range chosen at export time.

## Why it matters
LinkedIn does not expose engagement data via any third-party API at Riché's account tier. These two exports are the only complete machine-readable record. Together they cover:

- **Outbound activity:** every post, every comment, every reaction given, every reshare (data archive)
- **Inbound engagement:** impressions per day, engagements per day, top posts by engagement and impressions, new followers per day (content analytics)
- **Audience composition:** demographics by job title, location, industry, seniority, company size, company (content analytics — used to verify Segment 1/2/3/4 mix in the actual audience)

Without this monthly cadence, the audit and quarterly review are blind to LinkedIn — the primary channel where Segment 2 lives.

## Where the exports live

**Path:** `Brand > LinkedIn Archive/`

Within that folder:
- **Monthly data archives:** subfolders named `{MM01YY}` (e.g., `05012026`, `06012026`). Contain the ~50 CSV files from "Get a copy of your data" plus sub-folders for Articles, Jobs, Verifications, Services Marketplace.
- **Content analytics exports:** all in a single `_Content Analytics/` subfolder. Files named `Content_{YYYY-MM-DD}_{YYYY-MM-DD}_RichéZamor` (date range in filename matches the export's chosen range).

The folder structure and naming convention are LOCKED. Skills that consume this data resolve the folders by these conventions; renaming or restructuring breaks the consumers.

## The monthly workflow (~15 min)

**Cadence:** First Sunday of each month, after the strategic-commenting block. Bundles into `corpus/growth/playbook/admin-tracking.md`.

### Part A — LinkedIn Data Archive (~10 min)

1. **Request the export** (1 min)
   - LinkedIn → Settings & Privacy → Data Privacy → Get a copy of your data
   - Select "The works" (or equivalent: full archive including activity data)
   - Submit. LinkedIn emails the download link within 10-30 minutes.

2. **Wait for the email** (passive)

3. **Download the .zip** (1 min) when the email arrives.

4. **Extract locally** (1 min). Contains ~50 CSVs plus folders for Articles, Jobs, Verifications, Services Marketplace.

5. **Upload to Google Drive** (5 min)
   - Navigate to `Brand > LinkedIn Archive/`
   - Create a new folder named `{MM01YY}` (e.g., `05012026` for May 2026)
   - Upload all extracted files. Sub-folders preserved.
   - Convert CSVs to Google Sheets via right-click → Open with → Google Sheets → Save back. (Skills consume Google Sheets format.)

6. **Verify upload** (1 min)
   - Open Shares; confirm most-recent row is from within last 24-48 hours
   - Open Connections; confirm row count matches LinkedIn's "X connections" badge ±5

### Part B — LinkedIn Content Analytics (~5 min)

1. **Open LinkedIn analytics** (1 min)
   - LinkedIn → Me → View Profile → Analytics (or directly at the Analytics page)

2. **Set date range and export** (2 min)
   - For monthly cadence: pick a fixed start date (e.g., Jan 1 of the year, or Jan 1 of when LinkedIn tracking began) through today. Each month, the range grows by ~30 days.
   - Alternative: just-prior-month (e.g., Apr 1 – Apr 30). Either works — the consuming skills filter rows by Date column inside the file.
   - Click "Export" or the equivalent CSV download.
   - File downloads as something like `Content_2026-01-01_2026-05-04_RichéZamor.xlsx`.

3. **Upload to Google Drive** (1 min)
   - Navigate to `Brand > LinkedIn Archive > _Content Analytics/`
   - Upload the file. Convert to Google Sheets.

4. **Verify** (1 min)
   - Open the file; confirm "Overall Performance" section header shows the right date range
   - Confirm the daily metrics table reaches up to the export date

## What's IN the data archive

These are the files the audit and quarterly review consume from the monthly `{MM01YY}/` folder:

| File | Direction | Columns | Used for |
|---|---|---|---|
| **Shares** | Outbound (Riché's posts) | Date, ShareLink, ShareCommentary, MediaUrl, Visibility | Posting cadence per week; ShareCommentary length distribution; MediaUrl frequency |
| **Comments** | Outbound (Riché's comments) | Date, Link, Message | Strategic commenting cadence; Message length as substance proxy |
| **Reactions** | Outbound (Riché's reactions given) | Date, Type (LIKE/PRAISE/EMPATHY/...), Link | Engagement-given count; Link cross-ref to target accounts |
| **InstantReposts** | Outbound (Riché's reshares) | Date, ShareLink | Reshare cadence; what's being amplified |
| **Connections** | State (current connection set) | Connected On, ... | Total count = follower-equivalent state; rows with Connected On in window = net new connections |
| **Articles** (folder) | Outbound (LinkedIn articles) | Folder of HTML files | Long-form publishing cadence |
| **Member_Follows** | State | Date, profile URL | Following pattern; cross-ref to target accounts |
| **Company Follows** | State | Followed on, company name | Company-level tracking |
| **Invitations** | Outbound + inbound | Direction, Date, ... | Invite cadence |
| **Profile Summary** | State | Aggregate profile stats | Profile-side baseline |

**The data archive is FULL HISTORY each time.** Each monthly export contains all data from account creation up to the export date. Skills only need to read the most-recent monthly folder; older folders are kept for redundancy/disaster-recovery but not actively consumed.

## What's IN the content analytics export

The Content Analytics file has 4-5 stacked tables in one Google Sheet:

1. **Overall Performance** — header row + Impressions total + Members reached total for the date range
2. **Daily Impressions + Engagements** — Date | Impressions | Engagements (one row per day in range)
3. **Top posts by Engagements** — Post URL | Post publish date | Engagements (sorted descending)
4. **Top posts by Impressions** — Post URL | Post publish date | Impressions (sorted descending)
5. **New followers per day** — Date | New followers
6. **Top Demographics** — Job titles, Locations, Industries, Seniority, Company size, Companies (each with Value + Percentage)

Used for:
- **Engagement-rate trend:** Engagements ÷ Impressions per day, smoothed weekly
- **Best-performing posts:** identify what content types win on engagement vs impressions
- **Follower growth velocity:** new-followers-per-day trend across the quarter
- **Audience composition validation:** verify Segment 1 (CXO/Director seniority + AI-PM target companies), Segment 2 (Director/Senior Product Manager titles), Segment 3 (Founder/Co-Founder titles), Segment 4 (event-organizer / podcast-host roles in Companies section)

## What's NOT in either export

- ❌ Profile views (LinkedIn Premium feature; separate workflow per `corpus/growth/channels/linkedin-premium-tracking.md`)
- ❌ Per-post comment text (have the URL, not the comments themselves; would require a separate scrape)
- ❌ Search appearances (LinkedIn analytics has it but not in the export)
- ❌ Reach by country/city below "Locations" demographic
- ❌ Per-comment-author engagement on Riché's posts (would let you measure peer-reshare-rate; not available)

## How the exports get consumed

**By `rz-website-audit` (weekly):**
The weekly audit reads the **most-recent** monthly archive folder (one folder, not a series). It filters rows by Date column for the past 7 days. From the data archive: Shares (cadence held this week?), Comments (commenting block held?). Optionally also reads the most-recent Content Analytics file for engagement-rate this week.

**By `rz-quarterly-review` (quarterly):**
The quarterly review reads:
- The **most-recent** monthly archive folder. Filter all relevant files by Date column for past 90 days.
- The **most-recent** Content Analytics file. Filter the daily tables by Date for past 90 days.

For first-run scenarios where some history is missing (e.g., only one monthly archive exists), the skill works with what's available. Connections file in the most-recent archive contains all historical connections, including those before the data-export workflow started, so connection-growth-over-90-days is always answerable from the most-recent archive.

**By `rz-self-improve` (occasional):**
When patterns emerge in voice or content drift, self-improve reads the Shares ShareCommentary text and the Top posts by Engagements/Impressions tables to surface what's working vs not.

## Edge cases and gaps

- **First-time setup:** the first export is the baseline; consumers don't fail on lack of prior history. The Connections file in the first export already contains all historical connections.
- **Travel month:** if you miss a month, the next month's full export contains all the data anyway. Catch up by uploading the next export normally; older folders just don't get filled in.
- **LinkedIn export delays:** if the email takes >24 hours, defer the upload to the next day. Don't delay the rest of the Sunday review.
- **Content Analytics date range chosen narrowly:** if you exported only a 30-day range and the quarterly review needs 90 days, it'll fall short. Defaulting to a "from a fixed start through today" range avoids this — each month grows by ~30 days, always covers the prior 90 with margin.
- **`Content_*` filename includes the user's display name:** `Content_2026-01-01_2026-05-04_RichéZamor.xlsx`. The É is preserved correctly in Drive but consuming code should not split on character class — match the filename pattern as `Content_*.xlsx` or `Content_*_RichéZamor.xlsx`.

## Examples
1. **Standard monthly export.** First Sunday of June 2026, ~15 minutes total. Riché requests the data archive (Part A), and while waiting, exports Content Analytics for `2026-01-01_2026-06-07` (Part B), uploads to `_Content Analytics/`. When the data archive email arrives, downloads + extracts + uploads to `06012026/`. Done.
2. **First-time setup (May 2026).** Riché creates `Brand > LinkedIn Archive/` and `_Content Analytics/` subfolder. Runs the May 1 data archive export → uploads to `05012026/`. Runs the Content Analytics export for `2026-01-01_2026-05-04` → uploads to `_Content Analytics/`. From this point forward, monthly cadence holds.
3. **Quarterly review consumption (Q3 2026).** First Sunday of October 2026. The skill identifies the most-recent monthly archive (`10012026/`) and the most-recent Content Analytics file (`Content_2026-01-01_2026-10-04_RichéZamor`). Filters Shares/Comments by Date for last 90 days. Filters Content Analytics daily-impressions table by Date for last 90 days. Uses the demographics section as-is (current snapshot). Produces a complete LinkedIn picture for Q3.

## Related entries
- `corpus/growth/playbook/admin-tracking.md` — the broader monthly-Sunday admin block
- `corpus/growth/playbook/strategic-commenting.md` — the daily activity captured in Comments
- `corpus/growth/channels/linkedin-cadence.md` — the cadence verified by Shares
- `corpus/growth/channels/linkedin-premium-tracking.md` — supplements with profile-view data
- `corpus/growth/metrics/segment-proxies-rollup.md` — uses outbound activity as leading indicators; uses Content Analytics demographics as actual audience composition
- `corpus/growth/databases/quarterly-reviews-schema.md` — Quarterly Reviews DB consumes per-quarter rollup

## Anti-patterns
- Renaming folders. Skills resolve via the `{MM01YY}` and `_Content Analytics` patterns; renames break the search.
- Treating the data archive as delta. It's full history each time; reading multiple monthly folders for one analysis duplicates data.
- Skipping the content analytics export because "it's tedious." Content Analytics is the ONLY source for engagement-received metrics; without it, the audit is blind to engagement rate trends.
- Storing CSVs without converting to Google Sheets. Possible but increases skill-side parsing complexity. Convert at upload time.
- Choosing a narrow date range for content analytics export "for tidiness." The 90-day window for quarterly review needs full coverage; a fixed-start growing-range is safer.
- Synthesizing engagement-received numbers from the data archive alone. The data archive doesn't have engagement received; don't fabricate.
