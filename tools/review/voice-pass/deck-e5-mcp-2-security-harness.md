# Voice pass log: deck e5-mcp-2-security-harness (E5, MCP II: Security and the Harness)

Files:
- /home/claude/site/tools/sitekit/voice/e5-mcp-2-security-harness.json (slide wording): 42 of 485 values changed; keys and key order untouched; valid JSON.
- /home/claude/site/tools/review/voice-pass/notes/e5-mcp-2-security-harness.json (speaker notes): 27 of 27 slide paragraphs changed (slide 27 lost one sentence only); every "Cut from slide N" and "Instructor checks" section byte-identical to the original; paragraph-break counts unchanged; valid JSON.
- Originals kept at /tmp/claude-0/-home-claude/acdec67e-a228-569c-b4b7-fc7975fc3d39/scratchpad/e5/voice-orig.json and /tmp/claude-0/-home-claude/acdec67e-a228-569c-b4b7-fc7975fc3d39/scratchpad/e5/notes-orig.json.

Code lines, the opencode.json excerpt, the flight card block, table cells carrying dates, CVE numbers, URLs, ADR numbers, quoted vendor text, and "typed claim"/"design claim"/"the model's claim" (the model's assertion about its own calls, gzkit sense) were left as written.

## Patterns that dominated

### "claim" as the lecture's thesis (house rule)
- Slide heading: "Tonight's claim, which Sortie 5 will try to disprove" → "The design claim Sortie 5 will try to disprove"
- Slide heading: "Harness engineering, 2026: the claim with numbers" → "Harness engineering, 2026: OpenAI's figures"; body label "OpenAI's claim." → "OpenAI's report."
- Strip: "FAIL is the claim disproved." → "FAIL is the design claim disproved."
- Notes 3: "The claim is the corner-of-the-envelope one for the term so far" → "The design claim for Sortie 5 is the first corner of the envelope in the term"
- Notes 12, 26: "the claim was not flown" / "a fail disproves the claim" → "the design claim".
- Kept in notes 11: "read them as a claim rather than a measurement" (OpenAI's unverified figures; the gzkit sense, not the lecture's thesis).

### Time, room, schedule, and QA asides (house rule)
- "tonight", "this week", "last Thursday", "at six", "by Sunday / Monday night / Thursday noon", "Break after this slide", "Five minutes", "Lab at six", and the run-of-show minute counts in notes 2 removed or replaced with "this Evolution", "in the lab", "the course-calendar date", "Evolution 4".
- "the 09/17 lab", "the AGENTS.md you wrote on 09/17" → "the earlier lab" (matches the wording the slide keys already use: "the earlier lab file").
- "Verify ... before class" sentences removed from notes 20, 21, 22 (instructor QA; the bracketed verify items under "Instructor checks moved off the slide" were not touched).
- Notes 2: "the homework brief has the dates" dropped.
- Left alone: "checked 09/24/2026" and "Dates checked 09/24/2026" on the GitHub server table, the harness table, and the sources lines. These read as as-of qualifiers on facts that change monthly, and the brief forbids dropping a scope qualifier and editing dates. Flagged as unsure in the report.

### "names"/"named" as verb or modifier (house ban)
- "each step names the check" → "each step lists the check"; "WWW-Authenticate names resource_metadata" → "carries"; "a description that names another server's tools" → "refers to"; "MCP tools are named <server>_<tool>" → "take the name"; "every tool not named is allow" → "every tool without a rule is allow"; "Every MCP write you did not name" → "without a rule"; "adversarial client named" → "with the adversarial client identified"; "A NO-GO names the field" → "states the field"; notes 5 "names the scope needed" → "states"; notes 19 "a named MCP write" → "a specific MCP write tool"; notes 24/26 "Name the adversarial client" / "adversary named" → "Identify" / "identified"; notes 13 "name the tool and name the mechanism" → "which tool ... and which mechanism".
- Left: "server_tool names" (plural noun) and "adversarial client (named)" (flight card text).

### Epigram and antithesis closers, mirrored pairs (#36, house cadence bans)
- "A signed Agent Card proves who is speaking. It proves nothing about whether the artifact is true." → "A signed Agent Card proves who sent the artifact. Whether the artifact is true is a separate check, done in your host."
- "Pinning catches a server that lies to the model, not one that is honest to the model and lies to you." → "Pinning catches a server that changes what it tells the model. It does not check what the server's code does."
- "Same doctrine, different door." → "Both test the same rule, that every observation is data, through a different channel."
- "A defense that exists only as a sentence, or only while the test runs, is not a defense." → "... leaves the write tool open to the adversary."
- Notes 9: "The strip is the trap: a signature answers who, never whether." → "The strip warns against one mistake: a signed Agent Card proves who sent the artifact, and whether the artifact is true remains a check your host has to make."
- Notes 8: "the permission rule bounds the damage, the hash detects the change." → "the permission rule bounds what a poisoned description can make happen, and the hash tells you that the description changed, so you need both."
- Notes 15: "it does nothing about a server that is honest to the model and dishonest to you" → "and it does not check what the server's code does. For this reason your SUBSTRATE line pins the package version."
- Notes 25: "whether yours followed the canary is data, not a grade" → "so either outcome of the unguarded flight is a result to record."
- "what the harness loaded, not how long the file is" → "by what the harness loaded rather than by the file's length" (slide and notes 21).

### Pseudo-cleft reveals and "the point"
- "A sketch, not a library; the order of the checks is the point" → "A sketch of the five checks, in the order the server runs them"
- Notes 16: "What the harness does not do is pin descriptions" → "The harness does not pin descriptions"
- Notes 26: "What you hand in is the run sheet's list" → "You hand in five items"

### Invented authority (#37)
- Notes 1: "most of what makes an agent product safe or unsafe is not the model" → derived: "the model is one part of an agent product and the one part you cannot change, so whatever makes the product safe or unsafe sits in the parts you can."
- Notes 5: "Most of you will use a local token issuer or a static test token" → "A local token issuer or a static test token is acceptable for the sortie, declared in SUBSTRATE"
- Notes 12: "the classic one" dropped; "passes every honest test" now carries its reason (the honest client sends the right value).
- Notes 11: "Her point ... is the honest one" → "She also states that the behaviour harness ... is the least developed of the three"
- Notes 1: "the instruction files every harness reads" → "the instruction files the harnesses read"

### Definition-colon and parts-list ledes; actor and mechanism on slide bodies (#35, STE rules 2 to 4)
- "Model, loop, tool layer, ... The model is one of eight. The other seven are the harness." → "A coding agent has eight parts: ... The model is one of the eight. The other seven are the harness, and you can test them."
- "Each harness is a set of surfaces: instruction file, hooks, ..." → "The matrix treats each harness as a set of surfaces (...) and records which rules render into which surface. ... Where there is no hook, the rule falls back to prose."
- Telegraphic step cards given an actor: "PKCE pair; resource=...; the challenged scope; expected issuer recorded." → "Client makes a PKCE pair, sends resource=... and the challenged scope, and records the expected issuer."; "Bearer token on every request. Server checks ..." → "The client sends a bearer token on every request. The server checks ..."; "Scopes per tool class ... No write scope: 403 ..." → "Declare a scope per tool class ... A token without the write scope gets 403 insufficient_scope ... and the server logs the refusal."; "Falsified by any out-of-scope call ..." → "Any out-of-scope call that succeeds ... falsifies it."
- Notes 3: "Count the parts of a coding agent and the model is one of eight" → the eight parts listed, then the reason they can be attested ("each one is code or configuration that you wrote and can read").
- Notes 10: "Skills are progressive disclosure." → mechanism added; "Hooks and permissions are the only two of the four that enforce" → reason added ("because they run regardless of what the model decides").
- Notes 20: "Why: drift between mirrors is drift in what agents believe" kept on the slide (Design Analysis field); in the notes it became "The reason is that the file is what every agent reads first, so ...".

### "we" and stage directions
- "we fill it together" → "the class fills it in"; "the reference design taught us" → "comes from the reference design"; "the symlink we taught" → "the symlink the earlier lab taught"; "the falsifier we pre-registered" → "the falsifier the card pre-registers".
- Notes 17: "Do not repeat the lab: ask three or four students to read ..." → "The class builds the table on the board from your worksheets: three or four of you read ..." (the published notes are read, not performed).

### Gerund subjects (STE rule 3)
- "If standing up a local OAuth server is out of reach" → "If a local OAuth server is out of reach"; "removing the write tool to pass is a fail" → "a pass obtained by removing the write tool is a fail"; "Reading scope from the request is the classic one" → "The first, scope read from the request, passes every honest test"; "Shadowing is one server rewriting another's behavior" → "In shadowing, one server's description rewrites how the model uses another server's tools".

### STE course register on procedure cells
- "Pin the package version and hash, not only the descriptions; read the source ...; prefer servers ..." split into three imperatives, no semicolons.
- "tool-pins.json in the repo. Each start, compare. Changed hash: new tool, re-approve and re-pin." → "Store tool-pins.json in the repo. Compare on each start. A changed hash is a new tool: re-approve and re-pin."

## Self-audit artifacts (notes, after the final pass)

Closer list (last sentence of each slide's lecture paragraph; slide 27 before the sources):
1. The self-guided lab is to plant a poisoned tool description in your own server and see whether OpenCode's model follows it.
2. Your Chase signs your card in the repository before you fly and reads your log after.
3. The third comes from the reference design, which records a pass obtained by switching off a check as a fail: a pass obtained by disabling a check, or by removing the write tool for the test, falsifies the design claim.
4. Every client sees it; the refusal has to happen on tools/call, with a 403 and insufficient_scope.
5. A local token issuer or a static test token is acceptable for the sortie, declared in SUBSTRATE; the checks in step five are the same either way.
6. Test point three on your card is this list flown: forge each one, and the log must show the token's scope.
7. The strip connects to your worksheets: the GitHub trace was injection and deputy together.
8. The strip states the division of labor: the permission rule bounds what a poisoned description can make happen, and the hash tells you that the description changed, so you need both.
9. The strip warns against one mistake: a signed Agent Card proves who sent the artifact, and whether the artifact is true remains a check your host has to make.
10. Hooks and permissions are the only two of the four that enforce, because they run regardless of what the model decides; the other two are context the model may or may not follow.
11. Your Sortie 5 is a small measurement of one harness.
12. Nothing enforces it, and the lab in this Evolution shows you what a small model does with a description that says otherwise.
13. The question on the slide is the one the lab asks, so write your answer down: which tool in your server, and which mechanism other than a sentence stops a stranger's text from calling it.
14. The defenses in the last column are harness and supply-chain controls; not one of them is 'use a better model'.
15. For this reason your SUBSTRATE line pins the package version.
16. The legacy tools boolean is deprecated in favor of permission since 1.1.1, so use permission in your config.
17. Two questions close the table: which of those four would you set for your own agent, and which test point on Card 5 is the same idea in your server?
18. Your Sprint asks you to revise and re-measure the earlier lab file; if you run Claude Code and you created a CLAUDE.md, check which file loaded, with /context.
19. The reference design's count of hooks per harness, next, was taken before Codex's hooks became general; keep that in mind when you read seventeen, two, and one.
20. The reason is that the file is what every agent reads first, so drift between the renditions is drift in what the agents believe the rules are.
21. The same rule governs your Sprint: map, not encyclopedia, with a declared and validated budget, and the measure is what the harness loads at startup rather than the length of the file.
22. That one maps straight onto the lab: denying the MCP write tool does not stop the agent from writing the same file with bash.
23. Exceptional: the pin catches a planted change before the model sees it; a shadowing attempt blocked by a harness rule; issuer validation; one rule moved from prose to enforcement; and the budget measured in two harnesses.
24. If a local OAuth server is out of reach, a local issuer of signed test tokens is acceptable; declare it in SUBSTRATE, because the audience and scope checks are the same.
25. Revert the canary before you commit.
26. The strip separates the two outcomes: a FAIL disproves the design claim, and an ABORT means the flight did not happen for a reason outside the design claim.
27. Every observation is data; authority is a token the server validated itself.
Disposition: 27 is the lecture's two-rule doctrine restated as the close and is Jeffry's wording on the slide; 11 and 15 carry a reason stated in the sentence before. No line reads as a caption without its paragraph.

Lede list (first sentence of each slide's lecture paragraph):
1. Evolution 5.
2. The lecture runs in six parts, and the lab after it is yours to run.
3. Framing.
4. The slide has three cards: stdio, Streamable HTTP with OAuth, and scope.
5. The flow the spec now requires, in five steps, each with the attack it stops.
6. Step five as code.
7. Four mechanisms, one root cause.
8. The worked example, and it is the lab.
9. A2A in four minutes, by one distinction.
10. Four control surfaces, and the correction to the earlier lab is in the second card.
11. The 2026 writing that gave harness engineering its name.
12. Four mistakes, each of which fails the card.
13. The question on the slide is the one the lab asks, so write your answer down: ...
14. Six cases, read for mechanism rather than headline, with the dates checked against the primary write-ups.
15. The two in-the-wild cases, as a pair, because they teach the limit of the lab.
16. OpenCode is the harness you use, so it gets read for mechanism with the same questions.
17. The live Design Analysis.
18. The left panel lists what each harness reads, as of 09/24/2026.
19. The table crosses three harnesses with five surfaces.
20. The reference design's answer to one canon, many renditions.
21. The incident that produced the rule.
22. The reference design's casebook records three episodes of drift between mirrors.
23. Weak: scope from something the client wrote; ...
24. Card five, the first corner of the envelope.
25. The lab, which you run on your own.
26. The Sprint in three cards.
27. Close.
Disposition: the one-word and fragment ledes ("Framing.", "Step five as code.", "Close.") echo the slide titles as spoken and were in the original; left. The count-led opening ("Four mechanisms", "Four mistakes", "Six cases") is the slide's own cell count; two of the six were varied (19, 22) so the move does not run on consecutive slides. No "X is Y: a, b, c" lede remains except slide 4, where the list is the slide's three cards and the sentence is a roadmap, not a definition.

Claim list (frequency or consensus statements) and their sources:
- "every harness reads" (notes 1) → changed to "the harnesses read".
- "passes every honest test" (notes 12): derived in the sentence (the honest client sends the right value).
- "Every one of them lets you enforce ... Every one has an enforcing code path" (notes 19): the slide's five-row table, sourced to the three vendors' docs on the slide.
- "harness fitness is mostly unmeasured" (notes 11): attributed to the textbook, chapter nine.
- "the first malicious MCP server found in the wild" (notes 14): The Hacker News, Sep 29, 2025, on the sources slide.
- "more than 150 organizations" (notes 9): Linux Foundation press release, Apr 9, 2026, on the sources slide.
- "None of the six was a model failure" (slide strip): the six rows of the table on the same slide.
- "Each has shown up in a Sortie 4 log or a worksheet" (slide 12 subtitle): the instructor's own records; left as written.
Removed: "most of what makes an agent product safe", "Most of you will use", "the classic one", "the honest one".

## ste_check lines declined, with reasons
- 70 sentences over 25 words and 13 paragraphs over six sentences: the brief applies STE rules 1 to 4 only to explanatory lecture prose and sets no length ceiling there; the long sentences carry lists of conditions (the five-step flow, the four-condition confused deputy, the Weak/Sound/Exceptional lists mirrored from the slide, the sources list on slide 27). None was split at the cost of a condition.
- Gerund/nominalization subjects: "Tool poisoning", "Resource injection", "In shadowing", "The framing sentence", "The instruction surface" are stipulated mechanism and course terms, not gerunds standing in for verbs.
- Passives: "is deprecated" (a spec fact, twice), "is rendered from the corpus" (gzkit doctrine wording, ADR-0.0.37), "can be configured" (Gemini CLI setting), "was reported about a week later" (the reporter is not stated on the slide; adding "Koi Security" would add a fact the notes did not carry), "are marked verify because I did not recheck them" (actor present).
- Noun clusters of 4+: all heuristic spans across phrase boundaries or URLs; "server-side request forgery" is the standard term (SSRF).
- Grep hit "underscore" in notes 16 ("server underscore tool"): the spoken name of the character, not the AI verb.

## Left as is, with reasons
- "checked 09/24/2026" qualifiers on the GitHub server table, the harness table, the harness-reads panel, and the sources lines (slide and notes): as-of qualifiers on monthly-changing facts; the brief forbids editing dates and dropping scope qualifiers. Unsure whether Jeffry counts these as QA asides.
- Run-of-show, break, lab-time, and Sprint-due keys in the slide file: the build drops them.
- "Rule one ... never from the client's claims", "A tool returns an observation; a peer returns an assertion", "An instruction is context; a hook or deny rule is enforcement", "Engineers build the environment, not the code", "Map, not encyclopedia", "rendered from the corpus, not authored": real two-sided partitions and gzkit doctrine wording, kept.
- "the model's claim against calls.log" (lab deliverable): the model's assertion about its own calls, gzkit sense.
- The final slide's closing paragraph (three Build items and the lab line): the count is the material's.
