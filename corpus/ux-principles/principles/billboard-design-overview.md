---
name: Billboard Design for Interfaces
domain: ux-principles
source_skill: design-review
entry_type: framework
length_target: 300-800
related: [corpus/ux-principles/principles/users-scan-not-read.md, corpus/ux-principles/principles/navigation-as-wayfinding.md, corpus/ux-principles/audit/01-hierarchy/clear-focal-point.md, corpus/ux-principles/audit/01-hierarchy/visual-noise.md]
---

# Billboard Design for Interfaces

## What it is

A framework for designing interfaces as if they were billboards passed at 60 mph: every element earns its place by being instantly readable, instantly understood, and instantly actionable. Users do not study interfaces; they glance at them. The five sub-rules of billboard design make this glance productive.

1. **Use conventions.** Logo top-left, nav top/left, search = magnifying glass. Don't innovate on navigation to be clever.
2. **Visual hierarchy is everything.** Related things visually grouped, nested things visually contained, more important = more prominent.
3. **Make clickable things obviously clickable.** Don't rely on hover for discoverability — especially on mobile.
4. **Eliminate noise.** Three sources: shouting (too many things competing), disorganization, clutter. Fix by removal.
5. **Clarity trumps consistency.** If clarity requires slight inconsistency, choose clarity.

## Why it matters

Designers who don't think in billboards build interfaces that reward sustained attention. Real users don't grant sustained attention; they glance and move on. A page that requires study to navigate is a failed billboard, regardless of how elegant it looks at rest. The billboard frame forces the question: would a user driving past at 60 mph understand this page? If not, simplify until they would.

## How to apply

1. **Glance test.** Show the page to someone for 5 seconds, hide it, ask what they remember. The dominant element should be the dominant message.
2. **Use convention by default.** Innovate on navigation only when you KNOW you have a better idea. Otherwise, use what every site uses — logo top-left, search top-right, nav at the top or left.
3. **Make clickable things obviously clickable.** Shape, location, and formatting (color, underlining) must signal clickability without requiring hover. Especially on mobile, where hover doesn't exist.
4. **Start with the assumption everything is visual noise.** Guilty until proven innocent. Each element must justify its existence by helping the scan.
5. **When clarity and consistency conflict, pick clarity.** A button styled slightly differently to make it obviously primary beats a "consistent" button no one finds.

## Examples

- **GOOD:** Amazon's product page — logo top-left, search bar prominent, "Buy now" button in unmistakable orange. You scan it in 2 seconds.
- **BAD:** A "minimal" portfolio site where the navigation is hidden behind a tiny dot, the logo is in a corner, and clicking is a guessing game.
- **GOOD:** Stripe's homepage hero — one headline, one CTA, one product visualization. Billboard-grade clarity.
- **BAD:** A SaaS landing page with 12 competing CTAs, three carousels, and a hero video. Nothing is loudest because everything shouts.

## Related entries

- `corpus/ux-principles/principles/users-scan-not-read.md`
- `corpus/ux-principles/principles/navigation-as-wayfinding.md`
- `corpus/ux-principles/audit/01-hierarchy/clear-focal-point.md`
- `corpus/ux-principles/audit/01-hierarchy/visual-noise.md`

## Anti-patterns

- Innovating on navigation placement to be distinctive. Distinctive ≠ usable.
- Treating consistency as more important than clarity. Consistency that confuses is worse than inconsistency that clarifies.
