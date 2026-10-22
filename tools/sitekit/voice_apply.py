#!/usr/bin/env python3
"""Apply the voice overrides (tools/sitekit/voice/<slug>.json) outside deck.py:

1. notes.json: the "Cut from slide N (full wording):" lines mirror slide paragraphs; rewrite them where the slide
   paragraph was rewritten, so the reader's "The slide's wording in full" matches the slide.
2. Lecture pages that are not yet web-native: the transcript <li> text is the slide wording; rewrite matching items.
   (glossary.py relinks terms afterwards; nav.py and reader.py are unaffected.)

Idempotent. Usage: python3 voice_apply.py <docs-dir>
"""
import re, sys, json, html, pathlib
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
import reader as RD

def load(slug):
    p = HERE / "voice" / (slug + ".json")
    if not p.exists(): return {}
    d = json.loads(p.read_text(encoding="utf-8"))
    return {k: v for k, v in d.items() if v != k}

def notes():
    path = HERE / "notes.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    n = 0
    for slug, (pptx, evo) in RD.DECKS.items():
        ov = load(slug)
        if not ov or pptx not in data: continue
        out = []
        for note in data[pptx]:
            lines = note.split("\n")
            new = []
            for l in lines:
                m = re.match(r"^(\s*[-•]\s*)(.*)$", l)
                if m and m.group(2) in ov:
                    n += 1
                    if ov[m.group(2)] == "": continue
                    new.append(m.group(1) + ov[m.group(2)])
                elif m and " / " in m.group(2) and any(p in ov for p in m.group(2).split(" / ")):
                    parts = m.group(2).split(" / ")
                    n += sum(1 for p in parts if p in ov)
                    new.append(m.group(1) + " / ".join(ov.get(p, p) for p in parts))
                elif l in ov:
                    new.append(ov[l]); n += 1
                else:
                    new.append(l)
            out.append("\n".join(new))
        data[pptx] = out
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
    print("notes.json: cut lines rewritten:", n)

def transcripts(docs):
    for slug in RD.DECKS:
        p = pathlib.Path(docs) / "lectures" / slug / "index.html"
        if not p.exists(): continue
        s = p.read_text(encoding="utf-8")
        if '<section class="deck"' in s: continue
        ov = load(slug)
        if not ov: continue
        cnt = 0
        # values applied on an earlier run: map them to the current value so later edits propagate
        prevp = HERE / "voice" / ".applied" / (slug + ".json")
        prev = json.loads(prevp.read_text(encoding="utf-8")) if prevp.exists() else {}
        stale = {prev[k]: ov[k] for k in ov if k in prev and prev[k] != ov[k] and prev[k] != k}
        ov = dict(ov); ov.update(stale)
        def li(m):
            nonlocal cnt
            raw = m.group(1)
            parts = re.split(r"<br\s*/?>", raw)
            out, changed = [], False
            for part in parts:
                plain = html.unescape(re.sub(r"<[^>]+>", "", part))
                if plain in ov:
                    out.append(html.escape(ov[plain])); changed = True
                else:
                    out.append(part)
            if changed: cnt += 1
            return "<li>%s</li>" % "<br>".join(out)
        a = s.find('<section class="transcript"'); b = s.find("</section>", a)
        if a < 0: continue
        sec = re.sub(r"<li>(.*?)</li>", li, s[a:b], flags=re.S)
        # slide titles in the transcript h3 / aria-label / T array
        s = s[:a] + sec + s[b:]
        tcnt = 0
        for k, v in ov.items():
            if "\n" in k or len(k) > 120: continue
            ek, ev = html.escape(k, quote=False), html.escape(v, quote=False)
            if ("<h3>%s</h3>" % ek) in s:
                s = s.replace("<h3>%s</h3>" % ek, "<h3>%s</h3>" % ev)
                s = re.sub(r'(aria-label="Slide \d+: )%s"' % re.escape(html.escape(k)), lambda m: m.group(1) + html.escape(v) + '"', s)
                tcnt += 1
            for a, b in ((json.dumps(k), json.dumps(v)), (json.dumps(k, ensure_ascii=False), json.dumps(v, ensure_ascii=False))):
                if a in s: s = s.replace(a, b)
        # schedule residue in transcripts of unconverted decks
        s = re.sub(r"Break · \d:\d\d–\d:\d\d", "Break", s)
        s = re.sub(r"<li>(\s|<br>)*</li>", "", s)  # overrides set to "" drop the item
        p.write_text(s, encoding="utf-8")
        prevp.parent.mkdir(exist_ok=True)
        prevp.write_text(json.dumps(load(slug), indent=1, ensure_ascii=False), encoding="utf-8")
        print(slug, "transcript items rewritten:", cnt, "titles:", tcnt)

# Literal fixes for slide text that the per-paragraph keys do not reach (headings with inline markup,
# table cells split across tags). Applied to built lecture and figure pages; idempotent.
LITERAL = [
    ("Flight Card 11 brief — Sortie 11", "Flight Card 11 brief · Sortie 11"),
    ("Flight Card 11 brief — <a", "Flight Card 11 brief · <a"),
    ("Flight Card 12 brief — <a", "Flight Card 12 brief · <a"),
    ("Flight Card 12 brief — Sortie 12", "Flight Card 12 brief · Sortie 12"),
    ("ADR-0.0.2 — 'popularity", "ADR-0.0.2: 'popularity"),
    ("ADR-0.0.2 — &#x27;popularity", "ADR-0.0.2: &#x27;popularity"),
    ("ADR-0.0.2 — &#39;popularity", "ADR-0.0.2: &#39;popularity"),
    ("</code> — mandatory RPC", "</code>: mandatory RPC"),
    ("</code> — one long-lived", "</code>: one long-lived"),
    ("` — mandatory RPC", "`: mandatory RPC"),
    ("` — one long-lived", "`: one long-lived"),
    ("as of this week", "as of October 2026"),
    ("A PRD that names a framework", "A PRD that specifies a framework"),
    ("A structured error naming the problem", "A structured error that identifies the problem"),
    ("The 2017 paper names a constraint", "The 2017 paper states a constraint"),
    ("None (checked 1.18.32)", "None (as of 1.18.32)"),
    ("Orchestration framework choices — ADR-1", "Orchestration framework choices: ADR-1"),
]

def literal(docs):
    import glob
    for f in glob.glob(str(pathlib.Path(docs) / "lectures" / "*" / "index.html")) + glob.glob(str(pathlib.Path(docs) / "figures" / "*.html")):
        p = pathlib.Path(f); s = p.read_text(encoding="utf-8"); o = s
        for a, b in LITERAL: s = s.replace(a, b)
        if s != o: p.write_text(s, encoding="utf-8"); print("literal fixes:", p.parent.name if p.name == "index.html" else p.name)

if __name__ == "__main__":
    notes()
    transcripts(sys.argv[1])
    literal(sys.argv[1])
