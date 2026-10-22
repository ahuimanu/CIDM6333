# Deck brief (supplements BRIEF.md; read BRIEF.md first)

Jeffry's lecture decks were co-written with AI, so their slide wording and speaker notes get the full chain (humaniser, ste-voice, scholarly-voice, humaniser battery check). You are assigned one deck. Two JSON files carry its text; edit the values in place and keep both files valid JSON (check with `python3 -c "import json,sys; json.load(open(sys.argv[1]))" <file>`).

## 1. Slide wording: `/home/claude/site/tools/sitekit/voice/<slug>.json`

An object whose keys are every paragraph (and table cell) extracted from the pptx, and whose values start out identical to the keys. The build applies `value` wherever the pptx paragraph equals `key`. Rules:

- Never change a key. Change only values. A value identical to its key means "unchanged".
- Keep slide titles, panel headings, chip labels, and other short labels close to their original length (the slide layout is fixed). Reword them only when they carry a banned shape (a "claim:" framing, "the move", an argued heading, an em dash).
- Code, commands, file paths, JSON, schema fields, URLs, numbers, dates, citations, and quoted material stay exactly as they are. Keys that are footers, page numbers, timings ("0:00", "4:00–4:05"), or session-running lines (run of show, break, lab, Sprint due) are dropped by the build; leave them unchanged.
- Body paragraphs on slides are read from the screen, so they stay short, but every sentence gets an actor and a mechanism, and the house bans apply (no em dashes; "names" as a verb; "the claim"/"Tonight's claim" framing goes, the statement stands on its own; "the move" goes; no antithesis closers; no rule-of-three for rhythm).
- "typed claim", "design claim", and the other course vocabulary listed in BRIEF.md stay.

## 2. Speaker notes: `/home/claude/site/tools/review/voice-pass/notes/<slug>.json`

A JSON array with one string per slide: the lecture as spoken, written out, which the site publishes as "Read this lecture" and as the per-slide panel under the viewer. Rules:

- Edit the lecture prose paragraphs. This is the main body of the work. Register: scholarly-voice course register (full sentences, terms stipulated when first used, reasons attached, derivation rather than asserted significance, concede-then-answer where a real objection exists); STE rules 1 to 4 (one term per object, concrete subject in judgment sentences, no gerund or nominalization subjects, noun clusters of three words at most). No "tonight", "this week", "next week", times, rooms, Canvas/WTClass, Discord, grading, homework, or Sprint due lines: the build strips these, but remove them at source when you meet them in a sentence you are rewriting, replacing "tonight" with "this Evolution" or dropping it.
- Leave bracketed timing marks such as "[0:00–0:02]" exactly where they are.
- Leave every "Cut from slide N (full wording):" section and the lines under it untouched (they mirror the slide wording and are handled from file 1).
- Leave the paragraph breaks ("\n\n") as they are; do not merge or split slides.
- Keep JSON escaping valid (quotes inside strings escaped, no raw newlines outside "\n").

## Pass log

Write `/home/claude/site/tools/review/voice-pass/deck-<slug>.md` with: counts (keys changed, notes paragraphs changed), the patterns that dominated with a few before/after pairs, the three self-audit artifacts (closer list, lede list, claim list) for the notes after the final pass, and anything you left as is with the reason. Report back in under 250 words.
