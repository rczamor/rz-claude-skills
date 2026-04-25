---
name: No Placeholder / Lorem Ipsum in Production
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/09-ai-slop/generic-hero-copy.md]
---

# No Placeholder Text in Production

## What it is
Lorem ipsum, "TODO copy", "Headline goes here", and similar placeholders must never appear in shipped product. This is a baseline professionalism check — if real copy isn't ready, the section isn't ready to ship.

## Why it matters
Placeholder text in production is the single most damaging credibility signal. It tells users "we didn't finish this" and "no one reviewed it before launch." Worse, lorem ipsum often slips through because it *visually* looks like real text — the eye reads "shape of paragraph" and skips on. The first time a user notices, the site loses years of trust.

## How to apply
- Grep the codebase for `lorem`, `ipsum`, `dolor sit amet`, `TODO`, `TBD`, `placeholder copy`, `headline goes here`. Flag every match.
- For input placeholders, the goal is to suggest format, not to label — labels go above the input. Placeholder example: "name@company.com" inside an email input.
- Pre-prod copy gate: copy review is part of the launch checklist, not an afterthought.
- For genuinely empty states (no content yet), see `audit/08-content/empty-states-warm.md` — empty isn't the same as placeholder.
- CMS / content models — never let optional fields default to a sample placeholder string at the DB layer; default to `null` and render the empty state.

## Examples (BAD vs. GOOD pairs)

BAD:
```html
<h1>Lorem ipsum dolor sit amet</h1>
<p>Consectetur adipiscing elit. Pellentesque dignissim...</p>
<button>Submit</button>
```

GOOD:
```html
<h1>Track your team's design quality in one dashboard.</h1>
<p>Helm Labs scores every PR for hierarchy, accessibility, and motion correctness in under 30 seconds.</p>
<button>Start a 14-day trial</button>
```

For empty states — instead of placeholder body text, render a deliberate empty state with message + action.

## Related entries
- `corpus/ux-principles/audit/09-ai-slop/generic-hero-copy.md` — generic copy is half-step better than lorem, but still flag-worthy.

## Anti-patterns
- "Welcome to [Product Name]" left in the hero post-launch.
- A sample blog post titled "Lorem Ipsum" still in the production CMS.
- Image alt text reading "alt text here" — common on rushed launches, kills accessibility.
