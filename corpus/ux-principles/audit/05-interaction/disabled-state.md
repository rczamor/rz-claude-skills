---
name: Disabled State — Reduced Opacity + cursor:not-allowed
domain: ux-principles
source_skill: design-review
entry_type: rule
length_target: 300-450
related: [corpus/ux-principles/audit/05-interaction/cursor-pointer.md, corpus/ux-principles/audit/03-color/wcag-aa-contrast.md]
---

# Disabled State — Reduced Opacity + cursor:not-allowed

## What it is

A disabled interactive element (button, input, link) should:

1. Be visually de-emphasized (typically 40-60% opacity, or a muted color).
2. Show `cursor: not-allowed` on hover.
3. Have `disabled` attribute (HTML) or `aria-disabled="true"` (for non-button elements).
4. Not respond to clicks.

The visual state communicates "this is currently unavailable"; the cursor reinforces; the attribute prevents interaction and tells assistive tech.

## Why it matters

Disabled states often signal what's required to enable an action: a Submit button stays disabled until the form is valid. Users see the disabled button, read the form for what's missing, and proceed. Without a clear disabled state, the user clicks, nothing happens, and they don't know why.

Make sure the disabled state is also accessible — text contrast can drop below WCAG AA for disabled text per the spec, but it should still be readable. Don't go below ~30% opacity.

## How to apply

1. **CSS:**
   ```css
   button:disabled,
   button[aria-disabled="true"] {
     opacity: 0.5;
     cursor: not-allowed;
     pointer-events: none;
   }
   ```
   Or muted color:
   ```css
   button:disabled {
     background: var(--color-disabled);
     color: var(--color-text-disabled);
     cursor: not-allowed;
   }
   ```
2. **Use the `disabled` HTML attribute on form elements.** It prevents submission and notifies assistive tech.
3. **For non-button clickables**, use `aria-disabled="true"` and prevent the click handler from running.
4. **Tooltip explaining why** can help: "Fill out all required fields to enable Submit."

## Examples

- **GOOD:** A Submit button at 50% opacity, `cursor: not-allowed`, and a tooltip "Complete the email field to submit." User knows exactly what to fix.
- **BAD:** A button that's normal-color but does nothing on click — user clicks repeatedly, frustrated, doesn't know it's disabled.
- **GOOD:** A "Save" button disabled until the form has changes. Visible state change reassures users their changes are tracked.
- **BAD:** A disabled button with no visual difference from an enabled one. Looks broken.

## Related entries

- `corpus/ux-principles/audit/05-interaction/cursor-pointer.md`
- `corpus/ux-principles/audit/03-color/wcag-aa-contrast.md`

## Anti-patterns

- Hiding disabled buttons entirely. The user loses the affordance — they don't know the action exists.
- Disabled state that's nearly identical to enabled — opacity 0.95, no cursor change. Looks like a bug.
