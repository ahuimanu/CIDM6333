#!/usr/bin/env python3
"""Add the speaker-notes reader to each lecture page.

For every slide: the notes prose (the lecture, written out) under the viewer for the current slide,
and a full "Read this lecture" section (slide thumbnail + notes + the slide's full wording) above the transcript.
[Verify ...] instructor reminders are removed. Idempotent.

Usage: python3 reader.py <docs-dir>   (expects notes.json beside this script)
"""
import re, sys, json, html, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import textbook as TB

HERE = pathlib.Path(__file__).parent
NOTES = json.loads((HERE / "notes.json").read_text(encoding="utf-8"))
DECKS = {
 "orientation": ("CIDM6333-Fall2026-Orientation.pptx", "E0"),
 "e0-index-zero": ("CIDM6333_E0_Lecture_IndexZero.pptx", "E0"),
 "e1-agent-loop": ("CIDM6333_E1_Lecture_AgentLoop.pptx", "E1"),
 "e2-patterns-frameworks": ("CIDM6333_E2_Lecture_PatternsFrameworks.pptx", "E2"),
 "e3-tools-as-contracts": ("CIDM6333_E3_Lecture_ToolsAsContracts.pptx", "E3"),
 "e4-mcp-1": ("CIDM6333_E4_Lecture_MCP1.pptx", "E4"),
 "e5-mcp-2-security-harness": ("CIDM6333_E5_Lecture_MCP2_Security_Harness.pptx", "E5"),
 "e6-context-engineering": ("CIDM6333_E6_Lecture_ContextEngineering.pptx", "E6"),
 "e7-memory": ("CIDM6333_E7_Lecture_Memory.pptx", "E7"),
 "e8-multi-agent-1": ("CIDM6333_E8_Lecture_MultiAgent1.pptx", "E8"),
 "e9-multi-agent-2": ("CIDM6333_E9_Lecture_MultiAgent2.pptx", "E9"),
 "e10-evals-as-gates": ("CIDM6333_E10_Lecture_EvalsAsGates.pptx", "E10"),
 "e11-observability-red-team": ("CIDM6333_E11_Lecture_Observability-RedTeam.pptx", "E11"),
 "e12-deployment": ("CIDM6333_E12_Lecture_Deployment.pptx", "E12"),
 "mini-attention-2017": ("CIDM6333_MiniLecture_Attention2017.pptx", None),
}

CSS = """<style id="reader-css">
.notecur{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:16px 20px;margin-top:12px}
.notecur .k{font-family:var(--display);font-weight:600;letter-spacing:.1em;text-transform:uppercase;font-size:12px;color:var(--accent-ink);margin-bottom:4px}
.notecur p{margin:0 0 8px;max-width:78ch}
.notecur p:last-child{margin-bottom:0}
.reader{margin-top:36px}
.reader h2{font-size:30px;margin-bottom:4px}
.reader .lede{margin-bottom:14px}
.rslide{display:grid;grid-template-columns:260px minmax(0,1fr);gap:14px 22px;padding:18px 0;border-top:1px solid var(--line);align-items:start}
.rslide .rthumb{display:block;width:100%;padding:0;border:0;background:none;cursor:pointer;border-radius:6px}
.rslide .rthumb:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.rslide img{width:100%;height:auto;border:1px solid var(--line);border-radius:6px;background:#fff;display:block}
.rslide .n{font-family:var(--mono);font-size:12.5px;color:var(--ink-2)}
.rslide h3{font-family:var(--display);font-weight:600;font-size:22px;margin:2px 0 8px;line-height:1.1}
.rslide p{margin:0 0 8px;max-width:78ch}
.rslide details{margin-top:6px;font-size:15px}
.rslide summary{font-family:var(--display);font-weight:600;letter-spacing:.05em;cursor:pointer;color:var(--ink-2)}
.rslide ul{margin:6px 0 0;padding-left:20px;display:grid;gap:4px;color:var(--ink-2)}
@media (max-width:700px){.rslide{grid-template-columns:1fr}}
</style>"""

# --- scrubbing: the site carries no schedule, no room, no contact details, no instructor reminders ---
SCHED = re.compile("|".join([
    r"\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\b\.?\s*\d{1,2}/\d{1,2}(/\d{2,4})?",      # Thu 10/22, Wed 11/11/2026
    r"\b\d{1,2}/\d{2}/\d{4}\b", r"\b(0?[1-9]|1[0-2])/[0-3]\d\b(?!/)",          # 10/22/2026, 09/17
    r"\b\d{1,2}:\d{2}\s*(a\.m\.|p\.m\.|am|pm)?(?![\d:])",                     # 4:00, 11:59 p.m., 5:46, 0:55
    r"\bCC2\d\d[A-Z]?\b", r"\bCalendly\b", r"\bWTClass\b", r"\bDiscord\b",
    r"\b(at|by) (six|five|noon|midnight)\b", r"\bone-thirty\b",
    r"\btonight\b", r"\bthis week\b", r"\blast (week|Thursday|semester)\b", r"\bnext (week|Thursday)\b",
    r"\bbefore class\b", r"\bverify on your version\b", r"\bin class\b",
    r"\b\d{3}-\d{3}-\d{4}\b", r"[\w.]+@wtamu\.edu", r"\bLabor Day\b", r"\bcode freeze\b",
    r"\bWednesdays?( night| evening)?\b", r"\bFriday( night)?\b", r"\bSaturday\b", r"\bSunday\b", r"\bMonday\b", r"\bTuesday\b", r"\bThursdays?\b",
    r"\bby appointment\b", r"\boffice hours\b", r"\bT/Th\b", r"\bdue (on )?the dates\b", r"\b11:59\b",
    # course management: the site carries the subject, not the running of a section
    r"\bconsultation\b", r"\bGo or No-Go\b", r"\bGo/No-Go\b", r"\bcard station\b", r"\binstall clinic\b",
    r"\bhomework\b", r"\bthe Sprint (closes|is due|due)\b", r"\bSprint due\b", r"\bSPRINT \(", r"\bbook (your|a|on|it|them)\b",
    r"\bceremony slot\b", r"\bceremonies\b", r"\bWTClass\b", r"\bCanvas\b", r"\bsyllabus\b", r"\bgrade[sd]?\b", r"\bgrading\b",
    r"\bper ?cent of (the|your) (grade|course)\b", r"\blab (tonight|at six|handout|is self-guided|runs)\b", r"\bLab (tonight|at six)\b",
    r"\bself-guided\b", r"\bChase signs\b", r"\bsigns? (Go|GO)\b", r"\brun of show\b", r"\bminutes? of (framing|spine|teardowns?)\b",
    r"\b(Framing|Spine|Teardowns|Lens and card|Lab and Sprint)\s*·", r"\bBreak\s*·", r"\bFive minutes\b", r"\bTwo hours\b",
]), re.I)
# slides that are about running a session, not the subject: dropped from web decks and from the reader
DROP_TITLE = re.compile(r"(run of show|\bmoves\b|^Break\b|\bminutes\b|^Lab( tonight)?\b|^The Sprint\b|^Sprint\b|^Homework\b|^Tonight\b|^This week\b|^Next week\b|^Agenda\b|^Logistics\b|^Housekeeping\b|^Office hours\b|^Due\b|^Calendar\b|^Schedule\b)", re.I)

DROPLINE = re.compile(r"^\s*(\|\s*)?(Instructor checks moved off the slide|\[?verify\b|Source[s]?:|gzkit (facts|items) (are|must))", re.I)

REWRITE = [(r"\bTonight's claim\b", "This Evolution's design claim"), (r"\bTonight's\b", "This Evolution's"), (r"\btonight's\b", "this Evolution's"),
           (r"\bthis week's\b", "this Evolution's"), (r"\bThis week's\b", "This Evolution's"), (r"\bnext week\b", "the next Evolution"), (r"\blast week\b", "the previous Evolution")]
def rewrite(text):
    for a, b in REWRITE: text = re.sub(a, b, text)
    return text

def scrub_sentence_list(text):
    """Drop every sentence that carries schedule or instructor-only content."""
    text = rewrite(text)
    text = re.sub(r"\s*\[[Vv]erify[^\]]*\]", "", text)
    text = re.sub(r"\s*\[[^\]]*\bverify\b[^\]]*\]", "", text)
    sents = re.split(r"(?<=[.!?])\s+", text)
    keep = [x for x in sents if not SCHED.search(x)]
    return " ".join(keep).strip()

def scrub_line(l):
    l = rewrite(l)
    l = re.sub(r"\s*\[[^\]]*\bverify\b[^\]]*\]", "", l, flags=re.I)
    if DROPLINE.search(l): return ""
    if SCHED.search(l):
        # a bullet with a date: keep the part before the first ' · ' segment that leaks, else drop the line
        segs = [x for x in re.split(r"\s·\s|\s\|\s", l) if not SCHED.search(x)]
        return " · ".join(segs).strip()
    return l

def split_notes(t):
    t = t.replace("\r", "")
    m = re.search(r"\n*Cut from slide \d+[^\n]*:\s*\n", t)
    prose, cut = (t[:m.start()], t[m.end():]) if m else (t, "")
    paras = [scrub_sentence_list(p.strip()) for p in re.split(r"\s/\s|\n\s*\n", prose) if p.strip()]
    paras = [p for p in paras if p and not DROPLINE.search(p)]
    cuts = [scrub_line(re.sub(r"^\s*[-•]\s*", "", l).strip()) for l in cut.split("\n") if l.strip()]
    cuts = [c for c in cuts if c and len(c) > 2]
    return paras, cuts

def para_html(paras):
    return "".join("<p>%s</p>" % html.escape(p) for p in paras) or "<p class=\"small\">No notes for this slide.</p>"

def process(path, slug):
    s = open(path, encoding="utf-8").read()
    if '<section class="deck"' in s:
        return "web-native, skipped"
    s = re.sub(r'<style id="reader-css">.*?</style>\n?', "", s, flags=re.S)
    s = re.sub(r'<div class="notecur".*?</div></div>\n?', "", s, flags=re.S)
    s = re.sub(r'<section class="reader".*?</section>\n?', "", s, flags=re.S)
    s = re.sub(r'<script id="reader-js">.*?</script>\n?', "", s, flags=re.S)
    s = re.sub(r'<p class="small chapters"[^>]*>.*?</p>\n?', "", s, flags=re.S)
    s = s.replace(' <a class="dl" href="#read">Read</a>', "")
    # scrub the slide-text transcript too (it was partly scrubbed at build time; finish the job)
    def scrub_li(m):
        raw = m.group(1)
        plain = html.unescape(re.sub(r"<[^>]+>", " ", raw))
        if not (SCHED.search(plain) or DROPLINE.search(plain) or re.search(r"\[[^\]]*\bverify\b[^\]]*\]", plain, re.I)):
            return m.group(0)
        parts = [x for x in re.split(r"<br\s*/?>", raw) if x.strip()]
        kept = []
        for part in parts:
            t = html.unescape(re.sub(r"<[^>]+>", " ", part))
            cleaned = scrub_line(t)
            if cleaned: kept.append(html.escape(cleaned))
        return ("<li>%s</li>" % "<br>".join(kept)) if kept else ""
    s = re.sub(r'<li>(.*?)</li>', scrub_li, s, flags=re.S)
    pptx, evo = DECKS[slug]
    notes = NOTES[pptx]
    titles = re.search(r'const T=\[(.*?)\], N=T\.length', s, flags=re.S)
    n_page = s.count('class="slide-t"')
    if len(notes) != n_page:
        print("WARNING", slug, "page has", n_page, "slides; notes has", len(notes))
    per = [split_notes(t) for t in notes[:n_page]]
    # css
    i = s.find("</style>"); s = s[:i] + "</style>\n" + CSS + s[i+8:]
    # current-slide note under the viewer
    cur = '<div class="notecur" id="notecur" aria-live="polite"><div class="k">The lecture, written out · slide <span id="noteno">1</span></div><div id="notebody">%s</div></div>\n' % para_html(per[0][0])
    m = re.search(r'<p class="small" style="margin-top:10px">.*?</p>', s, flags=re.S)
    assert m, slug
    old_p = m.group(0)
    new_p = cur + '<p class="small" style="margin-top:10px">Arrow keys step through the slides. The panel above is the lecture written out for the slide on screen. <a href="#read">Read this lecture</a>, below, has the whole lecture in slide order, with each slide\'s full wording. Names and systems that appear without introduction are in the <a href="../../glossary/">glossary</a>.</p>'
    s = s.replace(old_p, new_p, 1)
    # Read link in the bar
    s = s.replace('<span class="count" id="count">', '<span class="count" id="count" role="status">')
    s = s.replace('<a class="dl" href="%s.pdf" download>PDF</a>' % slug, '<a class="dl" href="%s.pdf" download>PDF</a> <a class="dl" href="#read">Read</a>' % slug, 1)
    # chapters line under the header
    if evo:
        chs = TB.chapters_for_evo(evo)
        dirs = TB.main_dirs()
        links = " · ".join('<a href="../../textbook/%s/">Chapter %d</a> <span class="small">(%s)</span>' % (dirs[c], c, r) for c, r in chs if c in dirs)
        chap = '<p class="small chapters" style="margin:0 0 10px"><strong>Textbook:</strong> %s · <a href="../../glossary/">Glossary</a></p>\n' % links
        s = s.replace('<div class="viewer">', chap + '<div class="viewer">', 1)
    # reader section
    T = [html.unescape(x) for x in re.findall(r'aria-label="Slide \d+: ([^"]*)"', s)][:n_page]
    for k in range(len(per)):
        if k < len(T) and DROP_TITLE.search(T[k].strip()):
            per[k] = (["This slide covered how the session ran and is not part of the lecture."], [])
    blocks = []
    for k, (paras, cuts) in enumerate(per):
        if k < len(T) and DROP_TITLE.search(T[k].strip()): continue
        nn = "%02d" % (k+1)
        cut_html = ('<details><summary>The slide\'s wording in full</summary><ul>%s</ul></details>' % "".join("<li>%s</li>" % html.escape(c) for c in cuts)) if cuts else ""
        blocks.append('<div class="rslide" id="r%d"><div><button type="button" class="rthumb" data-i="%d" aria-label="Open slide %s in the viewer"><img loading="lazy" src="s-%s.webp" alt=""></button><div class="n">slide %s</div></div><div><h3>%s</h3>%s%s</div></div>' % (k+1, k, nn, nn, nn, html.escape(T[k] if k < len(T) else ""), para_html(paras), cut_html))
    reader = '<section class="reader" id="read" aria-label="Read this lecture"><h2>Read this lecture</h2><p class="lede small">The speaker notes follow here slide by slide. Under each slide is what the lecture says about it, and then the slide\'s own wording. Click a slide image to open it in the viewer above.</p>%s</section>\n' % "".join(blocks)
    s = s.replace('<section class="transcript"', reader + '<section class="transcript"', 1)
    # js: keep the current-slide panel in sync, and make reader thumbnails jump
    js = '<script id="reader-js">(function(){const N=%s;const $=i=>document.getElementById(i);function show(k){if(!N[k])return;$("noteno").textContent=k+1;$("notebody").innerHTML=N[k];}const c=$("count");new MutationObserver(()=>{const k=parseInt(c.textContent)-1;show(k);}).observe(c,{childList:true,characterData:true,subtree:true});show(parseInt(c.textContent)-1);document.querySelectorAll(".rslide .rthumb").forEach(im=>im.addEventListener("click",()=>{const b=document.querySelector(\'#strip button[data-i="\'+im.dataset.i+\'"]\');if(b){b.click();$("stage").scrollIntoView({behavior:"smooth",block:"start"});}}));})();</script>\n' % json.dumps([para_html(p) for p, c in per])
    s = s.replace("</body></html>", js + "</body></html>")
    open(path, "w", encoding="utf-8").write(s)
    return len(per)

def main(docs):
    for slug in DECKS:
        p = pathlib.Path(docs) / "lectures" / slug / "index.html"
        if p.exists(): print(slug, process(str(p), slug), "slides")

if __name__ == "__main__":
    main(sys.argv[1])
