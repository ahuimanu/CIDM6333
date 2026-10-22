#!/usr/bin/env python3
"""Apply West Texas A&M brand standards (WT Brand Quick Guide v2.2, Sep 2026) to the site.

Swaps the design tokens and font stacks wherever they appear: tools/sitekit/common.css and
page-head.html (sources), and every built page under docs/ (pages carry inline copies of the
token block). Idempotent: each mapping goes from an old value to a brand value that is not
itself a key.

Light mode: WTAMU Maroon #450012 for headings, accents, rules and the primary chart series;
white page; Caliche Dust #fff4e2 panels; Thunderstorm #545859 secondary text; Panhandle Sky
#7ca6d8 as the second series and the model panel. Dark mode keeps the same roles with
lighter tints so text and marks stay readable on a dark ground.
Fonts: Avenir Next / Helvetica Neue (brand); JetBrains Mono kept for code (the brand has no mono).

Usage: python3 brand.py <docs-dir>
"""
import re, sys, pathlib
HERE = pathlib.Path(__file__).parent

# token-scoped first (old value shared by two tokens), then plain value swaps
SCOPED = [
    ("--s-b:#B45C0C", "--s-b:#7CA6D8"),  # light second series
    ("--s-b:#D47A22", "--s-b:#9DBDE4"),  # dark second series
]
VALUES = {
    # light
    "#F2F4F6": "#FFFFFF",  # --bg: white (brand primary)
    "#E7ECF0": "#FFF4E2",  # --surface-2: Caliche Dust
    "#15212B": "#1C1C1C",  # --ink: near-black
    "#4F606D": "#545859",  # --ink-2: Thunderstorm
    "#B6C2CC": "#D6D1C8",  # --line
    "#E4EEF4": "#EEF3FA",  # --model: Panhandle Sky tint
    "#7FA7BD": "#7CA6D8",  # --model-line: Panhandle Sky
    "#B45C0C": "#450012",  # --accent: WTAMU Maroon
    "#F7E4D0": "#FFF4E2",  # --accent-soft: Caliche Dust
    "#8A4406": "#450012",  # --accent-ink: Maroon
    "#2A76AE": "#450012",  # --s-a: Maroon (primary series)
    # dark
    "#0E151B": "#170F11", "#16212A": "#21171A", "#1F2C37": "#2D2124",
    "#E2E8ED": "#F4EEE6", "#9AAAB6": "#BDB8B0", "#3B4B58": "#4C3E42",
    "#12232E": "#1A2330", "#43758E": "#7CA6D8",
    "#F0A04B": "#E89AAE",  # dark accent: maroon tint
    "#3A2916": "#3D1220",  # dark accent-soft: deep maroon
    "#F6B874": "#F2B8C6",  # dark accent-ink
    "#3F9AD6": "#E89AAE",  # dark --s-a: maroon tint
}
SANS = '"Avenir Next","Helvetica Neue",Helvetica,Arial,sans-serif'
FONTS = [
    ('"Barlow Condensed","Arial Narrow",Arial,sans-serif', SANS),  # original display stack -> replaced below by DISPLAY_NEW
    ('"Source Serif 4",Georgia,"Times New Roman",serif', SANS),
    ("'Source Serif 4'", '"Avenir Next"'), ('"Source Serif 4"', '"Avenir Next"'),
]
GFONT = re.compile(r"https://fonts\.googleapis\.com/css2\?family=[^\"']*")
GFONT_NEW = "https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"
# Display type (headings, labels, and all SVG figure text) stays condensed: the figures' fixed-width
# labels were laid out for a condensed face, and a regular-width face spills out of their boxes.
# Barlow Condensed comes first because the figure geometry was measured in it; Avenir Next Condensed
# (the brand family's condensed cut) is the fallback. Body text is Avenir Next.
DISPLAY_OLD = '--display:"Avenir Next","Helvetica Neue",Helvetica,Arial,sans-serif'
DISPLAY_MID = '--display:"Avenir Next Condensed","Barlow Condensed","Arial Narrow",sans-serif'
DISPLAY_NEW = '--display:"Barlow Condensed","Avenir Next Condensed","Arial Narrow",sans-serif'

def brand(s):
    for a, b in SCOPED: s = s.replace(a, b)
    for a, b in VALUES.items():
        s = re.sub(re.escape(a), b, s, flags=re.I)
    for a, b in FONTS: s = s.replace(a, b)
    s = GFONT.sub(GFONT_NEW, s)
    s = s.replace(DISPLAY_OLD, DISPLAY_NEW).replace(DISPLAY_MID, DISPLAY_NEW)
    return s

def main(docs):
    files = [HERE / "common.css", HERE / "page-head.html", HERE / "article.css"]
    files += [p for p in pathlib.Path(docs).rglob("*") if p.suffix in (".html", ".css")]
    n = 0
    for p in files:
        if not p.exists(): continue
        s = p.read_text(encoding="utf-8"); t = brand(s)
        if t != s: p.write_text(t, encoding="utf-8"); n += 1
    print("brand applied to", n, "files")

if __name__ == "__main__":
    main(sys.argv[1])
