# Voice-pass review: orientation, E0 (index zero), E1 (agent loop)

Scope: `pairs/orientation.md`, `pairs/e0-index-zero.md`, `pairs/e1-agent-loop.md`. Each entry gives the location, the category (1 facts, 2 contradictions, 3 surviving AI shapes, 4 meaning damage), BEFORE and AFTER text, the problem, and a fix. Entries run from most to least serious.

Counts (by primary category): category 1: 23; category 2: 5; category 3: 6; category 4: 6 (40 total; several category 1 entries also involve a contradiction).

---

### 1. E0 slide 19: invented citation (cat 1, ADDED)
- BEFORE: "The practitioner literature on auditing names an accountability gap: audits without access, attestations nobody observed."
- AFTER: "The practitioner literature on auditing (Raji and colleagues, 'Auditing Work') describes an accountability gap..."
- Problem: The reviser added a citation that BEFORE did not have, and the attribution is wrong. "Auditing Work: Exploring the New York City algorithmic bias audit regime" (FAccT 2024, arXiv 2402.08101) is by Groves, Metcalf, Kennedy, Vecchione, and Strait. Raji is not an author.
- Fix: Remove the parenthetical, or replace it with a source that has been checked at page level for the "audits without access" wording.

### 2. Orientation slide 32 against slide 12 and its own cut section: make-up policy (cat 2 and cat 1, CHANGED and DROPPED)
- BEFORE notes: "Consultations are not made up late." BEFORE cut: "Miss a Thursday → Calendly slot before the week ends, or the Evolution is capped."
- AFTER notes: "Missed consultations are not made up." AFTER cut: "Consultations are not made up late. If you miss a class, book a make-up consultation, or the Evolution is capped." Slide 12 cut: "A missed class: book a make-up consultation, or the Evolution is capped."
- Problem: The notes now say a missed consultation is never made up, while the cut text and slide 12 say to book a make-up. The pass also dropped the time window ("before the week ends") and the booking channel (Calendly). That window is what made "not made up late" consistent with "book a make-up".
- Fix: Put "before the week ends" back in all three places, and change the slide 32 notes back to "Consultations are not made up late."

### 3. Orientation slide 12: class-size condition dropped (cat 1, DROPPED)
- BEFORE: "With fewer than ten of us this works. ... Three deep slots a week over twelve weeks means everyone gets four deep Drifts"
- AFTER: "The small class size makes this schedule possible. ... Three deep slots per session over twelve Evolutions give each student four deep Drifts"
- Problem: The arithmetic (36 slots ÷ 4) holds only with nine or fewer students. The AFTER notes state the four-Drift guarantee with no condition.
- Fix: Restore the number: "With nine or fewer students, three deep slots per session over twelve Evolutions give each student four deep Drifts."

### 4. E1 slide 10 cut: new architecture claim that contradicts orientation slide 18 (cat 1 and cat 2, ADDED)
- BEFORE cut: "Governance arrived as the missing component, not as a wrapper."
- AFTER cut: "gzkit treats governance as one of the agent's components (the one ReAct and AutoGPT lacked), so the ledger and the gates sit inside the loop."
- Problem: "the ledger and the gates sit inside the loop" is a new architecture claim. Orientation slide 18 says gzkit "sits one tier above the vendor harnesses and wraps them ... It does not run agents."
- Fix: Delete the "so the ledger and the gates sit inside the loop" clause, or restate the BEFORE sentence.

### 5. Orientation slides 1, 20, 21, 33 and E0 slide 21: WTClass removed (cat 1, DROPPED)
- BEFORE: "In WTClass you submit the repository URL and a PDF of the flight log"; "entered in WTClass as score × 5"; "in evolution-00/ and in WTClass"; "the mechanics are in the orientation deck and WTClass"
- AFTER: "You submit the repository URL and a PDF..."; "entered in the gradebook"; "Submit in evolution-00/."; "The submission mechanics are in the orientation deck."
- Problem: WTClass is a proper name, and it tells students where to submit. With it gone, no deck says where the PDF goes, and the slide 33 cut now names only the repository folder as the place to submit.
- Fix: Restore "WTClass" in each place. It is a location, not a date or a time.

### 6. Orientation slide 21: provisional status of the rubric dropped (cat 1, DROPPED)
- BEFORE: "The rubric will be posted before the first Evolution is due; this is its intended shape so you know what I am looking for from day one."
- AFTER: "The rubric has five dimensions, each scored from zero to four."
- Problem: The notes now present the rubric as final. The AFTER cut text still says "The posted rubric governs. This slide states the rubric's intent."
- Fix: Open with "The posted rubric governs; this slide shows its intended shape."

### 7. Orientation slide 11: the sonar explanation disagrees with its cut section, and the causal claim was softened (cat 2 and cat 1, CHANGED)
- BEFORE notes: "The naval metaphor is exact. Moving makes noise that masks signals; listening requires stillness. Production and verification cannot happen at the same moment"
- AFTER notes: "The term comes from submarine practice: a boat moving at speed makes noise that masks other signals, so it drifts to listen. Building and verifying likewise compete for the same attention"
- AFTER cut: "The terms come from anti-submarine warfare ... A ship cannot move and listen at the same time, because its own engine noise masks the sonar."
- Problem: The notes say "submarine practice / a boat", and the cut says "anti-submarine warfare / a ship". "Cannot happen at the same moment" has also become "compete for the same attention", which is a weaker claim and removes the reason the week is split.
- Fix: Use "anti-submarine warfare" and "ship" in both places, and restore "cannot happen at the same moment".

### 8. Orientation slide 30 cut: "only folder I write to" contradicts the same list (cat 2, CHANGED)
- BEFORE: "feedback/ what I write into your repo after review — nothing else comes from me"
- AFTER: "feedback/ what I write into your repo after review (the only folder I write to)"
- Problem: The same list gives "final/ brief.md (mine)", so the instructor also writes in final/.
- Fix: "feedback/: my review notes; apart from brief.md in final/, nothing else in the repo comes from me."

### 9. Orientation slide 5: new names and a new frequency claim about 2023 (cat 1, ADDED and CHANGED)
- BEFORE notes: "Most of what went wrong in 2023 was the halt condition." BEFORE cut: "The halt condition is the part 2023 forgot."
- AFTER notes: "The autonomous agents of 2023 (AutoGPT among them) failed mostly at the halt condition, and spiraled." AFTER cut: "The 2023 autonomous agents (AutoGPT, BabyAGI) ran this loop without a halt condition."
- Problem: The pass added system names, a "mostly" frequency claim about the agents, and the "spiraled" outcome. In the cut, it turned a summary judgment into a flat technical statement (no halt condition at all) that the BEFORE did not make.
- Fix: Keep BEFORE's scope ("The halt condition is what the 2023 loops left out"), or move the claim to E1 slide 8, where AutoGPT is taken apart with evidence.

### 10. E0 slide 9: dated frequency claim replaced by an overgeneralized causal claim (cat 1, CHANGED)
- BEFORE: "because since 2024 most of what fills a context window is tool results"
- AFTER: "The context window of an agent harness fills with tool results, so context management is a problem you meet only after tool calling exists"
- Problem: "only after tool calling exists" is new and false (long documents and long conversations need context management without tools). The pass also dropped the "since 2024" qualifier.
- Fix: "In an agent harness, tool results fill most of the context window, so this course teaches tools before context management."

### 11. E0 slide 5 cut: "foundation" redefined (cat 1 and cat 2, ADDED)
- BEFORE: "The foundation is where the bill is delivered."
- AFTER: "The deferred cost comes due in the foundation: the data, weights, and infrastructure the system stands on."
- Problem: Slides 4 and 5 define the data foundation as ownership, definitions, quality, and lineage. "Weights and infrastructure" is a new definition that contradicts them.
- Fix: "...comes due in the data foundation: ownership, definitions, quality, lineage."

### 12. E0 slide 14: evaluation row rewritten into a muddle (cat 1 and cat 4, CHANGED)
- BEFORE: "Evaluation: in both, mostly the human."
- AFTER: "Evaluation: in the chat assistant the human reads the answer, and in the harness the tests it runs and the human, with nothing built in."
- Problem: The new claim that the harness runs tests sits next to "nothing built in", so the row contradicts itself. It is also harder to read than BEFORE.
- Fix: "Evaluation: in both, the human does most of it; the harness can run tests the human asks for, but it has no built-in evaluator."

### 13. E0 slide 22: a necessary condition became a sufficient one (cat 1, CHANGED)
- BEFORE: "most of the design choices only make sense once you ask who was answering and for what."
- AFTER: "a design choice makes sense once you ask who was answering and for what."
- Problem: "Only make sense once" means the question is required. "Makes sense once" means the question is enough. The claim's scope also widened from most choices to any choice.
- Fix: "many design choices make sense only after you ask who was answering for them, and for what."

### 14. Orientation slide 17: "Everything" became "Most", and the notes now disagree with the cut (cat 1 and cat 3, CHANGED)
- BEFORE: "Everything since is those ideas with a language model in the reasoner slot"
- AFTER: "Most later designs put a language model in the reasoner slot of one of these ideas, and part of the survey is to recognize which one." AFTER cut: "Later systems reuse these ideas..."
- Problem: This introduces an unsourced "Most" (#37). It also adds the premise that each design maps to exactly one prior idea, and it no longer matches the cut text.
- Fix: "Later designs reuse these ideas with a language model in the reasoner slot, and part of the survey is to trace which ideas each one reuses."

### 15. E1 slide 9 cut: ReAct claim changed (cat 1, CHANGED)
- BEFORE: "it optimized for a benchmark and left everything else out."
- AFTER: "ReAct's authors ... evaluated it against benchmarks and nothing else."
- Problem: The new sentence makes a different, checkable claim about the paper's evaluation method. The AFTER notes still say "optimized for a benchmark".
- Fix: Restore "optimized for a benchmark and left everything else out".

### 16. E1 slide 14: E3 pointer removed (cat 1, DROPPED)
- BEFORE: "that becomes the injection test point in week three."
- AFTER: "that rule becomes the injection test point in a later Evolution."
- Problem: "Week three" maps to E3, which is an Evolution number and not a calendar date. The orientation deck's E3 card (test point 4) confirms it.
- Fix: "...becomes the injection test point in E3."

### 17. Orientation slide 25: causal link dropped (cat 1, DROPPED)
- BEFORE: "Claude Code has the richest hook system, which is why gzkit renders seventeen hooks into it."
- AFTER: "Claude Code has the most extensive hook system, and gzkit renders seventeen hooks into it."
- Problem: The reason, which is the Design Analysis point of the slide, became a bare conjunction.
- Fix: "...and for that reason gzkit renders seventeen hooks into it."

### 18. Orientation slide 34 cut: slide wording replaced with new content (cat 1, ADDED and DROPPED)
- BEFORE cut: "The systems you will study were designed by people who had to answer for them. Build one you can answer for."
- AFTER cut: "...had to answer for them. You answer for your Final System at the closeout ceremony, where I observe the demonstration and attest."
- Problem: The "full wording" section no longer matches the slide. It drops "Build one you can answer for" and adds an attestation sentence.
- Fix: Restore the cut section to the slide's text.

### 19. E0 slide 15: Anthropic attribution added (cat 1, ADDED)
- BEFORE: "Most production agents are workflows and should be."
- AFTER: "Anthropic recommends the workflow wherever the path is known in advance, and the open loop only where it is not"
- Problem: The pass replaced an unsourced claim with an attribution. That direction is right, but the paraphrase is close to the source without matching it ("workflows offer predictability ... for well-defined tasks, whereas agents are the better option when flexibility ... is needed"), and nobody has checked it.
- Fix: Check the wording against "Building Effective Agents", or soften it to "Anthropic's guide favors workflows for well-defined tasks".

### 20. E0 slide 5: "done" claim rewritten with a new reason (cat 1, CHANGED)
- BEFORE: "'done' is the most dangerous word in the course."
- AFTER: "'done' is the term to define first, because the agent's halt and your attestation both depend on it."
- Problem: The pass replaced Jeffry's line with a different claim and a reason he did not give.
- Fix: Ask Jeffry. Otherwise keep the BEFORE wording and attach the reason after it.

### 21. E1 slide 8: actor added, and the notes disagree with the cut (cat 1 and cat 2, CHANGED)
- BEFORE cut: "It also produced the field's first shared failure record"
- AFTER cut: "Its users also published a shared record of failures". AFTER notes: "it gave the field its first shared record of failure."
- Problem: The cut adds "users published" and drops "first", while the notes keep "first". The two now differ on who produced the record and whether it was the first.
- Fix: Use one formulation in both places. Keep "first" only if a source supports it.

### 22. E1 slide 10: the loop now lacks two different things (cat 2, ADDED)
- BEFORE: "The reference design's origin is the loop plus the thing the loop lacked."
- AFTER: "...the loop plus the thing the loop lacked, a record of intent that survives the session. ... Governance arrived as the missing component."
- Problem: The added appositive names "a record of intent" as the missing thing. The same paragraph then names governance, and slide 9 names "a budget, an evaluator, and a record".
- Fix: Drop the appositive. Let "Governance arrived as the missing component" carry the point.

### 23. E0 slides 3 and 16: speaker cues to ask the room are gone (cat 4)
- BEFORE: "Ask them: who answered for the last piece of generated code you shipped? Sit in the silence for a moment." / "Ask the room: where on this curve were you last week?"
- AFTER: "Consider who answered for the last piece of generated code you shipped." / "Ask yourself where on this curve you sat during your last project."
- Problem: These are speaker notes. The instructor's cue to put the question to the class is gone, and "last week" became "last project".
- Fix: "Ask the class who answered for ..., and wait for answers." Restore "last week" as well.

### 24. E0 slide 9: "differ from the catalog order" does not fit the second item (cat 4)
- BEFORE: "Two things to notice. First, the middle is inverted from the catalog ... Second, the two starred weeks run on a local open-weight model"
- AFTER: "Two things differ from the catalog order. ... Second, the two starred Evolutions run on a local open-weight model"
- Problem: The local-model requirement is not about order, so the new lede is wrong for half of what follows.
- Fix: "Two features of the table need attention."

### 25. E0 slide 18: the Docs gate sentence is garbled (cat 4)
- BEFORE: "Docs: what is written matches what runs."
- AFTER: "Docs match what is written to what runs."
- Problem: The sentence now says the docs perform the matching, which reads as ungrammatical.
- Fix: "The Docs gate checks that what is written matches what runs."

### 26. E0 slide 19: direction of answerability reversed (cat 4)
- BEFORE: "It makes one build answerable."
- AFTER: "Its scope is one build, and it makes that build answerable to the engineer who signed."
- Problem: The course's sense is that the engineer answers for the build. "Answerable to the engineer" says the reverse.
- Fix: "Its scope is one build, and it makes the engineer who signed answerable for that build."

### 27. Orientation slide 10 against slides 8 and 11: deadline wording (cat 2)
- AFTER slide 10: "You fly the rest of the sortie on your own before the next session." AFTER slides 8 and 11: "due the evening before the consultation" / "due the evening before the next session".
- Problem: "Before the next session" and "the evening before" give two different deadlines.
- Fix: Slide 10: "...on your own; it is due the evening before the next session."

### 28. Orientation slide 6: "observed", and the narrowed "without both" (cat 1, ADDED and CHANGED)
- BEFORE: "The degradation pattern: ..." / cut "Without both, governance is theater."
- AFTER: "The course structure follows from one observed pattern, the Degradation Pattern." / cut "If humans do not engage, the gates alone produce governance theater."
- Problem: "Observed" adds an empirical claim that has no source. The cut now covers only one of the two failure cases.
- Fix: Drop "observed". In the cut, keep "Without both sides, governance is theater."

### 29. Orientation slide 7: class-size number dropped (cat 1, DROPPED)
- BEFORE: "with under ten of us the class together covers the whole corpus"
- AFTER: "because the class is small, the class together covers the whole corpus"
- Problem: The pooling claim depends on the number, and the number is gone. The same loss happens on slide 12.
- Fix: "because the class has fewer than ten students, ..."

### 30. Orientation slides 16 and 17: small additions that are accurate but should be noted (cat 1, ADDED)
- Slide 16: "The vendor's harness" became "Anthropic's harness". "It is short on purpose" became "its length is fixed at about a hundred and fifty words so that it forces a choice of what to say."
- Slide 17: "in November, MCP" became "Anthropic released MCP in November".
- Problem: These are facts and a rationale that BEFORE did not state. Both attributions are correct (MCP was announced in November 2024). "Fixed at about" contradicts itself, and the rationale is new.
- Fix: Keep the attributions. Change "its length is fixed at about" to "it is about a hundred and fifty words on purpose".

### 31. Orientation slide 18 and E0 slide 20: epigram landings (cat 3, #36)
- Orientation slide 18 AFTER: "A system read from the inside, with its incident history, teaches what a README omits."
- E0 slide 20 AFTER: "That last question contains the course's whole concern, because an intent nobody preserved is an intent nobody can answer for."
- Problem: Both are caption lines that turn a phrase. The E0 line is a mirrored chiasmus.
- Fix: Delete the orientation line. In E0, end at "...after the person who decided has left the session."

### 32. Orientation slides 9 and 22, plus the slide 2 cut: antithesis and moral closers (cat 3)
- Slide 9: "The final system is this stack, closed out under the Heavy lane, and not a new project." Slide 22: "...closed out under the Heavy lane and released, and not a new project."
- Slide 2 cut: "The course trains you to be the person who answers for the system."
- Slide 15: "I grade this record, and a statement that the system worked is not part of it."
- Problem: Each sentence lands on an antithesis or a moral. The slide 9 and slide 22 closers are also near-identical.
- Fix: Slides 9 and 22: "The final system is this stack, closed out under the Heavy lane." In the slide 2 cut, restore the BEFORE line, or delete the closer.

### 33. Orientation slide 13 and slide 34 notes: decorative and invented-authority closers (cat 3, #36 and #37)
- Slide 13: "the last one matters most" became "the fifth carries the rest".
- Slide 34: "the designs that lasted had answerability built in from the start."
- Problem: "Carries the rest" is a metaphor that claims the other four rules depend on the fifth. Slide 34 makes a sourceless generalization about which designs lasted, and "from the start" is new.
- Fix: Slide 13: "the fifth matters most:". Slide 34: cut the clause after "had to answer for them".

### 34. Orientation slides 6, 17, 18, 25, 29: "we" remains (cat 3, house rule)
- AFTER: "we discuss your AI log in consultation"; "because we have its full record"; "because we have its whole record"; "the systems we take apart"; "which we discuss in the consultation hour".
- Problem: The house rules ban "we". The pass removed it in some sentences and left it in these.
- Fix: Use "the course" or "you and I" (for example, "you and I discuss your AI log in consultation").

### 35. Orientation slide 19: templated sibling sentences (cat 3, #34 and #38)
- AFTER: "The ADR gate requires ... The TDD gate requires ... The Docs gate requires ... The BDD gate requires ... The Human gate requires ..."
- Problem: Five sentences with the same frame make a uniform rhythm. E0 slide 18 covers the same gates with varied verbs.
- Fix: Merge them into one sentence ("gzkit has five gates: ADR (intent before implementation), TDD (...), ...").

### 36. E1 slide 7: mirrored echo (cat 3)
- AFTER: "a budget that lives only in the prompt is a budget the model can argue away, so halts live in code and in the ledger."
- Problem: "A budget ... is a budget" echoes the BEFORE epigram instead of stating the rule.
- Fix: "the model can argue past a budget stated only in the prompt, so code enforces every budget and the ledger records every halt."

### 37. E1 slide 12: "honestly" dropped, leaving a tautology (cat 4)
- BEFORE: "a local-model squawk logged honestly"
- AFTER: "a local-model squawk logged as a squawk"
- Problem: The new phrase says nothing.
- Fix: "a local-model failure logged as a squawk rather than hidden or scored as a FAIL".

### 38. Orientation slide 26: Ollama called a model (cat 4)
- BEFORE: "runs on anything, including Ollama"
- AFTER: "runs on any model, Ollama included"
- Problem: Ollama is a local model runtime, not a model.
- Fix: "runs on any provider, including a local Ollama endpoint."

### 39. Orientation slide 32: communication channels dropped (cat 1, DROPPED; may be deliberate)
- BEFORE: "Office hours Tuesday and Thursday afternoons by Calendly, and the Discord between classes."
- AFTER: (removed)
- Problem: The schedule part could go, but the Discord channel and the Calendly booking route are not dates or times.
- Fix: "Book office hours through Calendly. Between classes, use the course Discord."

### 40. E0 slide 2 and E1 slide 2: time allocations per part dropped (cat 1, DROPPED; may be deliberate)
- BEFORE: "Framing for ten minutes; the two maps for fifteen; ... thirteen ... fourteen ... eight" / "Ten minutes of framing, twenty on the spine, ..."
- AFTER: E0 gives no durations. E1 gives only "gets the most time".
- Problem: This is the lecture's pacing plan. The other slides keep their `[~N min]` tags, so dropping the plan here looks like an over-reach of the time-removal rule.
- Fix: Ask Jeffry whether pacing counts as "times" for the deliberate-removal rule. If it does not, restore the minutes.

---

## Problems that were already in BEFORE (outside scope; the pass neither caused nor fixed them)
- E1 slide 4 cut: "Chain-of-thought (Wei et al., 2022) / 'Let's think step by step.'" The phrase comes from Kojima et al. (2022), zero-shot CoT, not from Wei et al.
- E1 slide 8 cut: "hundreds of thousands of GitHub stars in weeks." AutoGPT passed roughly 100k stars in its first weeks, so "hundreds of thousands" in weeks needs a source.
- E1 slide 9: the start date of one project (January 2026) is used as evidence for "how long the field took to act on the lesson".

---

## Repair log

Notes edited in `fix/orientation.json`, `fix/e0-index-zero.json`, `fix/e1-agent-loop.json` (array lengths 34/22/14 kept, JSON valid). One slide value edited in `sitekit/voice/e1-agent-loop.json` (#36).

1. FIXED. Removed "(Raji and colleagues, 'Auditing Work')" from E0 slide 19 notes. FOR JEFFRY: the slide wording itself (BEFORE and AFTER) reads "Raji et al.; 'Auditing Work'", and that paper is by Groves, Metcalf, Kennedy, Vecchione, and Strait. Pre-existing, not changed.
2. FIXED. Slide 32 notes back to "Consultations are not made up late."; "before the week ends" restored in the slide 32 and slide 12 cut text. Calendly not restored (ruling).
3. FIXED. Slide 12: "This schedule works because the class has fewer than ten students" and "With nine or fewer students, three deep slots ... four deep Drifts".
4. FIXED. E1 slide 10 cut restored to BEFORE: "Governance arrived as the missing component, not as a wrapper." FOR JEFFRY: "not as a wrapper" (BEFORE) still sits against orientation slide 18, "wraps them ... It does not run agents." Pre-existing tension.
5. LEFT (ruling: WTClass removal). FOR JEFFRY: no deck now says where the repository URL and flight-log PDF are submitted (orientation slides 20, 21, 33; E0 slide 21).
6. FIXED. Slide 21 notes open with "The rubric will be posted before the first Evolution is due. This slide shows its intended shape ..."
7. FIXED. Slide 11 notes: "anti-submarine warfare", "a ship", "stops engines to listen", "cannot happen at the same moment".
8. FIXED. Slide 30 cut: "feedback/ my review notes; apart from brief.md in final/, nothing else in the repo comes from me".
9. FIXED. Slide 5 notes restored to "Most of what went wrong in 2023 was the halt condition."; cut to "The halt condition is the part the 2023 loops neglected."
10. FIXED. E0 slide 9: "Since 2024, tool results have filled most of an agent harness's context window, so the course teaches tools before context management".
11. FIXED. E0 slide 5 cut: "The foundation is where the deferred cost comes due." (weights/infrastructure removed).
12. FIXED. E0 slide 14 evaluation row restored to BEFORE: "in both, the human does most of it." (reviewer's "harness can run tests" not used; it would add a fact).
13. FIXED. E0 slide 22: "most of its design choices make sense only after you ask who was answering for them, and for what" (BEFORE's "most" kept).
14. FIXED. Slide 17: "Later designs reuse these ideas with a language model in the reasoner slot, and part of the survey is to trace which ideas each one reuses."
15. FIXED. E1 slide 9 cut: "so it optimized for a benchmark and left everything else out."
16. FIXED. E1 slide 14: "the injection test point in E3."
17. FIXED. Slide 25: "and for that reason gzkit renders seventeen hooks into it."
18. FIXED. Slide 34 cut restored: "...had to answer for them. Build one you can answer for."
19. LEFT (ruling: E0 Anthropic workflow advice). FOR JEFFRY: the paraphrase "recommends the workflow wherever the path is known in advance, and the open loop only where it is not" has not been checked against "Building Effective Agents".
20. FIXED. E0 slide 5 restored: "'done' is the most dangerous word in the course." FOR JEFFRY: whether to add a reason after it (the pass's reason, "the agent's halt and your attestation both depend on it", was not his).
21. FIXED. E1 slide 8 cut: "It also produced the field's first shared record of failures" (matches notes; "first" is BEFORE's, unsourced).
22. FIXED. E1 slide 10 notes: appositive dropped. Note: the E1 slide title (BEFORE and AFTER) still reads "the thing the loop lacked: a record of intent that survives the session" (pre-existing).
23. FIXED. E0 slide 3: "Ask the class who answered ..., and wait for answers."; slide 16: "Ask the class where on this curve each of them was last week."
24. FIXED. E0 slide 9: "Two features of the table need attention. First, the middle is inverted from the catalog order".
25. FIXED. E0 slide 18: "The Docs gate checks that what is written matches what runs."
26. FIXED. E0 slide 19: "it makes the engineer who signed answerable for that build."
27. FIXED. Slide 10: "You fly the rest of the sortie on your own; it is due the evening before the next session."
28. FIXED. Slide 6: "observed" dropped; cut: "Without both sides, governance is theater."
29. FIXED. Slide 7: "because the class has fewer than ten students".
30. FIXED. Slide 16: "it is about a hundred and fifty words on purpose." Attributions kept.
31. FIXED. Orientation slide 18 closing line deleted; E0 slide 20 now ends at "...has left the session."
32. FIXED. Slide 9 closer cut to "...closed out under the Heavy lane."; slide 22: "...closed out under the Heavy lane and released. You do not start a new project for it."; slide 2 cut restored to BEFORE ("The course is about being the one who answers."); slide 15 closer cut.
33. FIXED. Slide 13: "the fifth matters most:"; slide 34 notes: clause about designs that lasted cut (BEFORE also carried that unsourced generalization).
34. FIXED. "we" replaced on slides 6, 7, 17, 18, 25, 29 (and slide 8 "before we talk" -> "before the consultation").
35. FIXED. Slide 19 gates merged into one sentence.
36. FIXED. E1 slide 7 notes: "the model can argue past a budget stated only in the prompt, so code enforces every budget and the ledger records every halt." Same echo removed from the slide 7 rule in `sitekit/voice/e1-agent-loop.json`.
37. FIXED. E1 slide 12: "a local-model failure logged honestly as a squawk".
38. FIXED. Slide 26: "runs on any provider, including a local Ollama endpoint."
39. LEFT (ruling: Calendly/Discord removal). FOR JEFFRY: orientation no longer says how to book office hours or a make-up consultation, or where to talk between classes.
40. FOR JEFFRY. Do the per-part minutes in E0 slide 2 and E1 slide 2 count as "times" under the removal rule? Other slides keep `[~N min]` tags. Not restored.

Pre-existing (not fixed): E1 slide 4 cut attributes "Let's think step by step" to Wei et al. (it is Kojima et al., 2022); E1 slide 8 cut "hundreds of thousands of GitHub stars in weeks" needs a source; E1 slide 9 uses gzkit's January 2026 start as evidence of how long the field took; E0 slide 19 slide wording "Raji et al." misattribution (see 1).
