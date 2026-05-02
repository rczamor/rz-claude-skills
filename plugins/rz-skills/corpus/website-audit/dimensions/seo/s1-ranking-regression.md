---
name: S1 — Organic Ranking Regression
domain: website-audit
source_skill: website-audit
entry_type: rule
length_target: 300-800
related: [corpus/website-audit/methodology/severity-scoring.md, corpus/website-audit/dimensions/seo/s2-low-ctr.md, corpus/website-audit/dimensions/seo/s3-quick-wins.md]
---

# S1 — Organic Ranking Regression

## What it is
A tracked query has dropped three or more positions week-over-week in Google Search Console data. The check runs against the GSC keyword history (28-day window with weekly comparison), flags any query that has lost meaningful ground, and routes the finding to either P0, P1, or P2 based on the query's traffic profile.

**Trigger:** any tracked query drops ≥3 positions WoW.

**Severity:**
- P0 if the query is in the top 10 by impressions (these are the queries actually moving traffic)
- P1 if positions 11–25 (recoverable, still relevant)
- P2 otherwise (low priority, monitor only)

**Source:** `Ahrefs:gsc-keywords` + `Ahrefs:gsc-positions-history`.

## Why it matters
A 3-position drop is the threshold where a query stops generating meaningful clicks. Position 4 to position 7 is roughly a 50% click-through-rate cut. Position 8 to position 11 is the falling-off-page-one cliff. Catching these regressions in the same week they happen is the difference between a recoverable refresh and a fully cooled keyword that takes months to rebuild.

The diagnostic value is also high. A regression on a single query is usually content drift or a competitor move; a regression across multiple queries on the same page is usually a technical issue (indexability, internal-link decay, schema break) that will keep getting worse until investigated.

## How to apply
- Pull the top 20 queries by impressions for the last 7 days, with WoW position deltas.
- For any query with a delta ≤ -3, capture: current position, previous position, query, ranking page URL, impressions, CTR, click delta.
- Group by ranking page. If three or more queries on the same page regressed simultaneously, escalate to P0 regardless of individual query rank — this is a page-level issue, not a query-level one.
- Inspect the page: content drift since last quarter, technical issues (broken canonical, 4xx anywhere in the path), competitor moves (run a SERP review per `corpus/growth/seo/serp-review-protocol.md`).
- Fix patterns: refresh content (add 200-400 words of substance), strengthen internal links from higher-authority pages, fix any technical issues, improve schema.

## Examples
1. **Single-query regression on a /thinking article.** "context layer architecture" drops from position 6 to position 11 in one week. Page has been stable for 60 days. SERP review reveals a new competitor article published last week with deeper coverage. Fix: refresh the article with 300 words specifically on the missing sub-topic; update the publish date to signal recency.
2. **Page-level regression cluster.** Three queries pointing to /thesis all drop 4+ positions simultaneously. Investigation reveals a broken internal link from /work that was sending authority to /thesis. Fix: restore the internal link; resubmit page in GSC.
3. **False positive caught.** A query drops from position 8 to position 14, but impressions are up 30% — Google is showing the page for a broader query set. Not a regression; a query-distribution shift. Note in audit, no Linear task.

## Related entries
- `corpus/website-audit/methodology/severity-scoring.md` — how P0/P1/P2 thresholds work
- `corpus/website-audit/dimensions/seo/s2-low-ctr.md` — sibling check for impression-but-no-click pages
- `corpus/website-audit/dimensions/seo/s3-quick-wins.md` — the inverse opportunity (positions 4-10 with traction)
- `corpus/growth/seo/serp-review-protocol.md` — how to run the SERP review when a regression is competitor-driven

## Anti-patterns
- Treating every position drop as actionable. Position fluctuations of 1-2 are noise; don't file Linear tasks for every wobble.
- Fixing the page without investigating the cause. A refresh that doesn't address why the regression happened often makes things worse — Google sees thrash, not improvement.
