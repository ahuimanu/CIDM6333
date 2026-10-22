# Pass log: topic-guide-1

File: `/home/claude/site/tools/review/voice-pass/tg/chunk1.md` (Course Topic Guide front matter, preface, "Using this book", chapters 1 to 7). Chain run in the brief's order: humaniser (full), ste-voice (rules 1 to 4 on paragraphs, full rules on procedures and bullets), scholarly-voice (last), humaniser battery as check only. Original kept at the scratchpad path `/tmp/claude-0/-home-claude/acdec67e-a228-569c-b4b7-fc7975fc3d39/scratchpad/tg1/chunk1.orig.md`.

Structure checks after the pass: every `# ` heading byte-identical to the original; table-row count (58), fence count, bracket-link count (4), subheading count (84) and list-item count (114) unchanged. 55 original lines changed, about 40 distinct edits.

## Changes by pattern

### Em dashes (house ban)
- Table thread labels: `**Survey** — why are...` → `**Survey**: why are...`; same for `**Build**`.
- Six empty cells in the Chapter-to-Evolution map (`| — |`) → `| none |`. The heading em dash on line 1 stays, per the brief.
- En dashes in ranges and compound terms (`1–2`, `4:00–6:30`, `belief–desire–intention`, `controller–worker`, `agent–computer`, `2020–2022`) are not em dashes and were left.

### "name" as a verb (house ban)
- "name the decision, the characteristics privileged..." (Conventions, and 2.5 The judgment loop) → "state the decision, ..., and the preservation mechanism." See "unsure" below.
- "mark every box you can already name a concrete system for" → "mark every box for which you can already give a concrete system."
- "Read the ReAct paper as a design document and name its components" → "and list its components."
- "Why they mattered anyway: they named the ambition." → "They mattered anyway, because they stated the ambition the field then pursued."
- Heading `### 7.5 Patterns named` → `### 7.5 The pattern vocabulary` (modifier form of the banned verb; still a label).
- Noun use kept: "three names for the same failure."

### "we" and actorless passives (#3, #5, #31; STE rule 2)
- "the one system for which we have the entire record, including what went wrong" → "for which this book has the entire record, including the record of what went wrong."
- "the difference is that here we kept the receipts" → "The kit differs in that its ledger kept the receipts for each one."
- "a governance kit was started with eleven days to go before it would be shown to students" → "I started a governance kit with eleven days to go before I would show it to students" (instructor speaking about his own decision).
- "Sprint and Drift ... was developed for CIDM 6330" → "I developed Sprint and Drift, the method of Part IV, for CIDM 6330."
- "the prose is being written in the order the course needs it" → "I am writing the prose in the order the course needs it."
- "The question asked of every system is the same:" → "Part II asks the same questions of every system:".
- "every box is assigned a chapter (table)" → "The table assigns every box a chapter."
- "Why the foundation is forgotten: it is unglamorous and it is where the cost lands" → "Designers neglect the foundation because it is unglamorous, and the cost lands there."
- "a design choice to be analyzed" → "a design choice for analysis."

### Epigram landings and mirrored pairs (#36; cadence bans)
- "The title is the thesis. *A system can produce an answer without being able to answer for it.* The engineer's irreducible role is answerability. Everything here is in service of building systems, and engineers, that can answer." → "The title states the thesis: a system can produce an answer without being able to answer for it. The engineer's role, the one no tool takes over, is to answer for the system. The survey, the build, and the governance chapters all serve that purpose."
- "Agentic AI is thin and new; the foundation is old and cracked." → "The agentic layer is the newest and thinnest, and the data foundation is the oldest and the one with the defects."
- "the cost of generated code is deferred, never erased" → "generated code defers its cost rather than removing it."
- "A loop without a halt condition is a bill." → "A loop without a halt condition runs until the budget is spent, so the halt condition is the cost control." (The reason the slogan compressed, stated.)
- "is BDI's commitment problem with a ledger" → "is BDI's commitment problem, with a ledger added to record the commitment."
- "And it is not neutral: it holds that..." (fourth "It is not" in a row, antithesis closer) → "The book takes a position: the human is index zero, ...".
- "you do not understand a component you have not had to make fail on purpose" → "a reader understands a component only after making it fail on purpose."

### Invented authority (#37)
- "Most production "agents" are workflows, and should be." → "Anthropic's own advice is to build the workflow unless the task needs the agent's flexibility, and a system marketed as an "agent" may be a workflow by this definition (exercise 2)." Source is the listed reading (Anthropic, "Building Effective Agents," 2024).
- "Frameworks change monthly" → "Frameworks change too often for a tutorial to stay current" (the premise without the unsourced rate).

### Definition-colon ledes (#35)
- "gzkit sits on the *agentic* layer without running a model at all: it is a governance meta-harness..." → "gzkit sits on the *agentic* layer and runs no model of its own. It is a governance meta-harness one tier above the vendor harness, and that placement is..."
- "This chapter *is* the reference design's doctrine: charter, lineage, genesis, command doctrine." → "This chapter is itself the reference design's doctrine, set out in four documents: charter, lineage, genesis, and command doctrine."
- "gzkit's genesis (2026-01-12) is the loop plus the thing the loop lacked: a record of intent" → "is the ReAct loop plus the one thing that loop lacked, a record of intent that survives the session."

### Semicolons (STE rule 9, course register)
Removed from prose and from outline bullets where they separated fragments: Acknowledgements (GovZero/gzkit sentence), 1.1, 1.3, 3.2, 3.4, 3.5, 3.6, Ch. 3 reference design, 4.1, 4.2, 4.3, 4.4, 5.1, 5.2, 6.3, 7.3, 7.4, 7.5. Each became a period or an "and".

### AI vocabulary (#7)
- "the first tool ecosystem and its failure" → "the first tool store, and why it failed."
- "Reference servers and the ecosystem" → "Reference servers and the community of servers around them."

### "the move"
- "Governance move to a foundation (2025)" (the word in its ordinary sense, but replaced to be safe) → "Governance transferred to a foundation (2025)."

### Procedures (STE)
- Exercise 1.1 split into two instructions: "...nine components each. Add one paragraph on what the harness adds and what it costs."
- 3.5 Command doctrine tenets: four semicolon-joined "X, not Y" fragments → one sentence introduced as "The four tenets of the command doctrine:" with "rather than" in place of the ", not" cadence.

## Self-audit artifacts (after the final pass)

### Closer list (last sentence of every prose paragraph)
- This book does three things at once because the course it grew out of does the same three things in the same term.
- The survey, the build, and the governance chapters all serve that purpose.
- The outlines are complete, and I am writing the prose in the order the course needs it.
- The kit differs in that its ledger kept the receipts for each one.
- Around it is a survey, because ..., and a build, because a reader understands a component only after making it fail on purpose.
- The book takes a position: the human is index zero, first in priority and final in authority, and a system whose human cannot answer for it is not finished.
- The essays that open each chapter first appeared in the *Sprint and Drift* newsletter.
- The weekly rhythm (...), the Sprint and Drift method, and the scoring live in Part IV and in the [run sheet].
- It is a governance meta-harness one tier above the vendor harness, and that placement is the first design choice the book examines.
- It deliberately leaves components one through six to the vendor harness.
- That exchange is the book's founding episode.
- Its "intent preservation across context boundaries" is BDI's commitment problem, with a ledger added to record the commitment.
- Read the genesis transcript alongside ReAct.
- See ch. 10.
- gzkit's controller–worker pipeline (ADR-0.18.0) explicitly borrows from role-based designs, then adds what they lacked: a fail-closed result contract and an independent reviewer whose claim is not evidence.
- The book treats that refusal as a design choice for analysis, and offers "an MCP server over gz verbs and the ledger" as a student project (ch. 13).

Verdict: none works as a slogan out of context; "That exchange is the book's founding episode" is short but states a fact about the genesis transcript rather than a moral. "whose claim is not evidence" is gzkit vocabulary and stays.

### Lede list (first sentence of every prose section)
- This book does three things at once because the course it grew out of does the same three things in the same term.
- The title states the thesis: a system can produce an answer without being able to answer for it.
- Every chapter carries a status line: *outline*, *draft*, *reviewed*, *final*.
- In January 2026 I started a governance kit with eleven days to go before I would show it to students.
- That record is the spine of this book.
- This book is not a framework tutorial.
- I developed Sprint and Drift, the method of Part IV, for CIDM 6330 (Software Architecture).
- The course runs thirteen Thursdays, 4:00–6:30 p.m., one Evolution per week.
- gzkit sits on the *agentic* layer and runs no model of its own.
- gzkit answers component eight (governance and human interface) with the Zero Doctrine and Gate 5, and component seven (evaluation) with gates, receipts, and RED witnesses.
- This chapter is itself the reference design's doctrine, set out in four documents: charter, lineage, genesis, and command doctrine.
- gzkit's personas, locks, and structured result contracts are FIPA-shaped.
- gzkit's genesis (2026-01-12) is the ReAct loop plus the one thing that loop lacked, a record of intent that survives the session.
- Sortie 1 (center): *a governed agent loop that halts*.
- gzkit's controller–worker pipeline (ADR-0.18.0) explicitly borrows from role-based designs, then adds what they lacked: ...
- gzkit does not use MCP, by doctrine: no external protocol may be a prerequisite for core governance operations.

Verdict: the seven "Reference design: gzkit" sections share a subject by design (the reader looks for the same thing in the same place in each chapter), and each lede states a different fact; the sibling rule permits this. "Every chapter carries a status line: ..." is a list of four status values, not a definition by apposition, and was left. The "Learning outcomes" sections all open "After this chapter you can:" by design (fixed template, kept).

### Claim list (frequency and consensus claims)
- "the systems built in industry have them too" (Preface). Kept: the source is the author's own governed airline-operations project (Acknowledgements, "roughly a hundred work items"), and the claim is that industry systems share these failure modes, which the ten-deep subagent and marker-file incidents instantiate. Flagged for Jeffry in case he wants a citation.
- "Most production "agents" are workflows" → removed; replaced with Anthropic's advice (sourced to the listed reading).
- "Frameworks change monthly" → removed the rate; kept the premise.
- Structural "every" (every chapter, every box, every Design Analysis, every system in Part II) describes the book's own layout and is not a frequency claim.

## ste_check lines declined, with reasons
- Sentences over 25 words (12 remaining): all in explanatory paragraphs, where the brief imposes no ceiling. The 84-word preface sentence carries four counts and four dated failure modes and loses precision if split. The two "It surveys / It builds / It governs" sentences each carry the full list of what a Part covers.
- Nominalized subjects: "The reference design throughout is gzkit" (stipulated term, allowed), "Which perception choices raised the resolve rate?" (exercise question; "perception" is a component name).
- Passive "look finished without being finished" (an agent is the actor; the construction is the point), "runs until the budget is spent" (the loop spends it; agent implied).
- Noun clusters: all eight are false positives (status-line values, spelled-out counts, a quoted gzkit phrase, heading text).
- Semicolons left (checker reports 0 because it skips bullets and blockquotes): in citations and reading lists (`Raji et al.; "Auditing Work"`, readings lines), inside the quoted covenant line in 3.3, in the "Course use" blockquotes, and in two bullets where the semicolon separates sub-lists whose items contain "and" (2.1 PEAS line, 2.3 the nine components). Converting the nine-component list to a numbered list would change structure.

## Left as is, deliberately
- "The course runs thirteen Thursdays, 4:00–6:30 p.m., one Evolution per week." The brief bans schedule and time details as asides; here the sentence is the subject of the section ("Using this book with CIDM 6333") and a fact, so it stays. Jeffry may want the clock time out of a textbook.
- Quoted gzkit and lecture lines: "You didn't lose control in one dramatic moment.", the covenant triplet in 3.3, "for maximizing Claudishness, only specification matters", "intent preservation across context boundaries", "the screen is a tool".
- The stage labels in 1.2 ("AI & ML: turn data into decisions. Deep learning: ... Agentic AI: automate entire processes.") read as the framework image's own labels and were not reworded.
- "with apology to test pilots" (dry parenthetical in the author's voice).
- Table cells in the "Why it is here" column are label fragments, which STE permits in tables.
