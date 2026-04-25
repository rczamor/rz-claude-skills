---
name: Mindless Choice Audit — Every Click Should Be Obvious
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 500-600
related: [corpus/ux-principles/principles/law-2-clicks-dont-matter-thinking-does.md, corpus/ux-principles/principles/law-1-dont-make-me-think.md, corpus/ux-principles/audit/01-hierarchy/clear-focal-point.md]
---

# Mindless Choice Audit — Every Click Should Be Obvious

## What it is

The mindless choice audit is the operationalized form of Law 2 ("clicks don't matter, thinking does"). For every decision point on every page — every button, link, dropdown, menu choice, modal option — ask: **is this click mindless? Is it obvious what will happen and that this is the right path?**

If a click requires the user to think about whether it's the right choice (vs. another visible option), it is NOT mindless. **Flag it as a HIGH-impact finding.**

This is one of the most powerful audits in design because it surfaces failures users feel but can't articulate — the "I wasn't sure if I should click this" moments that drain attention.

## Why it matters

Most usability problems are mindless-choice failures: a Continue button that doesn't say what continues; two visually-equal buttons forcing comparison; a menu item whose label gives no clue about destination; a modal with three "OK / Cancel / Don't ask again" options where the differences aren't clear.

These don't usually appear in heuristic checklists because they require contextual judgment — but they're the highest-impact UX failures because they happen at every interaction point.

## How to apply

1. **At every decision point, ask three questions:**
   - **Does the user know what will happen if they click this?**
   - **Does the user know this is (or isn't) the right choice for what they want?**
   - **Could a competing option pull them away in confusion?**
2. **If the answer to any is "they'd have to think,"** flag the choice.
3. **Common offenders:**
   - **Generic labels:** "Continue", "Submit", "OK", "Yes/No" without context.
   - **Two equally-weighted CTAs:** "Sign up" and "Sign in" rendered identically.
   - **Modal choice ambiguity:** "Save / Don't save / Cancel" — what's the difference between Don't save and Cancel?
   - **Dropdown / menu items without sub-labels:** "Settings" → "Account / Privacy / Security / Other" — which one has password change?
4. **Fix patterns:**
   - Replace generic labels with verb + noun ("Save API Key").
   - Visually distinguish primary from secondary actions.
   - Restructure ambiguous choices ("Save changes" vs. "Discard changes" — clearer than Save/Don't Save).
   - Add sub-labels or icons to menu items.

## Examples

- **GOOD:** A modal "Are you sure?" with two clear buttons: "Delete account" (red) and "Keep my account" (gray). Mindless: the user knows exactly what each does.
- **BAD:** Same modal with "Yes" and "No". Yes to what? The user re-reads the question.
- **GOOD:** A signup CTA labeled "Start free trial — no credit card" — the user knows what they're getting.
- **BAD:** Same CTA labeled "Get started" with three competing buttons of equal weight ("Pricing", "Features", "Contact").
- **GOOD:** Confirmation: "Save changes? Save / Discard." Both verbs unambiguous.
- **BAD:** Confirmation: "Are you sure? OK / Cancel." User has to map OK and Cancel to actions.

## Related entries

- `corpus/ux-principles/principles/law-2-clicks-dont-matter-thinking-does.md` — the underlying law
- `corpus/ux-principles/principles/law-1-dont-make-me-think.md` — same principle, broader frame
- `corpus/ux-principles/audit/01-hierarchy/clear-focal-point.md` — one primary CTA prevents this

## Anti-patterns

- Treating mindless-choice failures as "user error." If users are confused, the choice was not mindless.
- Defaulting to "OK / Cancel" or "Yes / No" for any confirmation. Use the verb the action represents.
