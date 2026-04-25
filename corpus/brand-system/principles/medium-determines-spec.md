---
name: Medium Determines Spec
domain: brand-system
source_skill: graphic-design
entry_type: rule
length_target: 400-600
related: [corpus/brand-system/principles/consistent-visual-language.md, corpus/brand-system/social/aspect-ratios.md, corpus/brand-system/implementation/2x-export-retina.md, corpus/brand-system/identity/neural-architect-overview.md]
---

# Medium Determines Spec

## What it is
When Riché needs a visual and the medium isn't specified, **ask first**. Is this for a LinkedIn post, a slide deck, the website, an email signature, a print one-sheet, a conference badge? The medium determines the dimensions, the density, the type sizes, and the interaction model. A graphic that works on LinkedIn fails on a slide and vice versa.

## Why it matters
Visual assets that work everywhere usually work nowhere. A LinkedIn carousel slide is 1080x1080, optimized for thumbnail readability with bold headlines. A conference talk slide is 1920x1080, optimized for projection at distance with even bolder type. A website hero panel is responsive, sized for desktop and mobile, optimized for scroll-into-view interaction. Asking "what medium" up front prevents wasted iteration: design once for the right canvas instead of three times for a wrong one.

## How to apply
The default questions before designing anything:

1. **What's the medium?** LinkedIn feed, LinkedIn carousel, X post, conference slide, blog inline, website hero, email signature, print, other.
2. **What are the dimensions?** Pull from `corpus/brand-system/social/aspect-ratios.md` or the medium's spec.
3. **What's the viewing context?** Mobile feed scroll? Desktop conference projection? Inline within a long-form blog? Each implies a different density.
4. **What's the interaction model?** Static, hover-reveal, animated build, fully interactive?
5. **What's the dwell time?** Feed scroll = 1–3 seconds. Slide = 30 seconds. Blog inline = 5–15 seconds. Website hero = 5–10 seconds.

Once those five answers are settled, the spec follows: type size, label density, animation use, export resolution.

**The questions to ask Riché when the medium is unclear:**
- "Is this for a LinkedIn post, a slide, or the website?"
- "If LinkedIn — feed image or carousel?"
- "If a slide — talk title slide or body slide?"
- "If website — hero or inline?"

Don't guess. Asking once saves three rework rounds.

## Examples
1. **A request for "a Five-Step Context Flow visual" with no medium specified.** Wrong move: design at 1080x1080 and ship. Right move: ask "is this for the keynote next week, the LinkedIn carousel, or the website?" — each produces a different render of the same diagram.
2. **A request for "a quote card."** Ask: LinkedIn feed (1200x627) or square (1080x1080)? The framing changes — landscape needs more horizontal space for the typography, square supports a more dramatic single-line treatment.
3. **A request for "a deck graphic."** Ask: pitch deck (sales context, denser slides) or talk deck (audience context, sparser slides)? The two have different density expectations.

## Related entries
- `corpus/brand-system/principles/consistent-visual-language.md` — the sibling principle that handles cross-medium consistency
- `corpus/brand-system/social/aspect-ratios.md` — the canonical sizes for each medium
- `corpus/brand-system/implementation/2x-export-retina.md` — export resolution is medium-dependent
- `corpus/brand-system/identity/neural-architect-overview.md` — what stays consistent across mediums

## Anti-patterns
- Designing once at "a generic size" and exporting to multiple platforms. The crops, the type sizes, and the legibility break on at least one of them.
- Treating "ask first" as a delay. It's not — it's the fastest path. One clarifying question saves three rounds of "this doesn't fit there."
