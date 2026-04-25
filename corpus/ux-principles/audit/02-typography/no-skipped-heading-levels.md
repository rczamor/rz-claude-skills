---
name: No Skipped Heading Levels
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/02-typography/scale-ratio.md, corpus/ux-principles/principles/users-scan-not-read.md]
---

# No Skipped Heading Levels

## What it is

Heading hierarchy must follow the document outline: `<h1>` → `<h2>` → `<h3>` → `<h4>`. Skipping levels (e.g., `<h1>` followed directly by `<h3>` with no `<h2>` between them) is a violation. One `<h1>` per page. Subsections nest in order.

This is both a semantic / accessibility rule (screen readers announce heading levels) and a visual hierarchy rule (size and weight should correspond to depth).

## Why it matters

Heading levels are the document's table of contents for both humans and machines. Screen readers let blind users navigate by heading level — a skipped level produces a confusing jump in the announced outline. Sighted scanning users also rely on heading depth to understand structure; an `<h3>` styled to look like an `<h2>` (because `<h2>` was skipped) produces visual / semantic mismatch.

## How to apply

1. **One `<h1>` per page.** Usually the page title.
2. **Nest in order.** `<h2>` for major sections, `<h3>` for subsections, `<h4>` rarely needed.
3. **Don't skip levels** to achieve a visual style. If you want a smaller heading, style the `<h2>` smaller — don't switch to `<h3>`.
4. **Audit:** scan the DOM for heading sequence. Any out-of-order jump is a finding.

## Examples

- **GOOD:**
  ```html
  <h1>Documentation</h1>
  <h2>Getting Started</h2>
  <h3>Installation</h3>
  <h3>Configuration</h3>
  <h2>API Reference</h2>
  ```
- **BAD:**
  ```html
  <h1>Documentation</h1>
  <h3>Installation</h3>  <!-- skipped h2 -->
  ```
- **GOOD:** A blog post with `<h1>` (title), `<h2>` (sections), `<h3>` (subsections). Nested correctly.
- **BAD:** A landing page with five `<h1>` tags because the designer wanted "five big headlines."

## Related entries

- `corpus/ux-principles/audit/02-typography/scale-ratio.md`
- `corpus/ux-principles/principles/users-scan-not-read.md`

## Anti-patterns

- Using heading tags for visual size. Use a CSS class (`.text-3xl`) for visual styling; use heading tags for semantic structure.
- Multiple `<h1>` tags per page. SEO and accessibility both penalize this.
