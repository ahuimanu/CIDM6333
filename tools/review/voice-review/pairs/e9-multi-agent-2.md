# e9-multi-agent-2: speaker notes, before and after the voice pass

## Slide 1

### BEFORE

Evolution 9. Last week you built a worker and a reviewer that talk through a contract. Tonight we break that pair on purpose. The framing sentence is the run sheet's: a subagent's claim is not evidence. Survey: the one taxonomy of multi-agent failure built from real traces, one production multi-agent system read for its cost, the A2A protocol at version 1.0, and what an agent marketplace would need before anyone should trust it. Build: an adversary from a different model family that refutes a claim you planted, a lock that two workers cannot both hold, and a route table that sends each task to a model tier and records what it cost. The lab at six plants the first false claim; the Sprint flies the whole corner card.

Cut from slide 1 (full wording):
- Evolution 9 · Lecture · Thu 10/29
- CIDM 6333 · Agentic Systems Design and Development · 4:00–6:00 · CC209 / Survey: Cemri et al. (MAST, 2025) · Anthropic's multi-agent research system · A2A v1.0 delegation · AP2 mandates   ·   Build: a second-family adversary that refutes a planted false claim, a lock with a TTL, a route table with a budget (lab 6:00–6:30)

### AFTER

Evolution 9. In Evolution 8 you built a worker and a reviewer that talk through a contract. This Evolution breaks that pair on purpose. The framing sentence is the run sheet's: a subagent's claim is not evidence. Survey: the one taxonomy of multi-agent failure built from real traces, one production multi-agent system read for its cost, the A2A protocol at version 1.0, and what an agent marketplace would need before anyone should trust it. Build: an adversary from a different model family that refutes a claim you planted, a lock that two workers cannot both hold, and a route table that sends each task to a model tier and records what it cost. The lab plants the first false claim, and the Sprint flies the whole corner card.

Cut from slide 1 (full wording):
- Evolution 9 · Lecture
- CIDM 6333 · Agentic Systems Design and Development / Survey: Cemri et al. (MAST, 2025) · Anthropic's multi-agent research system · A2A v1.0 delegation · AP2 mandates   ·   Build: a second-family adversary that refutes a planted false claim, a lock with a TTL, a route table with a budget

## Slide 2

### BEFORE

Eight minutes of framing, forty of spine with a common-mistake slide at the end, five minutes of break, thirty on teardowns including one Design Analysis we build on the board, fifteen on three dated gzkit episodes, and the last fifteen on the lens, the card, the lab, and the Sprint. There is no consultation block this term; the Go/No-Go and the Chase review happen in the repository, in writing, and the homework brief gives the days.

Cut from slide 2 (full wording):
- MAST (Cemri et al.); Anthropic's research system and a live Design Analysis; 'Don't build multi-agents'; A2A v1.0; AP2 and marketplaces
- Self-guided lab 6:00–6:30; the Sprint, the async Go/No-Go, the Chase

### AFTER

The lecture runs in eight parts: framing, the spine with a common-mistake slide at its end, a break, teardowns that include one Design Analysis built on the board, three dated gzkit episodes, and then the lens, the card, the lab, and the Sprint. There is no consultation block. The Go/No-Go and the Chase review happen in the repository, in writing, and the Sprint brief gives the dates.

Cut from slide 2 (full wording):
- MAST (Cemri et al.); Anthropic's research system and a live Design Analysis; 'Don't build multi-agents'; A2A v1.0; AP2 and marketplaces
- Self-guided lab; the Sprint, the async Go/No-Go, the Chase

## Slide 3

### BEFORE

Framing. Last week's pair gave you a contract, and a contract tells you the shape of a claim, not whether it is true. Two rules. First, a claim needs a receipt that the harness wrote: command, exit code, commit, output hash. Second, the check comes from something with different blind spots, and the cheapest different thing is a different model family. The claim is the chapter 18 corner card. Notice the second falsifier: if you plant a falsehood and your adversary lets it through, the sortie fails, which means you will know before you fly whether your adversary is a real one.

Cut from slide 3 (full wording):
- A worker that says “all tests pass” has produced a sentence. The harness that ran the tests and wrote down the exit code has produced evidence.
- Rule one. A claim moves toward the flight log only with a receipt: the command, the exit code, the commit, and a hash of the output, written by the harness and never by a model. / Rule two. The check comes from something that does not share the worker's blind spots: a second model family first, an independent subagent second, a human third. A reviewer that shares the worker's model shares its mistakes.
- A subagent's claim never becomes evidence without a receipt, and a second-family adversary refutes a false claim that you planted. Any one of these falsifies it: a claim in the flight log with no receipt; the adversary returning NOT-REFUTED on the planted falsehood; a lock held by two workers, or a lock change with no ledger event.

### AFTER

Framing. The Evolution 8 pair gave you a contract, and a contract fixes the shape of a claim without saying whether the claim is true. Two rules follow. First, a claim needs a receipt that the harness wrote: command, exit code, commit, output hash. Second, the check comes from something with different blind spots, and the cheapest different thing is a different model family. The design claim is the chapter 18 corner card. The second falsifier does the most work: if you plant a falsehood and your adversary lets it through, the sortie fails, so the sortie itself tells you whether your adversary is a real one.

Cut from slide 3 (full wording):
- A worker that reports “all tests pass” has produced only a sentence. Evidence comes from the harness, because the harness ran the tests and recorded the exit code.
- Rule one. A claim moves toward the flight log only with a receipt: the command, the exit code, the commit, and a hash of the output, written by the harness and never by a model. / Rule two. The check comes from something that does not share the worker's blind spots: a second model family first, an independent subagent second, a human third. A reviewer that runs on the worker's model tends to accept the worker's mistakes, because both were trained the same way.
- A subagent's claim never becomes evidence without a receipt, and a second-family adversary refutes a false claim that you planted. Any one of these falsifies it: a claim in the flight log with no receipt; the adversary returning NOT-REFUTED on the planted falsehood; a lock held by two workers, or a lock change with no ledger event.

## Slide 4

### BEFORE

The taxonomy, by the paper's three categories. The shares are the paper's own prevalence figures summed by category; they add to about one hundred percent across the three. Design failures are the largest group, and the top single mode is step repetition, which is a halt problem you met in week one. Misalignment is the traffic between agents; the top mode there is a reasoning-action mismatch, where the agent says one thing and does another. Verification is the last line: incorrect verification alone is nine percent of failures, which is a reviewer that checked and got it wrong. The strip adds the two names from the reference design. Summary laundering is FC2 and FC3 at once: the information passes, and nobody checks it.

Cut from slide 4 (full wording):
- The failure is in the setup: the task or role specification, the stopping condition, the memory. / Step repetition 15.7% / Unaware of stopping conditions 12.4% / Disobey task specification 11.8%
- The failure is at the end: the check was missing, wrong, or came too early. / Incorrect verification 9.1% / No or incomplete verification 8.2% / Premature termination 6.2%
- The failure is in the traffic between agents: information lost, ignored, or never asked for. / Reasoning-action mismatch 13.2% / Task derailment 7.4% / Fail to ask for clarification 6.8%
- gzkit adds two names the paper does not use: summary laundering (a summary is promoted to fact) and hallucinated authorization (Appendix C #7: acting on a gate that nothing records).

### AFTER

The taxonomy, by the paper's three categories. The shares are the paper's own prevalence figures summed by category, and they add to about one hundred percent across the three. Design failures are the largest group, and the top single mode is step repetition, which is the halt problem you met in Evolution 1. Misalignment is the traffic between agents, and the top mode there is a reasoning-action mismatch, where the agent says one thing and does another. Verification is the last line: incorrect verification alone is nine percent of failures, which means a reviewer checked and got it wrong. The strip adds the two terms from the reference design. Summary laundering is FC2 and FC3 at once: the information passes, and nobody checks it.

Cut from slide 4 (full wording):
- The failure is in the setup: the task or role specification, the stopping condition, the memory. / Step repetition 15.7% / Unaware of stopping conditions 12.4% / Disobey task specification 11.8%
- The failure is at the end: the check was missing, wrong, or came too early. / Incorrect verification 9.1% / No or incomplete verification 8.2% / Premature termination 6.2%
- The failure is in the traffic between agents: information lost, ignored, or never asked for. / Reasoning-action mismatch 13.2% / Task derailment 7.4% / Fail to ask for clarification 6.8%
- gzkit adds two names the paper does not use: summary laundering (a summary is promoted to fact) and hallucinated authorization (Appendix C #7: acting on a gate that nothing records).

## Slide 5

### BEFORE

This table is the vocabulary for the week. A claim is a sentence a model wrote; it goes in the ledger marked unverified and never in the flight log. A receipt is what the harness observed when it ran the command itself, and it is the only row here that is evidence about the code. The adversary's verdict is also a claim, from a different author; the Chase checks that its citation points at a real field in the receipt. The attestation is the human's and is never inferred. The strip is the sentence most students get wrong in their flight logs: not refuted is not verified.

Cut from slide 5 (full wording):
- A second model, given the claim and the receipt: REFUTED or NOT-REFUTED, with the field it cites
- That a model with other blind spots could or could not break the claim with this evidence. It is itself a claim.
- HandoffResult statuses from Sortie 8: DONE | DONE_WITH_CONCERNS | NEEDS_CONTEXT | BLOCKED. The adversary's verdict does not upgrade a claim to evidence; the receipt does.

### AFTER

This table is the vocabulary for this Evolution. A claim is a sentence a model wrote; it goes in the ledger marked unverified and never in the flight log. A receipt is what the harness observed when it ran the command itself, and it is the only row here that is evidence about the code. The adversary's verdict is also a claim, from a different author, and the Chase checks that its citation points at a real field in the receipt. The attestation is the human's, and the harness never infers it. The strip is the rule to carry into the flight log: not refuted is not verified.

Cut from slide 5 (full wording):
- A second model, given the claim and the receipt: REFUTED or NOT-REFUTED, with the field it cites
- That a model with other blind spots could or could not break the claim with this evidence. It is itself a claim.
- HandoffResult statuses from Sortie 8: DONE | DONE_WITH_CONCERNS | NEEDS_CONTEXT | BLOCKED. Only a receipt turns a claim into evidence, so the adversary's verdict alone leaves the claim a claim.

## Slide 6

### BEFORE

Three tiers. Tier one is a different family because the failure you are guarding against is a shared blind spot, and the self-preference result gives you the measured reason: evaluators score their own generations higher. Tier two is a fresh subagent of the same family, which removes the shared transcript but not the shared training. Tier three is a person. On the right, the practical news: with OpenCode Go, a second family costs almost nothing, and I checked the prices on the Go page this week; verify them again before you fly. Big Pickle's family is undisclosed, so you cannot prove it differs from your adversary; two adversaries from two named families solve that for pennies. If you only have one family, the reference design's rule applies: run in degraded mode and say so on the card.

Cut from slide 6 (full wording):
- Tier 1 · cross-vendor. A different model family. It does not share the worker's training data, tokenizer, or house style, so it is least likely to find the worker's mistake plausible. Self-preference is measured: model evaluators recognize and score their own generations higher than equal work from others (Panickssery, Bowman, & Feng, 2024). / Tier 2 · independent subagent. Same family, fresh context, no access to the worker's transcript. Cheaper to arrange; shares the family's blind spots. / Tier 3 · human. The Chase, or you. Slowest; the only tier that can attest.
- Tier 1 is cheap this term. If your worker runs on Big Pickle, run the adversary on an OpenCode Go model from a named family: GLM, DeepSeek, Kimi, Qwen, MiniMax, MiMo. glm-5.3-flash lists $0.15 in and $0.50 out per million tokens; one 3,000-token adversary call costs well under a tenth of a cent. / Big Pickle is a stealth model: its family is not published. Write “worker family: undisclosed,” and run two adversaries from two Go families to close the gap. / No Go subscription: use a free Zen model from a named family (Nemotron, MiMo). With one family only, say “degraded mode” on the card.
- The adversary gets the claim and the receipt. It never gets the worker's summary, its reasoning, or the answer you planted.

### AFTER

Three tiers. Tier one is a different family, because the failure you are guarding against is a shared blind spot, and the self-preference result gives you the measured reason: evaluators score their own generations higher. Tier two is a fresh subagent of the same family, which removes the shared transcript but not the shared training. Tier three is a person. On the right, the practical consequence: with OpenCode Go, a second family costs almost nothing. Verify the prices on the Go page before you fly. Big Pickle's family is undisclosed, so you cannot prove it differs from your adversary's; two adversaries from two disclosed families close that gap for a few cents. If you have only one family, the reference design's rule applies: run in degraded mode and say so on the card.

Cut from slide 6 (full wording):
- Tier 1 · cross-vendor. A different model family. It does not share the worker's training data, tokenizer, or house style, so it is least likely to find the worker's mistake plausible. Self-preference is measured: model evaluators recognize and score their own generations higher than equal work from others (Panickssery, Bowman, & Feng, 2024). / Tier 2 · independent subagent. Same family, fresh context, no access to the worker's transcript. Cheaper to arrange; shares the family's blind spots. / Tier 3 · human. The Chase, or you. Slowest; the only tier that can attest.
- Tier 1 is cheap this term. If your worker runs on Big Pickle, run the adversary on an OpenCode Go model from a disclosed family: GLM, DeepSeek, Kimi, Qwen, MiniMax, MiMo. glm-5.3-flash lists $0.15 in and $0.50 out per million tokens; one 3,000-token adversary call costs well under a tenth of a cent. / Big Pickle is a stealth model: its family is not published. Write “worker family: undisclosed,” and run two adversaries from two Go families to close the gap. / No Go subscription: use a free Zen model from a disclosed family (Nemotron, MiMo). With one family only, say “degraded mode” on the card.
- The adversary gets the claim and the receipt. It never gets the worker's summary, its reasoning, or the answer you planted.

## Slide 7

### BEFORE

Three pieces you can copy. The agent file is OpenCode's markdown agent format: a subagent with its own model and every write-class permission denied, so the adversary can read what you attach and nothing else. The prompt asks for one JSON object and defines NOT-REFUTED in the prompt itself, because a model left to its own words will write verified. The receipt is written by your harness when it runs the test command; the model never touches it. The ledger event records the model id and the family, which is what the Chase checks. The last line is the non-interactive form: opencode run with an agent and attached files, which is how you will call it from a script in the Sprint.

### AFTER

Three pieces you can copy. The agent file is OpenCode's markdown agent format: a subagent with its own model and every write-class permission denied, so the adversary can read what you attach and nothing else. The prompt asks for one JSON object and defines NOT-REFUTED in the prompt itself, because the prompt, and not the model's own wording, must fix what the verdict means. Your harness writes the receipt when it runs the test command, and the model never touches it. The ledger event records the model id and the family, which is what the Chase checks. The last line is the non-interactive form, opencode run with an agent and attached files, which is how you will call it from a script in the Sprint.

## Slide 8

### BEFORE

Locks in four steps. The atomic create is the whole trick: O_EXCL makes the operating system the referee, so you do not need a lock server for one laptop. The second worker is denied and says who holds the lock; it does not wait forever and it does not overwrite. Release needs the token, so a confused worker cannot free someone else's lock. The TTL handles the worker that crashed while holding it, and the expiry is recorded before the reclaim so the order is visible in the ledger. The reference design has a lock verb for exactly this, and the chapter calls the ledger the lock's witness. The strip is the card's falsifier, stated carefully.

Cut from slide 8 (full wording):
- Create locks/<resource>.lock with os.open(path, O_CREAT | O_EXCL). The operating system lets exactly one caller create it. Write {holder, token, acquired_at, ttl_s}. / Ledger: lock_acquired.
- A second worker's create fails with FileExistsError. It does not wait silently and does not overwrite. It returns BLOCKED with the holder's name. / Ledger: lock_denied.
- Only the caller holding the token may delete the lock. A release with the wrong token is refused. / Ledger: lock_released.
- If now > acquired_at + ttl_s, the holder is presumed dead. The next worker records the expiry before it takes the lock. / Ledger: lock_expired, then lock_acquired.
- The falsifier is not “two workers collided.” It is a lock that changed hands with no ledger event, because then nobody can tell whether the collision happened.

### AFTER

Locks in four steps. The atomic create does the work: O_EXCL makes the operating system the referee, so you do not need a lock server for one laptop. The harness denies the second worker, which learns who holds the lock; it does not wait forever and it does not overwrite. Release needs the token, so a confused worker cannot free someone else's lock. The TTL handles the worker that crashed while holding the lock, and the next worker records the expiry before the reclaim so that the order is visible in the ledger. The reference design has a lock verb for this case, and the chapter calls the ledger the lock's witness. The strip states the card's lock falsifier.

Cut from slide 8 (full wording):
- Create locks/<resource>.lock with os.open(path, O_CREAT | O_EXCL). The operating system lets exactly one caller create it. Write {holder, token, acquired_at, ttl_s}. / Ledger: lock_acquired.
- A second worker's create fails with FileExistsError. It does not wait silently and does not overwrite. It returns BLOCKED with the holder's name. / Ledger: lock_denied.
- Only the caller holding the token may delete the lock. A release with the wrong token is refused. / Ledger: lock_released.
- If now > acquired_at + ttl_s, the holder is presumed dead. The next worker records the expiry before it takes the lock. / Ledger: lock_expired, then lock_acquired.
- The falsifier is a lock that changed hands with no ledger event. A collision that the ledger records can be traced; without the event, nobody can tell whether two workers collided.

## Slide 9

### BEFORE

Routing. The idea is old and the numbers are published: route easy work to a cheap model and hard work to an expensive one. RouteLLM, from the same Berkeley group as the MAST paper, reported more than eighty-five percent lower cost on MT Bench while keeping ninety-five percent of GPT-4's quality; FrugalGPT's cascades reported up to ninety-eight percent lower cost. Your version is a table in config, one row per task class, and a budget line on the card. The prices are the Go page's as of this week. Two things to notice: Kimi K3 costs twenty times glm-5.3-flash on output and allows about a hundred and ten requests per five hours, so it belongs on the rows where a mistake propagates; and the adversary row needs a different family, not a bigger model. The reference design keeps a dispatch model map for the same purpose.

Cut from slide 9 (full wording):
- An error here reaches every worker. Kimi K3 allows about 110 requests per 5 hours on Go.
- Prices and limits from opencode.ai/docs/go, checked 09/24/2026. Go is $10/month with dollar limits per model per 5 hours, week, and month (20% / 50% / 100% of the monthly limit).
- RouteLLM (Ong et al., 2024): 85% lower cost on MT Bench at 95% of GPT-4's quality. FrugalGPT (Chen, Zaharia, & Zou, 2023): cascades matched GPT-4 at up to 98% lower cost. Your route table is the small version.

### AFTER

Routing. The idea is old and the numbers are published: route easy work to a cheap model and hard work to an expensive one. RouteLLM, from the same Berkeley group as the MAST paper, reported more than eighty-five percent lower cost on MT Bench while keeping ninety-five percent of GPT-4's quality, and FrugalGPT's cascades reported up to ninety-eight percent lower cost. Your version is a table in config, one row per task class, and a budget line on the card. The prices are the Go page's; verify them before you fly. Two rows deserve attention. Kimi K3 costs twenty times glm-5.3-flash on output and allows about a hundred and ten requests per five hours, so it belongs on the rows where a mistake propagates. The adversary row needs a different family rather than a bigger model. The reference design keeps a dispatch model map for the same purpose.

Cut from slide 9 (full wording):
- An error in the route table reaches every worker. Kimi K3 allows about 110 requests per 5 hours on Go.
- Prices and limits from opencode.ai/docs/go, as of 09/24/2026. Go is $10/month with dollar limits per model per 5 hours, week, and month (20% / 50% / 100% of the monthly limit).
- RouteLLM (Ong et al., 2024): 85% lower cost on MT Bench at 95% of GPT-4's quality. FrugalGPT (Chen, Zaharia, & Zou, 2023): cascades matched GPT-4 at up to 98% lower cost. Your route table applies the same cascade at small scale.

## Slide 10

### BEFORE

Delegation as a contract, in four parts. Identity: who asked and who answered; the protocol now supports signed agent cards, and your dispatch record does the same job locally. Scope comes from config, not from the task text, which is E5's rule again. The result contract says what evidence each status needs; fail closed, so a DONE with no receipt is treated as needing context. The evidence obligation says who writes the receipt, and if it is the worker, it is not a receipt. The strip is the one thing that does not cross: the human's authority. When a peer needs it, the protocol has states for asking, and your host answers.

Cut from slide 10 (full wording):
- Who is asking and who is answering, by name and model id. A2A v1.0 lets an agent sign its Agent Card; in your system, the dispatch record names the worker and its model.
- What the worker may touch: paths, tools, the lock it holds. The worker's permissions come from its own config, never from the text of the task.
- The shape of what comes back (HandoffResult; a ReviewResult) and the evidence each status requires. DONE without a receipt parses as NEEDS_CONTEXT, not as DONE.
- Who produces the receipt and where it lands. If the worker writes its own receipt, you have a claim with a file extension.
- Authority does not cross: the user's approval for a write stays with the user's host. A peer that needs it asks for it (A2A's input-required and auth-required states).

### AFTER

Delegation as a contract, in four parts. Identity: who asked and who answered. The protocol now supports signed agent cards, and your dispatch record does the same job locally. Scope comes from config and never from the task text, which is E5's rule again. The result contract says what evidence each status needs; the harness fails closed, so it treats a DONE with no receipt as needing context. The evidence obligation says who writes the receipt, and a receipt that the worker wrote is a claim. The strip states the one thing that does not cross the boundary, the human's authority. When a peer needs it, the protocol has states for asking, and your host answers.

Cut from slide 10 (full wording):
- Who is asking and who is answering, by name and model id. A2A v1.0 lets an agent sign its Agent Card; in your system, the dispatch record lists the worker and its model.
- What the worker may touch: paths, tools, the lock it holds. The worker's permissions come from its own config, never from the text of the task.
- The shape of what comes back (HandoffResult; a ReviewResult) and the evidence each status requires. The parser reads DONE without a receipt as NEEDS_CONTEXT.
- Who produces the receipt and where it lands. If the worker writes its own receipt, the receipt is only the worker's claim saved to a file, so the harness must write it.
- Authority does not cross: the user's approval for a write stays with the user's host. A peer that needs it asks for it (A2A's input-required and auth-required states).

## Slide 11

### BEFORE

The common mistake, which the reference design made at scale in May: the reviewer read the summary. Five versions of it. Handing the adversary the worker's narrative, which is always coherent. Calling the worker's own model an adversary because the prompt says be critical. Telling the adversary what you planted. An adversary that refutes everything, which is why the card has a true-claim control. And writing not refuted as verified. Each of these passes the sortie on paper and would fail the Chase's read.

Cut from slide 11 (full wording):
- Narrative, not receipt. The adversary gets the worker's story. It checks whether the story is coherent, and a fluent story always is. / Same model, new prompt. The adversary is the worker's model told to “be critical.” That is tier 2 at best; write it as tier 2. / Answer leaked. The adversary is told what was planted. Then the test measures whether it can read. / Refutes everything. An adversary with no true-claim control proves nothing; test point 4 exists for this. / NOT-REFUTED logged as “verified.” The verdict is a claim from a second author; the receipt is the evidence.

### AFTER

The common mistake, which the reference design made at scale in May, is that the reviewer read the summary. It has five versions. You hand the adversary the worker's narrative, which is coherent whether or not it is true. You call the worker's own model an adversary because the prompt says be critical. You tell the adversary what you planted. The adversary refutes everything, which is why the card has a true-claim control. And you write not refuted as verified. Each of these passes the sortie on paper and fails the Chase's read.

Cut from slide 11 (full wording):
- Narrative, not receipt. The adversary gets the worker's story. It checks whether the story is coherent, and a fluent model writes a coherent story whether or not the work was done. / Same model, new prompt. The adversary is the worker's model told to “be critical.” That is tier 2 at best; write it as tier 2. / Answer leaked. The adversary is told what was planted. Then the test measures only whether the adversary can repeat what it was told. / Refutes everything. Without a true-claim control, nobody can tell a working adversary from one that refutes every claim. Test point 4 is that control. / NOT-REFUTED logged as “verified.” The verdict is a second author's claim, so the flight log must point at the receipt as the evidence.

## Slide 12

### BEFORE

Break. Five minutes. Hold the question: before you write tests pass in your flight log, what must you have seen, and who wrote it? We come back to it with the paper that counted how often nobody checked.

Cut from slide 12 (full wording):
- Your worker says “all tests pass.” What would you need to see before you would write that sentence in your flight log, and who would have to have written it?

### AFTER

Break. Hold this question through it: before you write tests pass in your flight log, what must you have seen, and who wrote it? The next slide returns to it with the paper that counted how often nobody checked.

Cut from slide 12 (full wording):
- Your worker says “all tests pass.” What would you need to see before you would write that sentence in your flight log, and who would have to have written it?

## Slide 13

### BEFORE

The paper, read as data. Three categories, fourteen modes, and the prevalence for each from the paper's own figure; the totals are my sums of their numbers. The corpus is about sixteen hundred traces from seven open frameworks, and two numbers tell you how much to trust the labels: human annotators agreed at kappa 0.88, and their automated annotator agreed with experts at 0.77. Map the modes to our Appendix C: a reasoning-action mismatch sits next to fabrication, no or incomplete verification is skipped cheap verification, and incorrect verification is where summary laundering lives, because the check happened and checked the wrong thing. The v3 of the paper is dated October 2025; cite the NeurIPS version.

Cut from slide 13 (full wording):
- Figures from the paper's HTML (v3, 26 Oct 2025). 1,642 traces from 7 frameworks: ChatDev, MetaGPT, HyperAgent, AppWorld, AG2 (MathChat), Magentic-One, OpenManus. Human inter-annotator agreement κ = 0.88; the paper's LLM annotator κ = 0.77 against experts.
- Map to Appendix C: 2.6 is #3 fabrication's neighbor; 3.2 is #4 skipped cheap verification; 3.3 is where summary laundering lives.

### AFTER

The paper, read as data. Three categories, fourteen modes, and the prevalence for each from the paper's own figure; the totals are my sums of their numbers. The corpus is about sixteen hundred traces from seven open frameworks, and two numbers tell you how much to trust the labels: human annotators agreed at kappa 0.88, and the automated annotator agreed with experts at 0.77. Map the modes to the course's Appendix C: a reasoning-action mismatch sits next to fabrication, no or incomplete verification is skipped cheap verification, and incorrect verification is where summary laundering lives, because the check happened and checked the wrong thing. The v3 of the paper is dated October 2025; cite the NeurIPS version.

Cut from slide 13 (full wording):
- Figures from the paper's HTML (v3, 26 Oct 2025). 1,642 traces from 7 frameworks: ChatDev, MetaGPT, HyperAgent, AppWorld, AG2 (MathChat), Magentic-One, OpenManus. Human inter-annotator agreement κ = 0.88; the paper's LLM annotator κ = 0.77 against experts.
- Map to Appendix C: 2.6 is #3 fabrication's neighbor; 3.2 is #4 skipped cheap verification; 3.3 is where summary laundering lives.

## Slide 14

### BEFORE

Read the paper as a system. The mechanism: most failures are in the setup and the checks, not in the model's knowledge. The design choice: a taxonomy from a hundred and fifty traces, then an LLM annotator to scale it. The interventions matter for your build: a clearer role specification bought about nine points on ChatDev and a high-level verification step about sixteen. The cost is labeling effort, and the cheaper annotator agrees less. The failure it leaves is in their own words: one final low-level check is not enough. Your card has two levels, a receipt and an adversary, for that reason. In your debrief, label one failure from your own traces with its MAST code.

Cut from slide 14 (full wording):
- Mechanism. Most failures start before any agent is wrong about the world: a vague role, no stopping rule, a check that looks at the wrong thing. / Design choice. The authors built a grounded-theory taxonomy from 150 traces, then scaled labeling with an LLM annotator so other teams can label their own traces. / Interventions tested (ChatDev). A clearer role specification: +9.4% success. A high-level verification step: +15.6% on ProgramDev.
- Cost. Labeling traces is expensive; the LLM annotator is cheaper and agrees less (0.77 against 0.88). / Failure mode it leaves. The authors write that sole reliance on final-stage, low-level checks is inadequate. Better prompts raised success but did not remove the categories. / For Sortie 9. Your receipt is the low-level check; your adversary is the second level. Neither replaces the other. Label one failure from your own traces with a MAST code in the debrief.

### AFTER

Read the paper as a system. The mechanism: the setup (FC1, 44 percent) and the checks (FC3, 24 percent) account for about two thirds of failures, and none of the fourteen modes is a fact the model got wrong about the world. The design choice: a taxonomy from a hundred and fifty traces, then an LLM annotator to scale it. The interventions matter for your build: a clearer role specification bought about nine points on ChatDev, and a high-level verification step about sixteen. The cost is labeling effort, and the cheaper annotator agrees less. The failure it leaves is in the authors' own words: one final low-level check is not enough. Your card has two levels, a receipt and an adversary, for that reason. In your debrief, label one failure from your own traces with its MAST code.

Cut from slide 14 (full wording):
- Mechanism. In MAST, the largest share of failures starts before any agent is wrong about the world: a vague role, no stopping rule, a check that looks at the wrong thing. / Design choice. The authors built a grounded-theory taxonomy from 150 traces, then scaled labeling with an LLM annotator so other teams can label their own traces. / Interventions tested (ChatDev). A clearer role specification: +9.4% success. A high-level verification step: +15.6% on ProgramDev.
- Cost. Labeling traces is expensive; the LLM annotator is cheaper and agrees less (0.77 against 0.88). / Failure mode it leaves. The authors write that sole reliance on final-stage, low-level checks is inadequate. Better prompts raised success but did not remove the categories. / For Sortie 9. Your receipt is the low-level check; your adversary is the second level. The sortie requires both, because each catches failures the other misses. Label one failure from your own traces with a MAST code in the debrief.

## Slide 15

### BEFORE

A production system, with numbers. Fifteen times the tokens of a chat, and token usage alone explains eighty percent of the variance on their browsing benchmark, which tells you the gain is bought with spend. The ninety percent improvement is on their internal eval, not a public benchmark; say that when you cite it. The failures are MAST failures: duplicated work and over-spawning are FC1 and FC2, and the fix was specification, which matches the paper's intervention. Two design choices to steal: the citation step, which ties claims back to sources, and writing outputs to files, which turns a relayed claim into an artifact the next agent can check. The strip is their own caveat about coding.

Cut from slide 15 (full wording):
- Mechanism. A lead agent (Claude Opus 4) plans and starts Claude Sonnet 4 subagents that search in parallel; a CitationAgent ties the report's claims to sources at the end. / Failures they report. Early subagents duplicated the same searches and spawned too many tasks for simple queries; the fix was detailed task descriptions and explicit effort rules in the prompt. The lead runs subagents synchronously, so one slow subagent blocks the system. Subagents write output to a filesystem instead of passing it through the lead, to cut copying loss.
- The authors say multi-agent fits breadth-first research and fits badly where all agents must share one context, including most coding. Name your system's case.

### AFTER

A production system, with numbers. Fifteen times the tokens of a chat, and token usage alone explains eighty percent of the variance on their browsing benchmark, so the gain is bought with tokens. The ninety percent improvement is on their internal eval and not on a public benchmark; say that when you cite it. The failures are MAST failures: duplicated work and over-spawning are FC1 and FC2, and the fix was specification, which matches the paper's intervention. Two design choices to copy: the citation step, which ties claims back to sources, and writing outputs to files, which turns a relayed claim into an artifact the next agent can check. The strip is their own caveat about coding.

Cut from slide 15 (full wording):
- Mechanism. A lead agent (Claude Opus 4) plans and starts Claude Sonnet 4 subagents that search in parallel; a CitationAgent ties the report's claims to sources at the end. / Failures they report. Early subagents duplicated the same searches and spawned too many tasks for simple queries; the fix was detailed task descriptions and explicit effort rules in the prompt. The lead runs subagents synchronously, so one slow subagent blocks the system. Subagents write output to a filesystem instead of passing it through the lead, to cut copying loss.
- The authors say multi-agent fits breadth-first research and fits badly where all agents must share one context, including most coding. State which case fits your system.

## Slide 16

### BEFORE

This is the board exercise. Nine rows, each answered from the post and nothing else; where the post is silent, the row is a question, and the governance row is one. Ask the room where a human stands between a subagent's finding and the report, and whether the citation agent is a receipt or a second claim. Then close with the judgment loop: the decision was parallel subagents; it privileges breadth and speed; it costs about fifteen times the tokens; the failure mode is a relayed finding treated as fact; the preservation mechanism is the citation step. This is the shape I expect in the Sprint's Design Analysis.

Cut from slide 16 (full wording):
- The lead saves its plan to memory because context past 200,000 tokens is truncated; outputs go to a filesystem.

### AFTER

This is the board exercise. Nine rows, each answered from the post and nothing else; where the post is silent, the row is a question, and the governance row is one. The question for the room is where a human stands between a subagent's finding and the report, and whether the citation agent is a receipt or a second claim. The judgment loop closes the exercise: the decision was parallel subagents; it privileges breadth and speed; it costs about fifteen times the tokens; the failure mode is a relayed finding treated as fact; the preservation mechanism is the citation step. This is the shape I expect in the Sprint's Design Analysis.

Cut from slide 16 (full wording):
- The lead saves its plan to memory because context past 200,000 tokens is truncated; outputs go to a filesystem.

## Slide 17

### BEFORE

A counterpoint from the same month. Cognition's position is that parallel subagents make hidden decisions that conflict, and the fix is one agent with full context. Read it next to Anthropic's post and they agree more than the titles suggest: split work that splits cleanly, keep work that carries decisions in one thread. Notice what this means for your adversary: it is the one agent you want to share nothing with the worker, because its job is to have different blind spots, not to continue the work.

Cut from slide 17 (full wording):
- Mechanism. Two subagents given parts of one task make decisions the other cannot see. Yan's example: one builds a background in the wrong visual style, the other a bird that matches neither, and the lead cannot reconcile them. / Design choice. One single-threaded agent with continuous context; compress history with a model when the window runs out. / Reading it against Anthropic's post. The two do not conflict. Research is breadth-first and splits cleanly; coding carries decisions forward. Your Sortie 9 does not ask you to parallelize anything; it asks you to check one claim with an agent that shares nothing with the worker.

### AFTER

A counterpoint from the same month. Cognition's position is that parallel subagents make hidden decisions that conflict, and the fix is one agent with full context. Read next to Anthropic's post, the two agree more than the titles suggest: split work that splits cleanly, and keep work that carries decisions in one thread. For your adversary this means it is the one agent that should share nothing with the worker, because its job is to bring different blind spots rather than to continue the work.

Cut from slide 17 (full wording):
- Mechanism. Two subagents given parts of one task make decisions the other cannot see. Yan's example: one builds a background in the wrong visual style, the other a bird that matches neither, and the lead cannot reconcile them. / Design choice. One single-threaded agent with continuous context; compress history with a model when the window runs out. / Reading it against Anthropic's post. The two do not conflict. Research is breadth-first and splits cleanly; coding carries decisions forward. Sortie 9 requires no parallel work: you check one claim with an agent that shares nothing with the worker.

## Slide 18

### BEFORE

A2A at version one. I checked the release page and the Linux Foundation announcement this week. The model has not changed since E5: an agent card, a task with states, artifacts back. Version one added signed agent cards, a task list method, modern OAuth flows, multi-tenancy, and a cleaner split between protocol and transport. The third card is the one to remember: opacity is a design principle, so you will never see the peer's receipts. A signature tells you who sent the artifact. It does not tell you the artifact is true. In your ledger it is a claim with a verified sender, and it gets the same treatment as your own worker's claim.

Cut from slide 18 (full wording):
- A client agent reads the remote agent's Agent Card (identity, skills, endpoint, auth) and sends a task. The task moves through states: working, input-required, auth-required, and completed, failed, canceled, or rejected. Results come back as Artifacts made of Parts.
- Signed Agent Cards / tasks/list with filtering and paging / OAuth 2.0 device-code and PKCE flows / Multi-tenancy; the application protocol separated from transport bindings / SDKs in Python, JavaScript, Java, Go, .NET
- The spec: agents collaborate “without needing access to each other's internal state, memory, or tools.” You never see the peer's receipts. A signed card proves who sent the artifact, not that the artifact is true.
- Design consequence: an A2A artifact enters your ledger as a claim with a verified sender. Re-run whatever you can, and send the rest to your adversary.

### AFTER

A2A at version one. The model has not changed since E5: an agent card, a task with states, artifacts back. Version one added signed agent cards, a task list method, modern OAuth flows, multi-tenancy, and a cleaner split between protocol and transport. The third card carries the design consequence: opacity is a design principle, so you never see the peer's receipts. A signature proves who sent the artifact and says nothing about whether the artifact is true. In your ledger it is a claim with a verified sender, and it gets the same treatment as your own worker's claim.

Cut from slide 18 (full wording):
- A client agent reads the remote agent's Agent Card (identity, skills, endpoint, auth) and sends a task. The task moves through states: working, input-required, auth-required, and completed, failed, canceled, or rejected. Results come back as Artifacts made of Parts.
- Signed Agent Cards / tasks/list with filtering and paging / OAuth 2.0 device-code and PKCE flows / Multi-tenancy; the application protocol separated from transport bindings / SDKs in Python, JavaScript, Java, Go, .NET
- The spec: agents collaborate “without needing access to each other's internal state, memory, or tools.” You never see the peer's receipts. A signed card proves the sender's identity only; the artifact's content still needs a check.
- Design consequence: an A2A artifact enters your ledger as a claim with a verified sender. Re-run whatever you can, and send the rest to your adversary.

## Slide 19

### BEFORE

Marketplaces and contracts, from the chapter's three requirements: identity, attestation, liability, with authorization split out because a protocol now exists for it. Identity is partly built with signed cards. Authorization is where AP2 goes: signed mandates that prove what the user approved for a purchase, and it lists authorization, authenticity, and accountability as the problems it solves. Attestation of work is the gap: nothing crosses an agent boundary that proves the tests ran. Liability ends where it always has, in contracts between people. The strip is why this course keeps the receipt in your harness.

Cut from slide 19 (full wording):
- Proof that a human granted this agent this scope. AP2 (announced Sep 2025) uses mandates: signed, tamper-evident credentials for a checkout and a payment.
- Proof that the work was done as claimed. Not built in any protocol here: no standard receipt for “tests pass” crosses an agent boundary.
- Who answers when the agent is wrong. AP2 names accountability as one of its three problems; the answer is still contracts between people.
- The protocols can prove who sent a claim and what the human allowed. Proving that the work was done is still your harness's job.

### AFTER

Marketplaces and contracts, from the chapter's three requirements, identity, attestation, and liability, with authorization split out because a protocol now exists for it. Signed cards build identity in part. Authorization is where AP2 goes: signed mandates that prove what the user approved for a purchase, and it lists authorization, authenticity, and accountability as the problems it solves. Attestation of work is the gap, because nothing that crosses an agent boundary proves the tests ran. Liability stays in contracts between people. For this reason the course keeps the receipt in your harness.

Cut from slide 19 (full wording):
- Proof that a human granted this agent this scope. AP2 (announced Sep 2025) uses mandates: signed, tamper-evident credentials for a checkout and a payment.
- Proof that the work was done as claimed. Not built in any protocol here: no standard receipt for “tests pass” crosses an agent boundary.
- Who answers when the agent is wrong. AP2 lists accountability as one of its three problems; the answer is still contracts between people.
- The protocols can prove who sent a claim and what the human allowed. Your harness still has to prove that the work was done.

## Slide 20

### BEFORE

The first of three dated episodes, all from the casebook. In May the reference design ran a chain of subagents ten deep, and each layer's polished summary became the next layer's fact. No single agent lied; the chain fabricated anyway, because nobody went back to the evidence. What resulted was a set of rules and the sentence that frames tonight. Read it with MAST: misalignment plus verification of the wrong object. Verify the details against the repository before class.

Cut from slide 20 (full wording):
- What happened. A chain of subagents ten deep, each summarizing the layer below it. Polished summaries were treated as facts by the layer above, and by the end nobody in the chain had looked at the primary evidence. / What resulted. The DO IT RIGHT rules, and the sentence above as doctrine. It is the origin of this week's framing and of Sortie 9's first falsifier. / MAST reading. FC2 (information passed without checking) and FC3 (verification of the summary, not the work). Appendix C #3 fabrication, without any single agent lying. / [Verify the date, the depth, and the rule's wording against AGENTS.md § Operator Doctrine and the insights corpus before class.]

Instructor checks moved off the slide:
- [Verify the date, the depth, and the rule's wording against AGENTS.md § Operator Doctrine and the insights corpus before class.]

### AFTER

The first of three dated episodes, all from the casebook. In May the reference design ran a chain of subagents ten deep, and each layer's polished summary became the next layer's fact. No single agent lied; the chain fabricated anyway, because nobody went back to the evidence. What resulted was a set of rules and the sentence that frames this Evolution. Read it with MAST: misalignment plus verification of the wrong object.

Cut from slide 20 (full wording):
- What happened. A chain of subagents ten deep, each summarizing the layer below it. Polished summaries were treated as facts by the layer above, and by the end nobody in the chain had looked at the primary evidence. / What resulted. The DO IT RIGHT rules, and the sentence above as doctrine. It is the origin of this Evolution's framing and of Sortie 9's first falsifier. / MAST reading. FC2 (information passed without checking) and FC3 (verification of the summary, not the work). Appendix C #3 fabrication, without any single agent lying. / [Verify the date, the depth, and the rule's wording against AGENTS.md § Operator Doctrine and the insights corpus before class.]

Instructor checks moved off the slide:
- [Verify the date, the depth, and the rule's wording against AGENTS.md § Operator Doctrine and the insights corpus before class.]

## Slide 21

### BEFORE

The June episodes. On the thirteenth an attestation was attributed to the operator who never gave it, which is hallucinated authorization in the plainest form, and it produced the first repudiation and an ADR. Three days later four briefs were attested for components that did not exist, which is fabrication at the gate. The chapter counts seven repudiations that month. The mechanism the reference design built is a repudiate verb that appends, never erases, so the ledger holds both the false attestation and its withdrawal. Your version is simpler: if a later check refutes something you logged, append the correction. Verify the ADR number and the count before class.

Cut from slide 21 (full wording):
- 2026-06-13. A Gate-5 attestation was attributed to the operator, who had never given it. The first repudiation; ADR-0.0.71. / 2026-06-16. Four briefs were attested for a renderer, a validator, a composer, and a playback store. None existed as attested. More repudiations; the enforcement-claim rule. / Chapter 18 counts seven Gate-5 repudiations in June. / [Verify the count, ADR-0.0.71, and the dates against the ADR index and ledger before class.]
- Failure modes. #7 hallucinated authorization (the June 13 case) and #3 fabrication (June 16), inside a multi-agent pipeline where each stage trusted the one before. / What the reference design did. It made withdrawal a recorded act: gz obpi repudiate appends a repudiation to the ledger; it does not erase the attestation. The history keeps both. / For your system. If an adversary later refutes something you logged as PASS, you append a correction to the ledger and the flight log. You never edit the old line.

Instructor checks moved off the slide:
- [Verify the count, ADR-0.0.71, and the dates against the ADR index and ledger before class.]

### AFTER

The June episodes. On the thirteenth a pipeline stage attributed a Gate-5 attestation to the operator, who never gave it, which is hallucinated authorization in the plainest form, and it produced the first repudiation and an ADR. Three days later a stage attested four briefs for components that did not exist, which is fabrication at the gate. The chapter counts seven repudiations that month. The mechanism the reference design built is a repudiate verb that appends and never erases, so the ledger holds both the false attestation and its withdrawal. Your version is simpler: if a later check refutes something you logged, append the correction.

Cut from slide 21 (full wording):
- 2026-06-13. A Gate-5 attestation was attributed to the operator, who had never given it. The first repudiation; ADR-0.0.71. / 2026-06-16. Four briefs were attested for a renderer, a validator, a composer, and a playback store. None existed as attested. More repudiations; the enforcement-claim rule. / Chapter 18 counts seven Gate-5 repudiations in June. / [Verify the count, ADR-0.0.71, and the dates against the ADR index and ledger before class.]
- Failure modes. #7 hallucinated authorization (the June 13 case) and #3 fabrication (June 16), inside a multi-agent pipeline where each stage trusted the one before. / What the reference design did. It made withdrawal a recorded act: gz obpi repudiate appends a repudiation to the ledger; it does not erase the attestation. The history keeps both. / For your system. If an adversary later refutes something you logged as PASS, you append a correction to the ledger and the flight log. You never edit the old line.

Instructor checks moved off the slide:
- [Verify the count, ADR-0.0.71, and the dates against the ADR index and ledger before class.]

## Slide 22

### BEFORE

The third episode, from August. The gate looked for a marker file and found one, left over from earlier work, and three hundred and fifty lines went in with no dispatch and no review. The rule that came out of it is the best single sentence in the casebook for this week: a presence check tells you something is armed, never that the procedure ran. The third card lists the reference design's mechanisms you are copying at small scale: a dispatch record per task, a lock verb, a model map for routing, and the Step 4b adversary with Codex preferred and degraded mode declared when there is only one vendor. A claim with no receipt is your system's marker file. Verify the figures and names before class.

Cut from slide 22 (full wording):
- Presence is not procedure: a marker file licensed work that no worker was dispatched to do and no reviewer read
- The pipeline gate checked only that a marker file existed. A stale marker licensed about 350 lines with no dispatch and no review. Stage 2 of the pipeline (implement, with dispatch per task and two-stage review) never ran.
- The rule: “A presence check answers ‘is something armed’, never ‘did the procedure run’.” The gate must read the record of the procedure, not the existence of a file.
- gz obpi dispatch: a dispatch record per task (“credit is never inferred”) / gz obpi lock: who may work on what / DISPATCH_MODEL_MAP: routing by role / Step 4b: Codex preferred as tier-1 adversary; one vendor = degraded mode, said aloud
- [Verify the ~350-line figure, the verbs, and DISPATCH_MODEL_MAP against the repository before class.] Test point 1 on your card is the same check: a claim with no receipt is a marker file.

Instructor checks moved off the slide:
- [Verify the ~350-line figure, the verbs, and DISPATCH_MODEL_MAP against the repository before class.]

### AFTER

The third episode, from August. The gate looked for a marker file and found one, left over from earlier work, and three hundred and fifty lines went in with no dispatch and no review. The rule that came out of it is the casebook sentence this Evolution rests on: a presence check tells you something is armed, never that the procedure ran. The third card lists the reference design's mechanisms you are copying at small scale: a dispatch record per task, a lock verb, a model map for routing, and the Step 4b adversary, with Codex preferred and degraded mode declared when there is only one vendor. Test point 1 on your card is the same check, because a claim with no receipt plays the part the marker file played.

Cut from slide 22 (full wording):
- Presence is not procedure: a marker file licensed work that no worker was dispatched to do and no reviewer read
- The pipeline gate checked only that a marker file existed. A stale marker licensed about 350 lines with no dispatch and no review. Stage 2 of the pipeline (implement, with dispatch per task and two-stage review) never ran.
- The rule: “A presence check answers ‘is something armed’, never ‘did the procedure run’.” The gate must read the record of the procedure, because a file's existence says nothing about whether the procedure ran.
- gz obpi dispatch: a dispatch record per task (“credit is never inferred”) / gz obpi lock: who may work on what / DISPATCH_MODEL_MAP: routing by role / Step 4b: Codex preferred as tier-1 adversary; one vendor = degraded mode, said aloud
- [Verify the ~350-line figure, the verbs, and DISPATCH_MODEL_MAP against the repository before class.] Test point 1 on your card is the same check: a claim with no receipt fails for the same reason a bare marker file does.

Instructor checks moved off the slide:
- [Verify the ~350-line figure, the verbs, and DISPATCH_MODEL_MAP against the repository before class.]

## Slide 23

### BEFORE

Weak: an adversary that is the worker's own model, an adversary fed the narrative, a claim copied into the log, not refuted written as verified, a lock that lives in one process, and cost described with an adjective. Sound: the falsehood named on the card before Go and hidden from the adversary, a harness-written receipt, a named second family that cites a receipt field, a true-claim control that passes, a real file lock with its events, and a cost table against a budget. Exceptional: a second falsehood that only reading the code can catch, the tier comparison, the crashed-holder case, a router that downgrades at the budget line, and a MAST mode reproduced on purpose.

Cut from slide 23 (full wording):
- Adversary is the worker's model with a “critic” prompt, written up as cross-family / Adversary is handed the worker's summary instead of the receipt / “Tests pass” copied from the worker into the flight log / NOT-REFUTED written as “verified” / Lock is a dict in one process; no TTL; no ledger events / Cost reported as “cheap”; no per-call numbers
- Planted falsehood named on the card before Go; the adversary is never told / Receipt written by the harness: command, exit code, commit, output hash / Adversary from a named second family; REFUTED cites a receipt field / True-claim control returns NOT-REFUTED / Atomic file lock with TTL; acquire, deny, and expire each in the ledger / Route table in config; cost table per call and per sortie against a declared budget
- Two planted falsehoods, one checkable only by reading code; result for each / Adversary run at tier 1 and tier 2 on the same claim; verdicts compared / Holder killed mid-task; TTL expiry and reclaim in order in the ledger / Router drops to a cheaper tier at the budget line, and the switch is logged / One MAST mode reproduced on purpose and coded in the debrief

### AFTER

Weak: an adversary that is the worker's own model, an adversary fed the narrative, a claim copied into the log, not refuted written as verified, a lock that lives in one process, and cost described with an adjective. Sound: the falsehood stated on the card before Go and hidden from the adversary, a harness-written receipt, a disclosed second family that cites a receipt field, a true-claim control that passes, a real file lock with its events, and a cost table against a budget. Exceptional: a second falsehood that only a reading of the code can catch, the tier comparison, the crashed-holder case, a router that downgrades at the budget line, and a MAST mode reproduced on purpose.

Cut from slide 23 (full wording):
- Adversary is the worker's model with a “critic” prompt, written up as cross-family / Adversary is handed the worker's summary instead of the receipt / “Tests pass” copied from the worker into the flight log / NOT-REFUTED written as “verified” / Lock is a dict in one process; no TTL; no ledger events / Cost reported as “cheap”, no per-call numbers
- Planted falsehood recorded on the card before Go; the adversary is never told / Receipt written by the harness: command, exit code, commit, output hash / Adversary from a disclosed second family; REFUTED cites a receipt field / True-claim control returns NOT-REFUTED / Atomic file lock with TTL; acquire, deny, and expire each in the ledger / Route table in config; cost table per call and per sortie against a declared budget
- Two planted falsehoods, one checkable only by reading code; result for each / Adversary run at tier 1 and tier 2 on the same claim; verdicts compared / Holder killed mid-task; TTL expiry and reclaim in order in the ledger / Router drops to a cheaper tier at the budget line, and the switch is logged / One MAST mode reproduced on purpose and coded in the debrief

## Slide 24

### BEFORE

Card nine, the second corner of the term. Six test points: the planted claim is recorded as unverified, the harness writes the receipt, the adversary refutes with a citation, a true claim survives, the lock denies and expires with events, and every call is routed and costed. The planted falsehood is written on the card and hidden from the adversary; the Chase's Go check confirms it is there and that the adversary's family is named. The falsifiers are the chapter's three plus the one the casebook taught: passing by telling the adversary the answer, by reusing the worker's model, or by editing a receipt is a fail. Abort is for infrastructure: the adversary's model is down or over its usage limit. Go is the Chase's signature in the repository by Saturday.

Cut from slide 24 (full wording):
- Flight Card 9 brief — Sortie 9: the planted falsehood
- Corner of the envelope · depends on Sortie 8 PASS · Go is the Chase's signature in the repo · every card names its planted falsehood

### AFTER

Card nine, the second corner of the term. Six test points: the ledger records the planted claim as unverified, the harness writes the receipt, the adversary refutes with a citation, a true claim survives, the lock denies and expires with events, and the router sends and prices every call. You write the planted falsehood on the card and hide it from the adversary, and the Chase's Go check confirms it is there and that the card states the adversary's family. The falsifiers are the chapter's three plus the one the casebook taught: passing by telling the adversary the answer, by reusing the worker's model, or by editing a receipt is a fail. Abort is for infrastructure, when the adversary's model is down or over its usage limit. Go is the Chase's signature in the repository by the course-calendar date.

Cut from slide 24 (full wording):
- Flight Card 9 brief: Sortie 9, the planted falsehood
- Corner of the envelope · depends on Sortie 8 PASS · Go is the Chase's signature in the repo · every card states its planted falsehood

## Slide 25

### BEFORE

The lab brief. It runs without me at six. You build a tiny module with one failing test, a worker report that lies about it, and a receipt script. Then three rounds against a second-family adversary: the claim alone, the claim with the receipt, and a true claim as the control. Round A is the lesson: an honest adversary without evidence should say it cannot refute, and a dishonest one will guess. Round B should refute and cite a receipt field, and you check the citation yourself, because the adversary's verdict is also a claim. You finish with the cost from opencode stats. Nothing needs a local model; free Zen models cover students without a Go subscription.

Cut from slide 25 (full wording):
- Lab (6:00–6:30): plant a falsehood, refute it with a receipt
- 0–4   Scratch folder evolution-09/lab/: an 8-line module, 3 tests (one fails), and a worker report that says 3/3 pass. / 4–9   Receipt: a 21-line script runs the tests and writes receipt.json (cmd, exit code, commit, hash). / 9–14  Round A: the adversary (other family) gets the claim only. Record its verdict. / 14–20 Round B: the adversary gets the claim and the receipt. Record its verdict and what it cites; check the citation yourself. / 20–25 Control: a true claim with its receipt. Record; then opencode stats for the cost. / 25–30 Worksheet, commit, ledger event.
- evolution-09/lab/: the files, receipt.py, receipt.json / .opencode/agents/adversary.md (reused in the sortie) / evolution-09/lab/adversary-log.md: model ids and families, three verdicts, your check of each citation, the cost line / A ledger event recording the commit / No Go subscription: use a free Zen model from a named family. Ollama is optional; nothing needs it. / The lesson to watch for in Round A: an honest adversary with no evidence cannot refute anything.

### AFTER

The lab brief. The lab is self-guided. You build a tiny module with one failing test, a worker report that lies about it, and a receipt script. Then you run three rounds against a second-family adversary: the claim alone, the claim with the receipt, and a true claim as the control. Round A is the lesson: an honest adversary without evidence should say it cannot refute, and a dishonest one will guess. Round B should refute and cite a receipt field, and you check the citation yourself, because the adversary's verdict is also a claim. You finish with the cost from opencode stats. Nothing needs a local model; free Zen models cover students without a Go subscription.

Cut from slide 25 (full wording):
- Lab: plant a falsehood, refute it with a receipt
- Scratch folder evolution-09/lab/: an 8-line module, 3 tests (one fails), and a worker report that says 3/3 pass. / Receipt: a 21-line script runs the tests and writes receipt.json (cmd, exit code, commit, hash). / Round A: the adversary (other family) gets the claim only. Record its verdict. / Round B: the adversary gets the claim and the receipt. Record its verdict and what it cites. Check the citation yourself. / Control: a true claim with its receipt. Record the verdict, then run opencode stats for the cost. / Worksheet, commit, ledger event.
- evolution-09/lab/: the files, receipt.py, receipt.json / .opencode/agents/adversary.md (reused in the sortie) / evolution-09/lab/adversary-log.md: model ids and families, three verdicts, your check of each citation, the cost line / A ledger event recording the commit / No Go subscription: use a free Zen model from a disclosed family. Ollama is optional; nothing needs it. / The lesson to watch for in Round A: an honest adversary with no evidence cannot refute anything.

## Slide 26

### BEFORE

The Sprint, with days. Friday the card goes in, adapted to your system, with the planted falsehood and both families named. Saturday your Chase reads only the card and signs Go or No-Go in the file; no Go, no sortie. Over the weekend you build and fly all six test points in one sitting and commit the log by Tuesday night. Wednesday the Chase reads the receipts and the ledger slice, not your story, and writes the verdict by six; you finish the Design Analysis and the AI_LOG entry and submit by midnight. The brief has the acceptance test for each file.

Cut from slide 26 (full wording):
- The Sprint: Sortie 9, due Wed 11/04, 11:59 p.m.
- Fri 10/30: card
- Sat 10/31: Chase Go
- Sun–Tue: fly
- Wed 11/04: verdict
- Adapt Card 9 to your system in evolution-09/flight-card.md. Name the planted falsehood, both model families, the budget. Commit; tag your Chase in the PR or issue.
- The Chase reads the card only and writes GO or NO-GO with one reason under CHASE. No Go, no sortie.
- Build the adversary, receipts, lock, route table. Fly TP1–6 in one sitting. Commit the flight log and cost table by Tue 11/03.
- The Chase reads receipts and the ledger slice and writes PASS or FAIL by 6:00 p.m. You add the Design Analysis and AI_LOG and submit by 11:59 p.m.

### AFTER

The Sprint, in four steps. First the card goes in, adapted to your system, with the planted falsehood and both families stated. Then your Chase reads only the card and signs Go or No-Go in the file; the sortie does not fly without a Go. Then you build and fly all six test points in one sitting and commit the log. Then the Chase reads the receipts and the ledger slice, and not your story, and writes the verdict; you finish the Design Analysis and the AI_LOG entry and submit. The brief has the acceptance test for each file.

Cut from slide 26 (full wording):
- The Sprint: Sortie 9
- Card
- Chase Go
- Fly
- Verdict
- Adapt Card 9 to your system in evolution-09/flight-card.md. State the planted falsehood, both model families, the budget. Commit; tag your Chase in the PR or issue.
- The Chase reads the card only and writes GO or NO-GO with one reason under CHASE. Without a GO, the sortie does not fly.
- Build the adversary, receipts, lock, route table. Fly TP1–6 in one sitting. Commit the flight log and cost table.
- The Chase reads receipts and the ledger slice and writes PASS or FAIL. You add the Design Analysis and AI_LOG and submit.

## Slide 27

### BEFORE

Close. A subagent's claim is a sentence; the receipt your harness wrote is the evidence; and the only way to know your adversary works is to plant something false and watch it get caught. Cards by Friday, Go by Saturday, verdicts by Wednesday. Sources checked 09/24/2026: arxiv.org/abs/2503.13657 and arxiv.org/html/2503.13657v3 (MAST); neurips.cc/virtual/2025/poster/121528; anthropic.com/engineering/multi-agent-research-system; cognition.com/blog/dont-build-multi-agents; github.com/a2aproject/A2A/releases; a2a-protocol.org/latest/specification; linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year; ap2-protocol.org; arxiv.org/abs/2406.18665 and lmsys.org/blog/2024-07-01-routellm (RouteLLM); arxiv.org/abs/2305.05176 (FrugalGPT); arxiv.org/abs/2404.13076 (self-preference); opencode.ai/docs/go, opencode.ai/docs/zen, opencode.ai/docs/agents, opencode.ai/docs/cli. gzkit episodes are from the course topic guide, Appendix G and chapter 18; verify against the repository.

Cut from slide 27 (full wording):
- A claim is a sentence. A receipt is evidence. Plant the lie and make your adversary find it.
- Before Saturday: the card, with the falsehood you will plant and the family of the model that must refute it. After Wednesday: a flight log in which every PASS points at a receipt.

### AFTER

Close. A subagent's claim is a sentence, the receipt your harness wrote is the evidence, and the one test of your adversary is a planted falsehood that it catches. Sources: arxiv.org/abs/2503.13657 and arxiv.org/html/2503.13657v3 (MAST); neurips.cc/virtual/2025/poster/121528; anthropic.com/engineering/multi-agent-research-system; cognition.com/blog/dont-build-multi-agents; github.com/a2aproject/A2A/releases; a2a-protocol.org/latest/specification; linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year; ap2-protocol.org; arxiv.org/abs/2406.18665 and lmsys.org/blog/2024-07-01-routellm (RouteLLM); arxiv.org/abs/2305.05176 (FrugalGPT); arxiv.org/abs/2404.13076 (self-preference); opencode.ai/docs/go, opencode.ai/docs/zen, opencode.ai/docs/agents, opencode.ai/docs/cli. The gzkit episodes are from the course topic guide, Appendix G, and chapter 18.

Cut from slide 27 (full wording):
- A claim stays a sentence until a receipt backs it. Plant the lie and make your adversary find it.
- The card: the falsehood you will plant and the family of the model that must refute it. The flight log: every PASS points at a receipt.

