# Lecture pages audit: glossary gaps, cryptic phrases, schedule leaks — 2026-10-22

Review agent; every lecture page's transcript and reader read in full against the glossary. Slide numbers are the page's numbering; W = "wording in full", N = notes, T = transcript.

## Headline finding (fixed the same day)
The reader republished what the transcript had scrubbed: every deck's "wording in full" and notes carried rooms, clock times, calendar dates, Calendly, WTClass, and instructor reminders; the orientation transcript carried contact details. `reader.py` now strips sentences and bullet segments that match a schedule/contact pattern, drops "Instructor checks moved off the slide" lines and every `[verify …]` marker, and re-scrubs the transcript.

## 1. Glossary gaps
Tier 1 (added to the glossary the same day): system card; guardrail; enforcement locus; Big Pickle / Zen / Go as an entry; Appendix G / incident casebook; trust doctrine (T0–T3) and trust-chain poisoning; MX mode; DO IT RIGHT rules; marker-file gate / presence is not procedure; canary (both uses); pre-registration / HARKing; attack card; two-stage review personas; dispatch record; deployment vocabulary (FastAPI, wheel, Docker/Podman, image digest, idempotency key, runbook); Nygard's stability patterns; uv / ruff / ty; Google ADK; spec-kit / OpenSpec / BMAD / GSD; computer use; MAST FC1–FC3; AI_LOG.md / LEDGER.md; the Course Topic Guide itself.

Tier 1 still open: run sheet; worksheet / lab handouts (the labs are not on the site); OKF, ARB, CMS, Magna Carta, airlock, foundation sunset (chapter 9.3's chain); Step 4b.

Tier 2 (partly added): gzkit ADR numbers (added under ADR); gz verbs (added); insights corpus (added); rulings store / session_orientation.py / exit bookmark; 258K exhaustion / 4,000-character budget; control-surface matrix (added); hollow antibody (added); τ-bench family (added); OpenTelemetry (added); Comment and Control / Opus 5 and GPT-5.5 cards / Apollo Research / SHADE-Arena; the six-case MCP incident casebook (Postmark, SmartLoader, Supabase, mcp-remote CVE-2025-6514, Koi Security); MCP threat mechanisms (added); OAuth plumbing (RFC 8707, 9728, 9207, DCR); MCP 2026-07-28 vocabulary (MCP Inspector, stdio, server/discover, MRTR, ttlMs, tasks extension); Böckeler / Lopopolo; Microsoft Agent Framework / Magentic-One / langgraph-supervisor / agent teams; routing and model families (added); O_EXCL lock; memory retrieval vocabulary (added); BART / DPR / FAISS / MBPP / AlfWorld / SpAIware; OWASP ASI codes (added); Context Rot / Lost in the Middle (added); harness knobs (added); ADR-1 apparatus (added); self-consistency / PaLM / Step schema / Claudishness / genesis / why.md (founding documents added); cognitive surrender etc. (added under Degradation Pattern); NIST / EU AI Act / ISO 42001 (added); JADE, Voyager, Devin, OpenHands, Aider, Jules, Zed (added); cloud agents (added); gzkit/OpenCode issue numbers; Sprint and Drift essay titles (added); Transformer details (added); orientation logistics (deliberately not added).

## 2. Still cryptic (notes assume something said elsewhere)
- E5 s1, s3, s7, s17: "last Thursday you tore down the GitHub MCP server"; "your Thursday worksheets" — an in-class lab not on the site.
- E5 s10, s12, s18; E6 s16: "our own 09/17 lab", "probe two" — the E3/E5 AGENTS.md lab is never described.
- E5 s11: "chapter nine's blind spot"; E1 s12, E3 s9, E4 s10, E0 s8, E0 s16: chapter numbers with no link (now linked via the textbook).
- E1 s10 W/T: "[Quote from genesis.md — verify…]" placeholder where the quotation should be.
- E2 s10 W/T and s11 N: bracketed summarize/verify placeholders.
- E3 s9: incident dates without a year; "GHI #844/#847" with no repository named.
- E4 s9: "the pool ADR"; "the campaign review" never introduced; W ends "Instructor checks moved off the slide:" (now stripped).
- E5–E12 closing-slide notes are raw source-URL dumps.
- E7 s14, s18; E10 s13, s17; E11 s6, s18; E12 s17: lecture-clock cross-references ("at one-thirty").
- E6 s3, s6, s12; E8 s19; E7 s21; E10 s18: instructor stage directions published as notes.
- E8 s5 T: table ends "gzkit row:" (truncated).
- E9 s4: "FC2 and FC3" before they are defined (s13).
- E9 s22: "Step 4b" defined only in passing at E8 s20.
- Or s24: "last semester's deck"; Or s29: gzkit document names with no description; E0 s5: "the framework image"; E0 s19: bare citation.
- E7 s26, E9 s24, E11 s23, E12 s23: reader wording is only the card title (full card in the transcript only).

## 3. Schedule leaks
All removed from the published pages by the scrubber. Patterns that were present: title-slide dates and rooms on every deck; the orientation calendar (s8), weekly rhythm (s10–12), office hours and contact details (s32, s34); every "Lab at six", "Consultation at five", "Go at 5:46", Sprint due dates, Calendly bookings, "Break · 0:55–1:00" slides, "checked 09/24/2026" stamps.

## 4. Errors and contradictions
1. Go/No-Go: orientation and E1–E4 say in class at 5:46; E5 on say no consultation; E9 s2 says "no consultation block this term" — two course structures. Glossary now says both, by phase; the decks still disagree.
2. Alias collisions (fixed): FC2/FC3, Go, Release, Berkeley, Wang.
3. FIPA source (fixed): fipa.org no longer hosts the specifications.
4. Claude Code hooks list (fixed): add UserPromptSubmit, Stop, SessionEnd.
5. Copilot entry (fixed): cloud agent rename, April 2026.
6. OWASP (fixed): Agentic Top 10 codes ASI01–ASI10.
7. SWE-bench (fixed): Verified and Pro.
8. E7 s11/s5/s15: a hard semester date (2026-12-15) inside the memory-record example.
9. Anthropic entry (fixed): 'Demystifying evals for AI agents'.
10. Title banners: SURVEY · BUILD · GOVERN · {DEFEND | MEASURE | FORGET | EVALUATE | FALSIFY | RED TEAM | RELEASE} vary by deck; the orientation says "four words: survey, build, govern, defend."
11. E5 s1 lecture 4:00–6:00 vs orientation's 4:00–5:00 + Drift: the format change is never explained.
12. Published placeholders (E1 s10, E2 s10) are content gaps, not just leaks.
13. Post-cutoff claims to check by the author: MCP 2026-07-28 GA details; A2A 1.0.0 date; Microsoft Agent Framework 1.0; Claude Code v2.1.277; Opus 5 / GPT-5.5 card figures; τ³-bench; OpenCode 1.18.32; Go prices.

Verified correct: ReAct foundation models; RAG 406M/21M/index-swap; Generative Agents 25 agents/score weights; Reflexion 91% vs 80%; MetaGPT 85.9/87.7; Anthropic 90.2%/15×; MAST κ 0.88/0.77; SWE-bench 2,294 / Verified 500; GAIA 466; WebArena 812 and 14.41%/78.24%; Wang 2023 66/80; Transformer 28.4 BLEU / 41.8 / 3.3e18 FLOPs / 65M.
