---
name: Competitive Analysis (Direct / Indirect / Emergent)
domain: pm-frameworks
source_skill: research
entry_type: pattern
length_target: 500
related: [corpus/pm-frameworks/strategy/dhm-model.md, corpus/pm-frameworks/strategy/seven-powers.md, corpus/pm-frameworks/strategy/porters-five-forces.md, corpus/pm-frameworks/strategy/positioning.md]
---

# Competitive Analysis (Direct / Indirect / Emergent)

## What it is

A three-tier competitive landscape model:

1. **Direct competitors:** firms offering substitutable products to the same target customer for the same job. (Suzy vs. Qualtrics for enterprise consumer-intelligence platforms.)
2. **Indirect competitors:** firms offering different products that solve the same job. (Suzy vs. in-house analyst teams using Excel + survey tools.)
3. **Emergent competitors:** firms not currently in the category but whose capabilities or distribution position them to enter. (Suzy vs. an AI-research company building survey-style features into a general-purpose chatbot.)

Each tier requires a different analytical approach:
- **Direct:** feature parity, pricing, win/loss analysis.
- **Indirect:** customer-journey mapping (what's the alternative they currently use?).
- **Emergent:** trend monitoring (what capability buildup signals category entry?).

## Why it matters

Most competitive analysis stops at direct competitors and misses where the actual competitive risk lives. Customers rarely choose between two direct competitors; they choose between your product and "doing nothing" or "using the existing workaround." That's indirect competition. And the existential risk usually comes from emergent competitors entering with adjacent capabilities — Netflix didn't lose to Hulu; Blockbuster lost to Netflix entering from outside the video-rental category.

The three-tier frame makes those distinct competitive threats visible and prescribes different responses to each.

For AI products, emergent competition is especially acute. Foundation-model providers, hyperscalers, and adjacent SaaS companies can enter most AI application categories with one product launch. The emergent tier dominates the strategic risk for most AI startups.

## How to apply

- **Map all three tiers** in a single artifact. Each tier should have 3–10 entries.
- **Pair with DHM.** For each direct competitor, what's their delight, hard-to-copy, margin? Where are you stronger or weaker?
- **Identify emergent threats** by scanning adjacent categories: which firms have capabilities that could be redirected into your category? What signal would indicate they're moving (hiring, partnerships, product launches)?
- **Update quarterly.** Emergent competitors become direct fast in AI; the tier that was empty last quarter may be full this quarter.
- **Use it to inform DHM defensibility.** The hard-to-copy leg should answer: against whom?

## Examples

1. **Suzy three-tier analysis.** Direct: Qualtrics, GLG, MarketCast. Indirect: in-house research teams; survey tools (SurveyMonkey, Typeform); consumer-research consultancies. Emergent: AI-research startups (Perplexity-style products positioning into research); hyperscaler offerings (Google's research-style features); enterprise CDP/analytics companies extending into qualitative.
2. **Helm Labs three-tier.** Direct: traditional close-software (BlackLine, FloQast). Indirect: Excel + audit-firm support; in-house FP&A. Emergent: AI-finance startups; ERP vendors extending close-narrative features.

## Related entries

- `corpus/pm-frameworks/strategy/dhm-model.md` — DHM informs which competitors matter and why
- `corpus/pm-frameworks/strategy/seven-powers.md` — powers analysis evaluates competitive defensibility
- `corpus/pm-frameworks/strategy/porters-five-forces.md` — substitutes ≈ indirect; threat of entry ≈ emergent
- `corpus/pm-frameworks/strategy/positioning.md` — positioning is how you differentiate from each tier

## Anti-patterns

- **Direct-only analysis.** Listing three SaaS competitors and considering the analysis done. Misses indirect (where most lost deals actually go) and emergent (where category-disrupting threats live).
- **Spec-comparison theater.** Filling a 50-row feature-parity matrix that says nothing about strategic differentiation. Feature parity is hygiene; competitive position lives in the DHM and Powers analysis.
