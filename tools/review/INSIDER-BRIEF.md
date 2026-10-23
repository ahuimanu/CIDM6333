# Sweep: reader-facing wording (Oct 23, 2026)

The course site (CIDM 6333, Jeffry Babb) is read by students. Some text addresses the author or describes how the material was produced instead of telling the reader something useful. Find and fix it in your files. Edit in place with the Edit tool.

## What counts as insider text (fix it)

- Production notes: "the deck marks these names for verification", "Table text is the deck's", "the figure uses the deck's shorter observation", "What this redraw adds or changes", "made up to show the pattern" (keep the fact that numbers are illustrative, state it plainly: "The numbers are illustrative."), "[verify]", "not yet located", "to be added", "the outline lists", "gzkit facts come from the course topic guide only", "the repository is the authority where the two differ".
- References to "the deck" as a source document. A student does not know what "the deck" is. Say "the E3 lecture" (or "the lecture") when the point is where the student met the idea; otherwise drop the attribution and state the fact.
- Self-description of the page or apparatus ("this page", "this figure draws", "the build", "the pass") when it tells the reader nothing they can use. A plain instruction ("Step with Next and Back") is fine.
- "we"/"our" meaning the author and an AI.
- Instructor-only remarks ("the instructor's mapping", "for the instructor").

## Rules

1. Never add a fact, number, date, name, or citation. Rewording only. If a sentence has no reader value once the production note is removed, delete it.
2. Keep citations, URLs, retrieval dates ("retrieved September 24, 2026"), quotations, code, and course vocabulary.
3. Keep source attributions that help the reader find or weigh a claim ("Anthropic's post reports..."). Only remove attributions to the course's own production files.
4. House style: no em dashes (a normal hyphen is fine), "names" not as a verb, no dates/times/rooms/LMS references.
5. HTML: change text only; keep tags, attributes, ids, classes, SVG geometry, and JavaScript working (strings inside JS arrays/objects may be edited, keep quotes and escaping valid). After editing a page, check it parses and its script still runs if you can (node --check on extracted script is fine).

## Report

Append a short log to `/home/claude/site/tools/review/insider-sweep.md` under a heading for your scope: counts and five before/after examples. Report back in under 120 words.
