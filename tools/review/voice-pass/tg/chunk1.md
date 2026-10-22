# CIDM 6333 — Course Topic Guide and Textbook Outline

*Generated 2026-08-24 from the MkDocs source (textbook/). Each chapter is an outline with learning outcomes, sections, systems analyzed, the gzkit reference-design episode, readings, the flight card it supports, and exercises. Appendix H is the 60·60·30 run sheet.*

---

# Answerable Systems

## The Design, Lineage, and Governance of Agentic Software

**Jeffry Babb, PhD** · Paul and Virginia Engler College of Business · West Texas A&M University

*Working draft, Fall 2026. Written for CIDM 6333, Agentic Systems Design and Development, and for anyone who has to answer for a system that a model helped build.*

---

This book does three things at once because the course it grew out of does the same three things in the same term.

**It surveys.** Part II traces the lineage of agent systems from symbolic agents and reinforcement learning through the LLM-agent generation of 2023 to the harnesses, orchestration frameworks, and protocols of 2025 and 2026. Part II asks the same questions of every system: why was it designed this way, what problem did that design answer, and what did the design cost?

**It builds.** Part III takes one agentic system apart into its components (loop, patterns, tools, MCP, context, memory, coordination, evaluation, operations) and shows how to build each layer so that you can fly it against a falsifiable claim and defend it without the tool in front of you.

**It governs.** Part I and Part IV describe the posture that keeps the other two honest: the human at index zero, the covenant, the five gates, Sprint and Drift, flight cards, the Design Analysis, and the closeout ceremony. The reference design throughout is gzkit, the GovZero Kit, because it is the one system for which this book has the entire record, including the record of what went wrong.

The title states the thesis: a system can produce an answer without being able to answer for it. The engineer's role, the one no tool takes over, is to answer for the system. The survey, the build, and the governance chapters all serve that purpose.

### How to read this book

- **As a course text.** The [week-by-week run sheet] maps every CIDM 6333 Evolution to its chapters. Read the Part II chapter for the week's survey and the Part III chapter for the week's build.
- **As a survey.** Read Part II straight through, then dip into Part III where a component interests you.
- **As a flight manual.** Read Part IV first, then use Part III chapter by chapter with the flight cards in Appendix A.

### Conventions

- **Design Analysis** boxes show a system dissected against the nine components ([method]).
- **Flight card** boxes give the falsifiable claim, test points, instrumentation, and falsifiers for a chapter's build ([method]).
- **Reference design** sections show what gzkit did about the chapter's problem, with the dated incident where one exists.
- **Judgment loop** closers (from CIDM 6330): state the decision, the characteristics privileged, the cost, the failure mode, and the preservation mechanism.

### Status

Every chapter carries a status line: *outline*, *draft*, *reviewed*, *final*. This is a working text. The outlines are complete, and I am writing the prose in the order the course needs it.


---

# Preface

## Why this book exists

In January 2026 I started a governance kit with eleven days to go before I would show it to students. By August it had been through seventy-six releases, eighty-seven decision records, five hundred and forty-two work briefs, and fifteen thousand ledger events, and it had accumulated a dated record of every way an agent can look finished without being finished: attestations for code that did not exist, hooks that never saw the write they were guarding, a pipeline gate that only checked that a marker file was present, a ten-deep chain of subagents whose polished summaries became "facts." None of those failures was exotic. They are the ordinary failure modes of agentic systems, and the systems built in industry have them too. The kit differs in that its ledger kept the receipts for each one.

That record is the spine of this book. Around it is a survey, because the kit's design choices only make sense against the choices the field made before it, and a build, because a reader understands a component only after making it fail on purpose.

## What this book is not

This book is not a framework tutorial. Frameworks change too often for a tutorial to stay current, and each one encodes a theory of control, which is the real subject. It is not a prompt-engineering book, and it is not an AI-safety book in the policy sense, although Part I situates the engineering posture against that literature. The book takes a position: the human is index zero, first in priority and final in authority, and a system whose human cannot answer for it is not finished.

## Acknowledgements and lineage

I developed Sprint and Drift, the method of Part IV, for CIDM 6330 (Software Architecture). The Evolution structure and the consultation rhythm come from CIDM 6395 (the MS-CISBA capstone). GovZero came from roughly a hundred work items of governed development in an airline-operations project. gzkit is its standalone descendant, with lineage from GitHub's spec-kit and the CLAUDE.md conventions. The flight-test program borrows its vocabulary from aircraft flight test, with apology to test pilots. The essays that open each chapter first appeared in the *Sprint and Drift* newsletter.


---

# Using this book with CIDM 6333

The course runs thirteen Thursdays, 4:00–6:30 p.m., one Evolution per week. Each Evolution carries two threads:

| Thread | Instrument | Chapter home |
|---|---|---|
| **Survey**: why are agentic systems designed the way they are? | The Design Analysis (nine components, one "why") | Part II, and the *Systems analyzed* table in every Part III chapter |
| **Build**: one individual system, one layer per week | The flight card and flight log | Part III, one chapter per Evolution |

The weekly rhythm (lecture 60 · consultation 60 · lab 30), the Sprint and Drift method, and the scoring live in Part IV and in the [run sheet].

## Chapter-to-Evolution map

| Evolution | Survey chapters | Build chapter | Method chapters |
|---|---|---|---|
| E0 Orientation | 1, 2, 3 | none | 22, 23, 24 |
| E1 The agent loop | 5 | 10 | 25 (init, PRD) |
| E2 Patterns and frameworks | 6, 8 | 11 | 25 (ADR) |
| E3 Tools | 6 | 12 | 23 |
| E4 MCP I | 7 | 13 | none |
| E5 MCP II, protocols, harness | 8, 9 | 14 | none |
| E6 Context | 8 | 15 | 25 (handoff) |
| E7 Memory | 6 | 16 | 26 (brief issued) |
| E8 Multi-agent I | 4, 6 | 17 | 25 (subagents) |
| E9 Multi-agent II | 9 | 18 | none |
| E10 Evaluation I | 7 | 19 | 23 |
| E11 Evaluation II | 9 | 20 | none |
| E12 Deployment | 9 | 21 | 25 (closeout) |
| Finals | none | none | 26 |


---

# 1. The Layers of AI, and the One Everybody Forgets

> **Course use.** CIDM 6333 · E0 Orientation. Status: **outline**.

## Learning outcomes

After this chapter you can:

- Place any AI system on the seven-layer stack and say which layers it actually exercises.
- Explain the five-stage progression from AI & ML to agentic AI and what changes at each step.
- Recognize when a system labelled "agentic" is a generative system with a loop bolted on, and say why that matters.

## Outline

### 1.1 The stack

- Data foundation (ownership, definitions, quality, lineage) → classical AI → ML → neural networks → deep learning → generative AI → agentic AI.
- Each layer stands on the one below, and none replaces it. The agentic layer is the newest and thinnest, and the data foundation is the oldest and the one with the defects.
- Designers neglect the foundation because it is unglamorous, and the cost lands there (E7 and E11 return to it).

### 1.2 The progression

- AI & ML: turn data into decisions. Deep learning: multi-layered networks. Gen AI: create new content. AI agents: autonomous tasks. Agentic AI: automate entire processes.
- The Agentic AI framework board: rings (foundation, creation, core systems, action, full automation) and columns. The table assigns every box a chapter.

### 1.3 What a language model adds and what it does not

- The model is a reasoner that generalizes from text. It has no persistent state, no ground truth, and no accountability, and the stack above it (tools, memory, evaluators, governance) exists to supply those three.
- The Newtonian-motion argument: generated code defers its cost rather than removing it.

### 1.4 Reading a system top-down and bottom-up

- Read a system in two passes: from the top, what does it claim to do, and from the bottom, what does it stand on. Worked example: a chat assistant vs. an agent harness.

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| A chat assistant (any vendor) | 2022– | The baseline: generative, no loop, no tools | Foundation, perception |
| Claude Code / Codex CLI | 2025 | What makes it an agent: loop, tools, permissions, harness | All nine |

## Reference design: gzkit

gzkit sits on the *agentic* layer and runs no model of its own. It is a governance meta-harness one tier above the vendor harness, and that placement is the first design choice the book examines.

## Readings

- Sprint and Drift, "Tree Hollow."
- gzkit `docs/user/why.md` (the Degradation Pattern) and `docs/examples/glossary.md`.
- The two framework images (Layers of AI; Agentic AI: A Complete Framework).

## Exercises and Design Analysis prompts

1. Write the E0 Design Analysis: a chat assistant versus an agent harness, nine components each. Add one paragraph on what the harness adds and what it costs.
2. Take the framework board and mark every box for which you can already give a concrete system. The boxes you leave blank are your reading list.



---

# 2. What Is an Agent? From PEAS to the Nine Components

> **Course use.** CIDM 6333 · E0 Orientation. Status: **outline**.

## Learning outcomes

After this chapter you can:

- Give the pre-LLM definition of an agent and specify one by PEAS.
- Describe the LLM agent loop and identify its halt condition.
- Dissect any agentic system into the nine components used throughout the book.

## Outline

### 2.1 The classical definition

- Russell & Norvig: perceives through sensors, acts through actuators; PEAS. Agent types: reflex, model-based, goal-based, utility-based, learning.
- BDI (belief–desire–intention) and multi-agent platforms as the pre-LLM coordination vocabulary.

### 2.2 The LLM agent loop

- Perceive (prompt, tool results) → reason (model call) → act (tool call or answer) → repeat until halt. ReAct as canonical form.
- Halt conditions, budgets, and why the systems of 2023 omitted them.

### 2.3 The nine components

- Foundation; perception; planning and reasoning; tool use and orchestration; memory and context; coordination; evaluation and feedback; governance and human interface; runtime and operations.
- For each: the question to ask, the typical answers, the failure that shows up when it is missing.

### 2.4 Workflows versus agents

- Anthropic's distinction: predefined code paths vs. model-directed control. Anthropic's own advice is to build the workflow unless the task needs the agent's flexibility, and a system marketed as an "agent" may be a workflow by this definition (exercise 2).

### 2.5 The judgment loop

- From CIDM 6330: state the decision, the characteristics, the cost, the failure mode, and the preservation mechanism. Every Design Analysis closes with it.

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| Russell & Norvig agent | 1995– | The definition that still holds | Perception, planning |
| ReAct | 2022 | The loop in its simplest form | Planning, tools |

## Reference design: gzkit

gzkit answers component eight (governance and human interface) with the Zero Doctrine and Gate 5, and component seven (evaluation) with gates, receipts, and RED witnesses. It deliberately leaves components one through six to the vendor harness.

## Readings

- Russell & Norvig, *Artificial Intelligence: A Modern Approach*, ch. 2 (any edition).
- Anthropic, "Building Effective Agents" (2024), sections on workflows vs. agents.
- Yao et al., "ReAct" (2022).

## Exercises and Design Analysis prompts

1. Specify your intended system by PEAS. Then map each PEAS element to one of the nine components.
2. Find a system marketed as an agent that is a workflow. Say why that is the right design.



---

# 3. The Human at Index Zero: Degradation, Covenant, Gates

> **Course use.** CIDM 6333 · E0 Orientation; revisited E5, E9, E11. Status: **outline**.

## Learning outcomes

After this chapter you can:

- Describe the Degradation Pattern and recognize it in your own practice.
- State the covenant and the Zero Doctrine and explain the two-sided obligation.
- Explain the five gates, the two lanes, and why human attestation cannot be automated.
- Situate the engineering posture against the AI-governance literature.

## Outline

### 3.1 The Degradation Pattern

- Week 1 to week 4: careful review → skimming → batch approvals → rubber stamp. "You didn't lose control in one dramatic moment."
- Cognitive surrender, mediated observation, governance theater: three names for the same failure.

### 3.2 The Zero Doctrine

- The human is index zero: first in priority, final in authority, cannot be automated away. Evolution of "zero": zero overhead → zero drift → index zero.
- Two sides of the covenant: gates constrain agents, and humans must engage. Read everything, and insist on Q&A.

### 3.3 The covenant and the three concerns

- Specification (agent-native), methodology (process-native), governance (human-native). "Specification without governance drifts; governance without methodology is theater; methodology without specification is arbitrary."
- Legislature / executive / judiciary as a constitutional metaphor.

### 3.4 Five gates, two lanes

- ADR, TDD, Docs, BDD, Human. Lite = 1–2. Heavy = 1–5. Ceremony must earn its place. Closed attestation vocabulary.
- Why Gate 5 is universal at the brief level and why there is no self-close path (ADR-0.0.36).

### 3.5 Command doctrine

- Aviation's Four P's (Degani & Wiener) as the model: philosophy → policies → procedures → practices. The four tenets of the command doctrine: accountability is non-transferable, authority must be instrumented rather than asserted, the model is a crew resource rather than a crew member, and evidence is artifacts rather than narration.

### 3.6 Against the governance literature

- NIST AI RMF, EU AI Act, ISO 42001, frontier-lab safety frameworks and system cards. The accountability gap that the practitioner literature (Raji et al.; "Auditing Work") identifies. Where an engineering covenant fits and where it does not.

## Reference design: gzkit

This chapter is itself the reference design's doctrine, set out in four documents: charter, lineage, genesis, and command doctrine. The genesis conversation (2026-01-12) records the model saying that "for maximizing Claudishness, only specification matters" and the operator insisting on all three concerns. That exchange is the book's founding episode.

## Readings

- gzkit `docs/user/reference/charter.md`, `lineage.md`, `genesis.md`; `docs/governance/GovZero/command-doctrine.md`; `docs/governance/ai-governance-brief.md` (§§5, 7, 8).
- Degani & Wiener (1997), "Philosophy, policies, procedures and practices."
- Sprint and Drift, "Who answers for the code"; "Code ergo sum."

## Exercises and Design Analysis prompts

1. Keep a one-week log of your own review behavior on AI-generated output. Where on the four-week curve are you?
2. Rewrite the covenant's five clauses for your own system: who defines intent, what constrains the agent, what verifies, who attests, what survives the session.



---

# 4. Before Language Models: Symbolic, BDI, Multi-Agent, and Reinforcement-Learning Agents

> **Course use.** CIDM 6333 · E0 background; E8 survey. Status: **outline**.

## Learning outcomes

After this chapter you can:

- Summarize the pre-LLM agent traditions and what each contributed.
- Recognize classical coordination vocabulary (FIPA, contract net, BDI) in modern multi-agent frameworks.
- Explain what reinforcement-learning agents got right about environments and reward that LLM agents lost.

## Outline

### 4.1 Symbolic agents and expert systems

- Production rules, knowledge representation, planning (STRIPS). Why brittleness ended the era and why the ideas returned as "planning" in LLM agents.

### 4.2 BDI and the agent-oriented programming movement

- Beliefs, desires, intentions. Commitment and reconsideration. Direct ancestors of "goal decomposition" and "intent preservation."

### 4.3 Multi-agent systems

- FIPA, JADE, contract-net protocol, blackboard architectures. Message passing, roles, negotiation. Read these before AutoGen and CrewAI, which reuse the same designs.

### 4.4 Reinforcement-learning agents

- Environment, reward, policy. Sample efficiency and reward hacking. LLM agents inherit the lesson that gaming the gate is not new (failure mode 9).

### 4.5 What carried forward, what was dropped

- Carried: PEAS, planning, coordination protocols. Dropped, then rediscovered: explicit state, halt conditions, evaluation against an environment.

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| STRIPS / expert systems | 1970s–80s | Planning and rules | Planning |
| BDI / AgentSpeak | 1990s | Intent as a first-class object | Planning, governance |
| FIPA / JADE / contract net | 1990s–2000s | Coordination protocols | Coordination |
| RL agents (DQN era) | 2013– | Environment, reward, gaming | Evaluation |

## Reference design: gzkit

gzkit's personas, locks, and structured result contracts are FIPA-shaped. Its "intent preservation across context boundaries" is BDI's commitment problem, with a ledger added to record the commitment.

## Readings

- Russell & Norvig, chs. 2, 11 (planning), and a multi-agent chapter.
- Rao & Georgeff on BDI (1995); Wooldridge, *An Introduction to MultiAgent Systems* (selected).
- Sutton & Barto, ch. 1.

## Exercises and Design Analysis prompts

1. Design Analysis: a JADE agent against a CrewAI agent. Which components changed? Which merely got renamed?



---

# 5. The Loop: Chain-of-Thought, ReAct, and the First Frameworks (2020–2022)

> **Course use.** CIDM 6333 · E1. Status: **outline**.

## Learning outcomes

After this chapter you can:

- Explain how prompting became a control structure.
- Read the ReAct paper as a design document and list its components.
- Say what LangChain wrapped, and why the wrapper later became a graph.

## Outline

### 5.1 From prompting to programs

- GPT-3 few-shot prompting. Chain-of-thought (Wei et al., 2022) as latent planning. Self-consistency.

### 5.2 ReAct

- Reasoning traces interleaved with actions. The thought–action–observation loop, which halts on a final answer. Component map. What it lacked: memory, budget, verification.

### 5.3 The first frameworks

- LangChain (late 2022): chains, agents, tools, memory as objects. The abstraction tax and why it drove practitioners to state graphs (ch. 11).

### 5.4 Design lessons

- A loop without a halt condition runs until the budget is spent, so the halt condition is the cost control. Observations are perception, and the harness treats them as untrusted input (ch. 14).

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| Chain-of-thought | 2022 | Reasoning as an emitted artifact | Planning |
| ReAct | 2022 | The canonical loop | Planning, tools |
| LangChain | 2022 | The first wrapper | Coordination, runtime |

## Reference design: gzkit

gzkit's genesis (2026-01-12) is the ReAct loop plus the one thing that loop lacked, a record of intent that survives the session. Read the genesis transcript alongside ReAct.

## Readings

- Wei et al., "Chain-of-Thought Prompting" (2022).
- Yao et al., "ReAct" (2022).
- Anthropic, "Building Effective Agents" (2024).
- Sprint and Drift, "Who answers for the code."

## Flight card supported

Sortie 1 (center): *a governed agent loop that halts*. See ch. 10.

## Exercises and Design Analysis prompts

1. Implement ReAct in under 80 lines against a local model. Add a budget. Remove the halt condition and record what happens.
2. Design Analysis: ReAct.



---

# 6. The Explosion of 2023: Tools, Autonomy, Memory, Roles

> **Course use.** CIDM 6333 · E2, E3, E7, E8 survey. Status: **outline**.

## Learning outcomes

After this chapter you can:

- Trace the 2023 generation system by system and the problem each answered.
- Explain why AutoGPT and BabyAGI spiraled and what the field learned.
- Distinguish learned tool use (Toolformer) from declared tool use (function calling).
- Describe the memory and role-based designs that anticipated 2025.

## Outline

### 6.1 Tools

- Toolformer (Feb): the model teaches itself API calls. OpenAI function calling (Jun): the API declares the schema. Gorilla and ToolBench: tool retrieval at scale. ChatGPT plugins as the first tool store, and why it failed.

### 6.2 Autonomy

- AutoGPT, BabyAGI (Mar–Apr): loops with goals and no grounding, budget, or evaluator. The spiral. They mattered anyway, because they stated the ambition the field then pursued.

### 6.3 Reflection and memory

- Reflexion (episodic memory of failure). Voyager (skill library). Generative Agents (memory stream, reflection, planning). MemGPT (the OS metaphor: paging context). Tree of Thoughts.

### 6.4 Roles

- CAMEL, MetaGPT (SOPs as prompts), AutoGen (conversation as coordination). FIPA rediscovered.

### 6.5 The year's design lesson

- Every one of the nine components appeared in 2023, and none appeared together with governance. The harness year (ch. 8) and the reference design fill that gap.

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| Toolformer | 2023 | Learned tool use | Tools |
| OpenAI function calling | 2023 | Declared tool use | Tools |
| AutoGPT / BabyAGI | 2023 | Autonomy without a halt | Planning, evaluation |
| Reflexion | 2023 | Memory of failure | Memory, evaluation |
| Voyager | 2023 | Skill library | Memory, tools |
| Generative Agents | 2023 | Memory stream and reflection | Memory |
| MemGPT | 2023 | Context as virtual memory | Memory, context |
| CAMEL / MetaGPT / AutoGen | 2023 | Role-based coordination | Coordination |

## Reference design: gzkit

gzkit's controller–worker pipeline (ADR-0.18.0) explicitly borrows from role-based designs, then adds what they lacked: a fail-closed result contract and an independent reviewer whose claim is not evidence.

## Readings

- Schick et al., "Toolformer" (2023).
- Shinn et al., "Reflexion" (2023).
- Park et al., "Generative Agents" (2023).
- Packer et al., "MemGPT" (2023).
- Wu et al., "AutoGen" (2023); Hong et al., "MetaGPT" (2023).

## Exercises and Design Analysis prompts

1. Design Analysis: AutoGPT. Which of the nine components was absent, and which absence caused the spiral?
2. Design Analysis: MemGPT vs. your harness's compaction. Same problem, different decade?



---

# 7. Agents Get Jobs (2024): Coding Agents, Computer Use, and MCP

> **Course use.** CIDM 6333 · E4, E10 survey. Status: **outline**.

## Learning outcomes

After this chapter you can:

- Explain how SWE-bench changed what "agent" meant.
- Compare SWE-agent, Devin, OpenHands, Aider, and Cursor as designs.
- Describe computer use as "the screen is a tool."
- Explain why MCP is a client–server protocol and what problem it answered.

## Outline

### 7.1 Benchmarks as forcing functions

- SWE-bench (and Verified): resolved-issue rate as the number that mattered. What benchmarks hide (ch. 19).

### 7.2 Coding agents

- SWE-agent (agent–computer interface design), Devin (the demo that set expectations), OpenHands (open reference), Aider (repo-map, git-native), Cursor (editor-native). Agentless as the counter-argument: a workflow beat the agents.

### 7.3 Computer use

- Screenshots as perception, clicks as actions. Latency, cost, and safety trade-offs.

### 7.4 MCP

- November 2024: hosts, clients, and servers. Tools, resources, and prompts. Capability negotiation. Transports. Why a protocol rather than a plugin format. Reference servers and the community of servers around them. Governance transferred to a foundation (2025).

### 7.5 The pattern vocabulary

- Anthropic, "Building Effective Agents" (Dec 2024): the five workflow patterns and the agent, and the advice to keep it simple. LangGraph: the agent as a state graph. Reasoning models change the planning component.

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| SWE-bench / SWE-agent | 2024 | Benchmark and ACI design | Perception, tools, evaluation |
| Devin / OpenHands | 2024 | The autonomous coding agent | All nine |
| Aider / Cursor | 2024 | Repo- and editor-native | Perception, tools |
| Agentless | 2024 | A workflow that beat agents | Planning |
| Claude computer use | 2024 | Screen as tool | Perception, tools |
| MCP | 2024 | The tool protocol | Tools, coordination |
| LangGraph | 2024 | State graphs | Coordination, runtime |

## Reference design: gzkit

gzkit does not use MCP, by doctrine: no external protocol may be a prerequisite for core governance operations. The book treats that refusal as a design choice for analysis, and offers "an MCP server over gz verbs and the ledger" as a student project (ch. 13).

## Readings

- Yang et al., "SWE-agent" (2024).
- Xia et al., "Agentless" (2024).
- Model Context Protocol specification (architecture; server primitives).
- Anthropic, "Building Effective Agents" (2024).

## Exercises and Design Analysis prompts

1. Design Analysis: SWE-agent's agent–computer interface. Which perception choices raised the resolve rate?
2. Design Analysis: MCP as a system. Where is the human?



---

