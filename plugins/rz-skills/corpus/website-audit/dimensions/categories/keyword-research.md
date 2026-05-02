---
name: Keyword Research Category
domain: website-audit
source_skill: website-audit
entry_type: rule
length_target: 600-900
related: [corpus/growth/seo/free-stack-overview.md, corpus/growth/seo/keyword-planner-monthly.md, corpus/growth/seo/serp-review-protocol.md]
---

# Keyword Research Category

## What it is
Five Keyword Research checks (K1–K5) that surface targeting opportunities and gaps using the free-stack approach (GSC + Google Keyword Planner + manual SERP review). Together they detect: stale Keyword Planner data, targeted-but-invisible keywords, SERP gaps on priority Context Layer terms, topic cluster gaps, and search-intent mismatches on ranking pages.

**The five checks:**

- **K1 Stale Keyword Planner data.** Any Target Keyword with status `Targeting` or `Researching` has `Volume Last Updated` older than 30 days. Severity: P2 individually; aggregates to P1 if more than 10 keywords are stale.
- **K2 New ranking opportunity (targeted but invisible).** Keyword has status `Targeting` AND monthly volume ≥100 AND zero GSC impressions in the last 28 days. Severity: P1 if Context Layer; P2 otherwise.
- **K3 SERP gap on priority Context Layer term.** For top 5 priority terms by `domain_weight × volume`, manual SERP review reveals competitor content in the top 10 but no richezamor.com page in the top 20. Severity: P1 for top-3 priority terms; P2 otherwise.
- **K4 Topic cluster gap.** Any of the 7 priority Context Layer topics has zero published /thinking articles tagged to it. Severity: P1 (this is the moat).
- **K5 Search intent mismatch on ranking page.** Keyword has status `Ranking`, a populated Target Page URL, AND the page's dominant content type doesn't match the typical SERP intent. Severity: P1.

**Sources:** Notion Target Keywords DB; GSC data via Ahrefs Webmaster Tools; SERP review via `web_search` + `web_fetch`; Content Topics DB query for K4.

## Why it matters
Keyword research without a paid SEO tool is workable at richezamor.com's stage, but it requires discipline. The free stack (Keyword Planner, GSC, manual SERP review) provides full keyword research capability if used consistently. The five K-checks are what enforce that consistency — they catch the discipline failures (stale data, neglected opportunities, missing content) before they accumulate into a strategic problem.

K4 is the highest-leverage check in this category. The 7 priority Context Layer topics define Riché's moat. Any cluster with zero articles is a strategic gap, not just a tactical one — the audit treats it as P1 and surfaces it for content queue planning.

K1 is the lowest-leverage but most frequent. Stale data accumulates if the monthly Keyword Planner refresh slips. The check at P2 individually escalates to P1 when 10+ keywords are stale, which is the threshold where the data quality starts compromising the other K-checks.

## How to apply
The category runs in 7 substeps (per Step 2k of the audit methodology):

1. **Read the Target Keywords DB.** Filter to status `Researching`, `Targeting`, or `Ranking`.
2. **Cross-reference with GSC.** For each keyword, look up the term in this run's GSC data. Record current position; null if not ranking. Update each row in Notion with current position and last-checked date.
3. **Flag stale volume data.** Any keyword with `Volume Last Updated` older than 30 days and status `Targeting` or `Researching` triggers K1.
4. **Identify ranking opportunities.** Keywords with monthly volume ≥100 and status `Targeting` that have no GSC impressions in the last 28 days trigger K2.
5. **Run SERP review on top N priority terms.** Sort the DB by `domain_weight × monthly_volume` (Context Layer = 2.5, PM = 1.5, Leadership = 1.0). For the top 5 terms, follow the SERP review protocol.
6. **Topic cluster check.** For each of the 7 priority Context Layer topics, count published /thinking articles tagged to that topic. Trigger K4 for any cluster with zero articles.
7. **Intent alignment check.** For keywords with status `Ranking` and a populated `Target Page URL`, fetch the page and compare its dominant content type against typical SERP results.

Fix patterns:

- **K1:** monthly Keyword Planner refresh by Riché (~15 min)
- **K2:** either no targeted page exists yet (action: draft an article), or the targeted page isn't surfacing (action: improve internal links, add the term to title/H1/first paragraph, ensure topical depth)
- **K3:** file a content brief in Linear with target keyword, intent type, competitor pattern summary, recommended differentiating angle, target word count
- **K4:** add a topic-cluster article to the Content Queue with format = Wednesday Deep Dive
- **K5:** either refactor the ranking page to match intent, or redirect/canonicalize to a better-fit page

If `TARGET_KEYWORDS_DB_ID` returns zero rows or the database is unconfigured, log `target_keywords_empty = true` in Run notes and skip K1–K5 for this run.

## Examples
1. **K1 fires with aggregated P1.** 14 keywords stale; the monthly refresh has slipped to 47 days. Fix: schedule the next Keyword Planner session this week.
2. **K2 fires with P1.** "context engineering" has status `Targeting`, monthly volume 1,200, zero GSC impressions in 28 days. No targeted page exists. Fix: draft a /thinking article specifically targeting the term.
3. **K3 fires with P1.** SERP review of "AI context layer" reveals 4 competitor articles in the top 10 (3 Medium aggregators, 1 academic paper). richezamor.com is not in the top 20. Fix: file content brief — informational intent, competitor articles average 1,500 words, recommended angle is the Riché-specific 5-step framework with the live demo as proof.
4. **K4 fires with P1.** The "Active Generation Pipeline" topic cluster has zero published articles. The cluster covers the 5-step process — curate, synthesize, consolidate, prioritize, store intelligently. Fix: add a Wednesday Deep Dive on the pipeline to the Content Queue.
5. **K5 fires with P1.** "context layer vs RAG" ranks at position 8; target page is a personal essay (narrative content type). Top SERP results are all comparison tables. Fix: refactor the ranking page to lead with a comparison table; keep the essay narrative as the explanatory section after.

## Related entries
- `corpus/growth/seo/free-stack-overview.md` — the methodology
- `corpus/growth/seo/keyword-planner-monthly.md` — the K1 fix workflow
- `corpus/growth/seo/serp-review-protocol.md` — the K3 protocol
- `corpus/growth/seo/topic-clusters.md` — the K4 cluster definitions
- `corpus/growth/seo/target-keywords-schema.md` — the Notion DB structure

## Anti-patterns
- Filing Linear tasks for every K1 trigger. Stale data is a process issue, not a per-keyword issue. Aggregate.
- Treating K3 as "we need to outrank everyone." Sometimes a SERP gap is acceptable (the term isn't aligned with positioning); the audit surfaces the gap, Riché decides whether to pursue.
