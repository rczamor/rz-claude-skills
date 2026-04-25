---
name: Empty States Designed With Warmth
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/05-interaction/empty-states.md, corpus/ai-product-ux/failure/, corpus/ux-principles/principles/goodwill-reservoir.md]
---

# Empty States Warm

## What it is
Every empty state — no items yet, no results, first run — must include three things: a **warm, specific message**, a **primary action** to fill the state, and a **visual anchor** (illustration, icon, or product-relevant graphic). "No items." with a gray period is the worst possible UX moment because it's the user's first impression of the empty surface.

## Why it matters
Empty states are first-run moments — the literal first time a user sees a screen. They set the tone for the entire product relationship. A cold "No items." reads as "you have nothing and the product doesn't care." A warm empty state reads as "we know this is empty for now; here's how to make it useful." This single element disproportionately drives activation, return-rate, and perception of quality.

## How to apply
- **Message** — speak to the user. "No projects yet — create your first one to get started." Not "0 projects" or "Empty list." Voice should match the brand but always be specific.
- **Primary action** — a clearly labeled button that takes them to the next step. "Create a project" / "Import contacts" / "Connect your Slack."
- **Visual anchor** — a small illustration, a product-relevant graphic, an icon. Not just whitespace. Helps the eye land. Avoid generic stock-illustrations; brand-specific imagery feels intentional.
- **Secondary cues** — optional: a one-line tip, a link to docs, a sample-data toggle. Don't overload — single primary action wins.
- For **search empty results** — also offer a "clear filters" or "browse all" escape hatch. Show the search query: "No results for 'kanbn' — try kanban?"
- For **error-as-empty** (failed to load): empty state turns into error state — see `audit/08-content/error-messages-specific.md`.
- Test by clearing the database and looking at every screen — every empty state visible should pass.

## Examples (BAD vs. GOOD pairs)

BAD:
```
No items.
```

GOOD:
```
[ small illustration of a folder ]

No projects yet
Projects help you group work and invite collaborators. Start with one, you can rename it later.

[ Create a project ]    Learn more →
```

GOOD — search empty:
```
No results for "kanbn"
Try "kanban" or [ Browse all docs ]
```

## Related entries
- `corpus/ux-principles/audit/05-interaction/empty-states.md` — interaction-state version of the same rule.
- `corpus/ai-product-ux/failure/` — empty-as-error and AI low-confidence states.
- `corpus/ux-principles/principles/goodwill-reservoir.md` — empty states either deplete or replenish goodwill.

## Anti-patterns
- "No items." — the universal sin.
- Empty state with no primary action — user stares at a wall.
- Generic stock illustration of an "empty box" used across every empty surface — feels off-the-shelf.
