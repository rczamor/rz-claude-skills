# Keyword Research and SERP Analysis

Covers the first two steps of the optimization pass: keyword research with the Ahrefs MCP and SERP analysis of top-ranking competitors.

## Step 1: Keyword Research (Ahrefs MCP)

Use the Ahrefs MCP tools for this. Do NOT rely on training data for keyword volumes, they're stale by definition.

**Canonical SEO methodology:** load `corpus/growth/seo/` for the free-stack approach (GSC + Keyword Planner + manual SERP review), the topic clusters that anchor Riché's authority territory, and the Target Keywords DB schema. Ahrefs MCP supplements those sources for keyword volume and SERP data; it does not replace them. SEO is owned by `rz-growth-marketing`; this skill applies it per-article.

Tools to call, in order:

1. **`Ahrefs:keywords-explorer-overview`** on the primary topic term (e.g., "situated context" or "context layer").
2. **`Ahrefs:keywords-explorer-related-terms`** to surface adjacent terms.
3. **`Ahrefs:keywords-explorer-matching-terms`** to find long-tail variants.
4. **`Ahrefs:serp-overview`** on the primary keyword to see who's ranking now.
5. **`Ahrefs:keywords-explorer-search-suggestions`** for question-form variants (these feed AIO).

Output the keyword block as a table with: keyword, monthly volume, keyword difficulty, search intent (informational / commercial / navigational / transactional), and whether the piece currently mentions it.

**Primary keyword selection criteria:**
- Volume ≥ 50/month OR strong AIO-citation potential (question-form, entity-rich)
- Difficulty realistic for richezamor.com's current authority (start with KD < 30 unless the topic is a pillar piece)
- Direct match to the piece's core argument, not a stretch

**Secondary keywords:** 3-5 related terms the piece can naturally cover without keyword stuffing. These earn long-tail traffic and reinforce topical authority.

## Step 2: SERP Analysis

From the `Ahrefs:serp-overview` results for the primary keyword:

- Identify the top 3 ranking pages
- Use `Ahrefs:site-explorer-top-pages` or `web_fetch` on each to understand: what angle they take, what H2s they use, what length they are, what they miss
- Articulate where Riché's piece differentiates (his POV, proof points, original framework)
- If all top 3 are saying the same thing and Riché is saying something different, that's the core differentiation claim. Make it explicit in the title and opening.
