# Voice pass log: deck e7-memory (Oct 22, 2026)

Files edited in place:
- `/home/claude/site/tools/sitekit/voice/e7-memory.json` (26 of 494 values changed; keys untouched; order unchanged; valid JSON)
- `/home/claude/site/tools/review/voice-pass/notes/e7-memory.json` (29 of 29 lecture paragraphs rewritten; every "Cut from slide N" section, every "Instructor checks" section, the paragraph-break count, and the sources list on slide 29 are byte-identical to the original; valid JSON)

Chain run: humaniser (full), ste-voice (rules 1 to 4 on the notes, `ste_check.py` on the extracted lecture text), scholarly-voice (course register, last), then the humaniser greps and shape battery as a check only (six sentence-level fixes, no redraft).

## Patterns that dominated

**"Tonight's claim" / "the claim" as thesis stand-in (BRIEF house rule).**
- Slide heading: "Tonight's claim, which Sortie 7 will try to disprove" → "What Sortie 7 will try to disprove"
- Notes 3: "The claim is the one in chapter 16." → "The design claim for Sortie 7 comes from chapter 16."
- Notes 12: "How you measure the claim." → "The on/off protocol is how you test the design claim."
- Table cell: "fails the Sortie 7 claim" → "fails the Sortie 7 design claim" (course vocabulary)

**"names"/"named"/"Name" as verb or modifier (nine slide values, one notes sentence).**
- "Name the kind before you pick the store" → "State the kind before you pick the store"
- "each change names what it supersedes" → "each change records what it supersedes"
- "'MemGPT' names the pattern" → "'MemGPT' is the pattern's name"
- "Named writers: user, rule, or agent" → "A stated writer: user, rule, or agent"
- "A named source for the incident casebook" → "A source listed for the incident casebook"
- Notes 17: "the neighbor named Adam Smith" → "a neighbor whose name is Adam Smith"

**Time and management asides (tonight, this week, last week, one-thirty, Friday night, Saturday the twenty-fourth, 11:59, homework).** All replaced with "this Evolution", "E6", "the reference-design section", or "the course-calendar date". Slide 28's dated schedule paragraph in the notes is now a dates-free statement of the written Go/No-Go and Chase steps. Slide title "Two retrievers you can run tonight" → "Two retrievers for the lab".

**Epigram and antithesis closers (#36; house "not X" ban).**
- Notes 4: "it has no state, it has a story" → the mechanism: "the loop cannot validate the goal, compare it with the last one, or test it, so the paragraph does not count as state."
- Slide: "That is flight-log data, not a reason to switch models." → "Record that in the flight log; do not switch models."
- Slide: "A memory you can replace, you can correct." → "A replaceable index can be corrected; weights cannot." (a real partition, both sides carry content)
- Notes 11: "Retention is where memory stops being a feature and becomes governance." → "A retention rule is where memory becomes a governance question, because each of its four answers assigns a right or a duty to someone."

**Invented authority (#37).**
- Slide: "Most course systems need episodic plus a small semantic store." → "Sortie outcomes are episodic and project facts are semantic, so those two stores fit a course system."
- Notes 4: "For most of your systems the answer is..." → derived from what a course system produces.
- Notes 20: "ChatGPT has the most controls" → the controls listed instead.
- Notes 1: "that fact shapes every design decision below" cut on the check-only rerun.

**Pseudo-cleft reveals.** "retrieval is what the course adds" → "the course adds retrieval"; "The ledger beside the store is what makes the store auditable" → "The ledger beside the store makes the store auditable, since it says what the store held on any date."

**Gerund and nominalization subjects (STE rule 3).** "Changing the model means re-embedding the store" → "A change of model requires re-embedding the store"; "Switching models means..." → "A switch of model means..."; "The decision to let the model manage its own memory buys..." → "If the model manages its own memory, the system gains..."; "The argument is auditability." → "The reason is auditability: a file can be diffed..."

**Argued or gerund headings (#32).** "Retention is governance" → "Retention as governance"; "Measuring memory: the on/off protocol" → "How to measure memory: the on/off protocol".

**"we" (house rule).** Slide subtitle "we fill the right column together" → "the class fills the right column together"; notes 21 "I will fill the right column with you... the answer we should land near" → "I fill the right column with the class, and the slide holds the answer the discussion should land near."

**Parts lists restored to sentences (scholarly-voice last).** Notes 25 (lens) and 26 (card) were comma-chained fragments; each band and each card field now sits in a full sentence with its reason (e.g., "a quiet substitution mid-flight would change the system under test").

**Fact repair while rewriting.** Notes 16 (RAG) said "swap a 2016 index for a stale one and accuracy on current leaders falls from seventy percent to four", which misstates the experiment; the slide wording (2016 index on 2016 leaders 70%, 2016 index on 2018 leaders 4%) is now what the notes say. Notes 19 (Reflexion) "one in six" → the slide's 16.3%.

## Self-audit artifacts (notes, after the final pass)

Closer list (last sentence of each lecture paragraph):
- The lab is self-guided and works with or without Ollama.
- The Go/No-Go and the Chase review are written steps in your repository, and the Sprint brief gives the dates.
- It has two halves, recall and forgetting, and three falsifiers: a fact that was never stored, an item kept past its rule, and retrieval that changes an answer it had no business changing.
- Write the kinds down before you build; the choice of store follows from them.
- A recalled sentence that traces to no record and no source file is a fabrication (App. C #3) even when it happens to be true, because nothing in the system can show how it got there.
- A run with memory off is the control that shows which of these happened.
- I checked the OpenCode Go and Zen documentation on September 24: neither offers an embeddings endpoint, so the course harness provides no hosted route, and no one needs another API key for this Evolution.
- A question set with no paraphrase question cannot distinguish the two retrievers, so a sortie without one has not tested the choice made in ADR-2.
- The strip states the policy: path A and path B both count for Sortie 7, and the card records which one you flew.
- Only the rule path yields a test the Chase can check (an id with an evict event, absent from the store, and no longer recalled), so the rule path is the one Sortie 7 flies.
- In other words, deletion of a derived store is a separate operation from deletion of its source, and your system needs that operation.
- If Big Pickle or a flash model gets the control wrong, that is a finding for the flight log; you record it, and you do not swap models to make the numbers look better.
- When an attacker plants the stale fact on purpose, OWASP's December 2025 list for agentic applications calls it ASI06, memory and context poisoning.
- I issue your personalized Final System brief on the course-calendar date, drawn from what your Drifts and sorties have shown; do not start the Final System before it arrives.
- Bring an answer back; the teardowns test it against four designs that answered the same question differently.
- The failure mode is fabrication (App. C #3), because the generator is free to answer beyond its passages; retrieval gives provenance only when the answer cites what it used.
- The strip connects to E9: a reflection that carries no pointers to its evidence is a summary nobody can check.
- The failure mode follows from the model owning its own memory: a wrong fact in the working block is read on every turn, and a correction the model does not save is lost (App. C #5).
- This is App. C #9, metagaming the gate, and it is the reason Sortie 7 checks each answer against the source file rather than against the model's own grading.
- Verify the table against the vendors' pages before you rely on it, because these features change monthly.
- If you choose MemGPT for your Design Analysis, this slide is a start; rebuild the analysis from the paper rather than copying the slide.
- Verify the count, the command syntax, and what the OKF bundle and gz context contain against the repository; I have not described them beyond what the topic guide states.
- Verify the dates and counts against CHANGELOG.md and the insights corpus.
- If you want a memory to be canon for some fact, ADR-2 has to argue the case.
- An exceptional Sortie 7 compares both retrievers on the paraphrase row, runs the chapter 16 exercise of planting one false record and measuring how many answers it changed before the forget event removed it, implements supersedes, sets a clock per kind with a reason for each, and chooses its threshold from data.
- Your Chase writes it under the card in the repository, and the Sprint brief gives the date.
- The lab is a first measurement; the five test points fly in the Sprint.
- I issue your personalized Final System brief on the course-calendar date; read it before E8, and do not start the Final System before you have it.
- Commit the card for your Chase on the course-calendar date. (followed by the unchanged sources list)

No line works as a caption or moral on its own; each carries a condition, a reason, or an instruction. "A memory is a claim with a source, and forgetting is an event" opens the close and is course vocabulary.

Lede list (first sentence of each paragraph):
- Evolution 7. In Evolution 6 you budgeted the window and wrote a handoff so that a fresh session could pick up where the old one stopped.
- The lecture runs in eight parts: framing, the spine, ADR-2, a break, the teardowns (one Design Analysis worked on the board), the reference design, the evaluation lens with the card, and the lab brief with the Sprint.
- Framing. The window you budgeted in Evolution 6 is gone when the session ends; memory is the part of it you chose to keep.
- Chapter 16 distinguishes five kinds of memory, and the sixth card on the slide is the question ADR-2 answers.
- The record is where the first rule becomes code.
- Retrieval has five steps, and each is an ADR-2 decision.
- Two retrievers, both in the lab's single file.
- The table is a worked example from the lab tool, run on two short synthetic flight logs.
- The slide lists four models you can pull, with the numbers from the Ollama library pages as of September 24.
- State first. Working state is a typed object the loop owns; the model proposes a change and the loop validates it before writing, which is the same contract your tools followed in E3.
- A retention rule is where memory becomes a governance question, because each of its four answers assigns a right or a duty to someone.
- The on/off protocol is how you test the design claim.
- The common mistake. Chapter 16 calls memory a vibing surface, by which it means a stale fact recalled as if it were current truth.
- ADR-2 is the memory decision.
- Break. The question on the slide is ADR-2 in miniature: one fact, one clock, and one person with the right to delete.
- RAG, read for its mechanism.
- Generative Agents. The mechanism is the memory stream and a retrieval score that adds three terms with equal weight: recency, importance, and relevance.
- MemGPT to Letta in four steps.
- Reflexion, in the authors' own sentence.
- Four shipping memory systems, read for the four retention questions.
- The live Design Analysis.
- The reference design.
- Four dated episodes from Appendix G, read as memory failures.
- Memory has a place in the layers of truth from E6.
- The evaluation lens has three bands.
- Flight Card 7 is an expansion card with a local retriever.
- The lab brief. You run the lab on your own laptop, and the handout is complete without me.
- The Sprint has five deliverables: the Sortie 7 flight log, the memory layer, the retention rule per kind with ADR-2, a Design Analysis of one memory system, and an AI_LOG entry.
- Close. A memory is a claim with a source, and forgetting is an event.

The lecture-paragraph ledes keep the deck's convention of a short label ("RAG, read for its mechanism.") because the panel under the viewer is keyed to a slide; the run-of-show line (paragraph 2) and the Sprint line (28) open on a counted list because the slide is a list. No "X is Y: a, b, c" definition lede remains in an explanatory paragraph.

Claim list (frequency or consensus statements):
- "Nomic-embed-text is the most pulled embedding model on Ollama." Source: the Ollama library page, cited in the sources list (ollama.com/library/nomic-embed-text), slide wording unchanged.
- Everything else matching "every", "nobody", "no one" is a rule or a mechanism ("every record carries a date", "every tool denied", "nothing is ever deleted"), not an authority claim.
- Removed: "Most course systems", "For most of your systems", "the most controls", "shapes every design decision below".

## ste_check lines declined, and long sentences kept

- Sentences over 25 words (50 in the notes): declined as a class. The brief applies STE rules 1 to 4 only to explanatory paragraphs, and the speaker notes are all explanatory. The longest (the three lens-band sentences at 48 to 52 words, the card falsifier sentence at 47, the discipline sentence at 48) each carry a list of conditions that would lose precision as fragments, which is the shape the notes had before and that scholarly-voice was asked to restore as sentences.
- Paragraphs over six sentences (24): declined; one paragraph per slide is fixed by the brief ("do not merge or split slides").
- Gerund/nominalized subjects flagged: "Three eviction policies follow", "The evaluation lens has three bands", "The instrumentation is...", "The judgment loop at the bottom reads as follows" are slide elements or stipulated terms, not judgments; declined. "The decision to let the model..." and "The argument is auditability" were real hits and were fixed.
- Passives with no actor: "what is known", "what is remembered", "is typed", "is derived", "can be diffed", "is graded against" are definitional and the actor is unknowable or stated in the clause; declined. "Each answer is checked" and "is issued" (twice) were fixed with "You check" and "I issue".
- Noun clusters: all 4+ hits are URL fragments in the sources list or adjective runs ("two short synthetic flight logs"); declined.
- Semicolons (53): allowed in explanatory paragraphs by the brief.

## Left as is, with reason

- Flight Card 7 block (slide 26, keys from "FLIGHT CARD — SORTIE 7" through "SPRINT  Sortie 7 log"): contains an em dash, "what the retention rule names", and "named ids". The block reproduces the card document in fixed-width layout; I treated it as quoted course material and did not edit it. If the card file itself is revised, these values should follow it.
- Run-of-show row "Memory is the part of context that survives; two rules; tonight's claim and what falsifies it" (slide 2) and the title "Homework: the E7 Sprint" (slide 28): dropped or session-running lines per the brief; left unchanged even though the first carries "tonight's claim".
- Check dates on slides ("checked 09/24/2026", "Run 09/24/2026", "Library pages checked 09/24/2026", "Vendor help pages and release notes checked 09/24/2026; these change monthly. Re-check the week of class."): these are the instructor's provenance dates for vendor facts, which the brief says never to edit, not QA asides about this pass. Left.
- "Chunking error, not a model error", "a pass can satisfy the check, not the intent", "Two were memory that was wrong; two were memory that was right and not read": contrasts where both sides carry content (a real partition), left.
- Slide 25 lens rows remain fragments: table cells.
- "Prose is not state." (slide 10) and "A memory is a claim with a source." (slides 3, 29): course rules in course vocabulary, left.
