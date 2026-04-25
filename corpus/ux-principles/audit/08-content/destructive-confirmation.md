---
name: Destructive Actions — Confirmation or Undo Window
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/principles/goodwill-reservoir.md, corpus/ux-principles/audit/08-content/button-labels-specific.md]
---

# Destructive Confirmation

## What it is
Any action that destroys data — deleting an account, project, message, file, or removing access — must be guarded by either (a) a confirmation modal that names the consequence, or (b) an undo window after the action with a visible toast and timer. Ideally both.

## Why it matters
Destructive actions are the single biggest goodwill-reservoir killer (`goodwill-reservoir.md`). One unintended deletion can erase trust the product spent months building. Conversely, a generous undo window — Gmail's "Undo Send", Linear's restore-issue toast — turns a moment of panic into a moment of relief. The bar is high because the cost of getting it wrong is high.

## How to apply
- For irreversible / high-stakes actions (delete account, delete production database) — confirmation modal that:
  - Names the object: "Delete repository: rczamor/skills" — not just "Delete?"
  - Names the consequence: "This will delete 247 files and remove access for 3 collaborators."
  - Requires retyping for highest-stakes (typing the project name to confirm) — friction here is welcome.
  - Action button label restates the verb + object: "Delete repository" — not "Yes" / "OK."
- For reversible / lower-stakes actions (delete message, archive task) — perform optimistically, show a toast with "Undo" for 5–10s. Match Gmail's standard.
- Never use "Are you sure?" — vague and trains users to click through.
- Destructive primary buttons use red / danger color, not gray.

## Examples (BAD vs. GOOD pairs)

BAD:
```
Are you sure?
[ Yes ]   [ No ]
```

GOOD — confirmation:
```
Delete project "Helm Labs Q3 Plan"?
This will permanently remove 23 files and revoke access for 2 collaborators.
This can't be undone.

Type "Helm Labs Q3 Plan" to confirm:  [____________]

[ Cancel ]    [ Delete project ]   ← red button, disabled until name matches
```

GOOD — undo:
```
Toast: "Message deleted.   [Undo]"   ← 8 seconds
```

## Related entries
- `corpus/ux-principles/principles/goodwill-reservoir.md` — friction depletes; respect replenishes.
- `corpus/ux-principles/audit/08-content/button-labels-specific.md` — confirmation buttons need specific labels.

## Anti-patterns
- "Are you sure?" — generic, trains tap-through behavior.
- Hard delete with no undo window even for low-stakes actions.
- Identical-looking primary buttons for "Confirm" and "Cancel" — easy mis-tap.
