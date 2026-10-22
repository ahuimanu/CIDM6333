# Deck pass log: e6-context-engineering (Oct 22, 2026)

Files edited in place:
- /home/claude/site/tools/sitekit/voice/e6-context-engineering.json (24 values changed, 0 keys changed; key order unchanged; JSON valid)
- /home/claude/site/tools/review/voice-pass/notes/e6-context-engineering.json (27 of 27 lecture paragraphs rewritten; every "Cut from slide N" and "Instructor checks" section left byte-identical; slide 27's source list after "Sources checked 09/24/2026:" left byte-identical; JSON valid)

Chain run: humaniser (full), ste-voice (rules 1 to 4 on explanatory prose; checker run on extracted prose), scholarly-voice (course register, sets the final surface), humaniser battery check-only (greps plus closer, lede, and claim lists below).

## Patterns that dominated

1. "Tonight" / "we" / schedule details (BRIEF house rule; humaniser #19 chat residue). Every paragraph carried at least one. Minute counts, "Thu 10/08", "Monday night", "Sunday", "Thursday noon", "Lab at six", "sticky note", "with me", "we build together" removed; "this Evolution" or "the lab" substituted.
   - "Tonight we treat the window as something you design and measure." → "This Evolution treats the window as an artifact you design and measure, which is the framing sentence of the deck: the window is an artifact with a budget."
   - Slide: "Tonight's claim, which Sortie 6 will try to disprove" → "The design claim Sortie 6 tries to disprove"
   - Slide: "Answer (we fill the gaps together)" → "Answer (a draft to argue with in class)"

2. "claim" as the lecture's thesis and "the move" / "moves" as step (BRIEF reek list).
   - "The claim is from Chapter 15: a handoff lets..." → "The design claim comes from Chapter 15: a handoff lets..."
   - Slide: "Compaction: four moves, from cheapest to most lossy" → "Compaction: four operations, from cheapest to most lossy"; notes follow ("Re-seeding is the move most people forget" → "Re-seeding is the fourth operation: after the summary, reload the canon and the ledger tail from disk...").
   - Slide: "Every one of the three is the same move: a fact the session kept asking for..." → "All three episodes end the same way: a fact the session kept asking for gets written where the next session reads it first."
   - Kept as course vocabulary: "typed claim", "design claim", "the summary is a claim", "the model's claim", "token claim", "FAIL is the design claim disproved".

3. "names"/"named" as verb (house ban). Five instances, including the flight card.
   - "the fresh session's first action is the one the handoff named" (slide 3, flight card DESIGN CLAIM line, notes) → "the handoff's first next step"
   - "takes a first action the handoff did not name" (falsifier) → "did not list" (same length)
   - "The handoff names a commit" → "records a commit"; "A NO-GO names the field to fix" → "states the field to fix"; "the action you named" → "the action you listed (first)"
   - Noun uses left: "field names", "tool names", "no names on decisions", "names enter first".

4. Epigram landings and "not X but Y" closers (#36, house cadence ban).
   - "Intent that lives only in the window dies with the window." (closing slide and notes) → "Intent kept only in the window is lost at the next compaction or session."
   - "A free model with an unpublished window: the only budget you can trust is the one you declared and logged." → "Big Pickle publishes no window size, so the budget you declared and logged per turn is the only limit you can check."
   - "The summary is a claim, not evidence." → "The summary is a claim; the child's evidence stayed in its window."
   - "Log the number the provider billed, not an estimate." → "Log the count the provider returned rather than your own estimate."
   - "The documented list of what survives /compact is the design, stated" → "...states the design"

5. Invented authority (#37) and unsourced superlatives.
   - "the shortcut every one of you will be tempted by" → "The last one is the shortcut: pasting the old transcript into the new session fails the test, because the test asks whether the handoff alone carried the intent."
   - "the most common bug you will hit" → "the difference produces a wrong total unless your code checks which fields came back"
   - "the move most people forget" → "the fourth operation"
   - "Cursor's January post is the cleanest statement of a design choice this year" → "Cursor's January post states one design choice"
   - Slide: "Each one has passed a demo and failed a sortie" → "Each one looks sound in a demo and fails a sortie's test points"
   - "Cursor's answer is the most interesting" → "differs from the other three and gets its own slide"

6. Actor removal / nominalization (STE rules 2 and 3; humaniser #3, #31).
   - "the reconciliation was a hard reset, and about 215 lines were lost" → "a hard reset reconciled the clone and discarded about 215 lines"
   - "Claude Code, Codex, and Cursor are read for mechanism" → "the teardowns read Claude Code, Codex, and Cursor for mechanism"
   - "FAIL means the design claim was disproved" → "FAIL means the sortie disproved the design claim"
   - "what you said only in conversation becomes a summary" → "compaction turns what you said only in conversation into a summary"

7. Scholarly-voice register: reasons attached ("because a derived view can be wrong without anyone having lied", "because the compaction call reads everything it summarizes"), "For this reason" at joints, derivation phrased as "follows from the definitions" (slide 10), QA asides ("Verify the ADR number ... before class", "verify the numbers against the casebook") dropped from the spoken paragraphs (they survive in the untouched "Instructor checks" sections).

## Self-audit artifacts (notes, after the final pass)

Closer list (last sentence of each lecture paragraph):
1. That number is the starting point.
2. The homework brief has the dates.
3. The last one is the shortcut: pasting the old transcript into the new session fails the test, because the test asks whether the handoff alone carried the intent.
4. Codex and OpenCode do not publish this table, so the lab measures their behavior instead of reading it.
5. The design consequence follows: the window is the provider's limit, the budget is your design decision below it, and for Big Pickle there is no published limit at all, so the budget you declare is the only number you have.
6. The OpenCode teardown shows a counter of that kind that is cumulative and not the window at all.
7. Your own loop needs all four operations, and Sortie 6 logs an event every time compaction runs.
8. The cost of isolation is the E9 lesson arriving early: the summary is a claim the parent has not checked, and the gzkit casebook holds a chain ten summaries deep in which polished summaries became facts.
9. Anthropic's long-running harness (November 2025) is the same design under other labels: a progress file, a feature list, and the git log, read first in every session.
10. Your README declares these layers, with paths, in the Sprint.
11. That is summary laundering from the human side, and it fails the sortie's one observable.
12. Write your answer down; the evaluation lens returns to it.
13. Keeping things out: Cursor's answer differs from the other three and gets its own slide.
14. The control points are the part that applies to your build: focus instructions on /compact, a compact-instructions section in CLAUDE.md, a PreCompact hook that can refuse, and a SessionStart hook with the compact matcher that can put your handoff back after every compaction.
15. For this reason your system keeps its own ledger: if the provider's record of intent is opaque, your evidence of intent has to live in a file you control.
16. A rule that must hold on every turn, placed in that mode, is the wishful rule from your E5 AGENTS.md probes, and the failure is Appendix C number four, the cheap verification skipped.
17. Find out what OpenCode assumes, and treat any answer the model gives about its own window as a claim to check against the export.
18. This is Sortie 6 at production scale: a handoff, a resume procedure, and a ledger, which in that harness is git.
19. Your Sprint Design Analysis does the same for one of the four harnesses.
20. The count of 116 handoffs by June 2026 comes from the casebook's 'utter shambles' entry, and it is a warning as much as a feature: handoffs accumulate, and a pile of them is itself a context problem.
21. For your build the translation is one line in the resume procedure: the handoff records a commit, and the fresh session checks where the working tree sits relative to that commit before its first action.
22. The third episode is AGENTS.md as a derived view, rendered from the corpus and trusted least, which connects to the 258K exhaustion in E5.
23. The last item costs little with a Go subscription; with Big Pickle alone, state that and skip it.
24. Go is asynchronous this term: your Chase signs the card in the repository by the date in the course calendar, and you do not fly before that signature.
25. The Sprint puts the same meter inside your own agent loop.
26. The strip at the bottom holds the distinction to keep: FAIL means the sortie disproved the design claim; ABORT means the flight did not happen for a reason outside the claim.
27. Measure every turn, decide what compaction may lose before it runs, and write the handoff for a stranger.
Verdict: each closer carries a fact, a pointer, or an instruction; none works as a caption on its own. #1 and #25 are short pointers to the next unit of work and were kept as such.

Lede list (first sentence of each lecture paragraph):
Evolution 6. / The lecture has six parts, and the lab after it is self-guided. / Framing. / Six categories. / Why a budget when the context window is a million tokens. / The instrument. / Compaction as four operations, in order of cost. / Four ways to keep tokens out of the window until they are needed. / Handoffs, with the seven sections from the chapter. / The architecture that makes the handoff checkable. / Three mistakes, each with a failure-mode number from Appendix C. / Five minutes. / The four harnesses in one table, so that the next four slides can take them one at a time. / Claude Code is the reference harness, and its documentation now states what survives compaction. / Codex in three cards. / Cursor's January post states one design choice: do not discard context, move it to files and let the agent search. / OpenCode, because it is the harness you fly. / Anthropic's harness for long-running agents, from November 2025. / Build this analysis in class; the second column is a draft, and your job is to argue with it. / The reference design's version of this Evolution. / Chapter 15 is built around this incident. / Three more episodes. / Weak: a size where a per-turn count belongs, ... / Card six returns to the expansion envelope after the corner in E5. / The lab, which you run on your own. / The Sprint in three cards. / Close.
Verdict: the spoken-label ledes ("Framing.", "The instrument.") are the lecturer's slide callouts and were kept from the original; no "X is Y: a, b, c" definition lede remains (the Cursor lede states a choice the post makes, with the post as actor). No two ledes share a template.

Claim list (frequency or consensus claims):
- "Codex and OpenCode do not publish this table" (source: the slide's source line, docs checked 09/24/2026).
- "every harness auto-compacts and every harness lets you trigger compaction by hand; only Claude Code gives you a hook that can block it" (source: the teardown table, same source line).
- "A small free model guesses" (lab step; the measured comparison is the evidence the lab produces). Kept because the lab checks it.
- "the model edits prose freely and structured files less" (source: Anthropic's quoted sentence on the slide).
Removed: "every one of you will be tempted by", "the most common bug you will hit", "the move most people forget", "the cleanest statement ... this year", "has passed a demo and failed a sortie".

## ste_check lines declined, with reasons

- 52 sentences over 25 words and 12 paragraphs over six sentences: declined. The brief sets no length ceiling for explanatory paragraphs, and these are the lecture as spoken; the long sentences carry lists of conditions (test points, the weak/sound/exceptional lens, the control points) whose count is the material's.
- Gerund/nominalized-subject hits: "The harness", "The instrument", "The compaction summary", "The configuration", "The decision", "The preservation mechanism", "The reference design", "The evidence section", "The question on the slide", "The sentence to carry", "The judgment loop": stipulated terms or physical objects (a slide element, a file), not nominalized verbs. One true hit ("the reconciliation was a hard reset") fixed.
- Passive hits: "are read for mechanism" fixed; "was disproved" fixed; "whatever mattered was written to a file" (the writer is unknown by design, which is the point of the sentence), "what was kept" (the provider hides the actor; the sentence says so), "is keyed to", "is mediated", "until they are needed" declined as idiomatic with no hidden actor.
- Noun-cluster hits: all 22 span clause boundaries ("window what compaction removes"); none is a real cluster.
- 33 semicolons: explanatory paragraphs, not procedures; declined.

## Left as is, with reasons

- Timing keys ("0:00–0:02"), run-of-show rows, footers, and slide numbers: unchanged (the build drops them).
- Code, config, paths, URLs, the flight card except the two "named"/"name" lines, the gzkit quotations ("Frontmatter can lie; the ledger is the truth."), Anthropic's and Cursor's quoted sentences, dates, the 09/24/2026 source lines on slides 4 and 13 (citation dates, not QA asides).
- "Where does a compaction summary sit? L3. It may inform the next turn; it may not overrule the ledger." Mirrored pair kept: the partition is real (inform vs overrule).
- "The harness already implements rule two: files reload, chat does not. Your loop should too." Kept: a real two-sided partition stated on the Claude Code docs.
- "Handoffs: writing for a stranger with no transcript": a label with a gerund noun, not an argued heading; kept.
- "The nine components on the board; most of the words go to memory and context, governance, and coordination": describes the slide's own table, not a frequency claim about the world; kept.
- Flight-card DESIGN CLAIM line reworded for the "named" ban ("the handoff's first next step"): the card is pre-registered course text, so the parent should confirm the matching line in the homework brief and Flight Card 6 reads the same way.
