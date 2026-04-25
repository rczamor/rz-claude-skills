---
name: Scoring — PASS / PARTIAL / FAIL
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/trunk-test.md, corpus/evaluation-frameworks/review-sections/]
---

# Scoring — PASS / PARTIAL / FAIL

## What it is

The scoring rubric for the Trunk Test:

- **PASS:** all 6 wayfinding questions answered clearly. The page stands alone — a cold visitor can orient themselves immediately.
- **PARTIAL:** 4-5 questions answered, 1-2 ambiguous or missing. The page is mostly oriented but has gaps.
- **FAIL:** 3 or fewer questions answered. The page does not provide adequate wayfinding.

A FAIL is a **HIGH-impact finding** regardless of visual polish. Polish does not compensate for navigational confusion.

## Why it matters

A clear three-tier scoring rubric forces the auditor to commit to a verdict. "Mostly fine" is not a category. The rubric also makes the trunk test reportable — engineering teams understand "FAIL → high-impact → must fix" more clearly than soft observations.

The asymmetry of the impact rating (FAIL is always high-impact) is intentional: wayfinding failures cascade. A user who can't orient themselves will fail every other interaction on the page.

## How to apply

1. **Run the trunk test** on every page in scope.
2. **Tally answered questions.** Strict counting — ambiguity counts as not answered.
3. **Apply rubric:**
   - 6 / 6 → PASS
   - 4-5 / 6 → PARTIAL
   - 0-3 / 6 → FAIL
4. **In the audit report:**
   - PASS pages: noted, no action.
   - PARTIAL: medium-impact finding, identify the missing questions.
   - FAIL: high-impact finding, list all unanswered questions, prescribe fixes.
5. **Aggregate scores across pages** for an overall site rating.

## Examples

- **PASS report:** "Trunk test: PASS. All six questions answered via header (logo + nav + search), page title, breadcrumbs, active section indicator."
- **PARTIAL report:** "Trunk test: PARTIAL (4/6). Missing: question 5 (no breadcrumbs on deep pages); question 6 (search buried in menu). Recommendation: add breadcrumbs, surface search in header."
- **FAIL report:** "Trunk test: FAIL (2/6). Logo links nowhere; no page title; hamburger menu hides primary nav. HIGH-impact finding — re-architect the page chrome before further polish."

## Related entries

- `corpus/ux-principles/audit/trunk-test.md` — the underlying test
- `corpus/evaluation-frameworks/review-sections/` — how to integrate into a review

## Anti-patterns

- Scoring with too much grace ("close enough"). The rubric is strict on purpose.
- Treating PARTIAL as "fine, polish later." It's medium-impact and worth fixing in the same pass.
