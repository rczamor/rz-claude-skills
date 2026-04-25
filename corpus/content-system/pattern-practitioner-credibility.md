---
name: Practitioner Credibility
domain: content-system
source_skill: copywriting
entry_type: rule
length_target: 300-800
related: [corpus/voice/voice-identity.md, corpus/content-system/pattern-show-dont-tell.md, corpus/content-system/pattern-specificity-test.md, corpus/voice/proof-points.md, corpus/voice/three-domain-balance.md]
---

# Practitioner Credibility

## What it is
A standing rule that every post reinforces the practitioner-not-commentator positioning. Riché is someone who builds, ships, and measures — not someone who comments on what others build. Every post should contain at least one signal that says: this person has actually done this. The signals can be a named system, a specific metric, a real moment of failure or learning, a translation of cognitive science into product architecture, or a live-demo capability mention.

## Why it matters
The market is saturated with AI commentators. Lenny is a great commentator (and a builder before that); Shreyas is a great commentator. Riché's positioning is upstream of commentary — practitioner-first. The market's attention to practitioners is greater than its attention to commentators because the commentary tier is crowded and the practitioner tier is genuinely rare. Every post that reads as commentary erodes the positioning. Every post that reads as practitioner work compounds it.

## How to apply

1. **Audit each draft for one practitioner signal.** The signal can be:
   - A named system (Grandstage, Suzy, IBM, Helm Labs, Context Layer Engine).
   - A specific metric tied to work shipped (300% growth, 350+ customers, six-week launch).
   - A specific moment of building or failing (the first user who churned, the rebuild week, the meeting that triggered the architectural shift).
   - A live-demo signal ("I demo the Context Layer Engine live on stage").
   - A real architectural decision named with specificity ("We chose to consolidate before retrieving").

2. **Avoid commentary phrasing.** "Many teams should consider..." "It's worth thinking about..." "The industry needs..." All commentary, all weakening. Replace with practitioner phrasing: "We built X. It failed. Here's what shipped instead."

3. **Use the live demo as a differentiator selectively.** When pitching to Segment 4 (event organizers), the live demo is the move. In standard posts, mention it once a month — not every post — to preserve the freshness.

4. **Connect to building, not just thinking.** When citing cognitive science, tie the citation to what changed in a system. Klein's RPDM doesn't matter unless it changes the prioritization step that ships in code.

5. **Resist the urge to comment on others.** A Tuesday Signal extends or challenges the news from a builder's vantage. It does not commentate on what other commentators have said about the news. That's a commentary-on-commentary loop that has no practitioner content.

## Examples

**Practitioner signal:** "At Grandstage we cut retrieved docs from 50 to 4 and accuracy went up. The model never changed. The pipeline did." — Named system, specific metric, specific decision. Three signals in two sentences.

**Commentary (failed):** "Teams should consider consolidating their retrieved documents to improve accuracy." — Zero practitioner signals. Reads like a Medium post.

**Live-demo signal in a CFP packet:** "I demo the Context Layer Engine live on stage so the audience sees the architecture running, not just diagrammed." Used selectively — once per CFP, not three times.

**Cognitive science tied to building:** "Klein's recognition-primed decision making is the basis for the prioritization step in the pipeline. It's not a citation — it's the reason the prioritization layer ranks signals by 'would an expert use this to decide?' rather than by relevance score."

**Resist commentary loop.** A Tuesday Signal could react to an Anthropic release by extending what a famous commentator said about the release. Don't. React to the release directly, with a builder's lens. The commentator doesn't add a layer of value; they add a layer of distance.

## Related entries
- `corpus/voice/voice-identity.md` — the practitioner-first identity at the voice level
- `corpus/content-system/pattern-show-dont-tell.md` — the named-system version of the rule
- `corpus/content-system/pattern-specificity-test.md` — specificity is the operational test
- `corpus/voice/proof-points.md` — the canonical practitioner credentials
- `corpus/voice/three-domain-balance.md` — the practitioner identity is reinforced through Context Layers (50%) and Product Management (30%)

## Anti-patterns
- Pure commentary post. A post that has no named system, no metric, no specific decision, no real moment. Reads as commentary regardless of substance. Don't ship.
- Over-using the live demo line. Mentioning it in every post turns the differentiator into a verbal tic. Use selectively.
- Commenting on commentators. Reacting to Lenny's reaction to Anthropic's release is two layers removed from the work. React to the work itself.
