---
name: Happy Talk Word Count Methodology
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/08-content/happy-talk-detection.md, corpus/ux-principles/audit/08-content/instructions-detection.md, corpus/ux-principles/principles/law-3-omit-then-omit-again.md]
---

# Happy Talk Word Count

## What it is
A reportable methodology: count total visible words on the page, classify each text block as **useful content** vs. **happy talk** (welcome paragraphs, self-congratulatory text, instructions nobody reads, generic mission statements), and report the percentage. Output as: *"This page has X total words. Y (Z%) are happy talk."*

## Why it matters
Word-count is the most legible quantitative metric for the Third Law. "This page has 1,400 words; 720 (51%) are happy talk" is undeniable in a way that "your hero is too verbose" is not. It gives writers, designers, and PMs a concrete target to ratchet down over time. It also surfaces pages where the *useful* word count is so low that the layout is essentially decorative.

## How to apply
The methodology, in order:

1. **Extract visible text** from the rendered page — body text only, ignoring code blocks, alt text, hidden elements. Use the trunk-test stripped DOM: `document.body.innerText`.
2. **Tokenize** into blocks (paragraphs, headings, list items, button labels, form labels). Each block gets classified independently.
3. **Classify each block** into one of three buckets:
   - **Useful** — describes a specific user job, value prop tied to outcome, factual feature claim, navigation, microcopy that performs a function.
   - **Happy talk** — welcome paragraphs, mission statements, "we're excited," generic value props ("all-in-one solution"), unspecific superlatives ("revolutionary," "powerful," "seamless"), self-congratulatory founder paragraphs.
   - **Instructions** — any block longer than one sentence that tells the user how to use the interface (count toward happy talk in the total).
4. **Compute** total visible words; sum of words classified as happy talk + instructions; ratio.
5. **Report** with selector-anchored examples for each happy-talk block:
   ```
   This page has 1,420 words.
   - Useful content: 700 words (49%)
   - Happy talk: 520 words (37%)
   - Instructions: 200 words (14%)
   - Total flagged: 720 words (51%)
   Examples:
   - <section.hero> "Welcome to Helm Labs! We believe..." — 142 words
   - <section.about-us> "Founded in 2024, our mission..." — 98 words
   ```
6. **Recommend a target** — under 20% combined happy-talk + instructions for marketing pages; under 5% for product UI.

## Examples (BAD vs. GOOD pairs)

BAD report: "The copy is too long. Trim it." — unactionable.

GOOD report: "1,420 words; 51% happy talk + instructions. Removing the 'Welcome to' hero paragraph (142 words) and the 'How it works' instruction block (200 words) takes the page to 1,078 words and 13% flagged content."

## Related entries
- `corpus/ux-principles/audit/08-content/happy-talk-detection.md` — the qualitative rule.
- `corpus/ux-principles/audit/08-content/instructions-detection.md` — the paired symptom.
- `corpus/ux-principles/principles/law-3-omit-then-omit-again.md` — the parent law.

## Anti-patterns
- Reporting raw word count without classification — "this page has 1,400 words" doesn't tell anyone what to cut.
- Counting *all* paragraphs as happy talk — overshoots, becomes useless. Classify rigorously.
- Treating happy talk as purely a marketing-page issue — product UIs accumulate it inside empty states, onboarding modals, and "tip of the day" widgets.
