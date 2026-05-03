---
name: Quarterly Priorities Template — Strategic Frames → Tactical Quarter
domain: growth
source_skill: growth-marketing
entry_type: template
length_target: 400-700
related: [corpus/growth/playbook/quarterly-channel-review.md, corpus/growth/strategy/channel-evaluation-framework.md, corpus/growth/strategy/channel-maturity-model.md, corpus/growth/playbook/budget-allocation.md, corpus/growth/metrics/quarterly-review-checklist.md]
---

# Quarterly Priorities Template — Strategic Frames → Tactical Quarter

## What it is
The structured format for translating Riché's evergreen growth corpus (strategy, channels, segments, dynamics) into 1-3 *named* priorities for a specific quarter. The corpus is the role-based what-and-why; this template is the quarter-specific what-now. Output goes to a Notion page or dated entry — NOT to corpus, since priorities change per quarter while the corpus stays evergreen.

## Why it matters
Without quarterly priorities, the role-based corpus describes everything well but commits to nothing specific. The skill knows the whole strategy space; it doesn't know what to bias toward this quarter. Without the bias, every recommendation is balanced ("you could do X, or Y, or Z") rather than directive ("this quarter, prioritize Y because Z").

Quarterly priorities also create the rallying point for the 60-min `corpus/growth/playbook/quarterly-channel-review.md` — at end-of-quarter, Riché asks "did we move the priorities?" not "how is everything?" The first question produces decisions; the second produces rumination.

The template forces 1-3 priorities (not 5+, not 0) because:
- 0 priorities = no quarterly direction; corpus alone is too neutral
- 1-3 = focus; one priority can hold for multiple quarters if the work is multi-quarter
- 4+ = priority dilution; everything-is-priority means nothing is

## The template structure

For each priority, name:

```
### Priority [N]: [Imperative phrase, e.g., "Reach 1,500 LinkedIn followers"]

**Why this quarter:** [What changed or what gate is approaching that makes this quarter the right time]

**Concrete target:** [Single measurable outcome with a number; not "more X" but "X = 1,500" or "ship N artifacts"]

**Strategic frame this serves:** [Which corpus entry's strategy this advances — link directly]

**Channels involved:** [Which active channels do the work; which deferred channels this enables]

**Time delta:** [How much of the 5.25 hr/wk budget shifts to this priority; what gives time to it]

**Reversal condition:** [What signal would tell us to drop or de-prioritize this mid-quarter]

**Quarterly review check:** [The single question to answer at end-of-quarter to call this done/extended/dropped]
```

## How to apply

**At the start of each quarter (during the quarterly review per `corpus/growth/playbook/quarterly-channel-review.md`):**

1. Review the prior quarter's priorities. Mark each: completed / extended / dropped / partially-met.
2. Identify what changed in the strategic context: gate progress on deferred channels, stage transitions on active channels, ROI shifts.
3. Pick 1-3 priorities for the next quarter using the template above.
4. Write them in Notion (or wherever Riché tracks priorities) — NOT in this corpus. Corpus describes the strategy space; the priorities describe the bet.
5. Link each priority back to the relevant corpus entry so the skill can reason about it.

**During the quarter:**

- Every recommendation the skill makes should be checked against priorities. "Should I add Reddit engagement this month?" → "Does it serve a current priority? If not, defer."
- Mid-quarter changes to priorities are permitted but should be deliberate (logged with reason) — not drift.
- The reversal condition is the early-warning. If hit, drop the priority cleanly rather than half-pursuing it.

**At end-of-quarter:**

- Answer each priority's quarterly review check. Done? Extended into next quarter? Dropped?
- Pattern recognition over 3-4 quarters informs longer-arc decisions.

## Example quarterly priorities (illustrative, not authoritative)

These are examples of what well-formed priorities look like. Riché's actual current-quarter priorities live in Notion and may differ.

---

### Priority 1: Reach the newsletter launch gates by end of Q3 2026

**Why this quarter:** LinkedIn followers projected to cross 1,500 in late August. Inbound podcast invites trending up (3 in July). The newsletter is the highest-leverage owned-channel addition (per `corpus/growth/strategy/owned-vs-rented-channels.md`).

**Concrete target:** All 4 newsletter gates closed by Sept 30: LinkedIn ≥1,500 (track weekly), 3 inbound invites/mo for 2 consecutive months (track in HubSpot), 12 articles published (currently 9 — need 3 more), monthly cadence committed.

**Strategic frame this serves:** `corpus/growth/strategy/owned-vs-rented-channels.md` (move toward 30% owned floor) + `corpus/growth/channels/newsletter-evaluation.md` (gates closure).

**Channels involved:** LinkedIn (drive follower growth), richezamor.com (3 articles), speaking (drive inbound invites). Newsletter goes from gated to launchable.

**Time delta:** +30 min/wk to richezamor.com article cadence; -30 min/wk from X cadence (pull back to 3x/wk during this quarter).

**Reversal condition:** Inbound invites drop to <2/mo for 2 consecutive months → defer launch to Q1 2027.

**Quarterly review check:** Did all 4 gates close? If yes, schedule Q4 launch. If 3-of-4, document remaining gate and re-target Q4 review.

---

### Priority 2: Establish GitHub-as-distribution as a working Experiment-stage channel

**Why this quarter:** GitHub scored 13 on `corpus/growth/strategy/channel-evaluation-framework.md` (high audience-overlap, strong repurposing fit, structurally underused by AI/PM peers). Low time cost (~30 min/wk fits without major cuts). The Helm Labs work produces natural artifacts to seed the channel.

**Concrete target:** 4 published repos by end of quarter, each accompanying an existing /thinking article. Each repo with: working README, <60-second quickstart, ≥5 stars.

**Strategic frame this serves:** `corpus/growth/strategy/channel-evaluation-framework.md` (high-scoring add) + `corpus/growth/channels/github-as-distribution.md` (channel definition).

**Channels involved:** GitHub (new), richezamor.com /thinking (source articles), LinkedIn (announcement posts).

**Time delta:** +30 min/wk for GitHub work; absorbed by tightening the Sunday batch session and integrating repo work into the article-writing flow.

**Reversal condition:** After 4 repos, if total stars across the 4 repos <20 → reconsider channel-evaluation score; possibly drop to Hobby-tier.

**Quarterly review check:** 4 repos shipped? Channel ready to graduate from Experiment to Invest stage?

---

### Priority 3 (optional): [If a third priority is needed; cap at 3 total.]

## What does NOT belong in quarterly priorities

- Recurring operational work (cadence, commenting, engagement) — this is baseline, not a priority. If cadence is not held, the diagnostic (`corpus/growth/diagnostics/engagement-drop-diagnostic.md`) covers it.
- Long-term aspirations without a concrete this-quarter step ("eventually launch a podcast" — defer until gates approach).
- Vague directional statements ("grow LinkedIn" — not measurable; pick a specific target).
- More than 3 priorities — forces dilution; pick the top 3.

## Examples of priority types observed across quarters

- **Channel-launch priorities:** drive a deferred channel toward gate-closure
- **Channel-deepening priorities:** move an Experiment-stage channel to Invest, or Invest to Optimize
- **Cadence-recovery priorities:** rebuild a channel after disruption (e.g., post-algo-change)
- **Content-anchor priorities:** ship a specific number of /thinking articles or major talks
- **Audience-target priorities:** hit a specific Segment 2 follower or peer-reshare threshold
- **Owned-channel priorities:** drive newsletter launch, list growth, website cadence
- **Network priorities:** reach a specific number of Tier-1 podcast appearances or named speaking events

A given quarter typically has one channel/cadence priority + one audience/content priority. Three priorities is the max and usually suggests one is really an operational item that belongs elsewhere.

## Related entries
- `corpus/growth/playbook/quarterly-channel-review.md` — the 60-min process where this template gets applied
- `corpus/growth/strategy/channel-evaluation-framework.md` — scoring informs priority selection
- `corpus/growth/strategy/channel-maturity-model.md` — stage transitions inform priority types
- `corpus/growth/playbook/budget-allocation.md` — the 5.25 hr ceiling that priorities must respect
- `corpus/growth/metrics/quarterly-review-checklist.md` — broader quarterly checklist this nests under

## Anti-patterns
- Picking 5+ priorities. Dilutes focus; nothing moves.
- Picking 0 priorities. Defaults to "balance everything," produces no quarterly bias.
- Setting non-measurable priorities ("grow audience"). The whole point is the measurable target.
- Storing the actual current-quarter priorities IN this corpus. Corpus is evergreen; priorities are dated. Priorities live in Notion or a dated planning artifact.
- Not reviewing prior-quarter priorities at the new quarterly review. The done/extended/dropped call is what makes the cycle work.
