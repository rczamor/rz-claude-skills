---
name: Reasoning Sidebar Pattern
domain: ai-product-ux
source_skill: product-design
entry_type: template
length_target: 600
related: [corpus/ai-product-ux/patterns/reasoning-transparency.md, corpus/ai-product-ux/reasoning/show-the-work-rule.md, corpus/ai-product-ux/reasoning/reasoning-vs-output.md, corpus/ai-product-ux/reasoning/skip-reasoning-rule.md, corpus/ai-product-ux/context/audit-log.md]
---

# Reasoning Sidebar Pattern

## What it is
A template UI for displaying AI reasoning: a collapsible, scrollable, time-stamped sidebar that sits alongside the AI output. Each entry is a step in the chain — what the model retrieved, what it filtered, what trade-off it made, what prompt it sent. Time-stamped so the user can match reasoning to outputs even after multiple iterations. The canonical implementation of reasoning transparency.

## Why it matters
Reasoning needs a home. Inline reasoning (interleaved with the output) interrupts reading; modal reasoning (in a popover) hides on every click; bottom-sheet reasoning competes with the output for vertical space. A side panel — collapsible by default but persistent when open — preserves the reading flow while offering on-demand depth. Time-stamping converts the reasoning from a snapshot into an audit trail.

## How to apply
1. **Right-rail placement, collapsible.** Default-open on first use, default-collapsed for repeat users (with one-click re-open).
2. **Time-stamp every step.** Match step timestamps to the streaming output so the user can correlate.
3. **Step types, not free text.** "Retrieved 7 sources." "Filtered to 4 by goal-alignment." "Selected top 2 by consistency." Structured beats prose for scanning.
4. **Each step is a click target.** Click "filtered to 4" → see which 3 were filtered out and why.
5. **Persist state per session.** If the user opened the panel for the previous answer, keep it open for the next.

## Examples
1. **Context Layer Demo reasoning sidebar.** The right-rail panel shows each of the five context steps as a time-stamped entry: retrieve (sources retrieved), filter (which dropped, why), score (quality dimensions), align (goal-alignment), synthesize (prompt and output). Click any step to expand. This is the canonical example of the pattern.
2. **Cursor's "thinking..." panel.** A lighter implementation — a side panel that streams the agent's reasoning token-by-token. Lacks the structured-step abstraction but earns trust by simply showing the work.
3. **Anthropic Claude's extended thinking display.** The "thinking" tokens are exposed in the UI as a collapsible block. Same shape, less interactive.

## Related entries
- `corpus/ai-product-ux/patterns/reasoning-transparency.md` — parent pattern
- `corpus/ai-product-ux/reasoning/show-the-work-rule.md` — the rule the sidebar enacts
- `corpus/ai-product-ux/reasoning/reasoning-vs-output.md` — the conceptual basis
- `corpus/ai-product-ux/reasoning/skip-reasoning-rule.md` — when not to auto-collapse
- `corpus/ai-product-ux/context/audit-log.md` — the historical companion

## Anti-patterns
- **Modal reasoning popover.** Click to open, click again to close, can't scroll while reading the output. The friction kills engagement.
- **Reasoning as flat free text.** A wall of prose with no structure. Users skim and miss the load-bearing step.
