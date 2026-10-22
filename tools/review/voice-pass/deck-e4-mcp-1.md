# Voice pass log: deck e4-mcp-1 (E4, MCP I: Building a Server)

Date: 2026-10-22. Chain: humaniser, ste-voice, scholarly-voice, humaniser battery (check only).

## Counts

- Slide wording (`/home/claude/site/tools/sitekit/voice/e4-mcp-1.json`): 19 values changed of 209 keys. Keys untouched; both files valid JSON; cut sections and timing marks in the notes untouched.
- Speaker notes (`/home/claude/site/tools/review/voice-pass/notes/e4-mcp-1.json`): all 13 lecture paragraphs rewritten (slide 11, the lens, got the lightest touch: sentence openers and one banned verb).

## Patterns that dominated

1. Session-running language in the lecture prose ("Last week", "This week", "next week", "tonight", "this summer", "this term", "before class", "Consultation at five", minutes per section). Replaced with Evolution numbers or dropped.
   - Before: "Tools are model-controlled and are last week's contract on the wire." After: "Tools are model-controlled; a tool is the E3 contract put on the wire."
   - Before: "Ten on framing, twenty on the spine because the build is a server and the wire changed this summer, ..." After: "The lecture has five parts: the framing; the spine, the longest part because the build is a server and the July revision changed the wire; ..."
2. "claim" / "the move" framing.
   - Slide: "Tonight's claim, which Sortie 4 will try to disprove" became "The statement Sortie 4 will try to disprove". Notes: "The claim for the sortie:" became "The design claim for the sortie is that ..." (course vocabulary).
   - "The four moves of the lab" became "The four steps of the lab"; "MCP's move was to make the boundary the thing that is specified" became "MCP specified the boundary between host and server, which neither predecessor had specified."
3. Antithesis closers and "not X, Y" chips.
   - "Negotiated, not assumed." became "Negotiated on every request."
   - "Prerequisites, not presence. A server above the core adds a way in, not a dependency." became "The doctrine forbids prerequisites and allows presence. A server above the core adds a way in without adding a dependency."
   - "The wire carries requests, not permissions." became "The wire carries requests; the host grants permission, and permission never travels." (slide and notes)
   - "Ask for input by returning, not by calling." (notes) dropped; the mechanism sentence before it already states it. Slide row: "The server asks the human by returning a result instead of calling back; ..."
4. Invented authority (#37): "The falsifier students underrate" became "One of the falsifiers is asymmetric"; "most tutorials online still teach roots and sampling" became "tutorials written before that revision still teach roots and sampling".
5. "names" as a verb/modifier: "names what changed" (twice) became "states what changed"; "the registry named as a supply chain" became "a registry without provenance counts as a supply chain"; slide "a named workflow" became "a workflow with a name and arguments".
6. Em dashes in three table cells (code label, description) replaced with a colon; code inside backticks untouched.
7. Actor removal (STE rule 2): fragment openers ("The architecture in one column...", "The server itself, in the shape...", "Card four, center of the envelope...") given a subject (the slide, Flight Card 4); passives without actor given one ("was deprecated" became "its vendor deprecated it"; "is how a refusal is held honestly" became "the review held the refusal the honest way").
8. Rhetorical question on slide 3 ("Works from the harness but not the script?") became a conditional sentence.
9. "we" (two instances) removed; "ecosystem" (AI-vocabulary grep) removed from the slide heading and the notes ("What a healthy protocol needs around it").
10. QA aside in the source footer ("Verify the lab's Python SDK version against this table before class") became a student instruction ("Check the Python SDK version you pinned against this table before you build"); the citation text is unchanged.

## Self-audit artifacts (notes, after the final pass)

Lede list (first sentence per slide):
1. Evolution 4.
2. The lecture has five parts: the framing; the spine, the longest part because the build is a server and the July revision changed the wire; three teardowns that end at the foundation; the reference design's refusal and the project that reverses it one tier up; and the evaluation lens with the flight card.
3. Framing.
4. The slide puts the architecture in one column and the primitives in the rest.
5. The revision that went to general availability on July 28 rewrote the wire, and the headline change is statelessness: there is no handshake and no session header, and every request carries its version and capabilities in its metadata.
6. This slide shows the server itself, in the shape the Python SDK gives you.
7. Two teardowns follow, both from before the protocol.
8. The third teardown reads MCP itself as a system, on the board as a Design Analysis.
9. The reference design refused the protocol this Evolution teaches, and the refusal is what this slide teaches.
10. This slide lays out the project that reverses the refusal one tier up, by primitive, so that the three kinds of control are visible.
11. A weak Sortie 4 shows one harness pretending to be two clients, a client silently repairing arguments, a log that is a narrative, a write tool on the wire with no gate, and a server built on a deprecated feature because the tutorial was from 2025.
12. Flight Card 4 sits at the center of the envelope and depends on Sortie 3, because the write gate must already hold before anything goes on the wire.
13. Close.

No repeated opening; no "X is Y: a, b, c" lede (slide 2's colon introduces a five-part enumeration that the deck discharges in order, Lee rule 1; slide 5's colon introduces the stipulation of "statelessness").

Closer list (last sentence per slide):
1. The revision of the specification that went to general availability on July 28 changed the wire in ways your SDK may or may not already reflect, so the lecture teaches the current revision and states what changed.
2. (single-sentence paragraph; same as lede)
3. One of the falsifiers is asymmetric: a tool that works from the harness and fails from the script means the harness was compensating for the protocol, and the sortie has measured the compensation.
4. A new server should not adopt a feature the specification has scheduled for removal.
5. Check which revision your pinned Python SDK speaks before you build, because the SDKs shipped on the day of the revision and a version pinned earlier may not have it.
6. The description is all the model sees, so write it as a contract; in E5 you will read tool descriptions that an adversary wrote.
7. MCP specified the boundary between host and server, which neither predecessor had specified.
8. Two more cards follow: what a protocol needs around it, where a registry without provenance counts as a supply chain, and the analysis in the template's five fields.
9. If gz validate fails, the server became a prerequisite and the doctrine no longer holds.
10. The strip holds the exercise from chapter 13, and the exercise is also the first instrument this course has given you against summary laundering: you can now diff the model's answer to 'what is attested?' against the resource the model was handed.
11. An exceptional Sortie 4 adds a third client with a divergence explained, a deliberately wrong schema that the server rejects, cache fields honored, the governance server with the attestation diff, and a debrief that states what the protocol forced you to write.
12. Record the revision on the SUBSTRATE line so that the Chase can tell the two apart.
13. Bring to the consultation your Sortie 3 verdicts and the name of the first tool you will serve.

None would work as a caption or moral out of context; each carries a rule, a condition, or a pointer stated with its reason.

Claim list (frequency or consensus statements):
- "tutorials written before that revision still teach roots and sampling" (slide 4): a statement about the content of pre-revision tutorials, which could not teach a revision that did not exist; no frequency word remains ("most tutorials online" removed).
- "every host still wrote its own loader, so the combinatorial cost did not change" (slide 7): the N×M premise of the deck, sourced to the slide 3 argument and the function-calling teardown on slide 7.
- No other "most", "usually", "often", or "every term" sentence remains.

## Grep battery (final)

Scholarly-voice greps (intensifiers, AI vocabulary, em dashes, summary openers, hedge stacks, "names", not-but cadence) return nothing on the edited notes prose and nothing on the slide values. Session-running greps ("tonight", "this week", "last week", "next week", "the move", "we ", "before class") return nothing in the lecture prose.

## ste_check lines declined

Rules 1 to 4 only apply to explanatory paragraphs (BRIEF.md), so the length lines (30 sentences over 25 words) and paragraph-count lines (5 paragraphs over 6 sentences) were read and not obeyed; each paragraph keeps at least one short pivot sentence. The gerund/nominalization heuristic flagged eight sentences, all with plain nouns as subjects (revision, specification, description, question, reference design); declined. "Function calling" is the product term and stays. Passive heuristic: "A kit whose job is to be trusted" (the point is that others trust it; actor is the user of the kit, left implicit on purpose), "'what is attested?'" (quoted prompt name), "the resource the model was handed" (the host hands it; stated two sentences earlier). Noun-cluster lines were all phrase-boundary false positives ("last fifty ledger events" is a count plus a two-word noun).

## Left as is, with reason

- Slide 13 title "A protocol is a contract that strangers can discover." is the deck's stipulated definition of a protocol, repeated in the notes with its reason attached; it is a definition, not a moral.
- Chip "Application-controlled. Content, not instructions (E5)." states a real partition (the E5 rule for resources) in a chip of fixed width; a longer form did not fit.
- Chip "User-controlled. The human picks; the server proposes." states two actors' roles, both load-bearing.
- Slide subtitle "Description without negotiation: why the pre-protocol attempts stalled" is a label of the section's question, in the form Lee uses for headings.
- Slide 2's run-of-show rows and all timing keys left unchanged (dropped by the build); only the title "Sixty minutes, five moves" was reworded to "five parts" in case it survives.
- Flight card lines (slide 12) left as written: the design claim text is course vocabulary.
- The quoted doctrine sentence and the campaign-review quotation left exactly as quoted.
- Notes slide 2 dropped the minute counts (schedule detail the brief excludes); the five-part order is preserved.
