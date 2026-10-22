# Cut pass: e6-context-engineering (Oct 22, 2026)

Chain run: humaniser, ste-voice, scholarly-voice, humaniser battery (check only). 35 edits to `cut/e6-context-engineering.json`. Keys and first lines unchanged; JSON valid; " / " counts unchanged on every line. Slide 2 (key "1") lost two schedule-only lines ("The run of show; the lab at 6:00 is yours", "6:00"), as CUT-BRIEF directs.

## Dominant patterns

- Schedule asides (11 edits): dates, clock times, CC209, "tonight", "Lab at six", minute markers in the lab step table, due dates in the flight card and homework.
  - "Lab tonight (6:00–6:30, self-guided): measure a session, resume it" → "Lab (self-guided): measure a session, then resume it"
  - "Commit evolution-06/flight-card.md by Sun 10/11." → "Commit evolution-06/flight-card.md."
- Mirrored pairs and epigram landings (#36), about 10 edits.
  - "The record is L2: the ledger. The TUI's counter is L3: a view someone else computed." → "The budget record belongs in the ledger (L2). The TUI's counter is a derived view (L3) that the harness computed, so it does not serve as the record."
  - "A free model with an unpublished window makes the lesson unavoidable: the only budget you can trust is the one you declared and logged." → "Because Big Pickle's window is unpublished, the only budget you can check is the one you declared and logged."
  - "One feature per session costs throughput and buys a clean state at every boundary." → "Working one feature per session lowers throughput, and in return each session ends in a clean state."
- "names/named" as a verb (4): "the one the handoff named" → "listed first"; "Your handoff names a commit" → "records"; "A NO-GO names the field" → "identifies".
- "claim" as an assertion stand-in (4): the model's token count in the lab ("write the claim down" → "write its answer down"); "the summary is a claim" → "an assertion without a receipt". Kept: DESIGN CLAIM, "a subagent's claim is not evidence", and the flight card's claim in FAIL/ABORT.
- Actorless and colon-lede shapes: "What must survive goes to a file" → "Write to a file whatever must survive"; heading "Load later, or load elsewhere: progressive disclosure and isolation" → "Progressive disclosure and isolation".
- Invented authority (#37): "These change monthly." → "Recheck these pages before you rely on them, because the vendors revise them."

## Self-audit

- Closer list: extracted per line; no antithesis morals or captions remain. "Answer: your own ledger, not the provider's blob" was rewritten twice; final "because the provider's compaction item is not human-readable" (matches the quoted source).
- Lede list: slide headings are labels; the colon heading on slide 8 was cut to a label.
- Claim list: "often 1,000–2,000 tokens (Anthropic)" keeps its source. Remaining "every" hits are mechanism ("every call", "every turn"), not frequency claims.
- Greps: no em dashes, no AI vocabulary, no hedges, no summary openers; "names" hits are all nouns (tool names, "no names on decisions").

## ste_check lines declined

All 34 over-25 lines are splitter artifacts (fragment lines with no terminal period joined to the next line) or quoted text (Anthropic's definition). The slide-24 flight card block is code-like and untouched apart from two due dates.

## Unsure

- "Source: Claude Code docs, ... checked 09/24/2026" and "Sources checked 09/24/2026" kept as source access dates (CUT-BRIEF protects citation dates; BRIEF calls "checked" dates QA asides).
- Flight card "SPRINT (due Wed 10/14)" became "SPRINT" padded to the column; "Go" left as written.
