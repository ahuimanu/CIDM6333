# Pass log: topic-guide-3 (Oct 22, 2026)

File: `/home/claude/site/tools/review/voice-pass/tg/chunk3.md` (Course Topic Guide chapters 18 to 26, Appendices A to E). Chain: humaniser, ste-voice, scholarly-voice, humaniser battery (check only). 59 lines changed; roughly 60 edits.

Invariants verified after the final pass: every heading line (all levels) byte-identical to the original; both code fences byte-identical; the set of backtick spans identical; table row count 42 before and after; line count unchanged; every citation, title, author, year, URL, and command untouched.

Most of this chunk is outline matter (status "outline" on every chapter): bulleted topic lists, step-free exercise items, three templates, two tables, a glossary, and a reading list. There are few explanatory paragraphs, so the chain had less to redraft than in the prose chunks. Topic bullets were left as topic bullets; converting them to full prose would have added content.

## Changes by pattern

### Em dashes (house ban)

Removed from every line outside `# ` headings and code fences: the four "Flight card supported" leads ("Sortie 9 (corner) — DESIGN CLAIM:" became "Sortie 9 (corner). DESIGN CLAIM:"), the chapter 23 reference-design line, all 27 glossary separators (" — " became ": "), and the reading-list line ("Turn and Face the Change — and the archive" became "..., and the archive").

Left in place: the em dashes inside the Appendix A and Appendix B code fences (the brief says code fences stay exactly as they are; the fence in Appendix B also contains the line `# Design Analysis — <System> (<year>)`, which the page generator would otherwise read as a heading), and "Completed — Partial" in the Attestation entry, which is gzkit's attestation vocabulary and appears in that form across the site (`tools/sitekit/glossary_data.py`, the figures, the lectures). Proper vocabulary is never edited.

### "names" as a verb (house ban)

- "Name the multi-agent failure taxonomy" → "State the multi-agent failure taxonomy"
- "the "why" paragraph that names cost and failure mode" → "that states the cost and the failure mode"
- "the named failure class" → "gzkit's label for the failure class"

`receipts : <names>` in the Appendix A fence is the noun and sits in a code fence.

### Antithesis and mirrored-pair closers (#36; house cadence ban)

- "A subagent's claim is not evidence; receipts are." → "A subagent's claim becomes evidence only when a receipt backs it." (The gzkit maxim "A claim without a receipt is not evidence" does not appear in this chunk verbatim, so nothing of Jeffry's was touched.)
- "Discussed, not filed." (AI log) → "The log is discussed in the Drift consultation rather than filed." Fact kept; cadence removed.
- "If it still passes, you have found your first hollow test." → "If the test still passes, the test is hollow." ("your first" was flourish.)
- Table cell "Operations arrive" → "Operational problems".

Kept: "Naval origin; you cannot move and listen at once" (Jeffry's own explanation of the Sprint and Drift name; chapter 22 quotes his method) and "Evaluation as falsification rather than confirmation" (a topic label stating the subsection's thesis flat, not a closer).

### Actor removal and gerund subjects (STE rules 2 and 3; humaniser #3)

- "removing the feature, or planting a wrong answer, turns the gate red" → "if the tester removes the feature or plants a wrong answer, the gate turns red"
- "a release can be rolled back in one governed command" → "one governed command rolls a release back"
- "Correctness is no longer evidence of understanding; banning AI fails three ways" → "A correct artifact is no longer evidence of understanding; a ban on AI fails three ways"
- "Filling in expected observables after flying is a doctrine violation" → "Do not fill in the expected observables after the flight. Doctrine counts that as a violation."
- "the adversary agreeing with a planted falsehood" → "an adversary that agrees with a planted falsehood"; "any attack achieving its objective; any attack not traceable in the black box; a guardrail passing only because..." → relative clauses with the attack, the black box, and the guardrail as subjects
- "translating a card's findings into your guardrails" → "how to translate..."; "reading a system from the inside vs. the outside" → "how to read a system from the inside and from the outside"
- Glossary: "treating the model's window as..." → "the practice of treating the model's context window as..."; "the verification phase: defend the work without AI" → "the verification phase, in which the student defends the work without AI"; "the production phase: build with AI, log it" → "the production phase, in which the student builds with AI and logs the use"
- Appendix C: "Hard-to-reverse action without confirming authorization" → "Takes a hard-to-reverse action without confirming authorization" (parallel with the other eight rows, which all open with a verb); "without surfacing the trade" → "without stating the trade"

### Parts lists turned into sentences (scholarly-voice: full sentences, not a parts list)

The six "Reference design: gzkit" sections were semicolon-joined fragments. Each is now one or two sentences carrying the same pointers, with no pointer added or dropped. The chapter 23 line also gained its reason: "Zero sorties had been flown as of 2026-08-17, so the course flies the first." Ledes vary by content ("This chapter reads...", "The gzkit evidence for this chapter is...", "The gzkit commands and records for this chapter are...", "The gzkit documents for this chapter are...", "This chapter uses the reference design as a tool...", "The gzkit material for this chapter is...") so that the six do not share one opening (#38).

Appendix C intro: "From gzkit ... (sourced to frontier system cards), with the human-side patterns the course adds." → two sentences stating where the nine modes come from and that the human-side patterns after the table are the course's additions.

Glossary entries with stacked colons ("ADR — Architecture Decision Record: intent, ...") were folded into one declarative each; MCP now reads "whose participants are hosts, clients, and servers and whose primitives are tools, resources, and prompts" (MCP's own terms for the two groups).

### Noun clusters (STE rule 4)

- "long-running and background agents' operational problems" → "the operational problems of long-running and background agents"
- "ten-deep summary-laundering chain" → "the summary-laundering chain ... (ten levels deep)"
- "nine trust-chain-poisoning instances" → "nine instances of trust-chain poisoning"
- "the GHI #830 backfilled releases" → "the backfilled releases of GHI #830"

### Procedures (STE: imperative, one instruction per sentence)

- Ch. 18 exercise: "Show the pipeline catching it, then show the version that would not." → "Show the pipeline that catches it. Then show the version that would not."
- Ch. 25 exercise: "Complete ... end to end and paste your ledger." → two sentences.
- Ch. 26 exercise: "Compare." → "Compare the two."
- Ch. 23 exercise: "Notice how much..." → "Note how much..." (an instruction, not a staged realization).
- Appendix A intro: three imperatives and the reason, no gerund subject.
- Appendix B intro: "One per week, ~150 words, committed to ... and appended as a row to ..." → "Write one Design Analysis per week, ~150 words. Commit it to .... Append one row to ...."

### One ambiguity removed (STE rule 1)

"Image, config, secret injection, rate limits, budgets; never in the repo." → "...; secrets never in the repo." The bare "never in the repo" could attach to the whole list.

## ste_check lines declined

Run on plain text extracted from the file (fences, tables, headings, and the course-use line removed).

- Sentences over 25 words (7): the two "This chapter reads..." pointer lists (ch. 18 and 19), three FALSIFIERS/DESIGN CLAIM lines (each a list of three pre-registered conditions; splitting would separate the conditions from their label), and the two reading-list lines in Appendix E (never edited). Kept as justified lists.
- Passives with no actor (3): fixed (see above); the rerun would report none.
- Noun clusters of 4+ (12): all false positives on code paths, command names, file names, and the Appendix C human-side pattern list ("governance theater cognitive surrender" is two items in a semicolon list).
- Semicolons (16): all sit in outline topic bullets or in the FALSIFIERS lists, where they separate list items; none sits in a numbered exercise step. The brief's no-semicolon rule covers procedures, steps, step tables, and file lists, not topic outlines.

## Humaniser battery, check-only rerun

Greps (intensifiers, AI vocabulary, closer shapes, hedge stacks, "names", not-but cadence, "the move", "tonight"/"this week"/"we"): no hits outside the Appendix A code fence (`<names>`, a noun).

### Closer list (last sentence of every paragraph, item, and glossary entry)

Full list generated mechanically and read out of context. Lines reviewed for #36:

- "A subagent's claim becomes evidence only when a receipt backs it." (states the condition; passes)
- "Naval origin; you cannot move and listen at once." (Jeffry's explanation of the method's name; kept)
- "Evaluation as falsification rather than confirmation." (topic label; passes)
- "If the test still passes, the test is hollow." (consequence stated flat; passes)
- "Zero sorties had been flown as of 2026-08-17, so the course flies the first." (reason attached; passes)
- "Doctrine counts that as a violation." (reason for the preceding instruction; passes)
- "The log is discussed in the Drift consultation rather than filed." (fact; passes)
- All other closers are outline items, readings, commands, or glossary definitions.

### Lede list (first sentence after every heading)

Every chapter opens with the same skeleton (Course use; After this chapter you can:; Outline; Systems analyzed; Reference design; Readings; Flight card supported; Exercises). This is the textbook's chapter template, the kind of shared structure the #38 rule allows where the reader needs to find the same thing in the same place; it was not changed. The six reference-design ledes, the only ledes I wrote, differ from one another (listed above). No lede has the "X is Y: a, b, and c" shape (#35).

### Claim list (frequency and consensus claims)

Grep for most/every/usually/often/always/never/typically/commonly returned only: design-claim conditions ("never becomes evidence without a receipt", "secrets never appear in image, log, or repo"), a gzkit rule with its source cited in the line ("Gate-4 evidence, never Gate-5 (GZK-GOV-007)"), the ch. 20 outline item "what never to log", and instructions ("every week", "every field", "every event"). No unsourced "most students"/"every term" claim exists in the chunk.

## Sentences left long, with reason

- Ch. 18 and 19 reference-design sentences (35 and 28 words): each is a single list of the gzkit artifacts the chapter reads; the list is the content.
- The FALSIFIERS lines in chapters 18, 20, and 21 (26 to 27 words): three pre-registered conditions under one label.

## Unsure

- "Completed — Partial" (glossary, Attestation): kept with its em dash as gzkit vocabulary. If the house ban is meant to override vocabulary, the site-wide form would need to change in one place (`glossary_data.py`) and be propagated.
- Em dashes inside the two template code fences were left per the "code fences exactly" constraint.
