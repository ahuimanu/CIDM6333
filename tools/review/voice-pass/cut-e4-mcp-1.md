# Cut-section pass: e4-mcp-1 (Oct 22, 2026)

File: cut/e4-mcp-1.json. 26 edits across 11 of 12 values. Keys, first lines, "- " line structure, and " / " separator counts unchanged (checked by script against a pre-edit copy). JSON valid.

## Counts
- Em dashes removed: 10 (heading, Flight Card title, slide 9 closer, six timeline entries turned to "Mon YYYY:"). Remaining: 0.
- "named" as modifier: 1 ("a named workflow" -> "a workflow with a title and arguments").
- Schedule fragments removed: 6 ("Thu 09/24", "4:00–5:00 · CC209", "tonight" -> "in this Evolution", "next week we will see" -> "E5 shows", "Go at 5:46", "Consultation at five" -> "Bring to consultation", "before class" on the SDK check).
- "we": 1 removed. "the claim" thesis stand-ins: none present.

## Dominant patterns
1. Antithesis / epigram closers (#36, "not X" cadence).
   - "a mismatch is an error, not a guess." -> "a mismatch produces an error that neither side resolves by guessing."
   - "The wire carries requests, not permissions." -> "The wire carries requests only, and no message on it grants permission."
   - "Each host still wrote its own loader: N×M by another name." -> "Each host still wrote its own loader, so the N×M adapter count remained."
   - "The refusal is about prerequisites, not about presence." -> "The refusal covers prerequisites only."
   - "the server has just given you the instrument to catch it." -> "a diff of the answer against the attestation resource catches it."
2. Actor removal (#3/#31, STE rule 2).
   - "Governance is delegated to the host by design, which is why E5 is about..." -> "The protocol's designers delegated governance to the host, and E5 examines..."
   - "Deprecated within a year in favor of GPTs and Actions." -> "OpenAI deprecated plugins within a year in favor of GPTs and Actions."
   - "nothing to remember between calls" -> "because the server keeps no state between calls"
3. Procedure register (STE): slide 6 steps split at semicolons ("Open the inspector. Confirm that..."), step 4's fragment list became "Confirm two entries for the two calls, with the same tool, arguments, and result."

## Closer list check
All value-line closers extracted out of context. No line reads as a moral or slogan after the pass. Kept as is: "Where it puts the human: outside the wire." (field of a decision record, not a landing), "Theory of control: ... no party owns the boundary between hosts." (labelled field).

## Lede list
Value first lines are fixed ("Cut from slide N"). Slide ledes: no definition-colon openings added; "Hosts, clients, servers, and the three server primitives" is a label.

## Claim list
No frequency claims. "Many teams generated those schemas from OpenAPI documents" (slide 7) is unsourced; left because it is a historical description of 2023 practice, flagged for the instructor.

## ste_check declined
Sentence-length and paragraph-length flags are artifacts: the checker joins slide lines with no terminal period into one sentence. Passives "is deprecated" (actor: the spec revision, stated in the same slide), "is attested", "be trusted", "is broken", "is misplaced" are declined as idiomatic states with the actor in context. "Transport independence" flagged as nominalized subject: it is a labelled term, kept.
