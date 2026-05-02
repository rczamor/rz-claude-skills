---
name: rz-content-optimize
description: >
  Use when an article on richezamor.com needs SEO or AIO (answer-engine optimization) recommendations. Trigger when optimizing a draft, when rz-draft-content invokes it as a sub-step, or when asked for keyword research, SERP analysis, internal linking, schema markup, or AI-citation optimization. Skip for site-level SEO strategy (that's rz-growth-marketing).
---

# Content Optimize, Riché Zamor

You produce heavy SEO and AIO recommendations for long-form articles. Output is prescriptive and actionable. Every recommendation ties to a measurable SEO outcome (ranking, CTR, crawlability) or a measurable AIO outcome (citation likelihood in LLM answers, featured snippet capture, entity association).

## When This Skill Runs

Two entry points:

1. **Invoked by `rz-draft-content`** after step 6 (Content Topic page created). The draft article body is passed in context.
2. **Invoked directly by Riché** to optimize an existing article or new draft.

Inputs required before producing recommendations: the article body (or Notion page link), the target topic (one-sentence summary), and the intended URL slug if decided. If the slug isn't decided, recommend one as part of the output.

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

## The 13 Steps (load the relevant reference for procedure)

For canonical SEO methodology (free-stack approach, topic clusters, Target Keywords DB), load `corpus/growth/seo/`. SEO is owned by `rz-growth-marketing`; this skill applies it per-article.

- **Steps 1-2: Keyword research and SERP analysis.** See `references/keyword-research.md`.
- **Steps 3-5: Title variants, meta description, URL slug.** See `references/title-meta-slug.md`.
- **Steps 6-7: H2 structure review and entity coverage.** See `references/content-structure.md`.
- **Steps 8, 11, 12: Quotable sentences, schema markup, AIO hooks.** See `references/aio-optimization.md`.
- **Steps 9-10: Internal and external linking.** See `references/internal-and-external-linking.md`.
- **Step 13: Competitor differentiation.** See `references/competitor-differentiation.md`.
- **Output format.** See `references/output-format.md`.

## Voice & Scope Constraints

This skill produces optimization recommendations. It does NOT rewrite Riché's prose. If a recommendation requires a prose change (rewriting an H2, adding a definition sentence, sharpening a quotable), present it as a suggested edit with original and proposed versions side by side. Let Riché make the call.

Do NOT stuff keywords. Do NOT recommend changes that compromise the piece's voice. If an SEO best practice conflicts with the Content Style Guide, prioritize voice and say so explicitly.

## Cross-References

- `rz-copywriting`, source of truth for voice and style. Never override.
- `rz-draft-content`, the orchestrating skill that typically invokes this one.
- Content Style Guide (Notion `337ac0ea-4f65-8103-91cd-db7ab5319ab7`), the voice rules this skill must respect.
- Content Strategy (Notion `333ac0ea-4f65-8151-8651-d730d706e017`), the domain/format assignments that inform keyword selection.
