# Step 6: Draft All Assets

Based on the format decision, produce the full asset set.

## If the format warrants a long-form article

Applies to Deep Dive, Framework, or Story with substantial content.

1. **Long-form article (website version):** canonical piece for richezamor.com. Full length, full argument structure, full examples. This is the anchor piece everything else links to.

2. **Short-form article (LinkedIn + X):** single shortened version (~500 to 700 words) used on both platforms. Condenses the long-form piece while preserving the core argument. Ends with a link to the website piece.

3. **LinkedIn promo post:** short post (150 to 250 words) promoting the LinkedIn short-form article. Written to earn the click.

4. **X promo tweet:** single tweet (~250 char) promoting the X short-form article.

## If the format doesn't warrant a long-form article

Applies to Hot Take, Signal, short Story.

1. **LinkedIn post:** the piece itself, formatted for LinkedIn.
2. **X post:** the piece itself, formatted for X. Single post (not a thread unless the format specifically calls for one).

No article, no derivative short-forms, no promo posts in this case.

## Drafting rules for all assets

- Every draft must pass the Content Style Guide voice check
- Never use any of the AI tells listed in the Content Style Guide or project instructions (no em dashes, no "In today's..." openers, no "Let's dive in," no empty superlatives, etc.)
- Lead with a specific moment, observation, or claim. Never an abstract setup
- Suzy can be referenced as a proof point when relevant. Confirm language is comfortable before publishing (flag this in the output)
- Credit source authors by name when the piece is a reaction to someone else's work

## Newsletter CTA comment (required for every LinkedIn and X post)

Every LinkedIn post and every X post (including standalone posts AND promo posts) must ship with a companion **first-comment CTA** that points readers to the newsletter signup. The newsletter signup lives on the richezamor.com homepage header and primary CTA, so the destination is `https://richezamor.com`.

**Why a comment, not the post body:** keeps the post body clean, preserves algorithmic reach (LinkedIn and X both downrank posts with outbound links in the body), and gives a natural place for the CTA without breaking voice.

**Drafting rules for the CTA comment:**

- Voice-match the post (same Content Style Guide rules apply: no AI tells, no empty superlatives, no "Let's dive in")
- One short paragraph plus the URL, not a sales pitch
- Connect to the post's specific argument when possible (e.g., "If the context-engineering thread above resonated...") rather than a generic "subscribe to my newsletter"
- Keep it ≤40 words on LinkedIn, ≤200 chars on X
- URL: `https://richezamor.com` (the homepage; signup is in the header and primary CTA)
- Do not duplicate the article link if the post body already contains one. The CTA is for the newsletter, not the article

**Example shape (do not copy verbatim, match to the post):**

> If you want more breakdowns like this in your inbox, the newsletter goes deeper than the post: https://richezamor.com

## Page body structure addendum: newsletter CTA blocks

Add a `# LinkedIn First Comment` block after every LinkedIn post or LinkedIn promo post, and a `# X Reply Comment` block after every X post or X promo tweet, containing the drafted CTA comment. See the page body structure below.

## Notion page creation

Create the page in the Content Topics database (`0fcb9c17-695f-4c04-a72b-6b03fe074f8b`). Properties to populate:

- **Topic:** the title/headline of the piece
- **Status:** `Drafting`
- **Priority:** `High` for news reactions in a hot news cycle, `Medium` otherwise
- **Domain:** one or more of Context Layers & AI / Product Management / Leadership
- **Format:** the decided format (Deep Dive / Framework / Hot Take / Signal / Story)
- **Content Type:** LinkedIn, X (add Website when a long-form article exists)
- **Linked Briefing:** if the source was a Daily Context Briefing, add the URL
- **Trigger Date:** today's date

## Page body structure

```
# Article (Website Long Form)
[long-form article, if created]

---

# Short Article (LinkedIn & X)
[shortened version, if long-form was created]

---

# LinkedIn Promo Post
[promo post, if article exists; else this is the LinkedIn post]

---

# LinkedIn First Comment
[newsletter CTA comment to post as the first comment on the LinkedIn post above; voice-matched, ≤40 words, links to https://richezamor.com]

---

# X Promo Tweet  (or # X Post)
[promo tweet or X post]

---

# X Reply Comment
[newsletter CTA comment to post as a reply on the X post above; voice-matched, ≤200 chars, links to https://richezamor.com]

---

# SEO & AIO Optimization
[from rz-content-optimize, if article exists]

---

# Research Notes
[adjacent content from step 2 plus past work from step 3]

---

# Publishing Notes
- Source article and URL
- Calendar slot and any override rationale
- Suzy language check reminder (if referenced)
- Image filenames (SVG plus PNG)
- Internal link candidates from past Content Topics
```
