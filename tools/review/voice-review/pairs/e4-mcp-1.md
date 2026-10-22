# e4-mcp-1: speaker notes, before and after the voice pass

## Slide 1

### BEFORE

Evolution 4. Last week a tool was a contract and the model was an untrusted caller. This week the contract leaves your process and goes on a wire, so that any host can discover it, and the question becomes what a protocol has to promise that a function signature does not. Survey: the plugin era that failed, the OpenAPI specs that described without negotiating, and the protocol that won and then moved to a foundation. Build: your E3 tools served over MCP, listed by the inspector, called by your harness and by a script, and logged by the server. The revision of the specification that went to general availability on July 28 changed the wire in ways your SDK may or may not already reflect, and the lecture teaches the current revision and names what changed.

Cut from slide 1 (full wording):
- Evolution 4 · Lecture · Thu 09/24
- CIDM 6333 · Agentic Systems Design and Development · 4:00–5:00 · CC209 / Survey: ChatGPT plugins · OpenAPI tool specs · MCP and its foundation   ·   Build: an MCP server over your tool layer; inspector; harness client and script client

### AFTER

Evolution 4. In Evolution 3 a tool was a contract and the model was an untrusted caller. In this Evolution the contract leaves your process and goes on a wire, so that any host can discover it, and the question becomes what a protocol has to promise that a function signature does not. The survey covers the plugin era that failed, the OpenAPI specs that described a tool without negotiating anything, and the protocol that won and then moved to a foundation. The build serves your E3 tools over MCP, lists them in the inspector, calls them from your harness and from a script, and logs each call at the server. The revision of the specification that went to general availability on July 28 changed the wire in ways your SDK may or may not already reflect, so the lecture teaches the current revision and states what changed.

Cut from slide 1 (full wording):
- Evolution 4 · Lecture
- CIDM 6333 · Agentic Systems Design and Development / Survey: ChatGPT plugins · OpenAPI tool specs · MCP and its foundation   ·   Build: an MCP server over your tool layer; inspector; harness client and script client

## Slide 2

### BEFORE

Ten on framing, twenty on the spine because the build is a server and the wire changed this summer, fifteen on three teardowns that end at the foundation, seven on the reference design's refusal and the project that reverses it one tier up, and eight on the lens and the card.

### AFTER

The lecture has five parts: the framing; the spine, the longest part because the build is a server and the July revision changed the wire; three teardowns that end at the foundation; the reference design's refusal and the project that reverses it one tier up; and the evaluation lens with the flight card.

## Slide 3

### BEFORE

Framing. The problem MCP answered was combinatorial. Before November 2024 each host and each tool wrote adapters for each other and the field paid N times M. A protocol lets each side write one adapter and pay N plus M. Then the three promises a protocol makes that a function signature cannot: discovery, negotiation, and transport independence. Your E3 tool had a schema and a gate and neither of these three, because nothing outside your process could ask it anything. The claim for the sortie: two independent clients, one server, identical behavior, every call logged. The falsifier students underrate is the asymmetric one: a tool that works from the harness and fails from the script means the harness was compensating, and the sortie has measured the compensation.

Cut from slide 3 (full wording):
- Every host that wanted a tool wrote its own adapter, and every tool that wanted a host wrote another. With N hosts and M tools the field maintained N×M adapters. A protocol makes each side implement one thing: N clients, M servers, N+M pieces of code.
- Discovery: a client can ask a server what it offers before it calls anything. Negotiation: client and server state which version and which capabilities they support, and a mismatch is an error, not a guess. Transport independence: the same server runs over a pipe on your laptop and over HTTP on a host you do not control. Your E3 tool had a schema and a permission gate. It did not have any of these three, because nothing outside your process could ask.
- Tonight's claim, which Sortie 4 will try to disprove / Every tool the server declares is discoverable, callable, and schema-validated from two independent clients, and every call is logged server-side. If a tool works from your harness but not from a script, the harness was doing work the protocol should have done, and you have measured that work.

### AFTER

Framing. The problem MCP answered was combinatorial. Before November 2024 each host and each tool wrote adapters for each other, and the field paid N times M. A protocol lets each side write one adapter and pay N plus M. A protocol then makes three promises that a function signature cannot: discovery, negotiation, and transport independence. Your E3 tool had a schema and a gate and none of these three, because nothing outside your process could ask it anything. The design claim for the sortie is that two independent clients and one server show identical behavior, with every call logged. One of the falsifiers is asymmetric: a tool that works from the harness and fails from the script means the harness was compensating for the protocol, and the sortie has measured the compensation.

Cut from slide 3 (full wording):
- Every host that wanted a tool wrote its own adapter, and every tool that wanted a host wrote another. With N hosts and M tools the field maintained N×M adapters. A protocol makes each side implement one thing: N clients, M servers, N+M pieces of code.
- Discovery: a client can ask a server what it offers before it calls anything. Negotiation: client and server state which version and which capabilities they support, and a mismatch produces an error that neither side resolves by guessing. Transport independence: the same server runs over a pipe on your laptop and over HTTP on a host you do not control. Your E3 tool had a schema and a permission gate. It did not have any of these three, because nothing outside your process could ask.
- The statement Sortie 4 will try to disprove / Every tool the server declares is discoverable, callable, and schema-validated from two independent clients, and every call is logged server-side. If a tool works from your harness and fails from a script, the harness did work the protocol should have done, and the difference between the two clients measures that work.

## Slide 4

### BEFORE

The architecture in one column and the primitives in the rest. Host, client, server: the human is in the host, one client per server, JSON-RPC both ways. The three primitives are distinguished by who controls them, and that is the design analysis. Tools are model-controlled and are last week's contract on the wire. Resources are application-controlled: the host decides what enters context, which is why next week a resource carrying an instruction is an attack and not a feature. Prompts are user-controlled. Two more cards: extensions and the tasks extension for long-running work, and the deprecation list from the July 28 revision, which matters because most tutorials online still teach roots and sampling. A new server should not adopt a feature the specification has scheduled for removal.

Cut from slide 4 (full wording):
- Hosts, clients, servers — and the three server primitives
- Host: the application the human is in (Claude Code, Codex, your script). Client: the connector inside the host, one per server. Server: the process that declares capabilities and answers requests, over JSON-RPC 2.0.
- Functions the model may call. Declared with a name, a description, a JSON Schema for input, and optionally one for output. The model chooses to call them; the host may gate the call first.
- Data the server exposes by URI: files, records, a ledger, 'what is attested?' The application decides which resources enter context and when.
- Reusable templates the server offers the user: a named workflow with arguments, surfaced as a slash command or a menu item in the host.
- Beyond the core: an `extensions` field in both capability sets; long-running work moved to the official tasks extension (`tasks/get` polling, `tasks/update` for input). Adopt an extension only when the core cannot express the need.
- Roots, sampling, and logging are deprecated with a twelve-month window: pass paths as tool arguments, call the model API directly, log to stderr or OpenTelemetry. The HTTP+SSE transport is deprecated; use Streamable HTTP.

### AFTER

The slide puts the architecture in one column and the primitives in the rest. The host is the application the human is in, each server gets one client inside the host, and client and server exchange JSON-RPC requests in both directions. The specification distinguishes the three primitives by who controls each one, and that distinction is the design analysis of the protocol, because control decides where consent can live. Tools are model-controlled; a tool is the E3 contract put on the wire. Resources are application-controlled: the host decides what enters context, and for this reason E5 treats a resource that carries an instruction as an attack. Prompts are user-controlled. Two more cards follow: extensions, with the tasks extension for long-running work, and the deprecation list from the July 28 revision. The deprecation list matters because tutorials written before that revision still teach roots and sampling. A new server should not adopt a feature the specification has scheduled for removal.

Cut from slide 4 (full wording):
- Hosts, clients, servers, and the three server primitives
- Host: the application the human is in (Claude Code, Codex, your script). Client: the connector inside the host, one per server. Server: the process that declares capabilities and answers requests, over JSON-RPC 2.0.
- Functions the model may call. Declared with a name, a description, a JSON Schema for input, and optionally one for output. The model chooses to call them; the host may gate the call first.
- Data the server exposes by URI: files, records, a ledger, 'what is attested?' The application decides which resources enter context and when.
- Reusable templates the server offers the user: a workflow with a title and arguments, surfaced as a slash command or a menu item in the host.
- Beyond the core: an `extensions` field in both capability sets; long-running work moved to the official tasks extension (`tasks/get` polling, `tasks/update` for input). Adopt an extension only when the core cannot express the need.
- Roots, sampling, and logging are deprecated with a twelve-month window: pass paths as tool arguments, call the model API directly, log to stderr or OpenTelemetry. The HTTP+SSE transport is deprecated; use Streamable HTTP.

## Slide 5

### BEFORE

The revision that went GA on July 28 is a rewrite of the wire, and the headline is statelessness: no handshake, no session header, version and capabilities in the metadata of every request. The stated rationale is infrastructure: any request can land on any instance behind a round-robin balancer. The change that bites a server author is the third row. Roots, sampling, and elicitation were server-initiated calls back into the client; now a server that needs more input returns a result typed input_required, and the client retries with the answers. Ask for input by returning, not by calling. The fourth row is your first test point: server/discover is mandatory and is the inspector's first call. Last two rows: subscriptions are one stream now, and list results must carry a TTL and a cache scope, so put your tools in deterministic order and give an honest TTL. Before class, check which revision the lab's Python SDK speaks; the SDKs shipped on the day, but a student's pinned version may not have.

Cut from slide 5 (full wording):
- No handshake. Every request carries protocol version and client capabilities in `_meta`; servers answer with `serverInfo` in `_meta`
- A request can land on any instance behind a plain load balancer; nothing to remember between calls
- Removed. `tools/list` and friends no longer vary per connection; cross-call state uses server-minted handles passed as ordinary arguments
- If your server needed a session, it now needs a handle, and the handle is a design decision to record
- Multi Round-Trip Requests: the server returns `resultType: "input_required"` with `inputRequests`; the client retries the original request with `inputResponses`
- A server that needs more from the human asks by returning, not by calling back; every result now carries `resultType`
- Source: modelcontextprotocol.io, 2026-07-28 changelog (GA July 28, 2026; Tier 1 SDKs shipped same day). Verify the Python SDK version installed in the lab against this table before class.

### AFTER

The revision that went to general availability on July 28 rewrote the wire, and the headline change is statelessness: there is no handshake and no session header, and every request carries its version and capabilities in its metadata. The changelog gives an infrastructure rationale: any request can land on any instance behind a round-robin balancer, because no instance has to remember anything between calls. The change that bites a server author is the third row. Roots, sampling, and elicitation were calls the server made back into the client; under the new revision a server that needs more input returns a result typed input_required, and the client retries the request with the answers attached. The fourth row is your first test point: server/discover is mandatory, and it is the inspector's first call. The last two rows cover subscriptions, which are now one stream, and list results, which must carry a TTL and a cache scope; put your tools in deterministic order and give an honest TTL. Check which revision your pinned Python SDK speaks before you build, because the SDKs shipped on the day of the revision and a version pinned earlier may not have it.

Cut from slide 5 (full wording):
- No handshake. Every request carries protocol version and client capabilities in `_meta`; servers answer with `serverInfo` in `_meta`
- A request can land on any instance behind a plain load balancer, because the server keeps no state between calls
- Removed. `tools/list` and the other list methods no longer vary per connection; cross-call state uses server-minted handles passed as ordinary arguments
- If your server needed a session, it now needs a handle. Record the handle as a design decision
- Multi Round-Trip Requests: the server returns `resultType: "input_required"` with `inputRequests`; the client retries the original request with `inputResponses`
- A server that needs more from the human asks for it in its result and does not call the client back; every result now carries `resultType`
- Source: modelcontextprotocol.io, 2026-07-28 changelog (GA July 28, 2026; Tier 1 SDKs shipped same day). Verify the Python SDK version installed in the lab against this table.

## Slide 6

### BEFORE

The server itself, in the shape the Python SDK gives you. FastMCP derives the input schema from type hints and the description from the docstring, so the code you wrote in E3 becomes a server with a decorator. The resource is a URI; here it is the last fifty ledger events. Transport is a flag: stdio tonight, Streamable HTTP when the host is not on your laptop. The four moves on the right are the lab in order, and the third is the one that matters: two clients, one of them a script, so that the harness cannot hide protocol work from you. The strip is the bridge to next week. The description is all the model sees, so write it as a contract; in E5 you will see tool descriptions written by an adversary.

Cut from slide 6 (full wording):
- 1. Declare one tool from E3, read-class, with its docstring as the description and its type hints as the schema. The write tool stays behind the E3 gate and does not go on the wire tonight. / 2. Run over stdio. Open the inspector; confirm server/discover answers and tools/list shows the tool with the schema you meant. / 3. Connect two clients: your harness (Claude Code, Codex, Gemini CLI, or OpenCode) by its MCP config, and a twenty-line script client from the SDK. Call the tool from each. / 4. Read the server log. Two calls, two entries, same tool, same arguments, same result. Capture that slice for the Chase.
- The description is the model's only view of the tool. Write it as a contract (what it does, what it must not do, side-effect class), because next week we will see what happens when someone else writes it.

### AFTER

This slide shows the server itself, in the shape the Python SDK gives you. FastMCP derives the input schema from the type hints and the description from the docstring, so the function you wrote in E3 becomes a server with one decorator. A resource is addressed by URI; here the URI returns the last fifty ledger events. The transport is a flag: stdio for this Evolution, Streamable HTTP when the host is not on your laptop. The four steps on the right are the lab in order. The third step carries the design claim, because two clients, one of them a script, leave the harness no way to hide protocol work from you. The strip at the bottom is the bridge to E5. The description is all the model sees, so write it as a contract; in E5 you will read tool descriptions that an adversary wrote.

Cut from slide 6 (full wording):
- 1. Declare one tool from E3, read-class, with its docstring as the description and its type hints as the schema. The write tool stays behind the E3 gate and does not go on the wire in this Evolution. / 2. Run over stdio. Open the inspector. Confirm that server/discover answers and tools/list shows the tool with the schema you meant. / 3. Connect two clients: your harness (Claude Code, Codex, Gemini CLI, or OpenCode) by its MCP config, and a twenty-line script client from the SDK. Call the tool from each. / 4. Read the server log. Confirm two entries for the two calls, with the same tool, arguments, and result. Capture that slice for the Chase.
- The description is the model's only view of the tool. Write it as a contract (what it does, what it must not do, side-effect class), because E5 shows what happens when someone else writes it.

## Slide 7

### BEFORE

Two teardowns, both pre-protocol. The plugin store of March 2023 was description without negotiation, hosted in one product, and it was gone inside a year. Function calling and the OpenAPI-derived schemas were the correct idea in-process, and they are what your E3 tool is, but every host still wrote its own loader, so the combinatorial cost did not move. Read both by their theory of control, as we did with the frameworks in E2: in the plugin model the vendor owns discovery and the loop, and in the OpenAPI model you own the loop and nobody owns the boundary. MCP's move was to make the boundary the thing that is specified.

Cut from slide 7 (full wording):
- A manifest, an OpenAPI document, and a one-paragraph description the model read to decide when to call the plugin. Hosted by the vendor, invoked inside one product, discoverable in one store. /  / What it got right: the model could read a spec and call an endpoint. What it lacked: any host but one, any negotiation of capability or version, any local transport, and any way for the plugin to offer content or prompts rather than functions. Deprecated within a year in favor of GPTs and Actions. /  / Theory of control: the vendor owns discovery, hosting, and the loop; you own an HTTP endpoint.
- Function calling arrived mid-2023: hand the model a JSON Schema per function, get back a structured call. Many teams generated those schemas from OpenAPI documents, one endpoint per tool. /  / What it got right: schemas as contracts, in-process, on any model. What it lacked: discovery (the host must already know the spec), negotiation (no version, no capability exchange), and a second primitive (everything is a function; no resources, no prompts). Each host still wrote its own loader: N×M by another name. /  / Theory of control: you own the loop and the schema; nothing owns the boundary between hosts.

### AFTER

Two teardowns follow, both from before the protocol. The plugin store of March 2023 offered description without negotiation, ran inside one product, and its vendor deprecated it within a year. Function calling and the OpenAPI-derived schemas were the correct idea in-process, and they are what your E3 tool is, but every host still wrote its own loader, so the combinatorial cost did not change. Read both by their theory of control, as E2 read the frameworks: in the plugin model the vendor owns discovery and the loop, and in the OpenAPI model you own the loop and nobody owns the boundary. MCP specified the boundary between host and server, which neither predecessor had specified.

Cut from slide 7 (full wording):
- A manifest, an OpenAPI document, and a one-paragraph description the model read to decide when to call the plugin. Hosted by the vendor, invoked inside one product, discoverable in one store. /  / What it got right: the model could read a spec and call an endpoint. What it lacked: any host but one, any negotiation of capability or version, any local transport, and any way for the plugin to offer content or prompts rather than functions. OpenAI deprecated plugins within a year in favor of GPTs and Actions. /  / Theory of control: the vendor owns discovery, hosting, and the loop; you own an HTTP endpoint.
- Function calling arrived mid-2023: hand the model a JSON Schema per function, get back a structured call. Many teams generated those schemas from OpenAPI documents, one endpoint per tool. /  / What it got right: schemas as contracts, in-process, on any model. What it lacked: discovery (the host must already know the spec), negotiation (no version, no capability exchange), and a second primitive (everything is a function; no resources, no prompts). Each host still wrote its own loader, so the N×M adapter count remained. /  / Theory of control: you own the loop and the schema; no party owns the boundary between hosts.

## Slide 8

### BEFORE

MCP itself as a system, on the board as a Design Analysis. Timeline down the left, ending at the foundation and the GA revision, so students see that the protocol has a governance apparatus of its own now: a deprecation policy with a twelve-month window and an enhancement-proposal process. The question the course asks of every system is where the human is, and the answer here is precise: in the host, and only in the host. The wire carries requests, not permissions. That is a design choice with a consequence, and the consequence is next week. Two more cards: what an ecosystem needs, with the registry named as a supply chain, and the analysis in the template's five fields.

Cut from slide 8 (full wording):
- Teardown: MCP as a system — where is the human?
- Nov 2024 — Anthropic publishes protocol, SDKs, reference servers. / Mar 2025 — Streamable HTTP; HTTP+SSE deprecated; OAuth authorization. / Jun 2025 — Resource indicators, structured tool output, elicitation. / Nov 2025 — Tasks (experimental), URL-mode elicitation. / Dec 2025 — Donated to the Agentic AI Foundation (Linux Foundation). / Jul 2026 — 2026-07-28 GA: stateless core, MRTR, deprecation policy.
- In the host, and only in the host. The protocol puts consent in the host: the client must get the human's approval before a tool runs, and the server must never assume it. The wire carries requests, not permissions. /  / Component focus: tools and coordination. Governance is delegated to the host by design, which is why E5 is about what happens when the host's trust is misplaced.
- A versioning and deprecation policy (twelve-month window; a registry of deprecated features). Independent SDKs (TypeScript, Python, Go, C#; Rust in beta). A server registry with provenance, because one without it is a supply chain (E5: SmartLoader). Governance that is not one vendor.
- Problem: N×M. Decision: a client–server protocol over JSON-RPC with three server primitives and negotiated capabilities. Alternatives: a plugin store; per-vendor function-calling formats; a library. Consequences: adoption across hosts, and a security surface that did not exist when tools were in-process. Where it puts the human: outside the wire.

### AFTER

The third teardown reads MCP itself as a system, on the board as a Design Analysis. The timeline runs down the left and ends at the foundation and the GA revision, so that the protocol's own governance apparatus is visible: a deprecation policy with a twelve-month window and an enhancement-proposal process. The question the course asks of every system is where the human is, and here the answer is precise: in the host, and only in the host. The wire carries requests; the host grants permission, and permission never travels. That design choice has a consequence, and E5 covers the consequence. Two more cards follow: what a protocol needs around it, where a registry without provenance counts as a supply chain, and the analysis in the template's five fields.

Cut from slide 8 (full wording):
- Teardown: MCP as a system. Where is the human?
- Nov 2024: Anthropic publishes protocol, SDKs, reference servers. / Mar 2025: Streamable HTTP; HTTP+SSE deprecated; OAuth authorization. / Jun 2025: Resource indicators, structured tool output, elicitation. / Nov 2025: Tasks (experimental), URL-mode elicitation. / Dec 2025: Donated to the Agentic AI Foundation (Linux Foundation). / Jul 2026: 2026-07-28 GA: stateless core, MRTR, deprecation policy.
- In the host, and only in the host. The protocol puts consent in the host: the client must get the human's approval before a tool runs, and the server must never assume it. The wire carries requests only, and no message on it grants permission. /  / Component focus: tools and coordination. The protocol's designers delegated governance to the host, and E5 examines what happens when the host's trust is misplaced.
- A versioning and deprecation policy (twelve-month window; a registry of deprecated features). Independent SDKs (TypeScript, Python, Go, C#; Rust in beta). A server registry with provenance, because a registry without provenance is an unchecked supply chain (E5: SmartLoader). Governance by a foundation instead of a single vendor.
- Problem: N×M. Decision: a client–server protocol over JSON-RPC with three server primitives and negotiated capabilities. Alternatives: a plugin store; per-vendor function-calling formats; a library. Consequences: adoption across hosts, and a security surface that did not exist when tools were in-process. Where it puts the human: outside the wire.

## Slide 9

### BEFORE

The reference design refused the protocol we are teaching, and the refusal is the lesson. The storage-tiers doctrine: no external protocol may be a prerequisite for a core governance operation. A kit whose job is to be trusted keeps the smallest dependency surface, which is the same posture as argparse over click. The campaign review nevertheless scored MCP as absent and un-designed, which is the honest way to hold a refusal: written, with alternatives, and open to reversal. The reversal is on the right: a server one tier up exposes the verbs and the ledger without becoming a prerequisite, and the falsifier for the tier boundary is simple. Kill the server; run gz validate. Verify the quoted sentence against the repository before class.

Cut from slide 9 (full wording):
- gzkit's governance verbs (gz status, gz validate, the ledger, receipts) run on the standard library over files. The storage-tiers doctrine says no external protocol may be a prerequisite for a core governance operation. /  / Why: a governance kit that needs a running server to say what is attested has made attestation depend on availability. The ledger must be readable with cat. The refusal is the same posture as ADR-0.0.2 (argparse over click): the smallest dependency surface for the thing whose job is to be trusted. /  / The campaign review scored MCP 'absent and un-designed' — a refusal is only a decision if it is written down with its alternatives, and this one was.
- The refusal is about prerequisites, not about presence. A server that sits above the core and exposes the verbs and the ledger adds a way in without adding a dependency: if the server is down, gz still works, and the ledger is still a file. /  / The pool ADR sketches exactly this: an MCP context server as a tier above core. The test of the tier boundary is the falsifier: kill the server and run gz validate. If it fails, the server became a prerequisite and the doctrine is broken. /  / [Verify against the current storage-tiers.md and the pool ADR before class; quote the doctrine sentence exactly.]

Instructor checks moved off the slide:
- [Verify against the current storage-tiers.md and the pool ADR before class; quote the doctrine sentence exactly.]

### AFTER

The reference design refused the protocol this Evolution teaches, and the refusal is what this slide teaches. The storage-tiers doctrine states that no external protocol may be a prerequisite for a core governance operation. A kit whose job is to be trusted keeps the smallest dependency surface, which is the same posture gzkit took in ADR-0.0.2 when it chose argparse over click. The campaign review nevertheless scored MCP as absent and un-designed, and the review held the refusal the honest way: written down, with its alternatives, and open to reversal. The reversal is on the right. A server one tier up exposes the verbs and the ledger without becoming a prerequisite, and the falsifier for the tier boundary is a two-step test: kill the server, then run gz validate. If gz validate fails, the server became a prerequisite and the doctrine no longer holds.

Cut from slide 9 (full wording):
- gzkit's governance verbs (gz status, gz validate, the ledger, receipts) run on the standard library over files. The storage-tiers doctrine says no external protocol may be a prerequisite for a core governance operation. /  / Why: a governance kit that needs a running server to say what is attested has made attestation depend on availability. The ledger must be readable with cat. The refusal is the same posture as ADR-0.0.2 (argparse over click): the smallest dependency surface for the thing whose job is to be trusted. /  / The campaign review scored MCP 'absent and un-designed'. A refusal counts as a decision only when someone records it with its alternatives, and the storage-tiers doctrine records this one.
- The refusal covers prerequisites only. A server that sits above the core and exposes the verbs and the ledger adds a way in without adding a dependency: if the server is down, gz still works, and the ledger is still a file. /  / The pool ADR sketches this design: an MCP context server as a tier above core. The test of the tier boundary is the falsifier: kill the server and run gz validate. If it fails, the server became a prerequisite and the doctrine is broken. /  / [Verify against the current storage-tiers.md and the pool ADR before class; quote the doctrine sentence exactly.]

Instructor checks moved off the slide:
- [Verify against the current storage-tiers.md and the pool ADR before class; quote the doctrine sentence exactly.]

## Slide 10

### BEFORE

The project that reverses the refusal one tier up, laid out by primitive so the three kinds of control are visible. Tools are the read-class verbs; writes stay gated as in E3. Resources are the ledger and the attestation record by URI, entering context only when the host decides. The one prompt is the question the ledger can answer. The strip is the exercise from the chapter, and it is also the first instrument this course has given you against summary laundering: the model's answer to what is attested can now be diffed against the resource it was handed.

Cut from slide 10 (full wording):
- gz_status(): the repo's governance state. gz_validate(scope): run the validators, return the report. Read-class only in the first cut. Any write verb (gz attest, gz release) stays behind a host gate and a confirmation event, exactly as in E3.
- ledger://events?tail=N: the last N events. attest://<artifact>: what the ledger records as attested for one artifact. receipts://<id>. The host decides when these enter context; the server never pushes them.
- /what-is-attested: a template that reads the attestation resource and answers only from it. The prompt is the human's way to ask the question the ledger can answer; the model's answer is then checkable against the resource it was given.
- The exercise from chapter 13: ask your harness 'what is attested in this repo?' and check its answer against the ledger. A summary that adds an attestation the ledger does not hold is summary laundering, and the server has just given you the instrument to catch it.

### AFTER

This slide lays out the project that reverses the refusal one tier up, by primitive, so that the three kinds of control are visible. The tools are the read-class verbs; the write verbs stay behind a host gate, as in E3. The resources are the ledger and the attestation record, addressed by URI, and they enter context only when the host decides. The one prompt asks the question the ledger can answer. The strip holds the exercise from chapter 13, and the exercise is also the first instrument this course has given you against summary laundering: you can now diff the model's answer to 'what is attested?' against the resource the model was handed.

Cut from slide 10 (full wording):
- gz_status(): the repo's governance state. gz_validate(scope): run the validators, return the report. Read-class only in the first cut. Any write verb (gz attest, gz release) stays behind a host gate and a confirmation event, as in E3.
- ledger://events?tail=N: the last N events. attest://<artifact>: what the ledger records as attested for one artifact. receipts://<id>. The host decides when these enter context; the server never pushes them.
- /what-is-attested: a template that reads the attestation resource and answers only from it. The prompt is the human's way to ask the question the ledger can answer; the model's answer is then checkable against the resource it was given.
- The exercise from chapter 13: ask your harness 'what is attested in this repo?' and check its answer against the ledger. A summary that adds an attestation the ledger does not hold is summary laundering, and a diff of the answer against the attestation resource catches it.

## Slide 11

### BEFORE

Weak: one harness pretending to be two clients, a client silently repairing arguments, a log that is a narrative, a write tool on the wire with no gate, and a server built on a deprecated feature because the tutorial was from 2025. Sound: discovery and listing captured from the inspector, two independent clients with identical logged calls, a server-side log with the four fields, the write tool held back with the reason written down, and the SDK and protocol revision on the substrate line. Exceptional: a third client with a divergence explained, a deliberately wrong schema rejected by the server, cache fields honored, the governance server with the attestation diff, and a debrief that names what the protocol forced you to write.

Cut from slide 11 (full wording):
- Server runs only inside one harness; the 'second client' is the same harness with a different prompt / Schema shown in tools/list differs from what the function accepts; the client 'fixed' the arguments / Server log missing or written by the client; calls counted from the narrative / A write tool on the wire with no gate; 'it was fine in testing' / Built on roots or sampling from a 2025 tutorial; deprecation not noticed
- server/discover and tools/list captured from the inspector, schema matching the type hints / Two independent clients (harness + script), same tool, same arguments, same result, both logged / Server-side log with timestamp, tool name, arguments, and outcome per call / Read tool on the wire; write tool held back with the reason recorded in the flight log / SDK version and protocol revision recorded on the card's SUBSTRATE line
- A third client (a different harness family) with a divergence found and explained / One tool deliberately declared with a wrong schema to show the server, not the client, rejecting it / ttlMs and cacheScope set and a client observed honoring them / The governance server: gz_status as a tool, ledger as a resource, and the 'what is attested?' diff run / A design signal in the debrief: what the protocol forced you to write that E3 let you skip

### AFTER

A weak Sortie 4 shows one harness pretending to be two clients, a client silently repairing arguments, a log that is a narrative, a write tool on the wire with no gate, and a server built on a deprecated feature because the tutorial was from 2025. A sound Sortie 4 shows discovery and listing captured from the inspector, two independent clients with identical logged calls, a server-side log with the four fields, the write tool held back with the reason written down, and the SDK and protocol revision on the SUBSTRATE line. An exceptional Sortie 4 adds a third client with a divergence explained, a deliberately wrong schema that the server rejects, cache fields honored, the governance server with the attestation diff, and a debrief that states what the protocol forced you to write.

Cut from slide 11 (full wording):
- Server runs only inside one harness; the 'second client' is the same harness with a different prompt / Schema shown in tools/list differs from what the function accepts; the client 'fixed' the arguments / Server log missing or written by the client; calls counted from the narrative / A write tool on the wire with no gate; 'it was fine in testing' / Built on roots or sampling from a 2025 tutorial; deprecation not noticed
- server/discover and tools/list captured from the inspector, schema matching the type hints / Two independent clients (harness + script), same tool, same arguments, same result, both logged / Server-side log with timestamp, tool name, arguments, and outcome per call / Read tool on the wire; write tool held back with the reason recorded in the flight log / SDK version and protocol revision recorded on the card's SUBSTRATE line
- A third client (a different harness family) with a divergence found and explained / One tool deliberately declared with a wrong schema to show the server rejecting it before any client repair / ttlMs and cacheScope set and a client observed honoring them / The governance server: gz_status as a tool, ledger as a resource, and the 'what is attested?' diff run / A design signal in the debrief: what the protocol forced you to write that E3 let you skip

## Slide 12

### BEFORE

Card four, center of the envelope, dependent on Sortie 3 because the write gate must already hold before anything goes on the wire. Four test points: discovery, a call from the harness, the same call from a script, and a bad call the server must reject. The abort criterion is the one that is new this term: an SDK and protocol revision mismatch that prevents discovery is infrastructure, not a failed claim, and it is a halt. Record the revision on the substrate line so the Chase can tell the difference.

Cut from slide 12 (full wording):
- Flight Card 4 brief — Sortie 4: one server, two clients
- Center of the envelope · depends on Sortie 3 PASS · Go at 5:46

### AFTER

Flight Card 4 sits at the center of the envelope and depends on Sortie 3, because the write gate must already hold before anything goes on the wire. The card has four test points: discovery, a call from the harness, the same call from a script, and a bad call the server must reject. The abort criterion is new to this card: an SDK and protocol revision mismatch that prevents discovery is an infrastructure failure rather than a refuted design claim, so it halts the sortie instead of failing it. Record the revision on the SUBSTRATE line so that the Chase can tell the two apart.

Cut from slide 12 (full wording):
- Flight Card 4 brief (Sortie 4): one server, two clients
- Center of the envelope · depends on Sortie 3 PASS

## Slide 13

### BEFORE

Close. A protocol is a contract that strangers can discover; that is what it adds to last week's tool. One tool on the wire, two clients, one log. Consultation at five: Sortie 3 verdicts, and the name of the first tool you will serve.

Cut from slide 13 (full wording):
- Put one tool on the wire, let two clients find it, and let the server keep the only log that counts. Consultation at five: Sortie 3 verdicts and your server's first tool in one sentence.

### AFTER

Close. A protocol is a contract that strangers can discover, and discovery is what the protocol adds to the E3 tool. The sortie puts one tool on the wire, connects two clients, and keeps one log at the server. Bring to the consultation your Sortie 3 verdicts and the name of the first tool you will serve.

Cut from slide 13 (full wording):
- Put one tool on the wire, let two clients find it, and let the server keep the log the Chase reads. Bring to consultation: Sortie 3 verdicts and your server's first tool in one sentence.

