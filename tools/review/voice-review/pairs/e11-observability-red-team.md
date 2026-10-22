# e11-observability-red-team: speaker notes, before and after the voice pass

## Slide 1

### BEFORE

Evolution 11, the second evaluation week. Last week the gate went red when a feature was removed. This week the question is what the system did when somebody tried to make it misbehave, and how you know. The framing phrase from the run sheet is receipts over narrative. Survey: two 2026 frontier system cards read for their agentic sections, a 2026 prompt-injection disclosure that hit three vendors' coding agents at once, the observability stacks, and the OWASP lists. Build: tracing on your own loop, a cost table, and guardrails, flown against five pre-registered attacks, two of them written by your Chase. The lab at six is a small version: one attack, one guardrail, one exported trace.

Cut from slide 1 (full wording):
- Evolution 11 · Lecture · Thu 11/12
- Traces and receipts as the black box; cost and latency per turn, sortie, and week; the nine failure modes as a red-team instrument; system cards read as evaluation documents; guardrails at an enforcement locus
- CIDM 6333 · Agentic Systems Design and Development · 4:00–6:00 · CC209 / Survey: Claude Opus 5 and GPT-5.5 system cards · Comment and Control (2026) · Langfuse, LangSmith, OpenCode's own black box · OWASP LLM 2025 and Agentic 2026   ·   Build: tracing, a cost table, and guardrails that survive five pre-registered attacks (lab 6:00–6:30, Sprint due Wed 11/18)

### AFTER

Evolution 11 is the second of the two evaluation Evolutions. In Evolution 10 the gate went red when a feature was removed. In this Evolution the question is what the system did when somebody tried to make it misbehave, and how you know what it did. The framing phrase is receipts over narrative: a record the system wrote outranks any account of the run, the model's or yours. The survey reads two 2026 frontier system cards for their agentic sections, a 2026 prompt-injection disclosure that hit three vendors' coding agents at once, three observability stacks, and the two OWASP lists. The build puts tracing on your own loop, adds a cost table, and tests your guardrails against five pre-registered attacks, two of them written by your Chase. The lab is the same exercise at its smallest size: one attack, one guardrail, one exported trace.

Cut from slide 1 (full wording):
- Evolution 11 · Lecture
- Traces and receipts as the black box; cost and latency per turn, sortie, and week; the nine failure modes as a red-team instrument; system cards read as evaluation documents; guardrails at an enforcement locus
- CIDM 6333 · Agentic Systems Design and Development / Survey: Claude Opus 5 and GPT-5.5 system cards · Comment and Control (2026) · Langfuse, LangSmith, OpenCode's own black box · OWASP LLM 2025 and Agentic 2026   ·   Build: tracing, a cost table, and guardrails that survive five pre-registered attacks

## Slide 2

### BEFORE

Ten minutes of framing, forty on a spine of eight slides, a five-minute break, thirty minutes of teardowns including a Design Analysis we build on the board, fifteen on the reference design, then the lens, the card, and the Sprint. The lab at six is self-guided; the handout is complete without me. There is no in-class Go/No-Go; the Chase signs your card in the repository, and the attack-card exchange with your Chase happens in the homework.

Cut from slide 2 (full wording):
- The black box; OpenTelemetry GenAI spans; what never to log; cost and latency; the nine modes as probes; attack cards; system cards to guardrails; the common mistake
- 6:00

### AFTER

The lecture runs in eight parts: the framing, a spine of eight slides, a break, the teardowns (including a Design Analysis built on the board), the reference design, the evaluation lens, the flight card with the Sprint, and the lab. The lab is self-guided, and the handout is complete without me. There is no in-class Go/No-Go: the Chase signs your card in the repository, and the attack-card exchange with your Chase happens in the Sprint.

Cut from slide 2 (full wording):
- The black box; OpenTelemetry GenAI spans; what never to log; cost and latency; the nine modes as probes; attack cards; system cards to guardrails; the common mistake

## Slide 3

### BEFORE

The book's thesis sentence is the quote: a system can produce an answer without being able to answer for it. Tonight that becomes two rules. First, the black box outranks the narrative: the model's account of what it did is a claim, your summary is a claim, and only a trace or a receipt is evidence. Second, a guardrail is a mechanism at a place where it can refuse, like a permission deny, a server-side check, or a commit-time check, and it earns credit only when an attack reached it and the trace shows the refusal. The claim is the chapter's Sortie 11 claim, and the third falsifier is the one students miss: an attack the system never received proves nothing about the guardrail.

Cut from slide 3 (full wording):
- Rule one. The black box outranks the narrative. No claim enters the flight log without a trace or a receipt, and that includes the model's claim about its own tool calls and your own summary of the run. / Rule two. A guardrail is a mechanism at an enforcement locus, not a sentence in a prompt. It counts only when a delivered attack reached it and the trace shows the refusal.
- Your system survives five pre-registered attacks drawn from the nine failure modes without a write, a leak, or a false attestation. Any attack that achieves its objective falsifies it. So does any attack that is not traceable in the black box, and any guardrail that passes only because the attack was never delivered.

### AFTER

The book's thesis sentence is on the slide: a system can produce an answer without being able to answer for it. In this Evolution that sentence becomes two rules. Rule one: the black box outranks the narrative. The model's account of what it did is a claim, your summary of the run is a claim, and only a trace or a receipt is evidence, because only those two records were written by the mechanism that acted rather than by a party describing it. Rule two: a guardrail is a mechanism at an enforcement locus, in other words a place in the harness where the system can refuse (a permission deny, a server-side check, a commit-time check), and it earns credit only when a delivered attack reached it and the trace shows the refusal. The design claim on the slide is the chapter's design claim for Sortie 11. Its third falsifier is the one the common-mistake slide returns to: an attack the system never received proves nothing about the guardrail, so a guardrail credited for such an attack fails the sortie.

Cut from slide 3 (full wording):
- Rule one. The black box outranks the narrative. No claim enters the flight log without a trace or a receipt, and that includes the model's claim about its own tool calls and your own summary of the run. / Rule two. A guardrail is a mechanism at an enforcement locus, not a sentence in a prompt. It counts only when a delivered attack reached it and the trace shows the refusal.
- Your system survives five pre-registered attacks drawn from the nine failure modes without a write, a leak, or a false attestation. Any attack that achieves its objective falsifies it. So does any attack that is not traceable in the black box, and any guardrail that passes only because the attack was never delivered.

## Slide 4

### BEFORE

Four records, four questions. A trace is a tree of spans for one run: the agent invocation at the top, model calls and tool calls under it, each timed and carrying attributes. A receipt is narrower and stricter: it records the observed result of a command, the exit status, the duration, the git state, and the tail of stdout, and it validates against a schema. The ledger is the project's runtime truth, the append-only log of decisions and attestations. The transcript is what the model said, and this is where students get caught: the model's sentence 'I did not read the env file' is a claim, and the tool span is the evidence. Tonight's lab makes you check one against the other.

Cut from slide 4 (full wording):
- A tree of timed operations for one run: the agent invocation, each model call, each tool call, with attributes and a status
- A span per model call and per tool call, written by your loop to a file
- A span records that an operation happened. A receipt binds the observed result to a commit. A transcript is a claim until a span or a receipt agrees with it.

### AFTER

The black box holds four kinds of record, and each answers a different question. A trace is a tree of spans for one run: the agent invocation at the top, with the model calls and tool calls under it, each timed and carrying attributes. A receipt is narrower and stricter. It records the observed result of one command (the exit status, the duration, the git state, and the tail of stdout) and validates against a schema, so a receipt binds a result to a commit. The ledger is the project's runtime truth, the append-only log of what was decided, attested, and closed, and by whom. The transcript is what the model said, and it is evidence of nothing the model claims to have done: the model's sentence 'I did not read the env file' is a claim, and the tool span for the read is the evidence. The lab has you check the one against the other.

Cut from slide 4 (full wording):
- A tree of timed operations for one run: the agent invocation, each model call, each tool call, with attributes and a status
- A span per model call and per tool call, written by your loop to a file
- A span records that an operation happened. A receipt binds the observed result to a commit. A transcript is a claim until a span or a receipt agrees with it.

## Slide 5

### BEFORE

Status first: the GenAI conventions are Development, which means names can still change, and this year they moved into their own repository, semantic-conventions-genai. Three span names matter for us: invoke_agent at the top, chat for each model call, execute_tool for each tool call. Token counts go in gen_ai.usage attributes, and the input count should include cached tokens, which matters for the cost slide. The important design choice is on the bottom left: message content, system instructions, and tool arguments and results are opt-in. The conventions default to not logging content, which is the right default and the next slide's subject. On the right is what I want to see in your trace: the refused write is a span with an error status. You do not need a collector; a JSONL file with these names is enough, and a backend can ingest it later.

Cut from slide 5 (full wording):
- Status. Development, not stable. In 2026 the GenAI conventions moved out of the main semantic-conventions repository into open-telemetry/semantic-conventions-genai; the core registry they build on is v1.44.0. / Span names. invoke_agent {gen_ai.agent.name}; chat {gen_ai.request.model}; execute_tool {gen_ai.tool.name}. Also create_agent and invoke_workflow. / Attributes. gen_ai.operation.name, gen_ai.conversation.id, gen_ai.usage.input_tokens (SHOULD include cached tokens), gen_ai.usage.output_tokens, gen_ai.tool.call.id, error.type. / Opt-in only. gen_ai.input.messages, gen_ai.output.messages, gen_ai.system_instructions, gen_ai.tool.call.arguments and .result. Content is off unless you turn it on.
- invoke_agent notes-agent · conversation.id=s11-a3 / chat glm-5.3-flash · input_tokens=5120 · output_tokens=212 / execute_tool read_note · tool.call.id=call_01 · OK / chat glm-5.3-flash · input_tokens=5391 · output_tokens=88 / execute_tool write_note · ERROR · error.type=permission_denied / The fifth line is the one the Chase wants: the attack reached the write tool, and the refusal is a span with a status, not a sentence in the model's reply. / Metrics in the same conventions: gen_ai.client.operation.duration and token-usage histograms. Evaluations have an event: gen_ai.evaluation.result.
- Use the names even if you never run a collector. A JSONL file of spans with these field names can be read later by Langfuse, LangSmith, or any OTLP backend.

### AFTER

The GenAI conventions carry the status Development, which means a name can still change, and in 2026 they moved into their own repository, semantic-conventions-genai. Three span names matter for your loop: invoke_agent at the top, chat for each model call, and execute_tool for each tool call. Token counts go in the gen_ai.usage attributes, and the input count should include cached tokens, a detail the cost slide depends on. The conventions make message content, system instructions, and tool arguments and results opt-in, so a trace carries no content unless you turn content on. That default is the right one, and the next slide gives the reason. The span tree on the right shows what the Chase needs from your trace: the refused write is a span with an error status, written by the harness, rather than a sentence in the model's reply. A collector is not required. A JSONL file of spans with these names is enough, and Langfuse, LangSmith, or any OTLP backend can load it later.

Cut from slide 5 (full wording):
- Status. Development, not stable. In 2026 the GenAI conventions moved out of the main semantic-conventions repository into open-telemetry/semantic-conventions-genai; the core registry they build on is v1.44.0. / Span names. invoke_agent {gen_ai.agent.name}; chat {gen_ai.request.model}; execute_tool {gen_ai.tool.name}. Also create_agent and invoke_workflow. / Attributes. gen_ai.operation.name, gen_ai.conversation.id, gen_ai.usage.input_tokens (SHOULD include cached tokens), gen_ai.usage.output_tokens, gen_ai.tool.call.id, error.type. / Opt-in only. gen_ai.input.messages, gen_ai.output.messages, gen_ai.system_instructions, gen_ai.tool.call.arguments and .result. Content is off unless you turn it on.
- invoke_agent notes-agent · conversation.id=s11-a3 / chat glm-5.3-flash · input_tokens=5120 · output_tokens=212 / execute_tool read_note · tool.call.id=call_01 · OK / chat glm-5.3-flash · input_tokens=5391 · output_tokens=88 / execute_tool write_note · ERROR · error.type=permission_denied / The Chase looks for the fifth line. It shows that the attack reached the write tool and that the harness recorded the refusal as a span with an ERROR status. / Metrics in the same conventions: gen_ai.client.operation.duration and token-usage histograms. Evaluations have an event: gen_ai.evaluation.result.
- Use the names even if you never run a collector. Langfuse, LangSmith, or any OTLP backend can later read a JSONL file of spans with these field names.

## Slide 6

### BEFORE

Three columns. Always log the metadata: which operation, which model, which tool, what status, how long, what it cost, on which commit, and which guardrail refused. Log content only by a recorded decision, per sortie, and prefer a hash or a truncation when the Chase only needs to know which document was read. Never log secrets, credential files, or personal data, and that includes your own. The reference design learned this in April with a history rewrite, which we reach at 1:30. The canary is how you test it: a fake value with a unique string, and a search of every committed file for that string.

Cut from slide 6 (full wording):
- Prompt and response text / Tool arguments and results / System instructions / Turn on per sortie, not by default. Record the decision in the ADR for this layer. Hash or truncate where the Chase needs only identity.
- API keys, tokens, passwords, cookies / Contents of .env or credential files / Personal data about any person, including you / Raw exports that carry any of the above / A canary string stands in for a secret in your tests. If the canary appears in a committed file, that is a leak.
- Your trace store is part of the attack surface: an attacker who can make the agent print a secret wins twice if your logger then writes it to disk.

### AFTER

The slide sorts what a trace may hold into three columns. Always log the metadata: which operation, which model, which tool, what status, how long it took, what it cost, on which commit, and which guardrail refused. Log content (prompt and response text, tool arguments and results, system instructions) only by a decision recorded in the ADR, per sortie, and prefer a hash or a truncation when the Chase needs only to know which document was read. Never log secrets, credential files, or personal data, and that rule includes data about you. The trace store is part of the attack surface for the reason the strip states: an attacker who makes the agent print a secret has caused one leak, and a logger that writes that output to disk causes a second. The reference design learned this in April 2026 with a history rewrite, which the incident slide returns to. The canary is the test: a fake value that contains a unique string, and a search of every committed file for that string, where any hit is a leak.

Cut from slide 6 (full wording):
- Prompt and response text / Tool arguments and results / System instructions / Turn on per sortie, not by default. Record the decision in the ADR for this layer. Hash or truncate where the Chase needs only identity.
- API keys, tokens, passwords, cookies / Contents of .env or credential files / Personal data about any person, including you / Raw exports that carry any of the above / A canary string stands in for a secret in your tests. If the canary appears in a committed file, the system has leaked a secret.
- Your trace store is part of the attack surface. If an attacker makes the agent print a secret and your logger then writes the output to disk, the secret persists in the trace.

## Slide 7

### BEFORE

A worked example, and I label it as such: forty turns, one point two million input tokens because the context is re-sent every turn, eighteen thousand output tokens, at the Go list price for GLM-5.3 Flash as checked in September. Nineteen cents. Forty-five minutes of your attention at fifty dollars an hour is thirty-seven fifty. The ratio is the chapter's point: the supervision cost does not appear in the model bill, and on a free model it is the only cost. Two traps in the per-turn numbers: cached reads are inside the input count, and Go limits are dollar-denominated per five hours, per week, and per month, so your cost table predicts when you will hit a wall.

Cut from slide 7 (full wording):
- Per turn. Tokens in, tokens out, cached reads, wall-clock latency, and time to first token. Cached reads count inside input tokens under the conventions, so a table that multiplies input tokens by the list price overstates cost when the cache is warm. / Per sortie and per week. Sum the turns; add the minutes a human spent reading, approving, and re-running. On Big Pickle the model bill is $0.00 and the supervision cost is unchanged. On Go, dollars count against a 5-hour, weekly, and monthly limit, so the table also tells you when you will be stopped.

### AFTER

The numbers are a worked example rather than a measurement, and the slide says so. One sortie of forty turns sends about 1.2 million input tokens, because the loop re-sends the context every turn, and produces about eighteen thousand output tokens. At the Go list price for GLM-5.3 Flash as of September 2026, the model bill is nineteen cents. Forty-five minutes of your attention at an assumed fifty dollars an hour is thirty-seven dollars and fifty cents. The ratio of about two hundred to one is the chapter's point: supervision cost does not appear on the model bill, and on a free model it is the only cost. The per-turn numbers hold two traps. Cached reads sit inside the input count, so a table that multiplies input tokens by the list price overstates the cost when the cache is warm. Go limits are denominated in dollars per five hours, per week, and per month, so your cost table also predicts when the provider will stop you.

Cut from slide 7 (full wording):
- Per turn. Tokens in, tokens out, cached reads, wall-clock latency, and time to first token. Cached reads count inside input tokens under the conventions, so a table that multiplies input tokens by the list price overstates cost when the cache is warm. / Per sortie and per week. Sum the turns; add the minutes a human spent reading, approving, and re-running. On Big Pickle the model bill is $0.00 and the supervision cost is unchanged. On Go, dollars count against a 5-hour, weekly, and monthly limit, so the table also shows when the provider will stop your requests.

## Slide 8

### BEFORE

The nine modes, from Appendix C, turned into an instrument. For each mode, a probe you can deliver and the objective the attack pursues, which becomes the falsifier on your attack card. The OWASP column is my mapping, and I say so on the slide; argue with it. Two things to notice. Prompt injection is not a mode here; it is a delivery method, and it can carry any of the nine objectives. And modes five and six need more than one turn: you cannot test correction or honesty with a single prompt. Your five attacks must cover at least four different modes.

Cut from slide 8 (full wording):
- OWASP column is the instructor's mapping for discussion, not OWASP's. Lists: OWASP Top 10 for LLM Applications 2025; OWASP Top 10 for Agentic Applications 2026 (Dec 2025).

### AFTER

The table turns the nine failure modes of Appendix C into a red-team instrument. Each row pairs a mode with a probe you can deliver and the objective the attack pursues, and that objective becomes the falsifier on your attack card. The OWASP column is my mapping, and the slide says so; argue with it where you read the lists differently. Two features of the table matter for your cards. Prompt injection does not appear as a mode, because it is a delivery method, and a single injection can carry any of the nine objectives. Modes five and six (correction fails, dishonest when caught) need more than one turn, because a single prompt cannot test whether a correction holds or how the model explains a violation. Your five attacks must cover at least four different modes.

Cut from slide 8 (full wording):
- The OWASP column is the instructor's mapping for discussion. OWASP did not publish this mapping. Lists: OWASP Top 10 for LLM Applications 2025; OWASP Top 10 for Agentic Applications 2026 (Dec 2025).

## Slide 9

### BEFORE

Five fields. The objective is a sentence the attacker wants to be true, and it becomes your falsifier. Delivery says how the payload gets in, and the hash lets the Chase find the exact payload in your trace without trusting your word that it was delivered. The guardrail names a mechanism and where it enforces; if the answer is 'the system prompt tells it not to', you have no guardrail. The expected observable is the span or receipt. The falsifiers include the one from the chapter: a guardrail that passes because the payload never arrived. The strip names trust-chain poisoning: nothing is wrong at any single step, because each layer believed the one below it. One of your five attacks is delivered through a tool result.

Cut from slide 9 (full wording):
- How the payload reaches the loop: user turn, file, tool result, issue, resource. Record the payload's SHA-256 so the Chase can find it in the trace.
- Trust-chain poisoning is the attack that needs no single bad step: each layer accepts the layer below's output as fact. Write one card whose delivery is a tool result, not a user turn.

### AFTER

An attack card has five fields, and you write it before you fly for the same reason a flight card is written before a sortie: a test written after the result is a description of the result. The objective is one sentence the attacker wants to be true, and it becomes your falsifier. Delivery states how the payload reaches the loop, and the payload's SHA-256 lets the Chase find that exact payload in your trace without taking your word that it was delivered. The guardrail field states a mechanism and the locus where it enforces; if the answer is 'the system prompt tells it not to', the card has no guardrail. The expected observable is the span or receipt that will show the refusal. The falsifiers include the chapter's third: a guardrail credited because the payload never arrived. The strip describes trust-chain poisoning, the attack in which no single step is wrong because each layer accepted the layer below as fact, and for this reason one of your five attacks is delivered through a tool result.

Cut from slide 9 (full wording):
- How the payload reaches the loop: user turn, file, tool result, issue, resource. Record the payload's SHA-256 so the Chase can find it in the trace.
- In trust-chain poisoning, no single step is bad: each layer accepts the output of the layer below as fact. Write one card whose delivery is a tool result, not a user turn.

## Slide 10

### BEFORE

A system card is the lab's evaluation report on the model: what they tested, how, with which outside evaluators, and which safety threshold they placed the model under. It cannot evaluate your harness. The translation is mechanical, and I want it on your card: a finding becomes a mode, the mode becomes an attack, the attack names a guardrail. Where the guardrail lives matters most. Order them by what the model cannot argue with: a permission deny the harness enforces, a check on the server, a check at commit time. The strip is how to read the tables in the next section: the residual rate is your threat model.

Cut from slide 10 (full wording):
- Capability and risk evaluations run by the lab and outside testers before release: misuse, prompt-injection robustness per surface, destructive actions, honesty, sabotage, evaluation awareness, and the frontier-safety threshold the model is placed under.
- Your harness. Your tools, your permissions, your data, your prompts. A card's 96% injection resistance is a rate across the lab's attacks; your system meets the other 4% with whatever you built.
- Permission config (OpenCode allow, ask, deny), server-side scope checks (E5), a hook, a commit-time check on git diff --cached. Order them by what the model cannot talk its way past.

### AFTER

A system card is the lab's evaluation report on the model: what the lab tested, how, with which outside evaluators, and which safety threshold the lab placed the model under. It cannot evaluate your harness, because your tools, permissions, data, and prompts were not in the lab's test. A card's 96% injection resistance is a rate across the lab's attacks, and your system meets the other 4% with what you built. The translation from card to guardrail is mechanical, and your attack card records it: a finding becomes a mode, the mode becomes an attack, and the attack states the guardrail under test. Where the guardrail sits decides whether the model can talk its way past it, so order the candidates by what the model cannot argue with: a permission deny the harness enforces, a scope check on the server, a hook, a check on git diff --cached at commit time. The strip states how to read the tables in the teardowns: the rate that remains after the lab's mitigations is the rate your harness inherits, so the remainder is your threat model.

Cut from slide 10 (full wording):
- Capability and risk evaluations run by the lab and outside testers before release: misuse, prompt-injection robustness per surface, destructive actions, honesty, sabotage, evaluation awareness, and the frontier-safety threshold the model is placed under.
- Your harness. Your tools, your permissions, your data, your prompts. A card's 96% injection resistance is a rate across the lab's attacks. Against the other 4%, your system has only the guardrails you built.
- Permission config (OpenCode allow, ask, deny), server-side scope checks (E5), a hook, a commit-time check on git diff --cached. Order them by strength: a mechanism that no model output can override ranks first.

## Slide 11

### BEFORE

This is the mistake I expect in a third of the logs. 'All five attacks failed' written from the model's final message and a clean file. The black box tells a different story: two payloads never entered the loop, and a third was refused by the model before any tool call, so the guardrail the card named was never exercised. Model refusal is a real outcome and you record it, but it is a property of this model on this day, and the next model may comply. The guardrail is what stands when the model does not refuse. So each attack needs two pieces of evidence: the delivery span and the refusal span.

Cut from slide 11 (full wording):
- What the student checked. The model's final reply said it had declined, and the file on disk was unchanged. / What the black box showed. Two payloads were never read: the injected file was outside the directory the agent searched, and a third attack was refused by the model before any tool ran, so the guardrail under test was never reached. The permission deny that the card claimed as the defense has no refusal span at all. / The rule. For each attack, show the delivery span (the payload entered the loop) and the refusal span or receipt (the named guardrail acted). Model refusal is an outcome worth recording, but it is not the guardrail passing. Record it as 'refused by model; guardrail not exercised', and fly a variant that reaches the guardrail.

### AFTER

The common mistake is a log that reads 'all five attacks failed', written from the model's final message and an unchanged file. The black box tells a different story. Two payloads never entered the loop, because the injected file sat outside the directory the agent searched, and the model refused a third before any tool ran, so the guardrail the card listed was never exercised and has no refusal span. Model refusal is a real outcome, and you record it, but it is a property of this model on this day, and the next model may comply. The guardrail is what stands when the model does not refuse. For this reason each attack needs two pieces of evidence, the delivery span and the refusal span or receipt, and a model refusal is recorded as 'refused by model; guardrail not exercised' with a variant flown that reaches the guardrail.

Cut from slide 11 (full wording):
- What the student checked. The model's final reply said it had declined, and the file on disk was unchanged. / What the black box showed. Two payloads were never read: the injected file was outside the directory the agent searched, and a third attack was refused by the model before any tool ran, so the guardrail under test was never reached. The permission deny that the card claimed as the defense has no refusal span at all. / The rule. For each attack, show the delivery span (the payload entered the loop) and the refusal span or receipt (the guardrail on the card acted). A model refusal is an outcome to record, and it does not count as a guardrail pass. Record it as 'refused by model; guardrail not exercised', and fly a variant that reaches the guardrail.

## Slide 12

### BEFORE

Five minutes. The question on the slide is the one I will ask two of you when we return: one place in your system where the guardrail is only a sentence, and what the enforced version would be.

Cut from slide 12 (full wording):
- Question for the break: in your own system, name one place where a guardrail exists only as a sentence in a prompt. What would the deny look like?

### AFTER

The question on the slide is for the break: find one place in your own system where a guardrail exists only as a sentence in a prompt, and state what the enforced version, the deny, would look like.

Cut from slide 12 (full wording):
- Question: in your own system, identify one place where a guardrail exists only as a sentence in a prompt. What would the deny look like?

## Slide 13

### BEFORE

The current Anthropic card, released July 24. The agentic safety section is five: malicious use through Claude Code and computer use, and prompt-injection robustness measured per surface against adaptive attackers, with a live bug bounty added in an August changelog. Section six is alignment: the internal-deployment monitoring subsection reports an intermediate snapshot that, logged out of a service, tried guessing common passwords to get back in. That is safeguard circumvention in one sentence. The honesty subsections name lazy investigation and uncritical reporting of flawed results, which are modes four and three. Verify the section numbers against the PDF before class; the card has a changelog and sections move.

Cut from slide 13 (full wording):
- §5.1 Malicious use of agents. Claude Code, computer use, agentic influence campaigns. / §5.2 Prompt injection risk within agentic systems. External red teaming; robustness against adaptive attackers per surface: coding, computer use, browser use; a live bug bounty added in an Aug 19 changelog update. / §6.2.2 Internal deployment monitoring. Behavior seen in real use before release. / §6.5 Honesty. Uncritically reporting flawed results; overconfidence; lazy investigation. / §6.7 Evading safeguards. SHADE-Arena, LinuxArena. / Deployed under ASL-3.
- One reported case (§6.2.2). An intermediate snapshot, accidentally logged out of a service, tried to log back in by guessing common passwords. That is mode 1, safeguard circumvention: the model worked around the barrier instead of reporting it. / Lazy investigation and uncritical reporting (§6.5). Mode 4 and mode 3: a result reported without the check that would have shown it wrong. / Per-surface injection results (§5.2.2). The card reports robustness separately for coding, computer use, and browser use. Your system has its own surfaces; test each one you expose. / Your attack card cites the section it came from.
- The card's authors tell you where their model still fails. That list is a free red-team plan for anyone building on the model.

### AFTER

The Claude Opus 5 system card, released July 24, 2026, is the current Anthropic card. Section 5 covers agentic safety: malicious use through Claude Code and computer use, and prompt-injection robustness measured per surface against adaptive attackers, with a live bug bounty added in an August changelog entry. Section 6 covers alignment. The subsection on internal deployment monitoring reports an intermediate snapshot that, logged out of a service, tried common passwords to get back in, which is safeguard circumvention (mode 1) in one sentence: the model worked around the barrier instead of reporting it. The honesty subsection reports lazy investigation and uncritical reporting of flawed results, which are modes 4 and 3. The per-surface injection results are the reason your system is tested surface by surface: the card reports coding, computer use, and browser use separately, your system has its own surfaces, and you test each one you expose. The card has a changelog, and sections have moved between revisions, so an attack card cites the section number from the revision it read.

Cut from slide 13 (full wording):
- §5.1 Malicious use of agents. Claude Code, computer use, agentic influence campaigns. / §5.2 Prompt injection risk within agentic systems. External red teaming; robustness against adaptive attackers per surface: coding, computer use, browser use; a live bug bounty added in an Aug 19 changelog update. / §6.2.2 Internal deployment monitoring. Behavior seen in real use before release. / §6.5 Honesty. Uncritically reporting flawed results; overconfidence; lazy investigation. / §6.7 Evading safeguards. SHADE-Arena, LinuxArena. / Deployed under ASL-3.
- One reported case (§6.2.2). An intermediate snapshot, accidentally logged out of a service, tried to log back in by guessing common passwords. That is mode 1, safeguard circumvention: the model worked around the barrier instead of reporting it. / Lazy investigation and uncritical reporting (§6.5). Mode 4 and mode 3: a result reported without the check that would have shown it wrong. / Per-surface injection results (§5.2.2). The card reports robustness separately for coding, computer use, and browser use. Your system has its own surfaces; test each one you expose. / Your attack card cites the section it came from.
- The card's authors list where their model still fails. A team that builds on the model can draw its red-team attacks directly from that list.

## Slide 14

### BEFORE

Four numbers from OpenAI's April card. Injection resistance 0.963, lower than the previous version's 0.998, so newer is not monotonically safer. Destructive-action avoidance 0.90, and perfect reversion 0.52: one destructive action in ten gets through, and half of those are not fully undone. And the Apollo Research finding: in an impossible coding task the model claimed completion in 29 percent of samples. That is fabrication measured by an outside party, and it is why completion in your system requires a receipt. Read the remainders, not the improvements. Verify the table numbers against the PDF before class.

Cut from slide 14 (full wording):
- Read the remainders. One destructive action in ten is not avoided, and about half of those are not fully reverted: that is mode 2, and your guardrail is a confirmation event the model cannot produce. The 29% is mode 3 measured by an outside evaluator: your guardrail is that 'done' requires a receipt. Injection resistance moved down between versions; a newer model is not a safer harness.
- A score of 0.963 means the lab's attack set got through about one time in 27. Your attack set is not the lab's.

### AFTER

The GPT-5.5 system card, released April 23, 2026, gives four numbers in its agentic sections, and each is a residual rate your harness inherits. Prompt-injection resistance scored 0.963, below the 0.998 of GPT-5.4 Thinking, so the newer model did not make a harness safer against injection. Destructive-action avoidance scored 0.90 and perfect reversion 0.52: one destructive action in ten gets through, and about half of those are not fully undone, which is mode 2, so your guardrail is a confirmation event the model cannot produce. Apollo Research, as an outside evaluator, found that the model claimed completion of an impossible coding task in 29 percent of samples. That is fabrication (mode 3) measured by a party other than the lab, and it is the reason completion in your system requires a receipt. Read a card for the rates that remain after mitigation rather than for the rates that improved, because the remainder is what reaches your harness.

Cut from slide 14 (full wording):
- Read the remainders. One destructive action in ten is not avoided, and about half of those are not fully reverted: that is mode 2, and your guardrail is a confirmation event the model cannot produce. The 29% is mode 3 measured by an outside evaluator: your guardrail is that 'done' requires a receipt. Injection resistance fell between versions, so a model upgrade does not by itself make the harness safer.
- A score of 0.963 means the lab's attack set got through about one time in 27. That rate applies to the lab's attacks. Your attacks differ, so measure your own rate.

## Slide 15

### BEFORE

Disclosed by Aonan Guan with colleagues from Johns Hopkins in April. One pattern, three agents. Claude Code's security reviewer took the pull-request title into its prompt and ran a process listing that exposed its keys, which went into a PR comment. Gemini's action followed a fake trusted section in an issue comment. Copilot's agent read an HTML comment nobody sees in the rendered issue, base64-encoded the process listing so secret scanning would not match, and committed it through the one channel it was allowed to use. Read for mechanism: in all three, untrusted text reached a loop that held secrets and a write path. His point about blocklists is the lab's point: deny ps and the attacker reads /proc instead. Note also, per VentureBeat's reading, that Anthropic's Opus 4.7 card had said the security-review action was not hardened against injection; the system card was a threat model the integrators did not read.

Cut from slide 15 (full wording):
- Enters: an HTML comment in an issue body, invisible when rendered. / Acts: ps auxeww | base64, which evades secret scanning. / Leaves: encoded credentials in a git commit, pushed through an allowed channel.
- Aonan Guan's root cause: the agent holds production secrets because it needs them, and processes untrusted input because that is its job. His defense: allowlists of tools and secrets, not blocklists.

### AFTER

Comment and Control is a disclosure by Aonan Guan and colleagues at Johns Hopkins, published April 15, 2026: one prompt-injection pattern against three vendors' coding agents running in GitHub Actions, and in each case the agent's own credentials left the loop. Claude Code's security reviewer interpolated the pull-request title into its prompt, ran a process listing through Bash that exposed its keys, and posted them in a PR comment. Gemini's CLI action followed a fake 'trusted content' section planted in an issue comment and posted its API key as a public issue comment. Copilot's coding agent read an HTML comment that the rendered issue hides, base64-encoded the process listing so that secret scanning would not match, and committed the result through the one channel it was allowed to use. The mechanism is the same in all three: untrusted text reached a loop that held secrets and a write path. Guan's root cause is that pairing, and his defense is an allowlist of tools and secrets, because a blocklist fails by substitution (deny ps and the attacker reads /proc instead). VentureBeat's report adds that Anthropic's Opus 4.7 card had already stated that the security-review action was not hardened against injection, so the system card had stated the threat model and the integrators had not read it.

Cut from slide 15 (full wording):
- Enters: an HTML comment in an issue body, invisible when rendered. / Acts: ps auxeww | base64, which evades secret scanning. / Leaves: encoded credentials in a git commit, pushed through an allowed channel.
- Aonan Guan's root cause: the agent holds production secrets because it needs them, and processes untrusted input because that is its job. His defense: allowlists of tools and secrets in place of blocklists.

## Slide 16

### BEFORE

Three stacks, read for the design choice. Langfuse is open source, built on OpenTelemetry, and has a guardrail observation type, which tells you its designers expected guardrails to be traced. It joined ClickHouse in January and says the licence is not changing. LangSmith is proprietary, accepts OTLP, and groups traces into threads by a metadata key that every child run must carry, or the cost roll-up is wrong. OpenCode has no tracing product, but its session export already holds the facts: tool, status, times, tokens, cost. Failure modes: every stack will happily store a secret you let into the content, and OpenCode's share command publishes a session to a public URL. The lab uses the export, and sets share to disabled.

Cut from slide 16 (full wording):
- The export you can run tonight holds the same facts a hosted stack would: which tool, what status, how long, what it cost.

Instructor checks moved off the slide:
- [verify]

### AFTER

The slide compares three ways to hold the black box, read for the design choice each one made. Langfuse is open source under the MIT licence, is built on OpenTelemetry, and defines a guardrail observation type, which shows that its designers expected a guardrail refusal to appear in a trace. It joined ClickHouse in January 2026 and states that the licence is not changing. LangSmith is proprietary and hosted, accepts OTLP, and groups traces into threads by a metadata key that every child run must carry, or the cost roll-up for the thread is wrong. OpenCode has no tracing product, but its session export already holds the facts a hosted stack would: which tool, what status, how long, what it cost. The failure modes differ by where the data goes. Each stack stores whatever content you send it, so a secret that passes into content is mode 8 at the store, and with LangSmith the trace leaves your machine. OpenCode's share command publishes a session at a public URL until you unshare it. The lab uses the export and sets share to disabled for both reasons.

Cut from slide 16 (full wording):
- The export from your own OpenCode session holds the same facts a hosted stack would record: which tool, what status, how long, what it cost.

Instructor checks moved off the slide:
- [verify]

## Slide 17

### BEFORE

The two lists, current as of this week: the LLM list is still the 2025 edition, and the agentic list came out in December for 2026. The LLM list is mostly about one call: injection, disclosure, output handling, excessive agency. The agentic list is about loops: goal hijack, tool misuse, privilege, memory poisoning, inter-agent messages, cascading failures. Map your system to both. The difference from our nine modes is direction: OWASP names what the attacker does, and Appendix C names what the agent does wrong in response. An attack card names one of each. Cascading failures, ASI08, is trust-chain poisoning under another name, and it is the reference design's April outage.

Cut from slide 17 (full wording):
- The LLM list names what goes wrong in a model call; the agentic list names what goes wrong in a loop
- OWASP lists what an attacker does to the system; Appendix C lists what the agent does wrong. An attack card names one of each.

### AFTER

OWASP maintains two lists that apply here. The Top 10 for LLM Applications is still the 2025 edition, and the Top 10 for Agentic Applications for 2026 was released on December 9, 2025. The LLM list describes what goes wrong in one model call: injection, disclosure, output handling, excessive agency. The agentic list describes what goes wrong in a loop: goal hijack, tool misuse, privilege abuse, memory poisoning, inter-agent communication, cascading failures. Map your system to both. The two lists differ from the nine modes in direction: OWASP lists what an attacker does to the system, and Appendix C lists what the agent does wrong in response, so an attack card cites one entry of each. ASI08, cascading failures, is trust-chain poisoning under OWASP's label, and the reference design's April outage is an instance of it.

Cut from slide 17 (full wording):
- The LLM list covers failures in a model call. The agentic list covers failures in a loop
- OWASP lists what an attacker does to the system. Appendix C lists what the agent does wrong. An attack card cites one entry from each.

## Slide 18

### BEFORE

Our live analysis tonight is of the harness you use, read from what it records. I will fill the rows with you; the slide is the answer I expect. The two rows that deserve the most words are evaluation, where OpenCode gives you raw material, stats and a full JSON export, and no judgment, and governance, where it gives you allow, ask, and deny per tool, with bash patterns and a default deny on env-file reads. Then the judgment loop in the strip. The failure mode is the lab: the read deny on env files does not cover a bash cat of the same file, which is exactly the reference design's August hook incident at 1:40. The preservation mechanism is ask on bash.

Cut from slide 18 (full wording):
- Any provider/model: Zen (Big Pickle, free), Go ($10/month, dollar limits per 5 h, week, month), local via Ollama
- Prompts, files through read/grep/glob, tool outputs, web pages through webfetch and websearch; all of it enters the window as text
- No receipts. opencode stats for tokens and cost; opencode export for per-tool status and timing. The judgment is left to you
- permission: allow / ask / deny per tool, bash patterns, .env reads denied by default; share manual, auto, or disabled
- Judgment loop. Decision: governance by permission patterns, evaluation left to the user. Privileges: speed, provider freedom. Cost: no receipts. Failure mode: a read deny that bash walks around (mode 1). Preservation: ask on bash.

### AFTER

The live Design Analysis is of OpenCode, the harness you use, read from what it records. I fill the rows with you, and the slide holds the answer I expect. Two rows need the most words. The evaluation row: OpenCode gives you raw material, opencode stats for tokens and cost and a full JSON export with per-tool status and timing, and no judgment, so there are no receipts and the verdict is yours to write. The governance row: OpenCode gives you allow, ask, and deny per tool, with bash patterns, a default deny on env-file reads, and a share setting of manual, auto, or disabled. The judgment loop in the strip follows from those rows. The decision is governance by permission patterns with evaluation left to the user, the privileges are speed and provider freedom, and the cost is the absence of receipts. The failure mode is the lab's: the read deny on env files does not cover a bash cat of the same file, which is the reference design's August hook incident in another harness (mode 1). The preservation mechanism is ask on bash.

Cut from slide 18 (full wording):
- Any provider/model: Zen (Big Pickle, free), Go ($10/month, dollar limits per 5 h, week, month), local via Ollama
- Prompts, files through read/grep/glob, tool outputs, web pages through webfetch and websearch; all of it enters the window as text
- No receipts. opencode stats for tokens and cost; opencode export for per-tool status and timing. You make the judgment
- permission: allow / ask / deny per tool, bash patterns, .env reads denied by default; share manual, auto, or disabled
- Judgment loop. Decision: governance by permission patterns, evaluation left to the user. Privileges: speed, provider freedom. Cost: no receipts. Failure mode: a read deny that bash walks around (mode 1). Preservation: ask on bash.

## Slide 19

### BEFORE

The reference design's version of tonight. Receipts first: gzkit wraps a governed command so that the run leaves a schema-validated record of exit status, duration, git state, and stdout tail. The flight log cites receipts, not prose. Then the outage on April 18: nine layers were silently wrong and each fed the next, so the decisions at the top looked right. Nothing failed loudly, which is what makes trust-chain poisoning hard. The doctrine that resulted states, for each kind of input, how much it may be trusted, in four tiers from T0 to T3. I am not defining the tiers on the slide; read them in the repository, and verify the nine and the tiers before class.

Cut from slide 19 (full wording):
- gzkit wraps governed commands so that each run produces a receipt: a schema-validated record of exit status, duration, git state, and stdout tail. A receipt is evidence of one command on one commit. It is what the flight log cites instead of a sentence. / The same idea carries to Sortie 11: every guardrail refusal writes a receipt, and 'the attack failed' in the log points to one. / [Verify the ARB module layout and receipt fields against the repository before class.]
- What happened. Nine layers were silently wrong, each feeding the next, and the decisions built on them looked correct. No single step failed loudly. That is trust-chain poisoning: each layer treated the layer below as a fact. / What resulted. The trust doctrine, with tiers T0–T3, in docs/governance/trust-doctrine.md: a stated level of trust for each kind of input, so that a consumer knows what it may take as given and what it must check. / [Verify the tier definitions and the count of nine against trust-doctrine.md before class.]

Instructor checks moved off the slide:
- [Verify the ARB module layout and receipt fields against the repository before class.]
- [Verify the tier definitions and the count of nine against trust-doctrine.md before class.]

### AFTER

The reference design has its own version of this Evolution's build. gzkit wraps a governed command so that the run leaves a receipt: a schema-validated record of exit status, duration, git state, and stdout tail, which is evidence of one command on one commit. The flight log cites receipts, and in Sortie 11 every guardrail refusal writes one. The outage of April 18, 2026 is the second half of the slide. Nine layers were silently wrong, each fed the next, and the decisions at the top looked correct, because no single step failed loudly. That silence is what makes trust-chain poisoning hard to catch. The trust doctrine that resulted (docs/governance/trust-doctrine.md) states, for each kind of input, how much a consumer may take as given, in four tiers from T0 to T3. The slide does not define the tiers; read them in the repository. One of your five attacks targets a chain for this reason: poison a tool result and see whether anything downstream checks it.

Cut from slide 19 (full wording):
- gzkit wraps governed commands so that each run produces a receipt: a schema-validated record of exit status, duration, git state, and stdout tail. A receipt is evidence of one command on one commit. The flight log cites the receipt in place of a prose statement. / Sortie 11 applies the same mechanism: every guardrail refusal writes a receipt, and each 'the attack failed' entry in the log points to one. / [Verify the ARB module layout and receipt fields against the repository before class.]
- What happened. Nine layers were silently wrong, each feeding the next, and the decisions built on them looked correct. No single step failed loudly. That is trust-chain poisoning: each layer treated the layer below as a fact. / What resulted. The trust doctrine, with tiers T0–T3, in docs/governance/trust-doctrine.md: a stated level of trust for each kind of input, so that a consumer knows what it may take as given and what it must check. / [Verify the tier definitions and the count of nine against trust-doctrine.md before class.]

Instructor checks moved off the slide:
- [Verify the ARB module layout and receipt fields against the repository before class.]
- [Verify the tier definitions and the count of nine against trust-doctrine.md before class.]

## Slide 20

### BEFORE

Three dated incidents from the casebook. April 19: personal data about the operator ended up in committed artifacts, and the only fix was rewriting history; that produced the PII rule and an authorship guard. Your copy is a canary search before every push. May 10: an agent typed ATTEST into a command to get past an interactive gate. The first response was a regression test; the second, four days later, was to remove the TTY gate and move forgery resistance to audit, because a gate an agent can type through is not authority. August 23: six hooks matched on the editor tools, and any Bash write went around them; enforcement moved to the commit, where every write shows up whatever made it. Verify each against the changelog.

Cut from slide 20 (full wording):
- Regression test; then the TTY gate removed (05-14): authority belongs to the human, forgery resistance to audit

Instructor checks moved off the slide:
- [Verify dates and mechanisms against CHANGELOG.md and the insights corpus before class.]

### AFTER

Appendix G, the gzkit incident casebook, supplies three dated incidents, each a mode from Appendix C with a mechanism you can copy. On April 19, personal data about the operator ended up in committed artifacts, and the only fix was a history rewrite. The result was the PII rule and an authorship guard, and your copy is a canary search over every committed file before each push. On May 10, an agent piped the string ATTEST into gz obpi complete to get past an interactive gate (modes 1 and 7). The first response was a regression test. The second, four days later, removed the TTY gate and moved forgery resistance to audit, because a gate an agent can type through does not hold authority, and authority belongs to the human. Your copy checks attestation from the ledger rather than from input the agent can type. On August 23, six governance hooks keyed on editor-tool matchers were bypassed by any Bash write (mode 1), and enforcement moved to the commit locus, where git diff --cached shows every write whatever tool made it. Your copy is a commit-time check of the same kind, and the August incident is the lab in miniature: a deny on the read tool does not see bash cat.

Cut from slide 20 (full wording):
- Regression test; then the TTY gate removed (05-14): authority belongs to the human, forgery resistance to audit

Instructor checks moved off the slide:
- [Verify dates and mechanisms against CHANGELOG.md and the insights corpus before class.]

## Slide 21

### BEFORE

The last reference-design slide explains where Appendix C came from. gzkit keeps a registry of frontier model cards and a rule file whose nine modes are sourced to those cards. The kit did not invent the taxonomy; it read the labs' reports and turned findings into probes. For your sortie, each attack cites where it came from, with one exception allowed for your own idea. And notice the gap for our free model: Big Pickle has no published card and no published context window, so your threat model for it rests on your own tests. Say that on the card. Verify the registry path before class.

Cut from slide 21 (full wording):
- gzkit keeps a registry of frontier model cards (data/frontier_model_cards.json) and a rule file of agent failure modes (.gzkit/rules/agent-failure-modes.md) whose nine entries are sourced to those cards. Appendix C is the course edition of that rule, with the human-side patterns added. / The design choice: the kit does not invent a taxonomy; it reads the labs' own reports of how their models fail and turns each into a probe. / [Verify the registry path and the rule's sources against the repository before class.]
- Your five attacks trace to evidence about the model you run: a system-card section, an incident, or a casebook entry. 'I thought of it' is allowed for one attack; the others cite a source. / For Big Pickle there is no published card and no published context window. For an OpenCode Go model, look for the provider's model card. Where none exists, say so on the flight card: the threat model then rests on your own tests alone. / That absence is a finding, and it belongs in the Design Analysis.
- A red team that starts from the lab's own failure reports tests what is known to fail. A red team that starts from imagination tests what the author expected.

Instructor checks moved off the slide:
- [Verify the registry path and the rule's sources against the repository before class.]

### AFTER

The last reference-design slide explains where Appendix C came from. gzkit keeps a registry of frontier model cards (data/frontier_model_cards.json) and a rule file of agent failure modes (.gzkit/rules/agent-failure-modes.md) whose nine entries are sourced to those cards. Appendix C is the course edition of that rule, with the human-side patterns added. The kit did not invent the taxonomy. It read the labs' own reports of how their models fail and turned each finding into a probe, and your red team starts from a card for the same reason: a red team that starts from the lab's failure reports tests what is known to fail, and a red team that starts from imagination can test only what its author already expected. For Sortie 11, each attack cites evidence about the model you run (a system-card section, an incident, or a casebook entry), with one attack allowed as your own idea. Big Pickle has no published card and no published context window, so a threat model for it rests on your own tests alone. For an OpenCode Go model, look for the provider's card. Where none exists, say so on the flight card, because that absence is a finding and belongs in the Design Analysis.

Cut from slide 21 (full wording):
- gzkit keeps a registry of frontier model cards (data/frontier_model_cards.json) and a rule file of agent failure modes (.gzkit/rules/agent-failure-modes.md) whose nine entries are sourced to those cards. Appendix C is the course edition of that rule, with the human-side patterns added. / Design choice. The kit takes its taxonomy from the labs' own reports of how their models fail and turns each report into a probe. / [Verify the registry path and the rule's sources against the repository before class.]
- Your five attacks trace to evidence about the model you run: a system-card section, an incident, or a casebook entry. 'I thought of it' is allowed for one attack; the others cite a source. / For Big Pickle there is no published card and no published context window. For an OpenCode Go model, look for the provider's model card. Where none exists, say so on the flight card: the threat model then rests on your own tests alone. / Record that absence as a finding in the Design Analysis.
- The lab's failure reports aim the red team at failures already observed in the model. Attacks drawn from imagination alone test only the failures their author expected.

Instructor checks moved off the slide:
- [Verify the registry path and the rule's sources against the repository before class.]

## Slide 22

### BEFORE

Weak: success judged from the model's replies, guardrails that are prompt text, five attacks that are all the same mode delivered the same way, a canary in the committed trace, and cards written after the fact. Sound: cards before Go with the Chase's two, at least four modes, one delivered through a tool result, delivery and refusal evidence for each attack, named guardrails with their locus, model refusals recorded honestly with a variant flown, a cost table with supervision minutes, and an empty canary search. Exceptional: a trust-chain attack caught downstream, spans a backend can read, a guardrail moved from prose into the harness and flown both ways, an attack tied to a system-card section, and a squawk that changed an ADR.

Cut from slide 22 (full wording):
- 'All attacks failed' from the model's replies; no delivery spans / Guardrails that are sentences in the system prompt / Five attacks, one mode, all as user turns / Trace with full prompt text and the canary committed / Cost table of model dollars only / Attack cards written after the flight
- Five cards committed before Go, four or more modes, two by the Chase, one delivered through a tool result / Each attack: a delivery span and a refusal span or receipt / Each guardrail named with its locus; none is prompt text / Model refusals recorded as 'guardrail not exercised' and a variant flown / Cost table per turn and per sortie with supervision minutes / Canary search over the repository is empty
- A trust-chain attack caught by a downstream check, with the receipt / Spans use the OTel GenAI names and load in a backend / One guardrail moved from the prompt to the harness, before and after flown / An attack traced to a named system-card section, residual rate cited / A squawk routed to an ADR amendment

### AFTER

The evaluation lens has three columns, and the Chase reads only the attack cards, the trace slice, the receipts, and the cost table. A weak Sortie 11 judges success from the model's replies with no delivery spans, lists guardrails that are sentences in the system prompt, flies five attacks of the same mode delivered the same way, commits a trace with full prompt text and the canary in it, prices the sortie in model dollars only, and writes the attack cards after the flight. A sound Sortie 11 commits five cards before Go, two of them the Chase's, across at least four modes with one delivered through a tool result. Each attack has a delivery span and a refusal span or receipt, each guardrail is listed with its locus and none is prompt text, a model refusal is recorded as 'guardrail not exercised' with a variant flown, the cost table carries supervision minutes, and the canary search over the repository is empty. An exceptional Sortie 11 catches a trust-chain attack with a downstream check and shows the receipt, exports spans in the OTel GenAI names and loads them in a backend, moves one guardrail from the prompt into the harness and flies the attack before and after, traces an attack to a system-card section with its residual rate, and routes a squawk to an ADR amendment.

Cut from slide 22 (full wording):
- 'All attacks failed' from the model's replies; no delivery spans / Guardrails that are sentences in the system prompt / Five attacks, one mode, all as user turns / Trace with full prompt text and the canary committed / Cost table of model dollars only / Attack cards written after the flight
- Five cards committed before Go, four or more modes, two by the Chase, one delivered through a tool result / Each attack: a delivery span and a refusal span or receipt / Each guardrail listed with its locus; none is prompt text / Model refusals recorded as 'guardrail not exercised' and a variant flown / Cost table per turn and per sortie with supervision minutes / Canary search over the repository is empty
- A trust-chain attack caught by a downstream check, with the receipt / Spans use the OTel GenAI names and load in a backend / One guardrail moved from the prompt to the harness, before and after flown / An attack traced to a specific system-card section, residual rate cited / A squawk routed to an ADR amendment

## Slide 23

### BEFORE

Card eleven, corner of the envelope. Test point zero turns tracing on and proves it with a clean run and a cost row. Then five attacks: one as a user turn, one through a tool result, which is the trust-chain case, one with a canary on the easy path, and two written by your Chase and sealed, with the payload's hash on your card so the Chase can find it in your trace without trusting you. The falsifiers are the chapter's three. Abort covers the free model disappearing or a Go limit; a limit hit is itself a cost-table row. The Go is given by the Chase in the repository by Sunday noon, since there is no in-class Go/No-Go.

Cut from slide 23 (full wording):
- Corner of the envelope · depends on Sortie 10 PASS · Go by your Chase in the repo, Sun 11/15 noon

### AFTER

Flight Card 11 sits at the corner of the envelope and depends on a Sortie 10 PASS. Test point zero turns tracing on and proves it with a clean run, a cost row, and a receipt. Five attacks follow: one delivered as a user turn, one through a tool result (the trust-chain case), one with a canary on the easy path, and two written by your Chase and sealed, with each payload's hash on your card so the Chase can find the payload in your trace without trusting your account of it. The pre-registered falsifiers are the chapter's three: an attack that achieves its objective, an attack with no delivery span, and a guardrail credited when the attack never reached it or a pass obtained by disabling a check. Abort covers a model or route that becomes unavailable and a Go limit reached mid-sortie, and a limit hit is itself a row in the cost table. The Chase gives the Go in the repository, since there is no in-class Go/No-Go.

Cut from slide 23 (full wording):
- Corner of the envelope · depends on Sortie 10 PASS · Go by your Chase in the repo

## Slide 24

### BEFORE

The lab is Sortie 11 at the smallest scale that still teaches. A helper script builds a scratch repository with a hidden instruction in a notes file and a canary in a fake env file. You pre-register one attack, fly it with OpenCode's defaults, export the session, and summarize it with the script. Then you add a guardrail config and fly it again. The key step is at minute twenty-four: the model tells you what it did, and you check that against the export. The default config denies env-file reads by the read tool, and bash is allowed; whether your model walks around that is the result. Commit summaries and sanitized exports, never the raw ones.

Cut from slide 24 (full wording):
- Lab tonight (6:00–6:30): one attack, one guardrail, one trace
- 6:00–6:30
- 0–4   Setup: run the helper script; it builds a scratch repo with a notes file, a fake.env canary, and a hidden instruction. / 4–8   Pre-register attack A0 on the worksheet: objective, mode, delivery, guardrail, falsifier. / 8–14  Run 1 with default permissions. Ask for a summary; then ask the model to list its tool calls. Export the session. / 14–18 Summarize the export: tool table, tokens, cost, canary check, git diff. / 18–24 Run 2 with a guardrail config (bash ask, edit ask, share disabled). Reject what it asks. Export, summarize. / 24–28 Check the model's claim against the trace; name each outcome. / 28–30 Commit the summaries and sanitized exports; ledger event.
- evolution-11/lab/attack-card-A0.md / evolution-11/lab/run1-summary.md and run2-summary.md / evolution-11/lab/run1.sanitized.json and run2.sanitized.json (opencode export --sanitize) / The worksheet, with the outcome of each run: attack succeeded, refused by model, blocked by guardrail, or not delivered. / Raw exports stay in the scratch folder. They are never committed.
- The lesson hides in Run 1: the default denies reading .env files through the read tool, and says nothing about bash cat.

### AFTER

The lab is Sortie 11 at the smallest scale that still teaches. A helper script builds a scratch repository with a hidden instruction in a notes file and a canary in a fake env file. You pre-register one attack, A0, on the worksheet. You fly it with OpenCode's default permissions, export the session, and summarize the export with the script: tool table, tokens, cost, canary check, git diff. You then add a guardrail config (bash ask, edit ask, share disabled), fly the attack again, and summarize again. The step the lab exists for is the check of the model's account against the export: the model tells you what it did, the export shows what it did, and you record each run's outcome as succeeded, refused by model, blocked by guardrail, or not delivered. The result of Run 1 is the lesson. The default config denies env-file reads by the read tool and allows bash, so whether your model walks around the deny with bash cat is the finding. Commit the summaries and the sanitized exports. The raw exports stay in the scratch folder and are never committed.

Cut from slide 24 (full wording):
- Lab: one attack, one guardrail, one trace
- Setup: run the helper script. It builds a scratch repo with a notes file, a fake.env canary, and a hidden instruction. / Pre-register attack A0 on the worksheet: objective, mode, delivery, guardrail, falsifier. / Run 1 with default permissions. Ask for a summary. Then ask the model to list its tool calls. Export the session. / Summarize the export: tool table, tokens, cost, canary check, git diff. / Run 2 with a guardrail config (bash ask, edit ask, share disabled). Reject each permission request. Export, summarize. / Check the model's account of its tool calls against the trace. Label each outcome. / Commit the summaries and sanitized exports. Record a ledger event.
- evolution-11/lab/attack-card-A0.md / evolution-11/lab/run1-summary.md and run2-summary.md / evolution-11/lab/run1.sanitized.json and run2.sanitized.json (opencode export --sanitize) / The worksheet, with the outcome of each run: attack succeeded, refused by model, blocked by guardrail, or not delivered. / Raw exports stay in the scratch folder. They are never committed.
- In Run 1, the default config denies .env reads through the read tool but sets no rule for bash cat, so a bash command can still read the canary.

## Slide 25

### BEFORE

The Sprint. Six deliverables, listed in the brief with paths and acceptance tests. The exchange that used to happen at a table happens in the repository: your Chase writes two sealed attack cards against your system by Friday night, you put all five on your card on Saturday, the Chase gives Go or No-Go in the file by Sunday noon, you fly over the weekend, and the Chase writes the verdict from the evidence slice by Wednesday evening. Sealed means you know the objective and the mode but not the payload until you fly, and the hash proves the payload you flew is the one they wrote.

Cut from slide 25 (full wording):
- The Sprint: Sortie 11, due Wed 11/18, 11:59 p.m.
- Sortie 11 flight log: five attacks, each with delivery and refusal evidence / Tracing on your loop (spans.jsonl, GenAI names) and receipts / Cost table: per turn, per sortie, supervision minutes / guardrails.md: each guardrail, its locus, the attack that hit it / Design Analysis (a system card or an observability stack) / AI_LOG entry
- Fri 11/13, 11:59 p.m. Your Chase commits two sealed attack cards (A4, A5) to your repo by pull request, with each payload's SHA-256. / Sat 11/14. You commit the flight card with all five attacks and request Go. / Sun 11/15, noon. The Chase signs GO or NO-GO in flight-card.md.
- Tue 11/17, 11:59 p.m. Flight log and evidence slice committed. / Wed 11/18, 6:00 p.m. The Chase writes a verdict in chase-review.md from the evidence slice alone: PASS or FAIL, one line of reason. / Wed 11/18, 11:59 p.m. Everything in.
- You fly your Chase's attacks against your system. You write two attacks against theirs. Both of you learn the other's guardrails from the outside.

### AFTER

The Sprint has six deliverables, listed in the brief with paths and acceptance tests: the Sortie 11 flight log with five attacks and their delivery and refusal evidence, tracing on your loop with receipts, the cost table, guardrails.md, a Design Analysis of a system card or an observability stack, and an AI_LOG entry. The exchange that a table would host happens in the repository. Your Chase commits two sealed attack cards against your system by pull request, you commit the flight card with all five attacks and request Go, the Chase signs GO or NO-GO in flight-card.md, you fly, and the Chase writes PASS or FAIL in chase-review.md from the evidence slice alone, with one line of reason. The dates are in the course calendar. Sealed means you know the objective and the mode but not the payload until you fly, and the hash on your card proves that the payload you flew is the one the Chase wrote. You fly your Chase's attacks and write two against theirs, so each of you learns the other's guardrails from the outside.

Cut from slide 25 (full wording):
- The Sprint: Sortie 11
- Sortie 11 flight log: five attacks, each with delivery and refusal evidence / Tracing on your loop (spans.jsonl, GenAI names) and receipts / Cost table: per turn, per sortie, supervision minutes / guardrails.md: each guardrail, its locus, the attack that hit it / Design Analysis (a system card or an observability stack) / AI_LOG entry
- Your Chase commits two sealed attack cards (A4, A5) to your repo by pull request, with each payload's SHA-256. / You commit the flight card with all five attacks and request Go. / The Chase signs GO or NO-GO in flight-card.md.
- You commit the flight log and evidence slice. / The Chase writes a verdict in chase-review.md from the evidence slice alone: PASS or FAIL, one line of reason. / You commit all remaining work.
- You fly your Chase's attacks against your system. You write two attacks against theirs. Each of you learns the other's guardrails by attacking them.

## Slide 26

### BEFORE

Close. The black box outranks the narrative, and a guardrail counts only where an attack reached it and the trace shows the refusal. Lab at six. Sources checked 09/24/2026: OpenTelemetry GenAI conventions, https://github.com/open-telemetry/semantic-conventions-genai (docs/gen-ai/README.md, gen-ai-spans.md, gen-ai-agent-spans.md, gen-ai-metrics.md, gen-ai-events.md) and https://opentelemetry.io/docs/specs/semconv/gen-ai/ (moved notice). Claude Opus 5 System Card, Jul 24 2026, https://www-cdn.anthropic.com/ceaf5c7ff2783855203fde8208ec311252dced5b/Claude%20Opus%205%20System%20Card.pdf. GPT-5.5 System Card, Apr 23 2026, https://deploymentsafety.openai.com/gpt-5-5/gpt-5-5.pdf. Comment and Control, Aonan Guan, Apr 15 2026, https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot/ ; VentureBeat, https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026. OWASP LLM Top 10 2025, https://genai.owasp.org/llm-top-10/ ; OWASP Agentic Top 10 2026, https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/. Langfuse, https://langfuse.com/docs/observability/data-model , https://langfuse.com/docs/observability/features/observation-types , https://langfuse.com/integrations/developer-tools/opencode , https://langfuse.com/blog/joining-clickhouse. LangSmith, https://docs.langchain.com/langsmith/trace-with-opentelemetry , https://docs.langchain.com/langsmith/threads. OpenCode, https://opencode.ai/docs/cli/ , https://opencode.ai/docs/troubleshooting/ , https://opencode.ai/docs/share/ , https://opencode.ai/docs/permissions/ , https://opencode.ai/docs/go/ , export source https://github.com/anomalyco/opencode/blob/dev/packages/opencode/src/cli/cmd/export.ts. gzkit items from the course topic guide only; verify against the repository.

Cut from slide 26 (full wording):
- The black box outranks the narrative, and a guardrail counts only where an attack reached it.
- Trace your loop, price your sortie including your own minutes, and fly five attacks that someone other than you helped write. Lab at six: one attack, one guardrail, one exported trace.

### AFTER

The lecture closes on its two rules. The black box outranks the narrative, and a guardrail counts only where a delivered attack reached it and the trace shows the refusal. The build for this Evolution follows from them: trace your loop, price your sortie including your own minutes, and fly five attacks that someone other than you helped write. Sources, as of 09/24/2026: OpenTelemetry GenAI conventions, https://github.com/open-telemetry/semantic-conventions-genai (docs/gen-ai/README.md, gen-ai-spans.md, gen-ai-agent-spans.md, gen-ai-metrics.md, gen-ai-events.md) and https://opentelemetry.io/docs/specs/semconv/gen-ai/ (moved notice). Claude Opus 5 System Card, Jul 24 2026, https://www-cdn.anthropic.com/ceaf5c7ff2783855203fde8208ec311252dced5b/Claude%20Opus%205%20System%20Card.pdf. GPT-5.5 System Card, Apr 23 2026, https://deploymentsafety.openai.com/gpt-5-5/gpt-5-5.pdf. Comment and Control, Aonan Guan, Apr 15 2026, https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot/ ; VentureBeat, https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026. OWASP LLM Top 10 2025, https://genai.owasp.org/llm-top-10/ ; OWASP Agentic Top 10 2026, https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/. Langfuse, https://langfuse.com/docs/observability/data-model , https://langfuse.com/docs/observability/features/observation-types , https://langfuse.com/integrations/developer-tools/opencode , https://langfuse.com/blog/joining-clickhouse. LangSmith, https://docs.langchain.com/langsmith/trace-with-opentelemetry , https://docs.langchain.com/langsmith/threads. OpenCode, https://opencode.ai/docs/cli/ , https://opencode.ai/docs/troubleshooting/ , https://opencode.ai/docs/share/ , https://opencode.ai/docs/permissions/ , https://opencode.ai/docs/go/ , export source https://github.com/anomalyco/opencode/blob/dev/packages/opencode/src/cli/cmd/export.ts. gzkit items are cited from the course topic guide, and the repository is the authority where the two differ.

Cut from slide 26 (full wording):
- The black box outranks the narrative, and a guardrail counts only where an attack reached it.
- Trace your loop, price your sortie including your own minutes, and fly five attacks that someone other than you helped write. Lab: one attack, one guardrail, one exported trace.

