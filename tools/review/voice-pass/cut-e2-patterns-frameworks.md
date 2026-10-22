# Cut-section voice pass: e1-agent-loop, e2-patterns-frameworks, e3-tools-as-contracts (Oct 22, 2026)

Chain run: humaniser, ste-voice, scholarly-voice, humaniser battery (check only). Keys, first lines, "- " line structure, and " / " separator counts verified unchanged against a backup copy by script; all three files load as JSON.

## Counts

- e1-agent-loop.json: 14 edits across 11 slide values
- e2-patterns-frameworks.json: 15 edits across 11 slide values
- e3-tools-as-contracts.json: 16 edits across 10 slide values
- Total: 45 edits. Em dashes removed: 30 (all outside bracketed notes). "names/named" as verb or modifier removed: 4. Schedule fragments removed: 12 (dates, "4:00–5:00 · CC209", "Go at 5:46", "tonight", "this week", "next week", "before class", "Consultation at five").

## Dominant patterns, with before/after pairs

1. Antithesis and epigram closers (#36, "not X. It is Y."), the largest group (about 14).
   - Before: "Autonomy without a stop condition is not a feature. It is an open account with the model provider..."
     After: "An agent loop with no stop condition keeps spending on the model provider's account, and it leaves open who is responsible for what the agent did."
   - Before: "If you cannot explain what the framework did on turn three, you do not own the loop; it owns you."
     After: "If you cannot explain what the framework did on turn three, you cannot defend the loop's behavior in Drift."
   - Before: "A blanket 'yes' that any later write can spend is not a confirmation; it is a disabled gate."
     After: "A blanket 'yes' that any later write can spend disables the gate."
2. Actor removal (#3, #31, STE rule 2). "ReAct was built to show" became "ReAct's authors built it to show"; "The model's every output ... is validated" became "Pydantic AI validates every model output"; "Practitioners hit the abstraction tax" became "Developers who used it paid the abstraction tax".
3. Invented authority (#37). Removed "Most production 'agents' are workflows"; "the demo everybody saw"; "the field's first shared failure record" (kept the record, dropped "first"); "Every 2024–25 design ... is a reply to this spring" became "The 2024–25 designs this course covers ... each answer a failure from that spring"; "Every failure mode of the contract shows up in the first ten turns" became "Expect these failures within the first ten turns."
4. "the claim" / "we": "the claim is false" became "the design claim is false"; "the first structure we put around it ... unless we design them out" rewritten with "a designer" and "the design" as actors; "when will we know" became "when the evidence will arrive".
5. Definition-colon ledes (#35): "Chain-of-thought is planning without commitment: ..." and "The abstraction tax: every layer ..." rewritten with a working verb first; the term is stipulated in the next sentence ("This course calls that cost the abstraction tax").

## Self-audit artifacts (after final pass)

Closer list (last sentence of each changed paragraph, out of context): "...the design claim is false." / "...an agent's next reasoning step depends on what the environment returned." / "Later Evolutions add each one." / "...so the Chase can tell a correct halt from an exit that left no record." / "Because nothing grounded the plans, each new plan read well while the task made no progress." / "...after two more years of the same failure." / "...so the ledger and the gates sit inside the loop." / "ADRs exist to prevent that post-hoc rationalization." / "...Sortie 2 fails, and the ADR stands as a rationalization of a choice already made." / "An ADR written after the code is post-hoc rationalization." / "A loop that swallows an error removes the evidence of that failure." / "For this reason a hook enforces a rule, where a prompt only states one." / "gzkit, the reference design, met that gap in August (next slide)." Check result: no shared cadence; none restates its paragraph. "where a prompt only states one" keeps a two-sided contrast; kept because the partition (hook vs. prompt) is real and both sides carry content (scholarly-voice rule 8).

Lede list (first line after the "Cut from" header): slide titles and labelled fragments ("Evolution 1 · Lecture", "Halt conditions, budgets, ...", "Teardown: the vendor SDKs (2025), and who owns the loop", "Flight Card N brief (Sortie N): ..."). No "X is Y: a, b, c" lede remains in prose; the "Theory of control:" and "Cost:" labels are slide fields, kept as labels.

Claim list (frequency words): "every" occurs only in rules and specifications ("every turn is in the ledger", "Give every tool a timeout"), not as frequency claims. "small local models fail the schema more often (E3 shows this)": comparative, demonstrated in E3's sortie; kept. "Frameworks change monthly" / "These SDKs change monthly": kept from source as the lecture's stated premise; flagged for Jeffry. "hundreds of thousands of GitHub stars in weeks": a fact from the original, not edited.

## Greps (final)

Em dash: only inside the bracketed notes "[Quote from genesis.md — verify ...]", "[Summarized from the ADR's title ... — verify ...]", which CUT-BRIEF says stay as they are (the build drops them). "names": only the noun ("field names", "current names", "alternatives as names"). "claim": only "design claim" / "DESIGN CLAIM". "before class": only inside bracketed notes. AI-vocabulary, intensifier, summary, hedge-stack, and "not X, but" greps: no hits.

## ste_check lines declined

- Sentences over 25 words (20 total): all in explanatory slide paragraphs or flight-card specification text; each carries a list or a condition that would lose precision if split. Longest: e1 slide 10, 71 words ("The operator's remedy changed the documents around the model call ... is an event."), kept because it carries the four-item document list that the original carried; e3 slide 7 Gorilla/ToolBench (31) and "Two lessons carry forward" (38) kept for the same reason.
- Noun clusters of 4+ (39): false positives on flight-card field lists, " · " separated fragments, and clause boundaries ("model never calls your function").
- Passives without actor: "was started" (gzkit): the original gives no founder name, so none was invented. "can then be attributed", "cannot be known", "was amended", "is recorded", "are learned", "was removed": the actor is the student or is irrelevant to the rule; kept.
- Gerund/nominalized subjects: "Function calling", "Type validation", "The enforcement matrix", "The founding exchange" are proper technical terms, not nominalized verbs.
- Semicolons (68): nearly all are in labelled fragments, table rows, and flight-card text carried from the original; slide register, left.

## Unsure

- e2 slide 3: removed "Most production 'agents' are workflows and should be" as unsourced. If Jeffry is drawing on Anthropic's "Building effective agents" (2024), he may want a sourced version back.
- e3 slide 12: "Consultation at five:" read as schedule; rewritten "Bring your Sortie 2 verdicts to consultation, and state which tool you will gate first." Consultation itself may count as a schedule item.
- e1 slide 10: "That is ADR-1, next week" became "(that is ADR-1, in Evolution 2)".
