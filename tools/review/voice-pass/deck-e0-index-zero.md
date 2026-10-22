# Deck pass log: e0-index-zero (Oct 22, 2026)

## Counts

- `/home/claude/site/tools/sitekit/voice/e0-index-zero.json`: 33 of 415 keys given a new value. Keys and key order unchanged.
- `/home/claude/site/tools/review/voice-pass/notes/e0-index-zero.json`: 22 of 22 lecture paragraphs rewritten. Every "Cut from slide N (full wording):" section byte-identical to the original. Timing marks kept in place. Both files load with `json.load`.

## Patterns that dominated

**Em dashes (house ban).** 18 slide keys carried one; replaced with a comma, a colon, or parentheses. "What a language model adds — and what it does not" → "What a language model adds, and what it does not". "Tool calls, file writes, messages, commits — the side-effect surface" → "...commits: the side-effect surface". Left as is: the em dash inside "Completed — Partial", which is gzkit's closed vocabulary.

**Session-running language (tonight, this week, Wednesday, times, rooms, WTClass, lab at six).** Removed from every notes paragraph; "this Evolution" or "Evolution N" stands in. "Five moves. Framing for ten minutes; the two maps for fifteen; ... what is due Wednesday. Nothing is on a screen tonight except these slides; the install clinic is in lab at six." → "The lecture has five parts. The first part frames the course. ... The fifth part presents the instrument you will use in every Evolution and the Evolution 0 brief." "week seven", "week eight", "week nine", "week eleven" → "Evolution 7" etc. (the slides already say E7, E8). The gzkit "Week 1 to Week 4" of the Degradation Pattern stays.

**"we" and stage directions.** "the one worked example we do on a slide tonight", "Every component we study", "Ask them: ... Sit in the silence for a moment", "Ask the room", "At five o'clock we go around the room" all removed or turned into third person or second person ("Consider who answered for the last piece of generated code you shipped").

**Invented authority (#37).** "'done' is the most dangerous word in the course" → "'done' is the term to define first, because the agent's halt and your attestation both depend on it". "the most common thing sold as agentic today" (slide and notes) → "a generative model with a loop bolted on, sold as 'agentic'" / "vendors sell such systems as agentic". "since 2024 most of what fills a context window is tool results" → "the context window of an agent harness fills with tool results, so context management is a problem you meet only after tool calling exists". "Most production 'agents' are workflows, and should be" (slide 15 and two notes paragraphs) → "Use a workflow wherever the path is known in advance" / "Anthropic recommends the workflow wherever the path is known in advance, and the open loop only where it is not" (that is what the cited post says; it does not give a share). "most of the design choices only make sense once you ask" → "a design choice makes sense once you ask". "The part people miss is that it has two sides" → "The covenant has two sides". "…and the one everybody forgets" → "…and the one that is easy to forget".

**Epigram and antithesis closers (#36, "not X. It is Y").** "A loop without a halt is a bill." → "A loop with no halt runs until the budget is gone." "The atom every later week decorates." → "Every later Evolution builds on this loop." "The chat assistant is not worse. It is a workflow with the human as the loop" → "The comparison does not rank the chat assistant below the harness: the chat assistant is a workflow with the human as the loop, and a workflow is the right design wherever the path is known in advance." "That last one is the whole course in one question." → "That last question contains the course's whole concern, because an intent nobody preserved is an intent nobody can answer for." "Agentic AI is thin and new; the foundation is old and cracked." → "Agentic AI is the newest and thinnest layer. The data foundation is the oldest, and it has cracks." "Policy frameworks say what must be true; a covenant says who does what on Wednesday" → "Policy frameworks state what must be true. A covenant states who does what in one session". "It makes one build answerable." (notes closer) → "Its scope is one build, and it makes that build answerable to the engineer who signed."

**"names"/"name" as verb; "claim"; "the move".** "names the stake" → "states the stake"; "names an accountability gap" → "describes"; "Name the decision... Name the cost..." → "State the decision..."; "Mark every box you can name a system for" → "Mark every box for which you can cite a real system". "makes the general claim: the cost of generated code is deferred" → "argues that the cost...". "Sixty minutes, five moves" / "Five moves." → "five parts". "every layer flown against a claim that a single observation could disprove" and "what it claims (top-down)" stay: course vocabulary (typed claim) and a plain verb.

**Semicolons in slide lines and run-on scholarly joints.** Slide subtitles with semicolons split into sentences ("Seven layers. Each stands on the one below, and none replaces it"). In the notes, reasons are attached with "because", "for this reason", "so that"; terms get a stipulation at first use (agent, PEAS, workflow and agent, Lite and Heavy).

## STE checker lines declined

- Sentences over 25 words in explanatory paragraphs: declined by brief (rules 1 to 4 only). Two sentences were split anyway (slide 9 "First, the middle is inverted..." at 50 words; slide 13 "The nine components..." at 58 words). Left long with a reason: the nine-component list sentence (nine items), the three-names sentence on the Degradation Pattern (three definitions, gzkit's), the four-rules sentence of the command doctrine (gzkit's list, one sentence on the slide), the ring-five sentence (lists the three missing components), the Design Analysis assignment sentence (three required parts).
- Paragraphs over six sentences: declined; the brief says no length ceiling in explanatory paragraphs, and each notes entry is one slide's spoken text, which the brief says not to split.
- Gerund/nominalized subjects flagged: definition, planning, learning, harness, foundation, attestation, judgment, performance (measure), consultation. All are course or field terms used as nouns (Deep learning, the judgment loop, the performance measure); declined.
- Passives flagged: "what is stored", "is deferred" (quoting the essay's thesis), "can also be read", "what was attested", "is known in advance", "cannot be automated away", "what is written", "must be instrumented" (gzkit rule). Declined; each is either a stipulated term's definition or gzkit wording. Two were fixed: "the course is built" → "I built the course", "every system idea is tested" → "I test every system idea".
- Noun clusters flagged are lists separated by commas and the PEAS expansion; declined.

## Self-audit artifacts (notes, after the final pass)

### Closer list
- Four words describe the semester (survey, build, govern, defend), and this Evolution covers the survey and govern pair.
- The fifth part presents the instrument you will use in every Evolution and the Evolution 0 brief.
- Governance supplies the third, and no software can automate it, because accountability belongs to a person.
- For this reason a Design Analysis starts at the bottom, with the question of what the system stands on.
- The Sprint and Drift essay 'Newtonian motion' argues that the cost of generated code is deferred, never erased.
- Evolutions 1 through 7 build the AI Agents column on your system, and Evolutions 8 through 12 build the Agentic AI column.
- Keep this picture, because each Evolution states which stop it is at.
- The exercise for Evolution 0 is to mark every box on the board for which you can cite a concrete system, and the blanks become your reading list for the semester.
- You need to know it exists so that in every Evolution you can say where you are on the board.
- Governance supplies accountability, and more software cannot supply it, because accountability is a property of a person.
- Your first exercise in Evolution 0 is to specify your intended system by PEAS.
- Sortie 1 is a loop that halts, on every input class, within budget, with every turn in the ledger.
- A Design Analysis consists of nine short answers and one paragraph on why.
- The comparison does not rank the chat assistant below the harness: the chat assistant is a workflow with the human as the loop, and a workflow is the right design wherever the path is known in advance.
- Reinforcement learning had already described reward hacking, so gaming the gate has a history older than the language model.
- The first exercise in chapter three is a one-week log of your own review behavior.
- It comes from a conversation in January in which the model said only specification matters and the operator refused.
- The doctrine has four rules: accountability is non-transferable; authority must be instrumented, not asserted; the model is a crew resource, not a crew member; evidence is artifacts, not narration.
- Its scope is one build, and it makes that build answerable to the engineer who signed.
- I will ask you about it in consultation.
- In consultation I test every system idea against one question: can it take all twelve layers?
- Your job is to build one you can answer for. (Jeffry's closing-slide thesis; kept.)

Two closers repeat a reason ("because accountability is/belongs to a person", slides 3 and 10); the slides make the same point twice by design (the definition, then the lens), so both stay.

### Lede list
- This lecture carries content rather than logistics, and the orientation deck holds the mechanics of the semester.
- The lecture has five parts.
- The course asks two questions.
- The first map has seven layers, and you can read it top down or bottom up.
- The data foundation is easy to forget because it is unglamorous and because its cost lands later, on someone else.
- The second map runs five stages left to right, and the unit of work changes at each stage.
- The road map shows the same five stages as stops.
- The framework board can also be read as rings out from the foundation: foundation, creation, core systems, action, full automation.
- This table gives the fill-in order.
- Before the definition of an agent, the reasoner in the middle of it needs a precise statement.
- The definition of an agent predates the language model and still holds.
- The LLM agent loop puts a language model in the reasoner slot.
- The nine components are how you take every system apart this semester, and their order matters.
- The Evolution 0 exercise, done on a slide, compares a chat assistant (left column) with an agent harness such as Claude Code or Codex CLI (right column) across the nine rows.
- Two distinctions carry out of this Evolution.
- The Degradation Pattern, from gzkit's why.md, is the reason I built the course the way I did.
- The Zero Doctrine answers the Degradation Pattern: the human is index zero.
- Five gates enforce the covenant.
- The posture needs its place among the governance frameworks, so that nobody mistakes it for the whole of AI governance.
- The judgment loop from CIDM 6330 is the survey thread's instrument, and it closes every Design Analysis.
- Evolution 0 asks for reading, writing, and setup.
- The thesis closes the lecture.

No repeated opening shape; no "X is Y: a, b, c" definition lede (the rings lede lists the five ring labels after a colon, which is the figure's content rather than a definition).

### Claim list (frequency or consensus)
- "vendors sell such systems as agentic" (slide 8): no share stated; the slide's own framing. Kept as a plain description, not a frequency.
- "Anthropic recommends the workflow wherever the path is known in advance, and the open loop only where it is not" (slide 15): sourced to "Building Effective Agents" (2024), which the slide cites.
- "the one place where engineers have built authority over an automated system for decades" (slide 18): Jeffry's framing from the slide's cut-from wording; kept.
- "the 2023 loops never wrote one down" (slide 11): sourced to AutoGPT and BabyAGI as the slide's examples.
- All "most" claims removed (see above).

## Left as is, with the reason

- "Named pattern; framework; ADR-1" (E2 table cell) and "E2 refactors your loop into a named pattern": "named" as a modifier is on the ban list, but "named pattern" appears to be the E2 deliverable's own term (the cut-from wording expands it to Anthropic's five patterns). Not changed; flagged for Jeffry.
- "Accountability is a property of a person, not a pipeline.", "You sign off, not the model.", the four command-doctrine bullets, and the three Degradation Pattern definitions: gzkit doctrine wording, unquoted on the slide; left exactly as written.
- "The Newtonian-motion argument: the cost of generated code is deferred, never erased." and the two closing-slide lines: Jeffry's own theses.
- "The run of show for tonight's lecture", "Due on the date in the course calendar. The mechanics are in the orientation deck and WTClass", "Toolkit: ... (install clinic in lab)", "0:00–0:03" and the like: run-of-show and logistics lines the build drops.
- "Completed — Partial": gzkit closed vocabulary; em dash kept.
- "Three names for the same failure": noun use of "names".
