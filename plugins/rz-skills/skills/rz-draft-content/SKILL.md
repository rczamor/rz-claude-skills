---
name: rz-draft-content
description: >
  Use when given a source (article URL, Daily Context Briefing, or raw thought) and asked to turn it into a complete content piece for richezamor.com plus LinkedIn/X. Trigger phrases: "/rz-draft-content," "draft a post from this," "turn this into a piece," "write content on this." Output lands in the Notion Content Topics database.
---

# Draft Content — Riché Zamor

You orchestrate the end-to-end content drafting workflow for Riché Zamor. Given a source (article URL, Daily Context Briefing, or raw thought), you produce a fully populated Content Topic page in the Notion Content Topics database with all derivative assets, optimization recommendations, and a brand-consistent graphic.

## Invocation

Triggered by `/rz-draft-content`, by Riché sharing a source and asking for a draft, or semantically when the conversation is clearly asking for the full pipeline.

## Execution Mode

**Fully autonomous.** Run all eight steps and present the finished deliverables at the end. Do not checkpoint between steps unless you hit a blocking ambiguity (e.g., the source can't be located, multiple plausible topics are conflated, or a required Notion document is unreachable). When you must ask, ask once, concisely, and continue.

## Reference Documents (Notion IDs)

These five documents ground every draft. Read all of them fresh at the start of every run — Riché updates them monthly.

- **Platform Document** — `337ac0ea-4f65-819d-bfac-e40a99b83543` (thesis, terminology, argument structure, communication framework)
- **Context Intelligence Research** — `337ac0ea-4f65-8189-abd9-e2248e5e8f18` (intellectual foundation, cognitive science grounding)
- **Content Strategy** — `333ac0ea-4f65-8151-8651-d730d706e017` (editorial calendar, format templates, domain split)
- **Content Style Guide** — `337ac0ea-4f65-8103-91cd-db7ab5319ab7` (voice, AI tells, prohibited phrasing)
- **Content Channel Strategy** — `331ac0ea-4f65-81fe-af8f-e37afebaeaf5` (channel-level positioning, audience targeting)

**Content Topics database:** `0fcb9c17-695f-4c04-a72b-6b03fe074f8b`

## The Eight Steps

### Step 1 — Pull Source Content

Identify what the source is and retrieve it.

- **URL provided:** use `web_fetch` first. If blocked (Forbes, WSJ, paywalled sites), fall back to `web_search` for the article title + author to find an accessible version or a detailed summary.
- **Daily Context Briefing referenced:** fetch the Notion page directly via `Notion:notion-fetch`. The briefing will contain the relevant link and the synthesized take.
- **Raw thought or topic:** skip retrieval. The thought itself is the source.
- **Tavily:** use `Tavily:tavily_research` or `Tavily:tavily_extract` when `web_fetch` fails and `web_search` snippets aren't rich enough. Tavily is the escalation path for difficult sources.

Capture: the source URL, author, publication date, and the full body text.

### Step 2 — Research Adjacent Content

Widen the lens. Run 2-3 targeted searches to surface related recent content. Purpose: ground the piece in the current conversation, not just the single source.

- Use `web_search` with keywords from the source (the primary concept, the specific claim, named entities)
- Look for: other writers' takes on the same topic, counter-arguments, related research or data points, adjacent news events that strengthen or complicate the source's claim
- Pull 3-5 adjacent pieces. Capture URLs, headlines, and 1-2 sentences of substance per piece.

This research goes into the Content Topic page under "Research Notes" and informs the drafting phase. Don't dump every link — synthesize what's relevant.

### Step 3 — Check Past Work

Two sources to check, both required:

**A. Content Topics database** (`0fcb9c17-695f-4c04-a72b-6b03fe074f8b`)
- Use `Notion:notion-search` with keywords from the source topic
- Identify any existing Content Topics on the same or adjacent themes
- Capture: Topic title, Notion URL, Status (draft / published / idea)

**B. Historical LinkedIn archive** (project files)
- Check `Shares.csv` for past shares and commentary on the topic
- Check the article HTML files for past long-form pieces touching the topic
- Check `Comments.csv` for engagement context on past posts

Report back two things in the final output:
1. **Angles already covered.** What's Riché already said about this topic so the new piece doesn't repeat.
2. **Internal link candidates.** Specific Content Topics or past articles this new piece should reference or link to.

If there's a strong past piece that already covers the angle, flag that explicitly — it may mean the new piece needs a different angle or should be scrapped.

### Step 4 — Ground in Brand Documents

Fetch all five reference documents fresh. Extract:

- **From Platform Document:** the specific terminology the piece should use, the argument structure it should follow, and which of the four core arguments (if there are four — check current version) this piece advances
- **From Context Intelligence Research:** any cognitive science, decision science, or neuroscience grounding that's relevant to the topic
- **From Content Strategy:** the calendar slot, the format template, the domain split check (50/30/20 Context Layers / PM / Leadership)
- **From Content Style Guide:** voice rules, AI tells to avoid, prohibited phrasing, quotable-sentence standards
- **From Content Channel Strategy:** audience targeting for the current piece, channel-specific positioning

Hold this context while drafting. Every voice decision in the draft must pass the Content Style Guide. Every terminology decision must pass the Platform Document.

### Step 5 — Determine Format

Default: follow the Content Strategy calendar slot for today.

- Monday → Hot Take
- Tuesday → Signal
- Wednesday → Deep Dive
- Thursday → Framework
- Friday → Story

**Override rule:** if the topic pulls hard toward a different format, make a hard suggestion with one-sentence rationale. Override triggers:

- **Topic is primarily a personal narrative** → Story (regardless of day)
- **Topic is a breaking news event that demands immediate response** → Hot Take or Signal
- **Topic requires multi-concept walkthrough to land** → Deep Dive (even if today is Framework day)
- **Topic is teachable as a repeatable model** → Framework (even if today isn't Thursday)
- **Topic is too thin for long-form but too sharp to skip** → Hot Take as a LinkedIn/X post only, no article

State the format decision at the top of the final output with the override rationale (if any).

### Step 6 — Draft All Assets

Based on the format decision, produce the full asset set.

**If the format warrants a long-form article** (Deep Dive, Framework, or Story with substantial content):

1. **Long-form article (website version)** — canonical piece for richezamor.com. Full length, full argument structure, full examples. This is the anchor piece everything else links to.

2. **Short-form article (LinkedIn + X)** — single shortened version (~500-700 words) used on both platforms. Condenses the long-form piece while preserving the core argument. Ends with a link to the website piece.

3. **LinkedIn promo post** — short post (150-250 words) promoting the LinkedIn short-form article. Written to earn the click.

4. **X promo tweet** — single tweet (~250 char) promoting the X short-form article.

**If the format doesn't warrant a long-form article** (Hot Take, Signal, short Story):

1. **LinkedIn post** — the piece itself, formatted for LinkedIn.
2. **X post** — the piece itself, formatted for X. Single post (not a thread unless the format specifically calls for one).

No article, no derivative short-forms, no promo posts in this case.

**Drafting rules for all assets:**
- Every draft must pass the Content Style Guide voice check
- Never use any of the AI tells listed in the Content Style Guide or project instructions (no em dashes, no "In today's..." openers, no "Let's dive in," no empty superlatives, etc.)
- Lead with a specific moment, observation, or claim — never an abstract setup
- Suzy can be referenced as a proof point when relevant; confirm language is comfortable before publishing (flag this in the output)
- Credit source authors by name when the piece is a reaction to someone else's work

### Step 7 — SEO/AIO Optimization (if article)

If and only if a long-form article was drafted, invoke `rz-content-optimize` on the article body. The optimize skill produces the full 13-section SEO & AIO block.

Append the block to the Content Topic page under a section titled **"SEO & AIO Optimization"**.

If no long-form article exists (Hot Take / Signal format), skip this step entirely. Do not produce SEO recommendations for LinkedIn-only or X-only posts.

### Step 8 — Generate Graphic

Default to the diagram templates documented in `rz-graphic-design`:

- **Comparison diagram** — for pieces arguing A vs B, two concepts, two approaches
- **Flow diagram** — for pieces walking through a process or sequence
- **Framework diagram** — for pieces teaching a named model (like the five-step context generation flow)
- **Flywheel** — for pieces about compounding loops
- **Radar/matrix** — for pieces about multiple dimensions of a single concept

Select the template that best fits the piece's core argument. Generate the graphic in SVG, respecting the full brand visual identity from `rz-graphic-design` (dark #0a0a0a background, teal #00d4a3 accent, JetBrains Mono labels, Inter body, monospace section labels in uppercase with letter-spacing, dashed outlines for containers where appropriate).

**Dimensions:** 1200x630 for a single LinkedIn/X compatible version. If the piece specifically needs a platform-tuned pair, also produce 1080x1080 (LinkedIn square) and 1600x900 (X optimized) — but the default is one graphic at 1200x630.

**Output both formats:**
- SVG (for editing and archival)
- PNG at 2x resolution (2400x1260) for upload

Save both to `/mnt/user-data/outputs/` and present them.

If the topic doesn't clearly map to any existing template, propose a new template design inline, generate it, and flag it for addition to the `rz-graphic-design` template library.

## Notion Page Creation

Create the page in the Content Topics database (`0fcb9c17-695f-4c04-a72b-6b03fe074f8b`). Properties to populate:

- **Topic:** the title/headline of the piece
- **Status:** `Drafting`
- **Priority:** `High` for news reactions in a hot news cycle, `Medium` otherwise
- **Domain:** one or more of Context Layers & AI / Product Management / Leadership
- **Format:** the decided format (Deep Dive / Framework / Hot Take / Signal / Story)
- **Content Type:** LinkedIn, X (add Website when a long-form article exists)
- **Linked Briefing:** if the source was a Daily Context Briefing, add the URL
- **Trigger Date:** today's date

Page body structure:

```
# Article — Website (Long Form)
[long-form article, if created]

---

# Short Article — LinkedIn & X
[shortened version, if long-form was created]

---

# LinkedIn Promo Post
[promo post, if article exists; else this is the LinkedIn post]

---

# X Promo Tweet  (or # X Post)
[promo tweet or X post]

---

# SEO & AIO Optimization
[from rz-content-optimize, if article exists]

---

# Research Notes
[adjacent content from step 2 + past work from step 3]

---

# Publishing Notes
- Source article and URL
- Calendar slot and any override rationale
- Suzy language check reminder (if referenced)
- Image filenames (SVG + PNG)
- Internal link candidates from past Content Topics
```

## Final Output to Chat

After the page is created, present to Riché:

1. **One-line summary** of what was produced (format, asset count, graphic template used)
2. **Link to the Notion page**
3. **Inline preview** of the LinkedIn promo post and X promo tweet (the two assets he'll actually publish first — keeps them reviewable without opening Notion)
4. **The graphic** (both SVG and PNG file links)
5. **Flagged decisions** — anything that needs explicit approval before publish (Suzy language, format override, keyword choice if SEO ran)

Keep the summary under 10 lines. The page is the deliverable; chat is the summary.

## Error Handling

- **Source unreachable:** if `web_fetch`, `web_search`, and `Tavily` all fail, stop and ask Riché for the article text or a different source.
- **Notion document unreachable:** if any of the five reference documents can't be fetched, proceed with the ones you have and flag the gap in the final output.
- **No past work found:** fine. Note it in Research Notes and move on.
- **Ahrefs MCP fails during optimization:** `rz-content-optimize` will fall back to web_search-based SERP analysis and flag that keyword volumes are estimates. Proceed.

## What This Skill Does NOT Do

- Does not publish to LinkedIn or X. Drafts only.
- Does not update the Content Topics database schema. Only creates pages within it.
- Does not edit the five reference documents. Read-only.
- Does not override Riché's voice. Every draft passes the Content Style Guide.

## Cross-References

- `rz-copywriting` — voice calibration for every draft
- `rz-content-optimize` — invoked in step 7 when a long-form article exists
- `rz-graphic-design` — invoked in step 8 for template selection and visual system
- `rz-growth-marketing` — consult when Linked Briefing data suggests a growth-specific angle
