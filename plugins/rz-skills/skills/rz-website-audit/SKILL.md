---
name: rz-website-audit
description: >
  Use when running the weekly diagnostic of richezamor.com or when fired by the Sunday 8pm America/New_York cron. Trigger phrases: "/rz-website-audit," "run the website audit," "weekly site review," "weekly site QA," "audit richezamor.com," "website scorecard." Read-only on Vercel and Google Search Console; never modifies the site itself.
---

# Website Audit (Riché Zamor)

You run a 6-step weekly diagnostic of richezamor.com against 22 scoring dimensions, assign severity, write a structured report into Notion, file up to 5 Linear tasks, and post a Slack headline. The skill is diagnostic only. It does not modify the website. Content fixes route through `rz-content-optimize` and `rz-draft-content`; brand voice fixes route through `rz-copywriting`; OG image regeneration routes through `rz-graphic-design`.

## Configuration constants

```
WEBSITE_DOMAIN              = richezamor.com
MAX_WEEKLY_TASKS            = 5
RUN_TIMEZONE                = America/New_York
VERCEL_PROJECT_ID           = prj_qtI2I2fvlAH5qeTnc4EVW52stG9t
VERCEL_TEAM_ID              = team_G5bsJ43GY5r9RqMjT4iEYO5c
LINEAR_TEAM_ID              = 72132418-b477-4450-a30a-77391d5cfc47   (Riche Zamor team)
LINEAR_PROJECT_ID           = 085484ef-b523-4142-bce2-7f9a23a05fa1   (Brand project)
LINEAR_ASSIGNEE_ID          = 646e8aef-65f5-47de-ba40-4f2ad99bbc15   (Riché)
NOTION_PARENT_ID            = 333ac0ea4f658086bcafcd3f53299b89       (Personal Brand)
NOTION_AUDIT_DB_ID          = 6d5673aef5a94f17867602778949f869
NOTION_AUDIT_DS_ID          = 889093b4-fb7d-4db5-a871-19e7bbe159fd
TARGET_KEYWORDS_DB_ID       = f5521fe72dec42c1808555fbac2d0d62
TARGET_KEYWORDS_DS_ID       = df1d8efa-ff31-4b18-beb5-0998e9dd9bc2
COMPETITORS_DB_ID           = c99eaa6d2e7448f0859ce6feba22a3ac
COMPETITORS_DS_ID           = 596ee7d6-46d8-464a-adfc-489576de0052
CONTENT_STRATEGY_PAGE_ID    = 333ac0ea4f6581518651d730d706e017
CONTENT_TOPICS_DB_ID        = 2c224f29490d44f99e7b58cb2e377086
SLACK_CHANNEL               = #brand
DOMAIN_BALANCE_TARGET       = 50% Context Layer / 30% PM / 20% Leadership
KEYWORD_PLANNER_STALE_DAYS  = 30
SERP_ANALYSIS_TOP_N         = 5
QUARTERLY_REBASELINE_MONTHS = January, April, July, October (first Sunday of)
```

## Cross-skill dependencies (read these first)

The audit does not own SEO methodology or brand voice. It LEVERAGES the canonical sources owned by other skills.

**SEO and keyword research are owned by `rz-growth-marketing`.** Pull from `corpus/growth/seo/` for keyword research methodology, SERP review protocol, topic clusters, the monthly Keyword Planner workflow, and the Target Keywords DB schema. The audit's S1–S8 atomic dimensions and K1–K5 keyword-research category dimensions reference this corpus; they do NOT redefine SEO concepts.

**Brand voice is owned by `rz-copywriting`.** Pull from `corpus/voice/` for the fatal-fifteen AI-tells list, voice anti-patterns, terminology rules, and the 50/30/20 domain balance frame. The audit's B1–B5 brand checks are detection rules ON TOP of the voice canon; they do NOT redefine voice rules.

If a dimension entry's text contradicts these source-of-truth corpora, the source-of-truth corpora win. Surface the contradiction in `rz-self-improve` for cleanup.

## Load from corpus

The audit reads its scoring rules, methodology, and benchmarking protocols from `corpus/website-audit/`. SEO methodology and the Target Keywords DB schema load from `corpus/growth/seo/`. Voice rules load from `corpus/voice/`.

**Dimensions (22 total).** Each dimension has an entry that defines the trigger, severity, source, and fix pattern.

SEO (8 atomic). `corpus/website-audit/dimensions/seo/`:
- `s1-ranking-regression.md`. Tracked query dropped 3+ positions week-over-week
- `s2-low-ctr.md`. High impressions, CTR below 2%
- `s3-quick-wins.md`. Query ranking in positions 4–10 with ≥100 weekly impressions
- `s4-indexability.md`. Page should be indexed but is not
- `s5-metadata-completeness.md`. Title, meta, OG, canonical, Twitter card completeness
- `s6-structured-data.md`. JSON-LD presence and validity
- `s7-internal-linking.md`. Inbound/outbound internal link density per article
- `s8-backlink-loss.md`. Recent loss of external backlinks

AIO (7 atomic). `corpus/website-audit/dimensions/aio/`:
- `a1-citation-absence.md`. Site not cited for tracked AIO queries
- `a2-citation-rank-decline.md`. Citation position dropped vs prior run
- `a3-crawler-accessibility.md`. AI crawlers blocked or rate-limited
- `a4-js-only-content.md`. Content visible only after JS render
- `a5-quotability-density.md`. Extractable self-contained sentences per page
- `a6-entity-consistency.md`. Named entity coverage across articles
- `a7-ai-friendly-schema.md`. Schema types optimized for LLM ingestion

Category-level (7). `corpus/website-audit/dimensions/categories/`:
- `traffic-engagement.md`. Sessions, bounce, time-on-page rollups
- `usability.md`. Heuristic checks across nav, forms, content
- `design.md`. Type, color, spacing, OG image consistency
- `brand.md`. Voice, positioning, B1 brand drift (loads voice canon from `corpus/voice/`)
- `technical-qa.md`. Lighthouse, Core Web Vitals, build health
- `chatbot.md`. `/api/chat` health, eval probe, citation behavior
- `keyword-research.md`. K1–K5 checks (loads SEO methodology from `corpus/growth/seo/`)

**Methodology (6)**. `corpus/website-audit/methodology/`:
- `bootstrap.md`. Step 1 (read DBs, last audit, run ID generation)
- `parallel-data-collection.md`. Step 2 (GSC, technical QA, Lighthouse, chatbot probe)
- `severity-scoring.md`. Step 3 (P0/P1/P2 rules, traffic-light rollups)
- `report-assembly.md`. Step 5 (page body composition, sections, format)
- `task-issuance.md`. Step 6a (Linear task creation, MAX_WEEKLY_TASKS cap)
- `slack-notification.md`. Step 6b (one-line Slack post, traffic light, link)

**SEO methodology (5, owned by `rz-growth-marketing`)**. `corpus/growth/seo/`:
- `free-stack-overview.md`. GSC + Keyword Planner + manual SERP review methodology
- `keyword-planner-monthly.md`. Riché's monthly refresh workflow (~15 min)
- `serp-review-protocol.md`. 5-step SERP review for the top N priority terms
- `topic-clusters.md`. 7 priority Context Layer clusters
- `target-keywords-schema.md`. Target Keywords DB structure and lifecycle

**Voice canon (used by B1–B5, owned by `rz-copywriting`)**. `corpus/voice/`:
- The fatal-fifteen AI-tells series (`fatal-fifteen-01-...` through `fatal-fifteen-15-...`)
- Voice anti-patterns (em dashes, "navigate", "leverage" without object, etc.)
- Three-domain balance overview (50/30/20)
- Terminology rules (Context Layer vs context management system)

**Audit-owned databases (2)**. `corpus/website-audit/databases/`:
- `competitors-schema.md`. Competitors DB structure with Tier and Type
- `weekly-audits-schema.md`. Weekly Audits DB where each run is stored

**Competitor benchmarking (2)**. `corpus/website-audit/competitor-benchmarking/`:
- `read-protocol.md`. 6-step benchmarking run, read-then-write
- `what-gets-benchmarked.md`. Five categories captured for Direct + Aspirational tiers

## The 6 steps

### Step 1: Bootstrap

Per `corpus/website-audit/methodology/bootstrap.md`:

1. Generate `audit_run_id` (UUID; threaded into every artifact for traceability).
2. Read the Target Keywords DB (`TARGET_KEYWORDS_DB_ID`), filter status != Deprioritized.
3. Read the Competitors DB (`COMPETITORS_DB_ID`), all rows, group by Tier.
4. Read the most recent page in the Weekly Audits DB (`NOTION_AUDIT_DB_ID`) for delta context.
5. Read `CONTENT_STRATEGY_PAGE_ID` and the Content Topics DB (`CONTENT_TOPICS_DB_ID`) for K4 cluster coverage.
6. Capture in-memory: keyword list, competitor list, last audit summary, content cluster counts.

If any DB returns zero rows, log the empty state in Run notes and continue with the dimensions that don't depend on it.

### Step 2: Parallel data collection

Per `corpus/website-audit/methodology/parallel-data-collection.md`. Run all 11 sub-steps concurrently where possible.

- GSC pulls via Ahrefs MCP (`gsc-keywords`, `gsc-pages`, `gsc-performance-history`, `gsc-anonymous-queries`)
- Technical QA: Lighthouse against home + 3 article pages; Core Web Vitals from `web-analytics-stats`
- Vercel deployment health and build logs (read-only)
- Chatbot probe: 3 known-good queries against `/api/chat`; capture latency, error rate, citation accuracy
- AIO query set: run the 20-query set against AI Overviews / Perplexity / ChatGPT, capture citations
- SERP review: run `serp-review-protocol.md` on the top 5 priority terms
- Internal link graph: crawl from sitemap, build inbound/outbound counts per page
- Site fetches: home + each /thinking article for content inspection
- Schema check: view-source on home + sample articles, count distinct JSON-LD types
- Brand voice scan: sample 3 recent /thinking articles for voice drift against the Content Style Guide
- Competitor benchmark prep: read Competitors DB rows (deferred to Step 4 sub-loop)

### Step 3: Score the 22 dimensions

Walk every dimension entry. For each, evaluate the trigger condition against this run's data. When a trigger fires, capture the finding (page URL, metric, observation) and the dimension's defined severity.

The 8 SEO atomic and 7 AIO atomic dimensions are evaluated per-page and aggregate to category traffic lights. The 7 category-level dimensions evaluate via their own sub-checks defined in each category file.

Apply severity rules per `corpus/website-audit/methodology/severity-scoring.md`:

- **P0** if impact = 5 OR (impact ≥4 AND effort ≤3) OR site-breaking
- **P1** if impact ≥3 AND effort ≤4
- **P2** otherwise
- Dimension-level definitions override the impact/effort calculation when more specific (e.g., A3 is always P0)

Compute per-dimension traffic light: green if no P0 and ≤2 P1; yellow if 1 P0 OR 3+ P1; red if 2+ P0. Overall light is the worst dimension light.

### Step 4: Competitor benchmarking

Per `corpus/website-audit/competitor-benchmarking/read-protocol.md`. Sequence between dimension scoring and report assembly.

- Direct + Aspirational tiers: full benchmark per `what-gets-benchmarked.md` (Performance, Content ecosystem, SEO/AIO foundations, Distinctiveness, AI presence)
- Adjacent tier: lightweight check (URL alive, content shipped this week)
- Write back to each row in the Competitors DB
- Diff against prior values; surface deltas in Competitive Movements section of the report

### Step 5: Assemble report and write to Notion

Per `corpus/website-audit/methodology/report-assembly.md`.

Create a new page in the Weekly Audits DB:

- Title: `YYYY-MM-DD` (the run date)
- Properties: Date, Traffic Light, P0/P1/P2 counts, Notion Run ID, Linear Tasks Created (set in Step 6), Summary, Overall Dimension Lights
- Body: executive summary, traffic-light rollup table, Notable Movements, per-dimension findings, Competitive Movements, Action List

The Summary property is the one-sentence headline (≤140 chars) that mirrors the Slack post.

### Step 6: Issue tasks and post Slack

**6a. Linear tasks** per `corpus/website-audit/methodology/task-issuance.md`:

- Walk findings in priority order: all P0, then P1 by dimension, then P2 if budget remains.
- Cap at `MAX_WEEKLY_TASKS` (= 5). Findings beyond the cap roll into the Action List on the Notion page.
- Each task: `LINEAR_TEAM_ID`, `LINEAR_PROJECT_ID`, `LINEAR_ASSIGNEE_ID`, severity-derived priority, link back to the Notion audit page section.
- Write the task count back to the Weekly Audits page's `Linear Tasks Created` property.

**6b. Slack notification** per `corpus/website-audit/methodology/slack-notification.md`:

- Post to `SLACK_CHANNEL` (`#brand`)
- One line: traffic light emoji + Summary + link to the Weekly Audits Notion page
- Do NOT paste the full report body to Slack

## What this skill does NOT do

- Does not modify the website. Diagnoses only; fixes route to other skills.
- Does not auto-publish content fixes. Page-level SEO and AIO fixes for pages flagged as P0 / P1 route to `rz-content-optimize`.
- Does not own SEO methodology. The audit calls out from `corpus/growth/seo/`; canonical SEO knowledge lives with `rz-growth-marketing`.
- Does not own brand voice rules. The audit's B1–B5 detection sits on top of `corpus/voice/`; canonical voice lives with `rz-copywriting`.
- Does not run keyword discovery. New candidates come from the monthly Keyword Planner job (`corpus/growth/seo/keyword-planner-monthly.md`), which is Riché's manual session.
- Does not benchmark Adjacent-tier competitors in full. Adjacent gets lightweight checks only.
- Does not write to Google Search Console or Vercel. Read-only on both systems.
- Does not auto-deprioritize keywords. The 90-days-zero-impressions guardrail prevents silent deletes; deprioritization is a manual call by Riché.
- Does not retro-edit prior audit pages. Each run lives in its own dated page; the time series is append-only.

## Cross-skill connections

**Upstream (the audit reads from these for canonical knowledge):**

- `rz-growth-marketing`. Owns SEO. Audit reads `corpus/growth/seo/` for keyword research methodology, SERP review protocol, topic clusters, the monthly Keyword Planner workflow, and the Target Keywords DB schema. The audit's K1–K5 dimensions and S1–S8 atomic fires use these as source of truth.
- `rz-copywriting`. Owns brand voice. Audit reads `corpus/voice/` for the fatal-fifteen AI tells, voice anti-patterns, and the 50/30/20 domain balance frame. The audit's B1–B5 dimensions detect drift against this canon.

**Downstream (the audit hands off to these for fixes):**

- `rz-content-optimize`. Page-level SEO and AIO fixes flagged as P0 or P1 in S1, S2, S5, A1, A5, A7.
- `rz-copywriting`. Voice rewrites when B1 fires. Audit surfaces the offending lines; copywriting authors the replacement.
- `rz-graphic-design`. OG image regeneration when D5 fires.
- `rz-draft-content`. When an audit P0 or P1 surfaces a content gap (K3 or K4) that needs a new article.
- `rz-product-design`. When usability dimensions surface a flow change rather than a content change.
- `rz-self-improve`. Corpus updates when the audit reveals a dimension's trigger or severity rule needs refinement, or when SEO/voice canon drifts away from how the audit references it.

## Run outputs (summary)

Every successful run produces:

- One new page in the Weekly Audits Notion DB (titled `YYYY-MM-DD`)
- Updated rows in the Target Keywords DB (Current Position, Last Checked, status transitions)
- Updated rows in the Competitors DB (Lighthouse, schema, cadence, AI presence, Last Audited)
- Up to 5 Linear tasks under Brand project, assigned to Riché
- One Slack post to `#brand` with traffic light, summary, and Notion link

## Failure modes and recovery

- **GSC pull fails.** Skip S1, S2, S3, S8 for this run; log `gsc_unavailable = true`. Other dimensions still score.
- **Chatbot probe fails.** Q-dimension fires P0 if /api/chat returns 5xx; P1 if eval queries miss expected citations.
- **Lighthouse run fails.** Skip Q-dimension Performance metrics for this run; degrade to a category-level note.
- **Notion write fails.** Retry once; if still failing, dump the assembled report to a local file with `audit_run_id` in the filename and surface the failure in Slack.
- **Linear task creation fails.** Continue with remaining tasks; log the failure in the Notion page Action List.
- **Slack post fails.** Final step; if it fails the audit is still complete in Notion. Surface the Slack failure in the run notes.

## Quarterly rebaseline (first Sunday of January, April, July, October)

On `QUARTERLY_REBASELINE_MONTHS` runs, add a retrospective pass:

1. Query the last 13 audit pages (one quarter).
2. List dimensions that were red 3+ times; surface for triage.
3. List dimensions that were green 13/13; consider lightening their cadence.
4. Re-validate the 7 priority topic clusters; adjust any that have drifted.
5. Re-tier 1–2 competitor rows if positioning has shifted.

The quarterly pass extends a normal run; it does not replace one. Allocate ~30 extra minutes for the retrospective.
