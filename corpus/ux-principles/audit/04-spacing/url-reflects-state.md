---
name: URL Reflects State — Filters, Tabs, Pagination in Query Params
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 400-500
related: [corpus/ux-principles/principles/navigation-as-wayfinding.md, corpus/ux-principles/audit/05-interaction/empty-states.md]
---

# URL Reflects State — Filters, Tabs, Pagination in Query Params

## What it is

If the user can change what they see (filter a list, switch a tab, paginate, sort), that change should be reflected in the URL. Filters → query params (`?status=active&priority=high`). Tabs → query params or path segments (`?tab=settings` or `/settings`). Pagination → query params (`?page=3`). Sort → query params (`?sort=name-asc`).

The principle: any state worth seeing should be linkable, shareable, and bookmarkable.

## Why it matters

URLs are the original sharing mechanism. When state lives only in JavaScript memory, users can't share their view, can't bookmark it, can't return to it after a refresh, and can't navigate back via the browser's Back button. All of these are basic web affordances that get broken by SPAs that ignore the URL.

This is also a wayfinding aid — the URL is part of the "where am I?" answer. A URL that reads `/dashboard/orders?status=pending&page=2` tells the user (and search engines, and analytics) exactly what view they're on.

## How to apply

1. **Filters → query params.** When a user selects "Status: Active", update the URL to `?status=active`.
2. **Tabs → query params or path.** Path is better for distinct views (`/settings/billing`); query for transient toggles (`?view=grid`).
3. **Pagination → query param.** `?page=3`. Don't load infinite-scroll without ANY URL hooks; keep a `?offset=` or `?cursor=`.
4. **Sort → query param.** `?sort=created_desc`.
5. **Refresh test.** Apply filter, refresh page. Does the filter survive? If no, fix.
6. **Share test.** Copy URL, paste in incognito. Same view? If no, fix.

## Examples

- **GOOD:** GitHub issues list — filter, label, sort all in URL: `?q=is%3Aopen+label%3Abug&sort=created`. Linkable.
- **BAD:** A SaaS dashboard where filtering by status updates the view but the URL stays `/dashboard`. Refresh = filter lost. Share = friend gets the unfiltered view.
- **GOOD:** Linear — current view, filter, sort all reflected in URL. Sharable links to specific issue lists.
- **BAD:** A modal opened via in-page state. URL doesn't change. User can't share the deep link.

## Related entries

- `corpus/ux-principles/principles/navigation-as-wayfinding.md`
- `corpus/ux-principles/audit/05-interaction/empty-states.md`

## Anti-patterns

- "We use a state management library so URLs aren't needed." URLs are the canonical state for the web.
- Updating the URL but breaking back-button behavior — make sure each URL change is a real history entry.
