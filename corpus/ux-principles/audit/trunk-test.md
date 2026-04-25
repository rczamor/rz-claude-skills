---
name: The Trunk Test
domain: ux-principles
source_skill: design-review
entry_type: template
length_target: 600-800
related: [corpus/ux-principles/principles/navigation-as-wayfinding.md, corpus/ux-principles/audit/scoring-pass-partial-fail.md, corpus/evaluation-frameworks/review-sections/]
---

# The Trunk Test

## What it is

The Trunk Test is a six-question audit that evaluates whether a page's navigation does its job. Imagine a user is dropped onto this page with no context — they have no memory of how they got here, no awareness of what site this is, no expectations. From a single look at the page, they should be able to answer all six questions:

1. **What site is this?** (Site ID visible and identifiable)
2. **What page am I on?** (Page name prominent, matches what the user clicked)
3. **What are the major sections?** (Primary nav visible and clear)
4. **What are my options at this level?** (Local nav or content choices obvious)
5. **Where am I in the scheme of things?** ("You are here" indicator, breadcrumbs)
6. **How can I search?** (Search box findable without hunting)

The test is harsh and intentional. Most pages fail. **A FAIL on the trunk test is a HIGH-impact finding regardless of how polished the visual design is.**

## Why it matters

Users land on pages from many sources — search results, shared links, deep links, browser history. They often arrive without the context the designer assumed. The trunk test simulates this real-world condition: can the page stand on its own?

Pages that pass the trunk test feel oriented; pages that fail feel disorienting. Disoriented users either click Back or click randomly until they accidentally find what they need (and then never trust the structure). Either way, the design has failed even if every other element is beautiful.

The Trunk Test is one of the most important audits for any product — and one of the most often skipped because teams design pages assuming users know the context.

## How to apply

1. **For every page in scope:** open it in an incognito window with no referrer. (Or imagine you've never seen this site before.)
2. **Answer the six questions one by one.** Be strict — "I think it's the dashboard but I'm not sure" counts as failure.
3. **Cover-everything-except-navigation test:** mentally cover all body content. Look only at the navigation chrome (logo, nav bar, breadcrumbs, page title, search). Can you still answer the six questions? If yes, the navigation is doing its job.
4. **Score: PASS / PARTIAL / FAIL**
   - **PASS:** all 6 answered clearly and confidently.
   - **PARTIAL:** 4-5 answered, 1-2 ambiguous or missing.
   - **FAIL:** 3 or fewer answered.
5. **A FAIL is a HIGH-impact finding.** Polish issues do not compensate. Fix the wayfinding.

## Examples

- **PASS:** GitHub repo page. (1) GitHub logo top-left = site ID. (2) Repo name + branch = page name. (3) Tabs (Code, Issues, PRs, Actions, Projects, etc.) = major sections. (4) File tree on left + recent commits on right = options at this level. (5) Breadcrumb + active tab underline = "you are here". (6) Search bar top center.
- **PASS:** Wikipedia article. (1) Wikipedia logo. (2) Article title huge. (3) Sidebar nav + "in other languages". (4) Article sections + table of contents. (5) Breadcrumb category. (6) Search top-right.
- **FAIL:** A "minimalist" portfolio site with a tiny logo, no nav menu, no page title, no breadcrumbs, hidden search. User can't tell what site this is, what page they're on, or what to do next.
- **PARTIAL:** A SaaS dashboard with a clear logo and search but missing breadcrumbs and an unclear page title. (1) ✓ (2) ? (3) ✓ (4) ✓ (5) ✗ (6) ✓. Score: PARTIAL.

## Common failure modes

- **Logo links nowhere or has no alt text** — site ID weak.
- **Page title missing or generic** ("Home" / "Dashboard" with no further context).
- **Navigation hidden behind hamburger on desktop** — sections not visible.
- **No breadcrumbs on deep pages** — user has no sense of depth.
- **Search hidden in a menu** — users can't find it.
- **Page title doesn't match what the user clicked** — disorienting context shift.

## Related entries

- `corpus/ux-principles/principles/navigation-as-wayfinding.md` — the principle this test operationalizes
- `corpus/ux-principles/audit/scoring-pass-partial-fail.md` — the scoring detail
- `corpus/evaluation-frameworks/review-sections/` — for framing in design reviews

## Anti-patterns

- Skipping the trunk test because "we know our users have context." Many users don't — search and shared links bring people in cold.
- Treating a FAIL as a polish issue. It's a high-impact finding; users get lost.
- "Minimalist" navigation where nothing is visible until interacted with. Loses every trunk-test question.
