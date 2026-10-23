#!/usr/bin/env python3
"""Make every web address on the site a working link that opens in a new window.

1. Bare URLs in page text (reading list, textbook, lecture notes, glossary) become
   <a href="..." target="_blank" rel="noopener">...</a>. Text inside <a>, <code>, <pre>,
   <script>, <style>, <textarea> and tag attributes is left alone.
2. Every existing link to another site (http/https, not the course site itself) gets
   target="_blank" rel="noopener".

Idempotent. Run after nav.py and brand.py. Usage: python3 linkify.py <docs-dir>
"""
import re, sys, pathlib, html

SITE = "ahuimanu.github.io/CIDM6333"
URL = re.compile(r"""https?://[^\s<>"'()\[\]]+[^\s<>"'()\[\].,;:!?]""")
SKIP = {"a", "code", "pre", "script", "style", "textarea", "title", "svg"}
TAG = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)\b[^>]*?(/?)>", re.S)

def link(m):
    u = m.group(0)
    href = html.unescape(u)
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (html.escape(href, quote=True), u)

def autolink(s):
    out, pos, stack = [], 0, []
    for m in TAG.finditer(s):
        text = s[pos:m.start()]
        out.append(text if stack else URL.sub(link, text))
        out.append(m.group(0))
        closing, name, selfclose = m.group(1), m.group(2).lower(), m.group(3)
        if name in SKIP and not selfclose:
            if closing:
                if stack and stack[-1] == name: stack.pop()
            else:
                stack.append(name)
        pos = m.end()
    tail = s[pos:]
    out.append(tail if stack else URL.sub(link, tail))
    return "".join(out)

def external_targets(s):
    def fix(m):
        tag = m.group(0)
        href = re.search(r'href="(https?://[^"]+)"', tag)
        if not href or SITE in href.group(1) or "target=" in tag: return tag
        return tag[:-1] + ' target="_blank" rel="noopener">'
    return re.sub(r"<a\b[^>]*>", fix, s)

def main(docs):
    n = 0
    for p in pathlib.Path(docs).rglob("*.html"):
        s = p.read_text(encoding="utf-8")
        t = external_targets(autolink(s))
        if t != s:
            p.write_text(t, encoding="utf-8"); n += 1
    print("linkify: pages changed:", n)

if __name__ == "__main__":
    main(sys.argv[1])
