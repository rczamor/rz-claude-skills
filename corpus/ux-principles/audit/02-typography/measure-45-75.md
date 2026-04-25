---
name: Measure — 45-75 Characters Per Line (66 Ideal)
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/02-typography/line-height.md, corpus/ux-principles/audit/04-spacing/max-content-width.md]
---

# Measure — 45-75 Characters Per Line (66 Ideal)

## What it is

The "measure" of body text is the number of characters per line. Legibility research (Bringhurst, *The Elements of Typographic Style*) puts the optimal range at **45–75 characters**, with **66 characters** being the ideal target. Lines shorter than ~45 chars force the eye to jerk back too often; lines longer than ~75 chars make it hard to track which line comes next when wrapping.

## Why it matters

Long-line body text (full-bleed paragraphs at 1200px wide) is one of the most common readability failures on the web. Designers focus on font-size and miss measure entirely. The result: technically legible text that fatigues the reader within a paragraph and gets abandoned.

Measure is especially critical for editorial content, blog posts, and documentation — anywhere the user actually reads sustained prose.

## How to apply

1. **In CSS:** `max-width: 65ch;` on prose containers (the `ch` unit equals the width of the "0" character, so 65ch ≈ 65 characters).
2. **Or set a pixel max-width** based on font-size: at 16px body, ~640px container hits ~66 chars per line.
3. **Audit:** count visible characters on the longest line of body text. If > 75, narrow the container.

## Examples

- **GOOD:**
  ```css
  .prose { max-width: 65ch; }
  ```
  At 16px body, this gives a comfortable 65-char measure.
- **BAD:** A blog post that runs body text full-width at 1200px wide. Measure: ~120 chars. Eye gets lost wrapping.
- **GOOD:** Medium articles default to ~66 chars per line. Notice how comfortable they are to read.
- **BAD:** A docs page with `width: 100%` on body paragraphs and no max-width. Measure varies 80-150 chars depending on viewport.

## Related entries

- `corpus/ux-principles/audit/02-typography/line-height.md`
- `corpus/ux-principles/audit/04-spacing/max-content-width.md`

## Anti-patterns

- "Full-width body text uses screen real estate efficiently." It uses pixels efficiently and reading speed inefficiently.
- Setting max-width in pixels (`max-width: 800px`) — works at one font-size, breaks if the user zooms.
