# 8. The Harness Year (2025): Claude Code, Codex, the SDKs, A2A, AGENTS.md, Skills, and Context Engineering

> **Course use.** CIDM 6333 · E2, E5, E6 survey. Status: **outline**.

## Learning outcomes

After this chapter you can:

- Describe what a harness is and why the field's design center moved to it.
- Compare the vendor harnesses and SDKs by their theory of control.
- Explain A2A against MCP, and AGENTS.md and skills as context surfaces.
- Define context engineering and the spec-driven kits.

## Outline

### 8.1 The harness

- Claude Code (Feb): terminal-native, tools, permissions, CLAUDE.md, then hooks, subagents, plan mode, compaction. Codex CLI and cloud; Gemini CLI; Copilot coding agent; Cursor and Windsurf.

### 8.2 The SDKs

- OpenAI Agents SDK (agents, handoffs, guardrails, tracing); Google ADK; Claude Agent SDK (the harness as a library); Pydantic AI (typed tool calls). Each encodes who owns the loop.

### 8.3 Protocols and surfaces

- A2A (agents as peers) vs. MCP (tools). AGENTS.md as the cross-vendor instruction file. Agent Skills as progressive disclosure. Hooks as a governance membrane.

### 8.4 Context engineering

- The window as an engineered artifact: budgets, compaction, subagents for isolation, progressive disclosure. The Anthropic and OpenAI guidance.

### 8.5 Spec-driven kits

- GitHub spec-kit, BMAD, OpenSpec, GSD. These kits supply a methodology and, for the most part, no governance layer. gzkit's comparison document sets them side by side.

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| Claude Code | 2025 | The reference harness | All nine |
| Codex CLI / cloud | 2025 | AGENTS.md-native; sandbox; background | Runtime, governance |
| OpenAI Agents SDK | 2025 | Handoffs, guardrails, tracing | Coordination, evaluation |
| Google ADK / A2A | 2025 | Agents as peers | Coordination |
| Claude Agent SDK | 2025 | Harness as library | Runtime |
| Pydantic AI | 2024–25 | Validation as governance | Tools |
| AGENTS.md / Skills | 2025 | Context surfaces | Context |
| spec-kit / BMAD / OpenSpec / GSD | 2025 | Methodology kits | Governance |

## Reference design: gzkit

gzkit enters this chapter as a meta-harness. It renders one canon into each harness's surfaces (17 hooks into Claude Code, 2 into Codex, 1 into Copilot), and the control-surface matrix that records this rendering is the chapter's central Design Analysis.

## Readings

- Anthropic, "Effective Context Engineering for AI Agents" (2025); "Effective Harnesses for Long-Running Agents" (2025).
- OpenAI, "A Practical Guide to Building Agents" (2025).
- gzkit `docs/design/agent-control-surface-matrix.md`; `docs/examples/comparison-gzkit-speckit-bmad.md`.

## Exercises and Design Analysis prompts

1. Write a Design Analysis of your harness. Then write the same analysis of that harness as gzkit sees it (which surfaces does gzkit render into?).
2. Write a Design Analysis of A2A against MCP. What is a peer that a tool is not?



---

# 9. 2026: Harness Engineering, Background Agents, and the Reference Design's Year

> **Course use.** CIDM 6333 · E5, E9, E11, E12 survey. Status: **outline**.

## Learning outcomes

After this chapter you can:

- Describe harness engineering as a discipline and state what it asserts.
- Explain long-running and background agents and their operational problems.
- Narrate gzkit's arc from genesis to the measurement era and extract the lessons.

## Outline

### 9.1 Harness engineering

- Böckeler and the OpenAI post argue that most of an agent product is not the model. gzkit's appraisal of that position, and the blind spots the appraisal records (harness fitness unmeasured; an illusion of quality produced by heavy gates).

### 9.2 Background and long-running agents

- Cloud sessions, scheduled tasks, compaction across days; the operational questions: scheduling, rollback, cost, who attests.

### 9.3 The reference design's arc

- Jan genesis → hooks → OBPI pipeline → CMS → subagents and personas → three layers of truth → receipts and patch cadence → universal attestation → map-not-encyclopedia → V.I.B.E.S. → Magna Carta → repudiations and the MX hangar → airlock → foundation sunset → measurement era and commit-locus enforcement.

### 9.4 The incident casebook (pointer)

- Twenty-five dated incidents (Appendix G): what happened, what mechanism resulted. Read three now: the hollow antibody (June), presence-is-not-procedure (Aug 21), hooks that missed Bash writes (Aug 23).

### 9.5 What 2026 settled and what it did not

- Settled: the window is an engineered artifact; the harness is the product; evidence outranks narrative. Open: stagnation detection; harness fitness; the limit that self-dogfooding cannot falsify a strategic bet.

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| Harness engineering (as a practice) | 2026 | The product is the harness | Runtime, governance |
| Background agents | 2025–26 | Operations problems arrive | Runtime |
| gzkit | 2026 | The reference design, with receipts | All nine |

## Reference design: gzkit

gzkit is the subject of the whole chapter. The timeline and the casebook draw on `CHANGELOG.md`, `RELEASE_NOTES.md`, the ADR index, the ledger, and `.gzkit/insights/agent-insights.jsonl`.

## Readings

- gzkit `docs/governance/harness-engineering-appraisal.md`; `RELEASE_NOTES.md` (selected); `AGENTS.md` § Operator Doctrine.
- Sprint and Drift, "Turn and Face the Change"; "Newtonian motion."

## Exercises and Design Analysis prompts

1. Pick one incident from Appendix G and write the flight card that would have caught it before it shipped.



---

# 10. Building the Loop: Perceive, Reason, Act, Halt

> **Course use.** CIDM 6333 · E1. Status: **outline**.

## Learning outcomes

After this chapter you can:

- Build a minimal agent loop against a hosted and a local model.
- Emit structured outputs and enforce a halt condition and a budget.
- Write a PRD for your system through a governed interview.

## Outline

### 10.1 The minimal loop

- Messages, a model call, a tool-or-answer decision, an observation, repeat. Structured output through Pydantic. The loop stops on a final answer, an exhausted budget, the max-turn count, or an error.

### 10.2 Two foundations

- Hosted API vs. Ollama's endpoint: the same loop runs against both with a different capability behind it. Measure both.

### 10.3 Governing it from the first commit

- gz init; the PRD interview; the ledger's first events. Why the PRD states the WHAT and leaves the HOW to later decisions.

### 10.4 What can go wrong on day one

- Loops that do not halt; tool-call formats the small model cannot produce; silent exceptions. Each becomes a falsifier.

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| ReAct | 2022 | The loop you are reproducing | Planning |
| AutoGPT | 2023 | The loop without a halt | Planning |

## Reference design: gzkit

This chapter works from `gz init`, `gz prd`, the interview transcript, and the `prd_created` event in the ledger. gzkit's own PRD (PRD-GZKIT-1.0.0) serves as the worked example.

## Readings

- Anthropic, "Building Effective Agents."
- gzkit `docs/examples/guide-prd.md`; `docs/examples/tutorial-first-project.md` (with the CLI corrections in Appendix F).

## Flight card supported

Sortie 1 (center). DESIGN CLAIM: the loop halts on every input class (answerable, unanswerable, adversarial) within budget, and every turn is in the ledger. FALSIFIERS: a run exceeding the turn budget; a halt with no ledger event; a "final answer" produced without a reasoning turn.

## Exercises and Design Analysis prompts

1. Build the loop twice: once with your chosen SDK, once with only the HTTP API. Record what the SDK hid.



---

# 11. Patterns and Orchestration Frameworks: Who Owns the Loop?

> **Course use.** CIDM 6333 · E2. Status: **outline**.

## Learning outcomes

After this chapter you can:

- Implement the five workflow patterns and the agent pattern.
- Choose an orchestration framework and record the decision as an ADR with alternatives and consequences.
- Explain each framework's theory of control.

## Outline

### 11.1 The patterns

- Prompt chaining; routing; parallelization (sectioning, voting); orchestrator–workers; evaluator–optimizer; the agent. When each applies; the "keep it simple" advice.

### 11.2 Frameworks as theories of control

- Claude Agent SDK (vendor owns the loop); OpenAI Agents SDK (handoffs, guardrails); ADK (hierarchy, A2A); Pydantic AI (types as governance); LangGraph (you own every edge); none/stdlib (the reference design's posture).

### 11.3 Writing ADR-1

- Intent, decision, consequences (positive and negative), alternatives, decomposition scorecard, feature checklist. Write the ADR before the code. An ADR written after the code rationalizes what was already built.

### 11.4 Refactoring the loop into a pattern

- A worked example: turn the E1 loop into orchestrator–workers or evaluator–optimizer without changing the tool layer.

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| LangChain → LangGraph | 2022→24 | Chains became graphs with state | Coordination |
| Pydantic AI | 2024–25 | Typed outputs | Tools |
| AutoGen / CrewAI / MetaGPT | 2023 | Role orchestration | Coordination |
| OpenAI Agents SDK / Claude Agent SDK / ADK | 2025 | Vendor SDKs | Runtime |

## Reference design: gzkit

The reference material is `gz plan create --kind feature --semver --lane`, the decomposition scorecard, and the forcing functions (pre-mortem, WWHTBT, constraint archaeology). ADR-0.0.2 (argparse over click; "popularity is not rationale") serves as the model ADR.

## Readings

- OpenAI, "A Practical Guide to Building Agents."
- gzkit `docs/examples/guide-adr.md`; ADR-0.0.2.
- Sprint and Drift, "Enthusiasm Is All You Need."

## Flight card supported

Sortie 2 (center). DESIGN CLAIM: the same task runs under two patterns with identical tool traces and a measurable difference in cost or quality that the ADR predicted. FALSIFIER: the ADR's predicted consequence does not appear in the evidence.

## Exercises and Design Analysis prompts

1. Write ADR-1. Have a peer red-team it with the ten challenges (So what? Scope, Alternative, Dependency, Gold standard, Timeline, Evidence, Consumer, Regression, Parity).



---

# 12. Tools as Contracts: Schemas, Permissions, Hooks, Recovery

> **Course use.** CIDM 6333 · E3 (local model required). Status: **outline**.

## Learning outcomes

After this chapter you can:

- Declare tools with schema-validated contracts and handle failure and retry.
- Gate write-class tools behind a confirmation event recorded in a ledger.
- Explain hooks as a governance membrane and the 2026-08-23 lesson about enforcement locus.

## Outline

### 12.1 Declaring a tool

- Name, description, JSON schema, Pydantic model; idempotency; side-effect class (read, write, irreversible).

### 12.2 Permission gating

- Read freely; write with confirmation; irreversible with attestation. The confirmation event is written to the ledger before the call. A confirmation that is not in the ledger does not count as one.

### 12.3 Hooks

- Claude Code hook events (SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop, SessionEnd); gzkit's 17. What a hook can see and what it cannot: the Bash-write bypass, and why gzkit relocated write-side enforcement to the commit locus (`git diff --cached`).

### 12.4 Failure and recovery

- Timeouts, malformed calls, tool errors as observations; retry budgets; when to halt instead.

### 12.5 Small models and tools

- Why a local 8B model is the right substrate for this Evolution: a brittle model fails wherever the tool contract is loose, so its brittleness makes the contract visible.

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| Toolformer | 2023 | Learned calls | Tools |
| Function calling | 2023 | Declared calls | Tools |
| Gorilla / ToolBench | 2023 | Tool retrieval | Tools |
| Computer use | 2024 | Screen as tool | Perception, tools |
| Claude Code hooks | 2025 | The membrane | Governance |
| gzkit hooks | 2026 | Presence vs procedure; commit locus | Governance |

## Reference design: gzkit

This chapter reads `.claude/hooks/` as emitted by `gz init`, `pipeline-gate.py` and `verifier-pipe-gate.py`, the 2026-08-21 presence-check incident, and GHI #844/#847 (write-side fences moved to the commit locus).

## Readings

- Schick et al., "Toolformer."
- gzkit `.claude/hooks/README.md`; `.gzkit/rules/agent-failure-modes.md`; `CHANGELOG.md` v0.34.5.
- Sprint and Drift, "Get the Balance Right."

## Flight card supported

Sortie 3 (expansion). DESIGN CLAIM: no write-tool executes without a prior confirmation event. Four test points including a prompt-injected write request. FALSIFIERS: a write with no preceding confirmation; a file change after denial; passing only by disabling the gate.

## Exercises and Design Analysis prompts

1. Implement the gate as a hook in your harness *and* as a check in your own loop. Show a write that one catches and the other misses.



---

# 13. The Model Context Protocol: Building Servers and Clients

> **Course use.** CIDM 6333 · E4. Status: **outline**.

## Learning outcomes

After this chapter you can:

- Explain MCP's architecture (hosts, clients, servers) and primitives (tools, resources, prompts).
- Build an MCP server with the Python SDK and exercise it from two clients.
- Compare MCP to plugins, OpenAPI tool specs, and function calling, and say why a protocol won.

## Outline

### 13.1 Why a protocol

- N×M integrations → N+M; capability negotiation; discovery; the plugin era's failure.

### 13.2 Architecture and primitives

- Host, client, server; tools (model-controlled), resources (application-controlled), prompts (user-controlled); sampling; roots; notifications.

### 13.3 Building a server

- FastMCP-style declaration; schemas from types; stdio transport first; testing with an inspector; connecting to your harness and to a script client.

### 13.4 A governance server

- The reference design has no MCP server. This section builds the one it lacks: `gz status`, `gz validate`, the ledger, and receipts exposed as MCP tools and resources, with "what is attested?" as a resource. Why gzkit refused MCP, and what changes when you add it one tier up.

### 13.5 Design Analysis of the ecosystem

- Reference servers; registries; the foundation; what a healthy protocol ecosystem needs (ch. 14 for security).

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| ChatGPT plugins | 2023 | The pre-protocol attempt | Tools |
| OpenAPI-style tool specs | 2023– | Description without negotiation | Tools |
| MCP | 2024 | The protocol | Tools, coordination |
| Agentic AI Foundation | 2025 | Governance of the protocol | Governance |

## Reference design: gzkit

The doctrine is in `docs/governance/storage-tiers.md` ("no external protocol may become a prerequisite for core governance operations"). The pool ADR sketches an MCP context server, and the campaign review scores MCP "absent and un-designed." The student project is an MCP server over gz verbs and the ledger.

## Readings

- Model Context Protocol specification.
- MCP Python SDK documentation.
- Sprint and Drift, "Stop the presses, hail the autoloom."

## Flight card supported

Sortie 4 (center). DESIGN CLAIM: every tool the server declares is discoverable, callable, and schema-validated from two independent clients, and every call is logged server-side. FALSIFIERS: a tool callable from one client but not the other; a call with no server-side log; a schema the client accepted that the server rejected.

## Exercises and Design Analysis prompts

1. Build the governance MCP server. Ask your harness "what is attested in this repo?" and check its answer against the ledger.



---

# 14. Protocols, Security, and Harness Engineering

> **Course use.** CIDM 6333 · E5. Status: **outline**.

## Learning outcomes

After this chapter you can:

- Harden an MCP server: transports, authentication, scope, least privilege.
- Explain tool poisoning, prompt injection via resources, and confused-deputy attacks, and defend against them.
- Write instruction files and skills for your own system and explain the control-surface matrix.

## Outline

### 14.1 Transports and auth

- stdio vs. HTTP; OAuth; tokens and scopes; why the server must not trust the client's claims.

### 14.2 The threat model

- Tool descriptions as attack surface; resources carrying instructions; cross-server shadowing; confused deputy. Untrusted content doctrine: every observation is data, never instruction.

### 14.3 A2A and delegation

- Agents as peers: agent cards, tasks, artifacts. What distinguishes a peer from a tool, and where authority sits.

### 14.4 Instruction files and skills

- AGENTS.md / CLAUDE.md / GEMINI.md; path-scoped rules; skills as progressive disclosure; map-not-encyclopedia; the instruction budget.

### 14.5 Harness engineering

- The product is the harness. gzkit as a meta-harness renders one canon into each vendor's surfaces. Fidelity validation; the 258K context exhaustion; drift between mirrors.

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| MCP security incidents | 2025 | Tool poisoning, injection | Governance |
| A2A | 2025 | Peers, not tools | Coordination |
| AGENTS.md / Skills / hooks | 2025 | Control surfaces | Context, governance |
| gzkit meta-harness | 2026 | Rendering one canon into many harnesses | Governance |

## Reference design: gzkit

The chapter's sources in gzkit are `docs/design/agent-control-surface-matrix.md`, `docs/governance/agents-md-doctrine.md` (ADR-0.0.54), `untrusted-content.md`, `gz validate --instructions-files-budget --invariant-coherence`, and the corpus→rendition playback of AGENTS.md (ADR-0.0.37).

## Readings

- Anthropic, "Effective Harnesses for Long-Running Agents."
- gzkit `agents-md-doctrine.md`, `agent-control-surface-matrix.md`.
- Sprint and Drift, "The cost of the wrong abstraction went to zero."

## Flight card supported

Sortie 5 (corner). DESIGN CLAIM: an adversarial client cannot exceed the server's declared scope, and a poisoned resource cannot cause a write. FALSIFIERS: any out-of-scope call succeeding; any write following a resource-borne instruction; passing only by disabling a check.

## Exercises and Design Analysis prompts

1. Write the AGENTS.md for your system under a 4,000-character budget. Then measure what your harness actually loads.



---

# 15. Context Engineering: Budgets, Compaction, Handoffs, and Layers of Truth

> **Course use.** CIDM 6333 · E6. Status: **outline**.

## Learning outcomes

After this chapter you can:

- Instrument the context window and manage it under a budget.
- Implement compaction and a session handoff that preserves intent across a fresh session.
- Design an append-only ledger for your system and declare the three layers of truth.

## Outline

### 15.1 The window as an artifact

- What is in it: instructions, history, tool results, retrieved memory. Measure the window, then budget it.

### 15.2 Compaction and progressive disclosure

- Summarize, drop, page; subagents for isolation; skills loaded on demand; the PreCompact hook.

### 15.3 Handoffs

- Seven sections (current state, important context, decisions with attribution, next steps, pending work, verification checklist, evidence); rulings stores; session-start advisement; the exit bookmark.

### 15.4 Layers of truth

- L1 canon (markdown), L2 ledger (append-only events), L3 derived (status views, markers). Precedence L2 > L1 > L3; L3 can never block a gate. Frontmatter can carry a false status; the ledger is the record a gate consults.

### 15.5 Intent preservation as the design goal

- Why memory is not the same as preserved intent; the AGENTS.md-as-derived-view episode.

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| Claude Code (CLAUDE.md, compaction, subagents) | 2025 | Context surfaces | Context |
| Codex (AGENTS.md, compaction) | 2025 | Context surfaces | Context |
| Cursor rules | 2024–25 | Editor-native context | Context |
| gzkit handoffs / rulings / ledger | 2026 | Intent across boundaries | Context, governance |

## Reference design: gzkit

The reference material is `docs/governance/state-doctrine.md` (ADR-0.0.9), `gz handoff create/resume`, `scripts/session_orientation.py`, `.gzkit/handoffs/rulings.jsonl`, the 2026-04-26 stale-clone incident, and ADR-0.0.37 with ADR-0.0.54.

## Readings

- Anthropic, "Effective Context Engineering for AI Agents."
- gzkit `state-doctrine.md`; `docs/user/reference/agent-input-disciplines.md`.
- Sprint and Drift, "Woven."

## Flight card supported

Sortie 6 (expansion). DESIGN CLAIM: a handoff written at session end lets a fresh session resume with no loss of intent (measured: the next action taken is the one the handoff specified). FALSIFIERS: the fresh session asks a question the handoff answered; an L3 view contradicts the ledger and wins.

## Exercises and Design Analysis prompts

1. Compute your system's context budget per turn for a week. Where did it go?



---

# 16. Memory: Retrieval, State, Eviction, Retention

> **Course use.** CIDM 6333 · E7 (local model required). Status: **outline**.

## Learning outcomes

After this chapter you can:

- Distinguish short-term (window), working (state), and long-term (store) memory and implement each.
- Build retrieval over local embeddings and measure its effect.
- Write eviction and retention rules and justify them as governance.

## Outline

### 16.1 Kinds of memory

- Window; structured state; episodic (what happened); semantic (what is known); procedural (skills). Which of these your system needs.

### 16.2 Retrieval

- RAG as memory-by-lookup; chunking, embeddings (local), similarity, reranking; when retrieval hurts.

### 16.3 The 2023 designs revisited

- Generative Agents' memory stream and reflection; MemGPT's paging; Reflexion's memory of failure; Voyager's skill library.

### 16.4 Governance of memory

- Retention, deletion, provenance, and who owns it; memory as a vibing surface (stale facts recalled as truth); insights corpora as governed memory.

### 16.5 ADR-2

- The memory decision with alternatives; the personalized Final System brief follows this Evolution's Drift.

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| RAG | 2020 | Memory by retrieval | Memory |
| Generative Agents | 2023 | Stream, reflection, planning | Memory |
| MemGPT / Letta | 2023– | Virtual memory | Memory, context |
| Reflexion | 2023 | Memory of failure | Memory, evaluation |
| Assistant memory features | 2024– | Retention questions | Governance |

## Reference design: gzkit

This chapter draws on `.gzkit/insights/agent-insights.jsonl` (558 governed course-corrections) with `gz insights remember`, the OKF knowledge bundle, and `gz context`. The reference design keeps its memory in files and the ledger by deliberate choice; this book adds retrieval on top of that.

## Readings

- Lewis et al., "Retrieval-Augmented Generation" (2020).
- Park et al., "Generative Agents"; Packer et al., "MemGPT"; Shinn et al., "Reflexion."
- Sprint and Drift, "Code ergo sum."

## Flight card supported

Sortie 7 (expansion, local). DESIGN CLAIM: with memory enabled, the system answers a question about a prior session correctly that it cannot answer with memory disabled, and eviction removes what the retention rule says it removes. FALSIFIERS: a recalled fact that was never stored; a retained item past its rule; retrieval that changes an answer that should not change.

## Exercises and Design Analysis prompts

1. Poison your own memory store with one false fact and record how far it propagates.



---

# 17. Multi-Agent Coordination I: Controller, Worker, Reviewer

> **Course use.** CIDM 6333 · E8. Status: **outline**.

## Learning outcomes

After this chapter you can:

- Build an implementer–reviewer pair with personas and a fail-closed structured result contract.
- Orchestrate with a state graph and explain the checkpoints.
- Explain gzkit's pipeline stages and roles.

## Outline

### 17.1 Why more than one

- Context isolation; independent review; parallelism; the same division of labor (plan / do / check) under every name since FIPA.

### 17.2 Roles and personas

- Implementer, spec-reviewer, quality-reviewer, narrator; traits and anti-traits; no generic expertise claims; the Why parameter.

### 17.3 Contracts

- HandoffResult (DONE | DONE_WITH_CONCERNS | NEEDS_CONTEXT | BLOCKED); ReviewResult (PASS | FAIL | CONCERNS with findings); fail-closed parsing.

### 17.4 State graphs

- LangGraph (or equivalent): nodes, edges, checkpoints, human-in-the-loop interrupts; the supervisor pattern.

### 17.5 The reference pipeline

- Stage 1 load context → 2 implement (dispatch per task; two-stage review) → 3 verify → 4 present evidence → 5 sync. Dispatch records: "credit is never inferred."

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| FIPA / BDI | 1990s | The original vocabulary | Coordination |
| CAMEL / MetaGPT / AutoGen / CrewAI | 2023–24 | Roles | Coordination |
| LangGraph supervisor | 2024 | Graph orchestration | Coordination |
| Claude Code subagents | 2025 | Harness-native workers | Coordination |
| gzkit pipeline | 2026 | Controller–worker with review | Coordination, governance |

## Reference design: gzkit

The pipeline is specified in ADR-0.18.0 and `docs/user/concepts/subagent-pipeline.md` and implemented in `src/gzkit/roles.py` and `pipeline_dispatch.py`. The personas live in `.gzkit/personas/`. The `--single-driver --reason` honesty flag completes the set.

## Readings

- gzkit `subagent-pipeline.md`.
- Yang et al., "SWE-agent."
- Sprint and Drift, "Optimism's flames."

## Flight card supported

Sortie 8 (expansion). DESIGN CLAIM: no implementer output reaches the main branch without a reviewer verdict, and a FAIL verdict blocks. FALSIFIERS: merged work with no ReviewResult; a malformed result parsed as PASS; the reviewer's claim accepted without the evidence it cites.

## Exercises and Design Analysis prompts

1. Give your reviewer a persona with anti-traits. Then remove them and measure the verdicts.



---

