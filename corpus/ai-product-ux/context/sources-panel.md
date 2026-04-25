---
name: Sources Panel
domain: ai-product-ux
source_skill: product-design
entry_type: template
length_target: 600
related: [corpus/ai-product-ux/patterns/context-display.md, corpus/ai-product-ux/context/correction-interface.md, corpus/ai-product-ux/context/context-quality-display.md, corpus/ai-product-ux/context/audit-log.md, corpus/voice/hook-data-is-not-context.md]
---

# Sources Panel

## What it is
A template UI for displaying the sources informing an AI answer — typically a side panel or expandable section that lists each source with title, snippet, retrieval rank, and a click-through to the underlying document. The panel is clickable, scrollable, and inspectable. The minimum bar for context display.

## Why it matters
Without a sources panel, AI answers float free of their evidence. A user who wants to verify must trust or distrust the whole answer. With a sources panel, verification becomes targeted — the user clicks the one citation that surprised them, reads the source, and either updates the AI's answer in their mind or files a correction. The panel turns a black-box output into an inspectable claim.

## How to apply
1. **Default to right-rail or bottom-drawer placement.** Persistent enough to invite inspection, not so dominant that it crowds the answer.
2. **Show retrieval rank, not just the source.** "Source 1 of 7" tells the user how the AI prioritized — and gives them an entry point if they disagree.
3. **Snippet, not full text.** A 2-3 line excerpt with the matched span highlighted. Click expands.
4. **Make every source clickable through to the original.** No source is too obvious to link.
5. **Group by quality dimension when there are many sources.** Freshness / consistency / completeness / goal-alignment groupings (see `context-quality-display.md`).

## Examples
1. **Context Layer Demo's right-rail sources panel.** Each source carries: rank, title, freshness chip, snippet with match highlight, and a "use this in synthesis" / "exclude this" toggle. The toggle feeds into the correction interface (see `correction-interface.md`).
2. **Perplexity's inline + side-panel citations.** Inline numbered citations link to the side panel; the panel shows the title, snippet, and link. A baseline implementation.
3. **Suzy Decision Engine's "panel respondents" surface.** For research-backed insights, the sources panel shows which respondent segments contributed, their consistency, and their sample size. Same shape, different content.

## Related entries
- `corpus/ai-product-ux/patterns/context-display.md` — parent pattern
- `corpus/ai-product-ux/context/correction-interface.md` — what users do with the panel
- `corpus/ai-product-ux/context/context-quality-display.md` — the scores that group sources
- `corpus/ai-product-ux/context/audit-log.md` — the history view of which sources fired when
- `corpus/voice/hook-data-is-not-context.md` — the thesis sources-panel demonstrates

## Anti-patterns
- **Sources buried two clicks deep.** A "view sources" link that opens a modal that opens a list. The friction is the message: don't actually look.
- **Sources without click-through.** Showing source titles but not letting the user open the underlying document. The panel becomes decorative.
