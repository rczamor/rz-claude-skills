---
name: Deep Dive Enrichment Checklist
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: template
length_target: 400-700
related: [corpus/linkedin-audit/deep-dive/trigger-criteria.md, corpus/linkedin-audit/methodology/deep-dive-candidate-selection.md]
---

# Deep Dive Enrichment Checklist

## What it is
The per-post enrichment workflow for Deep Dive candidates Riché elects to investigate. Triggered manually after the audit's candidate list is reviewed; not part of the monthly audit run itself. Output: a "Deep Dive: {post URL}" sub-section appended to the current month's Notion audit page.

Source data for enrichment is NOT in the bulk export. Riché obtains it via:
- LinkedIn Community Management API (once the context management system has the connector live — preferred path)
- Manual click-through on the post (fallback, ~15 min/post)
- Browser-assisted scraping (alternative fallback, requires care re: LinkedIn TOS)

## Invocation

```
/rz-linkedin-audit deep-dive {post-url}
```

Or natural-language equivalent: "deep dive on the post about agent memory architectures." The skill resolves the URL from this month's Deep Dive Candidates list or from explicit URL.

## What enrichment gathers

The 6 enrichment dimensions:

### 1. Engagement type breakdown
Decompose the engagement count into:
- Reactions (and which type — Like, Praise, Empathy, Insightful, Funny, Curious)
- Comments
- Bookmarks
- Shares (and whether shared with commentary or as quote)

The bulk export gives only total engagements; this breakdown reveals whether the post earned reactions (low effort) vs comments/shares (higher effort, higher signal).

### 2. Commenter list with ICP match
For each commenter:
- Name, current role, current company
- ICP match: Yes/No (Yes = Senior+ at AI-PM target company, or founder, or event organizer)
- New connection vs existing connection
- Their own engagement quality (do they comment substantively or drive-by?)

The commenter list is often the highest-signal output. A post with 50 reactions and 8 substantive comments from Director+ AI-PM operators is far more valuable than 200 reactions with 2 drive-by comments.

### 3. Click data
- Where the post links externally (richezamor.com, GitHub, conference page, etc.)
- Approximate click-through count (LinkedIn doesn't always expose precisely)
- Where clicks went (UTM analysis if available)

If the post has no external links, this dimension is N/A.

### 4. Post copy and thesis classification
- Full post copy preserved
- Hook type (counter-claim / framework / story / signal-quote / case-study)
- Thesis: 1-sentence summary of the post's core argument
- Domain confirmation: validates Posts Master Domain assignment

### 5. Comments themed
Categorize each comment as:
- Substantive (≥30 words, adds perspective or asks a sharp question)
- Drive-by (<30 words, "great post" or simple agreement)
- Question (asks something specific)
- Pushback (disagrees with the thesis)
- Riché's reply (his comment on his own post)

Substantive + question + pushback are the high-signal comments. Drive-by counts toward reach but not toward engagement quality.

### 6. Inferred mechanism
Why did this post perform? Pull on:
- Was a peer creator's reshare visible (see P5 cross-reference)?
- Did it ride a topical wave (something happening in the AI/PM news cycle)?
- Did it benefit from a specific hook pattern (counter-claim opener, etc.)?
- Did it tap into an underserved topic (CI gaps from Audience Composition)?

A 1-paragraph hypothesis. Not certain — the LinkedIn algo is opaque — but informed.

## Output format

Appended to the month's Notion audit page as a sub-section:

```
### Deep Dive: {post URL}

Published {publish date}, {N} days old at deep-dive time.
{period total impressions} impressions, {period total engagements} engagements ({rate}%).

**Hook:** {hook type} — "{first 60 chars of post}"
**Thesis:** {1-sentence summary}
**Domain:** {Context Intelligence / PM / Leadership / Intersection}
**Format:** {Hot Take / Signal / Deep Dive / Framework / Story}

**Engagement breakdown:**
- Reactions: {N} ({Like N, Praise N, Insightful N, ...})
- Comments: {N}
- Bookmarks: {N}
- Shares: {N} (with commentary: {N})

**Commenter cohort:**
- {N} comments total
- {N} from ICP-match commenters ({list of names if ≤5})
- {N} substantive, {N} drive-by, {N} questions, {N} pushback

**Click data (if applicable):**
{N} clicks to {destination URL} — UTM analysis: {breakdown}

**Inferred mechanism:**
{1-paragraph hypothesis: peer reshare / topical wave / hook pattern / topic gap}

**Implications:**
{1-2 sentences: what this tells us about format/topic/hook strategy going forward}
```

## When to enrich vs skip

After reviewing the 5 candidates from the audit, Riché picks which (if any) to enrich. Heuristics:

- **High impressions, low engagement quality (lots of drive-by reactions, few substantive comments)** → enrich is low-priority; the post got reach but didn't compound.
- **Mid impressions, high engagement quality (Director+ commenters, substantive thread)** → enrich is high-priority; this is the kind of post worth understanding.
- **Late bloomer with peer reshare visible** → enrich is high-priority; understanding the reshare mechanism informs network strategy.
- **Post with high CTA click count** → enrich for the click data alone if the destination matters (e.g., richezamor.com /thinking traffic).

## Examples

1. **High-priority enrichment.** A Framework post on agent memory architectures, 4,500 impressions, 56 engagements. Comments include 2 from VP-PM at Series-B AI companies and 1 from a known YC founder. Enrichment shows 3 substantive comments, 2 questions, 1 pushback. Inferred mechanism: pushback comment triggered thread that recruited additional ICP commenters. Implication: counter-claim hooks invite pushback that pulls in ICP discussion.
2. **Skip enrichment.** A Hot Take with 12K impressions, 80 reactions (95% Like), 2 drive-by comments. High reach, low signal. Riché reviews and skips enrichment. Notes in audit: "Top reach this month but low engagement quality; not enrichment-worthy."
3. **Late-bloomer enrichment.** A 6-month-old Suzy story resurfaced with 8K impressions this month. Enrichment shows the resurface was triggered by Lenny mentioning Suzy in his newsletter (peer reshare adjacent). Implication: occasional name-checks from authority sources can revive evergreen posts.

## Related entries
- `corpus/linkedin-audit/deep-dive/trigger-criteria.md` — selects the candidates this checklist enriches
- `corpus/linkedin-audit/methodology/deep-dive-candidate-selection.md` — Step 5 audit selection (precedes manual enrichment)

## Anti-patterns

- Enriching all 5 candidates by default. Enrichment is gated; pick the worth-it ones.
- Treating the post copy classification as authoritative without cross-checking against Posts Master Domain. Manual classification can drift; reconcile to the canonical Content Topics DB tagging.
- Confusing reactions with engagement quality. 100 Like reactions ≠ 100 substantive comments. The breakdown matters.
- Skipping the inferred-mechanism section because "it's just speculation." Speculation grounded in evidence is the input to better strategy; absence of speculation = absence of strategy update.
