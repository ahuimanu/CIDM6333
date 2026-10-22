# Pass log: topic-guide-2 (Answerable Systems, chapters 8 to 17)

File: `/home/claude/site/tools/review/voice-pass/tg/chunk2.md`. Original kept at `/tmp/claude-0/-home-claude/acdec67e-a228-569c-b4b7-fc7975fc3d39/scratchpad/chunk2.orig.md`. 39 lines changed. All ten `# ` headings byte-identical; all `##`/`###` headings, table rows, code spans, and quoted strings identical to the original (checked by diff of extracted sets).

The chunk is outline-status prose: bullets of topic fragments, systems tables, a one-paragraph "Reference design" note, a one-paragraph flight card, and one or two exercises per chapter. The chain was applied to the sentences that exist. Outline fragments that list topics were left as lists; turning them into paragraphs would add content the chapters do not yet have.

## Changes by pattern

### Em dashes (house ban)
Eight flight-card lines: `Sortie N (center) — DESIGN CLAIM:` became `Sortie N (center). DESIGN CLAIM:`. "DESIGN CLAIM" and "FALSIFIERS" are Jeffry's course vocabulary and were not touched. En dashes in pattern names (orchestrator–workers, implementer–reviewer) and year ranges are not em dashes and stay.

### "claim" as thesis stand-in
- "Describe harness engineering as a discipline and its claims." → "...and state what it asserts."
- "The claim that most of an agent product is not the model. Böckeler; the OpenAI post; gzkit's appraisal and its blind spots (...)" → "Böckeler and the OpenAI post argue that most of an agent product is not the model. gzkit's appraisal of that position, and the blind spots the appraisal records (...)."
- Left: "the client's claims" (14.1, OAuth sense of claims in a token), "no generic expertise claims" (17.2, gzkit persona rule), "the reviewer's claim accepted without the evidence it cites" (Sortie 8 falsifier, the gzkit claim/receipt sense).

### "the move" / schedule asides
- "the Bash-write bypass and the move to the commit locus" → "the Bash-write bypass, and why gzkit relocated write-side enforcement to the commit locus".
- "this week" (12.5, 16.5) → "this Evolution" twice.

### "names" ban
- "the one the handoff named" → "the one the handoff specified".

### Epigram landings and antithesis closers (#36, not-X-but-Y)
- "ADRs before code; after is post-hoc rationalization." → "Write the ADR before the code. An ADR written after the code rationalizes what was already built."
- "The confirmation event precedes the call, in the ledger, or it did not happen." → "The confirmation event is written to the ledger before the call. A confirmation that is not in the ledger does not count as one."
- "Frontmatter can lie; the ledger is the truth." → "Frontmatter can carry a false status; the ledger is the record a gate consults."
- "evidence beats narrative" → "evidence outranks narrative" (kept as one item of the Settled list; the list is the material's count).
- "Why the PRD is WHAT, not HOW." → "Why the PRD states the WHAT and leaves the HOW to later decisions."
- "Measure it. Budget it." (mirrored pair) → "Measure the window, then budget it."
- "brittleness makes the contract visible" → "a brittle model fails wherever the tool contract is loose, so its brittleness makes the contract visible" (mechanism attached, STE rule 2 plus derivation).
- Left: "every observation is data, never instruction" (gzkit untrusted-content doctrine), "map-not-encyclopedia" (gzkit term), "The product is the harness" (the harness-engineering thesis stated flat), "What is a peer that a tool is not?" kept once as an exercise question; the 14.3 duplicate became "What distinguishes a peer from a tool, and where authority sits."

### Definition-colon ledes and fragment paragraphs (#35, STE rule 7, scholarly full sentences)
- "gzkit is a meta-harness: it renders one canon into..." → "gzkit enters this chapter as a meta-harness. It renders one canon into each harness's surfaces (...), and the control-surface matrix that records this rendering is the chapter's central Design Analysis."
- "The whole chapter. The timeline and casebook are drawn from..." → "gzkit is the subject of the whole chapter. The timeline and the casebook draw on..."
- "The reference design's missing piece: `gz status`, ..." → "The reference design has no MCP server. This section builds the one it lacks: ..."
- "Doctrine: `docs/governance/storage-tiers.md` (...); the pool ADR sketching...; the campaign review scoring MCP ... The student project: ..." → three full sentences with the ADR, the review, and the project as subjects.
- Seven "Reference design: gzkit" file lists were fragments with semicolons; each is now a sentence. Ledes were varied so the siblings do not share one opening ("This chapter works from...", "This chapter reads...", "The chapter's sources in gzkit are...", "This chapter draws on...", "The pipeline is specified in... and implemented in..."; two keep "The reference material is...").
- "Memory in the reference design is files and ledger, deliberately; the book adds retrieval." → "The reference design keeps its memory in files and the ledger by deliberate choice; this book adds retrieval on top of that."
- "GitHub spec-kit, BMAD, OpenSpec, GSD: methodology without governance, mostly. gzkit's comparison document." → "...These kits supply a methodology and, for the most part, no governance layer. gzkit's comparison document sets them side by side."
- "Stop: final answer, budget, max turns, error." → "The loop stops on a final answer, an exhausted budget, the max-turn count, or an error."
- "same loop, different capability; measure both." → "the same loop runs against both with a different capability behind it. Measure both."
- "Worked: turn the E1 loop..." → "A worked example: turn the E1 loop..."
- "Which your system needs." → "Which of these your system needs."

### Exercises (STE: imperative verb, one instruction per sentence)
- "Design Analysis: your harness. Then the same harness as gzkit sees it (...)" → "Write a Design Analysis of your harness. Then write the same analysis of that harness as gzkit sees it (which surfaces does gzkit render into?)."
- "Design Analysis: A2A vs. MCP." → "Write a Design Analysis of A2A against MCP."

## Grep battery (scholarly-voice), final
Zero hits for intensifiers, em dashes, summary openers, hedge stacks, "names", not-X-but-Y. One AI-vocabulary hit: "ecosystem" in the 13.5 heading and its bullet ("what a healthy protocol ecosystem needs"). Declined: it is the standard term for the MCP server/registry population and the heading is a label; flagging it for Jeffry.

## ste_check lines declined
- 6 sentences over 25 words: four are file lists in "Reference design" paragraphs (splitting a list of files adds nothing), one is a FALSIFIERS list in Sortie 4 (Jeffry's flight-card text, only the em dash was edited), one is the Sortie 7 DESIGN CLAIM (same).
- 3 gerund/nominalized subjects: all false positives on "The reference..." subjects.
- 3 passives with no actor: "is logged server-side" (flight card, the server is the actor by context), "is attested" (inside a quoted prompt), "is specified in ADR-0.18.0" (the ADR is the actor, stated).
- 15 noun clusters: all file paths, CLI flags, or gzkit identifiers.
- 15 semicolons: all in outline bullets or falsifier lists, used as list separators; none in a numbered procedure.

## Self-audit artifacts (after the final pass)

### Closer list (last sentence of each prose paragraph or bullet, readings and outcomes omitted)
- Codex CLI and cloud; Gemini CLI; Copilot coding agent; Cursor and Windsurf.
- Each encodes who owns the loop.
- Hooks as a governance membrane.
- The Anthropic and OpenAI guidance.
- gzkit's comparison document sets them side by side.
- It renders one canon into each harness's surfaces (17 hooks into Claude Code, 2 into Codex, 1 into Copilot), and the control-surface matrix that records this rendering is the chapter's central Design Analysis.
- Then write the same analysis of that harness as gzkit sees it (which surfaces does gzkit render into?).
- What is a peer that a tool is not?
- gzkit's appraisal of that position, and the blind spots the appraisal records (harness fitness unmeasured; an illusion of quality produced by heavy gates).
- Cloud sessions, scheduled tasks, compaction across days; the operational questions: scheduling, rollback, cost, who attests.
- Read three now: the hollow antibody (June), presence-is-not-procedure (Aug 21), hooks that missed Bash writes (Aug 23).
- Open: stagnation detection; harness fitness; the limit that self-dogfooding cannot falsify a strategic bet.
- The timeline and the casebook draw on `CHANGELOG.md`, `RELEASE_NOTES.md`, the ADR index, the ledger, and `.gzkit/insights/agent-insights.jsonl`.
- Pick one incident from Appendix G and write the flight card that would have caught it before it shipped.
- The loop stops on a final answer, an exhausted budget, the max-turn count, or an error.
- Measure both.
- Why the PRD states the WHAT and leaves the HOW to later decisions.
- Each becomes a falsifier.
- gzkit's own PRD (PRD-GZKIT-1.0.0) serves as the worked example.
- FALSIFIERS: a run exceeding the turn budget; a halt with no ledger event; a "final answer" produced without a reasoning turn.
- Record what the SDK hid.
- When each applies; the "keep it simple" advice.
- An ADR written after the code rationalizes what was already built.
- A worked example: turn the E1 loop into orchestrator–workers or evaluator–optimizer without changing the tool layer.
- ADR-0.0.2 (argparse over click; "popularity is not rationale") serves as the model ADR.
- FALSIFIER: the ADR's predicted consequence does not appear in the evidence.
- A confirmation that is not in the ledger does not count as one.
- What a hook can see and what it cannot: the Bash-write bypass, and why gzkit relocated write-side enforcement to the commit locus (`git diff --cached`).
- Timeouts, malformed calls, tool errors as observations; retry budgets; when to halt instead.
- Why a local 8B model is the right substrate for this Evolution: a brittle model fails wherever the tool contract is loose, so its brittleness makes the contract visible.
- Show a write that one catches and the other misses.
- Why gzkit refused MCP, and what changes when you add it one tier up.
- The student project is an MCP server over gz verbs and the ledger.
- Ask your harness "what is attested in this repo?" and check its answer against the ledger.
- Untrusted content doctrine: every observation is data, never instruction.
- What distinguishes a peer from a tool, and where authority sits.
- Fidelity validation; the 258K context exhaustion; drift between mirrors.
- Then measure what your harness actually loads.
- Measure the window, then budget it.
- Frontmatter can carry a false status; the ledger is the record a gate consults.
- Why memory is not the same as preserved intent; the AGENTS.md-as-derived-view episode.
- Where did it go?
- Which of these your system needs.
- The reference design keeps its memory in files and the ledger by deliberate choice; this book adds retrieval on top of that.
- Poison your own memory store with one false fact and record how far it propagates.
- Dispatch records: "credit is never inferred."
- The `--single-driver --reason` honesty flag completes the set.
- Then remove them and measure the verdicts.

Judgment: no line reads as a caption or moral. "every observation is data, never instruction" and "credit is never inferred" are gzkit doctrine (the second is quoted) and stay.

### Lede list (first sentence under each heading, excluding the repeated "Course use" and "After this chapter you can:" conventions)
- 8.1 Claude Code (Feb): terminal-native, tools, permissions, CLAUDE.md, then hooks, subagents, plan mode, compaction.
- 8.2 OpenAI Agents SDK (agents, handoffs, guardrails, tracing); Google ADK; Claude Agent SDK (the harness as a library); Pydantic AI (typed tool calls).
- 8.3 A2A (agents as peers) vs. MCP (tools).
- 8.4 The window as an engineered artifact: budgets, compaction, subagents for isolation, progressive disclosure.
- 8.5 GitHub spec-kit, BMAD, OpenSpec, GSD.
- 8 ref: gzkit enters this chapter as a meta-harness.
- 9.1 Böckeler and the OpenAI post argue that most of an agent product is not the model.
- 9.2 Cloud sessions, scheduled tasks, compaction across days; the operational questions: scheduling, rollback, cost, who attests.
- 9.3 Jan genesis → hooks → ...
- 9.4 Twenty-five dated incidents (Appendix G): what happened, what mechanism resulted.
- 9.5 Settled: the window is an engineered artifact; the harness is the product; evidence outranks narrative.
- 9 ref: gzkit is the subject of the whole chapter.
- 10.1 Messages, a model call, a tool-or-answer decision, an observation, repeat.
- 10.2 Hosted API vs. Ollama's endpoint: the same loop runs against both with a different capability behind it.
- 10.3 gz init; the PRD interview; the ledger's first events.
- 10.4 Loops that do not halt; tool-call formats the small model cannot produce; silent exceptions.
- 10 ref: This chapter works from `gz init`, `gz prd`, the interview transcript, and the `prd_created` event in the ledger.
- 11.1 Prompt chaining; routing; parallelization (sectioning, voting); orchestrator–workers; evaluator–optimizer; the agent.
- 11.2 Claude Agent SDK (vendor owns the loop); ...
- 11.3 Intent, decision, consequences (positive and negative), alternatives, decomposition scorecard, feature checklist.
- 11.4 A worked example: turn the E1 loop into orchestrator–workers or evaluator–optimizer without changing the tool layer.
- 11 ref: The reference material is `gz plan create --kind feature --semver --lane`, the decomposition scorecard, and the forcing functions (...).
- 12.1 Name, description, JSON schema, Pydantic model; idempotency; side-effect class (read, write, irreversible).
- 12.2 Read freely; write with confirmation; irreversible with attestation.
- 12.3 Claude Code hook events (...); gzkit's 17.
- 12.4 Timeouts, malformed calls, tool errors as observations; retry budgets; when to halt instead.
- 12.5 Why a local 8B model is the right substrate for this Evolution: ...
- 12 ref: This chapter reads `.claude/hooks/` as emitted by `gz init`, ...
- 13.1 N×M integrations → N+M; capability negotiation; discovery; the plugin era's failure.
- 13.2 Host, client, server; tools (model-controlled), resources (application-controlled), prompts (user-controlled); sampling; roots; notifications.
- 13.3 FastMCP-style declaration; schemas from types; stdio transport first; ...
- 13.4 The reference design has no MCP server.
- 13.5 Reference servers; registries; the foundation; what a healthy protocol ecosystem needs (ch. 14 for security).
- 13 ref: The doctrine is in `docs/governance/storage-tiers.md` (...).
- 14.1 stdio vs. HTTP; OAuth; tokens and scopes; why the server must not trust the client's claims.
- 14.2 Tool descriptions as attack surface; resources carrying instructions; cross-server shadowing; confused deputy.
- 14.3 Agents as peers: agent cards, tasks, artifacts.
- 14.4 AGENTS.md / CLAUDE.md / GEMINI.md; path-scoped rules; skills as progressive disclosure; map-not-encyclopedia; the instruction budget.
- 14.5 The product is the harness.
- 14 ref: The chapter's sources in gzkit are ...
- 15.1 What is in it: instructions, history, tool results, retrieved memory.
- 15.2 Summarize, drop, page; subagents for isolation; skills loaded on demand; the PreCompact hook.
- 15.3 Seven sections (...); rulings stores; session-start advisement; the exit bookmark.
- 15.4 L1 canon (markdown), L2 ledger (append-only events), L3 derived (status views, markers).
- 15.5 Why memory is not the same as preserved intent; the AGENTS.md-as-derived-view episode.
- 15 ref: The reference material is `docs/governance/state-doctrine.md` (ADR-0.0.9), ...
- 16.1 Window; structured state; episodic (what happened); semantic (what is known); procedural (skills).
- 16.2 RAG as memory-by-lookup; chunking, embeddings (local), similarity, reranking; when retrieval hurts.
- 16.3 Generative Agents' memory stream and reflection; MemGPT's paging; Reflexion's memory of failure; Voyager's skill library.
- 16.4 Retention, deletion, provenance, and who owns it; ...
- 16.5 The memory decision with alternatives; the personalized Final System brief follows this Evolution's Drift.
- 16 ref: This chapter draws on `.gzkit/insights/agent-insights.jsonl` (558 governed course-corrections) with `gz insights remember`, ...
- 17.1 Context isolation; independent review; parallelism; the same division of labor (plan / do / check) under every name since FIPA.
- 17.2 Implementer, spec-reviewer, quality-reviewer, narrator; traits and anti-traits; no generic expertise claims; the Why parameter.
- 17.3 HandoffResult (...); ReviewResult (...); fail-closed parsing.
- 17.4 LangGraph (or equivalent): nodes, edges, checkpoints, human-in-the-loop interrupts; the supervisor pattern.
- 17.5 Stage 1 load context → 2 implement (...) → 3 verify → 4 present evidence → 5 sync.
- 17 ref: The pipeline is specified in ADR-0.18.0 and `docs/user/concepts/subagent-pipeline.md` and implemented in `src/gzkit/roles.py` and `pipeline_dispatch.py`.

Judgment: outline ledes are topic lists by design (status: outline). No "X is Y: a, b, c" opening survives in the prose paragraphs. The chapter skeleton (Learning outcomes, Outline, Systems analyzed, Reference design, Readings, Flight card, Exercises) is shared across all ten chapters; it is a textbook convention the reader uses to find the same thing in the same place and was kept.

### Claim list (frequency or consensus statements)
- "Böckeler and the OpenAI post argue that most of an agent product is not the model." Source: attributed in the sentence.
- "These kits supply a methodology and, for the most part, no governance layer." Source: gzkit `docs/examples/comparison-gzkit-speckit-bmad.md`, listed in the chapter's readings.
- "the same division of labor (plan / do / check) under every name since FIPA" (17.1). A scope statement about the systems in the chapter's table, not a frequency claim; left.
- DESIGN CLAIM lines use "every" as a test condition, not as an observed frequency; left.

## Sentences left long
- The four "Reference design" file-list sentences (26 to 31 words): a list of files reads as one sentence; splitting it adds nothing.
- Sortie 4 FALSIFIERS and Sortie 7 DESIGN CLAIM: Jeffry's flight-card text; only the em dash preceding "DESIGN CLAIM" was edited.
- 12.5 "a brittle model fails wherever the tool contract is loose, so its brittleness makes the contract visible": 27 words including the lead-in; the "so" clause is the mechanism the original asserted without one.

## Flags for Jeffry
- "ecosystem" (13.5 heading and bullet) is on the AI-vocabulary grep; left as the standard MCP term.
- "the reviewer's claim accepted without the evidence it cites" (Sortie 8): kept as the gzkit claim/receipt sense; could become "the reviewer's verdict" if he prefers, but "verdict" already appears twice in that sentence.
- "no generic expertise claims" (17.2): kept as the gzkit persona rule's wording.
