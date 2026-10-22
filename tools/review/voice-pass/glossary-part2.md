# Voice pass log: glossary-part2

File: `/home/claude/site/tools/review/voice-pass/glossary-parts/part2.py` (50 `g(...)` entries, Handoff through Nygard). Only the `what`, `when`, `why` string literals were edited; `term`, `cat`, `src`, `aliases`, `ch` were checked by AST against the original (copy kept at the scratchpad `part2.orig.py`) and are byte-identical on all 50 entries. Every line still parses as a Python expression. 107 string fields changed across the 50 entries (every entry touched).

## What changed, by pattern

### Definition-colon ledes (#35) and parts-list fragments

Almost every `what` opened "Term: a, b, and c." or as a verbless fragment ("A benchmark of...", "Maker of..."). Each now opens with a full sentence whose subject is the term, with the specification in the sentence that follows.

- Before: `Model Context Protocol: a client–server protocol over JSON-RPC in which a host (the harness) connects clients to servers that expose three primitives, tools, resources, and prompts, with negotiated capabilities. One server serves every client: N×M integrations become N+M.`
  After: `The Model Context Protocol is a client–server protocol over JSON-RPC. A host (the harness) connects clients to servers, and each server exposes three primitives, tools, resources, and prompts, under capabilities the two sides negotiate. Because one server serves every client, N×M integrations become N+M.`
- Before: `Maker of GPT models, ChatGPT, function calling (June 2023), the Agents SDK, and Codex.`
  After: `OpenAI makes the GPT models, ChatGPT, function calling (June 2023), the Agents SDK, and Codex.`
- Before (why): `E3: tools as contracts. Figure 04 plays one call through...`
  After: `E3 treats tools as contracts, and Figure 04 plays one call through model, harness, gate, human, tool, and ledger.`

### Epigram landings (#36)

Caption-shaped closers were either folded into a sentence with the mechanism or dropped when the `why` already carried the point.

- `Autonomy without a halt condition: it looped, spent, and rarely finished.` → `It had autonomy without a halt condition, so it looped, spent, and rarely finished.`
- `Roles as configuration.` (AutoGen) → dropped from `what`; the `why` now reads `It is in E8's survey as the framework in which roles are configuration rather than prompts.`
- `Memory as a claim about what went wrong.` (Reflexion) → `In the course's terms, each stored reflection is a claim about what went wrong.`
- `The first plan-do-check with typed messages.` → `It is the first plan-do-check protocol with typed messages.`
- `...the gap between them is where accidents live.` → `...accidents occur in the gap between the two.`

### Invented authority (#37)

- Handoff `why`: `the weakest of the memory strategies in Figure 14's table, and the most common.` The "most common" had no source in the decks or the Figure 14 page, so it was cut. The replacement attaches the reason the table gives: `Figure 14's table lists it as the weakest of the memory strategies, because nothing in the loop reads it unless the next session is told to.`

### "named" ban

- RAG: `The 2020 paper named the pattern` → `The 2020 paper gave the pattern its name.`
- MT-Bench: `The paper that named LLM-as-a-judge` → `The paper gave LLM-as-a-judge its name and measured three of its biases`.

### Pseudo-cleft

- JSON Schema `why`: `A closed status enum in the schema is what makes a result parse fail-closed.` → `A closed status enum in the schema makes a result parse fail-closed, because a status outside the enum fails validation instead of passing through.`

### Empty `why` fields filled (brief: each entry states why it is in the course)

Fourteen entries had an empty `why` with the course reason buried in `what` or absent. Where the reason was in `what`, it moved to `why` (OWASP, OpenAPI, RAG, Ollama, Langfuse, Anthropic, OpenAI, Invariant Labs, Linux Foundation, BLEU, Berkeley exploits, Transformer, Degani and Wiener). Where it was absent, the `why` states only what the `ch` field and the neighbouring entries already support (HumanEval, GAIA, WebArena, ToolBench as four of E10's five benchmarks; CrewAI in Chapter 17's survey; BabyAGI beside AutoGPT in Chapter 6; JSON-RPC as the E4 server's message format; AutoGen in E8's survey).

### Empty `when` fields filled where the `what` already carried the maker and date

AP2 (`Google, September 2025.`), BabyAGI (`Yohei Nakajima, March 2023.`), Pydantic AI (`The Pydantic team, 2024 onward.`), Memory layer (`Students build it in E7's lab.`).

### STE pass (rules 1 to 4, explanatory register)

- Passives with no actor: `The handoff is built in E6` → `Students build the handoff in E6`; `The model was trained with Adam... and its results are reported` → `The authors trained the model with Adam... and they report its results`.
- Noun cluster: `gives your own agent tools` → `gives tools to your own agent`.
- Semicolons in drafted prose: one (`Founded in 1996; part of the IEEE from 2005.`) → `FIPA was founded in 1996 and has been part of the IEEE since 2005.` The remaining ten semicolons are all inside citation strings in `when` and were not touched.
- Semicolon-chained clauses in `what`/`why` were split into sentences throughout (A2A `when`, SWE-bench, OAuth, Tool).

### Scholarly-voice pass

Reasons attached in the same sentence ("because", "so") where a `why` previously stood as a label; "argues that" used for a lecture's thesis (`E2 argues that every framework is a theory of who owns the loop`); parentheses kept for the second track (examples, codes, dates).

## Course vocabulary kept verbatim

`memory is a claim with a date, and the loop does not open the drawer by itself` (Figure 14, steer-the-middle); `message type as claim type` (E8), rephrased only to a full sentence (`a message type is a claim type`); `'under every name'`; `'receipts over narrative'`; `'presence is not procedure'`; `'data, not instructions'`; `'tool poisoning'`; `'mandates'`; `'Smallville'`; `'autonomous agent'`; `'Mind'`; all paper and post titles; every citation, URL, number, and date.

## Self-audit artifacts (after the final pass)

### Closer list (last sentence of each `what`, and of each `why`)

All 50 `what` closers and 50 `why` closers were listed out of context. None is an antithesis, a moral, or a slogan. Two were examined: `It is the first plan-do-check protocol with typed messages.` (a dated factual claim, kept) and `The questions are easy for humans and hard for agents.` (GAIA's own framing of its benchmark, kept). `Roles in AutoGen are configuration.` was the one caption-shaped closer and was removed.

### Lede list (first sentence of each `what`)

Every lede is "Term is/was/stands for/makes/lets ..." or an attributed "argues that". No "X is Y: a, b, c" opening remains. The repeated "X is a ..." shape is the glossary form the brief asks for (a definition per entry), not a templated sibling page.

### Claim list (frequency and consensus claims)

- `a ledger records every add, recall, and evict` (design fact of recall.py, from the E7 handout)
- `one server serves every client` (MCP's N+M argument, from the spec)
- `every message the E4 server sends or receives is in this format` (follows from MCP being JSON-RPC 2.0)
- `requires every message to carry a performative` (FIPA-ACL specification)
- `Every memory layer in the course is a RAG loop over its own records` (course design statement, carried over from the original)
- `E2 argues that every framework is a theory of who owns the loop` (attributed to the E2 deck, which carries that sentence)
- `Every model the course's harnesses call descends from it` (Transformer lineage, carried over from the original)
- Cut: `and the most common` (Handoff), no source.

### Sibling diff

The five E10 benchmark entries (SWE-bench, HumanEval, GAIA, WebArena, ToolBench) share one `why` move (membership in E10's set of five), worded differently in each. Shared because the fact is shared; flagged here so a reader can decide whether four of them should say more.

## ste_check lines declined

- Sentences over 25 words (12): the brief exempts explanatory paragraphs from the ceiling. Each long sentence carries a list of items or a paper title (Anthropic's six posts; the Transformer's components; Degani and Wiener's title; A2A's version history; SWE-bench's 2,294 issues and conditions; CrewAI's role/goal/backstory plus process modes). Splitting would drop a fact or a qualifier.
- Paragraphs over six sentences (2): A2A and Transformer. The checker read `what` + `when` + `why` as one paragraph; on the page they render as three labelled fields.
- Gerund/nominalized subjects (3): `The harness`, `Function calling`, `Tool argument schemas` are proper terms, not nominalizations.
- Passives (remaining): `It records what was done` (the content of the handoff, actor unknown by design); `It is built on signed 'mandates'` and `is built on it` (a protocol and a testbed, the builder is in the `when`); `A2A was donated to the Linux Foundation` (actor named in the A2A entry); `agents are organized into crews` (CrewAI's own framing).
- Noun clusters of 4+ (14): all heuristic hits on comma lists (`model, harness, gate, human, tool`), post titles, or bias lists; none is a real noun stack.

## Open points for the caller

- Handoff `why`: the mechanism sentence (`because nothing in the loop reads it unless the next session is told to`) is derived from Figure 14's "the loop does not open the drawer by itself"; confirm it matches what Figure 14's table says about handoffs.
- AutoGen `why`: `roles are configuration rather than prompts` adds the contrast with CAMEL (`roles assigned by prompt alone`); the original said only `Roles as configuration.`
- BabyAGI `why` (`Chapter 6 reads it beside AutoGPT as the 2023 loop in its smallest form`) and CrewAI `why` (`It is in Chapter 17's survey of coordination frameworks`) are inferred from the `ch` fields, not from a deck sentence.
