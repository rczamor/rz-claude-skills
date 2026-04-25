---
name: Happy Talk Detection
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/principles/law-3-omit-then-omit-again.md, corpus/ux-principles/audit/08-content/happy-talk-word-count.md, corpus/ux-principles/audit/09-ai-slop/generic-hero-copy.md]
---

# Happy Talk Detection

## What it is
"Happy talk" is the introductory paragraph that talks about the product instead of letting users use it: "Welcome to [X]," "Our mission is to...", "We're so excited to bring you...", "Here at [Company] we believe..." Krug's test: if you can hear "blah blah blah" in your head while reading it, it's happy talk. Flag every instance for removal.

## Why it matters
Happy talk is the paragraph everyone wrote, no one reads, and the product wears like a stained shirt. It pushes useful content below the fold, dilutes the value prop, signals that no one stripped the page back to its job-to-be-done, and is one of the most reliable AI-content tells. Krug's Third Law says omit needless words and *get rid of half what's left* — happy talk is the first thing to cut.

## How to apply
- Scan the page for these openers — they almost always introduce happy talk:
  - "Welcome to..."
  - "Our mission is to..."
  - "We're excited to..."
  - "Founded in [year], we believe..."
  - "Here at [Company]..."
  - "[Product] is the all-in-one solution for..."
  - Any opening that mentions the company or product before describing what the user will *do*.
- Apply the blah-blah-blah test: read the paragraph in your head with "blah blah blah" replacing nouns and verbs. If the meaning doesn't change, it's happy talk.
- Recovery: replace with a single specific value-prop sentence, then jump straight to the product/CTA. "Track your team's design quality in one dashboard. [Try it free]" beats five paragraphs of welcome.
- For AI-generated copy specifically — happy talk is one of the strongest hallucination signals. AI fills gaps with feel-good filler.
- Flag in audit reports as: **"Happy talk detected at <selector>: '<first 80 chars>...' — recommend removal or replacement with a 1-line value prop."**

## Examples (BAD vs. GOOD pairs)

BAD:
> Welcome to Helm Labs! We're so excited to introduce you to our platform. Here at Helm Labs, we believe that great design deserves great tools. Our mission is to empower designers everywhere to ship work they're proud of. We can't wait to see what you create...

GOOD:
> Score every PR for design quality in 30 seconds. **[Start free trial]**

## Related entries
- `corpus/ux-principles/principles/law-3-omit-then-omit-again.md` — the parent principle.
- `corpus/ux-principles/audit/08-content/happy-talk-word-count.md` — methodology for measuring it.
- `corpus/ux-principles/audit/09-ai-slop/generic-hero-copy.md` — happy talk's twin.

## Anti-patterns
- Confusing "warm voice" with happy talk — warmth is fine, but it must serve the user's task.
- Treating brand statement as happy talk — brand-voice manifestos belong on About pages, not landing pages.
- Cutting happy talk and replacing with terse jargon — find the user-job sentence instead.
