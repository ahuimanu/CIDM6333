#!/usr/bin/env python3
"""Master styles and the shared navigation for every HTML page under docs/.

- docs/assets/site.css   : the common style block (tokens, type, figure player, panels, article) + nav styles
- docs/assets/nav.html   : the nav fragment, pulled in by htmx on load; hyperscript marks the current section
- every page: <link> to site.css, htmx and hyperscript scripts, a <div class="sitenav" hx-get=...> after <div class="wrap">;
  the page's own copy of the common style block is removed, page-specific styles stay inline.

Idempotent. Usage: python3 nav.py <docs-dir>
Site root is /CIDM6333/ (GitHub Pages project site); change ROOT if the site moves.
"""
import re, sys, os, pathlib

ROOT = "/CIDM6333/"
HERE = pathlib.Path(__file__).parent
COMMON = (HERE / "common.css").read_text(encoding="utf-8")
ARTICLE = (HERE / "article.css").read_text(encoding="utf-8")

NAV_CSS = """
/* ---------- site navigation (shared fragment, assets/nav.html) ---------- */
.sitenav{min-height:44px}
nav.site{display:flex;flex-wrap:wrap;align-items:center;gap:4px 18px;margin:-10px 0 18px;padding:8px 0 10px;border-bottom:1px solid var(--line);font-family:var(--display);font-weight:600;font-size:16.5px;letter-spacing:.06em;text-transform:uppercase}
nav.site a{color:var(--ink-2);text-decoration:none;padding:2px 0;border-bottom:2px solid transparent}
nav.site a:hover,nav.site a:focus-visible{color:var(--accent-ink);outline:none}
nav.site a[aria-current="page"]{color:var(--ink);border-bottom-color:var(--accent)}
nav.site .brand{color:var(--ink);font-weight:700;letter-spacing:.1em;margin-right:6px}
nav.site .brand small{display:block;font-weight:500;font-size:12px;letter-spacing:.08em;color:var(--ink-2);text-transform:none}
@media (max-width:640px){nav.site{gap:4px 12px;font-size:14px}}
"""

NAV_HTML = """<nav class="site" aria-label="Site">
<a class="brand" href="%(r)s">CIDM 6333<small>Agentic Systems Design and Development</small></a>
<a data-sec="Home" href="%(r)s">Home</a>
<a data-sec="Figures" href="%(r)s#figures">Figures</a>
<a data-sec="Lectures" href="%(r)slectures/">Lectures</a>
<a data-sec="Exercises" href="%(r)s#exercises">Exercises</a>
<a data-sec="Glossary" href="%(r)sglossary/">Glossary</a>
<a data-sec="Textbook" href="%(r)stextbook/">Textbook</a>
</nav>
""" % {"r": ROOT}

# hyperscript: after htmx swaps the fragment in, mark the link whose data-sec matches this page's section
HS = "on htmx:afterSettle for a in <a[data-sec]/> in me if a@data-sec is my @data-section then set a@aria-current to 'page' end end"

def section_of(rel):
    rel = rel.replace(os.sep, "/")
    if rel == "index.html": return "Home"
    top = rel.split("/")[0]
    return {"figures": "Figures", "lectures": "Lectures", "exercises": "Exercises",
            "glossary": "Glossary", "textbook": "Textbook"}.get(top, "")

def process(path, rel):
    s = open(path, encoding="utf-8").read()
    # strip earlier injections
    s = re.sub(r'<style id="site-nav-css">.*?</style>\n?', "", s, flags=re.S)
    s = re.sub(r'<nav class="site".*?</nav>\n?', "", s, flags=re.S)
    s = re.sub(r'<div class="sitenav".*?</div>\n?', "", s, flags=re.S)
    s = re.sub(r'<link rel="stylesheet" href="[^"]*assets/site\.css">\n?', "", s)
    s = re.sub(r'<script src="[^"]*assets/(htmx|_hyperscript)\.min\.js"></script>\n?', "", s)
    # move the common blocks out
    s = s.replace("<style>\n" + COMMON + "</style>\n", "")
    s = s.replace("<style>\n" + ARTICLE + "</style>\n", "")
    s = s.replace("<style>\n" + COMMON + "</style>", "")
    # assets after <body>
    assets = ('<link rel="stylesheet" href="%(r)sassets/site.css">\n<script src="%(r)sassets/htmx.min.js"></script>\n'
              '<script src="%(r)sassets/_hyperscript.min.js"></script>\n') % {"r": ROOT}
    m = re.search(r"<body>\s*", s)
    if not m:
        return False
    s = s[:m.end()] + assets + s[m.end():]
    # nav container after the first <div class="wrap">
    m = re.search(r'<div class="wrap">\s*', s)
    if not m:
        return False
    div = '<div class="sitenav" hx-get="%sassets/nav.html" hx-trigger="load" hx-swap="innerHTML" data-section="%s" _="%s"></div>\n' % (ROOT, section_of(rel), HS)
    s = s[:m.end()] + div + s[m.end():]
    open(path, "w", encoding="utf-8").write(s)
    return True

def main(docs):
    assets = pathlib.Path(docs) / "assets"; assets.mkdir(exist_ok=True)
    (assets / "site.css").write_text("/* CIDM 6333 course site · master styles. Built by tools/sitekit/nav.py; edit common.css / article.css there. */\n" + COMMON + ARTICLE + NAV_CSS, encoding="utf-8")
    (assets / "nav.html").write_text(NAV_HTML, encoding="utf-8")
    n = 0
    for p in sorted(pathlib.Path(docs).rglob("*.html")):
        rel = str(p.relative_to(docs))
        if rel.startswith("assets/"): continue
        if process(str(p), rel): n += 1
        else: print("skipped", rel)
    print("nav + master styles applied to", n, "pages")

if __name__ == "__main__":
    main(sys.argv[1])
