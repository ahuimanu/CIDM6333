# Voice pass brief (Oct 22, 2026)

You are revising prose that Claude drafted for Jeffry Babb's CIDM 6333 course site (Agentic Systems Design and Development, West Texas A&M). Jeffry flagged the prose as carrying AI register ("'claim' and 'the move' language are AI reek"). Run his voice chain over the file(s) assigned to you, editing in place.

## The chain, in this order

1. **humaniser** (full pass): `/root/.claude/skills/synced/5be94afe-931f-4e50-9eb7-2c854097b334_977856c7-71a7-4075-bc14-9b42ecb2650e/humaniser/SKILL.md`. Read it and `references/shape-patterns.md` (the shape battery) before editing. Patterns 29 to 40 matter most here: epigram landings (#36), definition-colon ledes (#35), invented authority (#37), templated siblings (#38), talking-about instead of instructing (#40), actor removal (#3, #5, #31).
2. **ste-voice**: `/root/.claude/skills/synced/5be94afe-931f-4e50-9eb7-2c854097b334_977856c7-71a7-4075-bc14-9b42ecb2650e/ste-voice/SKILL.md`. Course register. Procedures, numbered steps, step tables, file lists: imperative verb, one instruction per sentence, about 20 words, no semicolons. Explanatory paragraphs: rules 1 to 4 only (one term per object, concrete subject in judgment sentences, no gerund or nominalization subjects, noun clusters of three words at most); no length ceiling there. The checker is `scripts/ste_check.py <file>` in that directory (run it on plain text you extract; inspect its lines, do not obey them blindly).
3. **scholarly-voice**: `/root/.claude/skills/synced/5be94afe-931f-4e50-9eb7-2c854097b334_977856c7-71a7-4075-bc14-9b42ecb2650e/scholarly-voice/SKILL.md`. Course register: flat declaratives with the reason attached in the same or next sentence; terms stipulated at first use; concede-then-answer only where a real objection exists; headings label, they do not argue; no encouragement closers; derive significance, never assert it. This pass runs last and sets the final surface: full sentences, not a parts list.
4. **humaniser battery, check only**: rerun the greps and the shape battery on the result. Fix what it flags in place. Do not redraft. Produce the self-audit artifacts: closer list (last sentence of every paragraph/caption, out of context), lede list (first sentence of every section/panel), claim list (any "most", "every", "usually", "often", "the one most often" frequency claim; each needs a source or goes).

## House rules that win every conflict

- No em dashes anywhere (use commas, parentheses, a colon, or a new sentence).
- "names"/"named"/"naming" as a verb or modifier is banned ("the figure names three things" → "the figure lists three things"). The noun "name" is fine.
- No "not X but Y" / "not X. It is Y." cadence as a closer; no antithesis morals; no pseudo-cleft reveals ("What matters is..."; "The point is..."); no word echoes; no mirrored pairs for rhythm; no rule-of-three for rhythm (a list has the count the material has).
- "claim" as a stand-in for a lecture's thesis ("Tonight's claim", "The claim:", "the lecture's claim") is the AI reek Jeffry flagged. Replace with the statement itself, stated flat, or with "argues that". **Exception: "typed claim" and "design claim" are Jeffry's own course vocabulary and stay exactly as written.** "A claim without a receipt is not evidence" is also his (gzkit) and stays. Likewise "receipt", "verdict", "ledger", "gate", "harness", "sortie", "flight card", "Chase", "Evolution", "Sprint", "Drift", "falsifier", "REFUTED/NOT-REFUTED", "Index zero", "Degradation Pattern", "V.I.B.E.S." stay.
- "the move" meaning a step or action is AI reek. Say the action: who does what to what, by what mechanism.
- Text in quotation marks that quotes a paper, a slide, gzkit, or Jeffry is never edited. Citations, URLs, file names, code, commands, JSON, numbers, dates, and proper names are never edited.
- Do not drop a fact, a condition, or a scope qualifier to satisfy a rule. Do not flatten explanation into a parts list.
- No chat artifacts, no "we", no first-person feeling or tangents (the humaniser's "add soul" guidance is essay advice; decline it here). "I" only where the instructor speaks about a decision.
- No QA or management asides ("checked 10/22/2026", schedule/time/room details, "tonight", "this week"). "this Evolution" is the allowed stand-in for "tonight".
- Keep the register plain academic English (Allen Lee): "for this reason", "in other words" at joints where a second formulation adds precision, parentheses for the second track (an example, a pointer, a qualification).

## Mechanics

- Edit the file(s) in place with the Edit tool. Keep every HTML tag, attribute, id, class, `data-*`, `href`, `<script>`, `<style>`, SVG geometry, and JSON array exactly as is; change only the human-readable text. In SVG `<text>`/`<tspan>` labels, keep the new label within about the same character count as the old (layout is fixed-width); leave labels alone unless they carry one of the banned shapes.
- In Python files, change only string literals; the file must still import (`python3 -c "import ast,sys;ast.parse(open(sys.argv[1]).read())" <file>`). Keep the `g(...)` call shapes and all keyword arguments.
- After editing HTML, confirm it still parses and the tag count is unchanged: `python3 - <<'EOF'` with `html.parser` counting start tags before and after (keep a copy of the original first).
- Run the scholarly-voice grep battery on the finished file and leave nothing flagged unless it sits inside a quotation or a proper name.
- Write a pass log to `/home/claude/site/tools/review/voice-pass/<slug>.md`: what you changed and why (grouped by pattern, with a few before/after pairs), the three self-audit artifacts after the final pass, every ste_check line you declined and why, and any sentence you left long with the reason.
- Report back in under 300 words: files changed, count of edits, the patterns that dominated, anything you were unsure about (quote it).
