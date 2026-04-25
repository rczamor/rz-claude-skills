---
name: Arc Step 1 — Start with Failure
domain: content-system
source_skill: copywriting
entry_type: template
length_target: 300-800
related: [corpus/content-system/wednesday-deep-dives.md, corpus/content-system/arc-step-2-name-the-assumption.md, corpus/voice/the-hook.md]
---

# Arc Step 1 — Start with Failure

## What it is
The opening move of any context generation deep dive: a concrete, specific failure that occurred when an AI system was given data and asked to behave as if it had context. Not a hypothetical. A real moment with a name, a number, a system, a stakeholder. The failure is the cold open — it earns the next 700 words.

## Why it matters
Most AI thought leadership opens with a thesis statement ("Context is the new moat") and loses the reader by paragraph two because nothing is at stake yet. Failure narratives create stakes. They also frame the rest of the piece: every subsequent claim is judged against whether it would have prevented the opening failure. This is what makes the practitioner voice land — the reader feels the cost before they hear the prescription.

## How to apply
1. Pick a real failure. Grandstage's first retrieval system, Suzy's pre-Decision-Engine pipeline, an Anthropic eval that surfaced bad behavior, a Helm Labs prototype that lied to itself.
2. Open with the moment, not the conclusion. "Tuesday afternoon. The retrieval system pulled 50 documents. The answer cited three. None of them were right."
3. Name what the team thought was happening vs. what was actually happening. The gap is the failure.
4. Resist the urge to explain why yet. Save the diagnosis for steps 2-3.
5. Length: 75-150 words. The opening should land in the first scroll.

## Examples

**Grandstage failure scene:** "Three weeks after launch, our top user told me the system was lying to her. She'd asked about a competitor's pricing change. The retrieval pipeline returned the right blog post, the right earnings call, the right LinkedIn post. The summary cited none of them and gave her a number we'd seen nowhere in the corpus. The model wasn't broken. The context was."

**Suzy failure scene:** "The Decision Engine demo had a 4% accuracy ceiling we couldn't break through. We added more documents, longer context windows, better embeddings. Nothing moved. The team kept tuning the model. The problem was upstream — we were giving it everything and asking it to know what mattered."

**IBM failure scene (composite for a post):** "An enterprise customer asked our personalization system why it had recommended a discontinued product. The system pulled fifteen relevant signals: recent purchases, support tickets, usage patterns. None of them said 'discontinued.' We'd indexed everything except the catalog status. The model did exactly what it was told. The context was incomplete by design."

## Related entries
- `corpus/content-system/wednesday-deep-dives.md` — step 1 opens every deep dive
- `corpus/content-system/arc-step-2-name-the-assumption.md` — the next move after the failure
- `corpus/voice/the-hook.md` — failure scenes set up the hook line ("data is not context")
- `corpus/content-system/pattern-show-dont-tell.md` — failure must be specific, named, real

## Anti-patterns
- Generic failure ("AI systems often hallucinate"). Failures need a name and a number.
- Failure as fable. A made-up story about "a CTO at a fictional company" reads like a textbook case. Use real systems Riché has touched.
- Burying the failure. If the first sentence is "Context architecture matters because..." the failure has been demoted to a supporting argument. Move it to the lead.
