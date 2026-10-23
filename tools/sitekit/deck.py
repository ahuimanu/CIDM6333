#!/usr/bin/env python3
"""Convert a pptx lecture deck into a web-native slide page.

Each slide's text boxes, panels, tables and code blocks become HTML in a 16:9 stage; the speaker notes sit beneath
the stage and in a "Read this lecture" section; the rendered WebP of each slide stays available as "as presented".
Course-management text (timings, rooms, dates, consultation, lab logistics) is dropped by the same rules as reader.py.
Glossary terms are linked on first mention per slide.

Usage: python3 deck.py <docs-dir> <slug>      e.g. python3 deck.py docs e8-multi-agent-1
Expects the pptx under /mnt/user-data/uploads/CIDM--CIDM6333/Lecture/ (or Fall 2026/Orientation/) and notes.json beside this script.
"""
import re, sys, json, html, pathlib
from pptx import Presentation
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import reader as RD
DROP_TITLE = RD.DROP_TITLE
import glossary as GL
import textbook as TB

HERE = pathlib.Path(__file__).parent
PPTX_DIR = pathlib.Path("/mnt/user-data/uploads/CIDM--CIDM6333")
SLIDE_W, SLIDE_H = 960, 540  # px at 9525 EMU/px for a 9144000 x 5143500 deck

# per-deck: figures to attach to slides (slide number -> figure slug), and the deck's own metadata
DECK_META = {
 "orientation": {"evo": "Orientation", "title": "Course Orientation", "figs": {5: "two-loops", 9: "steer-the-middle"}},
 "e0-index-zero": {"evo": "E0", "title": "The Human Is Index Zero", "figs": {8: "steer-the-middle", 12: "two-loops"}, "cols": {17: 476, 20: 614}},
 "e1-agent-loop": {"evo": "E1", "title": "The Agent Loop", "figs": {3: "loop-that-halts", 6: "loop-that-halts", 7: "loop-that-halts"}, "cols": {5: 564}},
 "e2-patterns-frameworks": {"evo": "E2", "title": "Patterns and Orchestration Frameworks", "figs": {3: "who-owns-the-loop", 4: "who-owns-the-loop", 9: "who-owns-the-loop"}},
 "e3-tools-as-contracts": {"evo": "E3", "title": "Tools as Contracts", "figs": {3: "the-gate-holds", 5: "the-gate-holds", 6: "the-gate-holds"}},
 "e4-mcp-1": {"evo": "E4", "title": "MCP I: Building a Server", "figs": {3: "n-plus-m", 4: "n-plus-m"}},
 "e5-mcp-2-security-harness": {"evo": "E5", "title": "MCP II: Security and the Harness", "figs": {4: "trust-boundaries", 7: "trust-boundaries", 10: "skill-on-demand", 18: "three-drawers"}},
 "e6-context-engineering": {"evo": "E6", "title": "Context Engineering", "figs": {3: "window-budget", 4: "window-budget", 6: "window-budget", 7: "window-budget", 8: "three-drawers"}},
 "e7-memory": {"evo": "E7", "title": "Memory: Retrieval, State, Eviction, Retention", "figs": {3: "memory-is-a-claim", 5: "memory-is-a-claim", 6: "memory-is-a-claim", 10: "memory-is-a-claim", 13: "pilot-and-planter"}},
 "e8-multi-agent-1": {"evo": "E8", "title": "Multi-agent I: Controller, Worker, Reviewer", "figs": {3: "plan-do-check", 7: "plan-do-check", 9: "plan-do-check", 10: "steer-the-middle", 12: "plan-do-check"}},
 "e9-multi-agent-2": {"evo": "E9", "title": "Multi-agent II: When Coordination Fails", "figs": {3: "claim-receipt-verdict", 5: "claim-receipt-verdict", 6: "claim-receipt-verdict"}},
 "e10-evals-as-gates": {"evo": "E10", "title": "Evaluation I: Evals as Gates", "figs": {6: "one-run-is-an-anecdote", 7: "one-run-is-an-anecdote", 10: "one-run-is-an-anecdote"}},
 "e11-observability-red-team": {"evo": "E11", "title": "Evaluation II: Receipts, Red Team, Safety", "figs": {3: "receipts-over-narrative", 4: "receipts-over-narrative", 5: "receipts-over-narrative"}},
 "e12-deployment": {"evo": "E12", "title": "Production Deployment", "figs": {7: "rolled-back", 10: "rolled-back", 11: "rolled-back"}},
 "mini-attention-2017": {"evo": "Mini-lecture", "title": "Attention Is All You Need, read as a design document", "figs": {4: "transformer-2017", 5: "transformer-2017", 6: "transformer-2017", 7: "transformer-evidence", 8: "transformer-evidence", 11: "two-loops"}},
}

TONE = {"F4EAEE": "rose", "E4F0F0": "teal", "F5F3F4": "neutral", "6D1F3B": "accent", "2E6F73": "accent2"}

def px(emu): return int(round(emu / 9525))

def shape_fill(sh):
    try:
        if sh.fill.type == 1: return str(sh.fill.fore_color.rgb)
    except Exception: pass
    return None

def para_text(p): return "".join(r.text for r in p.runs)

# Voice overrides: tools/sitekit/voice/<slug>.json maps a slide paragraph (or table cell) as extracted from the pptx
# to its revised wording (the humaniser / STE / scholarly-voice pass of Oct 22, 2026). The pptx stays the source of
# layout; the JSON is the source of the words. Keys that no longer match any paragraph are reported at build time.
VOICE = {}
VOICE_HIT = set()
def load_voice(slug):
    global VOICE
    p = HERE / "voice" / (slug + ".json")
    VOICE = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
    VOICE_HIT.clear()
def ov(t):
    if t in VOICE and VOICE[t] != t:
        VOICE_HIT.add(t); return VOICE[t]
    return t

def is_code_box(paras, fonts):
    if any(f and "Courier" in f for f in fonts): return True
    lines = [para_text(p) for p in paras if para_text(p).strip()]
    if len(lines) < 3: return False
    codey = sum(1 for l in lines if re.match(r"^\s{2,}\S|^(def |class |import |from |if |elif |else:|try:|except|return |for |while |with |OK = |[\w\.]+\(.*\)\s*$|---$|\$ |\w+ = |\[\w+#?\d*\]|TASK |DISPATCH |CHASE )", l) or l.rstrip().endswith(("{", "}", "\\")))
    return codey >= max(2, len(lines) * 0.5)

def extract(pptx_path):
    p = Presentation(str(pptx_path))
    out = []
    for n, sl in enumerate(p.slides, 1):
        texts, panels, tables = [], [], []
        for sh in sl.shapes:
            L, T, W, H = px(sh.left), px(sh.top), px(sh.width), px(sh.height)
            if sh.has_table:
                tb = sh.table
                rows = [[ov(c.text) for c in r.cells] for r in tb.rows]
                tables.append({"l": L, "t": T, "w": W, "h": H, "rows": rows})
                continue
            if not sh.has_text_frame:
                continue
            paras = [x for x in sh.text_frame.paragraphs if not (para_text(x).strip() and VOICE.get(para_text(x)) == "")]  # override "" drops the line
            txt = "\n".join(para_text(x) for x in paras).strip()
            fill = shape_fill(sh)
            if not txt:
                if sh.name.startswith("Shape") and W > 40 and H > 20:
                    panels.append({"l": L, "t": T, "w": W, "h": H, "tone": TONE.get(fill, "neutral"), "items": []})
                continue
            fonts = [r.font.name for x in paras for r in x.runs]
            sizes = [r.font.size.pt for x in paras for r in x.runs if r.font.size]
            bold = any(r.font.bold for x in paras for r in x.runs)
            runs = [[(r.text, bool(r.font.bold)) for r in x.runs] if ov(para_text(x)) == para_text(x) else [(ov(para_text(x)), False)] for x in paras]
            texts.append({"l": L, "t": T, "w": W, "h": H, "paras": [ov(para_text(x)) for x in paras], "runs": runs, "size": max(sizes) if sizes else 11,
                          "bold": bold, "allbold": all(r.font.bold for x in paras for r in x.runs if r.text.strip()), "code": is_code_box(paras, fonts), "fill": fill, "name": sh.name})
        out.append({"n": n, "texts": texts, "panels": panels, "tables": tables})
    return out

def classify(slide):
    """Pick title/subtitle; drop timing, footer, page number; attach texts to panels."""
    texts = slide["texts"]
    drop, title, sub, kick = [], None, None, None
    for t in texts:
        joined = " ".join(t["paras"]).strip()
        if t["t"] > 490 and t["size"] <= 8: drop.append(t); continue                    # footer, page number
        if re.match(r"^CIDM 6333 · Fall 20\d\d\b", joined): drop.append(t); continue           # deck footer with term and page
        if t["l"] > 700 and t["t"] < 60 and re.match(r"^\d:\d\d", joined): drop.append(t); continue  # timing
        if t["t"] < 60 and t["size"] >= 14 and t["bold"] and title is None and t["l"] < 100: title = t; continue
        if t["t"] < 60 and t["size"] <= 11 and t["h"] <= 40 and title is None and sub is None and not t["bold"]: kick = t; continue  # "Evolution 8 · Lecture"
        if title is not None and sub is None and t["t"] < 110 and t["t"] >= title["t"] and not t["bold"] and t["size"] <= 14: sub = t; continue
    body = [t for t in texts if t not in drop and t is not title and t is not sub and t is not kick]
    # title slide: the big bold text is the title even if lower
    if title is None:
        cands = [t for t in body if t["bold"] and t["size"] >= 20]
        if cands:
            title = max(cands, key=lambda t: t["size"]); body.remove(title)
            subs = [t for t in body if t["t"] > title["t"] and t["t"] < title["t"] + 120 and not t["bold"] and t["size"] >= 12]
            if subs: sub = subs[0]; body.remove(sub)
    # attach to panels by containment of the text box centre
    for t in body:
        cx, cy = t["l"] + t["w"] / 2, t["t"] + t["h"] / 2
        host = None
        for pnl in slide["panels"]:
            if pnl["l"] <= cx <= pnl["l"] + pnl["w"] and pnl["t"] <= cy <= pnl["t"] + pnl["h"]:
                if host is None or pnl["w"] * pnl["h"] < host["w"] * host["h"]: host = pnl
        if host: host["items"].append(t)
        else: slide.setdefault("free", []).append(t)
    for pnl in slide["panels"]: pnl["items"].sort(key=lambda t: (t["t"], t["l"]))
    slide["title"], slide["sub"], slide["kick"] = title, sub, kick
    return slide

def scrub_paras(paras):
    out = []
    for ptxt in paras:
        if not ptxt.strip(): out.append(""); continue
        c = RD.scrub_line(ptxt) if len(ptxt) < 160 else RD.scrub_sentence_list(ptxt)
        if c.strip(): out.append(c)
    # collapse leading/trailing blanks
    while out and not out[0].strip(): out.pop(0)
    while out and not out[-1].strip(): out.pop()
    return out

def run_html(t, ptxt):
    """Escape a paragraph; keep bold lead-ins when the paragraph text is unchanged by scrubbing."""
    for runs in t.get("runs", []):
        if "".join(x for x, b in runs) == ptxt and any(b for x, b in runs) and not all(b for x, b in runs if x.strip()):
            return "".join(("<strong>%s</strong>" if b else "%s") % html.escape(x) for x, b in runs)
    return html.escape(ptxt)

def render_text(t, in_panel):
    paras = scrub_paras(t["paras"])
    if not paras: return ""
    if t["code"]:
        tail = []
        while paras and re.match(r"^[A-Z][^{}()\[\]=]*[.!?]$", paras[-1].strip()) and not paras[-1].startswith(" "):
            tail.insert(0, paras.pop())
        while paras and not paras[-1].strip(): paras.pop()
        long = ' class="long"' if len(paras) > 20 else (' class="mid"' if len(paras) > 14 else "")
        return '<pre%s><code>%s</code></pre>' % (long, html.escape("\n".join(paras))) + "".join("<p>%s</p>" % html.escape(x) for x in tail)
    h = []
    i = 0
    first = True
    while i < len(paras):
        ptxt = paras[i]
        if not ptxt.strip(): i += 1; continue
        if first and in_panel and t["allbold"] and len(ptxt) < 90 and len(paras) == 1 and t.get("size", 11) >= 11.5:
            h.append("<h4>%s</h4>" % html.escape(ptxt)); i += 1; first = False; continue
        first = False
        # a label line followed by short lines -> list
        if ptxt.rstrip().endswith(":") and i + 1 < len(paras) and all(len(x) <= 110 for x in paras[i+1:i+3] if x.strip()):
            h.append("<p><strong>%s</strong></p>" % html.escape(ptxt))
            items = []
            j = i + 1
            while j < len(paras) and paras[j].strip() and len(paras[j]) <= 110 and not paras[j].rstrip().endswith(":"):
                items.append(paras[j]); j += 1
            if items: h.append("<ul>" + "".join("<li>%s</li>" % run_html(t, x) for x in items) + "</ul>")
            i = j; continue
        if not in_panel and t["bold"] and t.get("size", 11) <= 9.5 and len(ptxt) <= 14 and ptxt.isupper():
            h.append('<span class="chip">%s</span>' % html.escape(ptxt)); i += 1; continue
        cls = ' class="quote"' if (t.get("size", 11) >= 14 and not t["bold"] and in_panel) else ""
        if t["allbold"] and len(ptxt) < 140: h.append("<p%s><strong>%s</strong></p>" % (cls, html.escape(ptxt)))
        else: h.append("<p%s>%s</p>" % (cls, run_html(t, ptxt)))
        i += 1
    return "".join(h)

def render_table(tb):
    rows = tb["rows"]
    if not rows: return ""
    head = "<tr>" + "".join("<th>%s</th>" % html.escape(c) for c in rows[0]) + "</tr>"
    body = "".join("<tr>" + "".join("<td>%s</td>" % html.escape(RD.scrub_line(c) if c else "") for c in r) + "</tr>" for r in rows[1:])
    return '<div class="tw"><table><thead>%s</thead><tbody>%s</tbody></table></div>' % (head, body)

def layout_rows(slide):
    """Group panels, tables and free texts into rows by vertical position; cells get width fractions."""
    cells = []
    for pnl in slide["panels"]:
        if pnl["tone"] in ("accent", "accent2") and pnl["h"] < 60:
            label = " ".join(" ".join(scrub_paras(t["paras"])) for t in pnl["items"]).strip()
            if label: cells.append({"t": pnl["t"], "l": pnl["l"], "w": pnl["w"], "h": pnl["h"], "html": '<span class="chip">%s</span>' % html.escape(label), "tone": "chipcell"})
            continue
        inner = "".join(render_text(t, True) for t in pnl["items"])
        if inner.strip(): cells.append({"t": pnl["t"], "l": pnl["l"], "w": pnl["w"], "h": pnl["h"], "html": inner, "tone": pnl["tone"]})
    for tb in slide["tables"]:
        cells.append({"t": tb["t"], "l": tb["l"], "w": tb["w"], "h": tb["h"], "html": render_table(tb), "tone": "table"})
    for t in slide.get("free", []):
        inner = render_text(t, False)
        if inner.strip(): cells.append({"t": t["t"], "l": t["l"], "w": t["w"], "h": t["h"], "html": inner, "tone": "free"})
    cells.sort(key=lambda c: (c["t"], c["l"]))
    rows = []
    for c in cells:
        if rows and abs(rows[-1][0]["t"] - c["t"]) < 18: rows[-1].append(c)
        else: rows.append([c])
    for r in rows: r.sort(key=lambda c: c["l"])
    # a row of chips collapses into one flex cell
    out = []
    for r in rows:
        if all(c["tone"] == "chipcell" for c in r):
            out.append([{"t": r[0]["t"], "l": r[0]["l"], "w": sum(c["w"] for c in r), "h": r[0]["h"], "html": '<div class="chips">%s</div>' % "".join(c["html"] for c in r), "tone": "free"}])
        else: out.append(r)
    return out

def row_html(r):
    tw = sum(c["w"] for c in r) or 1
    cols = " ".join("%.2ffr" % (c["w"] / tw * len(r)) for c in r)
    return '<div class="row" style="grid-template-columns:%s">' % cols + "".join('<div class="cell %s">%s</div>' % (c["tone"], c["html"]) for c in r) + "</div>"

def column_body(rows, split):
    """Two-column reflow for slides whose pptx layout puts a tall panel beside a stack of rows:
    cells left of `split` stack in the left column, cells right of it in the right column,
    and cells that straddle the split become full-width rows after the columns."""
    cells = [c for r in rows for c in r if not (c["t"] > 490 and re.fullmatch(r"\s*\d+\s*", re.sub(r"<[^>]+>", "", c["html"])))]
    left = [c for c in cells if c["l"] + c["w"] <= split + 4]
    right = [c for c in cells if c["l"] >= split - 4 and c not in left]
    wide = [c for c in cells if c not in left and c not in right]
    def group(cs):
        out = []
        for c in sorted(cs, key=lambda c: (c["t"], c["l"])):
            if out and abs(out[-1][0]["t"] - c["t"]) < 18: out[-1].append(c)
            else: out.append([c])
        for r in out: r.sort(key=lambda c: c["l"])
        return out
    lw = max((c["l"] + c["w"] for c in left), default=split) - min((c["l"] for c in left), default=0)
    rw = max((c["l"] + c["w"] for c in right), default=split) - min((c["l"] for c in right), default=split)
    html_cols = '<div class="row cols" style="grid-template-columns:%.2ffr %.2ffr"><div class="col">%s</div><div class="col">%s</div></div>' % (
        lw, rw, "".join(row_html(r) for r in group(left)), "".join(row_html(r) for r in group(right)))
    return [html_cols] + [row_html(r) for r in group(wide)]

def render_slide(slide, n, total, meta, fig, img):
    title = html.escape(" ".join(scrub_paras(slide["title"]["paras"])) if slide["title"] else "")
    sub = html.escape(" ".join(scrub_paras(slide["sub"]["paras"])) if slide["sub"] else "")
    rows = layout_rows(slide)
    split = meta.get("cols", {}).get(slide["n"])
    body = column_body(rows, split) if split else [row_html(r) for r in rows]
    if not body and not title: return ""
    kick = "%s · slide %d of %d" % (meta["evo"] + ("" if meta["evo"] in ("Orientation", "Mini-lecture") else " · Lecture"), n, total)
    figlink = ('<a href="../../figures/%s.html" target="_blank">Figure: %s</a>' % (fig, fig.replace("-", " "))) if fig else ""
    return ('<section class="slide" data-n="%d"%s><div class="kick">%s</div><h2>%s%s</h2><div class="body">%s</div>'
            '<div class="foot"><span>CIDM 6333 · %s</span><span>%s</span></div></section>') % (
            n, (' data-fig="%s"' % fig) if fig else "", kick, title, ("<small>%s</small>" % sub) if sub else "", "".join(body), meta["evo"], figlink)

def slide_kept(title):
    return not DROP_TITLE.search((title or "").strip())

CSS = """<style id="deck-css">
.stage{background:var(--surface); border:1px solid var(--line); border-radius:12px; overflow:hidden}
.slides{position:relative; aspect-ratio:16/9; width:100%}
.slide{position:absolute; inset:0; padding:clamp(16px,2.6vw,36px) clamp(18px,3vw,44px); display:none; grid-template-rows:auto auto 1fr auto; gap:8px; overflow:hidden; background:var(--surface)}
.slide.cur{display:grid}
.slide .kick{font-family:var(--display); font-weight:600; letter-spacing:.12em; text-transform:uppercase; font-size:clamp(11px,1.05vw,13.5px); color:var(--accent-ink)}
.slide h2{font-family:var(--display); font-weight:700; font-size:clamp(22px,2.9vw,40px); line-height:1.02; margin:0; letter-spacing:-.01em; text-wrap:balance}
.slide h2 small{display:block; font-weight:500; font-size:clamp(13px,1.35vw,18px); color:var(--ink-2); margin-top:5px; letter-spacing:0}
.slide .body{min-height:0; display:grid; align-content:start; gap:10px; font-size:clamp(12.5px,1.3vw,17.5px); line-height:1.38; overflow:auto}
.slide .row{display:grid; gap:12px; align-items:start}
.slide .row.cols{align-items:start}
.slide .col{display:grid; gap:10px; align-content:start; min-width:0}
.slide .cell{min-width:0}
.slide .cell.rose,.slide .cell.teal,.slide .cell.neutral{border-radius:9px; padding:10px 14px}
.slide .cell.rose{background:var(--accent-soft)}
.slide .cell.teal{background:var(--model); border:1px solid var(--model-line)}
.slide .cell.neutral{background:var(--surface-2)}
.slide .cell h4{font-family:var(--display); font-weight:600; font-size:1.05em; margin:0 0 6px; letter-spacing:.02em}
.slide .cell p{margin:0 0 6px}
.slide .cell p.quote{font-size:1.12em; font-style:italic; line-height:1.3}
.slide .cell ul{margin:0 0 6px; padding-left:1.1em; display:grid; gap:3px}
.slide .cell pre{margin:0; background:var(--surface-2); border:1px solid var(--line); border-radius:8px; padding:8px 10px; font-size:.82em; line-height:1.35; overflow:auto; white-space:pre-wrap; overflow-wrap:anywhere}
.slide .cell.teal pre,.slide .cell.rose pre,.slide .cell.neutral pre{background:var(--surface)}
.slide .cell pre code{font-family:var(--mono)}
.slide .cell pre.mid{font-size:.74em}
.slide .cell pre.long{font-size:.66em; line-height:1.3}
.slide table{border-collapse:collapse; width:100%; font-size:.86em}
.slide th{font-family:var(--display); font-weight:600; letter-spacing:.05em; text-transform:uppercase; font-size:.8em; color:var(--ink-2); text-align:left; padding:4px 7px; border-bottom:1.5px solid var(--ink-2)}
.slide td{padding:4px 7px; border-bottom:1px solid var(--line); vertical-align:top}
.slide .tw{overflow:auto; max-height:100%}
.slide .foot{font-family:var(--display); font-weight:500; font-size:clamp(11px,1vw,13px); color:var(--ink-2); letter-spacing:.04em; display:flex; justify-content:space-between; gap:12px}
.slide .foot a{color:var(--accent-ink); text-decoration:none; border-bottom:1px dotted var(--accent)}
.slide a.gl{color:inherit; text-decoration:none; border-bottom:1px dotted var(--accent)}
.slide a.gl:hover{color:var(--accent-ink)}
.slide .chips{display:flex; gap:8px; flex-wrap:wrap}
.slide .chips .chip{font-size:.95em}
.slide.title{align-content:center}
.slide.title h2{font-size:clamp(32px,5.2vw,68px)}
.figframe{position:absolute; inset:0; display:none; background:var(--bg)}
.figframe iframe{width:100%; height:100%; border:0}
.slides.show-fig .figframe{display:block}
.ctrls{border-top:1px solid var(--line); display:flex; gap:10px; align-items:center; padding:12px 18px; flex-wrap:wrap}
.ctrls .count{font-family:var(--mono); font-size:14px; color:var(--ink-2)}
.ctrls .title{font-family:var(--display); font-weight:600; font-size:17px; min-width:0; flex:1 1 200px}
.ctrls .hint{font-size:13.5px; color:var(--ink-2); font-family:var(--display); letter-spacing:.04em}
.ctrls a.dl{font-family:var(--display); font-weight:600; font-size:15px; letter-spacing:.04em; color:var(--accent-ink); background:var(--surface); border:1px solid var(--ink-2); border-radius:8px; padding:7px 14px; text-decoration:none}
button[aria-pressed="true"]{background:var(--ink); color:var(--bg); border-color:var(--ink)}
.strip{display:flex; gap:6px; overflow-x:auto; padding:10px 14px 14px; border-top:1px solid var(--line)}
.strip button{flex:0 0 auto; width:150px; height:58px; padding:6px 8px; border:2px solid var(--line); border-radius:6px; background:var(--surface); color:var(--ink); overflow:hidden; cursor:pointer; text-align:left; display:grid; grid-template-columns:auto 1fr; gap:6px; align-items:start; font-family:var(--display); font-weight:500; letter-spacing:0; font-size:12.5px; line-height:1.15}
.strip .sn{font-family:var(--mono); font-size:11px; color:var(--ink-2)}
.strip .st{display:-webkit-box; -webkit-line-clamp:3; -webkit-box-orient:vertical; overflow:hidden}
.strip button[aria-current="true"]{border-color:var(--accent)}
:fullscreen .stage{border:0; border-radius:0; height:100vh; display:grid; grid-template-rows:1fr auto}
:fullscreen .slides{aspect-ratio:auto; height:100%}
:fullscreen .strip{display:none}
@media (max-width:760px){ .slides{aspect-ratio:auto} .slide{position:relative; min-height:0; overflow:visible} .slide .body{overflow:visible} .orig,.figframe{position:relative; min-height:56vw} }
@media print{ .slide{display:grid!important; position:relative; page-break-after:always; height:7.5in; border-bottom:1px solid #ccc} .ctrls,.strip,.orig,.figframe{display:none} }
</style>
<style id="reader-css">
.notecur{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:16px 20px;margin-top:12px}
.notecur .k{font-family:var(--display);font-weight:600;letter-spacing:.1em;text-transform:uppercase;font-size:13px;color:var(--accent-ink);margin-bottom:4px}
.notecur p{margin:0 0 8px;max-width:78ch}
.notecur p:last-child{margin-bottom:0}
.reader{margin-top:36px}
.reader h2{font-size:30px;margin-bottom:4px}
.rslide{display:grid;grid-template-columns:90px minmax(0,1fr);gap:14px 22px;padding:18px 0;border-top:1px solid var(--line);align-items:start}
.rslide .rthumb{display:block;padding:4px 8px;border:1px solid var(--line);background:var(--surface);cursor:pointer;border-radius:6px;font-family:var(--mono);font-size:13px;color:var(--ink-2)}
.rslide .rthumb:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.rslide img{width:100%;height:auto;border:1px solid var(--line);border-radius:6px;background:#fff;display:block}
.rslide .n{font-family:var(--mono);font-size:13px;color:var(--ink-2)}
.rslide h3{font-family:var(--display);font-weight:600;font-size:22px;margin:2px 0 8px;line-height:1.1}
.rslide p{margin:0 0 8px;max-width:78ch}
@media (max-width:700px){.rslide{grid-template-columns:1fr}}
</style>"""

def build(docs, slug):
    meta = DECK_META[slug]
    pptx_name = RD.DECKS[slug][0]
    pptx = PPTX_DIR / "Lecture" / pptx_name
    if not pptx.exists(): pptx = PPTX_DIR / "Fall 2026" / "Orientation" / pptx_name
    load_voice(slug)
    slides = [classify(s) for s in extract(pptx)]
    miss = [k for k in VOICE if k not in VOICE_HIT and VOICE[k] != k and VOICE[k] != ""]
    if miss: print("voice overrides with no matching paragraph (%d):" % len(miss), *[repr(m[:60]) for m in miss], sep="\n  ")
    notes = RD.NOTES[pptx_name]
    pairs = GL.link_terms()
    total = len(slides)
    keep = []
    for s in slides:
        ttl = " ".join(s["title"]["paras"]) if s["title"] else ""
        if DROP_TITLE.search(ttl.strip()): continue
        keep.append(s)
    total = len(keep)
    out_slides, titles, per = [], [], []
    for idx, s in enumerate(keep, 1):
        n = s["n"]; img = "s-%02d.webp" % n
        h = render_slide(s, idx, total, meta, meta["figs"].get(n), img)
        if not h:
            continue
        if idx == 1: h = h.replace('<section class="slide"', '<section class="slide title"', 1)
        out_slides.append(h)
        titles.append(" ".join(scrub_paras(s["title"]["paras"])) if s["title"] else ("Slide %d" % n))
        paras, cuts = RD.split_notes(notes[n-1])
        per.append((idx, paras))
    import linkify as LK
    N = [LK.autolink(RD.para_html(p)) for n, p in per]
    nums = [n for n, p in per]
    # textbook line
    evo_key = RD.DECKS[slug][1]
    chs = TB.chapters_for_evo(evo_key) if evo_key else []; dirs = TB.main_dirs()
    chap = " · ".join('<a href="../../textbook/%s/">Chapter %d</a> <span class="small">(%s)</span>' % (dirs[c], c, r) for c, r in chs if c in dirs)
    strip = "".join('<button type="button" data-i="%d" aria-label="Slide %d: %s" title="%s"><span class="sn">%d</span><span class="st">%s</span></button>' % (i, i + 1, html.escape(titles[i]), html.escape(titles[i]), i + 1, html.escape(titles[i])) for i, n in enumerate(nums))
    reader = "".join('<div class="rslide" id="r%d"><div><button type="button" class="rthumb" data-i="%d" aria-label="Open slide %d in the viewer">slide %02d</button></div><div><h3>%s</h3>%s</div></div>' % (i + 1, i, i + 1, i + 1, html.escape(titles[i]), N[i]) for i, n in enumerate(nums))
    head = (HERE / "page-head.html").read_text(encoding="utf-8").replace("{{TITLE}}", html.escape(meta["evo"] + " · " + meta["title"]))
    page = head + CSS + '''
<div class="wrap">
<nav class="crumbs"><a href="../../">CIDM 6333</a> · <a href="../">Lectures</a> · %(evo)s</nav>
<header>
  <div class="eyebrow">Lecture · %(evo)s · web-native deck</div>
  <h1>%(title)s</h1>
  <p class="lede">%(lede)s</p>
  <div class="weeks" style="display:flex;gap:6px;flex-wrap:wrap;margin-top:6px"><span class="chip">%(evo)s</span><span class="chip">%(count)d slides</span></div>
</header>
%(chapline)s
<section class="deck" aria-label="Slides">
<div class="stage" id="stage">
<div class="slides" id="slides" tabindex="0" aria-label="Slides; use the arrow keys">
%(slides)s
<div class="figframe" id="figframe"></div>
</div>
<div class="ctrls">
  <button id="prev" type="button" aria-label="Previous slide">◀ Back</button>
  <button id="next" class="primary" type="button" aria-label="Next slide">Next ▶</button>
  <span class="count" id="count" role="status">1 / %(count)d</span>
  <span class="title" id="stitle"></span>
  <button id="figbtn" type="button" aria-pressed="false" hidden>Figure</button>
  <button id="full" type="button">Full screen</button>
  <a class="dl" href="#read">Read</a>
</div>
<div class="strip" id="strip" role="group" aria-label="Slides">%(strip)s</div>
</div>
</section>
<div class="notecur" id="notecur" aria-live="polite"><div class="k">The lecture, written out · slide <span id="noteno">1</span></div><div id="notebody"></div></div>
<p class="small" style="margin-top:10px">Arrow keys step through the slides, and "Figure" opens the interactive figure a slide refers to. The panel above is the lecture written out for the slide on screen. <a href="#read">Read this lecture</a>, below, has the whole lecture in slide order. Names that appear without introduction link to the <a href="../../glossary/">glossary</a>.</p>
<section class="reader" id="read" aria-label="Read this lecture"><h2>Read this lecture</h2><p class="lede small">The speaker notes follow here slide by slide. Click a slide number to open that slide in the viewer above.</p>%(reader)s</section>
<footer>CIDM 6333 · Lecture · %(evo)s</footer>
</div>
<script id="reader-js">(function(){const N=%(N)s;const NUMS=%(NUMS)s;const $=i=>document.getElementById(i);
const slides=[...document.querySelectorAll(".slide")], n=slides.length; let cur=0;
const strip=$("strip"), btns=[...strip.querySelectorAll("button")];
function fit(s){ const bd=s.querySelector(".body"); if(!bd) return; bd.style.fontSize=""; let k=1; const base=parseFloat(getComputedStyle(bd).fontSize);
  while(bd.scrollHeight>bd.clientHeight+2 && k>0.72){ k-=0.04; bd.style.fontSize=(base*k)+"px"; } }
window.addEventListener("resize",()=>fit(slides[cur])); document.addEventListener("fullscreenchange",()=>setTimeout(()=>fit(slides[cur]),60));
function go(i){ cur=Math.max(0,Math.min(n-1,i)); slides.forEach((s,j)=>s.classList.toggle("cur",j===cur)); const s=slides[cur];
  $("count").textContent=(cur+1)+" / "+n; const h2=s.querySelector("h2").cloneNode(true); h2.querySelectorAll("small").forEach(e=>e.remove()); $("stitle").textContent=h2.textContent.trim(); fit(s);
  $("noteno").textContent=NUMS[cur]; $("notebody").innerHTML=N[cur]||"";
  const f=s.dataset.fig; $("figbtn").hidden=!f; if(!f){ $("slides").classList.remove("show-fig"); $("figbtn").setAttribute("aria-pressed","false"); }
  else if($("slides").classList.contains("show-fig")){ $("figframe").innerHTML='<iframe src="../../figures/'+f+'.html?embed=1" title="Figure"></iframe>'; }
  const pv=$("prev"), nx=$("next"); pv.disabled=cur===0; nx.disabled=cur===n-1; if(document.activeElement===nx&&nx.disabled) pv.focus(); if(document.activeElement===pv&&pv.disabled) nx.focus();
  btns.forEach((b,j)=>{ if(j===cur) b.setAttribute("aria-current","true"); else b.removeAttribute("aria-current"); }); if(btns[cur]) btns[cur].scrollIntoView({block:"nearest",inline:"nearest"});
  try{ history.replaceState(null,"","#"+(cur+1)); }catch(e){} }
$("prev").addEventListener("click",()=>go(cur-1)); $("next").addEventListener("click",()=>go(cur+1));
btns.forEach(b=>b.addEventListener("click",()=>go(+b.dataset.i)));
$("figbtn").addEventListener("click",()=>{ const on=$("slides").classList.toggle("show-fig"); $("figbtn").setAttribute("aria-pressed",on); if(on){ $("figframe").innerHTML='<iframe src="../../figures/'+slides[cur].dataset.fig+'.html?embed=1" title="Figure"></iframe>'; } else $("figframe").innerHTML=""; });
$("full").addEventListener("click",()=>{ const st=$("stage"); if(document.fullscreenElement) document.exitFullscreen(); else if(st.requestFullscreen) st.requestFullscreen(); });
document.querySelectorAll(".rslide .rthumb").forEach(im=>im.addEventListener("click",()=>{ go(+im.dataset.i); $("stage").scrollIntoView({behavior:"smooth",block:"start"}); }));
function stageActive(){ const st=$("stage"); const r=st.getBoundingClientRect(); return st.contains(document.activeElement) || (r.top<window.innerHeight*0.6 && r.bottom>window.innerHeight*0.4); }
document.addEventListener("keydown",e=>{ if(e.target.matches("input,select,textarea,iframe")) return; if(!stageActive()) return;
  if(e.key==="ArrowRight"||e.key==="PageDown"){ go(cur+1); e.preventDefault(); } if(e.key==="ArrowLeft"||e.key==="PageUp"){ go(cur-1); e.preventDefault(); }
  if(e.key==="Home"){ go(0); e.preventDefault(); } if(e.key==="End"){ go(n-1); e.preventDefault(); } if(e.key==="f"||e.key==="F"){ $("full").click(); } });
const h=parseInt(location.hash.slice(1)); go(isNaN(h)?0:h-1);
})();</script>
</body></html>
''' % dict(evo=meta["evo"], title=html.escape(meta["title"]), lede=html.escape(" ".join(scrub_paras(slides[0]["sub"]["paras"])) if slides[0]["sub"] else ""), count=len(out_slides), chapline=('<p class="small chapters" style="margin:0 0 10px"><strong>Textbook:</strong> %s · <a href="../../glossary/">Glossary</a></p>' % chap) if chap else '<p class="small chapters" style="margin:0 0 10px"><a href="../../glossary/">Glossary</a></p>',
           slides="\n".join(out_slides), slug=slug, strip=strip, reader=reader, N=json.dumps(N), NUMS=json.dumps(nums))
    outp = pathlib.Path(docs) / "lectures" / slug / "index.html"
    outp.write_text(page, encoding="utf-8")
    print(slug, "web-native:", len(out_slides), "slides")

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
