---
name: Preferred terminology
domain: voice
source_skill: copywriting
entry_type: rule
length_target: 300-800
related: [corpus/voice/terminology-never-use.md, corpus/voice/terminology.yaml, corpus/voice/hook-data-is-not-context.md, corpus/voice/attribute-authoritative-accessible.md]
---

# Preferred Terminology

## What it is
The list of terms Riché uses when writing about context architecture, AI products, and the work that makes them function. These terms are precise — each one names a specific operation or concept rather than gesturing at a vague theme — and they are stable across the body of work, so the audience accumulates familiarity and the vocabulary compounds.

The canonical preferred list:

- **context synthesis / context orchestration** — the act of combining inputs across sources into a coherent representation
- **consolidation** — the step that reduces synthesized inputs to decision-ready context
- **decision-ready context** — context formatted for the user's next decision, not for general reading
- **context quality** — the measure that matters more than retrieval recall
- **five-step context generation** — curate, synthesize, consolidate, prioritize, store intelligently
- **"Data is not context"** — the canonical Hook

## Why it matters
A consistent vocabulary is what lets a writer build a body of work that cross-references itself. When "consolidation" means the same thing in piece #1 and piece #50, the audience gets fluent in the framework. When the term shifts between "consolidation," "compression," "synthesis," and "intelligence" across the body, the audience never gets purchase. The preferred list is also a defense against the manufactured-jargon failure mode (see `anti-pattern-jargon-retrieval-aware.md`) — every term on the list names a real operation, so reaching for the preferred term forces the writer to commit to a specific claim.

## How to apply
- When drafting Context/AI content, use the preferred terms before reaching for synonyms.
- "Synthesis" and "orchestration" are interchangeable for the upstream combination step. Pick one within a single piece; don't alternate.
- "Consolidation" is the load-bearing term — it's the step most teams skip and the term that signals Riché's framework. Use it consistently.
- "Decision-ready context" is the user-facing outcome. Use when writing about UX, product decisions, or what the model surfaces to the user.
- "Context quality" is the metric framing. Use when contrasting with retrieval recall or model size.
- "Data is not context" is the Hook. Use as the anchor provocation; rotate the supporting one-liners around it.

## Examples
GOOD: "The consolidation layer is the one most teams skip. Curate works. Synthesis works. Then they retrieve more, hoping more becomes meaning. The fix is decision-ready context — the slice the user actually needs to act."

GOOD: "Models commoditize. Context quality doesn't. That's the moat."

GOOD: "Suzy's Decision Engine ships less to the user because the context orchestration layer does the work upstream. The user sees three insights per decision, not thirty."

GOOD: "The five-step context generation process: curate, synthesize, consolidate, prioritize, store intelligently. Each step compounds. Skip one and the whole chain leaks."

BAD (drifting vocabulary): "The compression layer is what teams skip. Curate works. Composition works. Then the system tries to optimize retrieval-aware intelligence."

GOOD (corrected): "The consolidation layer is what teams skip. Curate works. Synthesis works. Then the system tries to optimize retrieval, which doesn't help — the missing step is consolidation, not better retrieval."

## Related entries
- `corpus/voice/terminology-never-use.md` — the never-use companion list
- `corpus/voice/terminology.yaml` — programmatic lookup of both lists
- `corpus/voice/hook-data-is-not-context.md` — the canonical Hook
- `corpus/voice/attribute-authoritative-accessible.md` — preferred terms support accessibility

## Anti-patterns
- Reaching for synonyms because "the term has been used too much in the piece." Repetition of preferred terms is fine; it builds vocabulary fluency in the audience.
- Inventing a new term because the existing preferred term doesn't quite fit. If the existing term doesn't fit, the claim probably needs to be sharpened, not the vocabulary expanded.
