---
name: Content Decay Analysis — Half-Lives by Channel
domain: growth
source_skill: growth-marketing
entry_type: framework
length_target: 400-700
related: [corpus/growth/strategy/repurposing-matrix.md, corpus/growth/metrics/repurpose-vs-create-decision.md, corpus/growth/metrics/channel-roi-calculation.md, corpus/growth/strategy/channel-evaluation-framework.md]
---

# Content Decay Analysis — Half-Lives by Channel

## What it is
The empirically-observed half-lives of content artifacts on each channel — how quickly each format loses relevance and reach after publication. Used to inform when content needs to be refreshed, when it can be repurposed for compounding return, and when investment in the format is worth its decay-adjusted cost.

| Channel / Format | Active half-life | Long-tail | Key implication |
|---|---|---|---|
| X tweet (single) | ~4 hours | ~24 hours | Built for attention; almost zero compounding |
| X thread | ~12 hours | ~3-7 days | Modest compounding via reshare; dies fast |
| LinkedIn post | ~24 hours | ~3-5 days | Main reach in first day; tail via comments |
| LinkedIn carousel | ~48-72 hours | ~7-14 days | Algorithm rewards saved-for-later signal |
| LinkedIn article (long-form) | ~7 days | ~30-60 days | Modest SEO; longer than posts |
| Newsletter issue | ~7 days (open + read) | ~14 days (forwards) | Email decay is fast; archive value low |
| /thinking article on richezamor.com | ~14 days (active) | ~12+ months | SEO compounding; multi-year tail |
| GitHub repo | ~7 days (active interest) | Multi-year (search + stars) | Discovery via topic search compounds |
| Show HN post | ~48 hours | Multi-year (HN archive + Google) | One-shot peak then long compounding tail |
| Podcast appearance | ~7 days (release peak) | ~6+ months | Tail driven by guest's audience cross-pollination |
| Conference talk | ~14 days (post-event) | ~18+ months (recording compounds) | Recording is what extends the tail |
| YouTube video | ~7 days (algorithmic peak) | Multi-year (search-driven discovery) | Strongest long-tail compounding of any format |

## Why it matters
Decay rates determine three operational decisions:

1. **Repurposing timing.** A LinkedIn post can be repurposed to X within 24 hours without competing with itself; a /thinking article should wait 14+ days to derive new social posts so the original gets its compounding window.
2. **Investment efficiency.** A 4-hour X thread that decays in 24 hours produces ~4 hours of output. A 4-hour /thinking article that compounds for 12 months produces vastly more total reach. Effort allocation should reflect this.
3. **Refresh decisions.** When content is recyclable (annual update of a popular article), the half-life informs when "stale" sets in. A post is stale at week 1; an article isn't stale until quarter 3-4.

The decay rates also explain why Riché's content strategy emphasizes /thinking articles and recorded speaking content over higher-volume social-only output: the long-tail compounding of long-form artifacts produces the bulk of the brand's compounding equity, even though the immediate engagement is smaller per-piece.

## How to apply

**For derivative timing (per `corpus/growth/strategy/repurposing-matrix.md`):**

- Source published Day 0
- Same-channel derivatives can wait 1-2 weeks (don't compete with the original's first-day window)
- Cross-channel derivatives can publish Day 1-3 (different audience surface)
- Long-form source → social derivative: wait until day 5+ so the article's first-week compounding isn't undercut
- Social source → long-form derivative: wait until enough engagement signal exists to inform the long-form (~7-14 days)

**For refresh decisions:**

- Long-form articles >12 months old AND still receiving traffic: candidates for refresh (update examples, add new context, re-publish)
- LinkedIn posts >1 month old: don't refresh; write new (the old one has fully decayed)
- Newsletter issues: don't refresh; the issue is dated by inbox-arrival time
- Conference talks: refresh annually if the framework has evolved; otherwise the recording compounds as-is

**For investment allocation:**

When choosing where to invest 4 marginal hours, the decay rates favor long-form over short-form for almost all uses. The exception: when short-form is being produced as a *derivative* (low marginal cost), in which case the math tilts back toward short-form because the source's investment is sunk.

**For "is this content still useful?" decisions:**

- LinkedIn post 2 weeks old generating engagement: anomaly; investigate (often a peer reshare)
- /thinking article 6 months old generating traffic: expected; healthy
- /thinking article 18 months old generating zero traffic: candidate for refresh OR archive
- Conference talk recording 2 years old still getting views: extend its life with a follow-up post linking it

## Examples
1. **Repurpose timing applied.** A /thinking article on context layer architectures publishes Sunday. Riché waits until the following Friday to publish the LinkedIn carousel derivative — gives the article 5 days of first-week compounding before the social derivative competes for attention.
2. **Refresh decision.** A 2024 article on "Suzy launch context drift" has been generating ~80 visits/month for 18 months. In Q4 2026, traffic drops to ~30 visits/month. Refresh decision: update the article with 2026 context (Helm Labs experiments validating the original lessons), re-publish, share via LinkedIn. Traffic returns to ~120 visits/month for the next 6 months.
3. **Investment-allocation decision.** Faced with 4 free hours: write a LinkedIn deep-dive (~3 weeks of compounding) OR draft a /thinking article (~12 months of compounding). Decision: /thinking article, with LinkedIn derivative coming a week later. Total reach over 12 months: ~5x the LinkedIn-only path.
4. **Decay-aware giving up.** A LinkedIn post from 6 weeks ago Riché is tempted to "repromote." Decay analysis: post is already past its tail; reposting would compete with itself or look like recycling. Decision: skip; write fresh derivative content from the same source artifact instead.

## Related entries
- `corpus/growth/strategy/repurposing-matrix.md` — derivative timing applies decay logic
- `corpus/growth/metrics/repurpose-vs-create-decision.md` — decay informs the repurpose decision
- `corpus/growth/metrics/channel-roi-calculation.md` — long-tail outcomes credit the originating quarter
- `corpus/growth/strategy/channel-evaluation-framework.md` — discovery-and-compounding criterion is decay-informed

## Anti-patterns
- Treating LinkedIn posts as long-tail assets. They aren't; the half-life is ~24 hours.
- Treating /thinking articles as short-tail. They are the compounding engine; investment should reflect that.
- Refreshing every old piece. Most aren't worth it; only the still-trafficked older articles deserve refresh investment.
- Ignoring the decay window when timing derivatives. Same-channel derivatives published in the source's compounding window cannibalize.
