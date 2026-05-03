---
name: GitHub as a Distribution Channel
domain: growth
source_skill: growth-marketing
entry_type: pattern
length_target: 400-700
related: [corpus/growth/hooks/practitioner-not-theorist.md, corpus/growth/hooks/live-demo-capability.md, corpus/growth/channels/website-context-layer-demo.md, corpus/growth/strategy/repurposing-matrix.md]
---

# GitHub as a Distribution Channel

## What it is
Public GitHub repositories, gists, and READMEs as a credibility-and-discovery channel. Distinct from GitHub-as-portfolio (showing your work to recruiters); this is GitHub-as-distribution: artifacts that *live* in the GitHub ecosystem (search, trending, stars, forks) and pull traffic into the broader brand. For an AI/PM positioning specifically, this is structurally underused — most PM thought leaders have no public code, which means a working repo is differentiated by absence-of-competition.

## Why it matters
GitHub is the highest-trust artifact a "practitioner not theorist" can produce. Anyone can write a LinkedIn post claiming "I built X." A repo with commits, tests, a README, and ≥10 stars proves it. The practitioner hook (`corpus/growth/hooks/practitioner-not-theorist.md`) and the live-demo hook (`corpus/growth/hooks/live-demo-capability.md`) both depend on artifacts that GitHub is the natural home for.

GitHub also feeds three growth loops the brand currently underuses:

1. **Discovery via topic search.** A repo tagged `context-layer` or `agent-memory` shows up when AI engineers search those tags — high-intent traffic.
2. **Star-based social proof.** Stars are a portable credibility signal that shows on every issue comment, every PR. Crosses platform.
3. **Cross-pollination with HN.** A repo with a working demo is a pre-built "Show HN" candidate (see `corpus/growth/channels/hackernews-launch-mechanics.md`).

The cost is low: ~30–60 min per artifact published, mostly already-spent on the article or demo it accompanies.

## How to apply
- **Every /thinking article that includes code gets a companion repo.** The article references the repo; the repo's README references the article. Two-way link, two-way SEO, two-way reach.
- **Repo naming convention: `{topic}-{format}`.** E.g., `context-layer-demo`, `agent-memory-eval`, `rag-vs-cl-comparison`. Searchable, descriptive, branded across the profile.
- **README discipline** (the README is the "post"):
  - One-paragraph summary up top
  - "Why this exists" link to the originating /thinking article
  - Quickstart that runs in <60 seconds
  - Architecture diagram (PNG; not Mermaid — renders inconsistently)
  - "About the author" link to richezamor.com
- **Pin the top 6 repos on the profile.** GitHub profile is a portfolio; pinning curates the narrative arc.
- **Tag-discipline:** add 5–8 topic tags per repo. `ai`, `llm`, `rag`, `context-layer`, `agent-memory`, `product-management`, `python` (or whatever language). Tags drive the discovery loop.
- **Issue triage cadence: weekly, 15 min.** Drop unmaintained repos to "archived" status rather than letting them rot publicly. An archived repo with stars is fine; a stale repo with open issues damages the practitioner signal.

## What NOT to publish
- Half-finished prototypes that won't run. A broken quickstart is worse than no repo.
- Client work, anything under NDA.
- Personal scratchpads or experiments without a README and a quickstart.
- Forks of other people's repos with no value-add.

## Repurposing chain
GitHub repo → /thinking article (the long-form) → LinkedIn carousel (architecture diagram + 5 takeaways) → 3 LinkedIn posts (one per major design decision) → X thread (the punchy version) → conference talk (next year). One repo, six derivatives. See `corpus/growth/strategy/repurposing-matrix.md` for the full matrix.

## Examples
1. **Article + repo pair.** A 2025 /thinking article on "Why naive RAG fails for multi-turn agents" ships with `context-layer-demo` repo: a 200-line Python implementation of the architecture from the article. The repo gets 47 stars in week 1; the article's traffic doubles vs. articles without companion repos.
2. **Show HN amplification.** The `agent-memory-eval` repo (a benchmark suite for comparing agent memory architectures) is posted to Show HN on a Tuesday morning. Lands on the front page; brings 4,200 GitHub stars and ~2,800 visits to richezamor.com over 48 hours.
3. **Hiatus call.** A repo from 2024 (`pgvector-vs-qdrant`) has accumulated 6 open issues that Riché doesn't have time to triage. Archived with a README note: "Archived as of {date}. Reach out if you want to maintain it." Cleaner than letting issues rot.

## Related entries
- `corpus/growth/hooks/practitioner-not-theorist.md` — the hook this channel proves
- `corpus/growth/hooks/live-demo-capability.md` — the live-demo hook lives in GitHub artifacts
- `corpus/growth/channels/website-context-layer-demo.md` — the website demo + repo cross-link
- `corpus/growth/channels/hackernews-launch-mechanics.md` — Show HN launch sequence
- `corpus/growth/strategy/repurposing-matrix.md` — the chain GitHub feeds

## Anti-patterns
- Publishing a repo without a README. The README *is* the artifact for non-engineers (most of Segment 1).
- Letting open issues pile up. The signal of "active maintainer" matters more than star count for credibility.
- Forking and renaming. Wastes the practitioner signal; original work or nothing.
- Treating GitHub as a private notebook. If it's public, it's a brand artifact — write it for an audience, not for future-you.
