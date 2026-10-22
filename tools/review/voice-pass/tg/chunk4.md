# Appendix F — Toolkit Setup (Route A and Route B)

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

## Known problems in py-gzkit 0.34.x (verified 2026-08-24)
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

# Appendix G — The gzkit Incident Casebook (2026)

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
| 2026-05-23 | The agent bundled four questions in one prompt | Operator economy of effort | Ch. 15 |
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
