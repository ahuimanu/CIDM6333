# e2-patterns-frameworks: speaker notes, before and after the voice pass

## Slide 1

### BEFORE

Evolution 2. Last week you built a loop that halts. This week you give it a name and a home. The framing sentence: every framework is a theory of who owns the loop, and choosing one is the first decision you will have to defend with alternatives on the table. Survey: LangChain to LangGraph, Pydantic AI, the role-based frameworks of 2023, and the vendor SDKs of 2025. Build: refactor the loop into a named pattern and write ADR-1. [0:00–0:01]

Cut from slide 1 (full wording):
- Evolution 2 · Lecture · Thu 09/10
- CIDM 6333 · Agentic Systems Design and Development · 4:00–5:00 · CC209 / Survey: LangChain → LangGraph · Pydantic AI · AutoGen / CrewAI / MetaGPT · the vendor SDKs   ·   Build: the loop refactored into a named pattern; ADR-1

### AFTER

Evolution 2. In Evolution 1 you built a loop that halts. In this Evolution you give that loop a name and a home. Every framework is a theory of who owns the loop, and the choice of a framework is the first decision you will defend with alternatives on the table. The survey covers LangChain to LangGraph, Pydantic AI, the role-based frameworks of 2023, and the vendor SDKs of 2025. The build refactors the loop into a pattern from the catalog and records the choice in ADR-1. [0:00–0:01]

Cut from slide 1 (full wording):
- Evolution 2 · Lecture
- CIDM 6333 · Agentic Systems Design and Development / Survey: LangChain → LangGraph · Pydantic AI · AutoGen / CrewAI / MetaGPT · the vendor SDKs   ·   Build: the loop refactored into a catalogued pattern; ADR-1

## Slide 2

### BEFORE

Ten on framing, twenty on the patterns because they are the build, fifteen on four teardowns grouped by their theory of control, seven on the reference design's model ADR, and eight on the evaluation lens and the card. Labor Day was Monday; nothing moved.

Cut from slide 2 (full wording):
- The five workflow patterns and the agent; when to keep it simple; refactoring E1's loop without touching the tool layer

### AFTER

The lecture has five parts: the framing, the pattern catalog (the longest part, because the patterns are the build), four teardowns grouped by their theory of control, the reference design's model ADR, and the evaluation lens with Flight Card 2.

Cut from slide 2 (full wording):
- The five workflow patterns and the agent; when to keep it simple; refactoring E1's loop without touching the tool layer

## Slide 3

### BEFORE

Framing. Do not learn a framework; learn what it assumes about control. LangGraph assumes you own every edge. The Claude Agent SDK assumes the vendor owns the loop and you supply tools and instructions. CrewAI assumes control is a conversation among roles. Those are theories, and the framework churn of 2022 to 2025 is the field arguing about them. Then the distinction from last week, sharpened: a workflow calls the model along paths you wrote; an agent lets the model steer. Most production agents are workflows and should be. Read the claim: same task, two patterns, identical tool traces, a difference the ADR predicted. If the prediction does not show up in the evidence, you wrote a rationalization. [~8 min]

Cut from slide 3 (full wording):
- Frameworks change monthly. Each one encodes a theory of where control should live — in your code, in the model, in the vendor's harness, or in a graph you draw. That theory is what you are choosing, and what you will defend.
- Workflow: the model is called along code paths you wrote. Agent: the model directs its own control flow. Most production 'agents' are workflows and should be — predictable, cheap, testable. Reach for the open loop only when the path cannot be known in advance.
- Tonight's claim, which Sortie 2 will try to disprove / The same task runs under two patterns with identical tool traces and a measurable difference in cost or quality that ADR-1 predicted. If the predicted consequence does not appear in the evidence, the ADR was rationalization, not a decision.

### AFTER

Framing. Learn what a framework assumes about control before you learn its API. LangGraph assumes that you own every edge. The Claude Agent SDK assumes that the vendor owns the loop and that you supply tools and instructions. CrewAI assumes that control is a conversation among roles. Each assumption is a theory, and the framework churn of 2022 to 2025 is the field arguing about those theories. The distinction from Evolution 1 now sharpens. A workflow calls the model along code paths you wrote. An agent lets the model direct its own control flow. Anthropic's guidance (December 2024) holds that most production agents are workflows and should be, because a workflow is predictable, cheap, and testable. Sortie 2 tests one statement: the same task runs under two patterns with identical tool traces, and the cost or quality difference that ADR-1 predicted appears in the evidence. If the predicted difference does not appear, the ADR recorded a rationalization. [~8 min]

Cut from slide 3 (full wording):
- A new framework has arrived every year since 2022. Each one encodes a theory of where control should live: in your code, in the model, in the vendor's harness, or in a graph you draw. When you pick a framework you pick its theory of control, and ADR-1 defends that choice.
- Workflow: your code calls the model along paths you wrote. Agent: the model directs its own control flow. A workflow is more predictable, cheaper, and easier to test, so build one wherever the path is known. Use the open loop only when the path cannot be known in advance.
- The statement Sortie 2 will try to disprove / The same task runs under two patterns with identical tool traces and a measurable difference in cost or quality that ADR-1 predicted. If the predicted consequence does not appear in the evidence, Sortie 2 fails, and the ADR stands as a rationalization of a choice already made.

## Slide 4

### BEFORE

The catalog. Five workflows and the agent. Prompt chaining: a fixed sequence with optional gates; accuracy over latency. Routing: classify, then dispatch. Parallelization, in two forms: sectioning and voting. Orchestrator-workers: a central model decomposes and delegates, and this is where next week's tools and week eight's subagents will plug in. Evaluator-optimizer: a producer and a critic in a loop, which is week ten's evaluation-as-gate in miniature. And the agent: the open loop you built last week, which the catalog puts last and recommends least. The advice in the source is to start with the simplest pattern that works and add complexity only when it measurably helps. That advice is your ADR's null hypothesis. [~8 min]

### AFTER

The catalog lists five workflows and the agent. Prompt chaining runs a fixed sequence with optional gates between steps and trades latency for accuracy. Routing classifies the input and dispatches it to a specialized path. Parallelization takes two forms, sectioning and voting. In orchestrator-workers a central model decomposes the task and delegates the parts, and the tools of Evolution 3 and the subagents of Evolution 8 plug in here. In evaluator-optimizer a producer and a critic run in a loop, which is the evaluation gate of Evolution 10 in miniature. The agent is the open loop you built in Evolution 1. The catalog puts it last and recommends it least. The source advises you to start with the simplest pattern that works and to add complexity only when it measurably helps. That advice is the null hypothesis of your ADR. [~8 min]

## Slide 5

### BEFORE

Worked example, in prose. Your E1 loop: model, step, answer or tool, repeat under budget; control sits with the model, bounded by code. Refactor one: orchestrator-workers. A planner splits the task; bounded workers each call one tool; a synthesis step answers. Control is now split, and each worker has its own budget. Refactor two: evaluator-optimizer. A producer drafts, a critic checks against criteria, at most K rounds. The halt is now a criterion rather than the model's say-so. The discipline for the sortie: hold the tool layer constant. Same tools, same order, or the refactor changed behavior and the comparison is meaningless. That is what makes the measured delta attributable to the decision in your ADR. [~7 min]

Cut from slide 5 (full wording):
- orchestrator(messages) → [subtask₁, subtask₂] / worker(subtask₁) → calls tool A / worker(subtask₂) → calls tool B / synthesize → answer /  / Control: split between a planner and bounded workers; each worker has its own budget. / Trace: same tools, same order — or the refactor changed behavior.
- producer(messages) → draft (tools A, B) / evaluator(draft, criteria) → PASS | revise / loop ≤ K rounds → answer /  / Control: a critic gates the halt; the halt condition is now a criterion, not a model's say-so. / Trace: same tools, plus evaluator turns you can count.
- Card 2's discipline: hold the tool layer constant so the only variable is the pattern. Then the cost or quality delta you measure is attributable to the decision you recorded, and to nothing else.

### AFTER

The worked example, in prose. Your E1 loop calls the model, reads a Step, either answers or calls a tool, and repeats under a budget. Control sits with the model, and code bounds it. The first refactor is orchestrator-workers. A planner splits the task, each bounded worker calls one tool, and a synthesis step produces the answer. Control is now split between the planner and the workers, and each worker has its own budget. The second refactor is evaluator-optimizer. A producer drafts, a critic checks the draft against criteria, and the loop runs at most K rounds. The halt is now a criterion rather than the model's say-so. The sortie requires one discipline: hold the tool layer constant. If the two runs do not call the same tools in the same order, the refactor changed behavior and the comparison measures nothing. With the tools held constant, the measured delta is attributable to the decision in your ADR and to nothing else. [~7 min]

Cut from slide 5 (full wording):
- orchestrator(messages) → [subtask₁, subtask₂] / worker(subtask₁) → calls tool A / worker(subtask₂) → calls tool B / synthesize → answer /  / Control: split between a planner and bounded workers; each worker has its own budget. / Trace: same tools, same order. A different order means the refactor changed behavior.
- producer(messages) → draft (tools A, B) / evaluator(draft, criteria) → PASS | revise / loop ≤ K rounds → answer /  / Control: an evaluator gates the halt. The loop stops when the draft meets a written criterion, and the producer cannot end the loop on its own say-so. / Trace: same tools, plus evaluator turns you can count.
- Card 2 holds the tool layer constant so that the pattern is the only variable. The cost or quality delta you measure can then be attributed to the decision ADR-1 recorded, and to nothing else.

## Slide 6

### BEFORE

The source's advice as a ladder, and each rung becomes a row in your ADR. Start with one model call and measure it; that is the baseline. Add a workflow only when the task decomposes and the gain is measurable, and you write the predicted delta before the run. Add an agent only when the path cannot be scripted and trust, budget, and evaluation exist, which is exactly what E1 gave you. Add a framework only when it buys something a stdlib loop cannot: checkpoints, tracing, typed handoffs. 'None' is a legitimate alternative and it must appear in ADR-1. The abstraction tax is the Drift problem: if you cannot explain what the framework did on turn three, you do not own the loop. [~5 min]

Cut from slide 6 (full wording):
- The abstraction tax: every layer a framework adds between you and the model call is a layer you cannot see into during Drift. If you cannot explain what the framework did on turn three, you do not own the loop; it owns you.

### AFTER

The source's advice forms a ladder, and each rung becomes a row in your ADR. Start with one model call and measure it. That measurement is the baseline row. Add a workflow only when the task decomposes and the gain is measurable, and write the predicted delta before the run. Add an agent only when the path cannot be scripted and trust, budget, and evaluation exist, which is what E1 gave you. Add a framework only when it buys something a stdlib loop cannot, such as checkpoints, tracing, or typed handoffs. 'None' is a legitimate alternative, and it must appear in ADR-1. Every layer a framework adds between you and the model call is a layer you cannot see into during Drift (the abstraction tax). If you cannot explain what the framework did on turn three, you do not own the loop. [~5 min]

Cut from slide 6 (full wording):
- Each layer a framework adds between your code and the model call is a layer you cannot inspect during Drift. This course calls that cost the abstraction tax. If you cannot explain what the framework did on turn three, you cannot defend the loop's behavior in Drift.

## Slide 7

### BEFORE

First teardown: the same company, two theories of control. LangChain in late 2022 wrapped the ReAct prompt in objects: chains, agents, tools, memory. It made the loop importable and it hid the loop, and practitioners paid the abstraction tax in opaque prompts and release-to-release drift. LangGraph in 2024 is the correction: the agent as a state graph you draw, with typed state, checkpoints, and a human interrupt as an edge. You own every edge. The four rows on the table are where the two differ most: planning went from hidden to explicit, memory from opaque objects to typed state, governance from none to an interrupt, runtime from a script to persisted runs with tracing. Judgment loop: the decision was to move control from the library into a graph the user draws; the cost is that you now have to draw it. [~5 min]

Cut from slide 7 (full wording):
- Chains, agents, tools, memory as objects — the first wrapper around the ReAct prompt. It made the loop importable, and it hid the loop. Practitioners hit the abstraction tax: opaque prompts, deep class hierarchies, behavior that changed with each release.
- The agent as a state graph: nodes are steps, edges are control flow you draw, state is an explicit typed object, checkpoints persist it, and a human-in-the-loop interrupt is an edge. You own every edge — which is the theory of control the first version denied you.

### AFTER

The first teardown covers one company and two theories of control. LangChain, in late 2022, wrapped the ReAct prompt in objects (chains, agents, tools, memory). The wrapper made the loop importable and also hid it, so practitioners paid the abstraction tax in opaque prompts and release-to-release drift. LangGraph, in 2024, corrected this by modeling the agent as a state graph you draw, with typed state, checkpoints, and a human interrupt as an edge. You own every edge. The four rows of the table are where the two differ. Planning went from hidden to explicit, memory from opaque objects to typed state, governance from none to an interrupt, and runtime from a script to persisted runs with tracing. In judgment-loop terms, LangChain's authors moved control from the library into a graph that the user draws, and the cost is that you now have to draw it. [~5 min]

Cut from slide 7 (full wording):
- Chains, agents, tools, and memory as objects: the first wrapper around the ReAct prompt. LangChain made the loop importable, and it also hid the loop from the developer. Developers who used it paid the abstraction tax: opaque prompts, deep class hierarchies, and behavior that changed with each release.
- The agent as a state graph: nodes are steps, edges are control flow you draw, state is an explicit typed object, checkpoints persist it, and a human-in-the-loop interrupt is an edge. You draw every edge yourself, and LangChain's first version gave you no such control.

## Slide 8

### BEFORE

Two more theories. Pydantic AI says the type system owns the boundary: every output is validated before it can act, tools are typed functions, and a malformed call never executes. Your E1 Step schema was this in miniature. The cost is that what the schema cannot express the model cannot do, and small models fail schemas more often, which is next week's lesson. The role-based frameworks say control is a conversation. CAMEL's two role players, MetaGPT's software company as prompts, AutoGen's chat-as-coordination, CrewAI's crews with roles and a process. It is FIPA and BDI rediscovered, and we go there properly in week eight. The cost is AutoGPT's cost multiplied: nobody in the conversation is an evaluator, and one role's polished summary becomes the next role's fact. [~5 min]

Cut from slide 8 (full wording):
- The model's every output — tool call, final result — is validated against a Pydantic model; a malformed one is retried or rejected before it can act. Dependencies are injected; tools are plain functions with schemas derived from type hints. /  / Theory of control: the type system owns the boundary between model and code. Your E1 Step schema was this idea in miniature. /  / Cost: what the schema cannot express, the model cannot do — and small local models fail the schema more often (E3's lesson).
- CAMEL: two role-playing agents talk a task to completion. MetaGPT: a software company as prompts — PM, architect, engineer — with SOPs as the coordination mechanism. AutoGen: conversation is the coordination primitive; agents are chat participants. CrewAI: roles, goals, backstories, and a process (sequential or hierarchical). /  / Theory of control: control is a conversation among personas. It is FIPA and BDI rediscovered with a language model in the reasoner slot (E8). /  / Cost: the same as AutoGPT's, multiplied — no one in the conversation is an evaluator, and a polished summary from one role becomes the next role's fact.

### AFTER

Two more theories. Pydantic AI holds that the type system owns the boundary between model and code. The library validates every output before the output can act, tools are typed functions, and a malformed call never executes. Your E1 Step schema was this idea in miniature. The cost is that what the schema cannot express the model cannot do, and small local models fail the schema more often, which Evolution 3 measures. The role-based frameworks hold that control is a conversation. CAMEL runs two role players, MetaGPT runs a software company as prompts, AutoGen treats chat as coordination, and CrewAI runs crews with roles and a process. This is FIPA and BDI rediscovered with a language model in the reasoner slot, and Evolution 8 takes it up in full. The cost is AutoGPT's cost multiplied. No one in the conversation is an evaluator, so one role's polished summary becomes the next role's fact. [~5 min]

Cut from slide 8 (full wording):
- Pydantic AI validates every model output (a tool call or a final result) against a Pydantic model, and it retries or rejects a malformed output before that output can act. The framework injects dependencies, and tools are plain functions whose schemas come from their type hints. /  / Theory of control: the type system owns the boundary between model and code. Your E1 Step schema applied the same idea on a small scale. /  / Cost: the model cannot do what the schema cannot express, and small local models fail the schema more often (E3 shows this).
- CAMEL: two role-playing agents talk a task to completion. MetaGPT: a software company as prompts (PM, architect, engineer), with SOPs as the coordination mechanism. AutoGen: conversation is the coordination primitive; agents are chat participants. CrewAI: roles, goals, backstories, and a process (sequential or hierarchical). /  / Theory of control: control is a conversation among personas. These frameworks rediscover FIPA and BDI with a language model in the reasoner slot (E8). /  / Cost: the same as AutoGPT's, multiplied. No role in the conversation evaluates, so a polished summary from one role becomes the next role's fact.

## Slide 9

### BEFORE

The vendor SDKs, read by their theory of control. OpenAI's Agents SDK: agents with handoffs and guardrails, a runner that loops, tracing built in. The Claude Agent SDK: the harness as a library; the vendor owns the loop, you supply tools, instructions, and hooks. Google's ADK: a hierarchy, with workflow agents for sequential, parallel, and loop control and A2A for peers. Notice each vendor's governance story: guardrail tripwires, permission prompts and hooks, callbacks. None of them records what was attested. [Verify the feature rows against current docs before class; they change monthly, and that churn is the lesson.] [~5 min]

Cut from slide 9 (full wording):
- Teardown: the vendor SDKs (2025) — who owns the loop?
- Details are as of early 2026 — verify current names and features before class; these SDKs change monthly, which is itself the lesson.

### AFTER

The vendor SDKs, read by their theory of control. OpenAI's Agents SDK composes agents with handoffs and guardrails, a runner loops, and tracing ships with the runner. The Claude Agent SDK ships the harness as a library: the vendor owns the loop, and you supply tools, instructions, and hooks. Google's ADK builds a hierarchy, with workflow agents for sequential, parallel, and loop control and A2A for peers. Each vendor has a governance story (guardrail tripwires, permission prompts and hooks, callbacks), and none of the three records what was attested. The feature rows are as of early 2026, and the rate at which they go stale is part of the teardown. [~5 min]

Cut from slide 9 (full wording):
- Teardown: the vendor SDKs (2025), and who owns the loop
- Details are as of early 2026. These SDKs change monthly, so check current names and features against each vendor's documentation.

## Slide 10

### BEFORE

The reference design's model ADR is about a command-line parser, and that is why it is a good model: the stakes are low and the reasoning is clean. Argparse over click. Click was more popular; popularity was rejected as a reason. What counted: zero external dependencies for a kit whose job is governance, a smaller upgrade surface, and the stdlib-first posture that later became doctrine. [Verify against the ADR text.] Your ADR-1 takes the same shape: intent from the PRD, the decision in one sentence, at least three alternatives including none, consequences both ways with the one you will measure, a scorecard, and a checklist of what the choice must support by week twelve. ADRs before code. Written after, they are rationalization. [~5 min]

Cut from slide 10 (full wording):
- Decision: build gzkit's CLI on the standard library's argparse rather than click. /  / Alternatives considered: click, typer, argparse — each with consequences, not adjectives. /  / The rationale that gives the ADR its name: click's popularity was rejected as a reason. The reasons that counted were zero external dependencies for a governance kit, a smaller attack and upgrade surface, and the stdlib-first posture that later became doctrine. /  / [Summarized from the ADR's title and the book's outline — verify the alternatives and consequences against the ADR text before class.]
- 1. Intent — what the loop must do (from the PRD) / 2. Decision — pattern + framework, in one sentence / 3. Alternatives — at least three, including 'none / stdlib'; each with what it buys and what it costs / 4. Consequences — positive and negative, and the one you will measure in Sortie 2 / 5. Decomposition scorecard — the decision scored against the alternatives on the criteria you named / 6. Feature checklist — what the choice must support by E12 (tools, MCP, memory, multi-agent, evals, serving) /  / ADRs before code. After is post-hoc rationalization.

### AFTER

The reference design's model ADR decides a command-line parser. The stakes are low, so the reasoning is easy to read, and for this reason it is a good model. The decision was argparse over click. Click was the more popular library, and the ADR rejected popularity as a reason. The reasons that counted were zero external dependencies for a kit whose job is governance, a smaller upgrade surface, and the stdlib-first posture that later became doctrine. Your ADR-1 takes the same shape: intent from the PRD, the decision in one sentence, at least three alternatives including none, consequences in both directions with the one you will measure, a scorecard, and a checklist of what the choice must support by Evolution 12. Write the ADR before the code. An ADR written after the code records a rationalization. [~5 min]

Cut from slide 10 (full wording):
- Decision: build gzkit's CLI on the standard library's argparse rather than click. /  / Alternatives considered: click, typer, argparse, each recorded with its consequences rather than with adjectives. /  / The ADR's title comes from its rationale: the decision rejected click's popularity as a reason. The reasons that counted were zero external dependencies for a governance kit, a smaller attack and upgrade surface, and the stdlib-first posture that later became doctrine. /  / [Summarized from the ADR's title and the book's outline — verify the alternatives and consequences against the ADR text before class.]
- 1. Intent: what the loop must do (from the PRD) / 2. Decision: pattern + framework, in one sentence / 3. Alternatives: at least three, including 'none / stdlib'; each with what it buys and what it costs / 4. Consequences: positive and negative, and the one you will measure in Sortie 2 / 5. Decomposition scorecard: the decision scored against the alternatives on the criteria you listed / 6. Feature checklist: what the choice must support by E12 (tools, MCP, memory, multi-agent, evals, serving) /  / Write the ADR before the code. An ADR written after the code is post-hoc rationalization.

## Slide 11

### BEFORE

Two minutes on how to stress a decision before you record it. Three forcing functions from the reference design's planning step. Pre-mortem: it is week twelve and the choice failed; write the story, and whatever you wrote is a consequence. What would have to be true for the alternative to have been right; if that is plausible, you need a measurable consequence. Constraint archaeology: where did each constraint come from; habit is not a constraint. Then the ten challenges, which you will use on a peer's ADR at the Chase station: so what, scope, alternative, dependency, gold standard, timeline, evidence, consumer, regression, parity. [Challenge list from chapter 11; expand each from gzkit's guide-adr.md if it differs.] [~2 min]

Cut from slide 11 (full wording):
- Three forcing functions, and ten challenges for your peer
- It is week twelve and this framework choice failed. Write the story. Whatever you wrote is a consequence for the ADR.
- So what? — what changes if this is wrong / Scope — what is deliberately out / Alternative — the strongest one you did not pick / Dependency — what this now requires / Gold standard — what 'good' would look like / Timeline — when will we know / Evidence — what you measured, not read / Consumer — who has to live with it / Regression — what got worse / Parity — what the alternative does that yours cannot
- 'What would have to be true' for the rejected alternative to have been right? If it is plausible, your decision needs a measurable consequence.

### AFTER

Stress a decision before you record it. The reference design's planning step supplies three forcing functions. In the pre-mortem, assume it is Evolution 12 and the choice has failed, then write the story. Whatever you wrote is a consequence. In the second, ask what would have to be true for the rejected alternative to have been right. If that is plausible, your decision needs a measurable consequence. In constraint archaeology, ask where each constraint came from (the PRD, the syllabus, or habit). Habit is not a constraint. The ten challenges, which you will put to a peer's ADR at the Chase station, are so what, scope, alternative, dependency, gold standard, timeline, evidence, consumer, regression, and parity (the list is chapter 11's). [~2 min]

Cut from slide 11 (full wording):
- Three forcing functions, and ten challenges for your peer
- Assume that in week twelve this framework choice has failed, and write the story of the failure. Add each consequence in the story to the ADR.
- So what? What changes if this is wrong / Scope: what is deliberately out / Alternative: the strongest one you did not pick / Dependency: what this now requires / Gold standard: what 'good' would look like / Timeline: when the evidence will arrive / Evidence: what you measured, not what you read / Consumer: who has to live with it / Regression: what got worse / Parity: what the alternative does that yours cannot
- 'What would have to be true' for the rejected alternative to have been right? If it is plausible, your decision needs a measurable consequence.

## Slide 12

### BEFORE

Weak: a framework chosen because a tutorial used it, alternatives as names, a refactor that also changed the tools so nothing is attributable, better asserted, ADR written afterward. Sound: two patterns, identical traces in the ledger, one consequence predicted and measured, three real alternatives including none, a scorecard whose winner is not the feature count, ADR committed before the refactor. Exceptional, and this is the one I want to see: the prediction did not appear and the ADR was amended with the evidence. A wrong prediction honestly recorded is worth more than a right one you cannot show. [~4 min]

Cut from slide 12 (full wording):
- Evaluation lens: a strong Sortie 2 and a strong ADR-1
- Framework chosen because a tutorial used it / ADR lists alternatives as names with no consequences / Refactor changed the tools too; traces differ; delta unattributable / 'Better' asserted; nothing measured / ADR written after the code
- Two patterns, same task, identical tool traces in the ledger / One consequence predicted in the ADR and measured: cost, latency, or a quality score / Three alternatives including none/stdlib, each with what it buys and costs / Scorecard filled; the winner is not the one with the most features / ADR committed before the refactor commit
- The predicted consequence did not appear — and the ADR was amended, with the evidence / A pre-mortem paragraph that names a week-12 failure and a mitigation / The peer's ten-challenge review answered in the ADR, not dismissed / A note on what the framework hid on turn three, and how you found out

### AFTER

A weak submission chose its framework because a tutorial used it, lists alternatives as names, refactored the tools along with the pattern so that nothing is attributable, asserts 'better' without a measurement, and wrote the ADR afterward. A sound submission runs two patterns with identical traces in the ledger, predicts one consequence and measures it, lists three real alternatives including none, fills a scorecard whose winner is not the feature count, and commits the ADR before the refactor. An exceptional submission, and the one I want to see, records a prediction that did not appear and amends the ADR with the evidence. The amended ADR gives the Chase the prediction, the evidence, and the correction on one record, which a correct prediction with no evidence cannot give. [~4 min]

Cut from slide 12 (full wording):
- Evaluation lens: a strong Sortie 2 and a strong ADR-1
- Framework chosen because a tutorial used it / ADR lists alternatives as names with no consequences / Refactor changed the tools too; traces differ; delta unattributable / 'Better' asserted; nothing measured / ADR written after the code
- Two patterns, same task, identical tool traces in the ledger / One consequence predicted in the ADR and measured: cost, latency, or a quality score / Three alternatives including none/stdlib, each with what it buys and costs / Scorecard filled; the winner is not the one with the most features / ADR committed before the refactor commit
- The predicted consequence did not appear, and the ADR was amended with the evidence attached / A pre-mortem paragraph that describes a week-12 failure and a mitigation / The peer's ten-challenge review answered in the ADR, not dismissed / A note on what the framework hid on turn three, and how you found out

## Slide 13

### BEFORE

Card two, still at the center of the envelope, and the first sortie with a dependency: Sortie 1 must have passed. The claim again. Three test points: the task under pattern A with a measurement, the same task under pattern B with the tool sequence identical, then the comparison against the prediction in the ADR. The falsifier people miss is the last one: an ADR dated after the refactor commit is a fail, because the prediction was not a prediction. Finish the card at five; Go or No-Go at 5:46; fly test point one in lab. [~3 min]

Cut from slide 13 (full wording):
- Flight Card 2 brief — Sortie 2: two patterns, one trace
- Center of the envelope · depends on Sortie 1 PASS · Go at 5:46
- ENVELOPE            center / DESIGN CLAIM        The same task runs under two patterns with identical tool traces and a measurable difference in cost or quality that ADR-1 predicted. / SYSTEMS UNDER TEST  E1 loop · pattern A · pattern B · tool layer (held constant) · ledger · ADR-1 / DEPENDS ON          Sortie 1 PASS on record / ENTRY CONDITIONS    clean tree · ADR-1 committed BEFORE the refactor commit · Go recorded / TEST POINTS         1 task under pattern A   → ledger: tool events [A₁…Aₙ]; cost/latency/quality recorded /                     2 same task, pattern B   → ledger: identical tool event sequence; second measurement /                     3 compare               → delta in the direction and rough size ADR-1 predicted / INSTRUMENTATION     ledger: two runs, tool sequences equal; receipts: run hashes; artifact: ADR-1 with the prediction, dated before TP1 / FALSIFIERS          tool sequences differ · no measurement recorded · the ADR's predicted consequence does not appear · ADR dated after the refactor / ABORT               framework install/runtime failure unrelated to the pattern (squawk) / CHASE               peer, from the two ledger slices and the ADR only → PASS / FAIL

### AFTER

Flight Card 2 stays at the center of the envelope and is the first sortie with a dependency: Sortie 1 must have passed. The design claim is the same statement: the same task runs under two patterns with identical tool traces and the cost or quality delta that ADR-1 predicted. There are three test points: the task under pattern A with a measurement, the same task under pattern B with the tool sequence identical, and the comparison against the prediction in the ADR. The fourth falsifier is the one to read twice. An ADR dated after the refactor commit is a FAIL, because an ADR dated after the result could have been written from the result, and the Chase cannot tell the difference. [~3 min]

Cut from slide 13 (full wording):
- Flight Card 2 brief (Sortie 2): two patterns, one trace
- Center of the envelope · depends on Sortie 1 PASS
- ENVELOPE            center / DESIGN CLAIM        The same task runs under two patterns with identical tool traces and a measurable difference in cost or quality that ADR-1 predicted. / SYSTEMS UNDER TEST  E1 loop · pattern A · pattern B · tool layer (held constant) · ledger · ADR-1 / DEPENDS ON          Sortie 1 PASS on record / ENTRY CONDITIONS    clean tree · ADR-1 committed BEFORE the refactor commit · Go recorded / TEST POINTS         1 task under pattern A   → ledger: tool events [A₁…Aₙ]; cost/latency/quality recorded /                     2 same task, pattern B   → ledger: identical tool event sequence; second measurement /                     3 compare               → delta in the direction and rough size ADR-1 predicted / INSTRUMENTATION     ledger: two runs, tool sequences equal; receipts: run hashes; artifact: ADR-1 with the prediction, dated before TP1 / FALSIFIERS          tool sequences differ · no measurement recorded · the ADR's predicted consequence does not appear · ADR dated after the refactor / ABORT               framework install/runtime failure unrelated to the pattern (squawk) / CHASE               peer, from the two ledger slices and the ADR only → PASS / FAIL

## Slide 14

### BEFORE

Close. A framework is a theory of who owns the loop. Choose one on evidence, record what you gave up, and be ready to be wrong where the ledger can see it. Consultation at five: Sortie 1 verdicts, and your framework leaning in one sentence.

### AFTER

A framework is a theory of who owns the loop. Choose one on evidence, record what you gave up, and be ready to be wrong where the ledger can see it.

