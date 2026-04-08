---
name: graphic-design
description: >
  Use this skill whenever Riché needs visual assets: social media graphics, LinkedIn post images, presentation slides, diagrams, infographics, architecture diagrams, framework visualizations, speaker one-sheets, brand assets, or any visual content. Also trigger when he needs to visualize the five-step context generation process, create comparison diagrams (RAG vs. Context Layer), build slide decks for talks, or create any visual that supports his personal brand. Trigger for any request involving visual design, graphics, illustrations, charts for content, or brand-consistent imagery.
---

# Graphic Design — Riché Zamor

You produce visual assets that reinforce Riché's "Neural Architect" brand identity. Every visual should feel like it came from the same system: technical, precise, dark-themed, and architecturally structured.

## Brand Visual Identity

**Color palette:**
- Primary backgrounds: near-black (#0a0a0a to #1a1a1a)
- Secondary backgrounds: dark gray (#2a2a2a for cards, panels)
- Primary text: high-contrast white (#f5f5f5)
- Secondary text: muted gray (#a0a0a0)
- Accent: select one per project from a technical palette (electric blue, emerald green, amber). Use sparingly for interactive elements, data highlights, and key diagram nodes.
- Never: pastels, gradients for decoration, neon colors

**Typography:**
- Clean, modern sans-serif for body text (Inter, system fonts)
- Monospace for technical elements (JetBrains Mono, Fira Code)
- Never script or decorative fonts
- Large type sizes for headlines in presentations, smaller dense type for diagrams

**Imagery style:**
- Architectural, structural, systems-oriented
- Node-and-edge diagrams, layer visualizations, flow diagrams
- Clean geometric shapes, not organic or hand-drawn
- Never stock photos of people pointing at screens
- Never generic AI imagery (robots, glowing brains, circuit boards)
- Never clip art or Canva-default visual elements

**Logo/branding:** "Neural Architect" theme. Consistent with richezamor.com dark theme. If generating brand marks, they should feel like they could be an IDE icon or a developer tool logo.

## Diagram Templates

These are recurring visual needs. When Riché asks for any of these, use the established structure.

### Five-Step Context Generation Flow

Curation, Synthesis, Consolidation, Prioritization, Intelligent Storage. This is NOT a simple left-to-right pipeline. Each step should have visual weight that communicates it's an active process, not passive data flow.

Structure:
- Five distinct stages, each with its own visual container
- Show transformation happening at each stage (input looks different from output)
- Use iconography or visual metaphors that distinguish active processing from simple data movement
- Arrows between stages should suggest transformation, not just flow
- Label each stage with a one-line description of what happens there

### RAG vs. Context Layer Comparison

Side-by-side showing what typical RAG does vs. what the full context generation process does.

Left side (RAG): Chunk, Embed, Store, Retrieve. Simple pipeline, minimal transformation.
Right side (Context Layer): Five steps with visible transformation at each stage.

The gap between the two sides is the visual argument. The Context Layer side should look richer, more sophisticated, more intentional.

### Context Quality Framework

Visual showing the dimensions of context quality:
- Freshness (is it current?)
- Consistency (does it align with other context?)
- Completeness (does it cover the decision space?)
- Goal-alignment (is it relevant to the current task?)

Can be rendered as a radar chart, a 2x2 matrix, or a card-based layout depending on the use case.

### Flywheel Diagrams

For audience development and content strategy. Circular flow showing reinforcing loops. Used in conjunction with the `growth-marketing` skill's flywheel model.

## Presentation Design

For conference talks and pitch decks:

- **One idea per slide.** If a slide needs a paragraph to explain, it's two slides.
- **Minimal text, maximum visual impact.** The speaker provides the explanation; the slide provides the anchor.
- **Dark backgrounds, high-contrast text.** Consistent with the brand palette.
- **Code snippets and architecture diagrams as visual anchors.** These signal practitioner credibility.
- **Never bullet-point walls.** If you need a list, make it visual (icons, cards, a flow).
- **Slide dimensions:** Default to 16:9. Optimize for projection (large type, high contrast).
- **Slide count:** For a 20-minute talk, aim for 25-35 slides. More slides with less content each is better than fewer dense slides.

### Talk Structure Template

1. Opening: a specific moment or failure (not "today I'll talk about...")
2. The problem: what most people get wrong
3. The thesis: Riché's alternative framing
4. The evidence: proof points, architecture, demos
5. The framework: what the audience can take home
6. The close: one clear takeaway, stated directly

## Social Media Graphics

For LinkedIn/X visual assets:

- **Aspect ratios:** LinkedIn feed images: 1200x627 or 1080x1080. X images: 1600x900.
- **Text overlays must be readable at mobile thumbnail size.** Test at 375px width.
- **Brand-consistent but not templated.** Avoid looking like Canva defaults. Each graphic should feel crafted, not generated from a template.
- **Diagrams and frameworks work better than abstract graphics.** Riché's audience wants substance in visuals, not decoration.
- **Consistent corner treatment:** Slight border radius (4-8px), never fully rounded.
- **Always include Riché's name or handle** subtly in the corner for attribution when shared.

## Implementation Notes

When creating visuals in code (SVG, HTML/CSS, React components):

- Use SVG for diagrams and icons. Clean paths, consistent stroke widths.
- Use CSS/Tailwind for layout-based visuals (comparison tables, card layouts).
- Use React components for interactive visualizations on richezamor.com.
- Export static versions at 2x resolution for retina displays.
- Maintain a consistent visual language across all outputs: same colors, same type scale, same spacing rhythm.

When Riché needs a visual and the medium isn't specified, ask: is this for a LinkedIn post, a slide deck, the website, or something else? The medium determines the dimensions, density, and interaction model.

Cross-reference the `product-design` skill for UI-specific visual decisions and the `copywriting` skill to ensure any text in visuals matches Riché's voice and terminology.
