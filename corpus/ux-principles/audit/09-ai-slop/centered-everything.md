---
name: Centered Everything (AI Slop)
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/brand-system/identity/imagery-anti-patterns.md, corpus/ux-principles/audit/01-hierarchy/eye-flow-natural.md]
---

# Centered Everything

## What it is
`text-align: center` on every heading, every description, every card, every CTA — top to bottom of the page. No left edge, no rhythm, no eye-flow path. The "look at me" of bad PowerPoint, ported to the web, generated at scale by every LLM trained on Squarespace and Tailwind starter pages.

## Why it matters
Centering everything eliminates the natural top-left to bottom-right reading path that makes a page scannable (`audit/01-hierarchy/eye-flow-natural.md`). It looks "balanced" but reads like a wedding invitation: each line floats independently with no relationship to the next. It's the easiest layout choice (no decision required) — which is exactly why AI defaults to it. Real design uses center sparingly: one centered hero on a marketing page, then left-aligned discipline elsewhere.

## How to apply
- Audit by searching for `text-align: center`, `text-center` (Tailwind), or `mx-auto` on every block — particularly in feature grids, testimonial sections, and CTA blocks.
- Default to **left-aligned** (or right-aligned in RTL languages) for body copy, headings inside cards, list items, form labels, and button-rows-aligned-to-content.
- Reserve center for: page titles in narrow narrative pages, modal headers, single-CTA hero blocks, and short call-outs (≤6 words).
- Card content: left-align the heading and description, even if the icon is centered above. Mixed alignment is fine and far more dynamic than full-center.
- Long-form text (5+ word descriptions): always left-align. Centered measure makes line-length jagged and unreadable.

## Examples (BAD vs. GOOD pairs)

BAD:
```html
<section class="text-center">
  <h2>Powerful Features</h2>
  <p>Everything you need to ship great work, in one place.</p>
  <div class="grid grid-cols-3 text-center">
    <article>
      <Icon centered/>
      <h3>Fast</h3>
      <p>Built for speed at any scale, with global edge deployment.</p>
    </article>
    <!-- ... -->
  </div>
</section>
```

GOOD:
```html
<section>
  <h2 class="text-center">Powerful features</h2>  <!-- center the section heading only -->
  <div class="grid grid-cols-3">
    <article>
      <Icon/>
      <h3>Fast</h3>            <!-- left-aligned -->
      <p>Built for speed at any scale, with global edge deployment.</p>
    </article>
    <!-- ... -->
  </div>
</section>
```

## Related entries
- `corpus/ux-principles/audit/01-hierarchy/eye-flow-natural.md` — the reading-path rule.
- `corpus/brand-system/identity/imagery-anti-patterns.md` — broader catalog.

## Anti-patterns
- Full-page center alignment "to feel balanced" — looks like a spec sheet.
- Centered paragraphs of 3+ lines — line endings become jagged and unreadable.
- Center-aligning data tables or numbers in columns (`tabular-nums` rule applies).
