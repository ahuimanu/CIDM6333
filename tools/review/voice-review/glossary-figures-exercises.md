# Voice-pass review: glossary, figures, exercises, home, lecture index, Steer the Middle mini deck

Scope: BEFORE `docs-before-387413a/` against AFTER `docs/` for `glossary/index.html`, `figures/*.html` (19), `exercises/*` (7), `index.html`, `lectures/index.html`, `lectures/mini-steer-the-middle/index.html`. Visible text only (scripts and styles stripped). `codec.py` is unchanged. The amber-to-maroon caption in `two-loops.html` is intended and is not reported. Changes that correct BEFORE against the actual files (the `git status` allowance and the codec-check skill steps in `exercises/steer-the-middle.html`) are not reported.

Findings are listed most serious first.

---

### 1. Transformer figure adds a sweeping claim about parameter counts
- **Location:** figures/transformer-2017.html, training-details caption
- **Category:** 1 (CHANGED)
- **BEFORE:** "frontier models are larger by orders of magnitude, and most labs no longer publish their sizes."
- **AFTER:** "Frontier models are larger by orders of magnitude, and since GPT-4 (2023) the labs that train them have stopped publishing parameter counts."
- **Problem:** The new sentence adds a date and a cause that are not in BEFORE, and it says all labs stopped, which is false: Meta, DeepSeek, Qwen and others still publish parameter counts.
- **Fix:** Go back to the BEFORE hedge ("most closed-model labs no longer publish their sizes"), or source the GPT-4 date and narrow the claim to closed frontier labs.

### 2. Mini deck slide numbers are wrong, and both index pages still say 15 slides
- **Location:** lectures/mini-steer-the-middle/index.html (every slide footer); lectures/index.html and index.html cards
- **Category:** 2
- **BEFORE:** 15 sections. Each footer number matched its section (slide 3 showed "3", and the last slide showed "15").
- **AFTER:** 14 sections, because the "Run of show" slide was removed. Section 2 shows "1", section 7 shows "5", and the last slide shows "12". Both index cards still read "Steer the Middle · 15 slides · web-only deck".
- **Problem:** The printed numbers no longer match slide positions, and the slide count on both index pages is now wrong.
- **Fix:** Renumber the footers to match the section order, and change "15 slides" to "14 slides" on both index pages.

### 3. Steer the Middle exercise now calls a memory record "a fact", which reverses the course's rule
- **Location:** exercises/steer-the-middle.html, step E7 "See"
- **Category:** 4 (also 2, against figures/memory-is-a-claim.html and the glossary)
- **BEFORE:** "That is the drawer from last week (Figure 14): memory is a claim with a date, and the loop does not open the drawer by itself."
- **AFTER:** "That is the memory drawer from E7 (Figure 14): a record is a fact that was true on a date, and the loop does not open the drawer by itself."
- **Problem:** The course teaches that a memory record is a claim, which can be wrong. Calling it "a fact that was true" undoes that rule, and Figure 08 and the glossary's memory-layer entry still say "memory is a claim with a date".
- **Fix:** Restore "a memory record is a claim with a date".

### 4. Plan-do-check now says the pipeline never records an attestation, but the ledger records them
- **Location:** figures/plan-do-check.html, the Sync row
- **Category:** 2
- **BEFORE:** "Sync. Ledger events, brief status, and dispatch records written. The human attests; the pipeline does not."
- **AFTER:** "Sync. The pipeline writes the ledger events, the brief status, and the dispatch records. The human attests, and the pipeline never records an attestation."
- **Problem:** The glossary's ledger entry says the ledger records "every command, verdict, gate, and attestation", and rolled-back.html fails a release that has "no attestation event". The original point was that the pipeline does not attest, not that it does not record.
- **Fix:** Write "The human attests, and the pipeline only records the attestation; it never makes one."

### 5. Glossary gives the wrong textbook chapters for the survey systems
- **Location:** glossary, entry "Other systems in the surveys" (JADE, Voyager, OpenHands, Aider, Jules, Zed)
- **Category:** 1 (ADDED)
- **BEFORE:** no "Why" line.
- **AFTER:** "Why it is in the course. The survey tables in Chapters 7 and 8 place each one in the lineage of agent platforms."
- **Problem:** In the textbook, JADE is in Chapter 4, Voyager is in Chapters 6 and 16, OpenHands and Aider are in Chapter 7, and Jules and Zed appear in no chapter.
- **Fix:** Delete the line, or name the chapters where each system actually appears.

### 6. Glossary adds a "Why" line to most entries, and many of the new lines carry new claims
- **Location:** glossary, whole page
- **Category:** 1 (ADDED) and 3 (#38 templated siblings)
- **BEFORE:** 79 "Why it is in the course" lines and 67 "Who, when" lines.
- **AFTER:** 148 "Why" lines and 87 "Who, when" lines.
- **Problem:** About 69 new "Why" lines and 20 new "Who, when" lines add content that was not in BEFORE. Some are circular ("It is in the course as the format that MCP's tool listing replaced." under OpenAPI). Some invent attributions (#5, #11, #12). Some are moral landings ("Without a squawk, a finding from the debrief has no record and no owner."; "The Final System is the proof that the student's harness can build something, and it is the point the course builds toward."). The uniform added slot is the #38 template.
- **Fix:** Keep the added "Why" lines only where BEFORE's own text moved there, and delete the rest. The new citations (Beck 2002, North 2006, SHA-2 2001, Degani and Wiener) can stay if Jeffry approves them.

### 7. Glossary persona entry makes up a writing order that contradicts the mini deck
- **Location:** glossary, entry Persona; lectures/mini-steer-the-middle, "A reviewer that cannot edit" slide
- **Category:** 2 (also 1, CHANGED)
- **BEFORE (glossary):** "The anti-trait explains; the permission deny enforces. Both, in that order."
- **BEFORE (deck):** "The deny enforces. The anti-trait explains. Both, in that order."
- **AFTER (glossary):** "The course asks for both, with the anti-trait written first."
- **AFTER (deck):** "Write both lines. The deny line stops an edit at the permission engine, and the anti-trait line tells the model the reason."
- **Problem:** BEFORE was already ambiguous. The glossary now states a specific rule (write the anti-trait first) that nothing supports, and the deck, which listed the deny first, dropped the order altogether.
- **Fix:** Have Jeffry rule on what "in that order" means. Then state that meaning, worded the same way, in both places, or remove the ordering claim from both.

### 8. Glossary handoff entry adds a reason that contradicts the window-budget figure
- **Location:** glossary, entry Handoff
- **Category:** 1 (ADDED, and DROPPED "most common") and 2
- **BEFORE:** "E6's build; the weakest of the memory strategies in Figure 14's table, and the most common."
- **AFTER:** "Figure 14's table lists it as the weakest of the memory strategies, because nothing in the loop reads it unless the next session is told to."
- **Problem:** The "because" clause is new. window-budget.html describes "a session-start advisement that loads the handoff before turn one (Claude Code's SessionStart hook)", which is a loop mechanism that does read the handoff.
- **Fix:** Drop the "because" clause, or reword it as "unless a session-start hook loads it".

### 9. The E3 card makes the permission gate, the retry rule and the halt part of a tool's contract
- **Location:** index.html and lectures/index.html, E3 card
- **Category:** 4 (also 2, against figures/the-gate-holds.html)
- **BEFORE:** "Schemas, side-effect classes, permission gating, retry, halting. The model is an untrusted caller. Hooks as a membrane."
- **AFTER:** "Each tool is a contract with a schema, a side-effect class, a permission gate, a retry rule, and a halt, and the model is an untrusted caller of it. Hooks sit between the two as a membrane."
- **Problem:** BEFORE was a list of topics. AFTER makes all five items fields of the tool contract, but the-gate-holds.html says the declaration has "Four fields, and the one the gate reads", and the gate and the halt belong to the harness. The membrane metaphor still carries the argument (#3).
- **Fix:** Write "Tools as contracts (schema, side-effect class), and the harness's permission gate, retries, and halts around them. A hook is the code the harness runs at the call."

### 10. Transformer figure narrows rotary position encoding to the Llama lineage
- **Location:** figures/transformer-2017.html, positional-encoding caption
- **Category:** 1 (CHANGED)
- **BEFORE:** "Many newer models encode position differently, for example by rotating queries and keys"
- **AFTER:** "Later models of the Llama lineage encode position by rotating the queries and keys instead"
- **Problem:** Rotary encoding (RoFormer, 2021) is used well outside the Llama lineage, for example in GPT-NeoX and PaLM, so the new attribution is too narrow and implies an origin it does not have.
- **Fix:** Restore "Many newer models (Llama among them) encode position by rotating the queries and keys".

### 11. Transformer figure adds a causal claim about attention cost
- **Location:** figures/transformer-2017.html, Table 1 caption
- **Category:** 1 (ADDED)
- **BEFORE:** "In 2026 n is a context window, far to the right of the crossing. Its O(1) sequential operations are why it trains in parallel on GPUs."
- **AFTER:** "In 2026 n is a context window, far to the right of the crossing, so the trade the paper made in favor of parallel training is now paid in attention cost at every call."
- **Problem:** The "so ... now paid ... at every call" inference is new and loose: inference cost depends on caching and kernels, and the chart itself says it ignores those.
- **Fix:** Cut the "so" clause, or write "so self-attention's per-layer cost now exceeds recurrence's on long windows".

### 12. Glossary routing entry gives the second-family adversary to E11 instead of E9
- **Location:** glossary, entry Routing and model families
- **Category:** 1 (ADDED)
- **BEFORE:** no "Why" line.
- **AFTER:** "Why it is in the course. The second-family adversary that E11's red team uses is drawn from this list."
- **Problem:** On this site, the other-family adversary belongs to E9 (claim-receipt-verdict.html: "E9 slide 17", Sortie 9's adversary tiers). Nothing in scope ties it to E11.
- **Fix:** Write "Sortie 9's adversary tier draws its other-family model from this list."

### 13. Plan-do-check adds a wrong causal link to the first falsifier
- **Location:** figures/plan-do-check.html, dispatch-record caption
- **Category:** 1 (ADDED)
- **BEFORE:** "the flight log says so and the sortie is an ABORT, not a PASS with a missing verdict."
- **AFTER:** "the flight log says so and the sortie is recorded as an ABORT, because a PASS with no verdict on record trips the first falsifier."
- **Problem:** The first falsifier on this page is "merged work with no ReviewResult on record", which is about merged work, not about a PASS, so the new "because" misstates the rule.
- **Fix:** Write "and the sortie is recorded as an ABORT; a PASS with no ReviewResult on record would be false."

### 14. Plan-do-check intro changes the reviewer criterion
- **Location:** figures/plan-do-check.html, intro
- **Category:** 1 (CHANGED)
- **BEFORE:** "a verdict counts only from a reviewer that can say no."
- **AFTER:** "a verdict counts only when it comes from a reviewer that cannot edit the work it judges."
- **Problem:** "Can say no" (can reject) and "cannot edit" are different conditions. The glossary's rule two needs both citations and no edit rights, and the intro now gives only one.
- **Fix:** Write "a verdict counts only from a reviewer that can return FAIL and cannot edit the work it judges."

### 15. Window-budget intro adds a purpose for the budget
- **Location:** figures/window-budget.html, intro; also index.html and lectures/index.html, E6 card
- **Category:** 1 (ADDED)
- **BEFORE:** "Step through the figure, then run the four compaction moves on a session and watch the stacks shrink."
- **AFTER:** "Compaction is the operation the budget exists to trigger, and the simulator runs its four moves..."; E6 card: "Compaction, progressive disclosure, subagents, handoffs, and the layers of truth each follow from that budget."
- **Problem:** Neither BEFORE text says the budget exists to trigger compaction. The same intro lists the budget's three obligations (know the contents, log the cost, decide what compaction may lose), and none of them is "trigger compaction".
- **Fix:** Delete the "exists to trigger" clause, and change "each follow from" to "are E6's tools for keeping within".

### 16. Skill figure adds a V&V requirement
- **Location:** figures/skill-on-demand.html, Final System note
- **Category:** 1 (ADDED)
- **BEFORE:** "A skill the model never calls is a procedure the system does not have."
- **AFTER:** "A skill the model never calls adds nothing to the harness, so the V&V must show the call."
- **Problem:** "The V&V must show the call" is a new grading requirement that BEFORE does not state.
- **Fix:** Have Jeffry confirm the requirement. If he does not, cut the "so" clause.

### 17. Loop figure intro adds a design rule
- **Location:** figures/loop-that-halts.html, intro
- **Category:** 1 (ADDED) and 3 (antithesis)
- **BEFORE:** "The agent loop perceives, reasons, acts, and then checks whether it must stop. This figure draws that loop as a state machine, with one labeled exit for each halt condition."
- **AFTER:** "...and then checks whether it must stop, and the check belongs in code rather than in the prompt. ... so that a run can end only through one of them and never silently."
- **Problem:** Both added clauses are new claims, and they arrive in the "rather than" and "never" antithesis cadence.
- **Fix:** Cut "and the check belongs in code rather than in the prompt" and "and never silently".

### 18. Big Pickle data-use caveat now names OpenCode as the actor
- **Location:** figures/claim-receipt-verdict.html, route table
- **Category:** 1 (CHANGED attribution)
- **BEFORE:** "Big Pickle data may be used to improve the model"
- **AFTER:** "OpenCode may use Big Pickle data to improve the model"
- **Problem:** The source does not say who uses the data (the model behind Big Pickle is undisclosed, and its provider may be the user), and the glossary keeps the passive "may be used for training".
- **Fix:** Restore the passive, or write "the provider behind Big Pickle may use..." if the OpenCode docs say so.

### 19. One-intent exercise drops the scope qualifier on prompt sentences
- **Location:** exercises/one-intent-three-drawers.html, memory-strategy table, last row
- **Category:** 1 (DROPPED)
- **BEFORE:** "A sentence in a prompt is not a mechanism; it holds in most runs, not all"
- **AFTER:** "A sentence in a prompt is not a mechanism, and Probe 3 and its rerun test whether it holds"
- **Problem:** BEFORE stated the observed behavior (it usually holds, and it fails sometimes), which is why it is not a mechanism. AFTER removes that reason and leaves only the assertion.
- **Fix:** Write "A sentence in a prompt is not a mechanism, because the model can ignore it on any run; Probe 3 and its rerun test it."

### 20. Eight figure intros drop the instruction to the reader
- **Location:** figures/claim-receipt-verdict, loop-that-halts, one-run-is-an-anecdote, pilot-and-planter, transformer-evidence, two-loops, who-owns-the-loop, window-budget (intro paragraphs); trust-boundaries drops "Then edit a tool description below and watch a pinned hash refuse it."
- **Category:** 4 (a reverse #40 regression)
- **BEFORE (example):** "Step through it with Next, the dots, or the arrow keys." (two-loops)
- **AFTER (example):** "The figure draws both loops and marks where each Evolution of the course works on them."
- **Problem:** Instructions ("Step through", "then run", "then edit") became descriptions. The reader now has to find the controls without being told, and the trust-boundaries pin panel no longer says what to do.
- **Fix:** Restore one imperative sentence per intro that says how to step and what to do in the panel below.

### 21. Exercise page walks the table "from E1 to E8", while the page says E0 to E8
- **Location:** exercises/steer-the-middle.html, paragraph after the table
- **Category:** 2
- **BEFORE:** "Tonight you walk that table from the top of the course to this week."
- **AFTER:** "In this Evolution you walk that table from E1 to E8."
- **Problem:** The same page says "This exercise walks it from E0 to E8", and the table's earliest row is E2, so "E1" matches neither.
- **Fix:** Write "from the first row to E8", or use "E0 to E8" as the rest of the page does.

### 22. Exercise intro says every table row pairs an OpenCode default, but two rows are additions
- **Location:** exercises/steer-the-middle.html, intro paragraph
- **Category:** 2
- **BEFORE:** "Most of those files are your version of something OpenCode already does by default."
- **AFTER:** "Each row of the table below pairs something OpenCode already does by default with the file you write..."
- **Problem:** The table has rows whose OpenCode column is "nothing: no store between sessions" and "an event bus", and the figure says "plus two additions". "Each" is false where BEFORE's "Most" was true.
- **Fix:** Write "Most rows pair..." and add "and two rows are additions OpenCode does not have".

### 23. Mini deck says the human "writes" both wide ends of the bar
- **Location:** lectures/mini-steer-the-middle, "The bar and its three widths" slide
- **Category:** 4
- **BEFORE:** "The model's part of the work is the thin part; the human owns both wide ends."
- **AFTER:** "The model does its work there, and the human writes both wide ends."
- **Problem:** The right end is V&V, where the human judges and does not write ("a human judges what came back" on the next slide), so "writes" misstates half the bar.
- **Fix:** Write "the human writes the specification at the left end and judges the result at the right end."

### 24. Mini deck says only evict or the retention date removes a record
- **Location:** lectures/mini-steer-the-middle, memory slide
- **Category:** 2
- **BEFORE:** "The drawer does not open itself, and it does not close itself either."
- **AFTER:** "Only evict or the retention date removes the record from the store."
- **Problem:** A retention date removes nothing by itself (exercise: "--today past that date removes it"), and memory-is-a-claim.html also offers "Forget one record by request".
- **Fix:** Write "Only an evict run, by date or by request, removes the record from the store."

### 25. Mini deck loses content from the removed run-of-show slide
- **Location:** lectures/mini-steer-the-middle, former slide 2
- **Category:** 4
- **BEFORE:** "The E8 deck, out of order: slides 3, 6, 7, 10, 11, 12" · "Push before you leave; the repository is the submission" · "Nothing is printed. The exercise page stays open beside OpenCode."
- **AFTER:** (slide removed)
- **Problem:** The times and durations were meant to go. The E8 slide list and the submission rule are content and were lost with them.
- **Fix:** Move the E8 slide list onto the title slide and "the pushed repository is the submission" onto the exercise slide.

### 26. Sprint and Drift glossary entry adds a grading claim
- **Location:** glossary, entry Sprint and Drift (method)
- **Category:** 1 (CHANGED)
- **BEFORE:** "The AI log and the Drift are how understanding is checked, rather than artifacts."
- **AFTER:** "The course grades understanding from the AI log and the Drift. The artifact on its own does not show what the student can defend."
- **Problem:** "Checked" became "grades", which is a statement about assessment policy that BEFORE did not make. The second sentence is an epigram landing (#36).
- **Fix:** Write "The AI log and the Drift, not the artifact alone, are where the course checks understanding."

### 27. Who-owns-the-loop counts "None / stdlib" as a framework
- **Location:** figures/who-owns-the-loop.html, intro
- **Category:** 1 (ADDED)
- **BEFORE:** "pick a framework from the E2 teardowns"
- **AFTER:** "The teardown panel below it takes the same question to eight frameworks from E2"
- **Problem:** The picker has eight rows, but one of them is "None / stdlib", so it covers seven frameworks.
- **Fix:** Write "to seven frameworks and the no-framework baseline from E2".

### 28. Home MAST card narrows the taxonomy to coordination
- **Location:** index.html, claim-receipt-verdict card
- **Category:** 1 (CHANGED)
- **BEFORE:** "the MAST failure matrix"
- **AFTER:** "The MAST failure matrix sorts fourteen ways coordination fails"
- **Problem:** MAST's three categories include specification and verification failures as well as coordination. The figure's own heading is "Fourteen ways a multi-agent system fails".
- **Fix:** Write "fourteen ways a multi-agent system fails".

### 29. Home one-run card drops half of what the simulator shows
- **Location:** index.html, one-run-is-an-anecdote card
- **Category:** 1 (DROPPED)
- **BEFORE:** "a simulation of how often a gate that sees few runs gets it wrong."
- **AFTER:** "The simulator counts how often a gate that sees only a few runs lets a regression through."
- **Problem:** The simulator also counts real improvements that the gate blocks (the figure says so), and the card now reports only one of the two errors.
- **Fix:** Add "or blocks a real improvement".

### 30. One-run figure label loses the pass@k and pass^k distinction
- **Location:** figures/one-run-is-an-anecdote.html, SVG label
- **Category:** 4
- **BEFORE:** "pass@k asks whether it can; pass^k asks whether it will"
- **AFTER:** "pass@k against pass^k"
- **Problem:** The label now tells the reader nothing about the difference between the two metrics, which was the label's whole content.
- **Fix:** Use "pass@k: any of k; pass^k: all of k" (about the same character count).

### 31. Attention mini-lecture card narrows the evidence and adds a justification
- **Location:** index.html and lectures/index.html, Attention (2017) card
- **Category:** 1 (CHANGED and ADDED)
- **BEFORE:** "The 2017 paper names a constraint, makes a trade, and backs it with evidence. Every model your harness calls descends from it."
- **AFTER:** "...and back the trade with their own tables. Every model your harness calls descends from this paper, which is why the course reads it as the first design record in the lineage."
- **Problem:** transformer-evidence.html lists six kinds of evidence, including attention pictures and a second task, not only tables. The "which is why" clause is a new rationale.
- **Fix:** Restore "with evidence" and cut the "which is why" clause.

### 32. Transformer figure narrows decoder-only to "the GPT lineage"
- **Location:** figures/transformer-2017.html intro; index.html card
- **Category:** 1 (CHANGED)
- **BEFORE:** "which half of the 2017 model today's chat models kept."
- **AFTER:** "which half of the 2017 model the chat models of the GPT lineage kept."
- **Problem:** Nearly all current chat models are decoder-only, not just GPT's descendants, so the scope is now narrower than the fact. (The pre-norm sentence's new "GPT-2 and the models after it" has the same over-general ending; its Xiong et al. citation is already in the page's references.)
- **Fix:** Restore "today's chat models".

### 33. Surviving epigram landings and antithesis in AFTER
- **Location:** several
- **Category:** 3 (#36)
- **AFTER examples:** window-budget.html "A file's length on disk is a different number."; trust-boundaries.html "Each catches what the other misses, so you need both."; claim-receipt-verdict.html "the adversary's size has no bearing on that."; rolled-back.html "a scenario that is only written proves nothing about the contract."; glossary Sortie "a claim without a sortie is an opinion" (kept from BEFORE).
- **Problem:** Each line closes its paragraph with a turn of phrase that adds no information.
- **Fix:** Delete each line, or fold its reason into the sentence before it.

### 34. "A sentence in the prompt is a request" is now a recurring template
- **Location:** plan-do-check.html, glossary (Hook, Guardrail), receipts-over-narrative.html, pilot-and-planter.html, mini deck
- **Category:** 3 (antithesis cadence, #38)
- **AFTER examples:** "whereas a sentence in the prompt is a request the model may ignore" (plan-do-check, glossary Hook, identical wording); "A sentence in a prompt asks the model to refrain and cannot itself refuse" (glossary Guardrail)
- **Problem:** The same contrast appears in the same wording in at least six places, and two of them are word for word.
- **Fix:** Keep the contrast in the glossary Guardrail entry, and elsewhere state only the mechanism (for example, "the harness enforces the deny on every call").

### 35. Expansion card loses the "has passed" condition
- **Location:** glossary, entry Expansion card
- **Category:** 1 (DROPPED)
- **BEFORE:** "usually after a center-of-envelope sortie has passed."
- **AFTER:** "The expected order is a center-of-envelope sortie first, then the expansion."
- **Problem:** The condition that the center sortie passed is gone, so the rule now concerns order only.
- **Fix:** Write "after a center-of-envelope sortie has passed".

### 36. Design Analysis frequency changed from "most lectures" to every lecture
- **Location:** glossary, entry Design Analysis
- **Category:** 1 (CHANGED)
- **BEFORE:** "one is done live in most lectures."
- **AFTER:** "the Teardown segment of a lecture performs one live."
- **Problem:** The revision removed the "most" (invented authority) but now implies that every lecture has one, which is a stronger and still unsourced claim.
- **Fix:** Write "the Teardown segment of a lecture, when it has one, performs one live."

### 37. Claim-receipt-verdict adds a dated term label and "the commit" to the receipt
- **Location:** figures/claim-receipt-verdict.html, intro and adversary-tier note
- **Category:** 1 (ADDED)
- **BEFORE:** "The harness that ran the tests and wrote down the exit code has produced evidence." · "tier 1 is cheap this term"
- **AFTER:** "the receipt the harness writes when it runs the tests itself (the command, the exit code, the commit)" · "tier 1 is cheap in Fall 2026"
- **Problem:** The glossary's receipt entry lists the command, the exit code, the output hash and the time, not a commit. "Fall 2026" adds a date where the pass was told to remove them.
- **Fix:** Use the glossary's field list, and write "tier 1 is cheap on OpenCode Go" with no date.

### 38. n-plus-m narrows the protocol ecosystem to implementers
- **Location:** figures/n-plus-m.html, ecosystem caption
- **Category:** 4
- **BEFORE:** "A healthy protocol ecosystem, in the deck's list, needs..."
- **AFTER:** "A protocol with a healthy set of implementers needs, in the deck's list, ..."
- **Problem:** The list that follows (a registry, governance, a versioning policy) is about more than implementers, so the new subject does not fit its own predicate.
- **Fix:** Write "A protocol, in the deck's list, stays healthy only with...".

---

**Counts by primary category (38 findings):** 1 = 23 · 2 = 6 · 3 = 2 · 4 = 7. Secondary tags: #3, #8 and #9 also count under 2; #6, #9 and #17 also count under 3.

---

## Repair log

Repair pass, Oct 22, 2026. Glossary edits are in `tools/sitekit/glossary_data.py` (parses); all other edits are in place under `docs/`.

1. FIXED. transformer-2017.html: restored "and most labs no longer publish their sizes"; GPT-4 date and cause removed.
2. FIXED. Mini deck footers renumbered to match position (2–5, 7–14; title and embedded figure carry no number); initial counter "1 / 14"; both index cards now "14 slides". The run-of-show removal stands (Jeffry's ruling).
3. FIXED. exercises/steer-the-middle.html E7 "See": "a memory record is a claim with a date".
4. FIXED. plan-do-check.html Sync row: "The human attests, and the pipeline records the attestation but never makes one."
5. FIXED. Glossary JADE/Voyager/... Why line now gives textbook chapters: JADE Ch. 4, Voyager Chs. 6 and 16, OpenHands and Aider Ch. 7 (Jules and Zed appear in no chapter, so not named). The entry's own `ch=(7, 8)` is pre-existing and left; see FOR JEFFRY.
6. FIXED. Glossary added lines checked against BEFORE, the course pages and topic-guide.md. Kept where the content moved from BEFORE's own text or is in the textbook/course pages (e.g. Gemini CLI, AP2, OWASP, RAG, Ollama, Langfuse, Anthropic, OpenAI, Invariant Labs, Linux Foundation, GAIA, WebArena, BLEU, Berkeley, Transformer, Degani and Wiener, SDK, System card, Google ADK, Computer use, Context rot, AI governance, Background agents, Harness knobs, gzkit founding docs, S&D essays, Incident casebook, Spec-driven kits; Ledger "The term is gzkit's" per Appendix D; Layers of truth ADR-0.0.9 per the E6 page; Routing citations per the E9 page). Deleted as unsupported or circular: Why lines for Final System, Covenant, Attestation, Brief, PRD, Expansion card, V.I.B.E.S., Controller/worker/reviewer, Exceptional, Route A/B, Judgment loop, GitHub Copilot, OpenAPI, CrewAI, HumanEval and ToolBench (neither is among E10's five: SWE-bench, GAIA, tau-bench, WebArena, AgentBench), LLM, Enforcement locus, Marker-file gate, Trust doctrine, MX mode, Canary, Attack card, Dispatch record, Deployment vocabulary, Toolkit, Memory retrieval vocabulary, ADR-1 apparatus; Who-when lines for Canary, Red team, TDD/BDD (Beck 2002, North 2006) and SHA-256 (SHA-2 2001), none of which the textbook or course pages support. Reduced to supported content: gz commands, BabyAGI, JSON-RPC, AutoGen, Two-stage review, MAST FC1–FC3, MCP threat mechanisms, Rollback, Chase and Squawk Who-when. Changed BEFORE lines that gained new claims were restored: Squawk, Falsifier, Index zero, Receipt, Nine failure modes, ReviewResult, Permissions, Compaction, Memory layer, SWE-bench ("first of the five" cut), Golden set ("run twice" cut), Agentic AI, Sortie Who-when.
7. FOR JEFFRY. Restored BEFORE's ordering in both places (glossary: "The anti-trait explains the rule to the model, and the permission deny makes the harness enforce it. Both, in that order."; deck: "Write both lines, in this order: the deny line stops an edit at the permission engine, and the anti-trait line tells the model the reason."). The two orders contradict each other, as they did in BEFORE.
8. FIXED. Glossary Handoff: "because" clause dropped; "and as the most common" restored.
9. FIXED. E3 card (both index pages): "Tools as contracts with a schema and a side-effect class, and the permission gating, retries, and halting the harness puts around them. The model is an untrusted caller, and hooks run between its call and the tool." Membrane metaphor removed from the card (the glossary Hook entry still quotes E3's "a membrane", pre-existing).
10. FIXED. Restored BEFORE: "Many newer models encode position differently, for example by rotating the queries and keys". Did not add "Llama among them" (new name).
11. FIXED. "so ... paid in attention cost at every call" cut.
12. FIXED. Glossary Routing Why: "The second-family adversary in E9's build is drawn from this list." (E9 page: "Build: a second-family adversary".)
13. FIXED. plan-do-check: restored "recorded as an ABORT, not as a PASS with a missing verdict."
14. FIXED. plan-do-check intro: restored "a reviewer that can say no".
15. FIXED. window-budget intro: "exists to trigger" removed; E6 card: "The deck then covers compaction, progressive disclosure, subagents, handoffs, and the layers of truth."
16. FIXED, and FOR JEFFRY. Restored BEFORE "A skill the model never calls is a procedure the system does not have."
17. FIXED. Both added clauses cut from loop-that-halts intro.
18. FIXED. Restored passive "Big Pickle data may be used to improve the model".
19. FIXED. "A sentence in a prompt is not a mechanism, because it holds in most runs, not all; Probe 3 and its rerun test it".
20. FIXED. One imperative sentence restored in all eight intros, plus trust-boundaries' "edit a tool description and watch a pinned hash refuse it". Two added claims in those intros also removed: trust-boundaries "because the server's scope check is the only check that reads the token itself"; one-run "which is the reason one run is an anecdote".
21. FIXED. "from E0 to E8".
22. FIXED. "Most rows ... and the other two rows are additions."
23. FIXED. "The human owns both wide ends: the human writes the specification at the left end and judges the result at the right end."
24. FIXED. Restored BEFORE meaning: "The loop does not open the drawer by itself, and it does not close the drawer by itself either."
25. FIXED. Title slide now says the lecture "takes slides 3, 6, 7, 10, 11, and 12 of the E8 deck out of order"; exercise slide step 10 ends "the pushed repository is the submission".
26. FIXED. "The AI log and the Drift, not the artifact alone, are where the course checks understanding."
27. FIXED. "pick one of seven frameworks or the no-framework baseline from the E2 teardowns".
28. FIXED. "fourteen ways a multi-agent system fails".
29. FIXED. "or blocks a real improvement" added back.
30. FIXED. Heading now "pass@k: any of k passes; pass^k: all of k pass" (matches the panel's own definitions).
31. FIXED. "back the trade with evidence"; "which is why" clause cut (both index pages).
32. FIXED. "today's chat models" restored in the lede and the home card; pre-norm note restored to "Most later models" (Xiong et al. citation kept; it is in the page's references). The "Decoder-only · GPT lineage" button label is from BEFORE and was left.
33. FIXED. window-budget folded into the previous sentence; trust-boundaries "so the sortie needs both controls"; claim-receipt-verdict "Choose the tier for its independence from the worker's blind spots, not for the size of the adversary model"; rolled-back "The scenarios are executed, not only written"; glossary Sortie epigram cut.
34. FIXED where the pass introduced it: plan-do-check ("The harness enforces the deny, and the anti-trait only explains it"), glossary Hook (contrast removed; Guardrail keeps it), pilot-and-planter step text (restored "A sentence in the prompt is not a mechanism"). LEFT the receipts-over-narrative and pilot-and-planter Final System lines and the mini deck E9–E10 line: their wording is BEFORE's.
35. FIXED. "usually after a center-of-envelope sortie has passed" restored.
36. FIXED. "the Teardown segment of a lecture, when it has one, performs one live".
37. FIXED. Lede now "with the command and its exit code" (no commit); "tier 1 is cheap on OpenCode Go".
38. FIXED. "A healthy protocol ecosystem needs, in the deck's list, ..." (BEFORE subject restored).

### For Jeffry
- Persona order (#7): glossary says the anti-trait comes first; the mini deck lists the deny first. Both say "in that order". Which order is meant, or should the ordering claim go?
- Skill V&V (#16): the pass had written "A skill the model never calls adds nothing to the harness, so the V&V must show the call." Reverted to BEFORE. Is "the V&V must show the call" a Final System requirement?
- Citations removed from the glossary (#6): TDD/BDD "Kent Beck, Test-Driven Development: By Example (2002); Dan North, 'Introducing BDD' (2006)" and SHA-256 "NIST's SHA-2 family (2001)". Neither the textbook nor the course pages carry them. Restore if you approve.

### Pre-existing (in BEFORE and AFTER, not fixed)
- Glossary receipt fields (command, exit code, output hash, time) differ from the E9 deck's (command, exit code, commit, output hash).
- Glossary JADE/... entry `ch=(7, 8)`: the textbook has JADE in Ch. 4, Voyager in Chs. 6 and 16, OpenHands/Aider in Ch. 7, Jules and Zed nowhere. HumanEval `ch=(19,)`: Chapter 19 does not mention it. ToolBench `ch=(19,)`: the textbook has it in Chs. 6 and 12.
- Glossary persona order vs mini deck order (see #7).
