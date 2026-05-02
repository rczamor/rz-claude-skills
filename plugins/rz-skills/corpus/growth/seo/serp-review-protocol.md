---
name: SERP Review Protocol
domain: growth
source_skill: growth-marketing
entry_type: pattern
length_target: 400-700
related: [corpus/growth/seo/free-stack-overview.md, corpus/growth/seo/topic-clusters.md, corpus/website-audit/dimensions/categories/keyword-research.md, corpus/growth/seo/target-keywords-schema.md]
---

# SERP Review Protocol

## What it is
The 5-step manual SERP review applied each week to the top `SERP_ANALYSIS_TOP_N` (= 5) priority terms in the Target Keywords DB. For each term it captures who is ranking, what format the SERP rewards, how fresh the winning content is, and how dense the competitive field is. The output drives K3 (SERP gap on priority Context Layer term) and informs whether richezamor.com can realistically rank.

| Step | Action | Tool |
|---|---|---|
| 1 | Sort the DB by `domain_weight × monthly_volume`, pick top 5 | Notion read |
| 2 | Run `web_search` for each term | web_search |
| 3 | Fetch the top 5 results | web_fetch (or Tavily fallback) |
| 4 | Capture per-result fields and classify SERP intent | structured note |
| 5 | Write findings back to the DB and the audit page | Notion write |

## Why it matters
SERP composition tells you whether richezamor.com can realistically rank, what format the audience expects, and whether to invest in long-form content or a different play entirely. A SERP dominated by aggregator sites and vendor blogs is a low-effort win; a SERP dominated by Lenny, Aakash, and Shreyas is a five-quarter campaign. Without this protocol, K3 fires generate "we should target X" recommendations that ignore the actual difficulty.

The freshness check is what turns a "we are losing" finding into a "we can win in 90 days" finding. A SERP full of 2022 articles is a refresh-driven opportunity; a SERP refreshed last month by an authority site is a different problem entirely.

## How to apply

**Domain weight constants:** Context Layer = 2.5, PM = 1.5, Leadership = 1.0. Sort the DB filtered to status `Researching`, `Targeting`, or `Ranking` by `domain_weight × monthly_volume` descending. Take the top 5.

**Per-term fields to capture for each of the top 5 SERP results:**

- Domain (e.g., lennysnewsletter.com, medium.com)
- Content type (article / video / docs / aggregator / forum)
- Word count (rough: under 800, 800–2000, over 2000)
- Freshness (publish or update date; older than 18 months is the staleness threshold)
- Schema present (yes/no based on a quick view-source check)
- Key entities mentioned (named people, products, frameworks)

**Classify the SERP:**

- **Intent:** informational, commercial, navigational, or mixed.
- **Competitor density:** low if fewer than 2 thought leaders are ranking, medium if 2-3, high if 4+. Thought leaders are tracked in the Competitors DB at Tier `Aspirational` or `Direct`.

**Output:** write findings into this run's Weekly Audits Notion page under a "SERP Review" section. Update Last Checked and Current Position on each of the 5 keywords' rows in the Target Keywords DB.

If `web_fetch` is blocked on a result (paywall, anti-bot), fall back to Tavily extract. If both fail, capture only the search snippet and flag `fetch_failed = true` in the notes.

## Examples
1. **Low-density SERP, refresh opportunity.** Term: "what is a context layer in AI products." Top 5: 3 Medium aggregators with 600-word posts from 2023, 1 vendor blog from late 2024, 1 academic preprint. Density: low. Intent: informational. Freshness: stale across the field. Recommendation: K3 fires P1; file a content brief targeting the term with a 1,800-word /thinking article that names richezamor.com's 5-step framework explicitly.
2. **High-density SERP, defer.** Term: "product management AI." Top 5: Lenny, Aakash, Shreyas, Reforge, plus one Medium aggregator. Density: high. Intent: mixed. Recommendation: do not target. K3 logs the gap as P2 with note "high-authority field; revisit at DR 30+."
3. **Mixed SERP, niche win.** Term: "evaluating context retrieval." Top 5: 2 academic papers, 1 vendor docs page, 2 Stack Overflow threads. Density: low (no thought leaders). Intent: informational. Freshness: docs page is 8 months old. Recommendation: K3 fires P1; the field is technical and Riché's Helm Labs eval framework piece would slot in.

## Related entries
- `corpus/growth/seo/free-stack-overview.md`. The broader free-stack methodology
- `corpus/growth/seo/topic-clusters.md`. Used to score domain weight
- `corpus/website-audit/dimensions/categories/keyword-research.md`. K3 fire criteria and severity rules
- `corpus/growth/seo/target-keywords-schema.md`. The DB the protocol reads and writes

## Anti-patterns
- Reviewing every keyword. Five is the cap; review discipline matters more than coverage.
- Skipping the freshness check. A 2022 SERP looks competitive on the surface but is a refresh-driven opportunity in disguise.
- Treating SERP density as the only signal. A medium-density SERP with one weak Lenny post can still be a win if Riché's angle differentiates.
