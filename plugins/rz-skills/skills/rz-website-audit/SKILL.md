---
name: rz-website-audit
description: >
  Use when running the weekly diagnostic of richezamor.com or when fired by the Sunday 8pm America/New_York cron. Trigger phrases: "/rz-website-audit," "run the website audit," "weekly site review," "weekly site QA," "audit richezamor.com," "website scorecard." Read-only on Vercel and Google Search Console; never modifies the site itself.
---

# Website Audit (Riché Zamor)

A 6-step weekly diagnostic of richezamor.com against 22 scoring dimensions. Assigns severity, writes a structured Notion report, files up to 5 Linear tasks, and posts a Slack headline. Diagnostic only; fixes route to `rz-content-optimize`, `rz-draft-content`, `rz-copywriting`, and `rz-graphic-design`.

## Quick Reference

| Situation | Load | Notes |
|---|---|---|
| Dimension lookup | `corpus/website-audit/dimensions/{seo,aio,categories}/` | 22 entries; trigger, severity, source, fix pattern |
| Severity score | `corpus/website-audit/methodology/severity-scoring.md` | P0/P1/P2 rules; do not guess |
| Competitor benchmark | `corpus/website-audit/competitor-benchmarking/` | Tier discipline: Direct + Aspirational full, Adjacent lightweight |
| Report assembly | `references/step-5-report-assembly.md` | Dated page, properties, body sections, Summary headline |
| Slack post | `references/step-6-task-issuance-and-slack.md` | One-line headline plus link only; never the full body |

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

- `corpus/website-audit/dimensions/` (22 entries: 8 SEO atomic in `seo/`, 7 AIO atomic in `aio/`, 7 category-level in `categories/`). Each defines trigger, severity, source, fix pattern.
- `corpus/website-audit/methodology/` (6 files: bootstrap, parallel data collection, severity scoring, report assembly, task issuance, Slack notification).
- `corpus/growth/seo/` (5 files, owned by `rz-growth-marketing`): free-stack, Keyword Planner, SERP review, topic clusters, Target Keywords schema.
- `corpus/voice/` (owned by `rz-copywriting`): fatal-fifteen AI-tells, anti-patterns, three-domain balance, terminology.
- `corpus/website-audit/databases/` (competitors, weekly audits schemas) and `corpus/website-audit/competitor-benchmarking/` (read protocol, what-gets-benchmarked).

## The 6 steps

1. **Bootstrap.** Generate run ID; read Target Keywords, Competitors, last audit, content strategy. See [references/step-1-bootstrap.md](references/step-1-bootstrap.md).
2. **Parallel data collection.** 11 concurrent sub-steps (GSC, Lighthouse, Vercel, chatbot, AIO, SERP, links, fetches, schema, voice, competitors). See [references/step-2-parallel-data-collection.md](references/step-2-parallel-data-collection.md).
3. **Score the 22 dimensions.** Evaluate triggers, assign P0/P1/P2, compute traffic lights. See [references/step-3-dimension-scoring.md](references/step-3-dimension-scoring.md).
4. **Competitor benchmarking.** Full benchmark for Direct + Aspirational; lightweight for Adjacent. Write back and diff. See [references/step-4-competitor-benchmarking.md](references/step-4-competitor-benchmarking.md).
5. **Assemble report.** Create a dated page in Weekly Audits DB with properties, body sections, and a Summary headline. See [references/step-5-report-assembly.md](references/step-5-report-assembly.md).
6. **Issue tasks and post Slack.** Up to `MAX_WEEKLY_TASKS` Linear tasks in priority order, then a one-line `#brand` post. See [references/step-6-task-issuance-and-slack.md](references/step-6-task-issuance-and-slack.md).

## What this skill does NOT do

- Does not modify the website. Diagnoses only; fixes route to other skills.
- Does not auto-publish content fixes. P0/P1 page-level SEO and AIO fixes route to `rz-content-optimize`.
- Does not own SEO methodology. Canonical SEO lives with `rz-growth-marketing` in `corpus/growth/seo/`.
- Does not own brand voice rules. Canonical voice lives with `rz-copywriting` in `corpus/voice/`.
- Does not run keyword discovery. New candidates come from the monthly Keyword Planner job (Riché's manual session).
- Does not benchmark Adjacent-tier competitors in full. Adjacent gets lightweight checks only.
- Does not write to Google Search Console or Vercel. Read-only on both systems.
- Does not auto-deprioritize keywords. The 90-days-zero-impressions guardrail prevents silent deletes; deprioritization is a manual call by Riché.
- Does not retro-edit prior audit pages. Each run lives in its own dated page; the time series is append-only.

## Common Mistakes

| Mistake | What goes wrong | Fix |
|---|---|---|
| Auto-deprioritizing keywords before 90 days of zero impressions | Silent deletes erode the keyword set Riché has been building | Honor the 90-days-zero-impressions guardrail; deprioritization is a manual call |
| Posting full audit body to Slack | Spams `#brand`; buries the headline | Slack gets one line plus the Notion link, nothing more |
| Creating Notion page before audit completes | Partial pages pollute the time series | Assemble the full report, then create the dated page once |
| Benchmarking every competitor every week | Burns time on Adjacent tier that does not move the needle | Direct + Aspirational get full; Adjacent gets lightweight only |
| Letting overall traffic light drift to green by ignoring small issues | Aggregated health hides accumulating P2s | Roll P2 counts up into the headline so small issues stay visible |

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

## Scripts

Deterministic logic lives in `scripts/`. Prefer these over reimplementing in prose.

- `scripts/severity_score.py` computes P0/P1/P2 per finding and the per-dimension and overall traffic lights from a JSON list of findings. Implements the rules in `corpus/website-audit/methodology/severity-scoring.md` exactly. Run `--self-test` to verify against the canonical examples.
- `scripts/run_lighthouse.sh` runs Lighthouse against a URL on mobile profile (override with `--form-factor desktop`) and emits the audit-relevant subset as one-line JSON: scores (performance, accessibility, best-practices, SEO) plus Core Web Vitals (LCP, INP, CLS, TTFB). Pipe to `severity_score.py` for the Q-dimension fire decisions.

## Run outputs

Every successful run produces: one dated page in the Weekly Audits DB, updated rows in Target Keywords and Competitors DBs, up to 5 Linear tasks, and one `#brand` Slack post.

## Failure modes and recovery

Common failures (GSC, chatbot, Lighthouse, Notion, Linear, Slack) each have a defined skip-or-degrade path so the run still completes. See [references/failure-modes.md](references/failure-modes.md) for the per-system rules.

## Quarterly rebaseline (first Sunday of January, April, July, October)

On `QUARTERLY_REBASELINE_MONTHS` runs, extend the normal run with a retrospective pass over the last quarter of audits, topic clusters, and competitor tiers. See [references/quarterly-rebaseline.md](references/quarterly-rebaseline.md) for the 5-step retrospective.
