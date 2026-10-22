# Figures QA — 2026-10-22

Review agent; all 19 figures loaded light and dark at 1400×900, stepped to the end, every control exercised, SVG geometry scanned, links checked. No JavaScript errors in any figure. All step counts match; dark mode renders correctly; no HTML overflow at 1400px. Cross-figure links resolve; five external links (opencode.ai ×3, arxiv ×2) could not be fetched from the review sandbox. Trust-boundaries' pinned hash recomputes correctly; the panels' arithmetic was spot-checked and is consistent.

## Visual defects to fix (real)
1. **one-run-is-an-anecdote**: in the dot plot at N = 1 the label "no interval with N = 1" runs past the SVG's right edge.
2. **plan-do-check**: in "Reviewer can edit" mode, "fail · round n of 3" and "writes the fix" overprint; "FAIL + findings" touches the spec-review box.
3. **three-drawers**: steps 3–4, the "+ pasted procedure" chip covers the AGENTS.md line "the model reads it; nothing makes it obey".
4. **who-owns-the-loop**: panel 4, the CONTROL line and "synthesize" overrun their boxes.
5. **window-budget**: "TURN_BUDGET RECORD (ILLUSTRATIVE)" cut off; "appended, never edited" wraps below the L2 LEDGER box; "You and the model" overruns; the small-print line nearly collides with a header.
6. **loop-that-halts**: step 9 overlay drawn over the dimmed halt-check text, which reads through.

Cosmetic: memory-is-a-claim "question" arrow label; n-plus-m slider readout wrap; pilot-and-planter mono path into the box border; receipts-over-narrative ghosted labels in "said" view; steer-the-middle ring crowding; transformer-evidence "One change per row" overrun and ~8.7px tick labels; trust-boundaries Part B vertical label under the gate marker.

## Missing links
The figures' "in your sortie" and "map" sections name lectures, figures, and glossary terms as text only. No figure links to a lecture, an exercise, or the glossary. (To do: names panel or inline links, as on the lecture pages.)

## Factual claims extracted for the fact-checker
Every number, date, name, and vendor behavior in the captions and panels, by figure, is listed in the review transcript; the ones the pages themselves flag `[verify]` go first: the Codex hook count, the 258K startup-context figure, ADR paths and numbers, the vendor SDK ownership rows, description pinning in Claude Code/Codex, OpenCode issue #30649; then the MAST v3 percentages and every 2026-dated vendor claim (MCP 2026-07-28 revision contents, OpenAI Feb 23 2026, Cursor Jun 25 2026 and Jan 2026, Berkeley Apr 8 2026, OpenCode Go prices checked 09/24/2026).

Key claims by figure (abridged):
- claim-receipt-verdict: MAST 1,642 traces, 7 frameworks, 3 categories / 14 modes, FC1 44.2% / FC2 32.4% / FC3 23.5%, κ 0.88 human / 0.77 LLM; gzkit ten-deep chain 2026-05-24; Go prices and limits; RouteLLM 85% cost at 95% quality; FrugalGPT up to 98% lower cost; Anthropic research system 15× tokens, 80% variance, 90.2%.
- loop-that-halts: ReAct finish as the only halt; AutoGPT/BabyAGI spring 2023; simulator prices illustrative.
- memory-is-a-claim: recall.py k=2, threshold 0.05; deck run scores; OWASP ASI06; MemGPT / rule / Generative Agents eviction.
- n-plus-m: MCP timeline Nov 2024 → Jul 2026 and the 2026-07-28 deprecations; SDK list; gzkit storage-tiers quote.
- one-run-is-an-anecdote: τ-bench GPT-4o results; DeMillo 1978; Nosek 2018; Kerr 1998; Wang 2023 66/80; Zheng 2023 >80% agreement; SWE-bench Verified audit 59.4% of 138 (OpenAI Feb 23 2026); Cursor 87.1→73.0, 731 trajectories, 57%/9% (Jun 25 2026); SWE-bench Pro 1,865 tasks / 41 repos; Berkeley eight benchmarks.
- plan-do-check: E8 trace; parser; reviewer.md (uses `bash`; docs say `shell`).
- receipts-over-narrative: OTel GenAI attribute names; OWASP mappings.
- rolled-back: Nygard patterns; uv commands; Claude Code routines quotes.
- skill-on-demand: OpenCode skill directories, name/description rules.
- the-gate-holds: gzkit 17/2/1 hooks; 08-21 and 08-23 incidents; GHI #844/#847.
- transformer-2017 / transformer-evidence: all values against Vaswani et al. 2017 (Tables 1–4, §5–6).
- trust-boundaries: MCP 2026-07-28 authorization details (RFC 9728, 9207, CIMD, DCR deprecated); Codex sandbox modes; Claude Code PreToolUse exit 2; OpenCode last-match-wins.
- two-loops: cost ~ square of prompt length; prompt caching.
- who-owns-the-loop: framework owner matrix "as of early 2026, flagged to verify".
- window-budget: Claude Code /compact behavior (reloads system prompt, tool definitions, CLAUDE.md, up to five files; skill bodies ≤5,000 tokens); Cursor 46.9% fewer tokens (Jan 2026); OpenAI AGENTS.md ~100 lines (Feb 2026); OpenCode #30649.
