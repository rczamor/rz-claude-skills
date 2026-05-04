---
name: LinkedIn Monthly Data Archive — Export Workflow
domain: growth
source_skill: growth-marketing
entry_type: template
length_target: 500-800
related: [corpus/growth/playbook/admin-tracking.md, corpus/growth/playbook/strategic-commenting.md, corpus/growth/channels/linkedin-cadence.md, corpus/growth/metrics/segment-proxies-rollup.md, corpus/growth/databases/quarterly-reviews-schema.md]
---

# LinkedIn Monthly Data Archive — Export Workflow

## What it is
Riché's monthly ~10-minute workflow for exporting his complete LinkedIn data archive and dropping it into Google Drive at a predictable folder path. The export becomes the data spine for outbound LinkedIn activity tracking — used by `rz-website-audit` (weekly trend) and `rz-quarterly-review` (quarterly-spanning analysis). Without this workflow, neither skill has reliable data on Riché's LinkedIn activity.

## Why it matters
LinkedIn does not expose engagement-tracking data via any third-party API at Riché's account tier. The native `/me/data` export is the only complete, machine-readable record of his LinkedIn activity. Once a month, it gives:

- **Outbound activity:** every post (Shares), every comment (Comments), every reaction given (Reactions), every reshare (InstantReposts)
- **Connection state:** every connection with their connection date (Connections)
- **Self-tracking:** Profile state, Articles published, Companies/People followed

Without this monthly cadence, the audit and quarterly review can only rely on Calendar-block estimation for cadence — much less reliable than the archive's direct row counts.

The 10-minute monthly cost is below the threshold where automation pays back. It also gives Riché a single deterministic moment per month to confirm "yes, I posted N times, I commented M times, I added P connections" — which is its own discipline value.

## Where the archive lives

**Google Drive path:** `LinkedIn Archive > {MM01YY}/`

`{MM01YY}` = month + 01 + 2-digit year for the export. Examples:
- May 2026 export: `05012026`
- January 2027 export: `01012027`

The folder convention is locked. Skills that consume this data search for the folder by the title pattern; renaming or restructuring breaks the consumers.

## The monthly export workflow (~10 min)

**Cadence:** First Sunday of each month, after the strategic-commenting block. Bundles into `corpus/growth/playbook/admin-tracking.md`.

1. **Request the export** (1 min)
   - Go to LinkedIn → Settings & Privacy → Data Privacy → Get a copy of your data
   - Select "The works" (or equivalent: full archive including activity data)
   - Submit. LinkedIn emails the download link within 10-30 minutes.

2. **Wait for the email** (passive — the rest of the workflow happens after the email arrives, typically same day)

3. **Download the .zip** (1 min) when the email arrives. File is typically a `Basic_LinkedInDataExport_*.zip`.

4. **Extract the .zip locally** (1 min). It contains ~50 CSV files plus folders for Articles, Jobs, Verifications, Services Marketplace.

5. **Upload to Google Drive** (5 min)
   - Navigate to `LinkedIn Archive` folder in Google Drive
   - Create a new folder named `{MM01YY}` (e.g., `05012026`)
   - Upload all extracted files into the folder. Sub-folders (Articles, Jobs, Verifications, Services Marketplace) preserved as Google Drive sub-folders.
   - Convert CSVs to Google Sheets via right-click → Open with → Google Sheets → Save back. (Skills consume Google Sheets format; raw CSVs work but conversion is one-time per file and makes downstream reading reliable.)

6. **Verify upload** (1 min)
   - Open the Shares sheet; confirm the most-recent row is from within the last 24-48 hours
   - Open the Connections sheet; confirm the row count matches the LinkedIn UI's "X connections" badge ±5

## What's IN the archive (high-value files)

These are the files the audit and quarterly review consume:

| File | Direction | Columns | Used for |
|---|---|---|---|
| **Shares** | Outbound (Riché's posts) | Date, ShareLink, ShareCommentary, MediaUrl, Visibility | Posting cadence per week; ShareCommentary length distribution; MediaUrl frequency (carousel/image/video usage) |
| **Comments** | Outbound (Riché's comments) | Date, Link, Message | Strategic commenting cadence; Message length as substance proxy |
| **Reactions** | Outbound (Riché's reactions given) | Date, Type (LIKE/PRAISE/EMPATHY/...), Link | Engagement-given count; Link cross-ref to target accounts in `corpus/growth/target-accounts/linkedin.yaml` |
| **InstantReposts** | Outbound (Riché's reshares) | Date, ShareLink | Reshare cadence; what's being amplified |
| **Connections** | State (current connection set) | Connected On, ... | Total count = follower-equivalent; rows with Connected On in window = net new connections |
| **Articles** (folder) | Outbound (Riché's LinkedIn-articles) | Folder of HTML files | Long-form publishing cadence (less frequent than posts) |
| **Member_Follows** | State (who Riché follows) | Date, profile URL | Following pattern; cross-ref to target accounts |
| **Company Follows** | State (companies Riché follows) | Followed on, company name | Company-level tracking |
| **Invitations** | Outbound + inbound | Direction, Date, ... | Invite cadence; cold-vs-warm patterns |
| **Profile Summary** | State | Aggregate profile stats | Profile-side baseline |

## What's NOT in the archive

The LinkedIn data export is structurally outbound-and-state. It does NOT contain:

- ❌ **Engagement received on Riché's posts** (likes/reactions received, comments received, impressions, click-throughs)
- ❌ **Profile views** (unless on LinkedIn Premium with view-tracking enabled, separate workflow)
- ❌ **Engagement rate** per post
- ❌ **Search appearances**
- ❌ **Reach/audience data**

For these, see `corpus/growth/channels/linkedin-premium-tracking.md` for the LinkedIn Premium workflow that supplements the archive with profile-view data. Engagement received per-post is genuinely unavailable without LinkedIn Marketing Developer Platform access (enterprise tier).

For the quarterly review, this is by design: outbound activity is the leading indicator (per `corpus/growth/metrics/leading-vs-lagging.md`); engagement received is the lagging indicator. Optimizing for outbound activity that fits Riché's strategy is what's controllable.

## How the archive gets consumed

**By `rz-website-audit` (weekly):**
The weekly audit reads only the most-recent monthly archive. For LinkedIn-related dimensions (T-engagement, B-voice, K-content cluster checks), it uses the Shares sheet to verify cadence held this week and to surface this week's posts for voice/dimension scoring.

**By `rz-quarterly-review` (quarterly):**
The quarterly review reads 4 monthly archives covering the quarter. For Q2 2026 review (early July 2026): pulls 04012026, 05012026, 06012026, 07012026. The first 3 cover April-June; the 4th gives the most recent connection-count snapshot.

**By `rz-self-improve` (occasional):**
When patterns emerge in voice or content drift, self-improve reads the Shares ShareCommentary text across recent archives to surface the drift evidence.

## When to skip / accept gaps

- **Travel month:** if the monthly export was missed, the next month's archive contains everything anyway (LinkedIn keeps the full history, not delta). Just upload as `{MM01YY}` for the month you're catching up on.
- **No new activity month:** still upload the archive even if Shares are zero. The skills check for missing archives differently than zero-activity archives.
- **LinkedIn export delays:** if the email takes >24 hours, defer the upload to the next day. Don't delay the rest of the Sunday review.

## Examples
1. **Standard monthly export.** First Sunday of June 2026, ~10 minutes. Riché requests the export Sunday morning, the email arrives 23 minutes later, downloads + extracts + uploads to `LinkedIn Archive > 06012026/`. Verifies Shares contains rows through May 31. Done.
2. **Catch-up after travel.** Riché missed April. In May, he runs the workflow normally for May (`05012026`), then runs it again immediately for April-data-only (he can't request a backdated export, but the May export contains April data too, so he doesn't need to). The April folder gets the same May-exported files but in a folder named `04012026`. Note: this is suboptimal but acceptable; the consumer skills filter by the Date column inside each file, not by the folder name.
3. **Failed verification.** Riché uploads the May archive but the Connections sheet shows 1,180 rows when LinkedIn UI says "1,247 connections." The export failed mid-way. He re-requests, re-uploads. Notes the issue in the next quarterly review notes.

## Related entries
- `corpus/growth/playbook/admin-tracking.md` — the broader monthly-Sunday admin block
- `corpus/growth/playbook/strategic-commenting.md` — the daily activity Riché is doing that the Comments file captures
- `corpus/growth/channels/linkedin-cadence.md` — the cadence the Shares file verifies
- `corpus/growth/channels/linkedin-premium-tracking.md` — supplements the archive with profile-view data
- `corpus/growth/metrics/segment-proxies-rollup.md` — uses outbound activity as leading indicators
- `corpus/growth/databases/quarterly-reviews-schema.md` — Quarterly Reviews DB consumes the per-quarter rollup

## Anti-patterns
- Renaming folders. Skills find archives via the `{MM01YY}` title pattern; renames break the search.
- Skipping months thinking "I'll do two next month." The export gives full history each time, so you can recover, but the discipline cost of the missed month compounds. Plus the consumer skills look for monthly folders; they degrade gracefully on missing folders but report the gap.
- Storing CSVs without converting to Google Sheets. Possible but increases skill-side parsing complexity. Convert once at upload time.
- Using a different folder convention. The `LinkedIn Archive > {MM01YY}` path is hard-referenced in `rz-website-audit` and `rz-quarterly-review`. Changes require updating both skills.
- Treating the archive as a substitute for engagement-received metrics. It's not in the data; don't synthesize fake numbers.
