---
name: Users Scan, They Don't Read
domain: ux-principles
source_skill: design-review
entry_type: concept
length_target: 300-800
related: [corpus/ux-principles/principles/billboard-design-overview.md, corpus/ux-principles/principles/law-3-omit-then-omit-again.md, corpus/ux-principles/audit/01-hierarchy/squint-test.md, corpus/ux-principles/audit/02-typography/no-skipped-heading-levels.md]
---

# Users Scan, They Don't Read

## What it is

Real users do not read interfaces — they scan them. Eye-tracking studies confirm it: users sweep across a page in F-shaped or Z-shaped patterns, fixating on headings, bolded terms, and visual landmarks, skipping past paragraphs entirely. We are designing billboards going by at 60 mph, not product brochures people will study at leisure.

Designing for scanning means visual hierarchy (prominence = importance), clearly defined areas, headings and bullet lists, and highlighted key terms.

## Why it matters

Designers who imagine attentive readers produce dense paragraphs of carefully worded prose that no one ever sees. The page may be technically informative and still functionally invisible — users glide past the careful writing because nothing in the visual hierarchy says "this matters." Scannability is not a stylistic preference; it's a survival requirement for any interface competing for human attention.

## How to apply

1. **Build prominence into hierarchy.** More important = more visually prominent (size, weight, color, position). Less important fades.
2. **Use headings, lists, and chunks.** Break long copy into short sections with descriptive headings. Bullet lists where ≥3 parallel items exist.
3. **Highlight key terms in body copy.** Bold the load-bearing word in a paragraph so a scanning user catches it.
4. **Clearly define areas.** A user should be able to point at any region of the page and name its purpose in 2 seconds.
5. **Run the squint test.** Blur the page in your mind (or literally squint). The hierarchy should still be visible — primary action visible, sections distinct, navigation locatable.

## Examples

- **GOOD:** A pricing page with three clearly bordered tier cards, each headline-size price, each bullet list of features. The user can compare in 5 seconds.
- **BAD:** A pricing page that runs paragraphs of feature descriptions inline. The user gives up before extracting any comparison.
- **GOOD:** Stripe's docs — short paragraphs, code samples set off, every section heading scannable.
- **BAD:** A wall of body text with no headings, no bolding, no whitespace breaks.

## Related entries

- `corpus/ux-principles/principles/billboard-design-overview.md` — the broader framing
- `corpus/ux-principles/principles/law-3-omit-then-omit-again.md` — fewer words to scan = more get seen
- `corpus/ux-principles/audit/01-hierarchy/squint-test.md` — the operational test
- `corpus/ux-principles/audit/02-typography/no-skipped-heading-levels.md` — heading structure for scanners

## Anti-patterns

- "Users will read this paragraph because it's important." If it were important, the design would make that obvious without the paragraph.
- Mistaking a designer's attention span (long, focused) for a user's (short, scanning).
