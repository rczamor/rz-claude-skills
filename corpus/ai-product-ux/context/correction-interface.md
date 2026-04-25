---
name: Correction Interface
domain: ai-product-ux
source_skill: product-design
entry_type: template
length_target: 600
related: [corpus/ai-product-ux/patterns/context-display.md, corpus/ai-product-ux/context/sources-panel.md, corpus/ai-product-ux/context/context-quality-display.md, corpus/ai-product-ux/context/audit-log.md, corpus/voice/hook-data-is-not-context.md]
---

# Correction Interface

## What it is
A template UI that lets users edit, remove, or re-rank the context that informs an AI's decisions. Toggle sources on/off, edit weights, exclude documents, mark sources as canonical. The corrections feed back into future generations. This is the half of context display that turns a debug surface into a learning loop.

## Why it matters
Showing context is necessary but insufficient. A user who can see the wrong source but can't remove it is just being shown a defect. A user who can correct the context turns each interaction into training data — the AI gets smarter on each use, and the user feels ownership over the system. The correction interface is what converts a passive viewer into an active operator. It is the difference between a tool and a system.

## How to apply
1. **One-click toggle on each source.** "Use" / "exclude" — instant. The user can see the synthesis update in response.
2. **Re-rank by drag, or by override score.** For sources that are correct but should weigh more or less.
3. **Mark as canonical.** Some sources should always fire for this user — let them flag those once and have it persist.
4. **Persist corrections per user, per workspace, per global level.** A correction at the user level is a preference; at the workspace level, a policy; at the global level, a fact about the corpus.
5. **Show the impact.** When the user toggles a source off, surface what changed in the output. The feedback loop is the reward.

## Examples
1. **Context Layer Demo's per-source toggle and re-rank.** The right-rail panel allows users to flip sources on/off and drag them up or down. The synthesis re-runs in place. This is the demo's most compelling moment for buyers — they realize they own the context.
2. **Suzy Decision Engine's "trust this segment" controls.** Buyers can mark certain respondent segments as canonical for their brand and exclude others. The corrections persist across all future automated insights for that workspace.
3. **Notion AI's "edit instructions" pattern.** Lighter-weight, but same shape — the user edits the instructions feeding the AI rather than just the output. A correction at the prompt-context layer.

## Related entries
- `corpus/ai-product-ux/patterns/context-display.md` — parent pattern
- `corpus/ai-product-ux/context/sources-panel.md` — what the corrections operate on
- `corpus/ai-product-ux/context/context-quality-display.md` — the scores users adjust
- `corpus/ai-product-ux/context/audit-log.md` — the trail of past corrections
- `corpus/voice/hook-data-is-not-context.md` — the thesis demonstrated by the loop

## Anti-patterns
- **View-only context display.** Showing sources but not letting users intervene. Half the value is missing.
- **Corrections that don't persist.** The user excludes a source, the AI uses it again next time. The correction was theater.
