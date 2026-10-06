#!/usr/bin/env python3
"""
lint_output.py - deterministic check of a revised text against the
revise-ai-draft-small rules. Small models do not reliably check their own
output, so run this after the model and re-run the model (or flag for a
human) on any FAIL. scripts/revise.py does this automatically.

Usage:
    python3 lint_output.py revised.txt [draft.txt]

Exit code 0 when there are no hard hits, 1 otherwise. Prints every hit.
Surface patterns only: it cannot judge whether a sentence states a moral
or whether a fact was invented. WARN lines are possible hits to check by eye.
"""
import re
import sys
from pathlib import Path

HARD = {
    "dash": r"[\u2014\u2013]",
    "preview": r"\b(in this (post|article|guide|piece)|we'll (cover|explore|look at|walk)|let's (dive|explore|break|take a look|look)|here's what you need to know|this guide (will|walks))\b",
    "world-opener": r"\b(in today's (fast[- ]paced|digital|ever[- ]changing|rapidly)|now more than ever|in an era of|in the modern world)\b",
    "old-vs-new": r"\b(gone are the days|built for a slower era|next[- ]generation|traditional \w+ (no longer|can't|won't))\b",
    "restatement": r"\b(this (shows|highlights|underscores|demonstrates) (that|how)|in other words|that's the power of)\b",
    "lesson": r"\b(it was a reminder that|the (real )?lesson (is|was|here)|in the end, it was never about)\b",
    "loss-threat": r"\b(fall behind|can't afford to ignore|(get|be) left behind)\b",
    "unnamed-source": r"\b(studies (show|suggest|have shown)|experts (agree|say|believe)|research (shows|suggests)|according to (experts|research|studies))\b",
    "recap-close": r"\b(in conclusion|in short,|to sum up|the bottom line( is|:)|the future (is|looks) bright)|\bready to \w+[^.?!]{0,60}\?|(^|[.!?]\s+)start today\b",
    "not-x-but-y": r"\b(it's not|isn't|wasn't|aren't)\b[^.;\u2014]{1,50}[,;\u2014]\s*(it's|it was|they're|that's)\b|\bnot (only|just|merely) [^.]{1,60}\bbut\b|\bless (a|an) \w+[^.]{0,30} than (a|an)\b",
    "as-if": r"\b(as if|as though)\b",
    "ai-words": r"\b(delve\w*|leverag\w+|utiliz\w+|crucial|pivotal|robust|seamless\w*|showcas\w+|underscor\w+|testament|tapestry|empower\w*|embark\w*|realm|moreover|furthermore)\b",
    "worth-noting": r"\bit's (worth|important to) not(e|ing)\b",
    "bold": r"\*\*[^*]+\*\*",
    "the-end": r"^\W*the end\W*$",
}
WARN = {
    "simile": r"\blike (a|an) \w+",
    "literal-or-not": r"\b(landscape|navigat\w+|foster\w*|unlock\w*|journey)\b",
    "body-emotion": r"\b(chest (tightened|ached|constricted)|throat (closed|tightened)|stomach (dropped|knotted|twisted)|heart (pounded|hammered|raced)|breath (caught|hitched))\b",
    "smell": r"\b(smell(ed|s)? (of|like)|scent of|the air (smelled|tasted|was thick))\b",
    "lesson-maybe": r"\b(realized that|understood that|it turns out)\b",
    "weak-verb-noun": r"\b(make|makes|made|achieve[sd]?|conduct(s|ed)?|perform(s|ed)?|carr(y|ies|ied) out) (a|an|the) \w+(tion|sion|ment|ance|ence|sis)\b",
    "passive-by": r"\b(is|are|was|were|been) \w+(ed|en) by\b",
}
QUOTES = "\"\u201c\u201d"


def norm(text):
    return text.replace("\u2019", "'").replace("\u2018", "'")


ABBR = {"mr", "mrs", "ms", "dr", "st", "jr", "sr", "vs", "etc", "e.g", "i.e", "inc", "ltd", "co", "mt", "no", "fig"}


def sentences(text):
    parts, start = [], 0
    for m in re.finditer(r"([.!?])([\"')\]*_\u201d]*)(\s+)", text):
        if not re.match(r"[A-Z0-9\"*(_\u201c]", text[m.end():m.end() + 1]):
            continue
        prev = re.findall(r"([A-Za-z.]+)$", text[start:m.start()])
        word = prev[0].lower().strip(".") if prev else ""
        if m.group(1) == "." and (word in ABBR or len(word) == 1):
            continue
        parts.append(text[start:m.end(2)].strip())
        start = m.end()
    parts.append(text[start:].strip())
    return [p for p in parts if p]


def scan(lines, patterns, label):
    n = 0
    for name, pat in patterns.items():
        for i, line in enumerate(lines, 1):
            for m in re.finditer(pat, line, re.IGNORECASE):
                n += 1
                print(f"{label} {name:14s} line {i}: ...{line[max(0, m.start() - 30):m.end() + 30]}...")
    return n


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    out = norm(Path(sys.argv[1]).read_text())
    lines = out.splitlines()
    hits = scan(lines, HARD, "FAIL")
    scan(lines, WARN, "WARN")
    paras = [p.strip() for p in re.split(r"\n\s*\n", out) if p.strip()]
    for k, p in enumerate(paras):
        is_title = k == 0 and not p.endswith((".", "!", "?"))
        if is_title or p.startswith("#") or p.startswith("[") or any(q in p for q in QUOTES):
            continue
        if len(sentences(p)) == 1 and len(p.split()) <= 6:
            hits += 1
            print(f"FAIL one-line-para    : {p}")
    for s in (x for q in paras for x in sentences(q)):
        if len(s.split()) > 35:
            hits += 1
            print(f"FAIL long-sentence    : {len(s.split())} words: {s[:70]}...")
    if len(sys.argv) > 2:
        src = norm(Path(sys.argv[2]).read_text())
        ratio = len(out.split()) / max(1, len(src.split()))
        print(f"INFO length ratio     : {ratio:.2f} (output words / draft words)")
        if ratio >= 1.0:
            hits += 1
            print("FAIL not-shorter      : output is not shorter than draft")
        nums = lambda t: set(re.findall(r"\d[\d,.]*%?", t))
        new = nums(out) - nums(src)
        if new:
            print(f"WARN new-numbers      : {sorted(new)} not in draft; confirm they come from facts")
    print(f"\n{'PASS' if hits == 0 else 'FAIL'}: {hits} hard hit(s)")
    sys.exit(0 if hits == 0 else 1)


if __name__ == "__main__":
    main()
