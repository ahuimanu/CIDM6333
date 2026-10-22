# Deck pass log: e3-tools-as-contracts (Oct 22, 2026)

Files:
- /home/claude/site/tools/sitekit/voice/e3-tools-as-contracts.json: 10 of 190 values changed (keys untouched; file valid JSON).
- /home/claude/site/tools/review/voice-pass/notes/e3-tools-as-contracts.json: 12 of 12 lecture paragraphs rewritten; every "Cut from slide N" tail verified byte-identical to the original; timing marks absent in this deck's notes (none to preserve); file valid JSON.

## Patterns that dominated

1. "Tonight's claim" / session asides (BRIEF house rule; humaniser #19/#33 register). Slide: "Tonight's claim, which Sortie 3 will try to disprove" -> "The design claim Sortie 3 will try to disprove". "Why a local 8B model this week" -> "...this Evolution". Notes: "Two weeks ago... last week... This week" -> "In Evolution 1... in Evolution 2... In this Evolution"; the minute-by-minute run of show (slide 2) became the five parts by label; "Consultation at five" -> "The consultation covers..."; "Verify the issue numbers and dates against the changelog before class" (QA aside) deleted.
2. "the move" (BRIEF). Slide 9 subtitle "the move to the commit locus" -> "fences moved to the commit locus".
3. "names" as a verb (BRIEF). "Confirm names tool and arguments" -> "Confirm states tool and arguments"; "A structured error naming the problem" -> "...that states the problem"; notes "a model will happily name a delete tool 'cleanup'" -> "a model will label a delete tool 'cleanup' without hesitation".
4. Compressed parts-list notes -> full sentences with actor and mechanism (STE rules 2 and 3; scholarly-voice course register). Before: "Parse, look up, validate, start with no confirm event, check the class, look for a confirm event bound to this tool and these arguments, deny and record if absent, otherwise record the call and run." After: "The loop parses the model's step, looks the tool up in the registry (an unknown tool halts), validates the arguments against the schema, and checks the side-effect class. For a read it records the call and runs the function. For any other class it searches the ledger for a confirm event bound to this tool and these arguments. If none exists, the loop records a denial, hands the model a DENIED observation, and continues." Before: "Two rows deserve emphasis." After: "Two rows need a reason attached." (the reasons then follow). Before (slide 10): three run-on column dumps of 59 to 68 words. After: each column as three or four sentences with the sortie as subject.
5. Gerund subjects and actorless passives (STE 2, 3). "Exhausting a timeout or a retry budget is a halt" -> "When a timeout or a retry budget runs out, the loop halts." "The local model is required because" -> "The course requires the local model because". "a tool with no class declared is treated as irreversible" -> "the gate treats a tool with no class declared as irreversible".
6. Antithesis closers (BRIEF; #36). Slide 4: "Declared on the tool, not inferred." -> "The tool declares its class; the gate never guesses it from the name." Slide 9: "Presence was verified; procedure was not. Fix: check the record of the procedure, not the output." -> "The gate verified presence and skipped procedure. Fix: check the record of the procedure (the ledger event) rather than the output." Notes slide 3: "not a moral claim, an architectural one" -> "The term is architectural rather than moral: the loop trusts nothing the model sends until the loop's own code has checked it."
7. Invented authority (#37). "breaks the contract often enough" -> "breaks the contract within its first ten turns" (the deck's own stated count).
8. Hidden-mechanism slide line. "A frontier model hides the contract." -> "A frontier model honors the contract, so you never see it enforced." (mechanism from the cut wording).

## Self-audit artifacts (notes, after the final pass)

Closer list (last sentence of each paragraph):
1. The course requires the local model because a small model breaks the contract within its first ten turns, so you watch every clause enforced.
2. The card has four test points in this Evolution, and the fourth is the injected write.
3. The design claim Sortie 3 will try to disprove ends with the phrase the fourth test point depends on: including when the write is requested by text the model read.
4. The strip states the fail-closed rule: the gate treats a tool with no class declared as irreversible.
5. The confirm comes from the human's action in the host (a keypress, a command), never from model output and never from content the model read.
6. A failure the ledger does not show is a failure the Chase cannot read, so a loop that swallows an error has removed its own evidence.
7. A retrieved tool the model has never seen is an untrusted tool, which is the tool-poisoning surface of Evolution 5 arriving two years early.
8. The reference design met that gap in August.
9. Chapter 12's exercise has you implement the gate both ways and show a write that one catches and the other misses.
10. After a denial, the model chooses a read path, and the filesystem hash is identical before and after the denied write.
11. The abort criterion separates infrastructure from the design claim: if the local model cannot produce a parseable tool call in N attempts, the sortie halts rather than fails, and you record N.
12. The consultation covers Sortie 2 verdicts and the tool you will gate first.
Disposition: each carries a rule, a reason, or a pointer; none works as a caption on its own. Closer 6 keeps the slide strip's reasoning (the "so" clause carries the consequence, stated nowhere else in the paragraph).

Lede list (first sentence of each paragraph): "Evolution 3." / "The lecture runs in five parts: ..." / "Framing." / "A tool declaration has four fields." / "The gate fits in fourteen lines of your own loop, which is why it is not a framework feature." / "The table lists six kinds of failure, and the loop handles each with the same shape of policy." / "The slide holds four teardowns, two on each side." / "Computer use (Anthropic, October 2024) shows what generality costs a contract." / "gzkit renders its canon into seventeen Claude Code hooks: ..." / "The lens has three columns." / "Flight Card 3 is the first expansion of the envelope, and it depends on a Sortie 2 PASS." / "Close."
Disposition: no repeated opening; the two colon ledes (slide 2, slide 9) list the parts the paragraph then discharges in order, not a definition by apposition (promise ledger: five parts, then five paragraphs; seventeen hooks by group, then the two incidents).

Claim list (sentences with most/every/never/often/usually): all "every"/"never" sentences state the loop's design rules or the flight card's pass conditions (what the gate does), not frequency claims about people. Two empirical statements remain: "a small model breaks the contract within its first ten turns" and "a frontier model honors the contract so reliably that you never see it enforced". Source: the deck's own slide 3 cut wording ("Every failure mode of the contract shows up in the first ten turns"), which is the instructor's statement and stays.

## ste_check lines declined

- 22 sentences over 25 words: explanatory paragraphs carry no length ceiling under the brief (rules 1 to 4 only). The longest remaining (42, 37, 37, 36 words) each carry a list of steps or conditions (the five loop steps, the two retrieval systems, the six lifecycle events) that would lose precision as fragments.
- 8 paragraphs over 6 sentences: one paragraph per slide; the brief forbids splitting slides.
- Gerund/nominalized subjects: "Function calling" is a proper term; "statement", "harness", "reference design", "consultation" are plain nouns (heuristic false positives).
- Noun clusters: all six spans cross phrase boundaries ("your own gate: gate", "delete tool 'cleanup' without").
- Passives: "the calls are learned", "the governed path was followed", "which rule is enforced where" keep the mechanism in the same sentence; left as is.
- 1 semicolon: "never reaches the function; it returns a structured error" in an explanatory paragraph, allowed.

## Left as is, with reason

- Slide strip "Read freely; write with confirmation; irreversible with attestation. No ledger event, no call.": three items because there are three classes; the compressed form is the slide's layout.
- "Learned calls put the contract in the model; declared calls put it in your loop." and "A hook sees the call, not the effect. A Bash call's write hides in the argument string.": real partitions with the mechanism in the next clause; one each per slide.
- Closing slide "Validate everything that crosses the boundary, gate every effect, and let the ledger say what happened.": three imperatives matching the lecture's three mechanisms (schema, gate, ledger).
- Slide 3 line "The model does not call your function. It emits text that asks for the call.": a real partition that the lecture argues from; kept, with "is yours" made concrete ("runs in your code").
- Unsure: slide 2 notes now omit the minute allocations entirely ("Ten on framing, twenty on the spine..."); the brief treats times as session-running detail, but if the published "Read this lecture" wants the proportions, the original line is in /tmp scratch copy only, not in the file.
