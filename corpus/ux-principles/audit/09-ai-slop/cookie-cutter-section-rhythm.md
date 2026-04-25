---
name: Cookie-Cutter Section Rhythm (AI Slop)
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/09-ai-slop/3-column-feature-grid.md, corpus/brand-system/identity/imagery-anti-patterns.md]
---

# Cookie-Cutter Section Rhythm

## What it is
The exact same landing-page sequence every AI-generated site ships: **hero → 3-column features → testimonials → pricing → final CTA**. Every section roughly the same height, the same padding, the same horizontal centerline. The visual rhythm of every Bubble / Framer / Webflow template ever built — and now every LLM's default.

## Why it matters
A landing page should be paced like an argument: tension, then evidence, then resolution. The cookie-cutter rhythm has no argument — every section is the same weight, so nothing stands out. Real designed sites vary section heights dramatically: a tall product-demo block, a short pull-quote, a wide stat band, a tight pricing table. Variation creates rhythm; rhythm creates pacing; pacing creates conversion. Equal sections create a beige.

## How to apply
- Audit your page section-by-section and ask three questions for each:
  1. **Is this the same height as the section above?** If yes, vary it deliberately.
  2. **Is this the same padding pattern?** If yes, vary it.
  3. **Does this section answer a question the previous one raised, or is it just "next thing on the script"?** If the latter, delete or restructure.
- Vary by:
  - **Section height** — full-viewport hero, then half-viewport story, then 30vh stat band.
  - **Background** — alternating neutral / accent / image-led / no-background.
  - **Layout** — 12-col asymmetric block, 2-col split, 1-col narrative, full-bleed image.
  - **Density** — alternate dense (table, comparison) with airy (single quote, single product shot).
- Skip sections you don't need. Nobody requires testimonials *and* logo wall *and* case-study *and* press-mentions all in a row — pick one form of social proof.
- Replace the closing CTA section with something more differentiated: a calendar embed, a real product try-it block, a "what happens next" walkthrough.

## Examples (BAD vs. GOOD pairs)

BAD section sequence:
```
[hero — 80vh, centered text]
[3-feature grid — 50vh, centered text]
[testimonial carousel — 50vh, centered text]
[pricing — 80vh, 3 equal pricing tiers]
[final CTA — 50vh, centered text "Ready to get started?"]
```
Five sections, all centered, all roughly half-screen, all featuring some flavor of generic copy.

GOOD section sequence:
```
[hero — 70vh, left-aligned headline + product screenshot]
[customer-logo strip — 15vh]
[product walkthrough — 100vh, scroll-driven]
[case study quote — 30vh, single quote in serif]
[pricing — 60vh, asymmetric: 1 plan called out + 2 supporting]
[FAQ — variable height, accordion]
```

## Related entries
- `corpus/ux-principles/audit/09-ai-slop/3-column-feature-grid.md` — the slop's most identifiable section.
- `corpus/brand-system/identity/imagery-anti-patterns.md` — broader catalog.

## Anti-patterns
- Believing "but this is the conversion-optimized layout." 5 years ago, maybe. Today it's the universal AI-generated fingerprint.
- Adding a section because it "should be there" (a logo wall, a stat band) without earning it with content.
- Equalizing section heights for "visual balance" — section heights should vary by argument weight.
