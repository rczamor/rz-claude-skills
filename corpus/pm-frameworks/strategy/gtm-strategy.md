---
name: GTM Strategy (Sales-Led / Product-Led / Marketing-Led / Community-Led)
domain: pm-frameworks
source_skill: research
entry_type: framework
length_target: 600
related: [corpus/pm-frameworks/discovery/four-fits.md, corpus/pm-frameworks/monetization/product-led-growth.md, corpus/pm-frameworks/monetization/sales-led.md, corpus/pm-frameworks/monetization/growth-loops.md]
---

# GTM Strategy (Sales-Led / Product-Led / Marketing-Led / Community-Led)

## What it is

The four dominant go-to-market motions, each defined by which function carries the buyer through the funnel:

1. **Sales-led growth (SLG).** A sales rep guides the buyer from awareness to purchase. High ACV, long cycles, complex products. Common in enterprise. (Salesforce, Snowflake.)
2. **Product-led growth (PLG).** The product itself is the primary acquisition, conversion, and expansion vehicle. Self-serve onboarding; freemium or trial; usage-based or seat-based monetization. (Notion, Figma, Slack.)
3. **Marketing-led growth (MLG).** Content, ads, SEO, and brand drive awareness and consideration; sales or product converts. Common in mid-market SaaS. (HubSpot, Drift.)
4. **Community-led growth (CLG).** A community of users, evangelists, or developers drives adoption through social proof, peer education, and network effects. (HashiCorp, Notion to a degree, dbt.)

Most successful companies are dominantly one motion with secondary support from others. Trying to run all four simultaneously usually produces weak versions of each.

## Why it matters

GTM motion choice is one of the four fits (channel-model fit). The wrong motion for the product, market, or model destroys unit economics. A high-ACV enterprise product attempting PLG starves the sales motion of leads. A self-serve consumer product running enterprise sales burns CAC against contracts that won't justify it.

Each motion has structural implications:
- **Capital intensity:** SLG burns cash early on quota-carrying reps; PLG burns cash on product engineering and inference.
- **Margin profile:** SLG tolerates high CAC if LTV justifies it; PLG depends on viral/self-serve mechanics keeping CAC low.
- **Defensibility:** SLG defends through switching costs; PLG defends through workflow embedding and network effects; CLG defends through community lock-in.

For AI products, motion choice is acute. AI products often have low CAC (viral demos) and high COGS (inference). The traditional PLG playbook (free tier scales acquisition, conversion to paid pays the bill) breaks when free-tier inference burns faster than paid conversion compensates. Many AI startups need a hybrid motion: PLG-led with sales-led for high-LTV accounts.

## How to apply

1. **Diagnose your fit.** What ACV does the product support? What does the buying journey look like? Who has authority to buy? The answers point to one dominant motion.
2. **Choose one primary motion.** Build the full system for that motion: team, process, metrics, tooling. Secondary motions support, not replace.
3. **Align the four fits.** Channel matches motion (SLG → outbound + ABM; PLG → search + content + virality; MLG → paid + organic; CLG → community + evangelism). Model matches motion. Market matches motion.
4. **Watch for motion mismatch signals.** Long sales cycles in PLG products → motion is wrong or pricing is too high. Self-serve users in SLG products without expansion path → motion is wrong or product is too simple.
5. **Layer secondary motions only after primary is healthy.** Adding sales to a PLG company too early starves the primary motion; layering after $10M+ ARR usually works.

## Examples

1. **Suzy Decision Engine.** Sales-led primary (350+ enterprise customers; high-ACV; complex implementations). Marketing-led secondary (thought leadership content). The product itself doesn't drive direct self-serve acquisition — the buyer is too far from the product, the implementation too complex.
2. **Helm Labs.** Sales-led primary (PE-backed CFOs; ~$200K ACV; warm-intro channel through funds). Community-led secondary (auditor relationships as evangelists). PLG would not work — the buyer is not the user; the implementation requires services.
3. **Hypothetical AI startup.** Mixed motion: PLG for individual users (free tier + $20/mo); SLG for enterprise accounts >$50K. Two distinct GTM systems running in parallel. This works only after PLG validates the wedge; running both from day one usually fails.

## Related entries

- `corpus/pm-frameworks/discovery/four-fits.md` — channel-model fit
- `corpus/pm-frameworks/monetization/product-led-growth.md` — PLG deep dive
- `corpus/pm-frameworks/monetization/sales-led.md` — SLG deep dive
- `corpus/pm-frameworks/monetization/growth-loops.md` — loops underpin most non-SLG motions

## Anti-patterns

- **All-of-the-above motion.** Attempting PLG, SLG, MLG, and CLG simultaneously without scale to support any. Each motion gets weak execution; pipeline doesn't materialize from any.
- **Motion-product mismatch.** Trying to run PLG on a product that requires services to value-realize. Customers sign up, fail to onboard, churn — and the team blames the funnel.
