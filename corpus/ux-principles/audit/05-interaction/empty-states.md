---
name: Empty States — Warm Message + Primary Action + Visual
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 400-500
related: [corpus/ux-principles/audit/08-content/empty-states-warm.md, corpus/ux-principles/audit/05-interaction/error-messages.md, corpus/ai-product-ux/]
---

# Empty States — Warm Message + Primary Action + Visual

## What it is

An empty state is what a list, dashboard, or section shows when there's nothing in it (no items yet, no search results, no notifications). Empty states should NOT be a literal "No items." text. They should be:

1. **A warm, human message** explaining what should be here and why it isn't yet.
2. **A primary action** — the next thing the user should do.
3. **A visual** — illustration, icon, or shape that gives the empty state weight.

This is one of the highest-leverage moments in any product: empty states are when users are most likely to leave or get stuck.

## Why it matters

A blank screen with "No items" tells the user nothing useful. A great empty state tells them what this section is for, why it's empty (often because they haven't done X yet), and what to do next. Empty states are the product's voice in moments of zero state — they teach without instructions.

Most apps have far more empty-state moments than they realize: first-run for every list, no-results for every search, success-state-after-clearing for every queue. Each is an opportunity.

## How to apply

1. **Write the message** as if greeting the user:
   - "No invoices yet. Send your first invoice to get paid."
   - "Inbox zero. You're all caught up."
   - "No results for 'foo'. Try a broader search."
2. **Provide the primary action** as a button:
   - "Create invoice" / "Send invoice"
3. **Add a visual.** A small illustration or icon. Doesn't have to be elaborate — even a single SVG line drawing.
4. **Don't write happy talk.** "Welcome to your invoices! We're so glad you're here..." → cut. Get to the point.

## Examples

- **GOOD:** Linear's empty issue list — "No issues yet. Create your first issue." + CTA + small icon.
- **BAD:** A list view that just says "No items." in 12px gray text. User has no path forward.
- **GOOD:** Gmail empty inbox — "Nothing in Inbox" + a friendly illustration. Confirms success rather than implying failure.
- **BAD:** A "No data" empty state on a dashboard with no explanation of how to add data.

## Related entries

- `corpus/ux-principles/audit/08-content/empty-states-warm.md` — content-side rules
- `corpus/ux-principles/audit/05-interaction/error-messages.md`
- `corpus/ai-product-ux/` — AI products especially benefit from great empty states

## Anti-patterns

- The empty state as a literal "No items." — unhelpful, cold, dead-end.
- Empty states that are "Welcome to..." paragraphs. Cut the welcome, keep the action.
