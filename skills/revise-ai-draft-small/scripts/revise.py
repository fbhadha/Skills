#!/usr/bin/env python3
"""
revise.py - apply the revise-ai-draft-small rules to a draft with a local
Ollama model.

Step mode (default) gives the model one small task per call:
  1. Code deletes sentences that match the DELETE table, headings in short
     nonfiction, "The End", and bold marks, and replaces dashes and fixed
     AI words.
  2. The model rewrites each flagged sentence on its own: figures of speech,
     "isn't X, it's Y", abstract triads, body-sensation emotion, AI words,
     repetition, weak verb plus noun, passive voice, sentences over 35 words.
     Bracketed notes such as [Graphic: ...] are never changed. A second pass retries any sentence
     still flagged.
  3. The model answers YES or NO for candidate sentences: lesson or moral, and
     in fiction, only smell, weather, light, or view. YES sentences go.
  4. The model picks the sentence each fact belongs after; code inserts it.
  5. Code joins one-line paragraphs; lint_output.py checks the result.

--single sends the whole draft with SKILL.md in one call. Use it for 14B and
larger only. In testing, Qwen2.5-3B copied the draft almost unchanged in that mode.

Usage:
  python3 revise.py draft.txt [facts.txt] [--model qwen2.5:14b]
                    [--genre auto|fiction|nonfiction] [--single] [--out revised.txt]
Needs Ollama on localhost:11434. Standard library only.
"""
import argparse
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL = (HERE.parent / "SKILL.md").read_text().split("---", 2)[2].strip()
MODEL = "qwen2.5:14b"
I = re.IGNORECASE

REWRITE_SPEC = """TASK: Rewrite one sentence so it reads as written by a person. Output only the rewritten sentence.

## RULES
- Replace a comparison ("like a", "as if", "as though") with the plain literal statement.
- Replace "isn't X, it's Y", "not only X but Y", or "less X than Y" with a plain statement of Y.
- Replace a list of three abstract words with the one most precise word.
- Replace a body sensation used for an emotion (chest tightened, throat closed, heart pounded) with the plain emotion word.
- Say a repeated word or phrase once.
- Replace a weak verb plus a noun made from a verb with the plain verb: "achieved an optimization of" becomes "optimized".
- Put the actor first, in active voice: "It was observed by management that" becomes "Management saw that".
- Replace crucial, vital, pivotal with important; robust with strong; enhance with improve; showcase, underscore, highlight with show; foster with build; empower with help; unlock with get; embark on with start; realm with area. Delete seamless.
- Split a sentence longer than 35 words into two or three sentences.
- Keep every name, number, and fact.
- Use a comma, a period, or parentheses in place of a dash.

## EXAMPLES
INPUT: The issue isn't the budget, it's the timeline.
OUTPUT: The issue is the timeline.
INPUT: Waiters shot through the room like comets, and her chest tightened.
OUTPUT: Waiters moved fast through the room, and she was afraid.
INPUT: The new process gives the team clarity, alignment, and momentum.
OUTPUT: The new process gives the team clarity.

## CHECK
- [ ] Output is the rewritten sentence and nothing else.
- [ ] No comparison, no dash, no word from the replace list."""

LESSON_SPEC = """TASK: Answer YES or NO. YES: the sentence states a moral, a lesson, or a general truth about life or people. NO: the sentence states a specific fact, event, action, feeling, or instruction.

## EXAMPLES
SENTENCE: Power, he realized, was never owned, only rented.
ANSWER: YES
SENTENCE: Some fires you have to jump yourself.
ANSWER: YES
SENTENCE: In the end, trust is what holds a team together.
ANSWER: YES
SENTENCE: He wrote two words in the notebook.
ANSWER: NO
SENTENCE: Block two hours on your calendar in the first week of each month.
ANSWER: NO
SENTENCE: She was afraid when the call came.
ANSWER: NO

## CHECK
- [ ] Output is YES or NO."""

SETTING_SPEC = """TASK: Answer YES or NO. YES: the sentence only describes a smell, the weather, the light, the sky, or a view, and no person acts, speaks, or thinks in it. NO: a person acts, speaks, or thinks in the sentence, or it states a plot fact.

## EXAMPLES
SENTENCE: The air smelled of jasmine and wet stone.
ANSWER: YES
SENTENCE: Below the hills, the city glittered under a gold sky.
ANSWER: YES
SENTENCE: He looked at the city and thought about what the film would cost.
ANSWER: NO
SENTENCE: The rain had flooded the road, so they turned back.
ANSWER: NO

## CHECK
- [ ] Output is YES or NO."""

FACT_SPEC = """TASK: Answer with one number: the numbered sentence that is about the same subject as FACT.

## EXAMPLE
SENTENCES:
1. Ship the laptop before the start date.
2. Book the first week before the person arrives.
FACT: Hires whose laptop arrived on day one finished training four days sooner.
ANSWER: 1

## CHECK
- [ ] Output is one number."""

DELETE = re.compile("|".join([
    r"\b(in this (post|article|guide|piece)|we'll (cover|explore|look at|walk)|let's (dive|explore|break|take a look)|here's what you need to know|this guide (will|walks))\b",
    r"\b(in today's|now more than ever|in an era of|in the modern world)\b",
    r"^(this (shows|highlights|underscores|demonstrates) (that|how)|in other words|that's the power of)\b",
    r"\b(it was a reminder that|the (real )?lesson (is|was|here)|in the end, it was never about)\b",
    r"\b(fall behind|can't afford to ignore|(get|be) left behind)\b",
    r"\b(studies (show|suggest|have shown)|experts (agree|say|believe)|research (shows|suggests)|according to (experts|research|studies))\b",
    r"^(in conclusion|in short,|to sum up|ultimately,|the bottom line|the future (is|looks) bright)",
    r"^ready to .*\?$",
    r"^start today\b",
]), I)
OLDNEW = re.compile(r"\b(gone are the days|built for a slower era|next[- ]generation|traditional \w+ (no longer|can't|won't))\b|^(back then|nowadays|these days)\b", I)
KEEP_NEXT = re.compile(r"https?://|www\.|\S+@\S+\.\w+|\b(contact|sign up|subscribe|email us|call us|register)\b", I)
SPECIFIC = re.compile(r"\d|\"|(?<=\s)[A-Z][a-z]+")
FLAGS = re.compile("|".join([
    r"\b(it's not|isn't|wasn't|aren't)\b[^.;]{1,50}[,;]\s*(it's|it was|they're|that's)\b",
    r"\bnot (only|just|merely) [^.]{1,60}\bbut\b",
    r"\bless (a|an) \w+[^.]{0,30} than (a|an)\b",
    r"\b(as if|as though|like (a|an) \w+)",
    r"\b\w+(ity|ness|ion|ence|ance|ment|ship), \w+,? (and|or) \w+",
    r"\b(chest (tightened|ached|constricted)|throat (closed|tightened)|stomach (dropped|knotted|twisted)|heart (pounded|hammered|raced)|breath (caught|hitched))\b",
    r"\b(crucial|pivotal|vital|robust|seamless|enhanc\w+|showcas\w+|underscor\w+|highlight(s|ed|ing)?|testament|tapestry|empower\w*|unlock\w*|embark\w*|realm|foster\w*)\b",
    r"\b(make|makes|made|achieve[sd]?|conduct(s|ed)?|perform(s|ed)?|carr(y|ies|ied) out) (a|an|the) \w+(tion|sion|ment|ance|ence|sis)\b",
    r"\b(is|are|was|were|been) \w+(ed|en) by\b",
    r"\b(?P<rep>\w{4,})\b(?:\W+\w+){0,3}?\W+(?P=rep)\b(?:\W+\w+){0,3}?\W+(?P=rep)\b",
]), I)
SETTING_WORDS = re.compile(r"\b(smell\w*|scent|odou?r|air|rain|wind|snow|fog|mist|lights?|sky|sun|moon|stars?|city|hills?|dark|darkness|shadows?|weather|sea|ocean)\b", I)
QUOTE = re.compile(r"\"")
ABBR = {"mr", "mrs", "ms", "dr", "st", "jr", "sr", "vs", "etc", "e.g", "i.e", "inc", "ltd", "co", "mt", "no", "fig"}
FORMS = {"e": "use", "es": "uses", "ed": "used", "ing": "using"}
WORD_FIX = [
    (r"^(but |and |so )?here's the thing:?\s*", lambda m: ""),
    (r"^(moreover|furthermore|additionally),?\s+", lambda m: ""),
    (r"\bit's (worth noting|important to note) that\s+", lambda m: ""),
    (r"\bdelv(e|es|ed|ing) into\b", lambda m: {"e": "look", "es": "looks", "ed": "looked", "ing": "looking"}[m.group(1).lower()] + " at"),
    (r"\butiliz(e|es|ed|ing)\b", lambda m: FORMS[m.group(1).lower()]),
    (r"\bleverag(es|ed|ing)\b", lambda m: FORMS[m.group(1).lower()]),
    (r"\bto leverage\b", lambda m: "to use"),
    (r"\bseamlessly\s+", lambda m: ""),
]


def chat(system, user, max_tokens=400):
    body = json.dumps({
        "model": MODEL, "stream": False,
        "options": {"num_ctx": 8192, "temperature": 0, "num_predict": max_tokens},
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
    }).encode()
    req = urllib.request.Request("http://localhost:11434/api/chat", data=body,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=900) as r:
        return json.load(r)["message"]["content"].strip()


def norm(t):
    return t.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')


def split_sentences(par):
    parts, start = [], 0
    for m in re.finditer(r"([.!?])([\"')\]*_]*)(\s+)", par):
        if not re.match(r"[A-Z0-9\"*(_]", par[m.end():m.end() + 1]):
            continue
        prev = re.findall(r"([A-Za-z.]+)$", par[start:m.start()])
        w = prev[0].lower().strip(".") if prev else ""
        if m.group(1) == "." and (w in ABBR or len(w) == 1):
            continue
        parts.append(par[start:m.end(2)].strip())
        start = m.end()
    if par[start:].strip():
        parts.append(par[start:].strip())
    return parts


def is_dialogue(t):
    return bool(QUOTE.search(t))


def is_title(p, i):
    return i == 0 and not re.search(r"[.!?]$", p)


def is_note(p):
    return p.lstrip().startswith("[")


def is_heading(p, i):
    return not is_note(p) and (p.startswith("#") or (i > 0 and "\n" not in p and len(p.split()) <= 10
                                                    and not re.search(r"[.!?:\"']$", p)))


def cap(s):
    return s[:1].upper() + s[1:] if s else s


def fix_dashes(s):
    dash = r"\s*[\u2014\u2013]\s*|\s+--\s+"
    if len(re.findall(dash, s)) == 2:
        s = re.sub(dash, " (", s, count=1)
        s = re.sub(dash, ") ", s, count=1)
    s = re.sub(dash, ", ", s)
    s = re.sub(r"\s+([,.;:!?)])", r"\1", s)
    s = re.sub(r",\s*,", ",", s)
    return re.sub(r"\(\s+", "(", s).strip()


def fix_words(s):
    for pat, rep in WORD_FIX:
        s = re.sub(pat, rep, s, flags=I)
    return cap(s.strip())


def detect_genre(text):
    paras = re.split(r"\n\s*\n", norm(text))
    if sum(1 for p in paras if QUOTE.search(p)) >= 2 or re.search(r"\b(he|she|they) (said|asked|whispered)\b", text, I):
        return "fiction"
    return "nonfiction"


def code_pass(text, genre):
    text = norm(text)
    paras = [p.strip() for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    short = genre == "nonfiction" and len(text.split()) < 800
    out = []
    for i, p in enumerate(paras):
        p = re.sub(r"\*\*(.+?)\*\*|__(.+?)__", lambda m: m.group(1) or m.group(2), p)
        if re.fullmatch(r"\W*the end\W*", p, I):
            continue
        if is_note(p):
            out.append(p)
            continue
        if is_title(p, i):
            out.append(p)
            continue
        if is_heading(p, i):
            if not short:
                out.append(p)
            continue
        if genre == "fiction" and re.match(r"(years|months|weeks|decades) later|in the (days|weeks|months|years) that followed|long after", p, I):
            continue
        if short and re.search(r"(?m)^\s*([-*\u2022]|\d+[.)])\s+", p):
            p = re.sub(r"(?m)^\s*([-*\u2022]|\d+[.)])\s+", "", p)
            p = re.sub(r"(?m)([^.!?:\s])\s*$", r"\1.", p)
        kept, framing = [], False
        for s in split_sentences(p):
            if OLDNEW.search(s):
                framing = True
                continue
            if DELETE.search(s) and not KEEP_NEXT.search(s):
                continue
            s = fix_words(fix_dashes(s))
            if s:
                kept.append(s)
        if framing and not any(SPECIFIC.search(s) for s in kept):
            kept = []
        if kept:
            out.append(" ".join(kept))
    return "\n\n".join(out)


def clean(ans, original):
    ans = " ".join(ans.strip().split("\n\n")[0].split())
    ans = re.sub(r"^(OUTPUT|Output|Rewritten sentence)\s*:\s*", "", ans).strip()
    if ans[:1] == '"' and ans[-1:] == '"' and original[:1] != '"':
        ans = ans[1:-1].strip()
    if not ans or "INPUT" in ans or len(ans.split()) > 1.5 * len(original.split()) + 10:
        return original
    return fix_dashes(norm(ans))


def rewrite_pass(text):
    out = []
    for i, p in enumerate(text.split("\n\n")):
        if is_title(p, i) or is_heading(p, i) or is_note(p):
            out.append(p)
            continue
        sents = []
        for s in split_sentences(p):
            if (FLAGS.search(s) or len(s.split()) > 35) and not is_dialogue(s) and "[" not in s:
                s = clean(chat(REWRITE_SPEC, s, 2 * len(s.split()) + 40), s)
            sents.append(s)
        out.append(" ".join(sents))
    return "\n\n".join(out)


def yes(spec, s):
    return chat(spec, f"SENTENCE: {s}\nANSWER:", 3).strip().upper().startswith("YES")


def drop_pass(text, spec, pick):
    paras = text.split("\n\n")
    out = []
    for i, p in enumerate(paras):
        if is_title(p, i) or is_heading(p, i) or is_dialogue(p) or is_note(p):
            out.append(p)
            continue
        sents = split_sentences(p)
        keep = [s for j, s in enumerate(sents)
                if KEEP_NEXT.search(s) or not pick(i, j, len(paras), len(sents), s) or not yes(spec, s)]
        if keep:
            out.append(" ".join(keep))
    return "\n\n".join(out)


def classify_pass(text, genre):
    lesson = lambda i, j, n, m, s: (genre == "fiction" and j == m - 1) or i == n - 1 or \
        bool(re.search(r"\b(realized|understood|learned|it turns out)\b", s, I))
    text = drop_pass(text, LESSON_SPEC, lesson)
    if genre == "fiction":
        text = drop_pass(text, SETTING_SPEC, lambda i, j, n, m, s: bool(SETTING_WORDS.search(s)))
    return text


def facts_pass(text, facts):
    facts = facts.strip()
    if not facts or facts.lower() == "none":
        return text
    paras = text.split("\n\n")
    flat = [(pi, si, s) for pi, p in enumerate(paras) if not (is_title(p, pi) or is_heading(p, pi) or is_note(p))
            for si, s in enumerate(split_sentences(p))]
    if not flat:
        return text + "\n\n" + facts
    listing = "\n".join(f"{k + 1}. {s}" for k, (_, _, s) in enumerate(flat))
    m = re.search(r"\d+", chat(FACT_SPEC, f"SENTENCES:\n{listing}\nFACT: {facts}\nANSWER:", 4))
    k = min(max(int(m.group()) - 1, 0), len(flat) - 1) if m else len(flat) - 1
    pi, si, _ = flat[k]
    sents = split_sentences(paras[pi])
    sents.insert(si + 1, facts)
    paras[pi] = " ".join(sents)
    return "\n\n".join(paras)


def finalize(text):
    out = []
    for i, p in enumerate(q for q in text.split("\n\n") if q.strip()):
        p = re.sub(r"[ \t]+", " ", p).strip()
        short = len(split_sentences(p)) == 1 and len(p.split()) <= 6
        prev_ok = out and not is_dialogue(out[-1]) and not (len(out) == 1 and is_title(out[0], 0))
        if short and i > 0 and not is_dialogue(p) and not is_heading(p, i) and not is_note(p) and prev_ok and not is_note(out[-1]):
            out[-1] = out[-1] + " " + p
        else:
            out.append(p)
    return "\n\n".join(out).strip() + "\n"


def revise(draft, facts="none", genre="auto"):
    genre = detect_genre(draft) if genre == "auto" else genre
    text = rewrite_pass(rewrite_pass(code_pass(draft, genre)))
    return finalize(facts_pass(classify_pass(text, genre), facts))


def main():
    global MODEL
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("facts", nargs="?")
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--genre", default="auto", choices=["auto", "fiction", "nonfiction"])
    ap.add_argument("--single", action="store_true")
    ap.add_argument("--out", default="revised.txt")
    a = ap.parse_args()
    MODEL = a.model
    draft = Path(a.draft).read_text()
    facts = Path(a.facts).read_text() if a.facts else "none"
    if a.single:
        text = chat(SKILL, f"draft:\n{draft.strip()}\nfacts:\n{facts.strip()}\n", 4096)
    else:
        text = revise(draft, facts, a.genre)
    Path(a.out).write_text(text.strip() + "\n")
    r = subprocess.run([sys.executable, str(HERE / "lint_output.py"), a.out, a.draft],
                       capture_output=True, text=True)
    print(r.stdout)
    print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
