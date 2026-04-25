---
name: Color Anti-Patterns
domain: brand-system
source_skill: graphic-design
entry_type: rule
length_target: 300-800
related: [corpus/brand-system/identity/color-palette.md, corpus/brand-system/identity/accent-colors.md, corpus/brand-system/identity/palette.yaml, corpus/brand-system/identity/imagery-anti-patterns.md]
---

# Color Anti-Patterns

## What it is
Three categories of color use that are disqualified from every Riché asset, regardless of medium: pastels, decorative gradients, and neon colors. These aren't aesthetic preferences — each one signals a brand position that contradicts the Neural Architect identity (technical practitioner, not consumer-marketing brand).

## Why it matters
A single off-brand color choice can collapse the practitioner positioning that the rest of the system is doing work to establish. A pastel-pink accent on a context architecture diagram tells the viewer "this is content marketing about AI," not "this is the person who builds the systems." The forbidden categories are forbidden because they each carry a strong signal in the opposite direction:

- **Pastels** signal "lifestyle / wellness / consumer SaaS."
- **Decorative gradients** signal "Web3 launch deck" or "AI marketing template."
- **Neon** signals "club poster / cyberpunk aesthetic / generic AI imagery."

## How to apply
- **No pastels, ever.** Mint, peach, lavender, baby blue — all disqualified. If a color reads as "soft," it doesn't belong.
- **No decorative gradients.** A gradient as a background fill, a gradient as a CTA button, a gradient on text — all disqualified. The only acceptable gradient is a functional one inside a chart (e.g., a heatmap legend) where the gradient encodes data.
- **No neon.** Hot pink, electric purple, lime green-yellow, cyber-cyan — all disqualified. The accent palette (electric blue, emerald, amber) is calibrated to feel technical without crossing into neon.
- **No multi-color accents in the same asset.** Even when the colors are individually on-brand, using all three at once breaks the "one accent per project" rule and reads as Canva.

## Examples
1. **Rejected: pastel-coral CTA button on a dark deck slide.** Replace with the project's chosen accent (blue/green/amber) or with a white outlined button.
2. **Rejected: purple-to-pink gradient banner on a LinkedIn post.** Replace with a flat near-black background and the diagram doing the work.
3. **Rejected: neon-green "AI" badge on a section header.** Replace with a JetBrains Mono label in `#a0a0a0` — the typography signals "AI/technical" without the visual cliché.

## Related entries
- `corpus/brand-system/identity/color-palette.md` — what to use instead
- `corpus/brand-system/identity/accent-colors.md` — the on-brand accent options
- `corpus/brand-system/identity/imagery-anti-patterns.md` — visual cliches that often arrive paired with off-brand color
- `corpus/brand-system/identity/palette.yaml` — machine-readable anti-pattern list

## Anti-patterns
- "But this client/partner brand is pastel — we should match." Riché's identity does not co-brand into pastels. Either the asset is co-branded with neutral chrome, or the partner brand sits in a clearly delineated section.
- Using a forbidden color "ironically" in a meme post. The viewer doesn't read irony at thumbnail size — they read the brand signal.
