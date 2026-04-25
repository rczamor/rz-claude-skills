---
name: Talk Abstract Format
domain: content-system
source_skill: copywriting
entry_type: template
length_target: 300-800
related: [corpus/content-system/format-cfp-submission.md, corpus/content-system/format-speaker-bio.md, corpus/content-system/wednesday-deep-dives.md, corpus/voice/the-hook.md]
---

# Talk Abstract Format

## What it is
A 200-300 word standalone abstract that pitches a talk to event programs, conference websites, or attendee-facing program pages. Structure: problem → thesis → takeaway. Written so a senior PM scanning the program decides this talk is worth a 50-minute conference slot. Differs from a CFP submission (which has additional packet items) and from a podcast pitch (which is conversational rather than program-facing).

## Why it matters
Program-facing abstracts are how attendees decide which sessions to attend at multi-track events. A great talk with a weak abstract gets a half-empty room; a clear abstract with a great hook fills the room and earns a stage moment. The abstract also influences the event organizer's own positioning — strong abstracts get featured in event marketing, which earns Riché outsized attention before he even speaks.

## How to apply

1. **Open with the problem (~60-80 words).** Specific failure mode. Not "AI is hard" — something like "Most teams build AI products by piping data into a large language model and calling it RAG. The agents that result get smarter with every model release and stay equally bad at deciding what matters."

2. **Name the thesis (~60-80 words).** What the talk argues. Use the canonical hook ("Data is not context") or one of the supporting one-liners. Tie the thesis to the five-step process explicitly.

3. **State the takeaway (~60-80 words).** What attendees will leave with. A concrete tool, framework, or test they can apply in their next sprint. "By the end, you'll have a concrete five-step audit you can run on any AI product within a week."

4. **Demo or proof signal (~30-50 words).** Mention the live demo or the named systems that ground the talk. This is the practitioner-credibility move that separates the abstract from a manifesto.

5. **Length:** 200-300 words. Single paragraph or 3-4 short paragraphs depending on the program style.

## Examples

**Sample abstract (260 words):**
"Most teams build AI products by piping data into a large language model and calling it RAG. The agents that result get smarter with every model release and stay equally bad at deciding what matters. The bottleneck isn't the model. It's everything upstream of it.

Data is not context. Context is what's left after you've decided what matters and consolidated the rest away. In this talk, I'll walk through the five-step process I've used to ship context architecture behind 300% user growth at Grandstage, a Decision Engine launch at Suzy that moved 350+ enterprise customers in six weeks, and personalization systems at IBM generating millions across product lines: curate, synthesize, consolidate, prioritize, store intelligently.

I'll show why expert decision-makers use less information, not more — Klein's recognition-primed decision making, Miller's working-memory limits — and how those findings translate directly to AI product architecture. We'll look at where the five-step process succeeds and where it doesn't, and what changes when the agent acts on context rather than just retrieves it.

By the end, you'll have a concrete five-step audit you can run on any AI product within a week, and a working test for whether the next model upgrade will actually fix the problem you think it will. I'll demo the Context Layer Engine — my personal knowledge system built on Letta — live on stage so you can see the architecture running, not just diagrammed."

**Why this works.** Problem in para 1, thesis with hook + named systems in para 2, science grounding in para 3, concrete takeaway in para 4 with demo signal. 260 words. Hits the practitioner positioning without being self-congratulatory.

## Related entries
- `corpus/content-system/format-cfp-submission.md` — the abstract is a component of the full CFP
- `corpus/content-system/format-speaker-bio.md` — bio accompanies the abstract
- `corpus/content-system/wednesday-deep-dives.md` — talks expand from deep dives
- `corpus/voice/the-hook.md` — the abstract uses the hook just like any other piece

## Anti-patterns
- Abstract as marketing copy. "Join us as Riché takes you on a journey through the world of context architecture." Faux-profound, vague, fileable.
- Missing the takeaway. If a reader can't tell what they'd leave with, the talk feels indulgent.
- No demo or named system. The abstract reads like commentary, not practitioner work.
