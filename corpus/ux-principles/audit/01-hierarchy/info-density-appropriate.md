---
name: Information Density Appropriate for Content Type
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/principles/users-scan-not-read.md, corpus/ux-principles/audit/04-spacing/rhythm.md]
---

# Information Density Appropriate for Content Type

## What it is

Different content types require different densities. A marketing page rewards low density (hero, headline, lots of whitespace). A power-user dashboard rewards high density (Bloomberg terminal, Linear, GitHub PR view). The rule: density should match the content type and audience expectation. Low-density marketing pages with sparse content read as confident; low-density dashboards with sparse content read as wasteful and force users to scroll forever.

## Why it matters

Density mismatch is jarring. A marketing site that crams 12 paragraphs into a hero feels desperate. A pro tool that surrounds two metrics with a screen of whitespace feels patronizing. Audiences come with implicit expectations:

- **Marketing / consumer / first-time:** lower density, more breathing room, hierarchy by whitespace.
- **Pro / dashboard / repeat-use:** higher density, hierarchy by typography and grouping.
- **Reference / docs:** medium density, scannable structure.

Designing for the wrong density telegraphs that you don't understand your user.

## How to apply

1. **Identify the audience.** First-time visitors? Power users? Mixed?
2. **Match the density.** Hero pages get whitespace. Dashboards get information. Docs get scannable chunks.
3. **Don't apply marketing-page restraint to a power tool.** Bloomberg users want every pixel productive.
4. **Don't apply dashboard density to a marketing site.** First-time users want breathing room.

## Examples

- **GOOD:** Stripe's pricing page — moderate density, generous spacing, headline-first. Marketing density.
- **GOOD:** Linear's issue board — high density, every pixel doing work, no decorative whitespace. Power-user density.
- **BAD:** A SaaS dashboard with marketing-page whitespace — three numbers per screen, requiring constant scrolling. User abandons.
- **BAD:** A landing page with dashboard-style density — 14 sections crammed above the fold. User overwhelmed.

## Related entries

- `corpus/ux-principles/principles/users-scan-not-read.md`
- `corpus/ux-principles/audit/04-spacing/rhythm.md`

## Anti-patterns

- "More whitespace is always better." Not on a power tool. Whitespace there is wasted screen.
- "Information density makes us look professional." Not on a marketing page. There it makes you look desperate.
