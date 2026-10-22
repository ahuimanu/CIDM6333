#!/usr/bin/env python3
"""Build docs/glossary/ and link glossary terms from the lecture pages.

- docs/glossary/index.html: every named thing, grouped by kind, with what / who-when / why in the course / source / chapters.
- each lecture page: a "Names on these slides" panel under the header, and the first mention of each term in every
  transcript block and reader block linked to its entry. Idempotent.

Usage: python3 glossary.py <docs-dir>
"""
import re, sys, html, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import glossary_data as GD
import textbook as TB

HERE = pathlib.Path(__file__).parent
HEAD = (HERE / "page-head.html").read_text(encoding="utf-8")
CATS = [("course", "Course vocabulary"), ("harness", "Harnesses and their parts"), ("protocol", "Protocols and standards"),
        ("system", "Systems, frameworks, and papers that built them"), ("org", "Organizations"),
        ("bench", "Benchmarks and evaluation"), ("paper", "Papers and books"), ("method", "Methods and general terms")]
# aliases too generic to auto-link in prose (they still count for the names panel only if distinctive)
NOLINK = {"model", "token", "tokens", "loop", "the loop", "Go", "hash", "brief", "briefs", "scope", "host", "hosts", "Claude", "window",
          "the window", "context", "agent", "Agent", "agents", "tool", "tools", "Tools", "judge", "Judge", "trace", "traces", "span", "spans",
          "lock", "locks", "schema", "schemas", "embedding", "embeddings", "workflow", "workflows", "worker", "controller", "reviewer",
          "implementer", "verdict", "permission", "plugin", "plugins", "hook", "skill", "subagent", "subagents", "Subagents", "handoff",
          "handoffs", "rollback", "Release", "canary", "attention", "halt", "Halt", "language model", "local model", "open-weight",
          "persona", "personas", "retriever", "Retention", "evict", "recall", "canon", "CANON", "DERIVED", "L1", "L2", "L3", "lane", "Lane",
          "Lite", "Heavy", "Gate", "Gates", "Expansion", "envelope", "Wang", "RED", "Zen", "REST", "HTTP", "API", "SDK", "SDKs", "CLI",
          "mandates", "injection", "Injection", "baseline", "delta gate", "closeout", "Closeout", "Drift", "Sprint", "Drifts", "The Sprint",
          "E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10", "E11", "E12", "Evolutions", "Sorties", "Park", "Yao",
          "layers of truth", "red witness", "second-family adversary", "adversary", "pytest", "uv run pytest", "Pydantic", "Zod",
          "Agent Skills", "skill tool", "progressive disclosure", "side-effect class", "function calling", "tool call", "custom tool", "custom tools",
          "rules file", "instruction file", "instruction files", "supervisor", "membrane", "ask on bash", "edit: deny", "permission gate",
          "compaction", "compacted", "harness", "harnesses", "harness engineering", "sha256", "hash-pin", "jsonl", "five patterns",
          "orchestrator-workers", "evaluator-optimizer", "agent loop", "retention rule", "dispatch record", "dispatch records", "squawks",
          "Attestations", "attestations", "attestation", "repudiation", "receipts", "Receipts", "ledger", "the ledger", "ledger.jsonl",
          "index zero", "Index Zero", "Degradation", "covenant", "the covenant", "judgment loop", "preservation mechanism", "Preservation",
          "flight log", "Flight log", "flight cards", "falsifiers", "Falsifiers", "Teardowns", "Design Analyses", "nine components",
          "failure modes", "nine modes", "laundering", "expansion card", "Exceptional mark", "Chase review", "CHASE", "opencode", "TUI",
          "Agent Card", "performative", "performatives", "pass@k", "position bias", "self-preference", "circuit breaker", "code freeze",
          "LLM-as-a-judge", "elicitation", "server registry", "host", "regression delta", "golden.jsonl", "memory.jsonl", "memory-ledger.jsonl",
          "retain_until", "docs/prd.md", "B-07", "ADRs", "Gate 4", "Gate 5", "Gate-4", "Gate-5", "FC2", "FC3", "DESIGN CLAIM", "ENVELOPE",
          "TEST POINTS", "INSTRUMENTATION", "ENTRY CONDITIONS", "SYSTEMS UNDER TEST", "SUBSTRATE", "PRE-REGISTERED FALSIFIERS",
          "Corner of the envelope", "Center of the envelope", "chain-of-thought", "Claude Code subagents", "Route B", "Path A", "Path B",
          "PASS", "FAIL", "CONCERNS", "DONE", "BLOCKED", "plan, do, check", "Plan, do, check", "anti-traits", "anti-trait", "GovZero", "gz",
          ".gzkit", "gz status", "gz arb red", "prompt injection", "tool poisoning", "Streamable HTTP", "FastMCP", "Python SDK", "GitHub MCP",
          "MCP server", "MCP servers", "StateGraph", "interrupt()", "checkpointer", "Devin", "Yan", "Smallville", "Berkeley", "Vaswani",
          "o-series", "GPT-4", "ChatGPT", "Codex CLI", "Codex cloud", "OpenAI Agents SDK", "Claude Agent SDK", "Copilot", ".cursor/rules",
          "opencode.json", "opencode/big-pickle", "Big Pickle", "OpenCode Go", "OpenCode Zen", "multi-agent research system",
          "Building Effective Agents", "Agentic AI Foundation", "Why Do Multi-Agent LLM Systems Fail", "Cemri", "Attention Is All You Need",
          "Nygard", "Zheng", "Panickssery", "Wataoka", "Gorilla", "MemGPT", "Letta", "LangGraph", "LangSmith", "Agent-to-Agent", "A2A v1.0",
          "OAuth", "PKCE", "PAT", "JSON-RPC 2.0", "OWASP Top 10", "Belief–Desire–Intention", "BDI agents", "Russell", "Norvig", "AIMA",
          "Contract net (Smith; FIPA)", "contract net", "FIPA-ACL", "Model Context Protocol", "Retrieval-Augmented Generation", "embeddinggemma",
          "SessionStart", "PreToolUse", "PostToolUse", "PreCompact", "CLAUDE.md", "agents.md", "SKILL.md", "tool.execute.before", "handoff.md",
          "recall.py", "VIBES", "V.I.B.E.S", "App. C", "Appendix C", "GZK-GOV-007", "ADR-0.0.71", "ADR-0.0.74", "ADR-0.18.0", "ADR-1", "ADR-2",
          "Sortie 1", "Sortie 7", "Sortie 8", "Sortie 9", "Sortie 10", "Sortie 11", "Flight Card 1", "Flight Card 7", "Flight Card 8",
          "Flight Card 10", "Flight Card", "The Chase", "Your Chase", "No-Go", "NO-GO", "Go/No-Go", "The Final System", "closeout ceremony",
          "Zero Doctrine", "Live Design Analysis", "Design Analysis Ledger", "ReviewResults", "Tree of Thoughts", "ToT", "CoT",
          "Chatbot Arena", "MT-Bench", "SWE-agent", "Agentless", "Agent Card", "Berkeley group"}
# Terms that ARE linked in prose: the entry term itself plus these distinctive aliases
LINK_EXTRA = {"FIPA", "BDI", "PEAS", "ReAct", "MetaGPT", "CAMEL", "AutoGen", "CrewAI", "LangGraph", "LangChain", "LangSmith", "Langfuse",
              "MemGPT", "Letta", "Toolformer", "Reflexion", "Generative Agents", "AutoGPT", "BabyAGI", "MCP", "A2A", "AP2", "OWASP", "OAuth",
              "PKCE", "JSON-RPC", "JSON Schema", "OpenAPI", "AGENTS.md", "CLAUDE.md", "Claude Code", "Codex", "Cursor", "Copilot", "Gemini CLI",
              "OpenCode", "Big Pickle", "Ollama", "Pydantic AI", "SWE-bench", "SWE-agent", "Agentless", "HumanEval", "GAIA", "WebArena",
              "ToolBench", "Gorilla", "MT-Bench", "Chatbot Arena", "BLEU", "MAST", "Cemri", "Zheng", "Panickssery", "Wataoka", "Nygard",
              "Degani", "Transformer", "Vaswani", "Anthropic", "OpenAI", "Cognition", "Invariant Labs", "Linux Foundation", "gzkit", "GovZero",
              "Sortie", "Chase", "Flight card", "Flight Card", "Evolution", "Design Analysis", "Teardown", "Final System", "Degradation Pattern",
              "Zero Doctrine", "index zero", "Index zero", "ledger", "Ledger", "receipt", "Receipt", "attestation", "Attestation", "HandoffResult",
              "ReviewResult", "RED witness", "V.I.B.E.S.", "ADR", "PRD", "OBPI", "squawk", "Squawk", "falsifier", "Falsifier", "falsifiers",
              "Go/No-Go", "No-Go", "Tree Hollow", "covenant", "Covenant", "five gates", "Five gates", "Gate 5", "Gate 4", "layers of truth",
              "Layers of truth", "compaction", "Compaction", "handoff", "Handoff", "recall.py", "SKILL.md", "skills", "Skills", "hooks", "Hooks",
              "PreToolUse", "PostToolUse", "SessionStart", "PreCompact", "permissions", "Permissions", "Contract net", "contract net", "Exceptional",
              "Route A", "Route B", "summary laundering", "Summary laundering", "persona", "Persona", "TDD", "BDD", "golden set", "Golden set",
              "RAG", "TTL", "JSONL", "SHA-256", "red team", "Red team", "rollback", "Rollback", "MAST", "Berkeley group", "judge biases",
              "Judge biases", "Agentic AI", "LLM", "SDK", "Sprint and Drift", "Smallville", "Agent Card", "Chain-of-thought", "chain-of-thought",
              "Tree of Thoughts", "Harness", "harness"}

def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")

ENTRIES = GD.E
for e in ENTRIES: e["slug"] = slug(e["term"])

def link_terms():
    """(pattern text, slug) pairs for prose linking, longest first."""
    pairs = []
    for e in ENTRIES:
        names = {e["term"]} | set(e["aliases"])
        for n in names:
            if n in LINK_EXTRA or n == e["term"]:
                if n in NOLINK and n != e["term"]: continue
                pairs.append((n, e["slug"]))
    pairs.sort(key=lambda p: -len(p[0]))
    return pairs

def panel_terms():
    """(pattern text, entry) for detecting which entries a deck mentions (distinctive names only)."""
    pairs = []
    for e in ENTRIES:
        for n in {e["term"]} | set(e["aliases"]):
            if len(n) >= 4 and (n[0].isupper() or any(ch in n for ch in "./-")) and n not in {"Agent", "Tools", "Judge", "Claude", "Release", "Halt", "Expansion", "Lite", "Heavy", "Gate", "Gates", "Lane", "Injection", "Corner", "Center", "Wang", "Park"}:
                pairs.append((n, e))
    pairs.sort(key=lambda p: -len(p[0]))
    return pairs

def boundary(pat):
    esc = re.escape(pat)
    lead = r"(?<![\w./-])" if pat[0].isalnum() else ""
    trail = r"(?![\w-])" if pat[-1].isalnum() else ""
    return lead + esc + trail

def link_block(block_html, pairs, href_prefix):
    """Link the first occurrence of each term inside the text nodes of one block."""
    done = set()
    parts = re.split(r"(<[^>]+>)", block_html)
    for pi, part in enumerate(parts):
        if part.startswith("<") or not part.strip(): continue
        for pat, sl in pairs:
            if sl in done: continue
            m = re.search(boundary(pat), part)
            if m:
                part = part[:m.start()] + '<a class="gl" href="%s#%s">%s</a>' % (href_prefix, sl, m.group(0)) + part[m.end():]
                done.add(sl)
        parts[pi] = part
    return "".join(parts)

def entry_html(e, depth_prefix):
    chs = ""
    if e["ch"]:
        dirs = TB.main_dirs()
        chs = " · ".join('<a href="%stextbook/%s/">Chapter %d</a>' % (depth_prefix, dirs[c], c) for c in e["ch"] if c in dirs)
    src = e["src"]
    if src.startswith("http"): src = '<a href="%s">%s</a>' % (src, html.escape(src))
    elif "http" in src:
        src = re.sub(r"(https?://\S+)", r'<a href="\1">\1</a>', html.escape(src))
    else: src = html.escape(src)
    rows = ['<p>%s</p>' % html.escape(e["what"])]
    if e["when"]: rows.append('<p class="gk"><b>Who, when.</b> %s</p>' % html.escape(e["when"]))
    if e["why"]: rows.append('<p class="gk"><b>Why it is in the course.</b> %s</p>' % html.escape(e["why"]))
    if src: rows.append('<p class="gk"><b>Read more.</b> %s</p>' % src)
    if chs: rows.append('<p class="gk"><b>Textbook.</b> %s</p>' % chs)
    al = [a for a in e["aliases"] if a.lower() != e["term"].lower()][:8]
    alias = ('<p class="gk small">Also appears as: %s</p>' % html.escape(" · ".join(al))) if al else ""
    return '<div class="gentry" id="%s"><h3>%s</h3>%s%s</div>' % (e["slug"], html.escape(e["term"]), "".join(rows), alias)

GCSS = """<style>
.gtoc{display:flex;flex-wrap:wrap;gap:6px 14px;margin:10px 0 24px;font-family:var(--display);font-weight:600;font-size:15px;letter-spacing:.04em}
.gtoc a{color:var(--accent-ink);text-decoration:none}
.gentry{padding:14px 0;border-top:1px solid var(--line)}
.gentry h3{margin:0 0 6px}
.gentry p{margin:6px 0;max-width:80ch}
.gentry .gk{font-size:15px;color:var(--ink-2)}
.gentry .gk b{font-family:var(--display);font-weight:600;letter-spacing:.05em;color:var(--ink)}
.gentry:target{background:var(--accent-soft);margin-inline:-14px;padding-inline:14px;border-radius:10px}
article{max-width:900px}
</style>"""

def build_glossary(docs):
    out = pathlib.Path(docs) / "glossary"; out.mkdir(exist_ok=True)
    toc = '<div class="gtoc">' + "".join('<a href="#cat-%s">%s</a>' % (c, n) for c, n in CATS) + "</div>"
    body = ['<h1>Glossary</h1><p class="lede">Every name that the lectures use without stopping to introduce it: systems, papers, protocols, companies, and the course\'s own vocabulary. Each entry says what the thing is, who made it and when, why it is in this course, and where to read more. Lecture transcripts link here on a term\'s first mention; each lecture page lists the names on its slides.</p>', toc]
    for c, n in CATS:
        es = sorted([e for e in ENTRIES if e["cat"] == c], key=lambda e: e["term"].lower())
        if not es: continue
        body.append('<h2 id="cat-%s">%s</h2>' % (c, n))
        body += [entry_html(e, "../") for e in es]
    body.append('<p class="small" style="margin-top:28px">%d entries. Dates and attributions were checked against the lecture decks and the sources named; corrections go to the instructor.</p>' % len(ENTRIES))
    page = HEAD.replace("{{TITLE}}", "Glossary · CIDM 6333") + GCSS + '\n<div class="wrap"><nav class="crumbs"><a href="../">CIDM 6333</a> · Glossary</nav><div class="eyebrow">CIDM 6333 · Agentic Systems · Glossary</div><article>' + "".join(body) + '</article><footer>CIDM 6333 · Glossary · Fall 2026</footer></div>\n</body></html>\n'
    (out / "index.html").write_text(page, encoding="utf-8")
    print("glossary:", len(ENTRIES), "entries")

LCSS = """<style id="gl-css">
a.gl{color:inherit;text-decoration:none;border-bottom:1px dotted var(--accent);}
a.gl:hover{color:var(--accent-ink);border-bottom-style:solid}
.names{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:12px 18px;margin:0 0 14px}
.names summary{cursor:pointer;list-style:revert}
.names .k{font-family:var(--display);font-weight:600;letter-spacing:.1em;text-transform:uppercase;font-size:12px;color:var(--accent-ink);margin-bottom:6px}
.names ul{list-style:none;margin:8px 0 0;padding:0;display:flex;flex-wrap:wrap;gap:4px 14px;font-size:15px}
.names li a{color:var(--ink);text-decoration:none;border-bottom:1px dotted var(--accent)}
.names li span{color:var(--ink-2)}
</style>"""

def link_lecture(path):
    s = open(path, encoding="utf-8").read()
    s = re.sub(r'<style id="gl-css">.*?</style>\n?', "", s, flags=re.S)
    s = re.sub(r'<details class="names">.*?</details>\n?', "", s, flags=re.S)
    s = re.sub(r'<div class="names">.*?</ul></div>\n?', "", s, flags=re.S)
    s = re.sub(r'<ul><li><a href="\.\./\.\./glossary/#[^"]*">.*?</ul></div>\n?', "", s, flags=re.S)
    s = re.sub(r'<a class="gl" href="[^"]*">(.*?)</a>', r"\1", s)
    s = re.sub(r'<a class=\\"gl\\" href=\\"[^"]*\\">(.*?)</a>', r"\1", s)  # inside the JSON array
    pairs = link_terms()
    href = "../../glossary/"
    # link inside transcript blocks and reader blocks
    def relink(m):
        return link_block(m.group(0), pairs, href)
    s = re.sub(r'<div class="slide-t".*?</div></div>', relink, s, flags=re.S)
    s = re.sub(r'<div class="rslide".*?</div></div>', relink, s, flags=re.S)
    # the current-slide panel: its paragraphs live in a JSON array inside <script id="reader-js">
    def relink_json(m):
        import json as _j
        arr = _j.loads(m.group(2))
        arr = [link_block(x, pairs, href) for x in arr]
        return m.group(1) + _j.dumps(arr) + m.group(3)
    s = re.sub(r'(<script id="reader-js">\(function\(\)\{const N=)(\[.*?\])(;const \$=)', relink_json, s, flags=re.S)
    # names panel: entries mentioned anywhere in transcript+reader text
    text = html.unescape(re.sub(r"<[^>]+>", " ", " ".join(re.findall(r'<section class="(?:transcript|reader)".*?</section>', s, flags=re.S))))
    found = {}
    for pat, e in panel_terms():
        if e["slug"] in found: continue
        if re.search(boundary(pat), text): found[e["slug"]] = e
    if found:
        items = sorted(found.values(), key=lambda e: (CATS.index(next(c for c in CATS if c[0] == e["cat"])), e["term"].lower()))
        lis = "".join('<li><a href="%s#%s">%s</a> <span>· %s</span></li>' % (href, e["slug"], html.escape(e["term"]), html.escape(first_clause(e["what"]))) for e in items)
        panel = '<details class="names"><summary class="k">Names on these slides · %d · each links to the glossary</summary><ul>%s</ul></details>\n' % (len(items), lis)
        s = s.replace('<div class="viewer">', panel + '<div class="viewer">', 1)
    i = s.find("</style>"); s = s[:i] + "</style>\n" + LCSS + s[i+8:]
    open(path, "w", encoding="utf-8").write(s)
    return len(found)

def first_clause(t):
    t = re.split(r"[.;:]", t)[0]
    return (t[:90] + "…") if len(t) > 90 else t

def main(docs):
    build_glossary(docs)
    for p in sorted((pathlib.Path(docs) / "lectures").glob("*/index.html")):
        if p.parent.name == "mini-steer-the-middle": continue
        print(p.parent.name, link_lecture(str(p)), "names")

if __name__ == "__main__":
    main(sys.argv[1])
