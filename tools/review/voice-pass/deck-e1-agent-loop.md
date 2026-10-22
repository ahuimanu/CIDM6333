# Deck pass log: e1-agent-loop (Oct 22, 2026)

Files edited in place:
- `/home/claude/site/tools/sitekit/voice/e1-agent-loop.json` (slide wording): 24 of 262 values changed; no keys touched; JSON valid; key order unchanged.
- `/home/claude/site/tools/review/voice-pass/notes/e1-agent-loop.json` (speaker notes): 14 of 14 lecture paragraphs rewritten; every "Cut from slide N" section byte-identical to the original (checked by script); JSON valid.

Chain run: humaniser (full), ste-voice (rules 1 to 4 on explanatory prose), scholarly-voice (final surface), humaniser battery as check only with grep battery and `ste_check.py` on extracted plain text.

## Patterns that dominated

1. "Tonight's claim" / "the claim for the week" framing (Jeffry's flagged reek). Slide heading "Tonight's claim, which Sortie 1 will try to disprove" is now "The design claim Sortie 1 will try to disprove" (course vocabulary, same length). In the notes, "read the claim for the week aloud, because it is the shape every claim will take" is now "read the design claim for this Evolution aloud, because every design claim in the course takes its shape".
2. "not X. It is Y" antithesis and epigram landings.
   - "Autonomy without a stop condition is not a feature. It is an open account with the model provider." -> "A loop with no stop condition keeps calling the model provider, and the provider keeps billing, until a human intervenes."
   - "Planning was present. Fluency without grounding is a spiral." -> "Planning was present. The model wrote fluent plans with no grounding, and the loop spiraled."
   - "a budget the model can talk itself out of is not a budget" -> "a budget that lives only in the prompt is a budget the model can argue away" (slide and notes).
   - "Not a better model call. A PRD that..." -> "The additions were a PRD that... None of them changed the model call."
   - "that is a finding, not a bug" (notes) -> "That result is a finding about the model, so record it in the flight log rather than treating it as a bug in your loop."
   - Subtitle "The Chase reads the black box, not your story" -> "The Chase reads the ledger slice and receipts only".
3. Parts-list notes (fragments with colons) rebuilt as full sentences with an actor and a mechanism, per scholarly-voice and STE rule 2. Example: "A message list. A bounded for-loop, which is the first halt. A model call that returns a structured Step..." -> "The loop starts with a message list. A bounded for-loop supplies the first halt. A model call returns a structured Step, so the decision is typed, and the parser rejects a malformed decision instead of the loop executing it."
4. "names"/"named" as a verb: "It named the ambition" -> "It stated the ambition"; "A PRD that names a framework" -> "A PRD that specifies a framework" (slide and notes).
5. Em dashes (three slide values; run-of-show line 26 left because the build drops it).
6. Session-management residue: "Tonight", "Last week", "this week", "next week", "December", "the next eleven weeks", "week three", "Consultation at five", "at 5:46", "in lab" removed or replaced with Evolution references.
7. Invented authority: "Every 2024–25 design replies to this spring" -> "The evaluators, budgets, and human-in-the-loop designs of 2024–25 reply to this spring"; "people write it wrong the first time" dropped, reason derived from the ADR-1 consequence instead.
8. Actor removal: "was started to fill that gap" -> "The operator started..."; "ReAct was built to show" -> "ReAct's authors built it to show"; "would be shown to students" -> "the operator would show the system to students"; "The three falsifiers are written now" -> "You write the three falsifiers now".
9. Count mismatch: "Notice three things" followed by four items -> "Four of the components deserve attention."
10. Chat artifact "Here is a trace" -> "The slide shows a trace".

## Self-audit artifacts (notes, after the final pass)

Closer list (last sentence of each paragraph):
0. The build is a governed loop that halts, with a PRD attested.
1. The consultation afterward takes your pitch in one sentence and your E0 Design Analysis, defended.
2. ...one sentence, and beside it the falsifiers that would disprove it (three, on this card).
3. ReAct adds the observation, so each reasoning step carries a piece of ground truth, and that one addition turns a generative system into an agent.
4. ReAct lacked memory, a budget, and verification, and each of those three is a later Evolution.
5. That result is a finding about the model, so record it in the flight log rather than treating it as a bug in your loop.
6. The rule for the semester follows from the last case: a budget that lives only in the prompt is a budget the model can argue away, so halts live in code and in the ledger.
7. The evaluators, budgets, and human-in-the-loop designs of 2024 and 2025 reply to that spring.
8. Write the one I did not do on the board.
9. It is short, and it never says how.
10. ...which is the post-hoc rationalization ADRs exist to prevent.
11. ...a flight-log paragraph on what the SDK hid, which is the exercise from chapter ten.
12. Finish the card at the card station, request Go or No-Go, and fly test point one while I am in the room.
13. Build one that stops, and can say why.
Disposition: 3 and 13 are the lecture's stated theses (13 is the deck's own closing line on slide 14) and carry the derivation in the same sentence; kept. 9 describes the PRD (short, no "how") and is information; kept. No line restates its paragraph.

Lede list (first sentence of each paragraph):
0. Evolution 1. 1. The lecture makes five moves. 2. The lesson comes before the history. 3. The prompt became a control structure in four steps over two years. 4. Read the ReAct paper as a design document. 5. The build fits in a dozen lines, and the slide reads top to bottom. 6. Five failures appear on day one, and each one maps to a falsifier or an abort on your card. 7. The second teardown is AutoGPT, and this one goes on the board with the room. 8. The table puts the two side by side. 9. The reference design began as the loop plus the thing the loop lacked, a record of intent that survives the session. 10. The PRD gets two minutes of its own, because the line between what and how decides whether ADR-1 will record real alternatives. 11. The evaluation lens has three columns. 12. The card for this Evolution sits at the center of the envelope, because this is the first sortie and nothing depends on it yet. 13. Two lines close the lecture.
Disposition: no "X is Y: a, b, c" opening; no repeated opening shape.

Claim list (frequency or consensus statements):
- "Every later Evolution adds tools, memory, coordination, or evaluation to this loop" (source: the course's Evolution sequence, E2 to E12; a plan statement, not an observation).
- "every design claim in the course takes its shape: one sentence, and beside it the falsifiers" (source: the flight card format the course uses).
- "Some small models cannot produce the schema at all" (source: the card's own ABORT criterion on slide 13).
- "The evaluators, budgets, and human-in-the-loop designs of 2024 and 2025 reply to that spring" (narrowed from "Every 2024–25 design"; the slide's cut wording lists these designs by name).
No other "most", "usually", "often" statements remain.

## ste_check lines declined, and why

- All 22 "sentences over 25 words": explanatory lecture prose, where the brief applies STE rules 1 to 4 only and scholarly-voice sets the rhythm. The 81-word sentence in paragraph 9 was split anyway (now two sentences, 32 and 16 words). The remaining long sentences carry lists of conditions (the PRD "what" list, the Sound column, the failure cases) that lose precision when split.
- All 9 "paragraphs over 6 sentences": one paragraph per slide is fixed by the brief (no merging or splitting).
- Gerund/nominalized subjects: all 8 are false positives on course terms ("framing sentence", "reference design", "evaluation lens", "instrumentation", "consultation").
- Passives with no actor: "the smallest unit an agent is built from", "the decision is typed", "is untrusted input" are states, not judgments; left. The other five were fixed (see pattern 8).
- Noun clusters of 4+: all 11 are the heuristic reading across clause boundaries ("loop halts anyway because"); none is a real cluster.

## Left as is, with the reason

- `[Quote from genesis.md · verify wording against the source before class.]` (slide) and `[Verify the quote against genesis.md.]` (notes): a verification condition on an unverified quotation, so dropping it would hide the condition; Jeffry should decide whether it stays on the published page.
- "(that is ADR-1, in Evolution 2)" replaced "next week" on the slide and the notes now say "ADR-1" without a time; Evolution 2 is inferred from the sequence (E1 this deck, ADR-1 next) and should be confirmed.
- "the injection test point in week three" became "in a later Evolution" because the Evolution number for the injection test point could not be confirmed from the deck.
- Run-of-show rows, timing keys, footers, and the Judgment loop shorthand line ("decision = full autonomy; cost = grounding; ...") are left unchanged (the build drops the first group; the last is course apparatus).
- Table cells on slide 7 keep their telegraphic form and semicolons (fixed-width layout; brief says reword short labels only for banned shapes).
- "A loop without a halt is a bill. Build one that stops, and can say why." and "Observations are perception. Treat them as untrusted input." (slide 14): the deck's framing lines, kept verbatim.
- "The PRD is WHAT, not HOW" (slide title): Jeffry's WHAT/HOW vocabulary; kept.
- "Rule for the semester" retains "semester" since it is the rule's name on the slide, not a schedule detail.
