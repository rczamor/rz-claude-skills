---
name: Arc Step 2 — Name the Assumption
domain: content-system
source_skill: copywriting
entry_type: template
length_target: 300-800
related: [corpus/content-system/arc-step-1-start-with-failure.md, corpus/content-system/arc-step-3-introduce-alternative.md, corpus/voice/the-hook.md]
---

# Arc Step 2 — Name the Assumption

## What it is
Step 2 of the context generation story arc: name the silent assumption that produced the failure. Almost always some flavor of "data equals context," "retrieval equals understanding," or "more information equals better answers." This step makes the reader's own assumption visible. Once named, it can be challenged.

## Why it matters
The reader will keep believing the same thing the failed team believed unless that belief is named explicitly. This is the move that converts a war story into a lesson. It also gives the reader a place to recognize themselves — "wait, that's what we do" — which is the conversion point from passive read to active engagement.

## How to apply
1. State the assumption directly, in one sentence. "Most teams assume data is context."
2. Locate it. Where does the assumption come from? Often: vector database marketing, RAG tutorials that skip the synthesis step, dashboards that conflate completeness with usefulness.
3. Show how the assumption is rational — it's the simplest explanation, it works in toy demos, it scales linearly until it doesn't. Empathy, not condescension.
4. Pivot. Signal that the rest of the piece will provide the alternative.
5. Length: 75-125 words. This step is the bridge, not the destination.

## Examples

**Following Grandstage failure:** "Most teams assume data is context. It's a reasonable assumption. The retrieval system worked: the right documents came back. The vector database told us we had the highest-quality embeddings in the corpus. Every metric said yes. Every metric was measuring the wrong thing. Data is the raw material. Context is what's left after you've decided what matters and consolidated everything else away."

**Following Suzy failure:** "We assumed more documents in the prompt would mean better answers. Every team I've worked with has made the same assumption — it's what the tooling rewards. Token windows get bigger; context windows get bigger; we fill them. The assumption rewards measurable inputs (documents, tokens, embeddings). It punishes the un-measurable thing that actually matters: which four pieces of information would let an expert decide?"

**Generic version for a Tuesday Signal:** "Anthropic's longer context windows reward teams who already curate well. Everyone else makes the same assumption: more capacity equals more capability. It's a familiar mistake. Disk space didn't make people better writers. Token budgets won't make systems smarter."

## Related entries
- `corpus/content-system/arc-step-1-start-with-failure.md` — the assumption is named in light of the failure
- `corpus/content-system/arc-step-3-introduce-alternative.md` — the alternative is named in light of the assumption
- `corpus/voice/the-hook.md` — "data is not context" is the canonical version of this naming move

## Anti-patterns
- Naming the assumption with contempt. "These teams should know better" closes the reader off. Empathy keeps them reading.
- Naming a different assumption than the one the failure exposed. The failure and the assumption have to line up tightly.
- Skipping the step. Going from failure straight to solution skips the move that makes the reader recognize themselves in the story.
