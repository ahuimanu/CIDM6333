# Voice pass log: glossary-part1

File: /home/claude/site/tools/review/voice-pass/glossary-parts/part1.py (49 `g(...)` entries). Original kept at the scratchpad copy part1.orig.py for the diff.

Edited only `what`, `when`, `why` literals. `term`, `cat`, `src`, `aliases`, `ch` verified identical to the original on all 49 entries by loading both files and comparing field by field. `ast.parse` passes on the finished file. 120 string literals changed (every entry had at least one).

## Changes by pattern

### Definition-colon ledes (#35) and parts lists (STE scope / scholarly-voice "full sentences")
Almost every `what` opened "The X: a, b, c." or as a headless noun phrase. Each now opens with the term as grammatical subject and a verb, with the specification moved to the next sentence.
- Before: "The unit of progression: one lecture, one build, one sortie, each adding one layer to the system." After: "An Evolution is the course's unit of progression. Each one pairs one lecture with one build and one sortie, and each adds one layer to the system."
- Before: "gzkit's five checkpoints on a piece of work: Gate 1 ADR (the decision is written), Gate 2 TDD ..." After: "The five gates are gzkit's checkpoints on a piece of work. Gate 1 is the ADR (the decision is written). Gate 2 is TDD ..."
- Before: "Velocity Increased, Bugs Expected Software: gzkit's name for the failure class ..." After: "V.I.B.E.S. stands for Velocity Increased, Bugs Expected Software. It is gzkit's term for the failure class ..."

### Epigram landings, antithesis closers, pseudo-clefts (#36, house cadence bans)
- Flight card/why. Before: "Pre-registration is what makes a passing run evidence instead of a story told afterwards." After: "A run counts as evidence only if the card was written before it. A card written afterward can be fitted to whatever happened."
- Squawk/why. Before: "The debrief is where findings become work items instead of memories." After: "Without a squawk, a finding from the debrief has no record and no owner."
- Falsifier/why. Before: "... not by whether the demo ran." After: "... because a demo can run for reasons the claim did not predict."
- Persona/why. Before: "The anti-trait explains; the permission deny enforces. Both, in that order." After: "The anti-trait tells the model what the role must not do, and the permission deny makes the harness refuse it. The course asks for both, with the anti-trait written first."
- Hooks/what. Before: "A hook is a mechanism in the loop; a sentence in the prompt is a request." After: "... whereas a sentence in the prompt is a request the model may ignore."
- Permissions/why. Before: "E3's point: the gate is enforced by the harness, not requested of the model." After: "E3 argues that a gate has to be enforced by the harness, because a gate requested of the model in the prompt can be ignored."
- Evolution/what. "the order is what matters" became "the order of the layers does not change."
Kept as Jeffry's or gzkit's phrasings: "a claim without a sortie is an opinion", "A claim without a receipt is not evidence", "The file beats the memory of the file", "'The ledger is the black box.'", "a map, not an encyclopedia" (ADR-0.0.54's title, now attributed in AGENTS.md).

### "names"/"named" as verb (house ban)
- Design Analysis: "each named with its mechanism" became "states the mechanism behind each".
- Hooks: "Claude Code names them SessionStart ..." became "Claude Code's hooks are SessionStart ...".
- Judgment loop: "name the decision" became "It states the decision".
Remaining grep hits ("three names", "field names", "hook names") are the noun and stay.

### "claim" as a thesis stand-in
- RED witness/why: "E10's Sortie 10 claim is that ..." became "Sortie 10's design claim in E10 is that ...".
- Exceptional, Expansion card, Sortie: bare "claim" became "design claim" where that is what it meant. "typed claim" (HandoffResult) untouched.

### Actor removal, second person, "you" (#3/#5/#31, scholarly-voice agent check)
"you run the build", "yours", "you did not write it" became "the student ..." throughout. "The method was developed for CIDM 6330" became "The instructor developed the method ...". "The Teardowns ... are read" became "The course reads ...". "the catalogue is needed" became "a reader needs the catalogue".

### Invented authority (#37)
- Expansion card: "usually after a center-of-envelope sortie has passed" became "The expected order is a center-of-envelope sortie first, then the expansion" (a norm, not a frequency claim).
- Design Analysis/when: "one is done live in most lectures" became "the Teardown segment of a lecture performs one live" (sourced to the Teardown entry's own text).
- AGENTS.md/why: "the first probe of every exercise" became "The first probe of an exercise".
- Controller/worker/reviewer: "under every name since FIPA" became "under one label or another since FIPA".

### Empty `why` fields filled
Final System, Covenant, Attestation, Brief, PRD, Expansion card, V.I.B.E.S., Controller/worker/reviewer, Exceptional, Route A/B, Judgment loop, GitHub Copilot now have a `why`, each derived from the entry's own `what`/`src` text. Empty `when` fields filled only where the file itself supplied the source: Ledger and Receipt ("The term is gzkit's"), Layers of truth (ADR-0.0.9, from the ADR entry's list), Gemini CLI and Chase (moved from `what`).

### Schedule words
"that week's problem" (gzkit/why) became "that chapter's problem"; "the memory week" became "the memory Evolution".

## Self-audit artifacts (after the final pass)

Closer list: all 120 non-empty field closers were listed out of context (see the check run). Lines that would work as a caption: "The file beats the memory of the file." and "A claim without a receipt is not evidence." Both are gzkit's own sentences and stay per the brief. No other closer is an antithesis or moral; each states a rule, a fact, or a reason.

Lede list: all 49 `what` openers are "<Term> is/are/stands for ...". Shared skeleton is the glossary form the brief asks for (what, who/when, why), so #38 is accepted by design. Three ledes end in a colon list (Squawk, Hooks, Context window); each list is the entry's content (the four squawk destinations, the loop events, the window's components), so they stay.

Claim list: 11 sentences with "every"/"never". All are course or gzkit rules (every sortie has a Chase; the ledger records every command; AGENTS.md loads every turn; self-review is never Gate 5, rule GZK-GOV-007), each traceable to the entry's `src`. No "most"/"usually"/"often" remains.

Sibling diff: not applicable (one file, one page).

## ste_check lines declined, with reasons
- 11 sentences over 25 words: all in explanatory text (glossary definitions, not procedures), where the brief sets no ceiling. Each carries a list that would lose precision if split: the Design Analysis component list, the ADR citation list, the Final System's three conditions, the Index zero two-part definition, the context-window contents, the Hooks event list.
- 6 "paragraphs" over 6 sentences: artifacts of the extraction (term + what + when + why joined as one block).
- Gerund/nominalized subjects: all heuristic false positives ("Careful reading becomes skimming" is the Degradation Pattern's own description; "Mutation testing", "Summary laundering", "In aviation", "In precedence" are terms or adverbials).
- Passives with no actor: those left are states ("is Completed"), gzkit's quoted rule, or passives whose actor is in the same sentence ("the controller rejects"). "is deleted on sight" (Persona) kept because the reason is attached in the same sentence.
- Noun clusters of 4+: all are enumerations with commas stripped by the checker, URLs, or proper names.
- Semicolons: 1 remaining, in the ADR `when` inside the gzkit ADR-0.0.2 parenthetical ("argparse over click: popularity is not rationale") was already a colon; the one the checker counts is in the Skills `src` field, which is not edited.

## Items left as is, flagged
- Attestation/what keeps "Completed — Partial" with its em dash: it is gzkit's status value, treated as code under the never-edit rule.
- En dashes in "2025–26", "controller–worker" are ranges and compounds, not em dashes.
- GitHub Copilot/why ("It is a vendor harness the course compares with OpenCode, Claude Code, and Codex.") is inferred from the category and the sibling entries, not from a stated course fact; confirm or cut.
- Sprint and Drift/when now says "The instructor developed the method"; the original said only "Developed for CIDM 6330", so the attribution is mine.
