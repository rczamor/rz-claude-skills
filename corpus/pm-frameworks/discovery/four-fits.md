---
name: Four Fits
domain: pm-frameworks
source_skill: research
entry_type: framework
length_target: 600
related: [corpus/pm-frameworks/lifecycle/pmf-pyramid.md, corpus/pm-frameworks/strategy/gtm-strategy.md, corpus/pm-frameworks/monetization/product-led-growth.md]
---

# Four Fits

## What it is

Brian Balfour's framework (Reforge) for diagnosing why some products grow and others stall: durable growth requires alignment across **four fits**, not just product-market fit alone.

1. **Market–Product fit:** the product solves a real, sufficiently large market's problem.
2. **Product–Channel fit:** the product's natural distribution channel matches its growth motion (viral product → social channels; high-ACV product → outbound sales).
3. **Channel–Model fit:** the channel's economics support the business model (paid ads only work if LTV/CAC clears).
4. **Model–Market fit:** the business model is appropriate for the market's willingness to pay and budget cycles.

A break in any link cascades. Most "PMF" failures are actually channel-model or model-market breaks misdiagnosed as product problems.

From Balfour's Reforge essays (2017–onward), particularly "Why Product Market Fit Isn't Enough."

## Why it matters

Founders default to product as the explanation for everything. The four fits correct that bias by making distribution and monetization peers of product, not afterthoughts. A good product on the wrong channel dies. A good product with the wrong model dies. A product-market hit with channel and model mismatches looks like a "growth problem" — but the diagnosis lives in the broken link, not in tactical channel optimization.

For AI products specifically: AI shifts model–market fit (token-based pricing creates new model options) and channel–model fit (AI-content channels enable distribution motions that didn't exist). Many AI-product failures in 2023–2025 are model–market breaks (priced like SaaS, but compute economics force usage caps that trigger churn).

## How to apply

1. **Diagnose each fit individually.** For each link, score: strong / weak / broken. Be honest — channel-model breaks are the most common and the most denied.
2. **Trace the cascade.** A weak channel-model fit will look like a product problem (high CAC, low LTV) but no product investment fixes it.
3. **Choose channels and models that match your motion.** Self-serve PLG products need self-serve channels (search, content, virality) and self-serve models (freemium, usage-based). Sales-led products need sales channels (outbound, partner) and sales models (annual contract, expansion).
4. **Pre-commit to one model and one primary channel.** Multi-channel, multi-model startups usually have none of the four fits.

## Examples

1. **Helm Labs.** Strong market-product fit (PE-backed CFOs need close-process visibility). Channel choice: founder-led outbound to portfolio CFOs through a fund-relationship channel. Model: high-ACV annual contract (14x typical close-software ACV). Four fits aligned because the channel (warm fund intro), the model (annual at $200K+), and the market (PE portfolio CFOs with budget) reinforced each other.
2. **A consumer AI tool with viral growth but $20/mo pricing and high inference costs.** Strong market-product, strong product-channel (viral), but channel-model is broken: free-tier inference burns cash faster than $20/mo conversion produces it. No amount of conversion-rate optimization fixes that.

## Related entries

- `corpus/pm-frameworks/lifecycle/pmf-pyramid.md` — PMF as one of the four fits
- `corpus/pm-frameworks/strategy/gtm-strategy.md` — channel selection
- `corpus/pm-frameworks/monetization/product-led-growth.md` — one specific four-fits configuration
- `corpus/pm-frameworks/monetization/usage-based-pricing.md` — model implications for AI products

## Anti-patterns

- **"We just need more PMF."** Treating any growth problem as a product problem. Often the channel or the model is the problem and product investment compounds the loss.
- **Stacking incompatible motions.** Trying to run PLG and enterprise sales simultaneously without separate teams, models, and channels. The fits don't align across motions.
