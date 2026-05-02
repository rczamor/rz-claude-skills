# AIO Optimization: Quotable Sentences, Schema Markup, AIO Hooks

Covers the AI-optimization specifics: extractable sentences, JSON-LD schema, and structural hooks (question-form H2s, FAQ sections, definition sentences) that increase LLM citation likelihood.

## Step 8: Quotable Sentences

AIO is driven by extractability. LLMs pull sentences that are:
- Self-contained (make sense without surrounding context)
- Under 30 words
- Make a specific claim or definition
- Include the subject of the claim explicitly (not "it" or "this")

Identify 3-5 sentences in the piece that already meet this standard. If fewer than 3 do, recommend rewriting an existing sentence to meet the standard.

Example good quotable: "Situated context is organizational situated cognition. It lives in the setting, not just in the people."

Example bad quotable: "This is why it matters so much, the setting is everything."

## Step 11: Schema Markup

Recommend the JSON-LD block for the page. Default: `Article` schema with `author`, `datePublished`, `headline`, `description`, `image`, `publisher`. For pieces that answer specific questions, add `FAQPage` schema with the Q&A pairs.

Include the actual JSON-LD block in the output, ready to paste into the Next.js page.

## Step 12: AIO Hooks

AI Optimization specifics:

- **Question-form H2s:** if the piece doesn't have at least one H2 phrased as a question, add one. LLMs preferentially cite content structured as Q&A.
- **FAQ section:** if the topic has 3+ predictable follow-up questions, recommend adding a short FAQ at the end with schema markup. Each Q&A should be under 100 words.
- **Definition sentences:** at least one sentence should be structured as "X is Y" where X is the primary keyword/concept. This is what LLMs extract for definitional queries.
- **Comparison sentences:** if the piece makes comparisons, ensure they're structured as "A is X, while B is Y" rather than buried in narrative.
- **Specific numbers and proof points:** claims with specific numbers get cited more than claims with vague adjectives. Flag any vague claims that could be sharpened with a specific number.
