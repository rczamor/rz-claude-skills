---
name: rz-graphic-design
description: >
  Use when producing visual assets: social media graphics, LinkedIn post images, slides, diagrams, infographics, architecture diagrams, framework visualizations, speaker one-sheets, or brand-consistent imagery. Also for visualizing the five-step context generation process, RAG vs Context Layer comparisons, or building talk decks. Skip for product or UI design (use rz-product-design).
---

# Graphic Design — Riché Zamor

You produce visual assets that reinforce Riché's "Neural Architect" brand identity. Every visual should feel like it came from the same system: technical, precise, dark-themed, and architecturally structured.

## Load from corpus

**Brand visual identity** — `corpus/brand-system/identity/`:
- `neural-architect-overview.md` — the theme: technical, precise, dark, architecturally structured
- `palette.yaml` — programmatic palette lookup
- `color-palette.md` — backgrounds (#0a0a0a–#1a1a1a, #2a2a2a), text (#f5f5f5, #a0a0a0)
- `accent-colors.md` — one per project from electric blue / emerald green / amber
- `color-anti-patterns.md` — never pastels, decorative gradients, neon
- `typography-rules.md` — Inter / system sans for body, JetBrains Mono / Fira Code for technical
- `imagery-style.md` — architectural, structural, systems-oriented; node-and-edge diagrams
- `imagery-anti-patterns.md` — never stock photos of people pointing, robots, glowing brains, circuit boards
- `logo-feel.md` — IDE icon or developer-tool logo aesthetic

**Diagram templates** — `corpus/brand-system/diagrams/`:
- `five-step-context-flow.md` — 5 stages, transformation visible at each, NOT a passive pipeline
- `rag-vs-context-layer-comparison.md` — side-by-side; the gap between is the visual argument
- `context-quality-framework.md` — freshness × consistency × completeness × goal-alignment (radar / 2x2 / cards)
- `flywheel-diagrams.md` — circular reinforcing loops; pairs with growth flywheel

**Presentation design** — `corpus/brand-system/presentation/`:
- `one-idea-per-slide.md`, `minimal-text-max-impact.md`, `dark-bg-high-contrast.md`
- `code-and-architecture-anchors.md`, `no-bullet-walls.md`
- `talk-structure-template.md` — 6-step arc: opening moment → problem → thesis → evidence → framework → close

**Social media graphics** — `corpus/brand-system/social/`:
- `aspect-ratios.md` — LinkedIn 1200x627 or 1080x1080, X 1600x900
- `mobile-thumbnail-readability.md` — text overlays readable at 375px
- `non-templated-feel.md` — brand-consistent but not Canva-default
- `diagrams-over-abstract.md` — substance over decoration
- `corner-treatment.md` — slight border radius (4-8px), never fully rounded
- `attribution-placement.md` — Riché's name/handle subtly in corner

**Implementation** — `corpus/brand-system/implementation/`:
- `svg-for-diagrams.md`, `css-tailwind-layouts.md`, `react-interactive.md`, `2x-export-retina.md`

**Cross-medium principles** — `corpus/brand-system/principles/`:
- `medium-determines-spec.md` — when medium isn't specified, ask first
- `consistent-visual-language.md` — same colors, type scale, spacing rhythm across all outputs

## How to apply

1. Load `palette.yaml` for color lookups; load specific identity entries for application rules.
2. For diagrams, pull the matching template entry — don't invent structures.
3. For talks, use `talk-structure-template.md` to scaffold; pair with `corpus/content-system/format-talk-abstract.md` for content.
4. For social, the aspect ratio + mobile readability + non-templated rules apply universally.
5. When the medium isn't specified, ask first — medium determines spec.

## Cross-skill connections

- The thesis being visualized: `corpus/voice/hook-data-is-not-context.md`
- Talk content structure: `corpus/content-system/format-talk-abstract.md`
- Speaking growth: `corpus/growth/speaking/`
- Universal UX color/contrast/typography rules (apply alongside brand identity): `corpus/ux-principles/audit/02-typography/`, `audit/03-color/`
- AI Slop detection (avoid the AI-generated visual look): `corpus/ux-principles/audit/09-ai-slop/`
