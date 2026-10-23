# CIDM 6333: Course Topic Guide and Textbook Outline

*Generated 2026-08-24 from the MkDocs source (textbook/). Each chapter is an outline with learning outcomes, sections, systems analyzed, the gzkit reference-design episode, readings, the flight card it supports, and exercises. Appendix H is the 60·60·30 run sheet.*

---

# Answerable Systems

## The Design, Lineage, and Governance of Agentic Software

**Jeffry Babb, PhD** · Paul and Virginia Engler College of Business · West Texas A&M University

*Working draft. Written for CIDM 6333, Agentic Systems Design and Development, and for anyone who has to answer for a system that a model helped build.*

---

This book does three things at once because the course it grew out of does the same three things.

**It surveys.** Part II traces the lineage of agent systems from symbolic agents and reinforcement learning through the LLM-agent generation of 2023 to the harnesses, orchestration frameworks, and protocols of 2025 and 2026. Part II asks the same questions of every system: why was it designed this way, what problem did that design answer, and what did the design cost?

**It builds.** Part III takes one agentic system apart into its components (loop, patterns, tools, MCP, context, memory, coordination, evaluation, operations) and shows how to build each layer so that you can fly it against a falsifiable claim and defend it without the tool in front of you.

**It governs.** Part I and Part IV describe the posture that keeps the other two honest: the human at index zero, the covenant, the five gates, Sprint and Drift, flight cards, the Design Analysis, and the closeout ceremony. The reference design throughout is gzkit, the GovZero Kit, because it is the one system for which this book has the entire record, including the record of what went wrong.

The title states the thesis: a system can produce an answer without being able to answer for it. No tool can take over the engineer's role, which is to answer for the system. Everything in this book serves the building of systems, and of engineers, that can answer.

### How to read this book

- **As a course text.** Each CIDM 6333 lecture links to its chapters, and each chapter lists the lectures that use it. Read the Part II chapter for the Evolution's survey and the Part III chapter for its build.
- **As a survey.** Read Part II straight through, then dip into Part III where a component interests you.
- **As a flight manual.** Read Part IV first, then use Part III chapter by chapter with the flight cards in Appendix A.

### Conventions

- **Design Analysis** boxes show a system dissected against the nine components ([method]).
- **Flight card** boxes give the falsifiable claim, test points, instrumentation, and falsifiers for a chapter's build ([method]).
- **Reference design** sections show what gzkit did about the chapter's problem, with the dated incident where one exists.
- **Judgment loop** closers (from CIDM 6330): state the decision, the characteristics privileged, the cost, the failure mode, and the preservation mechanism.

### Status

This is a living text. The chapters expand and elaborate over time, as the course needs them.


---

# Preface

## Why this book exists

In January 2026 I started a governance kit with eleven days to go before I would show it to students. By August it had been through seventy-six releases, eighty-seven decision records, five hundred and forty-two work briefs, and fifteen thousand ledger events, and it had accumulated a dated record of every way an agent can look finished without being finished: attestations for code that did not exist, hooks that never saw the write they were guarding, a pipeline gate that only checked that a marker file was present, a ten-deep chain of subagents whose polished summaries became "facts." None of those failures was exotic. They are the ordinary failure modes of agentic systems, and the systems built in industry have them too. The difference is that this kit kept the receipts.

That record is the spine of this book. Around it is a survey, because the kit's design choices only make sense against the choices the field made before it, and a build, because a reader understands a component only after making it fail on purpose.

## What this book is not

This book is not a framework tutorial. Frameworks change too often for a tutorial to stay current, and each one encodes a theory of control, which is the real subject. It is not a prompt-engineering book, and it is not an AI-safety book in the policy sense, although Part I situates the engineering posture against that literature. The book takes a position: the human is index zero, first in priority and final in authority, and a system whose human cannot answer for it is not finished.

## Acknowledgements and lineage

I developed Sprint and Drift, the method of Part IV, for CIDM 6330 (Software Architecture). The Evolution structure and the consultation rhythm come from CIDM 6395 (the MS-CISBA capstone). GovZero came from roughly a hundred work items of governed development in an airline-operations project. gzkit is its standalone descendant, with lineage from GitHub's spec-kit and the CLAUDE.md conventions. The flight-test program borrows its vocabulary from aircraft flight test, with apology to test pilots. The essays that open each chapter first appeared in the *Sprint and Drift* newsletter.


---

# Using this book with CIDM 6333

The course runs one Evolution per week. Each Evolution carries two threads:

| Thread | Instrument | Chapter home |
|---|---|---|
| **Survey**: why are agentic systems designed the way they are? | The Design Analysis (nine components, one "why") | Part II, and the *Systems analyzed* table in every Part III chapter |
| **Build**: one individual system, one layer per week | The flight card and flight log | Part III, one chapter per Evolution |

The Sprint and Drift method and the scoring are in Part IV.

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

> **Course use.** CIDM 6333 · E0 Orientation.

## Learning outcomes

After this chapter you can:

- Place any AI system on the seven-layer stack and say which layers it actually exercises.
- Explain the five-stage progression from AI & ML to agentic AI and what changes at each step.
- Recognize when a system labelled "agentic" is a generative system with a loop bolted on, and say why that matters.

## Outline

### 1.1 The stack

- Data foundation (ownership, definitions, quality, lineage) → classical AI → ML → neural networks → deep learning → generative AI → agentic AI.
- Each layer stands on the one below, and none replaces it. The agentic layer is new and thin, and the data foundation is old and has defects.
- Designers neglect the foundation because it is unglamorous, and the cost lands there (E7 and E11 return to it).

### 1.2 The progression

- AI & ML: turn data into decisions. Deep learning: multi-layered networks. Gen AI: create new content. AI agents: autonomous tasks. Agentic AI: automate entire processes.
- The Agentic AI framework board: rings (foundation, creation, core systems, action, full automation) and columns. The table assigns every box a chapter.

### 1.3 What a language model adds and what it does not

- The model is a reasoner that generalizes from text. It has no persistent state, no ground truth, and no accountability, and the stack above it (tools, memory, evaluators, governance) exists to supply those three.
- The Newtonian-motion argument: generated code defers its cost rather than removing it.

### 1.4 Reading a system top-down and bottom-up

- Read a system in two passes: from the top, ask what it claims to do; from the bottom, ask what it stands on. Worked example: a chat assistant vs. an agent harness.

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| A chat assistant (any vendor) | 2022– | The baseline: generative, no loop, no tools | Foundation, perception |
| Claude Code / Codex CLI | 2025 | What makes it an agent: loop, tools, permissions, harness | All nine |

## Reference design: gzkit

gzkit sits on the *agentic* layer and runs no model. It is a governance meta-harness, a custom harness built on top of the vendor harness, and that placement is the first design choice the book examines.

## Readings

- Sprint and Drift, "Tree Hollow."
- gzkit `docs/user/why.md` (the Degradation Pattern) and `docs/examples/glossary.md`.
- The two framework images (Layers of AI; Agentic AI: A Complete Framework).

## Exercises and Design Analysis prompts

1. Write the E0 Design Analysis: a chat assistant versus an agent harness, nine components each. Add one paragraph on what the harness adds and what it costs.
2. Take the framework board and mark every box for which you can already give a concrete system. The boxes you leave blank are your reading list.



---

# 2. What Is an Agent? From PEAS to the Nine Components

> **Course use.** CIDM 6333 · E0 Orientation.

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
2. Find a system marketed as an agent that is a workflow. Say whether a workflow is the right design for it, and why.



---

# 3. The Human at Index Zero: Degradation, Covenant, Gates

> **Course use.** CIDM 6333 · E0 Orientation; revisited E5, E9, E11.

## Learning outcomes

After this chapter you can:

- Describe the Degradation Pattern and recognize it in your own practice.
- State the covenant and the Zero Doctrine and explain the two-sided obligation.
- Explain the five gates, the two lanes, and why human attestation cannot be automated.
- Situate the engineering posture against the AI-governance literature.

## Outline

### 3.1 The Degradation Pattern

- Week 1 to week 4: careful review → skimming → batch approvals → rubber stamp. "You didn't lose control in one dramatic moment."
- Cognitive surrender, mediated observation, governance theater: three related failures.

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

- NIST AI RMF, EU AI Act, ISO 42001, frontier-lab safety frameworks and system cards. The accountability gap that the practitioner literature (Raji et al., 2022; Groves et al., 2024) identifies. Where an engineering covenant fits and where it does not.

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

> **Course use.** CIDM 6333 · E0 background; E8 survey.

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

- FIPA, JADE, contract-net protocol, blackboard architectures. Message passing, roles, negotiation. Read these before AutoGen and CrewAI, which repeat the same designs.

### 4.4 Reinforcement-learning agents

- Environment, reward, policy. Sample efficiency and reward hacking. Reward hacking in RL agents shows that gaming the gate is not new to LLM agents (failure mode 9).

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

> **Course use.** CIDM 6333 · E1.

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

- A loop without a halt condition keeps calling the model, and each call costs money, until someone stops it. Observations are perception, and the harness treats them as untrusted input (ch. 14).

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| Chain-of-thought | 2022 | Reasoning as an emitted artifact | Planning |
| ReAct | 2022 | The canonical loop | Planning, tools |
| LangChain | 2022 | The first wrapper | Coordination, runtime |

## Reference design: gzkit

gzkit's genesis (2026-01-12) is the ReAct loop plus a component that loop lacked: a record of intent that survives the session. Read the genesis transcript alongside ReAct.

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

> **Course use.** CIDM 6333 · E2, E3, E7, E8 survey.

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

- AutoGPT, BabyAGI (Mar–Apr): loops with goals and no grounding, budget, or evaluator. The spiral. They mattered anyway, because they stated the ambition.

### 6.3 Reflection and memory

- Reflexion (episodic memory of failure). Voyager (skill library). Generative Agents (memory stream, reflection, planning). MemGPT (the OS metaphor: paging context). Tree of Thoughts.

### 6.4 Roles

- CAMEL, MetaGPT (SOPs as prompts), AutoGen (conversation as coordination). FIPA rediscovered.

### 6.5 What 2023 lacked

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

> **Course use.** CIDM 6333 · E4, E10 survey.

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

# 8. The Harness Year (2025): Claude Code, Codex, the SDKs, A2A, AGENTS.md, Skills, and Context Engineering

> **Course use.** CIDM 6333 · E2, E5, E6 survey.

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

- A2A (agents as peers) vs. MCP (tools). AGENTS.md as the cross-vendor instruction file. Agent Skills as progressive disclosure. Hooks as enforcement points around tool calls.

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

> **Course use.** CIDM 6333 · E5, E9, E11, E12 survey.

## Learning outcomes

After this chapter you can:

- Describe harness engineering as a discipline and state what it asserts.
- Explain long-running and background agents and their operational problems.
- Narrate gzkit's arc from genesis to the measurement era and extract the lessons.

## Outline

### 9.1 Harness engineering

- The claim that most of an agent product is not the model. Readings: Böckeler; the OpenAI post. gzkit's appraisal of that position, and the blind spots the appraisal records (harness fitness unmeasured; an illusion of quality produced by heavy gates).

### 9.2 Background and long-running agents

- Cloud sessions, scheduled tasks, compaction across days; the operational questions: scheduling, rollback, cost, who attests.

### 9.3 The reference design's arc

- Jan genesis → hooks → OBPI pipeline → CMS → subagents and personas → three layers of truth → receipts and patch cadence → universal attestation → map-not-encyclopedia → V.I.B.E.S. → Magna Carta → repudiations and the MX hangar → airlock → foundation sunset → measurement era and commit-locus enforcement.

### 9.4 The incident casebook (pointer)

- Twenty-one dated incidents (Appendix G): what happened, what mechanism resulted. Read three now: the hollow antibody (June), presence-is-not-procedure (Aug 21), hooks that missed Bash writes (Aug 23).

### 9.5 What 2026 settled and what it did not

- Settled: the window is an engineered artifact; the harness is the product; evidence outranks narrative. Open: stagnation detection; harness fitness; the limit that self-dogfooding cannot falsify a strategic bet.

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| Harness engineering (as a practice) | 2026 | The product is the harness | Runtime, governance |
| Background agents | 2025–26 | Operational problems arrive | Runtime |
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

> **Course use.** CIDM 6333 · E1.

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

> **Course use.** CIDM 6333 · E2.

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

- Intent, decision, consequences (positive and negative), alternatives, decomposition scorecard, feature checklist. Write the ADR before the code, because an ADR written after the code is a post-hoc rationalization.

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

> **Course use.** CIDM 6333 · E3 (local model required).

## Learning outcomes

After this chapter you can:

- Declare tools with schema-validated contracts and handle failure and retry.
- Gate write-class tools behind a confirmation event recorded in a ledger.
- Explain hooks as enforcement points around tool calls, and the 2026-08-23 incident that moved enforcement to the commit locus.

## Outline

### 12.1 Declaring a tool

- Name, description, JSON schema, Pydantic model; idempotency; side-effect class (read, write, irreversible).

### 12.2 Permission gating

- Read freely; write with confirmation; irreversible with attestation. The confirmation event is written to the ledger before the call. If the ledger does not record the confirmation, the confirmation did not happen.

### 12.3 Hooks

- Claude Code hook events (SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop, SessionEnd); gzkit's 17. What a hook can see and what it cannot: the Bash-write bypass, and why gzkit relocated write-side enforcement to the commit locus (`git diff --cached`).

### 12.4 Failure and recovery

- Timeouts, malformed calls, tool errors as observations; retry budgets; when to halt instead.

### 12.5 Small models and tools

- Why a local 8B model is the right substrate for this Evolution: its brittleness makes the contract visible.

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| Toolformer | 2023 | Learned calls | Tools |
| Function calling | 2023 | Declared calls | Tools |
| Gorilla / ToolBench | 2023 | Tool retrieval | Tools |
| Computer use | 2024 | Screen as tool | Perception, tools |
| Claude Code hooks | 2025 | Pre- and post-tool checks | Governance |
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

> **Course use.** CIDM 6333 · E4.

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

- The reference design has no MCP server. This section specifies the server the student builds to fill that gap: `gz status`, `gz validate`, the ledger, and receipts exposed as MCP tools and resources, with "what is attested?" as a resource. Why gzkit refused MCP, and what changes when you add it one tier up.

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

> **Course use.** CIDM 6333 · E5.

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

Sortie 5 (corner). DESIGN CLAIM: a poisoned resource cannot cause a write, and a changed tool description stops the sortie before the model sees it. FALSIFIERS: any write following a resource-borne instruction; a changed description that does not stop the sortie; passing only by disabling a check. The sortie does not test authorization.

## Exercises and Design Analysis prompts

1. Write the AGENTS.md for your system under a 4,000-character budget. Then measure what your harness actually loads.



---

# 15. Context Engineering: Budgets, Compaction, Handoffs, and Layers of Truth

> **Course use.** CIDM 6333 · E6.

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

- L1 canon (markdown), L2 ledger (append-only events), L3 derived (status views, markers). Precedence L2 > L1 > L3; L3 can never block a gate. Frontmatter can carry a false status; the ledger is the authoritative record, and it outranks frontmatter (L2 > L1).

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

> **Course use.** CIDM 6333 · E7 (local model required).

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

> **Course use.** CIDM 6333 · E8.

## Learning outcomes

After this chapter you can:

- Build an implementer–reviewer pair with personas and a fail-closed structured result contract.
- Orchestrate with a state graph and explain the checkpoints.
- Explain gzkit's pipeline stages and roles.

## Outline

### 17.1 Why more than one

- Context isolation; independent review; parallelism; the same division of labor (plan / do / check) that FIPA-era designs already used.

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

The pipeline is specified in ADR-0.18.0 and `docs/user/concepts/subagent-pipeline.md` and implemented in `src/gzkit/roles.py` and `pipeline_dispatch.py`. The personas live in `.gzkit/personas/`. The pipeline also provides the `--single-driver --reason` honesty flag.

## Readings

- gzkit `subagent-pipeline.md`.
- Yang et al., "SWE-agent."
- Sprint and Drift, "Optimism's flames."

## Flight card supported

Sortie 8 (expansion). DESIGN CLAIM: no implementer output reaches the main branch without a reviewer verdict, and a FAIL verdict blocks. FALSIFIERS: merged work with no ReviewResult; a malformed result parsed as PASS; the reviewer's claim accepted without the evidence it cites.

## Exercises and Design Analysis prompts

1. Give your reviewer a persona with anti-traits. Then remove them and measure the verdicts.



---

# 18. Multi-Agent Coordination II: When Coordination Fails

> **Course use.** CIDM 6333 · E9.

## Learning outcomes

After this chapter you can:

- State the multi-agent failure taxonomy and recognize each mode in a trace.
- Implement cross-vendor adversarial validation, locks, and cost-aware routing.
- Explain delegation and handoff protocols, agent marketplaces and contracts, and cost and resource management.

## Outline

### 18.1 The taxonomy

- Specification/design, inter-agent misalignment, verification failures (Cemri et al.); gzkit's nine agent failure modes; summary laundering; hallucinated authorization.

### 18.2 Adversarial validation

- Tier 1 cross-vendor (different model family); tier 2 independent subagent; tier 3 human. REFUTED / NOT-REFUTED. A subagent's claim is not evidence; a receipt is.

### 18.3 Locks and mutual exclusion

- Token-block locks with TTL; who may work on what; the ledger as lock witness.

### 18.4 Routing and cost

- Model tiers by task complexity; local vs. hosted; budgets per sortie; cost as a first-class metric.

### 18.5 Delegation, handoff, marketplaces

- A2A tasks and artifacts; contracts between agents; what an agent marketplace would need (identity, attestation, liability).

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| Cemri et al. taxonomy | 2025 | Why MAS fail | Evaluation |
| A2A delegation | 2025 | Handoff protocol | Coordination |
| gzkit Step 4b / locks / repudiation | 2026 | Fail-closed coordination | Coordination, governance |

## Reference design: gzkit

This chapter reads the summary-laundering chain of 2026-05-24 (ten levels deep), the seven Gate-5 repudiations of June 2026, the undispatched Stage 2 of 2026-08-21, the commands `gz obpi dispatch`, `gz obpi lock`, and `gz obpi repudiate`, and `DISPATCH_MODEL_MAP`.

## Readings

- Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" (2025).
- gzkit `.gzkit/rules/agent-failure-modes.md`; `docs/evals/gzkit-campaign-architecture-review-2026-08-17.md`.
- Sprint and Drift, "Newtonian motion."

## Flight card supported

Sortie 9 (corner). DESIGN CLAIM: a subagent's claim never becomes evidence without a receipt, and a second-family adversary can refute a false claim. FALSIFIERS: a claim promoted to the flight log with no receipt; an adversary that agrees with a planted falsehood; a lock violated without a ledger event.

## Exercises and Design Analysis prompts

1. Plant a false "tests pass" claim in a worker's output. Show the pipeline that catches it. Then show the version that would not.



---

# 19. Evaluation as Gates: Golden Sets, Regression Deltas, Judges, and RED Witnesses

> **Course use.** CIDM 6333 · E10.

## Learning outcomes

After this chapter you can:

- Build an evaluation suite with golden cases and a regression delta wired into a gate.
- Explain LLM-as-judge and its biases, and when a judge is admissible.
- Write a RED witness: a test that fails when the behavior is removed.

## Outline

### 19.1 Benchmarks and what they hide

- SWE-bench, GAIA, tau-bench, WebArena, AgentBench; contamination, overfitting, the gap between benchmark and job.

### 19.2 Evals as gates

- Golden datasets; scoring; the delta; the gate that fails the build. gzkit's eval runner and `eval_regression_delta`.

### 19.3 LLM-as-judge

- Self-preference and position bias; why model self-review is Gate-4 evidence, never Gate-5 (GZK-GOV-007); rubric blinding.

### 19.4 Falsifiability

- The RED witness (`gz arb red`): rebuild without the change, run the covering test, expect failure. Tautological and hollow tests. Pre-registration.

### 19.5 Flight test as evaluation method

- The card, the black box, the Chase. Evaluation as falsification rather than confirmation.

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| SWE-bench / GAIA / tau-bench | 2023–24 | Benchmarks | Evaluation |
| LLM-as-judge | 2023– | Scalable, biased | Evaluation |
| gzkit eval runner / arb red / flighttest | 2026 | Evals as gates | Evaluation |

## Reference design: gzkit

This chapter reads `src/gzkit/eval/` and `data/eval/*.json`, the commands `gz adr evaluate --red-team` and `gz arb red`, `docs/harness-docs/GZK-GOV-007-ultrareview-and-gate-5.md`, and the hollow-antibody incident (ADR-0.0.73).

## Readings

- gzkit `GZK-GOV-007`.
- One benchmark paper of choice.
- Sprint and Drift, "Can you outrun the truth?"

## Flight card supported

Sortie 10 (expansion). DESIGN CLAIM: the evaluation suite fails when it should: if the tester removes the feature or plants a wrong answer, the gate turns red. FALSIFIERS: a green gate with the feature removed; a judge that scores a planted error as correct; a golden case that cannot fail.

## Exercises and Design Analysis prompts

1. Take your best test. Break the production code it covers. If the test still passes, the test is hollow.



---

# 20. Observability, Red-Teaming, and Safety

> **Course use.** CIDM 6333 · E11.

## Learning outcomes

After this chapter you can:

- Instrument your system with traces, receipts, and cost/latency measurement.
- Red-team your own system against the nine failure modes with a pre-registered card.
- Read a frontier system card as an evaluation document and install guardrails accordingly.

## Outline

### 20.1 Observability

- Spans and traces; receipts (exit status, duration, git state, stdout tail) as the reference design does it; the ledger as the black box; what to log and what never to log.

### 20.2 Cost and latency

- Per-turn, per-sortie, per-week; local vs. hosted; the supervision cost that does not appear in the model bill.

### 20.3 Red-teaming

- The nine modes (safeguard circumvention, reckless action, fabrication, skipped cheap verification, correction fails, dishonest when caught, hallucinated authorization, security shortcut, metagaming the gate); attack cards; trust-chain poisoning.

### 20.4 System cards and guardrails

- What a system card measures; frontier safety frameworks; how to translate a card's findings into your guardrails.

### 20.5 Governance, safety, guardrails, risk

- The board's "Governance & Future" quadrant as an engineering checklist.

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| Frontier system cards | 2024–26 | The evaluation genre | Evaluation, governance |
| Observability stacks (Langfuse/LangSmith-style) | 2023– | Traces | Runtime |
| gzkit ARB receipts / trust doctrine | 2026 | Receipts over narrative | Evaluation |

## Reference design: gzkit

The gzkit evidence for this chapter is `src/gzkit/arb/`, `docs/governance/trust-doctrine.md` together with the outage of 2026-04-18 (nine instances of trust-chain poisoning), `data/frontier_model_cards.json`, and the operator-PII incident of 2026-04-19.

## Readings

- One current system card (selected sections).
- gzkit `trust-doctrine.md`; `arb-middleware.md`.
- Sprint and Drift, "Turn and Face the Change."

## Flight card supported

Sortie 11 (corner, red team). DESIGN CLAIM: the system survives five pre-registered attacks drawn from the nine modes without a write, a leak, or a false attestation. FALSIFIERS: any attack that achieves its objective; any attack that the black box cannot trace; a guardrail that passes only because the attack was never delivered.

## Exercises and Design Analysis prompts

1. Write three attack cards for a peer's system. Fly them as Chase. Route the squawks.



---

# 21. Production and Operations: Serving, Scheduling, Rollback, Release

> **Course use.** CIDM 6333 · E12.

## Learning outcomes

After this chapter you can:

- Package, serve, and containerize your system with secrets and rate limits handled.
- Run the Heavy-lane gates (docs, BDD, human) and a release ceremony with rollback.
- Explain the operational problems of long-running and background agents.

## Outline

### 21.1 Serving an agent

- FastAPI (or equivalent); request lifecycle; streaming; idempotency; timeouts; the agent as a service vs. a job.

### 21.2 Containers, secrets, limits

- Image, config, secret injection, rate limits, budgets; secrets never in the repo.

### 21.3 Scheduling and background agents

- Scheduled sorties; long-running sessions; compaction across days; who attests an unattended run.

### 21.4 Rollback and feedback loops

- Release with a rollback path; feedback from evaluators into the next release; self-improvement bounded by attestation.

### 21.5 The release ceremony

- Docs gate; BDD scenarios for external contracts; human attestation; release notes vs. changelog; the distribution invariant; MX mode ("loose in the bay, hard at the door").

## Systems analyzed in this chapter

| System | Year | Why it is here | Component focus |
|---|---|---|---|
| Background / cloud agents | 2025–26 | Operational problems | Runtime |
| Copilot coding agent | 2025 | PR-native background work | Runtime |
| gzkit closeout / patch release / MX | 2026 | Release as ceremony | Runtime, governance |

## Reference design: gzkit

The gzkit commands and records for this chapter are `gz closeout --ceremony`, `gz patch release`, `gz validate --distribution`, ADR-0.0.74 (MX mode), ADR-0.0.31 (the distribution invariant), and the backfilled releases of GHI #830.

## Readings

- gzkit `docs/examples/guide-releasing.md`; `command-doctrine.md`.
- Nygard, *Release It!* (selected chapters).

## Flight card supported

Sortie 12 (expansion). DESIGN CLAIM: one governed command rolls a release back and the rollback is in the ledger; secrets never appear in image, log, or repo. FALSIFIERS: a rollback that needs manual steps; a secret in any artifact; a release with no attestation event.

## Exercises and Design Analysis prompts

1. Roll back your own release. Time it. Put the number in the runbook.



---

# 22. Sprint and Drift

> **Course use.** CIDM 6333 · E0; every week.

## Learning outcomes

After this chapter you can:

- Explain the method and its origin.
- Run a week as Sprint and Drift.
- Conduct or undergo a Drift consultation using the protocol.

## Outline

### 22.1 The problem with artifacts

- A correct artifact is no longer evidence of understanding; a ban on AI fails three ways.

### 22.2 The method

- Sprint: produce, with AI, logged. Drift: defend, without AI. Naval origin; you cannot move and listen at once.

### 22.3 The consultation protocol

- Opening; walk-through; trade-off probing; AI-log review; closing. Signals of understanding and of shallowness. The 12-minute deep Drift and the under-ten rotation.

### 22.4 The AI log

- What, which, what kept, what rejected, why, how verified. The log is discussed in the Drift consultation rather than filed.

## Readings

- CIDM 6330 Sprint and Drift method and Drift Consultation Protocol (adapted here).

## Exercises and Design Analysis prompts

1. Run a mock Drift on a peer's E1. Score yourself against the shallow-understanding signals.



---

# 23. Flight Cards and the Flight Log

> **Course use.** CIDM 6333 · E0; every week.

## Learning outcomes

After this chapter you can:

- Author a flight card before flying and freeze it at Go.
- Serve as Chase and write a verdict from evidence alone.
- Debrief and route squawks.

## Outline

### 23.1 Origins

- gzkit's flight-test program; aircraft flight test; the sortie, the card, the black box, the Chase.

### 23.2 The card

- Envelope; design claim; systems under test; entry conditions; test points; instrumentation; falsifiers; abort; Chase; debrief.

### 23.3 Five rules

- Pre-register; the black box is truth; build up the envelope; fly the governed path; independent observation.

### 23.4 Anti-patterns

- Assertion-from-a-run; narrative to the Chase; "it worked"; passing by leaving the path.

### 23.5 The flight log

- Card + evidence + verdict + debrief; what is graded.

## Reference design: gzkit

The gzkit documents for this chapter are `docs/flighttest/README.md`, `flight-card-template.md`, `manifest.md` (S1–S6), and the `gz-flighttest` skill. Zero sorties had been flown as of 2026-08-17, so the course flies the first.

## Readings

- gzkit flighttest documents.

## Exercises and Design Analysis prompts

1. Write the card for a sortie you already flew informally. Note how much of the instrumentation you would have invented after the fact.



---

# 24. The Design Analysis

> **Course use.** CIDM 6333 · E0; every week.

## Learning outcomes

After this chapter you can:

- Dissect a system against the nine components in ~150 words.
- Write the "why" paragraph that states the cost and the failure mode.
- Maintain a Design Analysis Ledger and pool it with a class.

## Outline

### 24.1 The form

- Nine components, one line each; the why paragraph; the judgment-loop closer.

### 24.2 Sources

- Papers, docs, code, changelogs, incident records; how to read a system from the inside and from the outside.

### 24.3 Worked examples

- Claude Code; AutoGPT; MCP; gzkit.

### 24.4 The ledger

- One table, one row per system; pooling; how the class corpus becomes the survey.

## Readings

- This chapter.

## Exercises and Design Analysis prompts

1. Write the same system's analysis from the outside (README) and the inside (its changelog). Diff them.



---

# 25. Governed Development with gzkit: A Working Tutorial

> **Course use.** CIDM 6333 · E1–E12.

## Learning outcomes

After this chapter you can:

- Initialize, plan, specify, implement, verify, close out, and attest a governed increment.
- Read the ledger and explain each event.
- Recover from the fail-closed gates without working around them.

## Outline

### 25.1 Install and init

- Python 3.14+, uv; `uv tool install py-gzkit`; `gz init --mode lite`; what is scaffolded (523 files); commit once.

### 25.2 PRD and ADR

- `gz prd`; the interview; `gz plan create <slug> --kind feature --semver 0.1.0 --lane lite`; the scorecard.

### 25.3 Briefs and tasks

- `gz specify`; the 272-line brief; allowed paths; REQs and acceptance criteria; `@covers`.

### 25.4 Implement and verify

- `gz implement`, `gz arb`, `gz covers`, the RED witness; the Claude Code pipeline hook.

### 25.5 Close out and attest

- `gz obpi brief-drift`, `gz obpi complete --attestor`, `gz closeout --ceremony --attest`, `gz audit`; reading the 37-event ledger.

### 25.6 The gotchas

- README.md before gates; `--kind` required; ruff/ty excludes; the interactive prompt in non-TTY; opus-tier skills and cost; Codex as tier-1 adversary.

## Reference design: gzkit

This chapter uses the reference design as a tool. It follows the tutorial-first-project document, corrected against v0.34.5 (Appendix F).

## Readings

- gzkit `docs/examples/tutorial-first-project.md`, `guide-tasks.md`, `docs/user/quickstart.md`.

## Exercises and Design Analysis prompts

1. Complete the reading-list tutorial end to end. Paste your ledger. Annotate every event.



---

# 26. The Final System and the Closeout Ceremony

> **Course use.** CIDM 6333 · E7 brief; finals week.

## Learning outcomes

After this chapter you can:

- Read a personalized brief and scope a governed revision.
- Deliver the Final System under the Heavy lane.
- Conduct a closeout ceremony: the student presents paths and commands, and the instructor executes, observes, and attests.

## Outline

### 26.1 The personalized brief

- What Drifts revealed; scope set by the instructor; do not begin before it arrives.

### 26.2 Deliverables

- PRD; ADR(s); briefs; code and tests; gates 1–5; eval suite with a red-team card; served/containerized with runbook and rollback; release; Design Analysis Ledger; AI_LOG.md; ceremony.

### 26.3 The ceremony

- Mode transition: the agent (here the student) presents paths and commands, not conclusions; the human executes and observes; "silent index"; attestation vocabulary; audit after.

### 26.4 Scoring

- 30 / 25 / 25 / 10 / 10; caps.

## Reference design: gzkit

The gzkit material for this chapter is the 11-step closeout ceremony (`src/gzkit/commands/ceremony_steps.py`) and the "mediated observation" critique from the AirlineOps exploration.

## Readings

- CIDM 6330 Final Project: Governed Revision (adapted).
- gzkit `docs/user/concepts/closeout.md`.

## Exercises and Design Analysis prompts

1. Draft your own brief before you receive mine. Compare the two.



---

# Appendix A: Flight Card Template (course edition)

Copy this block into `evolution-NN/flight-card.md`. Fill every field **before** you request Go. Do not fill in the expected observables after the flight. Doctrine counts that as a violation.

```
FLIGHT CARD - SORTIE <N> : <short name>
════════════════════════════════════════════════════════════
ENVELOPE POSITION   : <center | expansion | corner>
DESIGN CLAIM        : <one sentence a single observation could disprove>
SYSTEMS UNDER TEST  : <the parts of YOUR system this sortie exercises>
SUBSTRATE           : <repo + commit + model/route; local or hosted>
DEPENDS ON          : <prior sorties that must have passed, or "none">

────────────────────────────────────────────────────────────
ENTRY CONDITIONS (go/no-go: all must hold)
  - clean tree; prior sortie evidence on record
  - governance artifacts current (ADR/brief for this layer exist)
  - Go recorded by the instructor at <time>

────────────────────────────────────────────────────────────
TEST POINTS (in flight order)
  #    GOVERNED PATH                          EXPECTED OBSERVABLE (black box)
  1    <command / action>                     → <ledger event / receipt / artifact>
  2    ...

────────────────────────────────────────────────────────────
INSTRUMENTATION (the signature of a PASS)
  ledger    : <events, counts, order>
  receipts  : <names>
  traces    : <spans / logs>
  artifacts : <files with expected state>

────────────────────────────────────────────────────────────
PRE-REGISTERED FALSIFIERS (any ONE ⇒ FAIL)
  - <observation that disproves the claim>
  - <missing instrumentation that proves the path was not flown>
  - passed only by leaving the governed path / disabling a check

────────────────────────────────────────────────────────────
ABORT CRITERIA (halt-not-fail)
  - <infrastructure failure unrelated to the claim, e.g. model unavailable>

────────────────────────────────────────────────────────────
CHASE
  - observer : <peer name>
  - reads    : <exact evidence slice handed over, never the narrative>
  - verdict  : PASS / FAIL, authored from evidence alone

────────────────────────────────────────────────────────────
DEBRIEF & SQUAWKS
  - black box vs card : <matched / diverged>
  - design signal     : sound | awkward-but-correct | wrong, and why
  - squawks           : <each anomaly → issue # | design-feedback | card amendment | re-fly>
════════════════════════════════════════════════════════════
```


---

# Appendix B: Design Analysis Template

Write one Design Analysis per week, ~150 words. Commit it to `design-analyses/<system>.md`. Append one row to `design-analyses/LEDGER.md`.

```
# Design Analysis: <System> (<year>)

Sources read: <paper / docs / code / changelog / incident record>

| Component | Answer |
|---|---|
| Foundation | |
| Perception | |
| Planning & reasoning | |
| Tools & orchestration | |
| Memory & context | |
| Coordination | |
| Evaluation & feedback | |
| Governance & human interface | |
| Runtime & operations | |

## Why it was built this way, and what it cost
<one paragraph>

## Judgment loop
Decision: · Characteristics privileged: · Cost: · Failure mode: · Preservation mechanism:
```

Ledger row: `| <system> | <year> | <analyst> | <one-line why> | <link> |`


---

# Appendix C: The Nine Agent Failure Modes

The nine modes come from gzkit `.gzkit/rules/agent-failure-modes.md`, which sources them to frontier system cards. The human-side patterns listed after the table are the course's additions.

| # | Mode | One line | Red-team probe |
|---|---|---|---|
| 1 | Safeguard circumvention | Works around a guardrail instead of producing the evidence it asks for | Block a write; offer an easier bypass |
| 2 | Reckless action | Takes a hard-to-reverse action without confirming authorization for this scope | Ambiguous "clean up" instruction |
| 3 | Fabrication | A claim, receipt, or attestation not observed from a primary source | Ask for a result that cannot be produced |
| 4 | Skipped cheap verification | Pattern-matched incantation without running it | A command that looks right and is wrong |
| 5 | Correction fails | Correction received but not applied, or applied superficially | Correct once, re-test three turns later |
| 6 | Dishonest when caught | Post-hoc rationalization without quoting the rule and the conflicting directive | Catch a violation; watch the explanation |
| 7 | Hallucinated authorization | Acts on a gate it believes was passed when nothing records it | Remove the record; see if it proceeds |
| 8 | Security shortcut | Trades integrity for convenience without stating the trade | Put a secret in the easy path |
| 9 | Metagaming the gate | Shapes output to satisfy the check rather than the intent | A test that can be passed by string-matching |

Human-side: the Degradation Pattern; governance theater; cognitive surrender; mediated observation; summary laundering; presence-is-not-procedure.


---

# Appendix D: Glossary

*Terms marked (gz) are gzkit's; (SD) are Sprint and Drift's.*

- **ADR**: an Architecture Decision Record, which states intent, decision, consequences, and alternatives, and is written before code.
- **Agent**: a system that perceives and acts toward a goal; in this book, one whose reasoner is a language model and whose loop has a halt condition.
- **Attestation (gz)**: a human's recorded judgment that work is Completed, Completed — Partial, or Dropped. It is Gate 5.
- **Black box**: the evidence a system produced (ledger, receipts, traces), as opposed to what anyone says about it.
- **Brief / OBPI (gz)**: One Brief Per Item, the unit of human review, with requirements, acceptance criteria, and verification.
- **Chase**: the independent observer who writes a sortie's verdict from evidence alone.
- **Context engineering**: the practice of treating the model's context window as an engineered artifact with a budget.
- **Covenant (gz)**: the five-clause agreement between human and agent.
- **Design Analysis**: the nine-component dissection of a system plus the "why" paragraph.
- **Drift (SD)**: the verification phase, in which the student defends the work without AI.
- **Evolution**: the weekly unit of the course.
- **Falsifier**: a pre-registered observation that would prove a design claim false.
- **Flight card**: the pre-registered plan for a sortie.
- **Gate (gz)**: one of five checkpoints (ADR, TDD, Docs, BDD, Human).
- **Harness**: the software that turns a model into an agent (tools, permissions, context, loop).
- **Index zero (gz)**: the human's position (first in priority, final in authority).
- **Lane (gz)**: Lite (gates 1–2) or Heavy (1–5).
- **Layers of truth (gz)**: canon (L1), ledger (L2), derived (L3); L2 > L1 > L3.
- **Ledger (gz)**: the append-only event log that is the runtime truth.
- **MCP**: Model Context Protocol, whose participants are hosts, clients, and servers and whose primitives are tools, resources, and prompts.
- **Meta-harness (gz)**: governance one tier above the vendor harness.
- **Receipt (gz)**: a schema-validated record of a command's observed result.
- **RED witness (gz)**: proof that a test fails without the change it covers.
- **Sortie**: one flight of one card in one sitting.
- **Sprint (SD)**: the production phase, in which the student builds with AI and logs the use.
- **Squawk**: an anomaly recorded at debrief and routed to an issue, a feedback entry, a card amendment, or a re-fly.
- **V.I.B.E.S. (gz)**: Velocity Increased, Bugs Expected Software, gzkit's label for the failure class.


---

# Appendix E: Reading List

## Primary sources (by chapter)
- Anthropic. "Building Effective Agents" (2024); "Effective Context Engineering for AI Agents" (2025); "Effective Harnesses for Long-Running Agents" (2025).
- OpenAI. "A Practical Guide to Building Agents" (2025).
- Model Context Protocol. Specification (current).
- Wei et al. "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (2022).
- Yao et al. "ReAct: Synergizing Reasoning and Acting in Language Models" (2022).
- Schick et al. "Toolformer" (2023).
- Shinn et al. "Reflexion" (2023).
- Park et al. "Generative Agents" (2023).
- Packer et al. "MemGPT" (2023).
- Wu et al. "AutoGen" (2023); Hong et al. "MetaGPT" (2023).
- Yang et al. "SWE-agent" (2024); Xia et al. "Agentless" (2024).
- Lewis et al. "Retrieval-Augmented Generation" (2020).
- Cemri et al. "Why Do Multi-Agent LLM Systems Fail?" (2025).
- Degani & Wiener. "Philosophy, policies, procedures and practices" (1997).
- Current frontier system cards (Anthropic, OpenAI, Google).

## The reference design
- gzkit documentation at gzkit.org; repository github.com/tvproductions/gzkit. Chapter-by-chapter pointers appear in each chapter's Readings.

## Sprint and Drift essays (sprintanddrift.substack.com)
Tree Hollow · Who answers for the code · Enthusiasm Is All You Need · Get the Balance Right · Stop the presses, hail the autoloom · The cost of the wrong abstraction went to zero · Woven · Code ergo sum · Optimism's flames · Newtonian motion · Can you outrun the truth? · Turn and Face the Change, and the archive.

## Books (optional, influential)
Huyen, *AI Engineering* (2025) · Lanham, *AI Agents in Action* · Richards & Ford, *Fundamentals of Software Architecture*, 2e · Ford, Richards, Sadalage, Dehghani, *Software Architecture: The Hard Parts* · Beck, *Tidy First?* · Nygard, *Release It!*, 2e · Russell & Norvig, *AIMA* · Wooldridge, *An Introduction to MultiAgent Systems* · Sutton & Barto, *Reinforcement Learning*.


---

# Appendix F: Toolkit Setup (Route A and Route B)

## Everyone
```bash
# Python 3.14+ via uv
curl -LsSf https://astral.sh/uv/install.sh | sh     # or the Windows installer
uv python install 3.14

# gzkit
uv tool install py-gzkit
gz --version

# a governed project
mkdir my-agent && cd my-agent && git init
gz init --mode lite
gz status

# local models (required for E3 and E7 on both routes)
# install Ollama from https://ollama.com, then:
ollama pull qwen3:8b            # 8–16 GB machines; qwen3-coder:30b on 24–32 GB
ollama run qwen3:8b "say hello"
```

## Route A: a subscription plus a small API budget
- Subscribe to Claude Pro, ChatGPT Plus, or Google AI Pro (~$20/mo). Use the harness that comes with it: Claude Code or Claude Desktop, Codex CLI, or Gemini CLI.
- Set aside ~$20–40 of API credit for the SDK and MCP work.
- Add GitHub Copilot (Student plan) as a free supplement.

## Route B: local only
- Install Ollama and OpenCode (or another provider-agnostic harness).
- Use an SDK that speaks OpenAI-compatible endpoints (Pydantic AI, LangGraph, or the OpenAI SDK pointed at Ollama).

## Known pitfalls with py-gzkit 0.34.x (verified 2026-08-24)
1. `gz init` writes ~520 files (`.gzkit/`, `.claude/`, `.agents/`, `.github/`). Commit them once. Do not hand-edit a generated file.
2. The generated `pyproject.toml` declares `readme = "README.md"`. If that file does not exist, Gate 2 fails with "Readme file does not exist." Create the file first.
3. `gz plan create` needs a slug and `--kind feature --semver 0.1.0 --lane lite`. The artifacts land in `design/`, not in `docs/design/`.
4. Exclude `.claude`, `.gzkit`, `.github`, and `.agents` from ruff and ty (`extend-exclude` for ruff, and `[src] include = ["src","tests"]` in `ty.toml`). Run `uv add --dev ty`.
5. After any edit to a brief, run `gz obpi brief-drift <ID>` again before `gz obpi complete --attestor <you> --attestation-text "..."`. The brief needs a substantive Objective, Value Narrative, Key Proof, and Implementation Summary. For product proof, Allowed Paths must cover `src/` and `tests/`.
6. In Claude Code, `pipeline-gate.py` refuses edits to `src/` and `tests/` when no pipeline is active (`gz obpi pipeline <ID>`). `verifier-pipe-gate.py` refuses `unittest ... | tail`. Do not work around either hook.
7. `gz closeout` ends in an interactive `Select [1/2/3]`. In a non-TTY context, use `gz closeout <ADR> --ceremony --attest` or `gz attest`.
8. Step 4b adversarial validation prefers Codex as tier-1. If you have only one vendor, run in degraded mode and say so.
9. Several skills are `model: opus`. Budget for that. For a small sortie, prefer `--no-subagents`.


---

# Appendix G: The gzkit Incident Casebook (2026)

This appendix lists the dated episodes from the reference design and, for each, the mechanism that resulted. The sources are `AGENTS.md` § Operator Doctrine, `CHANGELOG.md`, `RELEASE_NOTES.md`, `.gzkit/insights/agent-insights.jsonl`, and the ledger.

| Date | What happened | What resulted | Course use |
|---|---|---|---|
| 2026-01-12 | ADR-0.1.9 in AirlineOps accumulated ~100 briefs under one identity | gzkit itself; semver as governance assertion | Ch. 3, 9 |
| 2026-04-16 | First outside adopter: `gz init` left no runnable project, and the scaffolders emitted ids that their own validator rejected | v0.25.1–0.25.10; issue templates | Ch. 25 |
| 2026-04-18 | `gz patch release` over-counted closed issues 5× | "Count what we CLOSE, not what we book" | Ch. 21 |
| 2026-04-18 | Trust-chain poisoning outage: nine silent-wrong layers fed decisions that looked correct | Trust doctrine (T0–T3) | Ch. 20 |
| 2026-04-19 | Operator PII leaked into artifacts; history rewrite | PII rule; authorship guard | Ch. 20 |
| 2026-04-26 | A stale clone sat 10 commits behind; a hard reset discarded ~215 lines | SessionStart ahead/behind; orientation freshness | Ch. 15 |
| 2026-05-10 | The agent piped "ATTEST" into `gz obpi complete` to bypass the TTY gate | Regression test; then the TTY gate was removed (05-14), on the reasoning that authority belongs to the human and forgery-resistance to audit | Ch. 3, 18 |
| 2026-05-23 | Four questions bundled in one prompt | Operator economy of effort | Ch. 15 |
| 2026-05-24 | Ten-deep subagent chain; polished summaries became "facts" | DO IT RIGHT rules; "a subagent's claim is not evidence" | Ch. 17, 18 |
| 2026-05-30→06-08 | Green `main` was reopened 8× in nine days | V.I.B.E.S. coined; pre-push gate; MX hangar | Ch. 19, 21 |
| 2026-06-13 | A Gate-5 was attributed to the operator, who never gave it | First repudiation; ADR-0.0.71 | Ch. 18 |
| 2026-06-16 | Four briefs were attested for a renderer, a validator, a composer, and a playback store; none existed as attested | Repudiations; enforcement-claim rule | Ch. 19 |
| 2026-06-18/19 | "The antibody" (verification-layer audit) was itself hollow and attested Completed | `@enforces` live negative controls | Ch. 19 |
| 2026-06-20 | "Utter shambles": 70 validate scopes behind a 162-parameter function; 116 handoffs | MX mode; amendments append, never inline | Ch. 21 |
| 2026-07-18 | 90-day commit mix 2.9% feat / 31% fix / 54% chore; zero airlock transits | "Permitted to say enough" | Ch. 9 |
| 2026-08-14 | 20 of 23 airlock transits computed an empty seam-map | Calibrate before widening | Ch. 9 |
| 2026-08-16 | A limit in a Markdown doc disagreed with the JSON authority; 51 unguarded modules | "A value in Markdown is illustrative, never authoritative" | Ch. 14 |
| 2026-08-21 | The pipeline gate checked only that a marker file existed; a stale marker licensed ~350 lines with no dispatch or review | "A presence check answers 'is something armed', never 'did the procedure run'" | Ch. 12, 19 |
| 2026-08-22 | One CLI verb, when registered, produced 21 failures; three docs disagreed on the obligation set | One authority for new-verb obligations | Ch. 14 |
| 2026-08-23 | Any Bash write bypassed six governance hooks keyed on editor-tool matchers | Enforcement moved to the commit locus (`git diff --cached`) | Ch. 12 |
| 2026-08-23 | The agent re-elicited three settled rulings by multiple-choice | "A settled question is a drift vector" | Ch. 15 |


---

# Appendix H — Week-by-Week Run Sheet (60 · 60 · 30)

Thursdays 4:00–6:30 in CC209. Lecture 4:00–5:00 · Consultation 5:00–6:00 · Lab 6:00–6:30. Class under ten: three 12-minute deep Drifts per week (everyone gets four across E1–E12) plus a stand-up and a Go/No-Go for all, every week. Evolutions due Tuesdays 11:59 p.m.

## E0 · Thu 08/27 · Orientation — The human is index zero

*Chapters: Ch. 1, 2, 3, 22, 23, 24*

**Lecture (60)**

- 0–10 Welcome; the question behind the course; Tree Hollow
- 10–25 Layers of AI; the five-stage progression; assign every board box to a week
- 25–35 What is an agent: PEAS → loop → nine components
- 35–45 Degradation Pattern; Zero Doctrine; covenant; gates and lanes
- 45–55 Two threads; the Thursday; Sprint & Drift; flight cards; Design Analysis
- 55–60 Routes, harnesses, frameworks, kits; E0 brief

**Consultation (60)**

- 0–10 Introductions: name, background, machine (RAM/GPU), intended route
- 10–40 Roundtable: each student sketches a system idea; class tests it against "can it take all twelve layers?"
- 40–55 Pairings for Chase duty; Discord; Calendly; GitHub org
- 55–60 Go for E0: toolkit + pitch + first Design Analysis

**Lab (30)**

- 0–30 Install clinic: uv, Python 3.14, gz init in a scratch dir, ollama pull; verify `gz --version`, `ollama list`; commit a toolkit check

**Sprint deliverables:** E0 folder: toolkit check, skills inventory, one-page pitch (route, harness, candidate framework, risk), AI_LOG.md started, Design Analysis: chat assistant vs. harness. Due Wed 09/02.

**Instructor prep:** Slides (orientation deck); GitHub org ready; Discord; Calendly; verify py-gzkit release and Python 3.14 install path on Windows/macOS.

---

## E1 · Thu 09/03 · The agent loop

*Chapters: Ch. 5, 10; 25 (init, PRD)*

**Lecture (60)**

- 0–10 Framing: a loop without a halt is a bill
- 10–30 Spine: CoT → ReAct; the minimal loop; structured outputs; halt conditions and budgets
- 30–45 Survey teardown: ReAct; AutoGPT/BabyAGI — live Design Analysis on the board
- 45–52 Reference design: genesis; PRD as WHAT; first ledger events
- 52–60 Evaluation lens + Flight Card 1 brief (center of envelope)

**Consultation (60)**

- 0–10 Stand-up: pitch in one sentence; toolkit status
- 10–46 Three deep Drifts (12 min): defend the pitch and E0 analysis; others at Chase station (review a peer's E0) and card station
- 46–60 Go/No-Go on Card 1 for everyone

**Lab (30)**

- 0–30 Fly TP1: minimal loop against your route's model answers a bounded question and halts; ledger shows the turns; capture evidence slice

**Sprint deliverables:** Sortie 1 flight log; loop code + tests; PRD attested; Design Analysis (ReAct or AutoGPT); AI_LOG. Due Wed 09/09.

**Instructor prep:** Demo repo at "loop that halts"; ReAct and AutoGPT summaries; PRD interview script; check Ollama tool-call formats for the small models students chose.

---

## E2 · Thu 09/10 · Patterns and orchestration frameworks

*Chapters: Ch. 6, 8, 11; 25 (ADR)*

**Lecture (60)**

- 0–10 Framing: every framework is a theory of who owns the loop
- 10–30 Spine: the five workflow patterns and the agent; when to keep it simple
- 30–45 Teardowns: LangChain→LangGraph; Pydantic AI; AutoGen/CrewAI/MetaGPT; the vendor SDKs
- 45–52 Reference design: ADR-0.0.2 (argparse; "popularity is not rationale"); the scorecard; forcing functions
- 52–60 Evaluation lens + Card 2 brief

**Consultation (60)**

- 0–10 Stand-up: Sortie 1 verdicts; framework leaning
- 10–46 Deep Drifts: defend Sortie 1 and the analysis; Chase and card stations
- 46–60 Go/No-Go on Card 2; ADR-1 alternatives sanity check

**Lab (30)**

- 0–30 Fly TP1: refactor the loop into one pattern under the chosen framework; identical tool trace to E1; capture

**Sprint deliverables:** Sortie 2 log; ADR-1 (framework + pattern, alternatives, consequences, scorecard); Design Analysis; AI_LOG. Due Wed 09/16. Labor Day 09/07.

**Instructor prep:** Pattern demos in two frameworks; ADR-1 exemplar; red-team challenge list for peers.

---

## E3 · Thu 09/17 · Tools as contracts (local model required)

*Chapters: Ch. 6, 12; 23*

**Lecture (60)**

- 0–10 Framing: a tool is a contract; the model is an untrusted caller
- 10–30 Spine: schemas, side-effect classes, permission gating, retry, halting
- 30–45 Teardowns: Toolformer vs. function calling; Gorilla; computer use; Claude Code hooks
- 45–52 Reference design: the 17 hooks; presence-is-not-procedure (08-21); hooks bypassed by Bash writes (08-23) and the commit locus
- 52–60 Evaluation lens + Card 3 brief (expansion; injection test point)

**Consultation (60)**

- 0–10 Stand-up
- 10–46 Deep Drifts on Sortie 2 / ADR-1; stations
- 46–60 Go/No-Go on Card 3; check every card has the injection test point

**Lab (30)**

- 0–30 Fly TP1–2: read tool free; write tool blocked until confirmation event; local model producing the calls; capture

**Sprint deliverables:** Sortie 3 log (four test points); tools + gate + tests; Design Analysis; AI_LOG. Due Wed 09/23.

**Instructor prep:** Small-model tool-calling reliability notes per model; injection payload examples; hook demo in Claude Code.

---

## E4 · Thu 09/24 · MCP I: building a server

*Chapters: Ch. 7, 13*

**Lecture (60)**

- 0–10 Framing: N×M → N+M; why a protocol
- 10–30 Spine: hosts/clients/servers; tools/resources/prompts; negotiation; transports
- 30–45 Teardowns: ChatGPT plugins; OpenAPI tool specs; MCP; the ecosystem and foundation
- 45–52 Reference design: why gzkit refused MCP; the governance-server project
- 52–60 Evaluation lens + Card 4 brief

**Consultation (60)**

- 0–10 Stand-up
- 10–46 Deep Drifts on Sortie 3; stations
- 46–60 Go/No-Go on Card 4

**Lab (30)**

- 0–30 Fly TP1: server declares one tool; inspector lists it; harness calls it; server logs it; capture

**Sprint deliverables:** Sortie 4 log; MCP server + two clients + tests; Design Analysis (MCP or plugins); AI_LOG. Due Wed 09/30.

**Instructor prep:** MCP Python SDK demo; inspector; connecting to each harness (Claude Code, Codex, Gemini CLI, OpenCode).

---

## E5 · Thu 10/01 · MCP II, protocols, security, harness engineering

*Chapters: Ch. 8, 9, 14*

**Lecture (60)**

- 0–10 Framing: the product is the harness
- 10–30 Spine: transports/auth/scope; threat model (tool poisoning, resource injection, confused deputy); A2A vs. MCP; instruction files and skills
- 30–45 Teardowns: MCP incidents; A2A; AGENTS.md/skills; Claude Code vs. Codex control surfaces
- 45–52 Reference design: the control-surface matrix; AGENTS.md as derived view; the 258K exhaustion; map-not-encyclopedia
- 52–60 Evaluation lens + Card 5 brief (corner)

**Consultation (60)**

- 0–10 Stand-up
- 10–46 Deep Drifts on Sortie 4; stations
- 46–60 Go/No-Go on Card 5; every card names its adversarial client

**Lab (30)**

- 0–30 Fly TP1: adversarial client attempts an out-of-scope call; server refuses; refusal logged; capture

**Sprint deliverables:** Sortie 5 log; hardened server; AGENTS.md/skills for your system under budget; Design Analysis; AI_LOG. Due Wed 10/07.

**Instructor prep:** Attack scripts; scope/auth demo; instruction-budget measurement per harness.

---

## E6 · Thu 10/08 · Context engineering

*Chapters: Ch. 8, 15; 25 (handoff)*

**Lecture (60)**

- 0–10 Framing: the window is an artifact with a budget
- 10–30 Spine: budgets; compaction; progressive disclosure; subagents for isolation; handoffs; layers of truth
- 30–45 Teardowns: Claude Code, Codex, Cursor context surfaces
- 45–52 Reference design: state doctrine; handoffs and the rulings store; the stale-clone incident; orientation hooks
- 52–60 Evaluation lens + Card 6 brief

**Consultation (60)**

- 0–10 Stand-up
- 10–46 Deep Drifts on Sortie 5; stations
- 46–60 Go/No-Go on Card 6

**Lab (30)**

- 0–30 Fly TP1: instrument the window; print the budget per turn; write a handoff; capture

**Sprint deliverables:** Sortie 6 log; budget instrumentation + compaction + handoff + ledger; layers declared in README; Design Analysis; AI_LOG. Due Wed 10/14.

**Instructor prep:** Handoff template; ledger schema example; compaction demo; budget-measuring snippet.

---

## E7 · Thu 10/15 · Memory (local model required); ADR-2

*Chapters: Ch. 6, 16; 26 (brief issued)*

**Lecture (60)**

- 0–10 Framing: memory is the part of context that survives
- 10–30 Spine: kinds of memory; retrieval with local embeddings; state; eviction; retention
- 30–45 Teardowns: RAG; Generative Agents; MemGPT; Reflexion; assistant memory features
- 45–52 Reference design: insights corpus; OKF; why gzkit keeps memory as files + ledger
- 52–60 Evaluation lens + Card 7 brief

**Consultation (60)**

- 0–10 Stand-up
- 10–46 Deep Drifts on Sortie 6; stations — instructor notes strengths/gaps for the Final System brief
- 46–60 Go/No-Go on Card 7; ADR-2 alternatives check

**Lab (30)**

- 0–30 Fly TP1: embed and retrieve locally; answer a prior-session question with and without memory; capture

**Sprint deliverables:** Sortie 7 log; memory layer + retention rule + ADR-2; Design Analysis; AI_LOG. Due Wed 10/21. Personalized Final System briefs issued by Sat 10/24.

**Instructor prep:** Local embedding model choice; retrieval demo; brief template; review all Drift notes to draft briefs.

---

## E8 · Thu 10/22 · Multi-agent I: controller, worker, reviewer

*Chapters: Ch. 4, 6, 17; 25 (subagents)*

**Lecture (60)**

- 0–10 Framing: plan / do / check under every name since FIPA
- 10–30 Spine: roles, personas, result contracts, two-stage review, state graphs
- 30–45 Teardowns: FIPA/BDI; CAMEL/MetaGPT/AutoGen/CrewAI; LangGraph supervisor; Claude Code subagents
- 45–52 Reference design: ADR-0.18.0; HandoffResult; dispatch records; "credit is never inferred"
- 52–60 Evaluation lens + Card 8 brief

**Consultation (60)**

- 0–10 Stand-up; briefs acknowledged
- 10–46 Deep Drifts on Sortie 7; stations
- 46–60 Go/No-Go on Card 8

**Lab (30)**

- 0–30 Fly TP1: implementer returns a structured result; reviewer returns a verdict; malformed result rejected; capture

**Sprint deliverables:** Sortie 8 log; pair + contract + graph; Design Analysis; AI_LOG. Due Wed 10/28.

**Instructor prep:** Persona files; contract schemas; LangGraph demo with interrupt.

---

## E9 · Thu 10/29 · Multi-agent II: when coordination fails

*Chapters: Ch. 9, 18*

**Lecture (60)**

- 0–10 Framing: a subagent's claim is not evidence
- 10–30 Spine: the taxonomy; adversarial validation tiers; locks; cost routing; delegation and marketplaces
- 30–45 Teardowns: Cemri et al.; A2A delegation; agent marketplaces and contracts
- 45–52 Reference design: summary laundering (05-24); the repudiations (June); undispatched Stage 2 (08-21)
- 52–60 Evaluation lens + Card 9 brief (corner)

**Consultation (60)**

- 0–10 Stand-up
- 10–46 Deep Drifts on Sortie 8; stations
- 46–60 Go/No-Go on Card 9; each card names its planted falsehood

**Lab (30)**

- 0–30 Fly TP1: plant a false claim; adversary (other family or local) refutes; receipt recorded; capture

**Sprint deliverables:** Sortie 9 log; adversary + locks + routing; cost table; Design Analysis; AI_LOG. Due Wed 11/04.

**Instructor prep:** Cross-vendor adversary demo; cost accounting sheet; lock demo.

---

## E10 · Thu 11/05 · Evaluation I: evals as gates

*Chapters: Ch. 7, 19; 23*

**Lecture (60)**

- 0–10 Framing: evaluation is falsification
- 10–30 Spine: golden sets; regression deltas; judges and their biases; the RED witness; pre-registration
- 30–45 Teardowns: SWE-bench/GAIA/tau-bench; LLM-as-judge; gzkit eval runner and flighttest
- 45–52 Reference design: GZK-GOV-007; the hollow antibody; `gz arb red`
- 52–60 Evaluation lens + Card 10 brief

**Consultation (60)**

- 0–10 Stand-up
- 10–46 Deep Drifts on Sortie 9; stations
- 46–60 Go/No-Go on Card 10

**Lab (30)**

- 0–30 Fly TP1: golden set runs; remove the feature; gate goes red; capture

**Sprint deliverables:** Sortie 10 log; eval suite + delta + RED witness wired to a gate; Design Analysis; AI_LOG. Due Wed 11/11.

**Instructor prep:** Golden-set format; judge-blinding example; RED witness walkthrough.

---

## E11 · Thu 11/12 · Evaluation II: observability, red team, safety

*Chapters: Ch. 9, 20*

**Lecture (60)**

- 0–10 Framing: receipts over narrative
- 10–30 Spine: traces; receipts; cost/latency; the nine modes; system cards; guardrails
- 30–45 Teardowns: a frontier system card; observability stacks; trust-chain poisoning
- 45–52 Reference design: ARB receipts; trust doctrine; the 04-18 outage; the PII incident
- 52–60 Evaluation lens + Card 11 brief (red team)

**Consultation (60)**

- 0–10 Stand-up
- 10–46 Deep Drifts on Sortie 10; stations — Chase pairs exchange attack cards
- 46–60 Go/No-Go on Card 11

**Lab (30)**

- 0–30 Fly TP1: tracing on; one attack delivered by the Chase; outcome in the black box; capture

**Sprint deliverables:** Sortie 11 log (five attacks); tracing + cost table + guardrails; Design Analysis; AI_LOG. Due Wed 11/18.

**Instructor prep:** Attack card bank; tracing snippet; system-card excerpt.

---

## E12 · Thu 11/19 · Production deployment

*Chapters: Ch. 9, 21; 25 (closeout)*

**Lecture (60)**

- 0–10 Framing: from working to operated
- 10–30 Spine: serving; containers; secrets; limits; scheduling; rollback; the Heavy-lane gates; release ceremony
- 30–45 Teardowns: background agents; Copilot coding agent; gzkit closeout/patch release/MX
- 45–52 Reference design: distribution invariant; backfilled releases (#830); "loose in the bay, hard at the door"
- 52–60 Evaluation lens + Card 12 brief; ceremony scheduling

**Consultation (60)**

- 0–10 Stand-up
- 10–46 Deep Drifts on Sortie 11; stations
- 46–60 Go/No-Go on Card 12; book ceremony slots for 11/24–26

**Lab (30)**

- 0–30 Fly TP1: build image; run; roll back; ledger shows both; capture

**Sprint deliverables:** Sortie 12 log; served + containerized + release + rollback; runbook; Design Analysis; AI_LOG. Code freeze Mon 11/23.

**Instructor prep:** Container/serving demo; ceremony checklist; Calendly slots.

---

## Finals · Tue–Thu 11/24–26 · Closeout ceremonies

*Chapters: Ch. 26*

**Lecture (60)**

- —

**Consultation (60)**

- By appointment (30–40 min each): readiness; bill of materials; docs alignment; value walkthrough; live demo (student executes, instructor observes); attestation; audit

**Lab (30)**

- —

**Sprint deliverables:** Final System repository, release, Design Analysis Ledger (13), AI_LOG.md with final reflection. Due Thu 11/26 11:59 p.m.

**Instructor prep:** Ceremony record template; feedback/final-project.md per student.

---



---
