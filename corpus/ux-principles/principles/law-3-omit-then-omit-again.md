---
name: "Law 3: Omit, Then Omit Again"
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-800
related: [corpus/ux-principles/principles/three-laws-overview.md, corpus/ux-principles/audit/08-content/happy-talk-detection.md, corpus/ux-principles/audit/08-content/instructions-detection.md, corpus/evaluation-frameworks/cognitive-patterns/17-subtraction-default.md]
---

# Law 3: Omit, Then Omit Again

## What it is

Get rid of half the words on each page, then get rid of half of what's left. Happy talk — self-congratulatory text that tells users how great the site is — must die. Instructions must die. If they need reading, the design has failed.

This is the most resisted law because every team that worked on the page has a paragraph they fought for. Cut anyway.

## Why it matters

Users scan; they don't read. Every word on a page costs something — either it earns its place by helping the user, or it dilutes the words that do. Welcome paragraphs, "we're excited to..." phrases, redundant explanations of obvious affordances, and instructions that compensate for unclear UI all reduce the signal-to-noise ratio. Users skip them, then miss the actually useful copy because they've trained themselves to skip.

## How to apply

1. **Count the words.** On any page, classify each text block as "useful content" vs. "happy talk" (welcome paragraphs, self-congratulation, instructions nobody reads). Report: "This page has X words. Y (Z%) are happy talk."
2. **Kill happy talk on sight.** "Welcome to [X]", "Your all-in-one solution for...", "Unlock the power of..." — flag and remove.
3. **Treat instructions as design defects.** Any instruction longer than one sentence is compensating for unclear UI. Flag both the instructions AND the interaction they're hiding.
4. **Run the omit-twice pass.** First pass: remove obvious filler. Second pass: from what remains, remove anything not load-bearing. Most pages survive both rounds.

## Examples

- **BAD:** "Welcome to Acme! We're excited to have you here. Acme is your all-in-one solution for managing your team's projects. To get started, simply click the button below to create your first project."
- **GOOD:** "Create project" button.
- **BAD:** Field with helper text "Please enter your email address in the format name@domain.com so we can send you important updates about your account."
- **GOOD:** Field labeled "Email" with placeholder `name@example.com`.
- **GOOD:** Stripe's docs — every word load-bearing, every example minimal, no "as you can see" filler.

## Related entries

- `corpus/ux-principles/principles/three-laws-overview.md`
- `corpus/ux-principles/audit/08-content/happy-talk-detection.md`
- `corpus/ux-principles/audit/08-content/instructions-detection.md`
- `corpus/evaluation-frameworks/cognitive-patterns/17-subtraction-default.md` — the underlying CEO pattern

## Anti-patterns

- "Marketing wants the welcome paragraph." Marketing is not the user. The user wants to do their job.
- "We need instructions because users get confused." Then the design is confusing. Fix the design, not the instructions.
