---
name: Repurpose vs Create — The Decision Tree
domain: growth
source_skill: growth-marketing
entry_type: pattern
length_target: 400-600
related: [corpus/growth/strategy/repurposing-matrix.md, corpus/growth/metrics/content-decay-analysis.md, corpus/growth/playbook/batch-writing-sunday.md, corpus/growth/strategy/channel-evaluation-framework.md]
---

# Repurpose vs Create — The Decision Tree

## What it is
The decision protocol applied at the start of every content batch session: should the next piece extend an existing source artifact, or author a new source? Default bias: extend (lower cost, higher leverage per hour) unless specific conditions favor creating new.

## The decision tree

For any open content slot:

```
1. Is there an existing source artifact <90 days old that hasn't been fully repurposed?
   → YES: Extend it (default path)
   → NO: Continue
   
2. Is there an existing source artifact 90-365 days old AND still generating traffic/engagement?
   → YES: Refresh + extend it
   → NO: Continue
   
3. Is there a clear new-thinking opportunity (new research, new lesson, new framework not in any existing source)?
   → YES: Create new source
   → NO: Skip the slot rather than ship voice-flat filler

4. Is the calendar pressure forcing a publish-something-anything decision?
   → YES: Stop. Skipping is better than shipping mediocre content. (See `corpus/growth/creator-dynamics/frequency-vs-quality-tradeoff.md`)
```

## Why it matters
The default reflex for most creators is "I need to publish today; let me write something new." This reflex burns 60-90 minutes per piece on net-new drafting AND dilutes the impact of existing source artifacts that haven't been fully repurposed. The right reflex is "what's the best thing to ship today given what already exists?" — which usually points to a derivative or refresh.

The decision tree exists because the right answer changes based on the existing source library. In a quarter with 3 strong /thinking articles and 2 talks, almost everything should be derivatives. In a quarter with no recent source work, a new source is the next investment. The tree keeps this honest.

## How to apply

**Sunday batch session, 10 min upfront:**

Before drafting any of the week's posts, run the decision tree. Inventory:

1. Source artifacts published in the last 90 days that haven't produced their full derivative count (per `corpus/growth/strategy/repurposing-matrix.md`)
2. Source artifacts 90-365 days old that are still generating measurable traffic or engagement
3. Any net-new thinking from the past 2 weeks of work (Helm Labs experiments, recent reading, recent client work) that hasn't found expression yet

The inventory determines the week's content composition:

- **Heavy-source week** (e.g., a /thinking article shipped 2 weeks ago): bias to extension; 4 of 5 posts as derivatives
- **Light-source week** (last source >60 days old): bias to creation; 1 source piece + supporting derivatives
- **Refresh week** (a 9-month-old article showing renewed interest): bias to refresh; updated article + derivative posts

**Allocation rules (rough percentages over a quarter):**
- Extending recent sources: 50%
- Refreshing older sources: 10%
- Creating new sources: 25%
- Standalone frequency content (no source connection): 15%

The 15% standalone budget exists because not every post can or should be a derivative — some news takes, some peer-comment-driven posts, some industry observations stand on their own. But when standalone content exceeds 25% of a quarter's output, the brand stops compounding and starts treadmill-ing.

## Indicators that point to "create new"

The tree biases to extension, but explicit signals indicate the new-source path:

- A specific new lesson from recent work that doesn't fit any existing article's frame
- A peer publication or industry event that demands a fresh response
- A speaking talk or podcast appearance whose central idea hasn't been written down yet
- A measurable gap in topic coverage (the K4 dimension from `corpus/website-audit/dimensions/categories/keyword-research.md` flagging an empty cluster)
- A planning-cycle moment (quarterly review surfacing a needed strategic content piece)

When 2 or more of these are present, the new-source path is right even if the existing-source library has unrepurposed material.

## Indicators that point to "skip rather than ship"

- No clear thesis for the post (would require ~60 min to develop one)
- Voice-quality concerns (the draft would risk a fatal-fifteen lint failure)
- Time pressure suggesting AI-generated filler is on the table
- Heavy-week conditions (travel, family, illness) where the cadence flexibility is the right tool

Skipping a post in these conditions costs nothing meaningful (cadence rebounds the next week); shipping a voice-flat post damages the brand.

## Examples
1. **Heavy-source week.** Sunday review: 2 weeks ago Riché shipped a /thinking article on agent memory; 5 of 8 derivatives produced. Decision: this week's 3 posts are the remaining 3 derivatives. Total drafting time: ~75 min vs ~3 hours for 3 net-new posts.
2. **Refresh decision.** Sunday review: a 2024 article on "context drift in production AI" has rebounded in traffic since a recent OpenAI announcement made the topic relevant again. Decision: refresh the article with 2026 context, then publish 2 derivative posts. Total time: ~3 hrs (refresh + derivatives) vs ~6 hrs for two new sources.
3. **New-source decision.** Sunday review: last source piece was 75 days ago; Helm Labs ran a new eval experiment last week with surprising results. Decision: this week's batch produces a new /thinking article on the experiment + 2 supporting LinkedIn posts as initial derivatives. The next 4 weeks' batches continue to derive from this new source.
4. **Skip decision.** Friday morning: Wednesday's planned post never got drafted; Riché has 30 min before the workday and is mentally tapped. Decision: skip the post; cadence will recover next week. Avoids shipping a 70%-quality piece that would have damaged voice consistency.

## Related entries
- `corpus/growth/strategy/repurposing-matrix.md` — defines what derivatives are possible from each source
- `corpus/growth/metrics/content-decay-analysis.md` — decay informs the 90-day cutoff
- `corpus/growth/playbook/batch-writing-sunday.md` — where the decision tree gets applied
- `corpus/growth/strategy/channel-evaluation-framework.md` — repurpose-fit is a channel-scoring criterion

## Anti-patterns
- Always creating new because new "feels productive." Burns time; under-leverages existing assets.
- Always repurposing because it's easier. Eventually the source library goes stale; new thinking stops getting captured.
- Repurposing a source that's been fully derived already. Diminishing returns; better to skip or create new.
- Treating "skip" as a failure. Skip preserves voice integrity; it's the right choice in the conditions named above.
