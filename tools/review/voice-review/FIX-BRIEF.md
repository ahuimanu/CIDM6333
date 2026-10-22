# Repair pass (Oct 22, 2026)

An independent review compared the course text before and after a voice pass and logged findings in `/home/claude/site/tools/review/voice-review/<scope>.md`. The voice pass made prose more concrete, and in doing so it sometimes invented or altered facts. Your job is to repair the findings in your scope, editing the source files listed below in place with the Edit tool.

## Rules, in priority order

1. **Never add a fact.** No new number, date, name, citation, attribution, causal claim, version, or frequency claim. If a finding says AFTER added or changed a fact, restore what BEFORE said (the finding quotes it; the full BEFORE text is in `pairs/<slug>.md` for decks, or `docs-before-387413a/` for pages). You may keep the improved sentence shape as long as the fact matches BEFORE exactly.
2. **Restore dropped facts, conditions and scope qualifiers** ("most", "nine or fewer students", "intended shape", "verify against the changelog" notes) from BEFORE. A BEFORE caution that was plain text (not in brackets) and says to verify something: restore it in square brackets, e.g. "[verify the issue numbers and dates against the changelog]", so the build hides it from the published page but keeps it in the source.
3. **Contradictions introduced by the pass:** resolve toward BEFORE. Contradictions that already existed in BEFORE: do not fix; list them in your report for Jeffry.
4. **Surviving AI shapes** (epigram closers, teaser closers, reveal frames, decorative metaphor such as "membrane", invented "most/every"): rewrite in place, in plain academic English, without adding facts. Prefer cutting a closing epigram over replacing it.
5. **Meaning damage:** restore BEFORE's meaning in the house style.
6. House rules still hold: no em dashes; "names" not as a verb (but a protocol field called `name` and phrases like "a named workflow" where "named" is technical stay); no "tonight"/dates/times/rooms. Course vocabulary stays ("typed claim", "design claim", "receipt", "verdict", "Chase", "Evolution", "Sprint", "Drift", "Completed — Partial").
7. **Rulings by Jeffry that stand** even if a finding flags them: "A new framework has arrived every year since 2022" (replaces "Frameworks change monthly"); E0's Anthropic workflow advice replacing "Most production 'agents' are workflows"; removal of WTClass/Canvas/Discord/Calendly mentions; "Retrieved Month D, YYYY" in place of "checked MM/DD/YYYY"; "Presence is not procedure". Do not revert these. If one of them now leaves a real gap (for example no deck says where to submit), list it for Jeffry instead.
8. Findings you judge wrong (the AFTER is correct and BEFORE was the error, or the reviewer misread): leave the text and list them with one line of reason.
9. Errors that exist in both BEFORE and AFTER (pre-existing): do not fix; list them.

## Files

- Deck speaker notes: `/home/claude/site/tools/review/voice-review/fix/<slug>.json` (a JSON array, one string per slide, lecture paragraph then a "Cut from slide N (full wording):" section). Keep the array length and keep valid JSON.
- Deck slide wording: `/home/claude/site/tools/sitekit/voice/<slug>.json` (edit values only, never keys).
- Textbook: `/home/claude/site/tools/sitekit/topic-guide.md` (and `readings.md`).
- Glossary: `/home/claude/site/tools/sitekit/glossary_data.py` (string literals only; must still parse).
- Figures, exercises, index pages, mini deck: the HTML under `/home/claude/site/docs/` (text only; keep tags and attributes).

## Report

Append to your scope's findings file a section "## Repair log": for each finding, FIXED / LEFT (reason) / FOR JEFFRY (the question, quoting the passage). Report back in under 200 words: counts, and every FOR JEFFRY item quoted.
