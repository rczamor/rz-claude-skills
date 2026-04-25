---
name: Purple/Violet Gradients (AI Slop)
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/brand-system/identity/imagery-anti-patterns.md, corpus/ux-principles/audit/09-ai-slop/decorative-blobs.md, corpus/ux-principles/audit/03-color/palette-coherent.md]
---

# Purple/Violet Gradient Backgrounds

## What it is
Purple/violet/indigo gradient backgrounds, blue-to-purple color schemes, or any "AI startup launch site circa 2023" gradient — typically `linear-gradient(135deg, #6366F1, #8B5CF6, #EC4899)` or close variants. The single most-copied background pattern of every AI-generated landing page since GPT-4. The visual fingerprint of "I asked Claude/ChatGPT to design my site."

## Why it matters
Purple-to-pink gradients became the lazy-default for "AI/tech/futuristic" because every model trained on Midjourney v3, Vercel templates, and 2022 SaaS launch pages saw them on rotation. The gradient itself is fine in isolation — Linear, Anthropic, and Stripe all use purple at moments. But *only* purple, *every section*, with no intent or color theory, is the slop. It also clashes with the rest of the design — purple gradients don't sit well next to the icon-in-pastel-circle pattern they almost always travel with.

## How to apply
- Audit `linear-gradient(...)`, `radial-gradient(...)`, and `bg-gradient-to-{dir}` (Tailwind) declarations. Flag any using purple/violet/indigo (`#6366F1`, `#8B5CF6`, `#EC4899`, `#A855F7`, `#7C3AED`, etc.) as the dominant scheme.
- Replacement options:
  - **Drop the gradient.** Most pages improve with a single neutral background and well-chosen typography.
  - **Pick a brand color and own it.** A flat brand color or a subtle two-tone gradient *in your actual brand palette* reads as intentional.
  - **Use color theory** — analogous colors, split-complementary, or a single-hue with varied saturation/lightness. Not "purple + pink + blue because they look futuristic."
- If you legitimately want a purple-gradient moment, use it **once** (e.g., a single hero or a single CTA card) — not as the default page background, every section background, every card hover state.
- Consider the brand-system imagery anti-patterns catalog (`corpus/brand-system/identity/imagery-anti-patterns.md`) for the broader "AI startup gradient" pattern family.

## Examples (BAD vs. GOOD pairs)

BAD:
```css
body { background: linear-gradient(135deg, #6366F1, #A855F7, #EC4899); }
.hero { background: radial-gradient(ellipse at top, #8B5CF6 0%, #4F46E5 100%); }
.cta-section { background: linear-gradient(to bottom right, #7C3AED, #DB2777); }
/* Purple top to bottom, no break */
```

GOOD — restrained, brand-anchored:
```css
:root {
  --bg-primary: #0E0E10;       /* deep neutral */
  --accent: #FF6B35;           /* one brand color (Riché's Neural Architect orange) */
}
body { background: var(--bg-primary); color: #FAFAF8; }
.hero { background: var(--bg-primary); }   /* no gradient by default */
.cta-card {
  background: linear-gradient(135deg, var(--bg-primary), color-mix(in oklab, var(--accent), var(--bg-primary) 85%));
}  /* one gradient, in-brand, used in one place */
```

## Related entries
- `corpus/brand-system/identity/imagery-anti-patterns.md` — broader catalog of AI-aesthetic tells.
- `corpus/ux-principles/audit/09-ai-slop/decorative-blobs.md` — companion pattern (purple gradients usually live inside floating blobs).
- `corpus/ux-principles/audit/03-color/palette-coherent.md` — palette discipline.

## Anti-patterns
- Believing the gradient is "the brand." It's not the brand — it's *every other* AI startup's brand. Pick something that actually distinguishes you.
- Swapping purple-pink for green-cyan and thinking the slop is fixed — same lazy gradient, different hues, still slop.
- Gradient on every CTA button — turns the conversion point into noise.
