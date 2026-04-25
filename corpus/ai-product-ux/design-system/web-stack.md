---
name: Web Stack (AI Products)
domain: ai-product-ux
source_skill: product-design
entry_type: resource
length_target: 500
related: [corpus/ai-product-ux/design-system/admin-ui-stack.md, corpus/ai-product-ux/design-system/motion-rules.md, corpus/brand-system, corpus/ai-product-ux/patterns/context-display.md]
---

# Web Stack (AI Products)

## What it is
The default frontend stack for Riché's customer-facing AI product surfaces — richezamor.com, the Context Layer Demo, conference demos. **Next.js 15 + Tailwind CSS + shadcn/ui customized to the Neural Architect aesthetic.** Dark theme by default. Monospace accents for technical credibility. shadcn primitives skinned, not reinvented.

## Why it matters
A consistent stack across customer-facing surfaces is a force multiplier for one-person product velocity. Decisions about color, type, motion, and component anatomy are made once, applied everywhere. A new demo can ship in days because the foundations are ready. Buyers also notice the consistency — the demo and the marketing site feel like one product, not a portfolio.

## How to apply
1. **Next.js 15 App Router.** Server components for context-heavy surfaces; client components for interactive AI panels. RSC streaming pairs naturally with model streaming.
2. **Tailwind CSS, no custom CSS.** Utility-first with a small set of custom design tokens. Colors and spacing live in `tailwind.config` matching `corpus/brand-system`.
3. **shadcn/ui as the component baseline.** Copy-in primitives, then skin. Don't fight the abstractions.
4. **Neural Architect customization.** Near-black backgrounds (#0a0a0a–#1a1a1a). High-contrast text. Accent colors (single dominant accent + one warning) used sparingly. JetBrains Mono or similar for monospace accents.
5. **Generous whitespace between sections; tight within related groups.** The decision-maker audience wants density without claustrophobia.

## Examples
1. **richezamor.com.** Full Next.js 15 + Tailwind + shadcn build with Neural Architect skin. The reference implementation — every other AI product surface inherits from it.
2. **Context Layer Demo.** Same stack. Demonstrates the design system applied to interactive AI surfaces — sources panels, reasoning sidebars, confidence chips all built from skinned shadcn primitives.
3. **Conference demo apps.** Same stack, scaffolded in hours. The stack is the moat against ramp-up tax.

## Related entries
- `corpus/ai-product-ux/design-system/admin-ui-stack.md` — the internal-facing counterpart (HTMX)
- `corpus/ai-product-ux/design-system/motion-rules.md` — motion language for this stack
- `corpus/brand-system` — the visual identity this stack expresses
- `corpus/ai-product-ux/patterns/context-display.md` — the surface this stack is optimized to render

## Anti-patterns
- **Stack drift across products.** Each new demo picks a fresh framework. Velocity dies in setup; visual coherence dies in delivery.
- **Custom CSS over Tailwind.** Every product writes its own utilities. Maintenance compounds; the design system fragments.
