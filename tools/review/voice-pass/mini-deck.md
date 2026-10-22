# Voice pass log: mini-deck (Steer the Middle mini lecture)

File: /home/claude/site/docs/lectures/mini-steer-the-middle/index.html (15 slides, no speaker-notes array, no glossary `<a class="gl">` tags present).
Edits: 30 Edit calls over 13 slides. Tag count 432 before and after; file parses with html.parser. No em dashes, no "names" as verb, no "the move", no "claim" outside "typed claim" (kept).

## Changes by pattern

### QA and management asides ("tonight", "last week", "checked" dates)
Eleven occurrences of "tonight"/"night", two of "last week", one dated footer.
- "Mini lecture · Evolution 8 · follow-along night" → "... follow-along session"
- "Tonight's exercise walks the figure left to right" → "This Evolution's exercise walks the figure from left to right"
- "E8 · the thing you build tonight" → "E8 · what you build in this exercise"
- "Two of last week's three drawers" → "Two of the three drawers from the previous Evolution"
- "last week's Probe 3 question" → "the previous Evolution's Probe 3 question"
- footer "OpenCode docs, checked 10/22/2026" → "OpenCode docs" (the brief lists this exact shape as an aside; the date is the only one dropped)
- "(an addition; not tonight)" → "(an addition, not in this exercise)"
Kept: the hour-two step timings (0–5, 5–9 ...) and "At 35 minutes"/"At 55 minutes", because they are the exercise's structure and the numbers are never edited.

### Headings that argue (scholarly-voice 14, humaniser #32)
- "The widths are where the human's work is" → "The bar and its three widths"
- "A tool is a schema plus a gate" → "Tools, schemas, and the permission gate"
- "Memory is a claim with a date" → "The memory record and its date" (also removes "claim" in the thesis sense)
- "Not tonight: the mechanisms in the loop" → "Mechanisms in the loop, deferred"
- "One window in, one answer out, nothing kept" → "The window, the reply, and no state between calls" (rule-of-three cadence)
- "what gets squeezed" → "what is compacted" (metaphor to the term the deck uses)

### Epigram landings, mirrored pairs, antithesis closers (#36, house cadence bans)
- "The drawer does not open itself, and it does not close itself either." → "The retriever decides when a record enters the window. Only evict or the retention date removes the record from the store."
- "The deny enforces. The anti-trait explains. Both, in that order." → "Write both lines. The deny line stops an edit at the permission engine, and the anti-trait line tells the model the reason."
- "Refused by persona, or denied by permission. An edit that goes through is the finding of the night." → "The persona should refuse, and if it does not, the permission engine should deny the edit. An edit that goes through is the finding of this exercise."
- "The model's part of the work is the thin part; the human owns both wide ends." → "The model does its work there, and the human writes both wide ends."
- "nothing in the rings notices" → "no component in the three rings reports the shrinkage"
- "Nothing in the loop knows." → "No step in the loop compares the record with the code."
- "a mechanism in the loop, not a sentence in the prompt" → "with a mechanism in the loop rather than a sentence in the prompt" (the contrast is the Probe question's content, so it stays as a qualifier, not a closer)

### Definition-colon ledes and fragments (#35, STE rule 7)
- "A tool is a contract: arguments, a result, exit codes." → "A tool is a contract that fixes its arguments, its result, and its exit codes."
- "E1's loop, shipped." → "This is the loop you drew in E1, shipped as a product."
- "Its trace is its own: the agent name in the TUI, ..." → "OpenCode leaves a trace of its own in the agent name in the TUI, the tool-call line, and the permission prompt."
- "What happens when the reviewer and the worker disagree, and a second reviewer..." → "E9 covers what happens when ... and adds a second reviewer with a different question."
- "Your code inside the loop for the first time:" → "E10 puts your code inside the loop for the first time:"
- "The difference is the trust boundary (Figure 06): the server's descriptions are someone else's text." → "..., because the server's descriptions are text that someone else wrote."
- "Nothing in the rings yet." → "The rings hold nothing yet."

### Actor and mechanism (STE rules 2, 3; brief: each sentence has an actor and a mechanism)
- "It keeps nothing between calls." → "The model keeps nothing between calls."
- "You can only change what goes into the window and what happens to what comes out." → "You can change only what the harness puts into the window and what the harness does with the reply."
- "most things ask, on purpose, so the room sees it" → "the permission file sets most tools to ask, on purpose, so that everyone in the room sees the prompt"
- "The retention date and evict are the mechanism; the sentence ... is a request." → "... are the mechanism that removes a stale record, and the sentence "data, not instructions" is a request to the model that the mechanism does not enforce." (quoted phrase untouched)
- "The model did not read the files; the loop did, and put the text" → "The model did not read the files. The loop read them and put the text in the next window."
- "Your V&V shows, for every file on it, what reads it, when, and the trace." → "... for every file on that ring, what reads the file, when it reads it, and the trace that it left."

### "names" ban
- "answers the standing-intent question and names the file" → "... and gives the file's name"

### Semicolons in step lists and table cells (STE course register)
Slide 14 step list (four items) and three table cells on slides 4 and 10 rewritten with commas, "then", "and", or "which". Explanatory paragraphs kept their semicolons where they had them (none remain in prose after the edits above).

## Self-audit artifacts (after the final pass)

### Closer list (last sentence of every paragraph, callout, and list block)
1. ...and most of it is your own version of what OpenCode already does by default.
2. ...each of you in your own repository, following the screen.
3. The exercise page stays open beside OpenCode.
4. The next turn starts from a window that the harness builds again.
5. You can change only what the harness puts into the window and what the harness does with the reply.
6. This is the loop you drew in E1, shipped as a product.
7. OpenCode leaves a trace of its own in the agent name in the TUI, the tool-call line, and the permission prompt.
8. Each outer item sits radially outside the thing it steers
9. All three rings sit inside the narrow band. The model does its work there, and the human writes both wide ends.
10. ...and no component in the three rings reports the shrinkage.
11. ...ends with you in the right band, reading a reviewer's verdict against a diff.
12. The rings hold nothing yet.
13. The loop read them and put the text in the next window.
14. The pattern you drew in E2 is now a permission difference between two agent definitions.
15. Then plan hex in plan and build it in build.
16. ...that declares the schema and calls the Python, so that all logic stays in Python.
17. It sets allow, ask, or deny per tool and per pattern, and the last matching rule wins.
18. The name, description, and schema go into the window, and the permission engine checks each call.
19. In this exercise you only locate the mcp block and record what it exposes.
20. ...on purpose, so that everyone in the room sees the prompt.
21. The third drawer, memory, is on the next slide.
22. ...are an addition with no counterpart on the middle ring.
23. The model then reads the record as fact.
24. ...is a request to the model that the mechanism does not enforce.
25. Only evict or the retention date removes the record from the store.
26. ...placed radially outside build and plan.
27. An edit that goes through is the finding of this exercise.
28. The controller routes FAIL back to the worker with a bound on rounds, then sends BLOCKED to the human.
29. Each of the three answers the previous Evolution's Probe 3 question with a mechanism in the loop rather than a sentence in the prompt.
30. A row with no trace is the finding.
31. ...what reads the file, when it reads it, and the trace that it left.
Judgment: lines 12 and 30 are short flat statements, not morals; 30 states the exercise's rule for the worksheet. No line reads as a caption or slogan.

### Lede list (first sentence of every slide body)
1. The model sits in the inner ring.
2. Hour one · lecture (list heading)
3. opencode/big-pickle (or any OpenCode Go model) reads a window of text and writes a reply, one token per pass.
4. OpenCode builds the window, calls the model, parses the tool call, checks the permission, runs the tool, and loops.
5. (table)
6. (bar) All three rings sit inside the narrow band.
7. (embedded figure)
8. A human writes what is wanted before the loop runs, and a human judges what came back.
9. A tool is a contract that fixes its arguments, its result, and its exit codes.
10. (table)
11. OpenCode keeps no store between sessions.
12. (code block) .opencode/agents/reviewer.md is your version of a built-in agent, placed radially outside build and plan.
13. E9 covers what happens when the reviewer and the worker disagree, and adds a second reviewer with a different question.
14. (step list)
15. (file list) The worksheet's last column asks whether each file was in your repository before this exercise.
Judgment: no "X is Y: a, b, c" opening remains; no repeated lede shape.

### Claim list (frequency and consensus claims)
- "most of it is your own version of what OpenCode already does by default" (slide 1): source is the slide 5 table, where seven of nine rows have an OpenCode counterpart. Kept.
- "default permissions: most allow" (slide 4): OpenCode docs (footer cites them). Kept.
- "the permission file sets most tools to ask" (slide 9): the slide's own permission block shows the "*": "ask" rules. Kept.
- "every turn" (slides 10, 15, table cells): a mechanism statement about AGENTS.md and instructions, not a frequency claim about people. Kept.

### Sibling diff
Not applicable; the deck is a single page.

## ste_check lines declined
- Sentences over 25 words (2): the custom-tool sentence on slide 9 (a definition with its reason attached) and the retention-date sentence on slide 11 (mechanism and request contrasted in one sentence). Both sit in explanatory paragraphs, where the brief sets no ceiling.
- Gerund/nominalized subjects (10): "harness", "compaction", "permission prompt", "retention date", "evolution-08", "the difference" are the deck's stipulated terms, table cells, or file names. Declined.
- Passives with no actor: "Nothing is printed" (a footer note; the instructor prints nothing) and "what is wanted" (E0's own phrase on the bar and the E0 paragraph). Declined. "most tools are set to ask" was fixed (actor: the permission file).
- Noun clusters of 4+ (20): all are file paths, tool lists, or code identifiers. Declined.
- Semicolons: the four the checker counted were in the step list and table cells and were removed; the remaining semicolons in the file are in CSS, JS, an aria-label, and HTML entities.

## Sentences left long
- Slide 9: "A custom tool is a ten-line .ts shim in .opencode/tools/ that declares the schema and calls the Python, so that all logic stays in Python." (27 words; the "so that" clause is the reason and belongs with the rule.)
- Slide 11: "The retention date and evict are the mechanism that removes a stale record, and the sentence "data, not instructions" is a request to the model that the mechanism does not enforce." (31 words; splitting would detach the quoted phrase from the contrast it is there to make.)
