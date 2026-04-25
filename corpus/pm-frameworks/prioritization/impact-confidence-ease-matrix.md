---
name: Impact / Confidence / Ease Matrix
domain: pm-frameworks
source_skill: research
entry_type: framework
length_target: 500
related: [corpus/pm-frameworks/prioritization/ice-scoring.md, corpus/pm-frameworks/prioritization/rice-scoring.md]
---

# Impact / Confidence / Ease Matrix (2×2 Visual)

## What it is

A visual variant of ICE scoring popularized by Reforge and growth-team practice. Plot candidate initiatives on a 2×2 matrix:

- **X-axis:** Effort/Ease (Easy ↔ Hard)
- **Y-axis:** Impact (Low ↔ High)
- **Bubble size or color:** Confidence (encoded so high-confidence initiatives stand out)

The four quadrants:
1. **Quick wins** (high impact, easy): do first.
2. **Big bets** (high impact, hard): plan for; sequence with confidence.
3. **Fill-ins** (low impact, easy): batch when capacity allows.
4. **Time sinks** (low impact, hard): kill or defer indefinitely.

## Why it matters

The visual matrix surfaces portfolio shape that ICE's collapsed score hides. A team whose roadmap is 80% time-sinks looks fine in spreadsheet form (each item has a positive ICE) but wrong in matrix form (the cluster is in the wrong quadrant). The 2×2 forces a portfolio conversation, not a one-by-one ranking conversation.

For high-velocity teams, the matrix doubles as a sprint-planning artifact: pick all the quick wins, one big bet, batch the fill-ins, and kill the time sinks. That sequence beats most explicit prioritization formulas in practice because it surfaces shape decisions stakeholders actually care about.

## How to apply

1. **List candidate initiatives** (8–20 typically).
2. **Score each on Impact, Effort, Confidence.** Use the same 1–10 scale as ICE.
3. **Plot on the 2×2.** Encode Confidence as bubble size (large = high confidence) or color (green = high, red = low).
4. **Read the quadrants:**
   - Quick wins → ship next sprint.
   - Big bets → discovery and assumption tests now; build later if validated.
   - Fill-ins → batch into spare capacity.
   - Time sinks → kill or defer to a future re-evaluation.
5. **Re-plot when major signals change** — model improvements, new customer data, competitive moves.

## Examples

1. **Suzy planning offsite.** Plotted 14 initiatives on the 2×2. Cluster of seven in time-sinks revealed an over-investment in middle-of-the-road defensive work. Two quick wins (in-app empty states; analyst-search query expansion) leapt forward; three big bets earned discovery resources; the seven time-sinks were deferred or killed.
2. **Helm Labs sequencing.** Pre-launch initiatives plotted: warm-intro outbound (quick win, high confidence) ahead of paid acquisition (low confidence, low impact at this stage = time sink). The visual made the sequencing argument easier to communicate to advisors than a spreadsheet.

## Related entries

- `corpus/pm-frameworks/prioritization/ice-scoring.md` — same factors, scored as formula
- `corpus/pm-frameworks/prioritization/rice-scoring.md` — adds Reach as a fourth dimension

## Anti-patterns

- **Cluster in the upper-left** (high impact, easy, high confidence). Suspect inflation. Real product work rarely has many "easy + high impact + high confidence" initiatives — those would have shipped already.
- **Plotting once, never again.** The matrix is a snapshot. Without re-plotting at planning cycles, it ossifies into wishful thinking from six months ago.
