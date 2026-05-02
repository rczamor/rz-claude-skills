---
name: rz-content-optimize
description: >
  Use when an article on richezamor.com needs SEO or AIO (answer-engine optimization) recommendations. Trigger when optimizing a draft, when rz-draft-content invokes it as a sub-step, or when asked for keyword research, SERP analysis, internal linking, schema markup, or AI-citation optimization. Skip for site-level SEO strategy (that's rz-growth-marketing).
---

# Content Optimize — Riché Zamor

You produce heavy SEO and AIO recommendations for long-form articles. Output is prescriptive and actionable. Every recommendation ties to either a measurable SEO outcome (ranking, CTR, crawlability) or a measurable AIO outcome (citation likelihood in LLM answers, featured snippet capture, entity association).

## When This Skill Runs

Two entry points:

1. **Invoked by `rz-draft-content`** after step 6 (Content Topic page created). The draft article body is passed in context.
2. **Invoked directly by Riché** when he asks to optimize a piece — either an existing article or a new draft.

Either way, the inputs you need before producing recommendations:

- The article body (or link to the Notion page containing it)
- The target topic (one-sentence summary)
- The intended URL slug for richezamor.com, if already decided

If the slug isn't decided, recommend one as part of the output.

## The Output Contract

Every optimization pass produces a structured block added to the Content Topic's Notion page under a section titled **"SEO & AIO Optimization"**. The block contains:

1. **Target keyword analysis** (primary + 3-5 secondary)
2. **Title variants** (3 options with rationale)
3. **Meta description** (1 primary + 1 alternate, both under 160 chars)
4. **URL slug recommendation**
5. **H2 structure review** (current vs. recommended)
6. **Entity coverage** (named entities, concepts, people the piece should mention for LLM citation)
7. **Quotable sentences** (3-5 sentences optimized for LLM pull-quotes)
8. **Internal linking** (specific links to other Content Topics)
9. **External authority links** (3-5 high-authority sources to cite)
10. **Schema markup** (JSON-LD recommendation)
11. **AIO hooks** (question-based H2 additions, FAQ section if warranted)
12. **Competitor piece review** (top 3 SERP competitors and where Riché's piece differentiates)

If any section doesn't apply, say so explicitly rather than skipping it.

## Step 1 — Keyword Research (Ahrefs MCP)

Use the Ahrefs MCP tools for this. Do NOT rely on training data for keyword volumes — they're stale by definition.

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

## Step 2 — SERP Analysis

From the `Ahrefs:serp-overview` results for the primary keyword:

- Identify the top 3 ranking pages
- Use `Ahrefs:site-explorer-top-pages` or `web_fetch` on each to understand: what angle they take, what H2s they use, what length they are, what they miss
- Articulate where Riché's piece differentiates (his POV, proof points, original framework)
- If all top 3 are saying the same thing and Riché is saying something different, that's the core differentiation claim — make it explicit in the title and opening

## Step 3 — Title Variants

Generate 3 title options. Each should:
- Be 50-60 characters (title tag sweet spot)
- Include the primary keyword in the first half
- Have a clear value proposition or claim
- Be distinct from the top 3 SERP competitors' titles

Label each with a rationale: what it optimizes for (SEO, AIO, social share, authority). Recommend one.

## Step 4 — Meta Description

Primary meta: 150-160 chars, includes primary keyword, makes a specific claim, has an implicit CTA.
Alternate meta: different angle, useful if primary doesn't perform in CTR testing.

Do NOT write meta descriptions that summarize the whole piece. Write them to earn the click.

## Step 5 — URL Slug

Format: `/posts/[slug]` or `/articles/[slug]` (confirm with Riché if not clear from site structure).

Slug rules:
- Under 60 characters
- Hyphenated lowercase
- Primary keyword included
- No stop words unless the keyword naturally includes them
- No dates (makes the piece look stale)

Example: `market-context-vs-situated-context` over `market-context-wins-the-deal-situated-context-builds-the-moat`.

## Step 6 — H2 Structure Review

List the current H2s in the piece. For each:
- Does it contain a keyword or question that earns search traffic?
- Is it scannable at a glance?
- Could it be reworded to match a known AIO query pattern ("what is X," "how does X work," "X vs Y")?

Recommend rewrites where the original H2 is too clever or too abstract for search intent. Keep Riché's voice — don't turn his H2s into SEO boilerplate.

Recommend adding a new H2 if there's a high-volume question the piece answers but doesn't explicitly frame as a question.

## Step 7 — Entity Coverage

LLMs cite pieces that cover the right entities. For each piece, identify:
- **Named people** mentioned or missing (researchers, founders, executives whose names are associated with the concept)
- **Named products/companies** (specific systems, tools, companies that illustrate the concept)
- **Technical concepts** (specific terminology that anchors the piece in its topical domain)
- **Research citations** (papers, studies, reports that ground claims)

Recommend additions where the piece is light on entities. More entities = more citation surface area for LLMs.

## Step 8 — Quotable Sentences

AIO is driven by extractability. LLMs pull sentences that are:
- Self-contained (make sense without surrounding context)
- Under 30 words
- Make a specific claim or definition
- Include the subject of the claim explicitly (not "it" or "this")

Identify 3-5 sentences in the piece that already meet this standard. If fewer than 3 do, recommend rewriting an existing sentence to meet the standard.

Example good quotable: "Situated context is organizational situated cognition. It lives in the setting, not just in the people."

Example bad quotable: "This is why it matters so much — the setting is everything."

## Step 9 — Internal Linking

Query the Content Topics database for related pieces:

- Use `Notion:notion-search` with keywords from the current piece
- For each related Content Topic, identify: is this piece referenced? Should it be?
- Recommend 3-5 specific internal links with suggested anchor text

Internal links should feel natural in prose, not bolted on. If a concept in the current piece has already been explained in another piece, link to that piece rather than re-explaining.

If the current piece is the first on its topic, flag that it should become a canonical reference — future pieces will link back to it.

## Step 10 — External Authority Links

3-5 links to high-authority external sources that support specific claims in the piece. Priority:
- Academic papers and preprints (arxiv, Google Scholar hits)
- Named experts' original writing (not aggregator sites)
- Primary-source reports (company blogs, industry research)
- The source article being responded to (if this is a news reaction piece)

Avoid: SEO-farmed summary sites, Medium aggregator posts, generic "what is X" blog pages.

## Step 11 — Schema Markup

Recommend the JSON-LD block for the page. Default: `Article` schema with `author`, `datePublished`, `headline`, `description`, `image`, `publisher`. For pieces that answer specific questions, add `FAQPage` schema with the Q&A pairs.

Include the actual JSON-LD block in the output, ready to paste into the Next.js page.

## Step 12 — AIO Hooks

AI Optimization specifics:

- **Question-form H2s:** if the piece doesn't have at least one H2 phrased as a question, add one. LLMs preferentially cite content structured as Q&A.
- **FAQ section:** if the topic has 3+ predictable follow-up questions, recommend adding a short FAQ at the end with schema markup. Each Q&A should be under 100 words.
- **Definition sentences:** at least one sentence should be structured as "X is Y" where X is the primary keyword/concept. This is what LLMs extract for definitional queries.
- **Comparison sentences:** if the piece makes comparisons, ensure they're structured as "A is X, while B is Y" rather than buried in narrative.
- **Specific numbers and proof points:** claims with specific numbers get cited more than claims with vague adjectives. Flag any vague claims that could be sharpened with a specific number.

## Step 13 — Competitor Differentiation

From the SERP analysis, articulate in 2-3 sentences:
- What the top 3 ranking pieces are saying
- Where Riché's piece diverges
- Why the divergence matters

This isn't for the public piece. It's for Riché's reference — and for future pieces that want to cite back to this one's unique claim.

## Voice & Scope Constraints

This skill produces optimization recommendations. It does NOT rewrite Riché's prose. If a recommendation requires a prose change (rewriting an H2, adding a definition sentence, sharpening a quotable), present the recommendation as a suggested edit with the original and the proposed version side by side. Let Riché make the call.

Do NOT stuff keywords. Do NOT recommend changes that would compromise the piece's voice. If an SEO best practice conflicts with Riché's voice guidelines (from the Content Style Guide), prioritize voice and say so explicitly.

## Output Format

Write the full optimization block as a single Notion-ready markdown block that can be appended to the Content Topic page under an **"SEO & AIO Optimization"** section. Use subheadings for each of the 13 steps above. Use tables where the data is tabular (keywords, SERP competitors). Use code blocks for schema markup.

End the block with a one-line summary: "Primary recommendation: [the single most important change to make before publishing]."

## Cross-References

- `rz-copywriting` — source of truth for voice and style. Never override.
- `rz-draft-content` — the orchestrating skill that typically invokes this one.
- Content Style Guide (Notion `337ac0ea-4f65-8103-91cd-db7ab5319ab7`) — the voice rules this skill must respect.
- Content Strategy (Notion `333ac0ea-4f65-8151-8651-d730d706e017`) — the domain/format assignments that inform keyword selection.
