---
name: Free-Stack Keyword Research Overview
domain: growth
source_skill: growth-marketing
entry_type: framework
length_target: 600-900
related: [corpus/growth/seo/keyword-planner-monthly.md, corpus/growth/seo/serp-review-protocol.md, corpus/growth/seo/topic-clusters.md, corpus/growth/seo/target-keywords-schema.md]
---

# Free-Stack Keyword Research Overview

## What it is
A keyword research methodology that uses three free sources together: Google Search Console (own-domain ranking data via Ahrefs Webmaster Tools free tier), Google Keyword Planner (search volume and competition for any keyword), and manual SERP review (`web_search` + `web_fetch` to inspect what's ranking for a query). Together, they replace the keyword-research dimension of a paid SEO tool ($30-50/month tools like Mangools, Semrush, or Ahrefs proper) at zero cost.

| Source | What it provides | Cost | Refresh cadence |
|---|---|---|---|
| Google Search Console (via Ahrefs Webmaster Tools) | Real ranking data, impressions, CTR, position, anonymous queries | $0 | Weekly (auto, via the audit) |
| Google Keyword Planner | Monthly search volume, competition level, related terms | $0 (Ads account required, no spend needed) | Monthly (manual by Riché) |
| Manual SERP review | Competitor coverage, content type, freshness, intent signals | $0 | Weekly on top 5 priority terms |

## Why it matters
At richezamor.com's stage and cadence (3-5 /thinking articles per month), the manual monthly Keyword Planner refresh costs ~15 minutes and the automated GSC + SERP review costs nothing in operator time. The free stack gives full keyword research capability — volumes, competition, related terms, SERP analysis, ranking data — without a monthly subscription.

The roles are complementary, not redundant: GSC tells you what you already rank for; Keyword Planner tells you what's worth targeting; SERP review tells you what the winning page looks like. Each source answers a different question. Together, they cover the full keyword research workflow.

The build-vs-buy decision flips when content cadence exceeds ~15 articles per month or when Riché invests in outbound SEO channels beyond LinkedIn. Until then, the free stack is sufficient and the manual monthly refresh is the right tradeoff.

## How to apply

**Skill responsibility (every weekly audit run):**

1. Read the Target Keywords DB (filter to status `Researching`, `Targeting`, `Ranking`)
2. Cross-reference each keyword with current GSC data; update each row's `Current Position` and `Last Checked`
3. Flag stale Keyword Planner data (K1)
4. Identify new ranking opportunities (K2)
5. Run SERP review on top 5 priority terms (K3)
6. Check topic cluster coverage (K4)
7. Check intent alignment on ranking pages (K5)

**Riché responsibility (monthly, ~15 minutes):**

The monthly Keyword Planner session has two jobs (per `corpus/growth/seo/keyword-planner-monthly.md`):

- **Job 1 — Refresh volumes:** paste current Target Keywords list, export volumes, update Notion
- **Job 2 — Discover new keywords:** seed-search expansion to surface 5-15 new candidate keywords

**Riché responsibility (ad hoc, when content ships):**

- Update `Target Page URL` on the keyword the article targets
- Move status `Targeting` → `Ranking` once GSC shows top-50 placement

## The 20-query AIO set composition

The audit also uses an AIO query set for citation tracking (separate from but related to the Target Keywords DB):

| Slots | Source | Rationale |
|---|---|---|
| 12 | Top GSC queries by impressions, last 28 days | Tracks citability against queries the audience already searches |
| 8 | Keywords from the last 7 Daily Briefings | Tracks citability against forward-looking topics Riché is pushing into |

The 12 GSC queries are filtered to maintain approximate domain balance: 7 Context Layer queries (the moat dimension), 3 PM queries, 2 Leadership queries. If GSC doesn't yield enough of a domain, backfill from Daily Briefings.

LLM queries are phrased the way a user would ask, not the way a keyword appears in GSC:
- `context layer` → `what is a context layer in AI products`
- `RAG architecture` → `what's the difference between RAG and context engineering`
- `agent memory systems` → `how do AI agents remember context across conversations`

## What good looks like over a quarter

The keyword research dimension should:

- Surface 8–12 K2 opportunities (terms targeted but not yet ranking)
- Surface 3–5 K3 SERP gaps (competitors winning where Riché has no page)
- Hold all 7 Context Layer topic clusters at ≥1 article (zero K4 fires)
- Keep K1 (stale data) at zero by maintaining the monthly refresh cadence
- Convert at least 4 keywords from `Targeting` → `Ranking`

If after 90 days K2 fires on the same 5 terms every week, the issue is content production, not the audit. Escalate to the Content Queue.

## Examples
1. **Standard weekly cycle.** Audit reads the Target Keywords DB (30 keywords), cross-references with GSC, finds 2 keywords newly in top 50 (status update to Ranking), 1 stale-volume warning (K1), 1 SERP gap on "AI context layer" (K3 P1).
2. **Monthly refresh by Riché.** Sunday afternoon, ~15 min. Pastes 30 keywords into Keyword Planner, updates volumes in Notion. Then runs 3 seed searches based on the week's Daily Briefings; adds 7 new keywords as Researching. K1 cleared.
3. **Build-vs-buy revisit.** After 18 months, Riché's content cadence has scaled to 12 articles/month and a new outbound SEO channel is launching. The free-stack manual refresh is taking 45 minutes/month and the SERP review on 5 terms isn't enough coverage. Time to reconsider Mangools or Ahrefs proper.

## Related entries
- `corpus/growth/seo/keyword-planner-monthly.md` — Riché's monthly workflow
- `corpus/growth/seo/serp-review-protocol.md` — the SERP review for K3
- `corpus/growth/seo/topic-clusters.md` — the 7 priority topics for K4
- `corpus/growth/seo/target-keywords-schema.md` — the Notion DB structure
- `corpus/website-audit/dimensions/categories/keyword-research.md` — the K1-K5 audit dimensions

## Anti-patterns
- Using paid keyword tool data alongside the free stack. The maintenance overhead of two sources of truth doesn't pay back at this content cadence.
- Skipping the monthly refresh because "the data is probably still close." Stale volumes silently corrupt K2 and the priority-score sort that drives K3.
