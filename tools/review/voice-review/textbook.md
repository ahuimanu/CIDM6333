# Voice-pass review: textbook

Scope: the 34 textbook pages (`docs/textbook/`: index, readings, ch-01 to ch-26, appendices A to G). BEFORE is `docs-before-387413a/textbook/`. I extracted the visible text of both versions (HTML stripped, with script, style, nav, header, and footer removed), read every diff line, and read the AFTER text of every chapter, the index, and Appendices C and G in full. Appendix headings changed from "Appendix A —" to "Appendix A:" on purpose; I did not report those changes.

The revision is light: about 330 changed lines out of roughly 15,000 words. Most edits break up semicolon lists, attach actors, or replace "name" verbs. Below are 37 findings, most serious first.

Counts by primary category: 1 (facts) = 20, 2 (contradictions) = 5, 3 (surviving shapes) = 9, 4 (meaning damage) = 3.

---

### 1. index: "one Evolution per session"
- Category: 1 (CHANGED)
- BEFORE: "The course runs one Evolution at a time."
- AFTER: "The course runs one Evolution per session."
- Problem: "At a time" means the Evolutions run in sequence. "Per session" makes a schedule claim, and it conflicts with the Glossary ("Evolution: the weekly unit of the course") and with "one layer per week" in the table directly below it.
- Fix: Restore "one Evolution at a time", or write "one Evolution per week" if that is the intended statement.

### 2. ch-05 §5.4: the halt-condition sentence no longer makes sense
- Category: 1 (CHANGED causal statement) and 4
- BEFORE: "A loop without a halt condition is a bill."
- AFTER: "A loop without a halt condition runs until the budget is spent, so the halt condition is the cost control."
- Problem: A budget is itself a halt condition (ch-10 §10.1 lists "an exhausted budget" as one), so a loop "without a halt condition" cannot stop when the budget runs out. The sentence also ends on an epigram.
- Fix: Write "A loop without a halt condition keeps calling the model, and each call costs money, until someone stops it."

### 3. ch-05 gzkit paragraph against §5.2: one thing lacked, or three?
- Category: 2
- §5.2 (AFTER): "What it lacked: memory, budget, verification."
- gzkit paragraph, BEFORE: "the loop plus the thing the loop lacked"
- gzkit paragraph, AFTER: "the ReAct loop plus the one thing that loop lacked, a record of intent"
- Problem: "The one thing" claims the record of intent was ReAct's only gap. Twenty lines earlier the same chapter lists three gaps, and none of them is a record of intent.
- Fix: Write "the ReAct loop plus a component that loop lacked: a record of intent that survives the session."

### 4. index Contents: "a later edition" against the Status note
- Category: 1 (ADDED) and 2
- BEFORE: "Every chapter is an outline edition: ... The prose follows."
- AFTER: "Each chapter is published here as an outline. ... The full prose will follow in a later edition."
- Problem: The Status paragraph just above says chapters move through outline, draft, reviewed, and final, and that "I am writing the prose in the order the course needs it". That means the prose arrives during the term, not in a later edition.
- Fix: Write "The full prose replaces each outline as the chapter's status advances."

### 5. ch-02 §2.4: new attribution to Anthropic, and a dropped stance that Exercise 2 still assumes
- Category: 1 (ADDED and DROPPED)
- BEFORE: "Most production \"agents\" are workflows, and should be."
- AFTER: "Anthropic's own advice is to build the workflow unless the task needs the agent's flexibility, and a system marketed as an \"agent\" may be a workflow by this definition (exercise 2)."
- Problem: The revision puts a paraphrase in Anthropic's mouth and gives no quotation. It also drops the normative "and should be", yet Exercise 2 still says "Say why that is the right design".
- Fix: Quote the post's own sentence (it advises finding "the simplest solution possible" and using agents "when flexibility and model-driven decision-making are needed"), and keep a sentence that says why a workflow is usually the right design.

### 6. readings, Chapter 2 entry: the banner's content is restated differently
- Category: 1 (CHANGED)
- BEFORE: "the page now carries a banner that the tooling landscape has changed"
- AFTER: "a banner that says its tooling advice is dated"
- Problem: "The landscape has changed" and "its advice is dated" are two different statements about the source, and the reviser did not check the page.
- Fix: Quote the banner text verbatim, or restore the BEFORE wording.

### 7. ch-09 §9.1: a thesis is now attributed to two named authors
- Category: 1 (ADDED attribution)
- BEFORE: "The claim that most of an agent product is not the model. Böckeler; the OpenAI post; gzkit's appraisal ..."
- AFTER: "Böckeler and the OpenAI post argue that most of an agent product is not the model."
- Problem: BEFORE listed the claim next to the sources. AFTER says both Böckeler and Lopopolo argue it, which needs a check against each article.
- Fix: Confirm that each article makes the argument, or write "The readings for this section (Böckeler; Lopopolo for OpenAI) address the position that ...".

### 8. index front matter: "its ledger kept the receipts for each one"
- Category: 1 (CHANGED)
- BEFORE: "the difference is that here we kept the receipts."
- AFTER: "The kit differs in that its ledger kept the receipts for each one."
- Problem: The new sentence says the ledger alone holds a receipt for every failure listed. Appendix G cites CHANGELOG, RELEASE_NOTES, the insights corpus, and AGENTS.md as well as the ledger.
- Fix: Write "The kit differs in that its records (ledger, changelog, insights corpus) kept the receipts."

### 9. readings, Chapter 10 entry: a version qualifier was dropped
- Category: 1 (DROPPED)
- BEFORE: "https://gzkit.org/examples/tutorial-first-project/ (re-verify against gzkit 0.34.9)"
- AFTER: the URL alone.
- Problem: The note was visible text, not a bracketed build note. It told the reader that the tutorial had not been checked against the current release. The version note later on the same page ("The tutorial page pins no version") now carries that warning alone.
- Fix: Restore it as a plain scope statement: "(not yet checked against 0.34.9; see the version note below)".

### 10. index thesis: "and engineers" was dropped
- Category: 1 (DROPPED) and 4
- BEFORE: "Everything here is in service of building systems, and engineers, that can answer."
- AFTER: "The survey, the build, and the governance chapters all serve that purpose."
- Problem: The BEFORE sentence had two objects, systems and engineers that can answer. The Drift half of the course (the engineer defends the work without AI) rests on the second, and it is gone. The new sentence is also a summary closer (#30).
- Fix: Write "The book's purpose is to build systems that can answer for their output and engineers who can answer for those systems."

### 11. ch-15 §15.4: what the ledger is was redefined
- Category: 1 (CHANGED)
- BEFORE: "Frontmatter can lie; the ledger is the truth."
- AFTER: "Frontmatter can carry a false status; the ledger is the record a gate consults."
- Problem: The ledger has gone from authoritative state (the Glossary says "runtime truth") to the thing a gate reads. That is narrower, and the chapter does not support it as stated, because gates also read L1 canon.
- Fix: Write "the ledger is the authoritative record, and it outranks frontmatter (L2 > L1)."

### 12. index: first-person authorship added
- Category: 1 (ADDED attribution)
- BEFORE: "In January 2026 a governance kit was started ..." / "Sprint and Drift ... was developed for CIDM 6330"
- AFTER: "In January 2026 I started a governance kit ... before I would show it to students." / "I developed Sprint and Drift ..."
- Problem: The passive BEFORE made no authorship claim. AFTER makes two, which Jeffry should confirm. The brief allows "I" only where the instructor speaks about a decision.
- Fix: Keep the sentences if Jeffry confirms them; otherwise restore the passive.

### 13. ch-01 §1.1: the layer comparison changed meaning
- Category: 1 (CHANGED)
- BEFORE: "Agentic AI is thin and new; the foundation is old and cracked."
- AFTER: "The agentic layer is the newest and thinnest, and the data foundation is the oldest and the one with the defects."
- Problem: "Cracked" said the foundation has defects. "The one with the defects" says it is the only layer with defects. The superlatives ("thinnest") are new claims.
- Fix: Write "The agentic layer is new and thin, and the data foundation is old and has defects that the layers above inherit."

### 14. ch-01 gzkit paragraph: "runs no model of its own"
- Category: 1 (CHANGED)
- BEFORE: "without running a model at all"
- AFTER: "runs no model of its own"
- Problem: "Of its own" suggests that gzkit runs someone else's model, which is a different statement from "runs no model at all".
- Fix: Write "and runs no model".

### 15. ch-04 §4.3: identity became lineage
- Category: 1 (CHANGED)
- BEFORE: "Read these before AutoGen and CrewAI; they are the same designs."
- AFTER: "Read these before AutoGen and CrewAI, which reuse the same designs."
- Problem: "Reuse" asserts that AutoGen and CrewAI borrowed from FIPA and JADE. BEFORE asserted only that the designs are the same, possibly through rediscovery, and ch-06 §6.4 says "FIPA rediscovered".
- Fix: Write "which repeat the same designs".

### 16. ch-06 §6.2: a causal claim was added
- Category: 1 (ADDED)
- BEFORE: "Why they mattered anyway: they named the ambition."
- AFTER: "They mattered anyway, because they stated the ambition the field then pursued."
- Problem: "The field then pursued" is a new historical claim with no source, and it ends the paragraph on a landing.
- Fix: Write "They mattered anyway, because they stated the goal of a fully autonomous loop."

### 17. Appendix F heading: pitfalls became defects
- Category: 1 (CHANGED)
- BEFORE: "Known gotchas against py-gzkit 0.34.x (verified 2026-08-24)"
- AFTER: "Known problems in py-gzkit 0.34.x (verified 2026-08-24)"
- Problem: Several items are usage steps, not defects in gzkit ("Commit them once", "Do not work around either hook"), and "problems in" attributes them to the tool.
- Fix: Write "Known pitfalls with py-gzkit 0.34.x".

### 18. Appendix G, 2026-05-23 row: an actor was added
- Category: 1 (ADDED)
- BEFORE: "Four questions bundled in one prompt"
- AFTER: "The agent bundled four questions in one prompt"
- Problem: The reviser supplied the actor, and the source (AGENTS.md § Operator Doctrine) has not been checked.
- Fix: Confirm the actor against the insights entry, or restore the BEFORE text.

### 19. readings version note: "checked" became "tested"
- Category: 1 (CHANGED)
- BEFORE: "Appendix F's gotchas were checked against 0.34.5."
- AFTER: "Appendix F's gotchas were tested against 0.34.5."
- Problem: "Tested" claims a run against that release, which is more than "checked" claimed.
- Fix: Restore "checked".

### 20. ch-13 §13.4: the section is now said to build the server
- Category: 1 (CHANGED)
- BEFORE: "The reference design's missing piece: gz status, gz validate, ... as MCP tools and resources"
- AFTER: "The reference design has no MCP server. This section builds the one it lacks ..."
- Problem: Ch-07 and this chapter's own gzkit paragraph call the server "the student project". The outline section does not build it.
- Fix: Write "This section specifies the server the student builds: ...".

### 21. ch-12 §12.5 and index ¶1: small additions
- Category: 1 (ADDED)
- ch-12, AFTER adds: "a brittle model fails wherever the tool contract is loose". This is plausible, but it is a new causal mechanism.
- index, AFTER adds "in the same term" to "the course it grew out of does".
- Problem: Both add content that BEFORE did not state.
- Fix: Keep ch-12 if Jeffry agrees with it. Cut "in the same term" from the index.

### 22. ch-09 §9.4 against Appendix G: incident count
- Category: 2
- ch-09 (unchanged): "Twenty-five dated incidents (Appendix G)"
- Appendix G: 21 dated rows.
- Problem: The count disagrees with the table it points to.
- Fix: Change the number to "Twenty-one", or add the four missing rows.

### 23. ch-26: who executes the closeout ceremony
- Category: 2
- Learning outcome (unchanged): "Conduct a closeout ceremony: the student executes, the instructor observes and attests."
- §26.3 (unchanged): "the agent (here the student) presents paths and commands, not conclusions; the human executes and observes"
- Problem: The outcome says the student executes, and §26.3 says the human (the instructor) executes.
- Fix: Decide who runs the commands and state it the same way in both places.

### 24. ch-03 §3.1 against Appendix C: one failure or several
- Category: 2
- ch-03: "Cognitive surrender, mediated observation, governance theater: three names for the same failure."
- Appendix C: these three appear as separate human-side patterns alongside the Degradation Pattern.
- Problem: One page treats them as synonyms, and the other lists them as distinct patterns.
- Fix: In ch-03, write "three related patterns (Appendix C) that end in the same failure".

### 25. ch-18 §18.2 against Appendix G and ch-06: a gzkit rule was paraphrased in one place only
- Category: 2 and 4
- BEFORE (ch-18): "A subagent's claim is not evidence; receipts are."
- AFTER (ch-18): "A subagent's claim becomes evidence only when a receipt backs it."
- Appendix G quotes the rule as "a subagent's claim is not evidence".
- Problem: Ch-18 now paraphrases the gzkit rule that Appendix G quotes, so the two pages state it differently. Ch-06 also still has the unclear phrase "an independent reviewer whose claim is not evidence".
- Fix: In ch-18, quote the rule as gzkit states it ("a subagent's claim is not evidence") and add "a receipt is". In ch-06, write "an independent reviewer whose verdict counts only with the evidence it cites".

### 26. ch-08 §8.3 and ch-12: the "membrane" metaphor survived
- Category: 3 (decorative metaphor)
- AFTER (unchanged): ch-08 "Hooks as a governance membrane."; ch-12 outcome "Explain hooks as a governance membrane"; ch-12 table caption "The membrane".
- Problem: The brief names this metaphor as an example, and it survived on three surfaces.
- Fix: Write "Hooks as enforcement points around tool calls" and give the caption as "Pre- and post-tool checks".

### 27. ch-04 §4.4: wrong actor and a reveal frame
- Category: 3 and 4
- BEFORE: "The lesson LLM agents inherit: gaming the gate is not new (failure mode 9)."
- AFTER: "LLM agents inherit the lesson that gaming the gate is not new (failure mode 9)."
- Problem: Agents do not inherit lessons; their designers do. "The lesson" frame also survived the rewrite.
- Fix: Write "RL agents gamed their reward signals long before LLM agents gamed gates (failure mode 9)."

### 28. index thesis paragraph: an appositive flourish
- Category: 3
- AFTER: "The engineer's role, the one no tool takes over, is to answer for the system."
- Problem: The appositive works as a caption-style flourish. It replaced "irreducible", which carried the same idea more plainly.
- Fix: Write "No tool can take over the engineer's role, which is to answer for the system."

### 29. ch-11 §11.3: a new epigram landing
- Category: 3 (#36)
- AFTER: "Write the ADR before the code. An ADR written after the code rationalizes what was already built."
- Problem: The second sentence is a moral line, not a reason.
- Fix: Write "Write the ADR before the code, so that the alternatives are still open when you weigh them."

### 30. ch-12 §12.2: a new epigram landing
- Category: 3 (#36)
- AFTER: "A confirmation that is not in the ledger does not count as one."
- Problem: The sentence restates the rule above it as a maxim.
- Fix: Write "A gate that finds no confirmation event in the ledger refuses the write."

### 31. ch-17 gzkit paragraph: filler closer
- Category: 3
- AFTER: "The --single-driver --reason honesty flag completes the set."
- Problem: "Completes the set" says nothing about the flag.
- Fix: Write "The --single-driver --reason flag records an honest exception when one agent does both roles."

### 32. ch-17 §17.1: invented authority
- Category: 3 (#37)
- AFTER (unchanged): "the same division of labor (plan / do / check) under every name since FIPA"
- Problem: "Every name since FIPA" is a universal claim with no source.
- Fix: Write "the same division of labor (plan / do / check) that FIPA, MetaGPT, and the gzkit pipeline each use".

### 33. ch-06 §6.5 and ch-12 outcome: "lesson" reveal labels
- Category: 3
- AFTER (unchanged): "6.5 The year's design lesson"; "the 2026-08-23 lesson about enforcement locus"
- Problem: Both labels frame the content as a reveal instead of naming it.
- Fix: Write "6.5 What 2023 lacked" and "the 2026-08-23 incident that moved enforcement to the commit locus".

### 34. ch-09 systems table against ch-21: sibling caption left behind
- Category: 3
- ch-21 (AFTER): "Operational problems"; ch-09 (unchanged): "Operations problems arrive"
- Problem: The revisers fixed the ch-21 caption, but the same row in ch-09 keeps the old phrasing.
- Fix: Change ch-09 to "Operational problems".

### 35. ch-02 Exercise 2 against §2.4: premise and hedge
- Category: 4
- AFTER: §2.4 says "may be a workflow"; Exercise 2 still says "Say why that is the right design."
- Problem: The exercise presupposes the normative claim that the revision removed from §2.4 (see finding 5).
- Fix: Rewrite the exercise as "Say whether a workflow is the right design for it, and why."

### 36. Appendix A template block: glyph change inside the copyable template
- Category: 4 (minor)
- BEFORE: "FLIGHT CARD — SORTIE <N> : <short name>"
- AFTER: "FLIGHT CARD · SORTIE <N> : <short name>"
- Problem: Students copy this block verbatim. A change is acceptable, but it should be made deliberately and kept consistent with gzkit's flight-card-template.md.
- Fix: Match the separator to gzkit's template file.

### 37. ch-01 §1.4: a direct question inside a statement
- Category: 4 (minor)
- AFTER: "Read a system in two passes: from the top, what does it claim to do, and from the bottom, what does it stand on."
- Problem: The embedded questions make the sentence harder to read than BEFORE's compact "(top)/(bottom)" form.
- Fix: Write "Read a system in two passes: from the top, ask what it claims to do; from the bottom, ask what it stands on."

---

## Checked and not reported
- Glossary, Appendix B, Appendix F imperatives, Appendix G passive-to-active rewrites, the Sortie line punctuation (" — " to ". "), and the "name" to "state/list/specify" swaps: the meaning is preserved.
- Readings "Both are now located and listed above": confirmed. Both items appear in the Chapter 9 list.
- ch-03 "set out in four documents": confirmed. The four files appear in the Readings.
- Appendix C "listed after the table": confirmed.

---

## Repair log

Edited: `tools/sitekit/topic-guide.md`, `tools/sitekit/readings.md`. Appendix H not touched.

1. FIXED. "one Evolution per week" (per instruction; restores the weekly meaning without schedule details).
2. FIXED. "A loop without a halt condition keeps calling the model, and each call costs money, until someone stops it."
3. FIXED. "the ReAct loop plus a component that loop lacked: a record of intent that survives the session."
4. FOR JEFFRY. The text lives in `sitekit/textbook.py` (Contents block), outside this repair's file scope: "Each chapter is published here as an outline. ... The full prose will follow in a later edition." BEFORE: "Every chapter is an outline edition: ... The prose follows." Restore BEFORE or use "The full prose replaces each outline as the chapter's status advances."?
5. LEFT. Jeffry's ruling on E0's Anthropic workflow advice stands. The Exercise 2 conflict is repaired under 35.
6. FIXED. Restored BEFORE: "a banner that the tooling landscape has changed".
7. FIXED. Restored the list form: "The claim that most of an agent product is not the model. Readings: Böckeler; the OpenAI post."
8. FIXED. "The difference is that this kit kept the receipts." (BEFORE meaning, no new ledger-only claim.)
9. FIXED. Restored as a hidden build note: "[re-verify against gzkit 0.34.9]".
10. FIXED. "Everything in this book serves the building of systems, and of engineers, that can answer."
11. FIXED. "the ledger is the authoritative record, and it outranks frontmatter (L2 > L1)."
12. FIXED (restored passive) and FOR JEFFRY: "In January 2026 a governance kit was started ... before it would be shown to students." / "Sprint and Drift ... was developed for CIDM 6330". Do you want first person ("I started", "I developed") here?
13. FIXED. "The agentic layer is new and thin, and the data foundation is old and has defects."
14. FIXED. "runs no model."
15. FIXED. "which repeat the same designs."
16. FIXED. "They mattered anyway, because they stated the ambition."
17. FIXED. "Known pitfalls with py-gzkit 0.34.x".
18. FIXED. Restored "Four questions bundled in one prompt".
19. FIXED. Restored "checked".
20. FIXED. "This section specifies the server the student builds to fill that gap:".
21. FIXED. ch-12 restored to BEFORE ("its brittleness makes the contract visible"); cut "in the same term" from the index.
22. FOR JEFFRY (pre-existing). ch-09: "Twenty-five dated incidents (Appendix G)"; Appendix G has 21 rows. Change the number or add rows?
23. FOR JEFFRY (pre-existing). ch-26 outcome "the student executes, the instructor observes and attests" vs §26.3 "the agent (here the student) presents paths and commands, not conclusions; the human executes and observes". Who runs the commands?
24. FOR JEFFRY (pre-existing). ch-03 "Cognitive surrender, mediated observation, governance theater: three names for the same failure." vs Appendix C listing them as separate patterns.
25. FIXED (ch-18: "A subagent's claim is not evidence; a receipt is."). ch-06 phrase "an independent reviewer whose claim is not evidence" is unchanged from BEFORE; LEFT.
26. FIXED. ch-08 "Hooks as enforcement points around tool calls."; ch-12 outcome and caption "Pre- and post-tool checks".
27. FIXED. "Reward hacking in RL agents shows that gaming the gate is not new to LLM agents (failure mode 9)."
28. FIXED. "No tool can take over the engineer's role, which is to answer for the system."
29. FIXED. "Write the ADR before the code, because an ADR written after the code is a post-hoc rationalization." (BEFORE content kept; reviewer's fix would add a new reason.)
30. FIXED. "If the ledger does not record the confirmation, the confirmation did not happen." (BEFORE meaning.)
31. FIXED. "The pipeline also provides the `--single-driver --reason` honesty flag." (Reviewer's description of the flag would add a fact.)
32. FIXED in ch-17: "that FIPA-era designs already used". The same phrase in Appendix H (Lecture E8 framing) is LEFT per instruction.
33. FIXED. "6.5 What 2023 lacked"; "the 2026-08-23 incident that moved enforcement to the commit locus" (per Appendix G).
34. FIXED. "Operational problems arrive".
35. FIXED. "Say whether a workflow is the right design for it, and why."
36. FOR JEFFRY. Appendix A template: "FLIGHT CARD · SORTIE <N> : <short name>" (BEFORE had an em dash, which house rules ban). gzkit's flight-card-template.md was not available to compare; confirm the separator.
37. FIXED. "from the top, ask what it claims to do; from the bottom, ask what it stands on."
