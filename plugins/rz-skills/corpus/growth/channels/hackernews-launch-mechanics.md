---
name: Hacker News Launch Mechanics (Show HN)
domain: growth
source_skill: growth-marketing
entry_type: pattern
length_target: 400-700
related: [corpus/growth/channels/github-as-distribution.md, corpus/growth/channels/website-context-layer-demo.md, corpus/growth/strategy/channel-evaluation-framework.md, corpus/growth/anti-patterns/no-untargeted-posts.md]
---

# Hacker News Launch Mechanics (Show HN)

## What it is
Hacker News (`news.ycombinator.com`) is the highest-leverage one-shot launch surface for a working technical artifact. A successful Show HN can drive 5,000–50,000 visits in 48 hours, ~100–500 GitHub stars, and 50–200 quality follow-up DMs/emails. The cost: ~2 hours of preparation per attempt; success rate is ~15% per attempt for a credible artifact. Unlike LinkedIn or X, HN traffic is dense with builders, founders (Segment 3), and senior engineers — the highest-fit audience for the practitioner positioning.

## Why it matters
HN is structurally optimized for one thing: launching technical artifacts to an audience of builders. For Riché's positioning — practitioner-first, demo-driven, context layer thesis — HN is the closest thing to a perfect-fit launch channel. Three reasons:

1. **Audience overlap is exceptional.** Segment 3 (AI founders Seed–Series B) reads HN daily. A successful Show HN reaches more of Segment 3 than 6 months of LinkedIn posting.
2. **The format rewards the practitioner positioning.** HN penalizes marketing voice; rewards specific, runnable, opinionated work.
3. **The compounding artifact survives.** Top HN posts get archived, referenced for years, and re-discovered through search. A successful Show HN from 2026 can still drive traffic in 2029.

The downside risk is reputation: a poorly-prepared launch that flames out (or worse, gets dismissed by top commenters as "low-effort AI hype") is a brand cost that outlasts the failed launch. Don't post until ready.

## When to attempt a Show HN
A candidate is ready when ALL of these are true:

1. **A runnable artifact exists.** Working code, working demo, working tool. Not a blog post; not a "thought leadership" piece. HN dismisses opinion launches.
2. **The artifact has a one-sentence thesis.** "X is broken; here's a working alternative" or "I built X in Y" or "Show HN: X (does Y at Z scale)."
3. **Documentation is clean.** README that runs in <60 seconds; clear quickstart; honest about what doesn't work yet.
4. **Riché has 6+ hours blocked across 48 hours after launch.** HN demands immediate, substantive engagement with comments. Disappearing after launch is the #1 cause of failed Show HNs.
5. **HN account exists with ≥1 month of substantive comment history.** Brand-new accounts get scrutinized harder; ~30 days of thoughtful comments on others' posts establishes baseline credibility.

## Timing rules
- **Best window: Tuesday or Wednesday, 8–10 AM Pacific Time.** Highest active reader count, lowest competing-launch density.
- **Avoid: Mondays (rough algo behavior), Fridays (dies on the weekend), tech earnings days (drowned out).**
- **Avoid the 24 hours after a major OpenAI / Anthropic announcement.** The front page is saturated with reactions; new launches drown.
- **One Show HN per topic per quarter.** Repeat launches of the same project look spammy.

## How to apply
**Title format:** `Show HN: {Project name} – {one-sentence what + why}`
- Good: "Show HN: context-layer-demo – A working RAG-vs-context-layer comparison in 80 lines"
- Bad: "Show HN: Check out my new context layer project!"

**Body format (the launch comment):**
- 2 sentences on what the project does
- 1 sentence on why you built it (problem statement)
- 1 line on what it doesn't do yet (honesty signal)
- Ask for specific feedback (not generic "thoughts?")
- Total: ~120 words. HN punishes long launch comments.

**Post-launch engagement (the work):**
- **First 30 min:** monitor for early comments. Reply to every substantive comment within 5 min. Early replies signal engagement to the algorithm.
- **First 4 hours:** every comment gets a substantive reply. Critique gets engaged with seriously, not defended against.
- **Hours 4–24:** check every 2 hours. Reply to questions, update the README based on feedback, ship quick fixes.
- **Hours 24–48:** declining attention; reply only to high-value threads.

**The follow-up (week 1):**
- Cross-post to LinkedIn and X with "the Show HN that…" framing on day 2 (don't do it day 1; let HN traffic peak organically).
- Write a short retrospective on richezamor.com if it took off (not if it didn't — failed launches don't deserve a postmortem post).
- Add every quality follow-up DM to HubSpot as a Tier 2 networking contact.

## Examples
1. **Successful launch.** Tuesday, 9 AM Pacific. `agent-memory-eval` (a benchmark suite). Lands on front page (#7) by 10:30 AM. Riché clears the calendar; replies to ~80 comments over 48 hours. 4,200 GitHub stars; 2,800 richezamor.com visits; 47 quality DMs (3 became podcast invites). One Show HN; one quarter of inbound traffic.
2. **Failed launch (avoided).** A 2025 article-only "Show HN" of a /thinking essay. Riché doesn't post — HN doesn't reward essays. Posted to LinkedIn instead.
3. **Mid-tier launch.** A demo posted on a Tuesday after a major Anthropic announcement. Reaches #34, drops off in 6 hours, ~200 visits. Riché learns the timing rule; doesn't repeat.

## Related entries
- `corpus/growth/channels/github-as-distribution.md` — every Show HN needs a GitHub repo
- `corpus/growth/channels/website-context-layer-demo.md` — the website demo as Show HN candidate
- `corpus/growth/strategy/channel-evaluation-framework.md` — channel scoring (HN is a one-shot, not recurring)
- `corpus/growth/anti-patterns/no-untargeted-posts.md` — HN especially punishes untargeted launches

## Anti-patterns
- Show HN of an article or essay. HN expects a *thing*; essays go on LinkedIn.
- Multiple accounts upvoting the launch. Detected, banned, brand cost.
- Disappearing after launch. The single highest-cost failure mode; auto-killed by the algo when the OP doesn't engage.
- Defending the project against critique. HN respects intellectual honesty more than authorial defensiveness.
- Reposting after a failed launch. Wait a quarter, change the angle, try again.
