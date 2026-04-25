---
name: Navigation Collapses Appropriately on Mobile
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/principles/navigation-as-wayfinding.md, corpus/ux-principles/audit/06-responsive/mobile-design-sense.md]
---

# Nav Collapse Pattern

## What it is
On mobile, top-level navigation must collapse into a pattern appropriate for the product's information architecture: hamburger menu (deep / occasional nav), bottom tab bar (3–5 primary destinations, app-style), or progressively-disclosed top-aligned nav (linear flows). The wrong choice makes the product feel either web-1.0 or Frankenstein.

## Why it matters
Mobile screens can't show a 6-link horizontal nav without crushing it. The collapse choice signals what the product *is* — bottom tabs say "this is an app you live in"; hamburger says "this is a site you visit"; sticky horizontal scroll says "this is a content list." Mismatch hurts wayfinding (Q3: "What are the major sections?") and disorients returning users.

## How to apply
- Bottom tab bar — best for products with 3–5 primary, persistent destinations (Home / Explore / Inbox / Profile). Targets 48px high, sits inside `env(safe-area-inset-bottom)`. Used by most app-shaped products.
- Hamburger / drawer — best for content-heavy sites with deep IA, settings-style nav, infrequent jumps. Cheap to implement; signals "site, not app." Don't bury primary CTAs inside.
- Sticky top bar with scrolling chips — best for content categories or filter-as-nav (Twitter/X, news sites).
- Whatever you pick, "current location" must be visible (Q5 of Trunk Test). Bottom tabs use icon-fill; drawer rows use accent color.
- Never combine all three — it's a tell that no one decided what the product is.

## Examples (BAD vs. GOOD pairs)

BAD — 6 links squashed into a 320px-wide top bar with overflow scrolling that the user doesn't notice; no current-state highlight.

GOOD — bottom tab bar with 4 primary items at 44px tall each, current tab indicated with filled icon + label color, plus a "More" overflow menu for the 5th+ destination. Hamburger only opens secondary settings.

```html
<nav class="bottom-tabs" aria-label="Primary">
  <a href="/" aria-current="page"><Icon name="home-fill"/> Home</a>
  <a href="/search"><Icon name="search"/> Search</a>
  <a href="/inbox"><Icon name="inbox"/> Inbox</a>
  <a href="/me"><Icon name="user"/> You</a>
</nav>
```

## Related entries
- `corpus/ux-principles/principles/navigation-as-wayfinding.md` — the 6 wayfinding questions.
- `corpus/ux-principles/audit/06-responsive/mobile-design-sense.md` — re-author, don't port.

## Anti-patterns
- Hamburger menu hiding the primary CTA — burying conversion behind two taps.
- Bottom tab bar with 7 destinations — they truncate, and you get a "More" tab that becomes a kitchen-junk drawer.
- Both top and bottom nav simultaneously, eating screen real estate.
