---
name: Max Content Width — No Full-Bleed Body Text
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/02-typography/measure-45-75.md, corpus/ux-principles/audit/04-spacing/grid-consistent.md]
---

# Max Content Width — No Full-Bleed Body Text

## What it is

Body text and other prose-heavy content should have a maximum width that keeps the line measure in the legibility range (45-75 chars per line). Full-bleed body text (text spanning the entire viewport width on wide screens) produces unreadably long lines.

The rule: set `max-width` on prose containers. Common values:

- **Body prose:** `max-width: 65ch;` (~65 chars per line at base font size)
- **Page container:** `max-width: 1200-1400px;` for marketing layouts
- **Dashboard / app:** wider is fine; not all content is long-form prose

## Why it matters

Prose at 1600px wide on an ultrawide monitor is essentially unreadable. The eye loses its place wrapping. Even at 1200px wide, body text becomes fatiguing. Setting a max-width is a one-line CSS fix that immediately raises the legibility floor for every reader on a large screen.

## How to apply

1. **CSS for prose:**
   ```css
   .prose, article p { max-width: 65ch; }
   ```
2. **CSS for page container:**
   ```css
   .container { max-width: 1280px; margin: 0 auto; }
   ```
3. **Distinguish prose width from layout width.** A page can be 1280px wide while body text inside it is 65ch wide.
4. **Audit:** on a 1920px wide window, do paragraphs run full-width? If yes, fix.

## Examples

- **GOOD:**
  ```css
  article {
    max-width: 65ch;
    margin: 0 auto;
  }
  ```
- **BAD:** A blog post with no `max-width` on body. On a 1920px monitor, lines are ~250 chars wide.
- **GOOD:** Medium articles — prose centered at ~680px wide regardless of viewport.
- **BAD:** A docs site where code blocks span 1800px wide because the layout container has no max.

## Related entries

- `corpus/ux-principles/audit/02-typography/measure-45-75.md`
- `corpus/ux-principles/audit/04-spacing/grid-consistent.md`

## Anti-patterns

- "Full-width feels modern." Full-width body text is illegible at scale.
- Setting page container max-width but forgetting prose max-width — page is fine, body text inside is still too wide.
