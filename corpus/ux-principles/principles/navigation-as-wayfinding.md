---
name: Navigation as Wayfinding
domain: ux-principles
source_skill: design-review
entry_type: framework
length_target: 300-800
related: [corpus/ux-principles/audit/trunk-test.md, corpus/ux-principles/audit/scoring-pass-partial-fail.md, corpus/ux-principles/principles/billboard-design-overview.md]
---

# Navigation as Wayfinding

## What it is

Users on the web have no sense of scale, direction, or location. Unlike a physical store, there are no walls, no aisles, no "you are here" signs by default. Navigation is the wayfinding system that compensates. It must always answer six questions, on every page, without the user thinking about them:

1. **What site is this?** (Site ID visible and identifiable)
2. **What page am I on?** (Page name prominent, matches what I clicked)
3. **What are the major sections?** (Primary nav visible and clear)
4. **What are my options at this level?** (Local nav or content choices obvious)
5. **Where am I in the scheme of things?** ("You are here" indicator, breadcrumbs)
6. **How can I search?** (Search box findable without hunting)

These six questions become the **Trunk Test**: cover everything except the navigation. You should still be able to answer all six. If not, the navigation has failed.

## Why it matters

Without wayfinding, users are lost. Lost users either hit Back (and rarely return) or click randomly until they accidentally find something (and then never trust the structure again). Wayfinding is what turns a collection of pages into a navigable product. It is also one of the most underweighted aspects of design — teams obsess over hero images while users can't tell which page they're on.

The Trunk Test is the operational version of this principle. It is harsh, and most pages fail. A trunk-test FAIL is a HIGH-impact finding regardless of how polished the visual design is.

## How to apply

1. **Persistent navigation on every page.** Same nav, same place. Users learn it once.
2. **Breadcrumbs for deep hierarchies.** Especially in docs, settings, multi-level catalogs.
3. **Current section visually indicated.** A highlighted nav item, a bold breadcrumb, a header that matches the section name.
4. **Page name prominent.** Often the H1, often matching the link text the user clicked to get here.
5. **Search findable.** Top-right is the convention. Don't bury it in a menu.
6. **Run the trunk test on every page.** Score PASS / PARTIAL / FAIL. FAIL is high-impact.

## Examples

- **GOOD:** GitHub repo page — logo top-left, repo name + branch breadcrumb, tabs (Code / Issues / PRs / Actions / etc.) clearly indicating sections, current tab underlined. All six questions answered.
- **BAD:** A SaaS dashboard where the page title and section indicator are missing. User clicked "Reports" from the sidebar, but nothing on the page confirms this is the Reports view.
- **GOOD:** Wikipedia — site ID at top, page title huge, search top-right, breadcrumbs and table of contents in the article. Wayfinding rich.
- **BAD:** A "minimal" marketing site where the logo links nowhere, there's no nav, and you have to scroll to figure out what page you're on.

## Related entries

- `corpus/ux-principles/audit/trunk-test.md` — the operational test
- `corpus/ux-principles/audit/scoring-pass-partial-fail.md` — how to score a trunk test
- `corpus/ux-principles/principles/billboard-design-overview.md` — wayfinding lives inside billboard design

## Anti-patterns

- Hiding navigation to "reduce clutter." Users without navigation don't see clean — they see lost.
- Innovative nav placements (centered hamburger, hidden until hover) for marketing sites. They lose the trunk test.
