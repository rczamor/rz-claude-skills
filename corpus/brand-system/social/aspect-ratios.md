---
name: Social Media Aspect Ratios
domain: brand-system
source_skill: graphic-design
entry_type: resource
length_target: 300-500
related: [corpus/brand-system/social/mobile-thumbnail-readability.md, corpus/brand-system/social/non-templated-feel.md, corpus/brand-system/principles/medium-determines-spec.md, corpus/brand-system/implementation/2x-export-retina.md]
---

# Social Media Aspect Ratios

## What it is
Standard dimensions for social graphics across the platforms Riché publishes on. These are the canonical export sizes — every social asset should match one of these ratios, never something custom.

**LinkedIn:**
- Feed image: **1200x627** (landscape, 1.91:1) — for posts where the image is the focal point and a link card is not in play.
- Square: **1080x1080** (1:1) — for carousel slides and standalone square graphics.

**X (Twitter):**
- Feed image: **1600x900** (16:9 landscape).

**Cross-platform:**
- Both LinkedIn and X downsize cleanly from the larger dimensions; export at the higher size and let the platform compress.
- For the LinkedIn carousel format specifically, every slide must be 1080x1080 — mixed dimensions break the carousel.

## Why it matters
Aspect ratios determine what text size is readable, what gets cropped at thumbnail, and what appears in the in-feed preview. A graphic designed for 1080x1080 and posted to X gets cropped to a 16:9 preview that hides half the content. Designing to platform-native ratios ensures the image lands in the feed exactly as intended — no surprise crops, no readability cliffs.

## How to apply
- **Decide the platform first.** Before designing, know whether the target is LinkedIn feed, LinkedIn carousel, or X. The medium determines the canvas.
- **Use the canonical sizes.** No custom dimensions. The list above is the full set.
- **Cross-post requires re-render.** A LinkedIn 1080x1080 graphic posted to X needs a 1600x900 version, not a thumbnail crop. Re-render at the new ratio.
- **Export at 2x retina.** A 1200x627 graphic exports at 2400x1254 to look sharp on high-DPI screens. See `corpus/brand-system/implementation/2x-export-retina.md`.
- **Test the preview.** Before publishing, view the asset at the platform's actual feed thumbnail size to confirm legibility.

## Examples
1. **LinkedIn carousel of the Five-Step Context Flow.** Seven slides, each 1080x1080. Slide 1: title. Slides 2–6: one stage per slide. Slide 7: takeaway + CTA.
2. **LinkedIn feed post with the RAG vs. Context Layer comparison.** Single 1200x627 landscape image. The compact two-column layout fits the wide aspect.
3. **X post with the Context Quality Framework radar chart.** Single 1600x900 image, the radar chart sized to fill 60% of the frame, attribution in the lower-right corner.

## Related entries
- `corpus/brand-system/social/mobile-thumbnail-readability.md` — what's legible at preview size
- `corpus/brand-system/social/non-templated-feel.md` — how to make these dimensions look crafted
- `corpus/brand-system/principles/medium-determines-spec.md` — the meta-rule
- `corpus/brand-system/implementation/2x-export-retina.md` — export resolution

## Anti-patterns
- Designing once at a custom size and uploading to multiple platforms. The crops will be wrong on at least one.
- Using portrait (1080x1350) for LinkedIn feed. Portrait works on Instagram; on LinkedIn it gets letterboxed and reads as off-platform.
