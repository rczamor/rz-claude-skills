---
name: Admin UI Stack (Context Layer Engine)
domain: ai-product-ux
source_skill: product-design
entry_type: resource
length_target: 500
related: [corpus/ai-product-ux/design-system/web-stack.md, corpus/ai-product-ux/design-system/motion-rules.md, corpus/ai-product-ux/context/audit-log.md, corpus/ai-product-ux/context/context-quality-display.md, corpus/brand-system]
---

# Admin UI Stack (Context Layer Engine)

## What it is
The default frontend stack for Riché's internal / admin-facing surfaces — primarily the Context Layer Engine admin UI. **HTMX + Tailwind CSS, dense dashboard layouts, server-rendered with progressive enhancement.** Optimized for scanning by operators, not reading by end users. Tables, metrics cards, timeline views, configurable panels.

## Why it matters
Admin UIs serve a different job than customer-facing surfaces. The user is an operator who needs information density, not narrative. They scan, query, and configure — they don't read. HTMX is a deliberate counter-choice to the customer-facing Next.js stack: server-rendered, fast, and well-suited to dense data displays without the React overhead. The split stack also reflects different deployment cadences — admin UI ships with the engine; the customer-facing demos ship independently.

## How to apply
1. **HTMX over a server framework (Flask / FastAPI / Rails).** Server renders dense HTML; HTMX handles partial updates. No React build pipeline to maintain.
2. **Tailwind CSS with the same tokens as the web stack.** Visual coherence between admin and customer-facing surfaces — same colors, same type, same spacing scale. Different layouts.
3. **Dashboard-style layout grid.** Fixed sidebar, top utility bar, content area split into configurable panels (sources / quality scores / audit log / synthesis preview).
4. **Tables, metrics cards, timeline views.** Operators scan tables for outliers; metrics cards for state; timelines for cause-and-effect. All three live on every screen.
5. **Optimized for keyboard.** Admin users live in keyboard. Every surface action gets a shortcut.

## Examples
1. **Context Layer Engine admin UI.** Server-rendered HTMX + Tailwind. Operators configure context-generation pipelines, inspect audit logs, tune quality thresholds. The visual language matches `corpus/brand-system` — Neural Architect dark theme — even though the stack differs from the customer-facing surfaces.
2. **Counter-example: most enterprise admin UIs.** Bootstrap 4 + jQuery, no design system, no consistency with the customer-facing brand. The contrast is the point — Riché's products are visually coherent across customer and admin surfaces in a category that almost never is.

## Related entries
- `corpus/ai-product-ux/design-system/web-stack.md` — the customer-facing counterpart (Next.js)
- `corpus/ai-product-ux/design-system/motion-rules.md` — the motion language (sparse, in admin contexts)
- `corpus/ai-product-ux/context/audit-log.md` — the canonical admin surface
- `corpus/ai-product-ux/context/context-quality-display.md` — the metric cards admin renders
- `corpus/brand-system` — the visual identity shared across stacks

## Anti-patterns
- **One stack to rule them all.** Forcing Next.js into the admin context just for consistency. The job is different; the stack should be different.
- **Visual divergence.** Letting admin UI ship with no design system because "it's just internal." Operators are users too; they internalize whatever you give them.
