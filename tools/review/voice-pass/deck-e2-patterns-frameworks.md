# Deck pass log: e2-patterns-frameworks (Oct 22, 2026)

Files edited in place:
- `/home/claude/site/tools/sitekit/voice/e2-patterns-frameworks.json` (slide wording): 26 of 252 values changed; keys untouched, key order verified identical, JSON valid.
- `/home/claude/site/tools/review/voice-pass/notes/e2-patterns-frameworks.json` (speaker notes): 14 of 14 lecture paragraphs changed; every "Cut from slide N" section and every bracketed timing mark left as it was; JSON valid.

Chain run: humaniser (full), ste-voice (rules 1 to 4 on lecture prose; full rules on table cells), scholarly-voice (final surface), humaniser greps and shape battery as a check.

## Patterns that dominated

1. "Tonight's claim" / "the claim" framing (BRIEF house rule). Slide heading "Tonight's claim, which Sortie 2 will try to disprove" became "The statement Sortie 2 will try to disprove". Notes slide 3 "Read the claim: same task, two patterns, identical tool traces, a difference the ADR predicted" became "Sortie 2 tests one statement: the same task runs under two patterns with identical tool traces, and the cost or quality difference that ADR-1 predicted appears in the evidence." Notes slide 13 "The claim again." became "The design claim is the same statement: ..." (design claim is course vocabulary and stays).
2. Definition-colon ledes and fragment chains (#35; slides read as parts lists). "The abstraction tax: every layer a framework adds is a layer you cannot see into during Drift. If you cannot explain what the framework did on turn three, it owns you." became "Every layer a framework adds is a layer you cannot see into during Drift (the abstraction tax). If you cannot explain what the framework did on turn three, you do not own the loop." "Chains, agents, tools, memory as objects: the first wrapper around the ReAct prompt." became "LangChain wrapped the ReAct prompt in objects (chains, agents, tools, memory)." Notes slide 4 and 5 catalog entries ("Prompt chaining: a fixed sequence...", "Refactor one: orchestrator-workers.") became full sentences with the pattern or the component as subject.
3. Actor removal (#3, #5, #31). "Every output is validated against a Pydantic model before it acts; malformed ones are retried or rejected." became "Pydantic AI validates every model output against a Pydantic model before the output acts, and retries or rejects a malformed one." "Popularity was rejected as a reason. What counted: ..." became "The ADR rejected popularity as a reason. It counted zero external dependencies, ...". "tracing built in" became "tracing ships with the runner".
4. Epigram landings and antithesis closers (#36). "A wrong prediction honestly recorded is worth more than a right one you cannot show." became "The amended ADR gives the Chase the prediction, the evidence, and the correction on one record, which a correct prediction with no evidence cannot give." "because the prediction was not a prediction" became "because an ADR dated after the result could have been written from the result, and the Chase cannot tell the difference." "with consequences, not adjectives" became "each with its consequences stated". "which is itself the lesson" became "the rate at which these rows go stale is part of the teardown".
5. Invented authority (#37). "Frameworks change monthly" (slide 3) became "A new framework has arrived every year since 2022", which the deck's own teardown dates (2022, 2023, 2024, 2025) support. "these SDKs change monthly" (slide 9, twice) dropped in favor of the dated scope line plus "verify each row against the current docs". "The falsifier people miss is the last one" became "The fourth falsifier is the one to read twice." "where the two differ most" became "where the two differ".
6. Argued heading. "The real subject is control, not the API" became "Where control lives, framework by framework" (a label, similar length).
7. "named"/"naming" ban. "the loop refactored into a named pattern" became "a pattern from the catalog" (slide subtitle and notes slide 1); "A pre-mortem naming a week-12 failure" became "A pre-mortem that states a week-12 failure".
8. Em dashes: four slide keys (run-of-show description, two subtitles, constraint archaeology) rewritten with a comma or colon.
9. Schedule and management asides removed from notes: "Last week"/"This week"/"next week"/"week eight"/"week ten"/"week twelve" became Evolution numbers (the slides themselves tie E3, E8, and E12 to those weeks); "Labor Day was Monday; nothing moved", "Two minutes on", "Finish the card at five; Go or No-Go at 5:46; fly test point one in lab", "Consultation at five: ..." dropped; the bracketed "[Verify ... before class ...]" and "[Challenge list from chapter 11; expand each ...]" notes dropped, with the provenance kept in prose ("the list is chapter 11's"; "The feature rows are as of early 2026"). "we go there properly in week eight" became "Evolution 8 takes it up in full".

## Self-audit artifacts (notes, after the final pass)

Closer list (last sentence of each lecture paragraph, timing marks stripped):
1. The build refactors the loop into a pattern from the catalog and records the choice in ADR-1.
2. The lecture has five parts: the framing, the pattern catalog (the longest part, because the patterns are the build), four teardowns grouped by their theory of control, the reference design's model ADR, and the evaluation lens with Flight Card 2.
3. If the predicted difference does not appear, the ADR recorded a rationalization.
4. That advice is the null hypothesis of your ADR.
5. With the tools held constant, the measured delta is attributable to the decision in your ADR and to nothing else.
6. If you cannot explain what the framework did on turn three, you do not own the loop.
7. In judgment-loop terms, LangChain's authors moved control from the library into a graph that the user draws, and the cost is that you now have to draw it.
8. No one in the conversation is an evaluator, so one role's polished summary becomes the next role's fact.
9. The feature rows are as of early 2026, and the rate at which they go stale is part of the teardown.
10. An ADR written after the code records a rationalization.
11. The ten challenges, which you will put to a peer's ADR at the Chase station, are so what, scope, alternative, dependency, gold standard, timeline, evidence, consumer, regression, and parity (the list is chapter 11's).
12. The amended ADR gives the Chase the prediction, the evidence, and the correction on one record, which a correct prediction with no evidence cannot give.
13. An ADR dated after the refactor commit is a FAIL, because an ADR dated after the result could have been written from the result, and the Chase cannot tell the difference.
14. Choose one on evidence, record what you gave up, and be ready to be wrong where the ledger can see it.

Disposition: 6 and 10 are the slide's own rule lines with the reason in the sentence before; 14 mirrors the closing slide. None restates its paragraph.

Lede list (first sentence of each lecture paragraph):
1. Evolution 2. In Evolution 1 you built a loop that halts.
2. The lecture has five parts: ... (one-sentence run-of-show paragraph)
3. Framing. Learn what a framework assumes about control before you learn its API.
4. The catalog lists five workflows and the agent.
5. The worked example, in prose.
6. The source's advice forms a ladder, and each rung becomes a row in your ADR.
7. The first teardown covers one company and two theories of control.
8. Two more theories.
9. The vendor SDKs, read by their theory of control.
10. The reference design's model ADR decides a command-line parser.
11. Stress a decision before you record it.
12. A weak submission chose its framework because a tutorial used it, ...
13. Flight Card 2 stays at the center of the envelope and is the first sortie with a dependency: Sortie 1 must have passed.
14. A framework is a theory of who owns the loop.

Disposition: no repeated opening; no "X is Y: a, b, c" lede (paragraph 2's colon introduces the part list the paragraph exists to give, and the count is stated).

Claim list (frequency or consensus statements):
- "A new framework has arrived every year since 2022." (slide 3) Source: the deck's teardowns (LangChain 2022, role-based frameworks 2023, LangGraph and Pydantic AI 2024, vendor SDKs 2025).
- "Most production 'agents' are workflows, and should be." (slide 3 and notes 3) Source: Anthropic, "Building Effective Agents," December 2024, cited in the panel heading and now in the notes sentence.
- "small local models fail the schema more often, which Evolution 3 measures" (notes 8) Source: the E3 sortie, stated in the sentence.
- "Every framework is a theory of who owns the loop" / "You own every edge" / "every output" / "every layer": universal statements of the lecture's thesis or of a library's documented behavior, not frequency claims about people.
- Removed: "Frameworks change monthly", "these SDKs change monthly" (twice), "The falsifier people miss", "where the two differ most".

## ste_check lines declined

- 17 sentences over 25 words: all in explanatory lecture paragraphs, where the brief sets no ceiling. The longest (45 words, "Your ADR-1 takes the same shape: ...") carries the six-part ADR list and loses the count if split.
- 8 paragraphs over six sentences: one paragraph per slide; the deck brief forbids merging or splitting slides.
- Gerund/nominalized subjects: "assumption", "distinction", "decision", "measurement", "reference design", "judgment-loop" are stipulated objects or proper course terms, not nominalized verbs.
- Passives: "cannot be scripted" (the source's wording of the catalog's condition); "what was attested" (course vocabulary; attest is the act). "tracing is built in" was fixed.
- Noun clusters: all six are span-detector false positives across clause boundaries.

## Left as is, with reasons

- "[Summarized from the ADR title; verify against the ADR text.]" (slide 10 value) is a QA aside, but an empty value's effect on the build is unknown, so the key is unchanged; the matching note in the lecture prose was dropped. Jeffry may want this key removed at build.
- "Timeline: when we know" (slide 11 challenge label) keeps "we": it is the chapter 11 challenge wording.
- "Cost: what the schema cannot express, the model cannot do (E3)." and "Types as governance; conversation as coordination": symmetric constructions marking a real partition; kept (scholarly-voice rule 8).
- "Alternatives listed as names, no consequences": noun "names", allowed.
- Run-of-show description cells (keys under the timing rows) were edited only for the one em dash; the build may drop them anyway.
- "Evidence: measured, not read" and "Habit is not a constraint": gzkit/reference-design wording.
