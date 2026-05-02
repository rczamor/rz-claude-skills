# Retrospective mode

Triggered by the SessionEnd hook with a transcript path, or by a manual prompt that names a transcript path or includes "retrospective."

## Inputs

A transcript file path. Likely under `~/.claude/projects/<project-slug>/<session-id>.jsonl`.

## Steps

1. **Read the transcript.** Use Read or Bash to scan the JSONL. Extract user messages and assistant text responses. Skip tool-use payloads unless they contain content (Edit / Write).

2. **Identify learning candidates:**
   - **User corrections.** Phrases like "no", "wrong", "actually", "rewrite this", "stop doing X", "don't ever". Extract the rule the user established. The strongest signal.
   - **Contradicted facts.** Places where a corpus or skill statement was contradicted by session reality (e.g. the skill says "Suzy launched in eight weeks" but the session correction says "six weeks").
   - **Repeated proof points.** New tools, new metrics, new framework names mentioned at least twice in the session that aren't yet in the corpus.

3. **Apply the conservative gate.** Open a PR only if at least ONE of:
   - An explicit user correction was made AND it implies a corpus/skill edit.
   - A factual statement in corpus/skill contradicts session reality.
   - A new proof point or framework was referenced at least twice in the session.

   Otherwise: log "no action" with the reason, and exit.

4. **Locate target files.** For each learning candidate, identify the target corpus / skill file(s). Use `Grep` to find existing references. Prefer editing the canonical corpus entry over the skill pointer.

5. **Check for duplicate PRs.** Use `mcp__github__list_pull_requests` to look for an open PR titled `self-improve: ...` that touches the same area. If one exists, append a commit to it rather than opening a new one. Branch already exists; just update.

6. **Otherwise create a new branch.** Naming: `claude/self-improve-<YYYYMMDD-HHMM>-<short-slug>`. Use `mcp__github__create_branch`.

7. **Apply the edits.** Use Edit / Write to modify the target files. Be surgical, change only what the evidence supports. Preserve the entry schema.

8. **Commit and push.** Stage the changes, commit with a message that quotes the evidence (under 80 chars title, body has the rule + transcript quote).

9. **Open the draft PR.** Use `mcp__github__create_pull_request` with `draft: true`. Body sections:

   ```markdown
   ## Learning
   <One-paragraph statement of what was observed.>

   ## Evidence
   > <Direct quote from the transcript, redacted for tokens/PII>
   (Session: <session-id>, transcript: <path>)

   ## Changes
   - `corpus/<path>.md` (what changed and why)
   - `skills/<path>/SKILL.md` (what changed and why)

   ## Test plan
   - Re-invoke <affected skill> and confirm the updated guidance is loaded.
   - Spot-check related entries for cross-link consistency.
   ```

10. **Return a summary** of what was learned, what changed, and the PR URL.

## Redaction rule

Before quoting any transcript text in the PR body:
- Remove API keys, tokens, secrets, credential-like strings.
- Remove email addresses unless they're public author handles.
- Remove file paths that look private (e.g. paths under `~/.ssh`, `~/.config`).
- Truncate long quotes to 280 chars max with `[...]` ellipsis.
