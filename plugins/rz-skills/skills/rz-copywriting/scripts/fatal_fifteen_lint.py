#!/usr/bin/env python3
"""
Fatal Fifteen voice linter for Riché Zamor's drafts.

Applies the 15 voice rules from corpus/voice/fatal-fifteen-*.md to a draft.
Most rules map to regex patterns; a few require structural analysis
(paragraph rhythm, multi-phrase bolding).

Usage:
    fatal_fifteen_lint.py <path-to-draft.md>
    cat draft.md | fatal_fifteen_lint.py -
    fatal_fifteen_lint.py draft.md --json     # machine-readable output

Exit codes:
    0  no violations
    1  violations found
    2  bad input

This is a heuristic linter. False positives are possible. The test of
truth is "would Riché actually say this?"; if a flagged line passes
that test, override with judgment.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class Violation:
    rule_id: str
    rule_name: str
    line: int
    column: int
    matched_text: str
    fix_hint: str


# Regex-based rules. Each rule's pattern matches the offending construction.
# Patterns are case-insensitive unless the construction is meaningful only in
# a specific case (rare).
REGEX_RULES = [
    {
        "id": "F01",
        "name": "In today's openers",
        "pattern": r"\bin today'?s\b",
        "flags": re.IGNORECASE,
        "fix": "Open with a specific moment, decision, or metric. Never start with a civilizational frame.",
    },
    {
        "id": "F02",
        "name": "Filler transitions",
        "pattern": r"\b(moreover|furthermore|additionally|that being said|that said|it'?s worth noting)\b",
        "flags": re.IGNORECASE,
        "fix": "Cut the transition. If the next idea genuinely depends on the prior one, restate the dependency in concrete terms.",
    },
    {
        "id": "F04",
        "name": "Empty superlatives",
        "pattern": r"\b(game[- ]changing|revolutionary|unprecedented|cutting[- ]edge|groundbreaking|paradigm[- ]shift|world[- ]class|next[- ]generation|state[- ]of[- ]the[- ]art)\b",
        "flags": re.IGNORECASE,
        "fix": "Replace with a specific verifiable claim (a number, a comparison, a named outcome).",
    },
    {
        "id": "F05",
        "name": "Faux-profound closings",
        "pattern": r"(as we navigate|the future of \w+ is being|we stand at an? inflection point|in this brave new world|now more than ever)",
        "flags": re.IGNORECASE,
        "fix": "Close with a concrete next step, a specific question, or a sharp reframe of the opening.",
    },
    {
        "id": "F11",
        "name": "Dive in / Buckle up / Here's the thing",
        "pattern": r"\b(let'?s dive in|buckle up|here'?s the thing)\b",
        "flags": re.IGNORECASE,
        "fix": "Cut the stage cue. Just say the next sentence.",
    },
    {
        "id": "F12",
        "name": "Thrilled / excited / honored to announce",
        "pattern": r"\b(i'?m (thrilled|excited|honored)|beyond (stoked|excited)|so (excited|thrilled|honored))\b",
        "flags": re.IGNORECASE,
        "fix": "Open with what you actually built or shipped. Skip the announcement framing.",
    },
    {
        "id": "F13",
        "name": "Navigate metaphor",
        "pattern": r"\bnavigat(e|ing) (the |this |these |an? |complex|changing|evolving|uncertain|new)",
        "flags": re.IGNORECASE,
        "fix": "Replace with a concrete verb (handle, decide, choose, build through, work around).",
    },
    {
        "id": "F15",
        "name": "Key Takeaway summary block",
        "pattern": r"^\s*(\*\*)?(key takeaway|bottom line|tl;?dr|main point|the takeaway)(\*\*)?\s*[:.]",
        "flags": re.IGNORECASE | re.MULTILINE,
        "fix": "Trust the reader. Cut the summary block.",
    },
    {
        "id": "VAP",
        "name": "Em dash (voice anti-pattern)",
        "pattern": r"—",
        "flags": 0,
        "fix": "Replace with a comma, period, or parentheses. Em dashes are a load-bearing AI tell in this voice.",
    },
]

# Performative rhetorical questions: a question whose phrasing is a generic
# "what does this mean for...?" / "where do we go from here?" pattern.
PERFORMATIVE_QUESTION_PATTERNS = [
    r"^\s*\??\s*but what does this mean for",
    r"are we ready for what comes next\??",
    r"where do we go from here\??",
    r"what does the future hold\??",
    r"so what do we do\??",
]


def _strip_code_fences(text: str) -> str:
    """Remove fenced code blocks so regex rules don't fire inside them."""
    return re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.DOTALL)


def lint_regex_rules(text: str) -> list[Violation]:
    """Run every REGEX_RULES entry across the text. Return violations with line/col."""
    violations: list[Violation] = []
    cleaned = _strip_code_fences(text)
    lines = cleaned.split("\n")
    for rule in REGEX_RULES:
        for line_idx, line in enumerate(lines, start=1):
            for m in re.finditer(rule["pattern"], line, rule["flags"]):
                violations.append(
                    Violation(
                        rule_id=rule["id"],
                        rule_name=rule["name"],
                        line=line_idx,
                        column=m.start() + 1,
                        matched_text=m.group(0).strip(),
                        fix_hint=rule["fix"],
                    )
                )
    return violations


def lint_performative_questions(text: str) -> list[Violation]:
    violations: list[Violation] = []
    cleaned = _strip_code_fences(text)
    lines = cleaned.split("\n")
    for line_idx, line in enumerate(lines, start=1):
        for pattern in PERFORMATIVE_QUESTION_PATTERNS:
            m = re.search(pattern, line, re.IGNORECASE)
            if m:
                violations.append(
                    Violation(
                        rule_id="F07",
                        rule_name="Performative rhetorical question",
                        line=line_idx,
                        column=m.start() + 1,
                        matched_text=m.group(0).strip(),
                        fix_hint="Replace with a specific question (what should X do, given Y?) or cut.",
                    )
                )
    return violations


def lint_uniform_paragraph_length(text: str) -> list[Violation]:
    """Flag drafts where every paragraph is roughly the same length.

    Heuristic: if the standard deviation of paragraph word counts is less than
    20% of the mean AND there are 4+ paragraphs, the rhythm is too uniform.
    Skips code blocks and short paragraphs (<10 words) which legitimately
    serve as punch lines.
    """
    cleaned = _strip_code_fences(text)
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", cleaned) if p.strip()]
    word_counts = [len(p.split()) for p in paragraphs if len(p.split()) >= 10]
    if len(word_counts) < 4:
        return []

    mean = sum(word_counts) / len(word_counts)
    variance = sum((w - mean) ** 2 for w in word_counts) / len(word_counts)
    stdev = variance**0.5

    if mean > 0 and (stdev / mean) < 0.2:
        return [
            Violation(
                rule_id="F09",
                rule_name="Uniform paragraph length",
                line=1,
                column=1,
                matched_text=f"{len(word_counts)} paragraphs at mean={mean:.0f} words, stdev={stdev:.0f}",
                fix_hint="Break the rhythm. Drop in a one-sentence paragraph or a punch line. Vary length deliberately.",
            )
        ]
    return []


def lint_multi_phrase_bolding(text: str) -> list[Violation]:
    """Flag paragraphs with 2+ bolded phrases."""
    cleaned = _strip_code_fences(text)
    paragraphs = re.split(r"\n\s*\n", cleaned)
    violations: list[Violation] = []
    line_offset = 1
    for para in paragraphs:
        bold_count = len(re.findall(r"\*\*[^*\n]+?\*\*", para))
        if bold_count >= 2:
            violations.append(
                Violation(
                    rule_id="F14",
                    rule_name="Multi-phrase bolding",
                    line=line_offset,
                    column=1,
                    matched_text=f"{bold_count} bolded phrases in one paragraph",
                    fix_hint="Bold one phrase per paragraph or none. Multi-bolding flattens emphasis to noise.",
                )
            )
        line_offset += para.count("\n") + 2
    return violations


def lint_symmetrical_triples(text: str) -> list[Violation]:
    """Heuristic: three adjectives in 'X, Y, and Z' rhythm, all single words ending similarly."""
    cleaned = _strip_code_fences(text)
    pattern = r"\b(\w+ing|\w+able|\w+ive|\w+ful)\s*,\s*(\w+ing|\w+able|\w+ive|\w+ful)\s*,?\s+and\s+(\w+ing|\w+able|\w+ive|\w+ful)\b"
    violations: list[Violation] = []
    for line_idx, line in enumerate(cleaned.split("\n"), start=1):
        for m in re.finditer(pattern, line, re.IGNORECASE):
            violations.append(
                Violation(
                    rule_id="F03",
                    rule_name="Symmetrical triple",
                    line=line_idx,
                    column=m.start() + 1,
                    matched_text=m.group(0),
                    fix_hint="Pick the strongest adjective and cut the other two. Triples sound like content; they aren't.",
                )
            )
    return violations


def run_all(text: str) -> list[Violation]:
    """Run every check; return all violations in source order."""
    out: list[Violation] = []
    out.extend(lint_regex_rules(text))
    out.extend(lint_performative_questions(text))
    out.extend(lint_symmetrical_triples(text))
    out.extend(lint_multi_phrase_bolding(text))
    out.extend(lint_uniform_paragraph_length(text))
    out.sort(key=lambda v: (v.line, v.column))
    return out


def format_human(violations: list[Violation], source_label: str) -> str:
    if not violations:
        return f"{source_label}: clean. No Fatal Fifteen violations detected.\n"
    lines = [f"{source_label}: {len(violations)} violation(s) found.\n"]
    for v in violations:
        lines.append(f"  [{v.rule_id}] {v.rule_name}")
        lines.append(f"    line {v.line}, col {v.column}: {v.matched_text!r}")
        lines.append(f"    fix: {v.fix_hint}")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Path to draft markdown, or '-' for stdin")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of human-readable")
    args = parser.parse_args()

    if args.path == "-":
        text = sys.stdin.read()
        source = "<stdin>"
    else:
        p = Path(args.path)
        if not p.exists():
            print(f"error: file not found: {p}", file=sys.stderr)
            return 2
        text = p.read_text()
        source = str(p)

    violations = run_all(text)

    if args.json:
        print(json.dumps([asdict(v) for v in violations], indent=2))
    else:
        print(format_human(violations, source))

    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
