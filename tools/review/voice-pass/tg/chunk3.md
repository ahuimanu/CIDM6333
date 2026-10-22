# 18. Multi-Agent Coordination II: When Coordination Fails

> **Course use.** CIDM 6333 · E9. Status: **outline**.

## Learning outcomes

After this chapter you can:

- State the multi-agent failure taxonomy and recognize each mode in a trace.
- Implement cross-vendor adversarial validation, locks, and cost-aware routing.
- Explain delegation and handoff protocols, agent marketplaces and contracts, and cost and resource management.

## Outline

### 18.1 The taxonomy

- Specification/design, inter-agent misalignment, verification failures (Cemri et al.); gzkit's nine agent failure modes; summary laundering; hallucinated authorization.

### 18.2 Adversarial validation

- Tier 1 cross-vendor (different model family); tier 2 independent subagent; tier 3 human. REFUTED / NOT-REFUTED. A subagent's claim becomes evidence only when a receipt backs it.

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

> **Course use.** CIDM 6333 · E10. Status: **outline**.

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

> **Course use.** CIDM 6333 · E11. Status: **outline**.

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

> **Course use.** CIDM 6333 · E12. Status: **outline**.

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

> **Course use.** CIDM 6333 · E0; every week. Status: **outline**.

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

> **Course use.** CIDM 6333 · E0; every week. Status: **outline**.

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

> **Course use.** CIDM 6333 · E0; every week. Status: **outline**.

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

> **Course use.** CIDM 6333 · E1–E12. Status: **outline**.

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

> **Course use.** CIDM 6333 · E7 brief; finals week. Status: **outline**.

## Learning outcomes

After this chapter you can:

- Read a personalized brief and scope a governed revision.
- Deliver the Final System under the Heavy lane.
- Conduct a closeout ceremony: the student executes, the instructor observes and attests.

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

# Appendix A — Flight Card Template (course edition)

Copy this block into `evolution-NN/flight-card.md`. Fill every field **before** you request Go. Do not fill in the expected observables after the flight. Doctrine counts that as a violation.

```
FLIGHT CARD — SORTIE <N> : <short name>
════════════════════════════════════════════════════════════
ENVELOPE POSITION   : <center | expansion | corner>
DESIGN CLAIM        : <one sentence a single observation could disprove>
SYSTEMS UNDER TEST  : <the parts of YOUR system this sortie exercises>
SUBSTRATE           : <repo + commit + model/route; local or hosted>
DEPENDS ON          : <prior sorties that must have passed, or "none">

────────────────────────────────────────────────────────────
ENTRY CONDITIONS (go/no-go — all must hold)
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
  - reads    : <exact evidence slice handed over — never the narrative>
  - verdict  : PASS / FAIL, authored from evidence alone

────────────────────────────────────────────────────────────
DEBRIEF & SQUAWKS
  - black box vs card : <matched / diverged>
  - design signal     : sound | awkward-but-correct | wrong — why
  - squawks           : <each anomaly → issue # | design-feedback | card amendment | re-fly>
════════════════════════════════════════════════════════════
```


---

# Appendix B — Design Analysis Template

Write one Design Analysis per week, ~150 words. Commit it to `design-analyses/<system>.md`. Append one row to `design-analyses/LEDGER.md`.

```
# Design Analysis — <System> (<year>)

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

# Appendix C — The Nine Agent Failure Modes

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

# Appendix D — Glossary

*Seed list; grows with the course. Terms marked (gz) are gzkit's; (SD) are Sprint and Drift's.*

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

# Appendix E — Reading List

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

