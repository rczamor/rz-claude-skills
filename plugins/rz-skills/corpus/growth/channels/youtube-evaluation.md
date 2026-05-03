---
name: YouTube Channel Evaluation
domain: growth
source_skill: growth-marketing
entry_type: framework
length_target: 500-800
related: [corpus/growth/strategy/channel-evaluation-framework.md, corpus/growth/strategy/repurposing-matrix.md, corpus/growth/playbook/channel-gates-for-adding.md, corpus/growth/anti-patterns/no-channel-sprawl.md, corpus/growth/speaking/recorded-content-strategy.md]
---

# YouTube Channel Evaluation

## What it is
Long-form video on YouTube. The most durable creator asset (a 5-year-old YouTube video can still drive monthly traffic; a 5-day-old LinkedIn post is dead). For Riché's positioning, the right format is *demo + commentary*: screen-recorded walkthroughs of context layer architectures, retrieval evals, agent memory implementations, with talking-head intro/outro. Currently **not** the right channel — production cost (3–6 hrs per 10-min video) breaks the time budget without proportional return at current audience size.

## Why it matters
YouTube is asymmetric: bad videos die fast and don't damage the brand; great videos compound for years. The format also serves three things LinkedIn and X cannot:

1. **Long-form technical depth** that the LinkedIn algo punishes (10+ minutes of architecture walkthrough).
2. **Search discovery** that compounds — YouTube is the world's #2 search engine and dominates "how to implement X" intent.
3. **Live-demo proof** that aligns with the `practitioner-not-theorist` and `live-demo-capability` hooks. A 12-minute "here's a working context layer in 80 lines of Python" video is the strongest possible artifact of that hook.

The reason it's deferred isn't strategic fit — fit is excellent. It's production economics: at sub-1K subscribers, 4 hours of production yields ~200 views. That same 4 hours produces 5 LinkedIn posts reaching ~10K impressions.

## When to launch (the gates)
All four must be true:

1. **≥3 talks delivered with usable recordings.** First 3–5 YouTube videos should be edited talk recordings, not new productions. Talk content is already drafted and rehearsed; YouTube becomes a free amplification channel for existing speaking work.
2. **≥10 /thinking articles published.** Source material for "article + demo" derivatives.
3. **A clean recording setup (mic, camera, OBS or similar).** Quality threshold: indistinguishable from Aakash Gupta or Lenny's solo videos. If the setup isn't there, the videos look amateur and damage the practitioner positioning.
4. **A 6-month commitment to monthly cadence.** YouTube punishes inconsistency harder than LinkedIn. Below 1 video/month, the algorithm treats the channel as inactive.

If any gate is open, defer. The recorded-content-strategy lives in `corpus/growth/speaking/recorded-content-strategy.md` and pre-stages the asset library.

## How to apply (pre-launch)
- **Recording-quality every speaking gig.** Even when the conference doesn't record, run a personal recording. These become the seed library.
- **No vlog-style content.** "A day in the life of an AI PM" is the wrong format for the brand. Stick to demos and talk recordings.
- **No YouTube Shorts.** See `corpus/growth/anti-patterns/no-tiktok-reels.md` — short-form vertical doesn't fit the audience.

## How to apply (post-launch — design rules)
- **Cadence: monthly, minimum.** Two cadence-recovery missed videos within 6 months → put the channel on hiatus and re-evaluate gates.
- **Format mix: 60% talk recordings (already produced), 30% article derivatives (script-light, screen-record + narration), 10% original demos.** Original-demo episodes are the highest-effort, lowest-frequency category.
- **Title format: outcome-led.** "I built a context layer in 80 lines of Python" beats "Context layer architecture explained." The demo is the proof.
- **Description: full transcript + 5+ links + chapter timestamps.** YouTube SEO + accessibility + cross-channel referral.
- **Cross-post a 90-second clip to LinkedIn and X within 24 hours.** Drives the first wave of views to seed the algorithm.

## Examples
1. **Talk-recording derivative.** Riché delivers a ProductTank NYC talk in June 2026. The personal recording (45 min) is edited to 22 min, titled "Why your RAG system is not a context layer (talk recording)," published on YouTube the following Sunday. 90-second teaser clip on LinkedIn drives ~40 views in week 1.
2. **Article derivative.** A 2025 /thinking article on Active Generation pipelines becomes a 14-min video walkthrough with screen-recorded code. Published as the "monthly demo" video.
3. **Hiatus decision.** After 8 months of monthly videos with average views <500 and zero subscriber inflection, Riché puts the channel on hiatus. Existing videos remain (they continue to compound on search). New production stops until a clear unlock condition (e.g., a viral talk, a referenced research paper).

## Related entries
- `corpus/growth/strategy/channel-evaluation-framework.md` — the criteria scoring
- `corpus/growth/strategy/repurposing-matrix.md` — talk → YouTube → LinkedIn → X derivative chain
- `corpus/growth/playbook/channel-gates-for-adding.md` — the gate discipline
- `corpus/growth/speaking/recorded-content-strategy.md` — pre-stages the asset library
- `corpus/growth/anti-patterns/no-channel-sprawl.md` — must displace something to launch

## Anti-patterns
- Launching with a "intro to my channel" video. Loses 90% of the few viewers who arrive. Lead with the strongest demo.
- Sub-monthly cadence with sporadic uploads. The algorithm reads inconsistency worse than absence.
- Production-quality below the practitioner peer baseline. A grainy webcam undermines the "I built this for real" hook.
- Vlogs, day-in-the-life, or face-camera-only takes. Wrong format for the positioning; demo + commentary or nothing.
