---
name: Repurposing Matrix — One Source, Many Derivatives
domain: growth
source_skill: growth-marketing
entry_type: framework
length_target: 500-800
related: [corpus/growth/strategy/channel-evaluation-framework.md, corpus/growth/playbook/batch-writing-sunday.md, corpus/growth/speaking/recorded-content-strategy.md, corpus/growth/metrics/content-decay-analysis.md, corpus/growth/metrics/repurpose-vs-create-decision.md]
---

# Repurposing Matrix — One Source, Many Derivatives

## What it is
A mapping of each "source" content artifact to the derivatives it should produce across the channel set. The matrix exists because creator-time is the constraint and *most channel-specific time* should be derivative work, not original creation. The 5.25 hr/week budget can sustain ~1 source-grade artifact per week if every source produces 4–8 derivatives across LinkedIn, X, newsletter, GitHub, and the long tail.

## The matrix

| Source artifact | Source cost | Direct derivatives | Total derivative count |
|---|---|---|---|
| **Speaking talk (45 min)** | ~6 hrs prep + delivery | YouTube video (talk recording), 1 LinkedIn carousel, 3 LinkedIn posts (one per main framework), 2 X threads, 1 podcast guest pitch (referencing the talk), 1 /thinking article | 9 derivatives |
| **/thinking article (1500–2500 words)** | ~4 hrs writing + research | 1 LinkedIn article (link + framing), 1 LinkedIn carousel, 3 LinkedIn posts (key claims), 1 X thread, 1 newsletter section (when active), 1 GitHub repo (if code), 5 Reddit comment seeds | 8–12 derivatives |
| **Podcast guest appearance (45 min)** | ~3 hrs prep + recording + show notes | 1 LinkedIn post (announce + best moment), 1 X thread (key takeaways), 1 90-sec video clip (cross-posted LI + X), 1 newsletter mention | 4–5 derivatives |
| **Working demo / GitHub repo** | ~6 hrs build + README | 1 /thinking article, 1 LinkedIn carousel (architecture diagram), 2 LinkedIn posts (design decisions), 1 X thread (build narrative), 1 Show HN candidate, 1 talk pitch | 6–8 derivatives |
| **Newsletter issue (1500–2500 words)** | ~3 hrs (after article exists) | 2 LinkedIn posts (preview + close), 1 X thread (top idea), 1 LinkedIn article version | 4 derivatives |

**Production rule:** the source artifact ships first, then the derivatives roll out across 5–10 days post-source. Derivatives never ship before the source — the source is the authoritative version that derivatives reference.

## Why it matters
The math without repurposing: 5.25 hrs ÷ ~1.5 hrs per LinkedIn post = ~3.5 posts/week. Burnout-adjacent. No room for articles, talks, or anything else.

The math with repurposing: 1 source artifact (4–6 hrs) produces 8–12 derivatives. Each derivative costs 15–45 min of adaptation. The same 5.25 hr budget supports 1 source + ~12 derivatives = 13 distinct pieces of audience-facing content per week.

The compounding logic also matters: a /thinking article repurposed across 5 channels produces 5x the discovery surface for the same intellectual investment. The article also keeps producing value over a 12-month decay window (per `corpus/growth/metrics/content-decay-analysis.md`), while the derivatives generate immediate engagement signal that feeds the algorithm to surface the source.

## How to apply

**Source selection (Sunday batch session):**
1. Pick the week's source artifact: typically a /thinking article, occasionally a talk recording or repo launch.
2. Outline the 6–10 derivatives the source will produce.
3. Schedule the derivative slots across the next 5–10 days.

**Derivative production rule:**
- Every derivative explicitly references the source ("from this week's essay…", "I broke this down in detail at richezamor.com/...")
- Derivative text is rewritten for the platform format, not copy-pasted (per `corpus/growth/anti-patterns/no-cross-platform-copy-paste.md`)
- Derivative content does not reveal more than the source — the source must remain the canonical version

**Adaptation patterns (concrete):**
- **Article → LinkedIn carousel (15 min):** pull the article's framework or list as carousel slides; cover slide + 5–7 content slides + close
- **Article → LinkedIn post (10 min):** lead with the article's most counter-intuitive claim; close with article link
- **Article → X thread (20 min):** punchy first tweet (not the article's intro); 5–9 follow-up tweets restructured for X reading patterns
- **Talk → LinkedIn carousel (30 min):** key slides as carousel; commentary in the post body
- **Demo → /thinking article (4 hrs — this is a NEW source, not a derivative; budget accordingly)

## Derivative timing rules
- **Day 0:** publish source
- **Day 0–1:** publish primary LinkedIn post (the source-announcement + key insight)
- **Day 1–2:** publish X thread (different angle from the LinkedIn post)
- **Day 2–4:** publish LinkedIn carousel (visual format extends the source)
- **Day 5–7:** publish secondary LinkedIn posts (key claims as standalone takes)
- **Day 7–10:** publish derivative comment seeds in target Reddit/HN threads (when relevant)

After day 10, the source decays into long-tail compounding. New derivatives don't generate net-new attention; let it rest.

## Examples
1. **Article-driven week.** Sunday: Riché ships a /thinking article on "Why naive RAG fails for multi-turn agents." Mon: LinkedIn post 1 (counter-intuitive claim from the article). Tue: X thread (different angle). Wed: LinkedIn carousel (the 4-stage framework as slides). Fri: LinkedIn post 2 (specific case study from the article). Following Mon: a LinkedIn post quoting a peer comment from the original post. 6 derivatives from 1 source over 8 days.
2. **Talk-driven week.** Riché delivers a ProductTank NYC talk on Tuesday. Wed: LinkedIn post (quote + key takeaway). Thu: X thread (the talk's framework). Following Sun: YouTube upload of the talk recording. Following Mon: LinkedIn carousel (best slides). Following Wed: long-form /thinking article that extends the talk's argument. 5 derivatives + 1 new source from one talk.
3. **Failure mode (no source).** A week with no source artifact. Three LinkedIn posts get drafted from scratch. Each takes 60–90 min. The week's content output is lower than a derivative-fed week and the time cost is double. Logged as a missed batch session.

## Related entries
- `corpus/growth/strategy/channel-evaluation-framework.md` — channels are scored partly on derivative-fit
- `corpus/growth/playbook/batch-writing-sunday.md` — where source + derivative planning happens
- `corpus/growth/speaking/recorded-content-strategy.md` — the talk-as-source pattern
- `corpus/growth/metrics/content-decay-analysis.md` — half-lives that inform derivative timing
- `corpus/growth/metrics/repurpose-vs-create-decision.md` — extend-an-old-source vs create-new-source

## Anti-patterns
- Skipping the source and only producing derivatives. No source means each "derivative" is actually a new piece — drives time cost back up.
- Publishing all derivatives in 24 hours. Compresses attention; loses the multi-day compounding window.
- Treating derivatives as lesser content. A well-adapted derivative outperforms a rushed original on every metric that matters.
- Repurposing without attribution. Every derivative should make the source easy to find, not bury it.
