---
name: Wednesday Deep Dives
domain: content-system
source_skill: copywriting
entry_type: pattern
length_target: 300-800
related: [corpus/voice/the-hook.md, corpus/voice/fatal-fifteen.md, corpus/content-system/arc-step-1-start-with-failure.md, corpus/content-system/hook-deep-dive-hook-use.md, corpus/content-system/pattern-show-dont-tell.md]
---

# Wednesday Deep Dives

## What it is
A 700-1,000 word LinkedIn article (or long-form post) that walks through one architectural decision, one product story, or one framework with conference-talk caliber detail. Specific numbers, named tools, real architectural decisions. The slot of the week where Riché demonstrates depth — the proof that he's a practitioner, not a commentator. The goal is for a senior PM to read it and think: this person has actually built this.

## Why it matters
Hot takes earn attention; deep dives earn credibility. Every Wednesday deep dive becomes a long-tail referral asset. Six months later, when someone DMs Riché asking "do you have something I can send my CTO on context architecture?" the deep dive is the link. It's also the natural source material for talk abstracts, podcast pitches, and the eventual newsletter.

## How to apply

A deep dive on context architecture follows the six-step story arc:

1. Open with a failure (what went wrong when the team treated data as context)
2. Name the assumption (most teams assume data = context)
3. Introduce the alternative (the five-step process: curate, synthesize, consolidate, prioritize, store intelligently)
4. Ground in cognitive science (one insight, selectively — Miller's 7±2, expert vs. novice information use)
5. Connect to product outcome (specific metric, UX, defensibility, unit economics)
6. Show, don't tell (reference a real system: Grandstage, Context Layer Engine, Claude Code Auto Dream, Letta)

Section structure for the article body:

- **Section 1 (~150 words):** The failure scene. Concrete, present-tense, specific.
- **Section 2 (~150 words):** The assumption being made and why teams default to it.
- **Section 3 (~300 words):** The five-step alternative, walked through with one named example per step.
- **Section 4 (~100 words):** The cognitive science grounding (one insight, no more).
- **Section 5 (~150 words):** What changed for the business — metric, UX shift, or defensibility argument.
- **Section 6 (~100 words):** A close that extends, not summarizes. Often the next problem this opens up.

## Examples

**Topic: How Grandstage's first context system shipped wrong.** Opens with the launch week: 50 retrieved docs, slow responses, hallucinations. Section 2: the team assumed bigger retrieval = better answers. Section 3: the rebuild — synthesis layer, consolidation pass, prioritization based on decision-readiness, storage by query intent. Section 4: Miller's 7±2 grounds why 4-document context outperforms 50. Section 5: 300% user growth and $0 CAC followed the rebuild. Section 6: opens the next question — what does the same architecture look like for agents that act, not answer?

**Topic: The five-step pipeline at Suzy.** A walk through the Decision Engine launch in six weeks: how Intelligence/Insights/Impact pillars mapped to the five steps; what 350+ enterprise customers exposed about consolidation under load.

**Topic: Why the Context Layer Engine is built on Letta.** A deeper architectural piece on agent memory, with named tools and a reproducible diagram. Closes by linking to the live demo.

## Related entries
- `corpus/content-system/arc-step-1-start-with-failure.md` through `arc-step-6-show-dont-tell.md` — the six-step story arc
- `corpus/content-system/hook-deep-dive-hook-use.md` — deep dives use the full anchor + supporting one-liner
- `corpus/content-system/pattern-show-dont-tell.md` — every deep dive references a real system
- `corpus/pm-frameworks/` — when the deep dive touches PM substance, source frameworks live here

## Anti-patterns
- Conference-talk caliber doesn't mean "comprehensive." It means specific. A 900-word piece that names two real systems beats a 1,500-word survey of context architecture in general.
- Burying the hook past the third paragraph. The opening failure has to land in the first 100 words or readers bounce.
