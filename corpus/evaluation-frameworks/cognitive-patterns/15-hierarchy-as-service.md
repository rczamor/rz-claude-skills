---
name: Hierarchy as Service
domain: evaluation-frameworks
source_skill: plan-ceo-review
entry_type: concept
length_target: 300-800
related: [corpus/evaluation-frameworks/cognitive-patterns/17-subtraction-default.md, corpus/evaluation-frameworks/review-sections/11-design-ux-review.md, corpus/evaluation-frameworks/design-rubric/dimensions.md]
---

# Hierarchy as Service

## What it is
Every interface decision answers: what should the user see first, second, third? Visual hierarchy is not about prettifying pixels — it is about respecting the user's attention. The 10x CEO views every UI as a contract: the user lends you their time, and the hierarchy you produce is your repayment. A page where everything competes for attention is a page that returns the user nothing for their attention. A page with clear hierarchy says "we know what you came for, and we put it first."

## Why it matters
Plans without hierarchy ship interfaces where every element is "important," which means none of them are. Users scan; they don't read. The first 5 seconds determine whether they stay. Hierarchy is the single design move that survives every other failure — bad copy with right hierarchy is comprehensible; great copy with no hierarchy is invisible. Plans that don't articulate hierarchy explicitly will produce interfaces that fall back on whatever feels balanced, which is rarely what serves the user.

## How to apply
1. For every screen in the plan, demand the answer: "What do they see first? Second? Third?" Three is the limit. If the plan can't name the top three, it hasn't designed the screen — it has populated a layout.
2. Apply the trunk test: if a user landed on this page from a search engine, could they identify (in 5 seconds) what the page is, where they are, and what they can do? If no, the hierarchy is broken.
3. Watch for "everything is bold" failures: every heading H1, every button primary, every block highlighted. Bolding is meaningful only by contrast.
4. Hierarchy is not just visual. Information hierarchy (what's loaded first, what's lazy-loaded), interaction hierarchy (what's keyboard-accessible first), and content hierarchy (which paragraph leads) all matter.

## Examples
1. **SaaS dashboard plan**: lists 14 widgets with no priority. Hierarchy intervention: "Two top-row widgets are 'today's count' and 'urgent items.' All others below the fold." The widget set might not change; the hierarchy does.
2. **Marketing landing page**: hero, sub-hero, three feature blocks, CTA, footer. Hierarchy is correct if first viewport is brand + headline + one CTA. Hierarchy is broken if the hero is competing with three feature blocks above the fold.
3. **Settings page**: 40 settings. Hierarchy: top 3 are "the things 80% of users change." Everything else is grouped into "Advanced." Without hierarchy, every setting reads as equally important and the user freezes.

## Related entries
- `corpus/evaluation-frameworks/cognitive-patterns/17-subtraction-default.md` — subtraction often produces hierarchy by removing noise
- `corpus/evaluation-frameworks/review-sections/11-design-ux-review.md` — Section 11's IA question is hierarchy-as-service
- `corpus/evaluation-frameworks/design-rubric/dimensions.md` — hierarchy is the most-failed design dimension

## Anti-patterns
- Treating hierarchy as a styling concern. It is an information-architecture concern that styling expresses.
- Setting hierarchy by what the team is excited about, not what the user came for. The user's hierarchy is the authority.
