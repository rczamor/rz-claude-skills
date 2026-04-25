---
name: Van Westendorp Price Sensitivity Meter
domain: pm-frameworks
source_skill: research
entry_type: framework
length_target: 400
related: [corpus/pm-frameworks/monetization/value-based-pricing.md, corpus/pm-frameworks/monetization/price-sensitivity-testing.md, corpus/pm-frameworks/discovery/customer-development.md]
---

# Van Westendorp Price Sensitivity Meter

## What it is

A 1976 survey method (Peter van Westendorp, Dutch economist) for estimating a product's acceptable price range. Four questions to a sample of target customers about the same product:

1. **Too cheap:** "At what price would you consider this so cheap that you'd doubt the quality?"
2. **Cheap (bargain):** "At what price would you consider this a bargain?"
3. **Expensive:** "At what price would you start to consider this expensive but still worth considering?"
4. **Too expensive:** "At what price would you consider it so expensive that you would not buy it?"

Plotting the cumulative distributions yields four intersection points: the **point of marginal cheapness**, **point of marginal expensiveness**, **optimum price point** (intersection of "too cheap" and "too expensive"), and **indifference price point** (intersection of "cheap" and "expensive"). The acceptable price range lies between marginal cheapness and marginal expensiveness.

## Why it matters

Most pricing in early-stage products is set by gut, anchor-to-competitor, or cost-plus. None reveal customer willingness to pay. Van Westendorp gives a fast, survey-based estimate of the acceptable range without the cost of conjoint analysis. It's especially useful when the product category has no obvious benchmark or when a startup is pricing a new category.

Limitations: it captures hypothetical willingness to pay, not behavior. People price differently in surveys than at the checkout. Use it to set a defensible band, then validate with real purchase data.

## How to apply

1. **Recruit a sample** of at least 100 target customers. Smaller samples produce noise; the method depends on cumulative distributions.
2. **Show a clear product description** (concept, problem solved, alternatives) before asking the four questions. Without context, the answers are arbitrary.
3. **Plot cumulative distributions** for each price band. The intersections produce the four price points.
4. **Use the optimum price point as a starting hypothesis**, the acceptable range as your bounds, and validate via actual purchase tests (e.g. real checkout, not stated intent).

## Examples

1. **Helm Labs price test.** Riché ran a Van Westendorp on a sample of 40 PE-backed CFOs for the close-software offering. Optimum point landed at ~$180K ARR; acceptable range $120K–$240K. Initial deals closed in the upper third of the range, consistent with the meter and 14x typical category ACV.
2. **Consumer SaaS.** A founder pricing a $9 vs $15 vs $29/mo tier ran the method on early signups. The data showed $19 as the optimum and $9 as "too cheap" — guiding the launch pricing away from the gut-instinct $9.

## Related entries

- `corpus/pm-frameworks/monetization/value-based-pricing.md` — pricing to value, not cost
- `corpus/pm-frameworks/monetization/price-sensitivity-testing.md` — the broader pricing-research toolkit
- `corpus/pm-frameworks/discovery/customer-development.md` — pricing as part of business hypothesis testing

## Anti-patterns

- **Treating stated price as actual willingness to pay.** Hypothetical answers consistently overstate. Use the meter for ranges, not commitments.
- **Skipping the description.** Asking the four questions without context yields random answers because customers don't know what they're pricing.
