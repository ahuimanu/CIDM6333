#!/usr/bin/env python3
"""Merge the voice-pass agent outputs back into the sources:
 glossary-parts/part{1,2,3}.py -> tools/sitekit/glossary_data.py
 notes/<slug>.json             -> tools/sitekit/notes.json (per deck, length must match)
 tg/chunk{1..4}.md             -> tools/sitekit/topic-guide.md
"""
import json, pathlib, sys, ast
HERE = pathlib.Path(__file__).parent
KIT = HERE.parent.parent / "sitekit"
sys.path.insert(0, str(KIT))
import reader as RD

what = sys.argv[1:] or ["glossary", "notes", "tg"]

if "glossary" in what:
    parts = [(HERE / "glossary-parts" / f"part{i}.py").read_text(encoding="utf-8") for i in (1, 2, 3)]
    joined = "".join(parts)
    ast.parse(joined)
    orig = (HERE / "glossary-parts" / "orig.py").read_text(encoding="utf-8")
    # same number of entries, same terms in the same order
    import re
    t0 = re.findall(r'^g\("([^"]+)"', orig, re.M); t1 = re.findall(r'^g\("([^"]+)"', joined, re.M)
    assert t0 == t1, (len(t0), len(t1), [a for a, b in zip(t0, t1) if a != b][:3])
    (KIT / "glossary_data.py").write_text(joined, encoding="utf-8")
    print("glossary_data.py merged:", len(t1), "entries")

if "notes" in what:
    path = KIT / "notes.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    for slug, (pptx, evo) in RD.DECKS.items():
        p = HERE / "notes" / (slug + ".json")
        if not p.exists(): continue
        new = json.loads(p.read_text(encoding="utf-8"))
        old = data.get(pptx)
        if old is None: continue
        assert len(new) == len(old), (slug, len(new), len(old))
        changed = sum(1 for a, b in zip(old, new) if a != b)
        data[pptx] = new
        print(slug, "notes merged; slides changed:", changed, "of", len(new))
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")

if "cut" in what:
    path = KIT / "notes.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    for slug, (pptx, evo) in RD.DECKS.items():
        p = HERE / "cut" / (slug + ".json")
        if not p.exists() or pptx not in data: continue
        cut = json.loads(p.read_text(encoding="utf-8")); n = 0
        for i, txt in cut.items():
            note = data[pptx][int(i)]; j = note.find("Cut from slide")
            assert j >= 0 and txt.startswith("Cut from slide"), (slug, i)
            if note[j:] != txt: n += 1
            data[pptx][int(i)] = note[:j] + txt
        print(slug, "cut sections merged; changed:", n, "of", len(cut))
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")

if "tg" in what:
    chunks = [(HERE / "tg" / f"chunk{i}.md").read_text(encoding="utf-8") for i in (1, 2, 3, 4)]
    joined = "".join(chunks)
    import re
    orig = (KIT / "topic-guide.md").read_text(encoding="utf-8")
    h0 = [l for l in orig.split("\n") if l.startswith("# ")]; h1 = [l for l in joined.split("\n") if l.startswith("# ")]
    assert h0 == h1, [(a, b) for a, b in zip(h0, h1) if a != b][:3]
    (KIT / "topic-guide.md").write_text(joined, encoding="utf-8")
    print("topic-guide.md merged:", len(h1), "top-level sections")
