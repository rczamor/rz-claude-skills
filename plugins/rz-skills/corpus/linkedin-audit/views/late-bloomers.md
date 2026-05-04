---
name: Late Bloomers View
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: framework
length_target: 300-500
related: [corpus/linkedin-audit/databases/master-tracker-sheet-schema.md, corpus/linkedin-audit/views/compounders.md, corpus/growth/strategy/repurposing-matrix.md, corpus/linkedin-audit/methodology/report-assembly.md]
---

# Late Bloomers View

## What it is
The Master Tracker tab that surfaces posts that newly appeared in TOP POSTS this month AND were published more than 30 days ago. These are evergreen content candidates — posts the LinkedIn algorithm rediscovered weeks or months after publish. Worth republishing on richezamor.com as `/thinking/` articles or referencing in newsletter.

Distinct from Compounders: Compounders kept growing while already in TOP POSTS. Late Bloomers entered TOP POSTS for the first time long after publish.

## Why it matters
Late bloomers are the closest thing to free wins in LinkedIn content. They're posts you've already written, already paid the production cost on, and the algorithm — for whatever reason — surfaced them again. The signal is:

1. **The topic has lasting relevance.** A 6-month-old post resurfacing means the topic isn't time-bound.
2. **The hook still works.** Late bloomers usually share strong hooks; the algorithm picked them out of the long tail.
3. **There's amplification potential.** A LinkedIn post that's now performing → republish on richezamor.com (with light edits and SEO optimization) → newsletter mention → potential for compounding.

Without an explicit Late Bloomers view, these posts surface mixed in with new posts in TOP POSTS rankings and Riché never recognizes them as evergreen candidates.

## Definition (Sheet formula)

In the `Late Bloomers` tab, filter `Posts Master`:

```
=QUERY(Posts_Master,
  "SELECT * WHERE Decay_Status = 'Late Bloomer'",
  -1)
```

`Decay Status = 'Late Bloomer'` is set in Posts Master when a post:
- Newly appeared in TOP POSTS this month (was not in TOP POSTS in any prior snapshot), AND
- Was published more than 30 days before the audit's Period End

The Posts Master upsert step (per `master-tracker-update.md`) sets this status during Step 3.

## Output for the audit

The audit page's "Late Bloomers" section narrates each one:

```
{N} previously-quiet posts entered the top 50 this month.

{URL} (published {days_old} days ago) gained traction via {inferred mechanism:
search / share / comment thread / featured by peer / unknown}. The post
covers {topic in 1 short clause}.

{repeat per late bloomer}

Late bloomers signal evergreen content potential — these are candidates
for the website's /thinking/ republication and for newsletter
inclusion when the newsletter launches.
```

If 0 late bloomers, omit the section.

## Inferred mechanism

For each late bloomer, the audit can infer the surfacing mechanism:

- If the post is a Framework or Deep Dive type and the impressions surged in a single week → likely a peer reshare that brought new audience
- If impressions grew steadily over 4+ weeks → likely search/algorithm surfacing (LinkedIn's "people also viewed" or topic clustering)
- If a comment thread on the post is long → likely conversation revival
- If unclear → mark "unknown"

This is an inference, not a measurement. Riché can verify by clicking through the post's notifications or Comments view.

## Examples

1. **Three late bloomers.** A 95-day-old Deep Dive on context evaluation, a 60-day-old Suzy story, a 45-day-old Framework on agent memory. Narrative covers all three with inferred mechanisms. Action item: republish the Deep Dive as `/thinking/evaluating-context-retrieval.md`.
2. **Single late bloomer with peer reshare.** Post resurfaced because Aakash Gupta reshared it (visible in P5 cross-reference). Narrative: "{URL} resurfaced via Aakash reshare. Engagement quality high (Director+ reactions)."
3. **No late bloomers.** Quiet month for the long tail. Section omitted from audit page; narrative briefly notes "No late bloomers this month."

## Related entries
- `corpus/linkedin-audit/databases/master-tracker-sheet-schema.md` — Posts Master Decay Status formula
- `corpus/linkedin-audit/views/compounders.md` — distinct adjacent view
- `corpus/growth/strategy/repurposing-matrix.md` — late bloomers feed `/thinking` republishing
- `corpus/linkedin-audit/methodology/report-assembly.md` — Step 7 narrates this view

## Anti-patterns

- Republishing late bloomers verbatim on `/thinking/`. Adapt for long-form: expand the framework, add concrete examples, add SEO-optimized headers.
- Counting posts <30 days old as late bloomers. Below the 30-day threshold, they're just normal post-life-cycle behavior.
- Treating absence of late bloomers as a problem. Most months have 0-3; 0 is fine.
- Skipping the inferred mechanism. The mechanism is what tells Riché whether to lean into the format (peer reshares = network play) or the topic (search surfacing = SEO play).
