---
name: Context as Product Surface
domain: ai-product-ux
source_skill: product-design
entry_type: concept
length_target: 600
related: [corpus/ai-product-ux/patterns/context-display.md, corpus/ai-product-ux/context/sources-panel.md, corpus/ai-product-ux/context/correction-interface.md, corpus/ai-product-ux/context/context-quality-display.md, corpus/voice/hook-data-is-not-context.md, corpus/pm-frameworks/ai-product-pm/five-step-context-generation.md]
---

# Context as Product Surface

## What it is
A concept. Context display is not a debug panel — it is the product. The treatment, prominence, and polish of the context surface should match (or exceed) the treatment of the AI output itself. Treating context as developer metadata, hidden behind a toggle, communicates that context is incidental to the experience. Treating context as a primary surface communicates that context is the point.

## Why it matters
This is the load-bearing UX expression of Riché's thesis. If the AI output sits center stage and the context sits in a collapsed sidebar with monospace text, the message to the user is: "the context is plumbing, the answer is the product." Buyers internalize that and treat context as something to ignore. If the context sits at parity with the answer — same typography, same prominence, same polish — the message becomes: "context is the product; the answer is a function of it." Buyers internalize *that* and start asking for context-quality features in their next contract.

## How to apply
1. **Match typography between context and output.** Don't give the answer beautiful prose and the sources monospace 12px. They are peers.
2. **Spend equal review time on both surfaces.** If you're polishing the answer card and ignoring the sources panel, the imbalance shows.
3. **Lead the product tour with context, not output.** What the buyer sees first frames everything. Show them the context surface; the output is the consequence.
4. **Use the same motion vocabulary on both.** When the answer streams in, the context streams in. Design system parity.

## Examples
1. **Context Layer Demo's center-stage context.** The demo's primary surface is the five-step context flow — sources, scores, corrections — with the synthesis as the consequence. This inverts the typical AI-product layout (output center, context in a sidebar). Buyers consistently describe the demo as "different" — the layout itself is the argument.
2. **Suzy Decision Engine's panel-data prominence.** Insight cards lead with respondent counts, segments, and consistency before the headline insight. The data is not subordinate to the conclusion — they share visual weight.
3. **Counter-example: most "AI search" products.** Output huge, citations as 1pt superscripts. Visual hierarchy says "trust the answer." Riché's products invert this on purpose.

## Related entries
- `corpus/ai-product-ux/patterns/context-display.md` — the pattern this concept anchors
- `corpus/ai-product-ux/context/sources-panel.md` — the implementation of context-as-surface
- `corpus/ai-product-ux/context/correction-interface.md` — the loop that requires context to be a surface
- `corpus/ai-product-ux/context/context-quality-display.md` — the scores that earn surface real estate
- `corpus/voice/hook-data-is-not-context.md` — the thesis
- `corpus/pm-frameworks/ai-product-pm/five-step-context-generation.md` — the framework

## Anti-patterns
- **Debug-panel framing.** Putting context behind a "developer tools" toggle. The framing tells users not to look.
- **Visual demotion.** Same content, smaller type, gray colors, monospace. The hierarchy says "this isn't the product." The user agrees.
