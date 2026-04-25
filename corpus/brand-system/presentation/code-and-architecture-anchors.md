---
name: Code and Architecture Anchors
domain: brand-system
source_skill: graphic-design
entry_type: rule
length_target: 400-600
related: [corpus/brand-system/diagrams/five-step-context-flow.md, corpus/brand-system/identity/imagery-style.md, corpus/brand-system/identity/typography-rules.md, corpus/brand-system/presentation/minimal-text-max-impact.md, corpus/voice/]
---

# Code and Architecture Anchors

## What it is
When a slide needs visual weight, default to a code snippet or an architecture diagram — not a stock illustration, not a pull-quote, not a metaphorical image. These two visual elements signal practitioner credibility: only someone who builds the system can show you the system or the code that runs it.

## Why it matters
The audience Riché is talking to filters fast. A slide with a stock illustration registers as "talker about technology." A slide with a real code snippet or a real architecture diagram registers as "person who built this." That distinction is what gets the audience to lean in. It's also what differentiates Riché from the broader pool of AI/PM speakers — most of them don't have shippable artifacts to put on a slide. Use the artifacts.

## How to apply
- **Code snippets.** Use real, runnable code. Render in JetBrains Mono on a `#1a1a1a` panel with a slight border (1px `#2a2a2a`). Keep snippets short — 6 to 12 lines max. Highlight the load-bearing line with the project's accent color. No fake or pseudo-code.
- **Architecture diagrams.** Use real systems. Show the actual layer structure, the actual component names, the actual data flow. Geometric, clean, white strokes on dark, single accent on the load-bearing component.
- **Annotate with restraint.** A small monospace label with an arrow can call out a specific line or component. Avoid full annotation overlays — they fight the diagram.
- **Don't recreate the source code as a graphic.** If the snippet is real, render the actual text. Don't substitute a "stylized" version.
- **Pair with one-line headline.** The slide headline names the takeaway in plain language; the code or diagram is the proof.

## Examples
1. **A talk slide on context curation.** Headline: "Curation is a filter step, not a fetch step." Below: a 10-line Python snippet of the curation function, with the filter line highlighted in electric blue. The code is the proof of the headline.
2. **A talk slide on the Context Layer architecture.** Headline: "The Context Layer is five stages, not one." Below: an architecture diagram showing the five stages as system components with named connections. No additional text needed.
3. **A talk slide on evaluation.** Headline: "We grade context on four dimensions." Below: a screenshot from Riché's actual evaluation rubric (real, with real metrics), one row highlighted in the accent color.

## Related entries
- `corpus/brand-system/diagrams/five-step-context-flow.md` — the diagram type that anchors many slides
- `corpus/brand-system/identity/imagery-style.md` — geometric vocabulary for diagrams
- `corpus/brand-system/identity/typography-rules.md` — monospace usage for code
- `corpus/brand-system/presentation/minimal-text-max-impact.md` — why these anchors replace prose
- `corpus/voice/` — the verbal positioning these visual anchors reinforce

## Anti-patterns
- Pseudo-code that's "cleaner than the real thing." If the audience asks where the code lives, the answer should be "in production." Pseudo-code can't survive that question.
- Architecture diagrams that hide the actual system because "it's too messy." The mess is the point — it shows the system shipped. Clean it up visually (consistent strokes, alignment) but don't sanitize the structure.
