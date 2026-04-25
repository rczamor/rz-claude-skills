# Corpus Inventory — Master Worklist

**Status:** Phase 0 in progress — slices are being filled by research agents. This file is the merged view; individual slices live in `corpus/INVENTORY/{domain}.md`.

**User review gate:** Once all 10 slices are filled and this file is merged, the session stops and asks the user to approve or edit before any of the ~450 entries are authored.

## Summary table (updated after research agents return)

| # | Domain                   | Entries | Inventory slice |
|---|--------------------------|---------|-----------------|
| 1 | voice                    | TBD     | [INVENTORY/voice.md](INVENTORY/voice.md) |
| 2 | content-system           | TBD     | [INVENTORY/content-system.md](INVENTORY/content-system.md) |
| 3 | pm-frameworks            | TBD     | [INVENTORY/pm-frameworks.md](INVENTORY/pm-frameworks.md) |
| 4 | growth                   | TBD     | [INVENTORY/growth.md](INVENTORY/growth.md) |
| 5 | networking               | TBD     | [INVENTORY/networking.md](INVENTORY/networking.md) |
| 6 | office-hours             | TBD     | [INVENTORY/office-hours.md](INVENTORY/office-hours.md) |
| 7 | brand-system             | TBD     | [INVENTORY/brand-system.md](INVENTORY/brand-system.md) |
| 8 | ux-principles            | TBD     | [INVENTORY/ux-principles.md](INVENTORY/ux-principles.md) |
| 9 | ai-product-ux            | TBD     | [INVENTORY/ai-product-ux.md](INVENTORY/ai-product-ux.md) |
| 10| evaluation-frameworks    | TBD     | [INVENTORY/evaluation-frameworks.md](INVENTORY/evaluation-frameworks.md) |
|   | **Total**                | **TBD** | |

## Per-entry format

Each inventory slice contains one line per entry:

```
{filename}.md  |  {entry_type}  |  {one-line hook}  |  source: {skill | research}  |  est_words: {N}
```

Entry types: `rule | framework | pattern | template | concept | person | resource | metric`

`source: skill` — language will be pulled directly from the source skill during authoring.
`source: research` — derived from public canon (JTBD, Wardley, AARRR, etc.); authoring agent cites the canonical reference.
