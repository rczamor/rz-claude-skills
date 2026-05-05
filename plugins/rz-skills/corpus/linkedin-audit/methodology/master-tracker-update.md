---
name: Master Tracker Update
domain: linkedin-audit
source_skill: rz-linkedin-audit
entry_type: pattern
length_target: 500-900
related: [corpus/linkedin-audit/databases/master-tracker-sheet-schema.md, corpus/linkedin-audit/methodology/export-parsing.md, corpus/linkedin-audit/views/compounders.md, corpus/linkedin-audit/views/late-bloomers.md]
---

# Master Tracker Update — Methodology

## Mechanism

Use Zapier's `google-sheets` `_zap_raw_request` action. It wraps HTTP to `sheets.googleapis.com/v4/...` with auth from the user's Zapier→Google Sheets connection.

If `google-sheets` isn't enabled in Zapier:

1. `list_enabled_zapier_actions(app="google-sheets")`
2. If empty: `enable_zapier_action(app="google-sheets")`, then prompt user to visit the returned auth URL.

## Operations

All to `https://sheets.googleapis.com/v4/spreadsheets/{MASTER_TRACKER_SHEET_ID}`. `Content-Type: application/json`. `valueInputOption=USER_ENTERED` (NOT `RAW` — formulas need to evaluate).

### Posts Master upsert (key = Post URL, column A)

1. `GET values/Posts Master!A2:A?majorDimension=COLUMNS` for current Post URLs.
2. For matched URLs: `PUT values/Posts Master!A{N}:O{N}?valueInputOption=USER_ENTERED` per row.
3. For new URLs: `POST values/Posts Master!A:O:append?valueInputOption=USER_ENTERED&insertDataOption=INSERT_ROWS` with all new rows in one call.

### Snapshots append

`POST values/Snapshots!A:I:append?valueInputOption=USER_ENTERED&insertDataOption=INSERT_ROWS` with body `{"values": [...]}`.

### Monthly Summary append

`POST values/Monthly Summary!A:K:append?valueInputOption=USER_ENTERED&insertDataOption=INSERT_ROWS` with one row.

### Auto-view formulas (first run only — skip if A1 already has a formula)

1. `POST values:batchClear` with `{"ranges": ["Compounders!A:Z", "'Late Bloomers'!A:Z"]}`.
2. `POST values:batchUpdate` with:

```json
{
  "valueInputOption": "USER_ENTERED",
  "data": [
    {"range": "Compounders!A1", "values": [["=QUERY(Snapshots!A:I, \"SELECT A, B, E, G, I WHERE G > 0 AND I > 7 ORDER BY G DESC LIMIT 20\", 1)"]]},
    {"range": "'Late Bloomers'!A1", "values": [["=QUERY('Posts Master'!A:O, \"SELECT A, C, N, F, I, J WHERE O = 'Late Bloomer'\", 1)"]]}
  ]
}
```

`Late Bloomers` has a space → single-quote in A1 notation. `Compounders` → no quotes.

## Zapier call shape

```python
execute_zapier_write_action(
    app="google-sheets",
    action="_zap_raw_request",
    instructions="<description>",
    output="<what to return>",
    params={
        "method": "POST",
        "url": "<full URL>",
        "headers": {"Content-Type": "application/json"},
        "body": "<JSON string>",
        "fail_on_errors": "true"
    }
)
```

`body` is a JSON string, not an object. Escape inner quotes for QUERY formulas.

## Verification

1. `GET values/Monthly Summary!A:K` — confirm new row.
2. `GET values/Compounders!A1:E5` — confirm QUERY spilled (headers, not formula text).
3. `GET values/'Late Bloomers'!A1:F5` — same.

If A1 shows the literal `=QUERY(...)` string instead of headers, `valueInputOption` was wrong. Must be `USER_ENTERED`.

## Common failures

- **403:** Zapier auth not set up. Run `enable_zapier_action` then prompt for auth URL.
- **Range parse error on Late Bloomers:** missing single quotes around tab name.
- **`#REF!` in QUERY result:** existing content in A2+ blocked spill. Run `batchClear` first.
- **Formula written as text:** `valueInputOption=RAW`. Use `USER_ENTERED`.
