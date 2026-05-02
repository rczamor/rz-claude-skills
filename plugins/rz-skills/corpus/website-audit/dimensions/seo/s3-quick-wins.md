---
name: S3 — Quick-Win Queries
domain: website-audit
source_skill: website-audit
entry_type: rule
length_target: 300-800
related: [corpus/website-audit/dimensions/seo/s1-ranking-regression.md, corpus/website-audit/dimensions/seo/s7-internal-linking.md, corpus/growth/seo/serp-review-protocol.md]
---

# S3 — Quick-Win Queries

## What it is
A query that's ranking in positions 4–10 and earning at least 100 impressions per week. These are "almost there" queries: page-one ranking achieved, but not in the top three positions where most clicks happen. Quick wins because relatively small investments in the page can move it into the top three.

**Trigger:** query in positions 4–10 with ≥100 impressions per week.

**Severity:** P1 (this is an opportunity, not a regression — but high-leverage).

**Source:** `Ahrefs:gsc-keywords`.

## Why it matters
The CTR curve is steep at the top of page one. Position 1 averages roughly 30% CTR; position 4 averages 7%; position 10 averages 2%. Moving a query from position 6 to position 2 can quadruple its click count without earning a single new impression. Quick-win queries are the highest-leverage SEO work because the page is already qualified — it's ranking, it's relevant, it just needs a push.

Quick wins also compound. A page that moves from position 6 to position 2 sends stronger engagement signals (higher CTR, longer dwell time, lower bounce) which reinforces the ranking. The push, once made, tends to hold.

## How to apply
- Pull GSC keywords data for the last 7 days. Filter to queries in positions 4–10 with impressions ≥100.
- Sort by `impressions × (1 − current CTR ratio)` — proxy for "what's the ceiling." Prioritize queries with high impressions and current low CTR.
- For each, identify the ranking page. Run a SERP review for the query (per `corpus/growth/seo/serp-review-protocol.md`).
- The fix pattern is multi-pronged:
  - **Content depth.** Add 200-400 words of substance specifically on the angles the top-3 results cover that the ranking page doesn't.
  - **Internal links.** Add inbound internal links to the ranking page from higher-authority pages (home, /thesis, related /thinking articles).
  - **Schema.** Improve schema markup if the top-3 results have richer structured data.
  - **Title and H1.** Confirm the primary keyword is in the title and H1, in the first half, with strong intent match.
- File one Linear task per quick-win query, not per finding type. The fixes are all on the same page anyway.

## Examples
1. **"context engineering" at position 7.** Page has 400 weekly impressions, 1.2% CTR. SERP review reveals top 3 results all have a "vs RAG" comparison section the ranking page lacks. Fix: add a 350-word comparison section. Page moves to position 3 within 21 days.
2. **"AI product manager" at position 9.** Page has 200 weekly impressions, 0.8% CTR. Top results are heavyweight (Lenny, Marty Cagan). Fix is harder — link investments from /thesis and three /thinking articles, plus a content refresh focused on the AI-PM-specific angle. Slower but real movement: position 9 to position 6 in 30 days.
3. **"context architecture" at position 4.** Page has 700 weekly impressions, 5.2% CTR. Already converting; light optimization (sharper title, one new internal link) moves it to position 2.

## Related entries
- `corpus/website-audit/dimensions/seo/s1-ranking-regression.md` — the inverse signal (ranking lost)
- `corpus/website-audit/dimensions/seo/s7-internal-linking.md` — internal links are the most reliable lever
- `corpus/growth/seo/serp-review-protocol.md` — how to compare against top-3
- `corpus/growth/seo/free-stack-overview.md` — context for quick-win queries within the broader keyword strategy

## Anti-patterns
- Stuffing more keyword variants into the page hoping to boost it. Google's algorithm doesn't reward density; it rewards depth on the topic.
- Trying to move position 30 queries up to page one as quick wins. Those aren't quick wins — they're new content investments. The 4-10 range is the sweet spot.
