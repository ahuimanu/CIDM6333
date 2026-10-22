# Voice-pass review: e11-observability-red-team, e12-deployment, mini-attention-2017

Reviewer note on method. Many AFTER sentences contain details that are absent from the BEFORE speaker notes (GPT-5.4 Thinking 0.998, MIT licence, "hosted", mode 8, `gz obpi complete`, Appendix G, Gemini posting GEMINI_API_KEY, test point zero's receipt, "the Chase reads ... and nothing else", Table 3 row letters, "about 30 tokens", the dashed return arrow, "seven segments"). I checked each of these against the BEFORE slide HTML in `tools/review/voice-pass/docs-before/lectures/`. Every one appears on the slide itself, so none is reported as an invented fact. The findings below are the ones that survived that check.

Findings are listed most serious first.

---

## 1. e12, slide 5: "turn limit" misdescribes the code (category 1, CHANGED)
- BEFORE: "The limit comes from the environment."
- AFTER: "The turn limit comes from the environment."
- Problem: The code on the slide reads `TURN_TIMEOUT_S` (a per-turn timeout in seconds), so "turn limit" will be read as a cap on the number of turns, which slide 4 sets up as the job's budget and not the service's.
- Fix: Write "The per-turn timeout (TURN_TIMEOUT_S) comes from the environment."

## 2. mini, slide 10: pre-norm attributed to GPT-2 and universalized (category 1, ADDED and CHANGED scope; also category 2)
- BEFORE: "And most later models move the normalization step before each sub-layer, which trains more stably at depth." (The slide's own label also says "most later models normalize before each sub-layer.")
- AFTER: "GPT-2 (Radford et al., 2019) moved the normalization step to the input of each sub-layer, and the models that followed kept that placement because it trains more stably at depth."
- Problem: The revision adds an attribution and a citation that are not in the BEFORE notes or on the slide, and it turns "most" into "the models that followed", so the notes now disagree with the slide.
- Fix: Keep "most later models", and either drop the GPT-2 citation or verify it at page level before you keep it.

## 3. e12, slide 27: closing rule turned from necessary into sufficient (category 1, CHANGED)
- BEFORE: "You have not released it until you have rolled it back."
- AFTER: "You have proven a release when you have rolled it back once: ..."
- Problem: BEFORE makes rollback a precondition of a release. AFTER makes one rollback proof of the release, and that is a different and weaker claim (the hash, the canary, and the attestation also count).
- Fix: Restore the necessary-condition form: "A release is not finished until you have rolled it back once."

## 4. e12, slide 3: wrong reason attached to the attestation falsifier (category 1, ADDED causal)
- BEFORE: "The last falsifier is the Heavy lane's: a release with no attestation event is not a release."
- AFTER: "... a release with no attestation event fails the card, because nobody has attested that the release exists."
- Problem: On slide 10 the Gate 5 attestation is a person's verdict on the work (Completed, Completed — Partial, Dropped). It does not attest that the release exists, so the added reason is wrong.
- Fix: Write "because Gate 5 requires a person, not the agent, to attest the release."

## 5. e12, slide 12: added reason does not fit one of the two sections (category 1, ADDED causal)
- BEFORE: "The two that matter most: rollback, ... and known gaps ..."
- AFTER: "Two sections get the closest reading from the Chase, because each gives the Chase something to run and measure: rollback, ... and known gaps ..."
- Problem: The Chase can run and time a rollback, but cannot "run and measure" a known-gaps section, so the reason is false for half of the pair.
- Fix: Give a reason for each section: rollback is the one the Chase runs and times, and known gaps is the one that limits what the Chase may hold you to.

## 6. e11, slide 13: possibility turned into an asserted fact (category 1, CHANGED)
- BEFORE: "Verify the section numbers against the PDF before class; the card has a changelog and sections move."
- AFTER: "The card has a changelog, and sections have moved between revisions, so an attack card cites the section number from the revision it read."
- Problem: BEFORE warns that sections can move. AFTER asserts that they have moved, and no source is given for that.
- Fix: Write "and a revision can renumber sections, so an attack card cites the section number from the revision it read."

## 7. e11, slide 4: non sequitur in the receipt sentence (category 1, CHANGED causal)
- BEFORE: "it records the observed result of a command, the exit status, the duration, the git state, and the tail of stdout, and it validates against a schema."
- AFTER: "... and validates against a schema, so a receipt binds a result to a commit."
- Problem: Schema validation does not bind anything to a commit. The recorded git state does that, so the "so" assigns the wrong cause.
- Fix: Write "and validates against a schema. Because it records the git state, a receipt binds a result to a commit."

## 8. mini, slide 6: scope qualifier dropped (category 1, DROPPED)
- BEFORE: "Many newer models encode position differently, but the problem is the same one."
- AFTER: "Later models encode position by other methods (rotary embeddings, for example), ..."
- Problem: Without "many", the sentence says that all later models abandoned sinusoidal encoding.
- Fix: Restore "Many later models".

## 9. e12, slide 26 vs slide 24: final-deliverable deadline now disagrees (category 2, CHANGED)
- BEFORE (slide 26 cut): "... AI_LOG.md with final reflection are due Thu 11/26 11:59 p.m."
- AFTER (slide 26 cut): "... are due at closeout." Slide 24 lecture AFTER: "... are due on the date in the course calendar."
- Problem: "At closeout" reads as "at your ceremony appointment", which can be days before the real deadline (the last ceremony day). The two slides now give different deadlines.
- Fix: Use "due on the date in the course calendar" in both places.

## 10. e11, slide 6: lecture cites a strip that no longer says what the lecture says (category 2)
- AFTER lecture: "The trace store is part of the attack surface for the reason the strip states: an attacker who makes the agent print a secret has caused one leak, and a logger that writes that output to disk causes a second."
- AFTER strip: "If an attacker makes the agent print a secret and your logger then writes the output to disk, the secret persists in the trace." (BEFORE strip: "... wins twice if your logger then writes it to disk.")
- Problem: The revised strip lost the "twice" idea, so "the reason the strip states" points to a statement the strip no longer makes.
- Fix: Restore the strip's original wording, or cut "for the reason the strip states".

## 11. e11, slides 3 and 23: "the chapter's three" falsifiers listed two different ways (category 2)
- Slide 3 AFTER (and cut text): achieves objective; "not traceable in the black box"; a guardrail that passes only because the attack was never delivered.
- Slide 23 AFTER: "an attack that achieves its objective, an attack with no delivery span, and a guardrail credited when the attack never reached it or a pass obtained by disabling a check."
- Problem: The slide 23 version comes from the flight card. It adds "a pass obtained by disabling a check" and narrows "not traceable" to "no delivery span", and both slides call the result "the chapter's three". This difference existed on the slides already, but the revision now spells out both lists in the notes.
- Fix: Make one list authoritative. On slide 23, either say "the chapter's three, plus the flight card's disabled-check rule", or align the flight card with slide 3.

## 12. Systemic: "Cut from slide N (full wording)" blocks were reworded (category 4)
- Examples: e11 s6 strip ("wins twice" became "persists in the trace"). e12 s3 ("The release is a thing, not a moment." lost "not a moment"). mini s7 title ("Evidence 1: better translations at a fraction of the training cost" became "Evidence 1: translation quality and training cost"). e11 s14 strip ("a newer model is not a safer harness" became "a model upgrade does not by itself make the harness safer").
- Problem: If these blocks are the slides' verbatim text, the house rule ("text that quotes ... a slide ... is never edited") was broken. Some of the rewrites also removed the slide's finding (the mini s7 title no longer states a result).
- Fix: Confirm whether these blocks were in scope. If not, revert them to BEFORE. In any case, restore the mini s7 title.

## 13. e11, slide 3: tautology in place of the slide's claim (category 4)
- BEFORE: "The claim is the chapter's Sortie 11 claim, and the third falsifier is the one students miss ..."
- AFTER: "The design claim on the slide is the chapter's design claim for Sortie 11."
- Problem: The sentence says the claim is the claim and never states it. The reader gets no content.
- Fix: State it: "Sortie 11 tests the chapter's design claim: your system survives five pre-registered attacks without a write, a leak, or a false attestation."

## 14. e12, slide 3: a derivation that does not hold (category 4)
- AFTER: "Two rules follow from that definition. First, a release is an artifact ... Second, the process receives its secrets at run time ..."
- Problem: The secrets rule does not follow from the definition of "operated" (a second person can release, see the version, and roll back), so "follow from" asserts a deduction the text does not make.
- Fix: Write "The lecture adds two rules."

## 15. e12, slide 4: chapter made the actor that serves agents (category 4)
- AFTER: "Chapter twenty-one, section one, serves an agent either as a service or as a job, ..."
- Problem: The chapter does not serve anything, so the sentence gives the wrong actor. BEFORE's "An agent is served either as ..." was clearer.
- Fix: Write "Chapter twenty-one, section one, distinguishes two ways to serve an agent: as a service or as a job."

## 16. e12, slide 24: demonstration narrowed to opening a file (category 1, ADDED)
- BEFORE: "Anything you would say, you show instead."
- AFTER: "Anything you would say, you show instead, by opening the file."
- Problem: The ceremony includes a live demo and run commands, so "opening the file" narrows what "show" means.
- Fix: Delete "by opening the file", or write "by running the command or opening the file".

## 17. e12, slide 19 strip: new mechanism asserted (category 1, ADDED)
- BEFORE: "the record is written when the release happens, not later."
- AFTER: "the release command writes the record at the moment of release."
- Problem: The revision makes the release command the writer. The source (the topic guide via the speaker's own hedged paraphrase) does not establish that mechanism.
- Fix: Write "the record is written at the moment of release."

## 18. e11 s13, s14; e12 s14, s17, s19: instructor hedges dropped from prose (category 1, DROPPED qualifier)
- BEFORE examples: e12 s14 "Verify every cell before class; these pages change monthly." e12 s19 "Verify both against the repository before class and correct my paraphrase if it is wrong." e11 s14 "Verify the table numbers against the PDF before class."
- AFTER: The hedges are gone. The bracketed check lists survive only on some slides (none on e12 s14, and none on the e11 s13 and s14 notes).
- Problem: Removing these "[verify]" notes is a sanctioned change, but they sat in prose and carried scope information: the vendor pages are volatile, and the speaker's gloss of ADR-31 and #830 is a paraphrase. On e12 s14 and e11 s13/s14 nothing now tells a reader that the numbers come from changing documents.
- Fix: Add an "Instructor checks moved off the slide" line for e12 s14 and e11 s13/s14, as the other slides have.

## 19. e11, slide 19: correlation recast as cause (category 1, CHANGED causal)
- BEFORE: "nine layers were silently wrong and each fed the next, so the decisions at the top looked right. Nothing failed loudly, which is what makes trust-chain poisoning hard."
- AFTER: "... and the decisions at the top looked correct, because no single step failed loudly."
- Problem: BEFORE gives the chained errors as the cause of the correct-looking decisions. AFTER moves the cause to the absence of a loud failure.
- Fix: Write "each fed the next, so the decisions at the top looked correct. No single step failed loudly."

## 20. e11, slide 9: epigram added as the card's rationale (category 3, #36)
- AFTER: "... for the same reason a flight card is written before a sortie: a test written after the result is a description of the result."
- Problem: The line is a mirrored-pair aphorism that was not in BEFORE, and it does the work a plain reason should do.
- Fix: Write "because a test written after the run can be fitted to what the run did."

## 21. e11, slide 24: reveal frame and pseudo-cleft (category 3)
- AFTER: "The step the lab exists for is the check of the model's account against the export ..." and "The result of Run 1 is the lesson."
- Problem: The first is a pseudo-cleft and the second is a "the lesson is" reveal. Both are banned shapes.
- Fix: Write "The key step checks the model's account against the export ..." and delete "The result of Run 1 is the lesson."

## 22. e11, slide 7: reveal frame survives (category 3)
- AFTER: "The ratio of about two hundred to one is the chapter's point: ..."
- Problem: "X is the point" is a reveal frame (BEFORE had the same shape, and the pass did not remove it).
- Fix: Write "The chapter draws one conclusion from the ratio of about two hundred to one: ..."

## 23. e11, slide 19: pseudo-cleft (category 3)
- AFTER: "That silence is what makes trust-chain poisoning hard to catch."
- Fix: Write "Because no step failed loudly, nothing flagged the poisoned chain."

## 24. e11, slides 11, 15, 21: moral and antithesis landings (category 3, #36)
- s11: "The guardrail is what stands when the model does not refuse." (an epigram and a pseudo-cleft)
- s15 closer: "... so the system card had stated the threat model and the integrators had not read it." (a moral landing)
- s21: "a red team that starts from the lab's failure reports tests what is known to fail, and a red team that starts from imagination can test only what its author already expected." (mirrored antithesis)
- Fix: s11, write "Only the guardrail stops an attack the model does not refuse." s15, end on the documented fact (the Opus 4.7 card said the action was not hardened). s21, keep only the reason: "the labs' reports list failures already observed in the model."

## 25. e12, slides 13 and 18: epigram closers (category 3, #36)
- s13: "... because the absence of a record is the finding."
- s18: "... and that is a design choice with a cost of its own."
- Fix: s13, write "write that answer down as a finding: no record exists." s18, state the cost: "so a new session cannot see what an earlier session learned."

## 26. mini, slides 7, 12, 2: reveal frames and pseudo-cleft (category 3)
- s7: "The French result gives a second lesson in reading tables."
- s12: "This lecture applied one test to the paper, and the test transfers: ..."
- s2: "... because the paper's tables, rather than its diagram, are what this course reuses."
- Fix: s7, write "The French result shows a table-text mismatch." s12, start "A design document states its constraint, its trade, and its evidence ..." s2, write "because this course reuses the paper's tables more than its diagram."

## 27. All three decks: templated slide ledes (category 3, #38)
- The AFTER notes repeat the same opening: "The slide sorts ..." (e11 s6), "The slide compares ..." (e11 s16), "The slide shows ..." (e12 s7, mini s10), "The slide takes ..." (e12 s20), "The slide redraws ..." (mini s4), "The table lists ..." (e12 s6, s14), "The table turns ..." (e11 s8).
- The AFTER notes repeat other openings too: "The evaluation lens has three columns" opens both e11 s22 and e12 s22. "As used in this lecture/course, X means ..." opens e12 s1 and s3 back to back.
- Fix: Open each note with its subject, as BEFORE often did ("Five concerns, each with ...", "Copilot's agent, read for ..."), and keep the "The slide ..." frame only where the note points at a visual.

## 28. e11, slide 3: rule statements as definition-colon ledes (category 3, #35, minor)
- AFTER: "Rule one: the black box outranks the narrative." "Rule two: a guardrail is a mechanism at an enforcement locus, in other words ..."
- Problem: This is acceptable for numbered rules, but it repeats the colon-definition shape that also opens s4, s10, and s13 ("A system card is the lab's evaluation report on the model: ...", "Section 5 covers agentic safety: ...").
- Fix: Leave the rules as they are, and give s13 a verb-led opening ("Section 5 reports agentic safety results for malicious use and ...").

---

No further findings beyond these 28.

---

## Repair log

1. FIXED. e12 s5: "The per-turn timeout (TURN_TIMEOUT_S) comes from the environment." (the name is on the slide's code).
2. FIXED. mini s10 notes: "Most later models move the normalization step to the input of each sub-layer, a placement that trains more stably at depth." GPT-2 citation dropped. The slide label in sitekit/voice/mini-attention-2017.json had the same change ("GPT-2 (2019) and its descendants"); restored to "Post-norm: most later models normalize before each sub-layer".
3. FIXED. e12 s27: "A release is not complete until you have rolled it back."
4. FIXED. e12 s3: restored BEFORE, "a release with no attestation event does not count as a release." The reviewer's Gate 5 reason was not used, because it would add a claim.
5. FIXED. e12 s12: restored BEFORE, "The two sections that matter most are rollback, ... and known gaps, ...". No reason added for either section.
6. FIXED. e11 s13: "a revision can renumber sections".
7. FIXED. e11 s4: "and validates against a schema. Because it records the git state, a receipt binds a result to a commit."
8. FIXED. mini s6: "Many later models".
9. FIXED. e12 s26 cut block now reads "due on the date in the course calendar", matching the live slide and s24.
10. FIXED. The live slide strip (voice JSON) says "A leaked secret that your logger writes to disk is a second leak", so the lecture was right. The s6 cut block now ends "the logger has caused a second leak."
11. FIXED in notes (s23 now gives the chapter's three and says the flight card extends the third to a pass obtained by disabling a check). The slide-level difference is pre-existing: FOR JEFFRY.
12. LEFT, per instruction: the cut blocks are co-written. Repaired only mini s7 (cut block now gives the live slide title "Evidence 1: better translations at lower training cost") and e11 s6 (see 10). e12 s3 "not a moment" and e11 s14 strip are left because their meaning is intact.
13. FIXED. e11 s3 states the claim from the slide.
14. FIXED. e12 s3: "The lecture adds two rules."
15. FIXED. e12 s4: "distinguishes two ways to serve an agent: as a service or as a job."
16. FIXED. e12 s24: "by opening the file" deleted.
17. FIXED. e12 s19 cut block: "the record is written at the moment of release" (matches the live slide).
18. FIXED. Bracketed checks added: e12 s14 "[Verify every cell before class; these pages change monthly.]"; e12 s19 "[Verify both against the repository before class and correct this paraphrase if it is wrong.]"; e11 s13 and s14 "Instructor checks moved off the slide" lines restored from BEFORE.
19. FIXED. e11 s19: "each fed the next, so the decisions at the top looked correct."
20. FIXED by cutting: e11 s9 "you write it before you fly, as a flight card is written before a sortie." No reason substituted.
21. FIXED. e11 s24: "The key step checks ..."; "The result of Run 1 is the lesson." deleted.
22. FIXED. e11 s7: "The chapter draws one conclusion from the ratio ..."
23. FIXED. e11 s19: "No single step failed loudly, and for that reason trust-chain poisoning is hard to catch." (BEFORE's meaning, no pseudo-cleft.)
24. FIXED. s11 as suggested; s15 ends on the Opus 4.7 card fact; s21 keeps only "the labs' reports list failures already observed in the model" (the slide strip's content).
25. FIXED. e12 s13 as suggested. e12 s18: closer cut ("because nothing persists except the branch."); the reviewer's replacement was not used because it adds a claim.
26. FIXED. mini s7, s12, s2 as suggested.
27. FIXED for e12 s3, s6, s7, s14, s20, s22; e11 s6, s8, s16; mini s4. LEFT: e11 s22 (keeps the lens lede now that e12 s22 does not), e12 s1, mini s10 (points at the visual).
28. FIXED. e11 s13 opens "Section 5 reports agentic safety results for ...". Rules left as they are.

FOR JEFFRY
- e11 s3 vs s23 flight card (pre-existing on the slides): slide 3 lists "any guardrail that passes only because the attack was never delivered"; the flight card's third falsifier reads "a guardrail credited when the attack never reached it, or a pass obtained by disabling a check". Which list is authoritative?
- e12 s24 and s26 notes still say "by appointment on Calendly" and "Book your ceremony slot on Calendly", against the Calendly-removal ruling. Remove, and if so, where do students book?
- e12 s27 notes still say "Sources checked 09/24/2026", not "Retrieved September 24, 2026".
- mini s7: BEFORE cut block said "at a fraction of the training cost"; the live slide says "at lower training cost". The cut block now follows the slide.
