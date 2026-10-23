#!/usr/bin/env python3
"""Build docs/textbook/ from the Course Topic Guide (Answerable Systems outline).

Usage: python3 textbook.py <docs-dir>
Front matter -> textbook/index.html; each "# N. Title" chapter and each "# Appendix X" -> its own page.
Appendix H (run sheet: dates, schedule) is deliberately not published.
"""
import re, sys, os, html, markdown, pathlib

HERE = pathlib.Path(__file__).parent
HEAD = (HERE / "page-head.html").read_text(encoding="utf-8")
SRC = (HERE / "topic-guide.md").read_text(encoding="utf-8")

# chapter -> evolutions (from the chapter-to-evolution map in the guide)
EVO_MAP = {
 "E0": ([1,2,3], None, [22,23,24]), "E1": ([5], 10, [25]), "E2": ([6,8], 11, [25]), "E3": ([6], 12, [23]),
 "E4": ([7], 13, []), "E5": ([8,9], 14, []), "E6": ([8], 15, [25]), "E7": ([6], 16, [26]), "E8": ([4,6], 17, [25]),
 "E9": ([9], 18, []), "E10": ([7], 19, [23]), "E11": ([9], 20, []), "E12": ([9], 21, [25]), "Finals": ([], None, [26]),
}
LECTURE_SLUG = {"E0":"e0-index-zero","E1":"e1-agent-loop","E2":"e2-patterns-frameworks","E3":"e3-tools-as-contracts",
 "E4":"e4-mcp-1","E5":"e5-mcp-2-security-harness","E6":"e6-context-engineering","E7":"e7-memory","E8":"e8-multi-agent-1",
 "E9":"e9-multi-agent-2","E10":"e10-evals-as-gates","E11":"e11-observability-red-team","E12":"e12-deployment"}

def chapters_for_evo(evo):
    s, b, m = EVO_MAP[evo]
    out = [(c, "survey") for c in s]
    if b: out.append((b, "build"))
    out += [(c, "method") for c in m]
    return out

def evos_for_chapter(n):
    out = []
    for evo, (s, b, m) in EVO_MAP.items():
        role = "survey" if n in s else ("build" if n == b else ("method" if n in m else None))
        if role: out.append((evo, role))
    return out

def split_top(src):
    """Split on top-level '# ' headings, ignoring fenced code blocks."""
    parts, cur, title, fence = [], [], None, False
    for line in src.split("\n"):
        if line.startswith("```"): fence = not fence
        if not fence and line.startswith("# "):
            if title is not None or cur: parts.append((title, "\n".join(cur)))
            title, cur = line[2:].strip(), []
        else:
            cur.append(line)
    parts.append((title, "\n".join(cur)))
    return parts

def slug(t):
    t = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    return t[:60].rstrip("-")

def clean(md):
    md = md.replace("4:00–6:30 p.m., ", "")
    md = re.sub(r"The course runs thirteen Thursdays[^\n]*\n", "The course runs one Evolution at a time. Each Evolution carries two threads:\n", md)
    md = re.sub(r"The weekly rhythm[^\n]*\n", "", md)
    md = md.replace("The week-by-week run sheet maps every CIDM 6333 Evolution to its chapters.", "The chapter-to-Evolution map on this page pairs every Evolution with its chapters.")
    md = re.sub(r"\n## Using this book with CIDM 6333\n", "\n## The Evolutions\n", md)
    md = re.sub(r"\[(week-by-week run sheet|run sheet|method)\]", r"\1", md)
    md = re.sub(r"\n---\s*$", "", md.strip()) + "\n"
    return md

def render(md):
    h = markdown.markdown(md, extensions=["tables", "fenced_code"])
    return h.replace("<table>", '<div class="tw"><table>').replace("</table>", "</table></div>")

def page(title, eyebrow, body, crumbs, depth, footer="CIDM 6333 · Answerable Systems"):
    head = HEAD.replace("{{TITLE}}", html.escape(title))
    return (head + '\n<div class="wrap"><nav class="crumbs">' + crumbs + '</nav><div class="eyebrow">' + eyebrow +
            '</div><article>' + body + '</article><footer>' + footer + '</footer></div>\n</body></html>\n')

def main(docs):
    out = pathlib.Path(docs) / "textbook"
    out.mkdir(parents=True, exist_ok=True)
    parts = split_top(SRC)
    front, chapters, appendices = [], [], []
    for title, body in parts:
        if title is None: continue
        if re.match(r"\d+\. ", title): chapters.append((title, body))
        elif title.startswith("Appendix"):
            if title.startswith("Appendix H"): continue
            appendices.append((title, body))
        elif title.startswith("CIDM 6333: Course Topic Guide") or title.startswith("CIDM 6333 — Course Topic Guide"): continue
        else: front.append((title, body))
    pages = []  # (dir, title, kind)
    for title, body in chapters:
        n = int(title.split(".")[0]); d = "ch-%02d-%s" % (n, slug(title.split(". ",1)[1]))
        pages.append((d, title, "chapter", n, body))
    for title, body in appendices:
        sep = ":" if ": " in title else "—"
        letter = title.split(sep)[0].strip().split()[-1]
        d = "appendix-%s-%s" % (letter.lower(), slug(title.split(sep,1)[1] if sep in title else title))
        pages.append((d, title, "appendix", letter, body))
    # chapter pages
    for i, (d, title, kind, key, body) in enumerate(pages):
        prev = pages[i-1] if i > 0 else None; nxt = pages[i+1] if i+1 < len(pages) else None
        extra = ""
        if kind == "chapter":
            ev = evos_for_chapter(key)
            if ev:
                links = " · ".join('<a href="../../lectures/%s/">%s</a> <span class="small">(%s)</span>' % (LECTURE_SLUG[e], e, r) if e in LECTURE_SLUG else "%s (%s)" % (e, r) for e, r in ev)
                extra = '<p class="small"><strong>Lectures that use this chapter:</strong> ' + links + '</p>'
        if kind == "chapter":
            extra += '<p class="small"><strong>Readings:</strong> <a href="../readings/#chapter-%d">this chapter\'s entries in the reading list</a></p>' % key
        body_html = "<h1>" + html.escape(title) + "</h1>" + extra + render(clean(body))
        nav = '<hr><p>' + ('<a href="../%s/">◀ %s</a>' % (prev[0], html.escape(prev[1])) if prev else "") + (" &nbsp;·&nbsp; " if prev and nxt else "") + ('<a href="../%s/">%s ▶</a>' % (nxt[0], html.escape(nxt[1])) if nxt else "") + '</p>'
        short = ("Chapter %d" % key) if kind == "chapter" else title.split(":" if ": " in title else "—")[0].strip()
        crumbs = '<a href="../../">CIDM 6333</a> · <a href="../">Textbook</a> · ' + html.escape(short)
        (out / d).mkdir(exist_ok=True)
        (out / d / "index.html").write_text(page(title, "Answerable Systems · " + ("Chapter" if kind=="chapter" else "Appendix"), body_html + nav, crumbs, 2), encoding="utf-8")
    # index page
    fm = "".join(("<h2>%s</h2>" % html.escape(t)) + render(clean(b)) for t, b in front if not t.startswith("Answerable"))
    title_body = [b for t, b in front if t.startswith("Answerable")]
    intro = render(clean(title_body[0])) if title_body else ""
    intro = re.sub(r"<h2>The Design, Lineage, and Governance of Agentic Software</h2>\s*<p><strong>Jeffry Babb, PhD</strong>.*?</p>\s*<p><em>Working draft.*?</em></p>", "", intro, flags=re.S)
    toc = ['<h2 id="contents">Contents</h2><p class="small">Each chapter is published here as an outline. The outline carries the learning outcomes, the section plan, the systems analyzed, the gzkit episode, the readings, and the exercises. The full prose will follow in a later edition.</p>']
    def group(name, lo, hi):
        items = [p for p in pages if p[2]=="chapter" and lo <= p[3] <= hi]
        return '<h3>%s</h3><ol start="%d">' % (name, lo) + "".join('<li><a href="%s/">%s</a></li>' % (d, html.escape(t.split(". ",1)[1])) for d,t,k,key,b in items) + "</ol>"
    toc.append(group("Part I · The posture", 1, 3)); toc.append(group("Part II · The survey", 4, 9))
    toc.append(group("Part III · The build", 10, 21)); toc.append(group("Part IV · The method", 22, 26))
    toc.append('<h3>Reading list</h3><p><a href="readings/">Every reading the chapters cite, with links.</a></p>')
    toc.append('<h3>Appendices</h3><ul>' + "".join('<li><a href="%s/">%s</a></li>' % (d, html.escape(t)) for d,t,k,key,b in pages if k=="appendix") + '</ul>')
    body = '<h1>Answerable Systems</h1><p class="lede"><em>The Design, Lineage, and Governance of Agentic Software</em> · Jeffry Babb, PhD · Working draft</p>' + intro + "".join(toc) + fm
    (out / "index.html").write_text(page("Answerable Systems · textbook", "CIDM 6333 · Textbook", body, '<a href="../">CIDM 6333</a> · Textbook', 1), encoding="utf-8")
    # readings page (verified links), linked from the index and from every chapter
    rd = (HERE / "readings.md").read_text(encoding="utf-8")
    rbody = re.sub(r"<h2>Chapter (\d+)", r'<h2 id="chapter-\1">Chapter \1', render(rd))
    (out / "readings").mkdir(exist_ok=True)
    (out / "readings" / "index.html").write_text(page("Reading list · Answerable Systems", "Textbook · Reading list", rbody, '<a href="../../">CIDM 6333</a> · <a href="../">Textbook</a> · Reading list', 2), encoding="utf-8")
    print("textbook:", len(pages), "pages +", "index + readings")
    return {p[3]: p[0] for p in pages if p[2]=="chapter"}

def main_dirs():
    """chapter number -> directory name, computed the same way main() does."""
    out = {}
    for title, body in split_top(SRC):
        if title and re.match(r"\d+\. ", title):
            n = int(title.split(".")[0]); out[n] = "ch-%02d-%s" % (n, slug(title.split(". ",1)[1]))
    return out

if __name__ == "__main__":
    main(sys.argv[1])
