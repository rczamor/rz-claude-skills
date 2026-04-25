---
name: 2x Retina Export
domain: brand-system
source_skill: graphic-design
entry_type: rule
length_target: 300-500
related: [corpus/brand-system/social/aspect-ratios.md, corpus/brand-system/implementation/svg-for-diagrams.md, corpus/brand-system/implementation/react-interactive.md, corpus/brand-system/social/mobile-thumbnail-readability.md]
---

# 2x Retina Export

## What it is
Static exports of any visual asset render at **2x** the target display resolution. A 1080x1080 social graphic exports as a 2160x2160 PNG. A 1200x627 LinkedIn feed image exports as a 2400x1254 PNG. The platform downsamples for display, but the high-DPI source ensures sharp rendering on retina screens.

## Why it matters
Modern devices are predominantly retina (iPhones since 2010, MacBooks for over a decade, most non-budget Android devices). A 1x export looks soft and slightly blurry on these screens — a quiet-but-real signal of low effort. A 2x export looks crisp on retina and downsamples cleanly to non-retina. Cost: a moderately larger file, well within platform limits. Benefit: every viewer sees the asset at its intended sharpness.

## How to apply
- **Default export multiplier: 2x.** A 1080x1080 design exports as a 2160x2160 PNG. A 1200x627 design exports as 2400x1254. Etc.
- **Source from SVG when possible.** SVG renders at any resolution without quality loss, so the 2x export is a render-time setting, not a quality compromise.
- **Format: PNG for static social, JPG only when file size is critical.** PNG preserves text crispness; JPG introduces artifacts around sharp typographic edges. The dark backgrounds make JPG artifacts especially visible.
- **Filename convention.** Suffix `@2x` so future you knows what you have: `five-step-flow-1080@2x.png`, `rag-comparison-1200@2x.png`.
- **Don't go higher than 2x.** 3x or 4x exports are mostly platform-rejected for size, and the benefit on most screens is invisible. 2x is the sweet spot.
- **Exception: print and stage screens.** For conference deck exports that may project at 4K+, render at 3x. For everything else, 2x.

## Examples
1. **LinkedIn carousel slide design canvas: 1080x1080. Final export: 2160x2160 PNG @2x.** Uploads cleanly to LinkedIn, displays sharp on retina screens.
2. **Blog post hero image design canvas: 1200x627. Final export: 2400x1254 PNG @2x.** Embedded inline in the blog post; displays sharp on the website's hero placement.
3. **Conference talk slide deck. Source slides: 1920x1080 (16:9). When exporting to PNG for sharing, render at 2x: 3840x2160.** Holds up on 4K projection.

## Related entries
- `corpus/brand-system/social/aspect-ratios.md` — the design canvases this rule applies to
- `corpus/brand-system/implementation/svg-for-diagrams.md` — where the high-DPI source originates
- `corpus/brand-system/implementation/react-interactive.md` — exporting React-rendered visuals at 2x
- `corpus/brand-system/social/mobile-thumbnail-readability.md` — sibling rule on visual quality

## Anti-patterns
- Exporting at 1x because "the platform compresses anyway." Compression on a 1x source produces visible softness; compression on a 2x source still produces a sharp result.
- Uploading 4x exports because "more pixels is better." Platforms reject or auto-downscale, and the file size is a sharing penalty.
