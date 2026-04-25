---
name: Mobile-Correct Form Inputs (Types & autoFocus)
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-500
related: [corpus/ux-principles/audit/06-responsive/text-readable-no-zoom.md, corpus/ux-principles/audit/05-interaction/touch-targets-44px.md]
---

# Forms Usable on Mobile

## What it is
Use the correct HTML input type for each field so mobile browsers show the appropriate keyboard, and never use `autoFocus` on the first field of a mobile form. Add `inputmode`, `autocomplete`, and `enterkeyhint` for additional polish.

## Why it matters
A user typing a phone number on a default `text` keyboard takes 2× longer than on a `tel` keyboard. Email fields without `type="email"` waste a tap on the @ key. Worst of all, `autoFocus` on mobile pops the keyboard the instant the page loads — pushing the page out of position, often hiding the very field that just got focused, and disorienting users trying to read context.

## How to apply
- `type="email"` for emails (pulls @ key, disables capitalization).
- `type="tel"` for phone numbers (numeric pad).
- `type="number"` only for actual numbers — but prefer `inputmode="numeric"` with `type="text"` for things like OTPs and ZIP codes (avoids spinner UI and arrow keys).
- `type="url"`, `type="search"`, `type="date"`, `type="time"` where they apply.
- `autocomplete="email"`, `"tel"`, `"name"`, `"current-password"`, `"one-time-code"` — gives iOS/Android autofill the right hint.
- `enterkeyhint="next" | "send" | "done"` to label the return key.
- **Never** `autoFocus` the first input on a mobile form. Let the user tap when ready.

## Examples (BAD vs. GOOD pairs)

BAD:
```html
<input type="text" placeholder="Email" autofocus>
<input type="text" placeholder="Phone">
<input type="number" placeholder="ZIP code"> <!-- spinners + decimal accidents -->
```

GOOD:
```html
<input type="email" autocomplete="email" enterkeyhint="next" placeholder="Email">
<input type="tel" autocomplete="tel" inputmode="tel" enterkeyhint="next" placeholder="Phone">
<input type="text" inputmode="numeric" pattern="[0-9]*" autocomplete="postal-code" placeholder="ZIP code">
```

## Related entries
- `corpus/ux-principles/audit/06-responsive/text-readable-no-zoom.md` — input font-size 16px to prevent iOS zoom.
- `corpus/ux-principles/audit/05-interaction/touch-targets-44px.md` — input height ≥44px.

## Anti-patterns
- `type="number"` for OTP codes — spinners appear; mobile shows decimal keyboard.
- `autoFocus` on mobile login pages — keyboard pops, page jumps, user gets lost.
- Forgetting `autocomplete` — every form becomes a hand-typing exercise.
