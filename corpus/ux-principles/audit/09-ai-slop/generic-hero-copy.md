---
name: Generic Hero Copy (AI Slop)
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/08-content/happy-talk-detection.md, corpus/brand-system/identity/imagery-anti-patterns.md]
---

# Generic Hero Copy

## What it is
Hero headlines made of training-set platitudes: "Welcome to [X]," "Unlock the power of...," "Your all-in-one solution for...," "The future of [vertical]," "Built for the modern team." These are the single most reliable AI-content signal — the LLM saw these patterns ten million times and they are now a reflex.

## Why it matters
Generic hero copy says everything and nothing. It works as a placeholder. It cannot fail because it makes no commitment. But it also cannot succeed: the user reads "Your all-in-one solution for [thing]" and learns absolutely nothing about what the product does, who it's for, or whether it's better than alternatives. Specific copy is intrinsically braver — it states a verifiable claim. Generic copy is the visual handshake of a product that didn't decide what it is.

## How to apply
- Detection — scan H1s, hero subheaders, and first paragraphs for these phrases:
  - "Welcome to [X]"
  - "Unlock the power of..."
  - "Your all-in-one solution for..."
  - "The future of [industry/category]..."
  - "Built for the modern [audience]..."
  - "[Product] is the [adjective] platform for..."
  - "Empower your team to..."
  - "Revolutionize / Transform / Elevate / Streamline / Optimize..." as the verb.
- Replace with a **specific job-to-be-done** sentence:
  - Bad: "Unlock the power of design at scale."
  - Good: "Score every PR for design quality in 30 seconds."
- Test: read the headline aloud. Does it tell someone *what changes for the user*? If no, it's slop.
- Pair with the happy-talk-detection rule — generic hero copy is happy talk's twin.

## Examples (BAD vs. GOOD pairs)

BAD:
```html
<h1>Welcome to Helm Labs.</h1>
<p>Unlock the power of design quality with our all-in-one solution. Built for the modern team.</p>
<button>Get Started</button>
```

GOOD:
```html
<h1>Score every PR for design quality in 30 seconds.</h1>
<p>10-category audit. WCAG-AA enforced. Plain-English review comments your engineers will actually read.</p>
<button>Try free for 14 days</button>
```

## Related entries
- `corpus/ux-principles/audit/08-content/happy-talk-detection.md` — overlapping rule.
- `corpus/brand-system/identity/imagery-anti-patterns.md` — broader catalog.

## Anti-patterns
- "We rewrote it but it still sounds the same" — likely still using the same verbs (Unlock / Empower / Streamline). Pick a real verb tied to the user's job.
- Replacing platitudes with industry jargon — "Leverage AI-powered synergies" is platitudes wearing a suit.
- Vague benefit + specific number ("Unlock the power of design quality. 10x faster.") — the number doesn't rescue the headline.
