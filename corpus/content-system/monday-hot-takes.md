---
name: Monday Hot Takes
domain: content-system
source_skill: copywriting
entry_type: pattern
length_target: 300-800
related: [corpus/voice/fatal-fifteen.md, corpus/voice/the-hook.md, corpus/content-system/hook-hot-take-single-line.md, corpus/content-system/pattern-specificity-test.md]
---

# Monday Hot Takes

## What it is
A 150-250 word LinkedIn post that opens the week with a confident, direct, slightly provocative claim. One clear position with 1-2 supporting points. Like a sharp observation at a dinner party — short sentences, no warm-up, no qualifiers. The take must be substantive (backed by what Riché has built or seen) but compressed enough to land in 30 seconds of feed-scroll.

## Why it matters
Mondays are when feeds are most active and Segment 2 product leaders are scanning between meetings. A long deep dive gets scrolled. A hot take with a clear position interrupts the scroll and earns a comment. It also forces voice discipline: 200 words leaves no room for filler, hedging, or the Fatal Fifteen.

## How to apply
1. Pick a single claim. If it takes more than one sentence to state, it's not a hot take.
2. Open with the claim itself — no "I've been thinking about" preamble.
3. Add 1-2 supporting points. Each point gets one short paragraph.
4. Close with a question or a sharper restatement of the claim. Never a "Key Takeaway" block.
5. Voice check: would Riché actually say this at a dinner with three other VPs?

## Examples

**Topic: The context problem.** A 180-word post that opens "Your AI doesn't have a model problem. It has a context problem." Two short paragraphs name two failure modes Riché has watched at IBM and Suzy: dumping CRM data into a vector store and calling it RAG. Closes: "Models get smarter every month. Context quality stays the same. Which one are you actually working on?"

**Topic: Retrieval theater.** Opens "Retrieval without consolidation is just efficient delivery of noise." One paragraph: an example from Grandstage where the v1 system retrieved the right 50 documents and still gave wrong answers because nothing synthesized them. One paragraph: the fix was a five-step pipeline that cut retrieved docs from 50 to 4. Closes with the count: "From 50 to 4. Better answer."

**Topic: PM org charts.** Opens "If your PM org has more strategy decks than shipped features, your problem isn't strategy. It's your operating cadence." Two paragraphs draw on Suzy's six-week Decision Engine launch as the counterexample.

## Related entries
- `corpus/voice/the-hook.md` — Monday hot takes lean heaviest on the hook one-liners
- `corpus/voice/fatal-fifteen.md` — voice rules apply universally
- `corpus/content-system/hook-hot-take-single-line.md` — hot takes use one one-liner only, no anchor
- `corpus/content-system/pattern-specificity-test.md` — every hot take needs at least one specific moment, decision, metric, or named tool

## Anti-patterns
- Hot take that's actually a deep dive: claim → three sub-points → context → caveat → call to action. If you find yourself adding "moreover," it's a Wednesday post in disguise.
- Provocation without substance. "AI is overrated" is provocation. "Your AI doesn't have a model problem; it has a context problem" is a take backed by something Riché has built.
