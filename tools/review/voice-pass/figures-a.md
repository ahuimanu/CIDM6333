# Voice pass log: figures-a (Oct 22, 2026)

Files, all under /home/claude/site/docs/figures/: claim-receipt-verdict.html, loop-that-halts.html, memory-is-a-claim.html, n-plus-m.html, one-run-is-an-anecdote.html, pilot-and-planter.html.

Chain run: humaniser (patterns 29 to 40 and the lexical greps), ste-voice (rules 1 to 4 in explanation; full rules in duty lists and step-table cells), scholarly-voice (closers carry a reason; stipulated terms kept), then the humaniser battery as a check on extracted artifacts. About 100 string edits across the six files; 94 source lines changed. Tag counts unchanged in every file (html.parser start-tag census, before and after); every `<script>` still parses (node `new Function`); no em dash remains in any of the six files; SVG geometry untouched; three SVG labels reworded at the same length because they carried the banned "names" verb.

## What changed, by pattern

### Epigram landings and antithesis closers (#36, house cadence bans)
- claim-receipt: "Independence is the property you are buying. Size is not." → "The tier you choose buys independence from the worker's blind spots; the adversary's size has no bearing on that."
- claim-receipt (twice): "If the worker writes its own receipt, you have a claim with a file extension." → "A receipt the worker writes for itself is a claim stored in a file, because the worker chose its contents." (second instance: "does not satisfy the obligation, because the worker chose its contents").
- claim-receipt: "An attestation that an agent writes for a human is not an attestation." → "An agent may not write it on the human's behalf, because the attestation records that a person read the receipts."
- claim-receipt: "A reviewer handed the worker's story checks whether the story is coherent, and a fluent story always is." → "...can check only whether the summary is coherent, and a model's summary is coherent whether or not the tests passed."
- claim-receipt: "Sortie 9 does not ask you to parallelize anything. It asks you to..." (not X. It is Y) → one sentence, action first.
- claim-receipt: "Your route table is the small version." → "applies the same idea at the scale of one sortie."
- one-run: "An evaluator is a system. It needs its own RED witness, or it becomes one more green light." → "An evaluator is itself a system, so it needs its own RED witness; without one it is one more check that passes whatever it sees."
- one-run: "A gate you run by hand when you remember is a report." → reason attached ("because nothing depends on its exit code").
- one-run: "Agreement is the reason judges are used; the biases are the reason they are checked. ... It can hold a gate shut. It cannot stand in for..." (mirrored pair plus antithesis) → two sentences with the mechanism and the citation.
- pilot: "Forgetting is an event, not a gap." → "The ledger line is the evidence that the forgetting happened as an event."
- pilot (simulator note): "It did not test the model. It tested the clock." → "this run tested the clock and never put the model's handling of a conflict to the test."
- pilot: "One rerun is one row on the worksheet, not a finding." → "; it supports no claim beyond that row."
- loop: caption title "A loop without a halt is a bill" (slogan) → "Four states and the exits between them".
- one-run: panel heading "pass@k asks whether it can; pass^k asks whether it will" (mirrored pair) → "pass@k against pass^k"; the paragraph beneath already states both definitions.

### Templated siblings (#38)
Ledes: the originals shared the shape "[one-line thesis]. This figure [draws/follows] X. Step through, then [use the simulator/run the probe] below." Each lede is now written from what its figure shows: claim-receipt opens on what a worker's report proves; loop on where the halt check belongs; memory on the two deck rules and where each becomes a field, a file, or a test; n-plus-m (unchanged) derives the two counts; one-run on why a gate must be able to fail; pilot on two students and three drawers. Step-0 captions ended on the same "Step through..., then [simulator]" line in four files; each now ends on what its own panels add. Shared skeleton kept where the reader looks for the same thing: the test-point map tables, "What the figure leaves out", "Readings".

### Invented authority (#37)
- n-plus-m: "Students tend to underrate the asymmetric falsifier." cut; replaced with "The asymmetric falsifier is the one to plan for."
- memory: "Most course systems need episodic memory plus a small semantic store" cut; ADR-2 sentence kept.
- pilot: a "holds in most runs" claim I had introduced into caption 11 was removed on the check-only rerun (the SVG label and the simulator still say it, as the simulator's stated assumption under "A model of the exercise, not a measurement").

### "names" as verb or modifier (house ban)
loop: "The deck names three absences" → lists; "the PRD names a latency budget" → sets; "If the Step names a tool" → specifies. memory: "It names the record ids" → gives; "The deck names this App. C #4" → files this under; "Named writers" → Listed writers; "Named ids gone" → The evicted ids gone; SVG "A newer record names the one it" → "points to the one it"; "a change names what it supersedes" → "lists what". one-run: "the named diff" (SVG, table, caption) → "the removal diff" (the term the pre-registration bar already uses); "the delta names each regressed id" → lists; "does not name the failed case" → list; "Zheng et al. (2023) name self-enhancement" → identify; SVG "names the / regressed ids" → "lists the". pilot: "names AGENTS.md" (SVG twice, table twice, captions twice, Planter duty) → "cites AGENTS.md"; "no source named" → "no source cited"; "names no source" → "cites no source"; worksheet row "source named" → "source cited". claim-receipt: "from a named family" → "from a published family". The noun ("gzkit adds two names", "The deck marks these names") stays. The Pilot's prompt text ("Name the file you took the answer from", "name your source") is the exercise's own prompt and was left verbatim.

### Schedule and management asides
"tonight" (n-plus-m SVG wire label, JS "Tonight's e3-tools server", memory stale-fact log) → "for Sortie 4" / "in this Evolution" / "today is"; "the evening", "this week", "last week", "week two/four", "week three" → "this Evolution", "Evolution 6", "Sortie 2 / Evolution 4", "Evolution 3"; "The deck asks/tells the instructor to verify ... before class" (claim-receipt, n-plus-m twice) → "The deck marks ... for verification against ..."; "Sprint due Wed 11/04", "Sprint due Wed 11/11" (eyebrows) and "the Sprint is due Wed 10/21" removed; "(class night)" option label → "(before the rule)"; "Thu 10/22/2026, in class." → "10/22/2026, the paired exercise."; "cheap this term" → "cheap in Fall 2026"; "(the week's reading)" → "(this Evolution's reading)".

### STE (actor, one term, no semicolons in procedures)
- claim-receipt: "the holder is presumed dead" → "the next worker treats the holder as dead"; "A summary is promoted to fact" → "Each layer promotes the summary below it to fact"; "Big Pickle data may be used" → "OpenCode may use Big Pickle data"; tier fragments ("Cheaper to arrange." "Slowest.") → full sentences.
- loop: three step-table cells with semicolon chains → one instruction per sentence.
- pilot: the Pilot and Planter duty lists (eleven bullets) → one action per sentence, no semicolons; the role stays the subject via the column heading.
- claim-receipt: "A gate that reads a record." (fragment) → "A gate that opens only on a record it reads."
- AI vocabulary: n-plus-m "protocol ecosystem" / "the ecosystem shares" → "a healthy set of implementers" / "every host and server shares".
- memory: "The pattern is what to compare." (pseudo-cleft) → "Compare the pattern of hits and misses across the four questions; the numbers themselves will not match."
- Table placeholders "—" (claim-receipt tier cell, memory heatmap "not in the store" cell) → "none" / "n/a", so no em dash remains.

## ste_check lines declined, and why
The checker ran on prose extracted from each file (panel paragraphs, list items, table cells, caption strings). Declined:
- Every "sentences over 25 words" line in explanatory paragraphs and captions (13, 7, 14, 4, 16, 9): the brief sets no ceiling there. The longest are falsifier lists ("Pre-registered falsifiers, any one of which fails the sortie: ...", 51 to 57 words) and the deck's quoted rows; splitting would turn a single pre-registered list into several claims. The two long lede sentences (memory 48 words, one-run 40) carry a list of what the figure shows and were kept.
- Gerund/nominalized-subject hits on "The harness ...", "The session ...", "The question ...", "The decision ...", "A retention rule ...", "Mutation testing ...": the subjects are stipulated terms or named systems, which rule 2 allows; the heuristic keys on the suffix.
- Passive hits inside quotations ("the results are known" in Kerr's title, "was exposed" inside OpenAI's sentence), inside the simulated transcripts ("your turn budget has been raised to 500" is the planted injection text), and where the actor is the sentence's own subject a clause earlier ("Roots, sampling, and logging are deprecated" by the revision the paragraph names; "is loaded on every turn" by OpenCode, stated in the previous caption). "has been seen red" is the deck's rule-one wording and stays.
- Noun-cluster hits that are file paths, commands, citation strings, or JSON field lists.
- Paragraphs over six sentences: the one-run Readings list and the pilot Probe-3 caption (seven short sentences describing one setup; splitting the caption would change the figure's JS array shape).
- Semicolon counts in explanatory paragraphs (house style); removed only from step-table cells and the duty lists.

## Sentences left long, with the reason
- memory lede, sentence 3 (48 words): one sentence carries the record's path and the lab's three controls; split, the controls would read as a separate instruction.
- one-run lede, sentence 2 (40 words): the four frozen things are the figure's four boxes, and the list is the point.
- claim-receipt, falsifier list (57 words) and memory, falsifier list (51): pre-registered lists, kept whole.
- one-run, "A judge that passes all four checks is a grader, and its verdict is still a model's claim about a model, so it can hold a gate shut but cannot stand in for a human's signature (GZK-GOV-007...)" (36): the chain premise, premise, therefore is the sentence.

## Unsure, left as is
- Panel headings with a colon and a gloss ("The RED witness: a gate must be seen to fail", "Pre-registration: the falsifier comes first", "The ten-deep chain: how a summary becomes a fact", "Routing and cost: send each task to a tier"): labels with a one-line gloss rather than arguments; left, since the brief said figure titles stay and the glosses are the deck's rules.
- Dates that double as schedule ("10/22" chips and eyebrows in pilot-and-planter, "checked 09/24/2026" on the price table): the figure's identity and a provenance date; kept.
- "The authors say multi-agent ... fits badly where all agents must share one context, including most coding" (claim-receipt): a frequency claim, but attributed to the Anthropic post.
- "because a model left to its own words will write 'verified'" (claim-receipt): the deck's rationale for the agent file, kept as the deck's.

## Self-audit artifacts after the final pass

# Lede list (first sentence of the page lede and of each panel)

## claim-receipt-verdict
- [lede] When a worker reports that all tests pass, the report proves only that the worker wrote it.
- [Fourteen ways a multi-agent system fails] The MAST taxonomy sorts 1,642 annotated traces from seven frameworks into three categories and fourteen modes.
- [The ten-deep chain: how a summary becomes a fact] In May 2026 the reference design ran a chain of subagents ten deep, each summarizing the layer below it.
- [Adversarial validation in three tiers] The tier you choose buys independence from the worker's blind spots; the adversary's size has no bearing on that.
- [Locks: who may work on what] The resource name, the 120-second TTL, and the clock are illustrative.
- [Routing and cost: send each task to a tier] Route by task class, declare a budget per sortie, and record the cost of every call.
- [“Don't Build Multi-Agents”] Walden Yan, Cognition, June 2025.
- [What coordination cost Anthropic's research system] A Claude Opus 4 lead plans and starts Claude Sonnet 4 subagents that search in parallel, and a CitationAgent ties the report's claims to sources at the end (June 2025).
- [Each test point checks one arrow in the figure] Pre-registered falsifiers, any one of which fails the sortie: a claim promoted to the flight log with no receipt; the adversary returning NOT-REFUTED on the planted falsehood; a lock held by two workers, or a lock change with no ledger event; passing only by telling the adversary the answer, using the worker's model, or editing a receipt.

## loop-that-halts
- [lede] An agent loop perceives, reasons, acts, and then checks whether it must stop, and the check belongs in code rather than in the prompt.
- [Fly one episode, one turn at a time] Pick a test point, set the two budgets, and step the loop.
- [The minimal loop, line by line] These twelve lines come from the deck.
- [The loop with a goal and no exit] The tinted boxes are model calls.
- [Flight Card 1 · Sortie 1: a governed loop that halts] Card text from the E1 deck, slide 13, rewrapped to fit.

## memory-is-a-claim
- [lede] A memory record is a claim with a source, and forgetting is an event.
- [Four questions against a five-record store] The deck runs four questions through recall.py with k = 2 and a threshold of 0.05.
- [A stale fact recalled with confidence] The deck's case: your Sortie 2 log says tests: uv run pytest -q.
- [The on/off protocol] Four kinds of question, asked twice, answered by the same model in a fresh session.
- [Four questions every retention rule answers] Rows quoted from the deck's slide 11.
- [Each test point exercises one part of this figure] Pre-registered falsifiers on the card (any one means FAIL): a recalled fact or cited id that was never stored; any item retained past its rule, or removed with no ledger event; retrieval that changes the control answer; passing only by editing the store or ledger by hand, or by letting the model read the repo.

## n-plus-m
- [lede] Before a shared protocol, every host that wanted a tool wrote its own adapter for it, so N hosts and M tools cost N×M adapters.
- [What each new tool costs] For the current N, the chart plots the integration code the field maintains as the number of tools grows.
- [What the protocol adds to E3's contract] Your E3 tool had a schema and a permission gate.
- [Who controls each primitive] The deck sorts the three server primitives by who controls them.
- [A stateless core] The revision that went to general availability on July 28, 2026 rewrote the wire, and its headline is statelessness.
- [Deprecated, and beyond the core] Deprecated in 2026-07-28.
- [Description without negotiation, and the protocol that followed] A protocol with a healthy set of implementers needs, in the deck's list, a versioning and deprecation policy, independent SDKs (TypeScript, Python, Go, C#; Rust in beta), a server registry with provenance, and governance that no single vendor holds.
- [Where is the human?] Read as a Design Analysis, MCP answers the N×M problem with a client–server protocol over JSON-RPC, three server primitives, and negotiated capabilities.
- [Sortie 4: one server, two clients] Design claim.
- [Why gzkit refused MCP, and the server one tier up] gzkit's governance verbs (gz status, gz validate, the ledger, receipts) run on the standard library over files.

## one-run-is-an-anecdote
- [lede] An evaluation that cannot fail proves nothing, because it would pass whatever the system did.
- [How often does a small-N gate decide wrong?] Simulation Figures are illustrative.
- [pass@k against pass^k] pass@k is the chance that at least one of k trials succeeds, so it rises with k and flatters. pass^k is the chance that all k succeed, so it falls with k, and it is the number a user who runs the task every day experiences.
- [The RED witness: a gate must be seen to fail] Rebuild without the change.
- [Pre-registration: the falsifier comes first] State the hypothesis, the measure, and the decision rule before you observe the outcome.
- [Judges, their biases, and the blinded rubric] Zheng et al.
- [Goldens copied from the system's own output] The set now encodes whatever the agent did on the day you ran it, bugs included.
- [SWE-bench Verified stops measuring the frontier] Contamination.
- [How the Berkeley group broke eight agent benchmarks] The group built an agent whose only job was to score well without solving anything.
- [The gate that fails when it should] Design claim: the evaluation suite fails when it should; removing the feature, or planting a wrong answer, turns the gate red.

## pilot-and-planter
- [lede] Two students share one repository and ask the model the same questions from different drawers.
- [Run the conflict probe] A model of the exercise, not a measurement.
- [Who checks what] The exercise runs in pairs.
- [The three outcomes] The Planter marks the exit from the written answer and from AGENTS.md, not from how sure the model sounded.
- [Each probe tests one drawer] Every probe runs on the same model id, written on the worksheet.


# Closer list (last sentence of every prose paragraph and caption, out of context)

## claim-receipt-verdict
- This figure follows the four records a multi-agent system writes about one piece of work; the failure matrix and the ten-deep chain below show what happens when a claim travels without a receipt.
- Receipt values are the deck's worked example.
- Select a mode to see what the deck says about it and which part of your build catches it.
- Where the deck says nothing about a single mode, the panel says so and gives the category's fix location.
- The deck does not quote the chain's text, so the summaries here are illustrative, built on the deck's worked receipt (3 tests run, 1 failure).
- The deck marks the date, the depth, and the rule's wording for verification against AGENTS.md.
- The tier you choose buys independence from the worker's blind spots; the adversary's size has no bearing on that.
- Model evaluators recognize and score their own generations higher than equal work from others (Panickssery, Bowman, & Feng, 2024).
- It is cheaper to arrange, and it shares the family's blind spots.
- This tier is the slowest, and it is the only one that can attest.
- With one family only, write “degraded mode” on the card.
- The deck's worked agent file denies the adversary edit, bash, and webfetch, and defines NOT-REFUTED inside the prompt, because a model left to its own words will write “verified.”
- The falsifier is a lock that changed hands with no ledger event, because then nobody can tell whether a collision happened.
- Prices and limits are from opencode.ai/docs/go, checked 09/24/2026; the deck says to verify them again before you fly.
- Your route table applies the same idea at the scale of one sortie.
- Two principles from the team that builds a coding agent.
- Yan's example: one builds a background in the wrong visual style, the other builds a bird that matches neither, and the lead cannot reconcile them.
- One single-threaded agent with continuous context, which compresses its history with a model when the window runs out.
- Sortie 9 asks you to check one claim with an agent that shares nothing with the worker, and it does not ask you to parallelize anything.
- A Claude Opus 4 lead plans and starts Claude Sonnet 4 subagents that search in parallel, and a CitationAgent ties the report's claims to sources at the end (June 2025).
- The authors say multi-agent fits breadth-first research and fits badly where all agents must share one context, including most coding.
- The deck marks these names for verification against the repository.
- Step through to see who writes each record and where your Sortie 9 lets it go.
- It never goes into the flight log on its own.
- The worker's sentence plays no part in this step.
- A receipt the worker writes for itself is a claim stored in a file, because the worker chose its contents.
- A reviewer that reads the worker's summary can check only whether the summary is coherent, and a model's summary is coherent whether or not the tests passed.
- NOT-REFUTED means that this adversary could not break the claim with this evidence; it does not mean verified.
- An agent may not write it on the human's behalf, because the attestation records that a person read the receipts.
- The first falsifier on Flight Card 9 is a claim promoted to the flight log with no receipt.
- The panels below apply both rules to the failure taxonomy, the ten-deep chain, locks, and routing.
- On Flight Card 9 this is the first falsifier: a claim promoted to the flight log with no receipt.
- The flight log cites the receipt, and the polished summaries stay in the ledger as unverified claims.

## loop-that-halts
- The simulator below flies scripted episodes through the same loop and reports the turn count, the tokens, and the bill as it goes.
- Real prices and token counts differ by provider and model.
- Each comment that says halt is one exit in the diagram.
- The ledger records the reason.
- Every decision in this loop came from the model, and nothing in code could end it.
- Both systems lacked the same three things: a budget, an evaluator, and a record.
- The governed path for this Evolution is gz init --mode lite, then gz prd, then the first ledger event, prd_created, then your attestation.
- An exceptional one includes a run designed to exhaust its budget, and the ledger shows that it did.
- Each step lights one state in the diagram and its lines in the code panel; the simulator below runs the whole loop on scripted episodes.
- Each turn therefore costs more than the one before it.
- Flight Card 1 treats a local model that cannot emit the schema at all as an abort and logs it as a squawk.
- The Chase grades your sortie from the ledger slice and the receipts only, so a turn that is missing from the ledger cannot count as evidence.
- On an unanswerable question, the model may never call it.
- An exception is an observation too, so a failing tool cannot end a run silently.
- A prompt that tells the loop to ignore its budget changes nothing, because the model never evaluates the check.
- A budget halt on an unanswerable question is the correct result for that test point.
- Episode 3 in the simulator plants an instruction inside a tool result.
- Turn the halt check off in the simulator to watch it.
- Fly all three test points in the simulator before you freeze your card.

## memory-is-a-claim
- One record from a flight log travels through retrieval into the context window and out again through eviction; the retrieval lab below then runs the deck's four questions against a five-record store, so you can watch the scores move as the chunking, the threshold, and the retriever change.
- Click a question to see its scores and the block the model would receive.
- A recall of an evicted fact must now fail, which is test point 5 on Flight Card 7.
- In a real store the ledger is append-only, and nothing removes its events.
- Put one in your Sortie 7 question set, or you have not tested the choice you made in ADR-2."
- The record ids, dates, and the unittest command line are constructed for the demo.
- When an attacker plants the stale fact on purpose, OWASP's agentic top 10 (Dec 2025) calls it ASI06, memory and context poisoning.
- Only the memory block changes between the two runs.
- That is data for the flight log, not a reason to change models mid-sortie."
- Of the three eviction policies the deck compares (by pressure in MemGPT, by rule, by relevance in Generative Agents), only the rule path gives the Chase a test to check, so Sortie 7 flies it.
- The lab handout is CIDM6333_Lab_E7_Memory.md.
- The steps that follow show where each rule becomes a field on a record, a file beside the store, or a test on the card.
- Hover a kind to see where it lives.
- The source files stay in the repository as L1 canon; the memory is a copy derived from them.
- Untick the heading box in the panel below to reproduce it.
- That consequence belongs in ADR-2.
- C #3), even when it happens to be true.
- In the layers of truth the ledger is L2 and the store is L3.
- Each recall is a ledger event.
- A record that says 'always do X' is content that some session, or some attacker, wrote, and E5's rule applies to your own store.
- The Chase checks that each evicted id has an event, is absent from the store, and that a question about it now fails.
- The deck's fixes are a supersedes field, dates in the block, and the authority order: the file in the repository is L1 and beats the memory, which is L3.
- If the answers match, the memory did not do the work.
- m-0101

## n-plus-m
- Move the sliders and step through the figure to watch the two counts part.
- Each line counts as one unit of work, although real adapters differ in size.
- It had none of these three, because nothing outside your process could ask it anything.
- Pick a primitive to trace its path from its controller to the server, or pick Sortie 4 to see one server called by two clients.
- The table is the deck's.
- The deck marks the protocol revision of the lab's Python SDK for verification; record yours on the card's SUBSTRATE line.
- Do not build a new server on a deprecated feature, even when a 2025 tutorial teaches it.
- The deck's advice is to adopt an extension only when the core cannot express the need.
- A registry without provenance is a supply chain, which E5 takes up with SmartLoader.
- MCP places the human outside the wire, and E5 studies what happens when the host's trust is misplaced.
- Every tool the server declares is discoverable, callable, and schema-validated from two independent clients, and every call is logged server-side.
- A tool that works from the harness and fails from the script means the harness was compensating, and the sortie has measured the compensation.
- An SDK and protocol-revision mismatch that prevents discovery aborts the card as halt-not-fail.
- The campaign review still scored MCP as absent and un-designed; a refusal counts as a decision only when someone writes it down with its alternatives.
- If validation fails, the server became a prerequisite and the doctrine is broken.
- Move the sliders to change N and M, and step through to see where each count comes from.
- Each line is code that a team writes, tests, and maintains.
- Either way, every host and tool pair needed its own integration.
- In the deck's words, the problem was combinatorial before it was technical.
- N hosts cost N pieces of code.
- In Sortie 4 you draw one of these lines yourself when you serve your E3 read tool.
- The chart below the figure plots both counts.
- Your E3 tool had a schema and a gate and none of these three.
- E5 shows the price, when the stranger who wrote a tool description turns out to be an adversary.
- The e3-tools server in this Evolution offers no prompt; /what-is-attested comes from the governance-server project.

## one-run-is-an-anecdote
- The simulator below shows how often a gate that sees only a few runs lets a regression through or blocks a real improvement, which is the reason one run is an anecdote.
- The real Sortie 10 gate also compares each case id, which this simulation leaves out.
- The curves assume independent trials with one fixed success chance per trial.
- Your card runs every model-in-the-loop case at least three times and reports pass^3 beside the mean.
- Restore, and watch it go green.
- Mutation testing (DeMillo, Lipton, & Sayward, 1978) changes the program on purpose: a suite that still passes has not tested what changed. gzkit records the result as a RED witness and runs it with gz arb red.
- The deck marks the gz arb red flags for verification against the repository.
- Nosek, Ebersole, DeHaven, and Mellor (2018) separate prediction, which tests a claim, from postdiction, which only generates one.
- In an eval suite, HARKing means choosing the threshold after seeing the score, dropping the case that failed, re-running until green, or adding a case the system already passes.
- Amendments append with a reason and never overwrite.
- Could the evidence have come out against you, and did you say in advance what that would look like?
- A judge that passes all four checks is a grader, and its verdict is still a model's claim about a model, so it can hold a gate shut but cannot stand in for a human's signature (GZK-GOV-007: model review is Gate-4 evidence, never Gate 5).
- It will catch a change, but it will never catch a wrong behavior that was already there, and it never asked whether the output was right.
- Rule for Sortie 10: every expected value in golden.jsonl traces to a requirement or an AI_LOG entry, never to a run.
- OpenAI wrote that gains on Verified “increasingly reflect how much the model was exposed to the benchmark at training time,” and recommends SWE-bench Pro (Scale AI, Sep 2025: 1,865 tasks, 41 repos, with public, held-out, and commercial partitions).
- A September 2026 preprint, SWE-Bench Pro Verified, closes those channels and re-scores.
- Appendix C #9, metagaming the gate: the agent satisfied the check by a route the check's author did not intend.
- Every exploit is a grader that trusted something the agent could touch.
- The Sortie 10 falsifiers are written to catch each row's small version in your own suite.
- Threshold, case count, predicted RED ids, and the removal diff are committed before Go, with the hash on the card.
- The deck marks these gzkit names and dates for verification against the repository.
- The simulator below the figure shows what the distribution step costs when N is small.
- A threshold or case changed after the first run is HARKing, and on Flight Card 10 it is a FAIL.
- You write each expected value by hand from the requirement, and never record it from the agent's output.
- Your card asks for at least three runs of each such case, with pass^3 reported beside the mean and the trial count stated with every rate.
- Your judge comes from a different model family, reads a blinded rubric, and judges both orders before its verdict counts.
- The simulator below draws this distribution and counts how often a gate decides wrong when N is small.
- An aggregate can hold steady while one requirement breaks and another improves, so the delta lists each regressed id and writes delta.json.
- A red gate that does not list the failed case sends you to the transcript blind.
- A gate you run by hand only when you remember to is a report, because nothing depends on its exit code. gzkit added a pre-push gate after green main was reopened eight times in nine days.
- You plant one wrong answer and expect the grader or judge to fail it.
- The RED witness and pre-registration let you find it before your Chase does.

## pilot-and-planter
- The probe model below lets you turn the three fixes on and off and watch the exit change.
- Unticking the first box is the role-swap rerun: Probe 3 with the "data, not instructions" sentence deleted.
- After Probe 3 the pair evicts, then swaps roles for one rerun of Probe 3 with the "data, not instructions" sentence deleted.
- One rerun is one row on the worksheet; it supports no claim beyond that row.
- A correct command with no source is silent merge, not intent held.
- The Planter checks against the file that holds the truth, never against how sure the answer sounds.
- The last probe asks whether a stale memory can beat a rule the model sees on every turn.
- The Planter then checks it against the file that holds the truth.
- The full file loads when the model calls the skill, and permission.skill ask shows that call as a prompt.
- That contradicts AGENTS.md, and nothing has removed it yet.
- This drawer is loaded on every turn, so a miss here is a harness problem, not a memory problem.
- The proof is the prompt itself, then the card against SKILL.md.
- The block says make test.
- This is the expected row, and it does not show what produced it, the model's disposition on that run or a mechanism in the loop; the three fixes at the end of the figure separate the two.
- This is the stale fact from Figure 08, planted on purpose by a partner.
- An answer with no source cannot be checked, so it fails the probe even when the command is right.
- The ledger line is the evidence that the forgetting happened as an event.
- The Final System's V&V must put intent held in the loop.


# Claim list (frequency or consensus claims: most / every / usually / often / tend to)

- [claim-receipt-verdict] The authors say multi-agent fits breadth-first research and fits badly where all agents must share one context, including most coding.
- [one-run-is-an-anecdote] The simulator below shows how often a gate that sees only a few runs lets a regression through or blocks a real improvement, which is the reason one run is an anecdote.
- [one-run-is-an-anecdote] Steps 3, 5 and 7, up close · E10 slides 6 and 7 How often does a small-N gate decide wrong?
- [one-run-is-an-anecdote] The simulator below draws this distribution and counts how often a gate decides wrong when N is small.