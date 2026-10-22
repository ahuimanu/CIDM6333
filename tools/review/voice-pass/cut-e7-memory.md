# Cut pass log: e7-memory.json (Oct 22, 2026)

File: /home/claude/site/tools/review/voice-pass/cut/e7-memory.json. Keys, first lines, line counts, and " / " counts unchanged (checked by script against a backup). JSON valid.

## Counts

- 45 edits across 25 of 29 slides.
- Em dashes removed: 1 (slide 26). None remain.
- "names/named/naming" removed: 10 (slides 4, 9, 11, 13, 14, 22, 25 x2, 27; plus imperative "Name" x2 on slides 4 and 27).
- Schedule fragments removed: 13 (dates, clock times, CC209, "tonight" x2, "next week", "checked 09/24/2026", lab minute markers 0–3 ... 28–30, "by Friday night").
- Epigram or antithesis closers rewritten: 12.
- "we" removed: 1 (slide 21).

## Dominant patterns, with before/after

Epigram closers (#36):
- "A record without provenance is a rumor the agent repeats." -> "No reader can check a record without provenance, and the agent still repeats it as fact."
- "A memory you can replace is a memory you can correct; weights you cannot." -> "You can correct a store by replacing its records, and you cannot correct a fact inside model weights in the same way."
- "Memory makes one injection permanent." -> "Because the memory persisted, one injection reached every later chat."

Not-X-but-Y closers:
- "a vector database is a scaling decision, not a memory decision." -> "the need for a vector database depends on scale, and the memory design does not require one."
- "That is data for the flight log, not a reason to change models mid-sortie." -> "Record the wrong answers in the flight log, and keep the same model for the whole sortie."

Actor removal / passive judgment (#3, #31):
- "it will be read as fact on every turn after" -> "the model reads it as fact on every later turn"
- "Deleting the source does not delete the memory." -> "A user who deletes the source does not delete the memory."

Unsourced frequency claim:
- "Most course systems need episodic memory ..." -> "Plan for episodic memory ... unless your system needs another kind."

Procedure (STE): lab steps split into one instruction per sentence, semicolons removed.

## Self-audit

Closer list (last sentence of each line, read out of context): no remaining epigram, antithesis moral, or pseudo-cleft. Kept as factual: "OpenAI closed the exfiltration channel; the memory write itself stayed possible." "Klaus picks a research partner from his reflections rather than from the count of his meetings." (paper's result).

Claim check: "A memory is a claim with a source" and "A memory record is a claim with a source" kept (claim/receipt sense, not a thesis stand-in). "fails the Sortie 7 claim by design" kept (flight card's claim). Frequency words: only universal rules ("every record", "every write"); no "most/usually/often" remain.

Grep battery: all seven scholarly-voice greps return nothing.

## ste_check lines declined

35 "over 25 words" hits. Nearly all are artifacts of extraction: slide fragments and list lines without terminal punctuation join into one "sentence", and title lines (slide 1, slide 21 judgment loop, slide 25 scorecard) are " · "/" / "-separated lists. Explanatory sentences left at 26 to 30 words (slide 3 falsifier sentence, slide 19 Reflexion figures) keep a condition or figure that a split would separate from its result.

## Judgment calls

- "on December 15" (slide 15 question) -> "at the end of the course" (schedule date). "course end (12/15)" in the retain_until rule (slide 11) kept, since it is the retention parameter.
- "Run 09/24/2026 on two synthetic logs" (slide 8) kept: it dates the data, not the schedule.
- Lab minute markers ("0–3", "3–8", ...) treated as lab timing and removed; step order carries the sequence.
