# Cut-section brief (supplements BRIEF.md; read BRIEF.md first)

The speaker notes for each lecture end with "Cut from slide N (full wording):" sections. They hold the slide's text in its full, untrimmed form, and the site publishes them under "The slide's wording in full". They were co-written with AI and still carry em dashes, "names" as a verb, "the claim" framing, antithesis closers, and schedule asides. Run the full chain on them (humaniser, ste-voice, scholarly-voice, humaniser battery check). Slide register: short, complete sentences or labelled fragments, each with an actor and a mechanism where it states a judgment.

## File

`/home/claude/site/tools/review/voice-pass/cut/<slug>.json` : an object whose keys are slide indexes and whose values are the full cut text for that slide. Edit the values in place with the Edit tool. Keep valid JSON (check: `python3 -c "import json,sys; json.load(open(sys.argv[1]))" <file>`).

## Rules

- Never change keys. Keep the first line of each value exactly ("Cut from slide N (full wording):"). Keep the line structure: lines starting with "- ", and the " / " separators between paragraphs inside a line (they mark slide paragraph breaks; " /  / " marks a blank paragraph). Do not merge or split lines.
- Remove every em dash (comma, colon, parentheses, or a new sentence). The only exception is the gzkit status "Completed — Partial", which stays verbatim.
- "names/named/naming" as a verb or modifier goes ("A PRD that names a framework" → "A PRD that specifies a framework"); the noun ("field names", "span names", "tool names") stays.
- "the claim" as a thesis stand-in goes; "typed claim", "design claim", and a flight card's claim (the sortie's falsifiable sentence) stay. The adversary's CLAIM/EVIDENCE prompt text is code and stays.
- Schedule lines: dates, clock times ("4:00–5:00", "0:55–1:00"), rooms ("CC209"), "tonight", "this week", "next week", "last week", Canvas/WTClass, Discord, Calendly, "Break", "Lab" timing lines: delete the schedule fragment but keep any substantive content on the same line (for example "Break · 0:55–1:00 Pick one check in your repository..." keeps "Pick one check in your repository..."). If a whole line is only schedule, replace it with an empty string after "- " is not allowed; instead delete the whole line including its newline.
- Bracketed notes such as "[Summarized from ... verify ...]" and "[verify]" stay as they are (the build drops them).
- Code, commands, file paths, JSON, field names, URLs, numbers, citation dates, quoted text, and proper names stay exactly.
- Do not drop a fact, a condition, or a scope qualifier.

## Report

Write `/home/claude/site/tools/review/voice-pass/cut-<slug>.md` (counts, dominant patterns with two or three before/after pairs, closer list check result). Report back in under 150 words, quoting anything you were unsure about.
