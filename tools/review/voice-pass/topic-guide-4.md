# Voice pass log: topic-guide-4 (Oct 22, 2026)

File: `/home/claude/site/tools/review/voice-pass/tg/chunk4.md` (Appendix F, Toolkit Setup; Appendix G, gzkit Incident Casebook; Appendix H, run sheet).
Original kept at `/tmp/claude-0/-home-claude/acdec67e-a228-569c-b4b7-fc7975fc3d39/scratchpad/chunk4.orig.md` for this session.

Scope: Appendix F and Appendix G only. Appendix H is unpublished schedule material and is byte-identical to the original (verified by diff from its `# ` heading to end of file). The three `# ` heading lines are byte-identical. The bash code fence, every inline code span, every table row count, every link and every number are unchanged (verified by diff of the sorted code-span list and of line-type counts).

## Changes by pattern

### Em dashes outside `# ` headings (house ban)
- `## Route A — subscription + small API budget` → `## Route A: a subscription plus a small API budget`
- `## Route B — local only` → `## Route B: local only`
- G row 2026-05-10: `the TTY gate removed (05-14) — authority belongs to the human, forgery-resistance to audit` → `the TTY gate was removed (05-14), on the reasoning that authority belongs to the human and forgery-resistance to audit`
- G row 2026-06-16: `playback store — none existed as attested` → `playback store; none existed as attested`

### "names/named" ban
- G row 2026-05-30: `V.I.B.E.S. named` → `V.I.B.E.S. coined`

### Procedure register in Appendix F (ste-voice: imperative verb, one instruction per sentence, condition before instruction, no semicolons)
- Route A and B bullets were noun fragments (a parts list). Each is now an instruction: `Claude Pro / ChatGPT Plus / Google AI Pro (~$20/mo) and its harness: ...` → `Subscribe to Claude Pro, ChatGPT Plus, or Google AI Pro (~$20/mo). Use the harness that comes with it: ...`; `~$20–40 of API credit for SDK and MCP work.` → `Set aside ~$20–40 of API credit for the SDK and MCP work.`; `Ollama + OpenCode (...)` → `Install Ollama and OpenCode (...)`.
- Every numbered item that chained clauses with semicolons was split into one-instruction sentences. Example, item 2: `declares readme = "README.md"; create it or Gate 2 fails with "Readme file does not exist."` → `declares readme = "README.md". If that file does not exist, Gate 2 fails with "Readme file does not exist." Create the file first.` (condition before instruction). Item 8: `with one vendor you run in degraded mode and say so` → `If you have only one vendor, run in degraded mode and say so.` Item 9: `budget accordingly, and prefer --no-subagents for small sorties` → `Budget for that. For a small sortie, prefer --no-subagents.`
- Item 5 lost its label-colon opener (`Briefs: after any edit run ...` → `After any edit to a brief, run ...`).
- Item 6: `refuses src//tests/ edits without an active pipeline` → `refuses edits to src/ and tests/ when no pipeline is active`; `Do not work around hooks` → `Do not work around either hook`.
- Heading: `Known gotchas against py-gzkit 0.34.x` → `Known problems in py-gzkit 0.34.x` (label; colloquialism dropped).

### Appendix G: actor removal (#3, #5, #31) and gerund or participle subjects (STE rules 2, 3)
- Intro was a verbless fragment plus a `Sources:` label (definition-colon shape, #35): now two full sentences (`This appendix lists the dated episodes from the reference design and, for each, the mechanism that resulted. The sources are ...`).
- `nine silent-wrong layers feeding decisions` → `nine silent-wrong layers fed decisions`
- `Stale clone 10 commits behind; ~215 lines discarded by hard reset` → `A stale clone sat 10 commits behind; a hard reset discarded ~215 lines`
- `Four questions bundled in one prompt` → `The agent bundled four questions in one prompt`
- `Agent piped` / `Agent re-elicited` → `The agent piped` / `The agent re-elicited` (STE rule 7, keep the article)
- `Gate-5 attributed to the operator that was never given` → `A Gate-5 was attributed to the operator, who never gave it` (the dangling `that` had attached to `operator`)
- `Registering one CLI verb produced 21 failures` → `One CLI verb, when registered, produced 21 failures`
- `Six governance hooks keyed on editor-tool matchers were bypassed by any Bash write` → `Any Bash write bypassed six governance hooks keyed on editor-tool matchers`
- `scaffolders emitted ids their own validator rejected` → `the scaffolders emitted ids that their own validator rejected`
- `Pipeline gate checked` → `The pipeline gate checked`
- Quoted ledger and doctrine text (`"Count what we CLOSE, not what we book"`, `"a subagent's claim is not evidence"`, `"Permitted to say enough"`, `"A value in Markdown is illustrative, never authoritative"`, `"A presence check answers ..."`, `"A settled question is a drift vector"`, `"Utter shambles"`, `"The antibody"`, `"facts"`) is untouched.

Edit count: 2 Edit calls covering 10 lines in Appendix F and 15 lines in Appendix G (25 lines changed in all).

## Grep battery after the final pass (Appendix F and G text)
- intensifiers, AI vocabulary, summary shapes, hedge stacks, "not X, but Y" cadence: no hits.
- em dash: hits only on the two `# ` heading lines, which are required to stay byte-for-byte.
- names/named/naming: no hits.
- "claim": two hits, both kept: `"a subagent's claim is not evidence"` (quoted gzkit text) and `enforcement-claim rule` (the name of a gzkit rule).
- "the move": no hits.

## Self-audit artifacts (final pass)

Closer list (last sentence of every prose paragraph and list item, out of context):
- F Route A: `Add GitHub Copilot (Student plan) as a free supplement.`
- F Route B: `Use an SDK that speaks OpenAI-compatible endpoints (Pydantic AI, LangGraph, or the OpenAI SDK pointed at Ollama).`
- F items 1 to 9: `Do not hand-edit a generated file.` / `Create the file first.` / `The artifacts land in design/, not in docs/design/.` / `Run uv add --dev ty.` / `For product proof, Allowed Paths must cover src/ and tests/.` / `Do not work around either hook.` / `In a non-TTY context, use gz closeout <ADR> --ceremony --attest or gz attest.` / `If you have only one vendor, run in degraded mode and say so.` / `For a small sortie, prefer --no-subagents.`
- G intro: `The sources are AGENTS.md § Operator Doctrine, CHANGELOG.md, RELEASE_NOTES.md, .gzkit/insights/agent-insights.jsonl, and the ledger.`
Verdict: every closer is an instruction or a fact. None works as a caption or moral (#36 pass). Item 3's `not in docs/design/` is a factual path contrast, not an antithesis cadence.

Lede list (first sentence of each section):
- Everyone: (code block only)
- Route A: `Subscribe to Claude Pro, ChatGPT Plus, or Google AI Pro (~$20/mo).`
- Route B: `Install Ollama and OpenCode (or another provider-agnostic harness).`
- Known problems: `gz init writes ~520 files (...).`
- Appendix G: `This appendix lists the dated episodes from the reference design and, for each, the mechanism that resulted.`
Verdict: no "X is Y: a, b, c" opening (#35 pass). Route A and Route B share an imperative opening because both are install lists (#38: shared structure where the reader looks for the same thing in the same place).

Claim list (frequency or consensus claims): none. `Several skills are model: opus` and `~520 files` are counts taken from the source, not frequency claims (#37 pass).

Sibling diff: not applicable within this chunk (Appendix F and G do not share a purpose).

## ste_check lines declined, with reasons
Run on plain text extracted from F and G (code fence dropped, table pipes turned into sentence breaks).
- `[34] If that file does not exist, Gate 2 fails with "Readme file does not exist." Create the file first.` flagged over 25 words: checker merged two sentences across the quoted period. Each sentence is under 20 words. Declined.
- `[27] First outside adopter: gz init left no runnable project, and the scaffolders emitted ids that their own validator rejected`: 19 words of prose plus backtick tokens; one table cell carrying the two facts of one episode. Declined.
- paragraphs over 6 sentences (the numbered list, the table): structure, not prose paragraphs. Declined.
- gerund/nominalized subjects `First repudiation`, `One authority for new-verb obligations`: these are the mechanism labels in the "What resulted" column, taken from gzkit. Declined.
- passives with no actor: `the TTY gate was removed`, `Green main was reopened`, `A Gate-5 was attributed`, `Four briefs were attested`. The source table does not say who removed, reopened, attributed or attested, and the brief forbids adding content, so no actor was invented. Declined.
- noun clusters of 4+: all are code spans, file names or proper names (`gz obpi complete --attestor`, `.gzkit/insights/agent-insights.jsonl`, `SessionStart ahead/behind`). Declined.
- semicolons: 20, all in Appendix G table cells, where they separate two results of one episode. Appendix F procedure text has none. Kept because the table is case material, not a step table.

## Sentences left long
- G row 2026-05-10 result cell (`Regression test; then the TTY gate was removed (05-14), on the reasoning that authority belongs to the human and forgery-resistance to audit`): 24 words. It carries the date and the two-part reason the source gave for removing the gate; splitting would lose the dependency between the removal and the reason.

## Open points for Jeffry
- `(verified 2026-08-24)` in the Known problems heading was kept. It reads like a QA aside, but it states which release the list was tested against, which is a scope qualifier the reader needs. Remove it if it is a management note.
- `V.I.B.E.S. named` became `V.I.B.E.S. coined` to clear the "names" ban. If the ledger entry uses "named", the quoted wording should come back in quotation marks.
