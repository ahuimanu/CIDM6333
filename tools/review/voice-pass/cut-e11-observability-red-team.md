# Cut pass: e11-observability-red-team

File: /home/claude/site/tools/review/voice-pass/cut/e11-observability-red-team.json
Keys unchanged (0 to 25). First lines unchanged. JSON valid. " / " separator counts unchanged in every value.

## Counts

- 30 edits across 20 of 26 values.
- 2 schedule-only lines deleted ("- 6:00" in slide 2; "- 6:00–6:30" in slide 24).
- Em dashes: none were present (en dashes in "T0–T3" and similar ranges are not em dashes and stay).

## Dominant patterns

1. **Schedule asides (12 fragments).** Removed dates, clock times, the room, "tonight", "at six", "for the break", and the lab minute markers (0–4 to 28–30). Substantive text on the same line stays.
   - "Fri 11/13, 11:59 p.m. Your Chase commits two sealed attack cards..." → "Your Chase commits two sealed attack cards..."
   - "Wed 11/18, 11:59 p.m. Everything in." → "You commit all remaining work."
2. **Epigram and antithesis closers (9).**
   - "The card's authors tell you where their model still fails. That list is a free red-team plan for anyone building on the model." → "The card's authors list where their model still fails. A team that builds on the model can draw its red-team attacks directly from that list."
   - "Injection resistance moved down between versions; a newer model is not a safer harness." → "Injection resistance fell between versions, so a model upgrade does not by itself make the harness safer."
   - "an attacker who can make the agent print a secret wins twice if your logger then writes it to disk" → "If an attacker makes the agent print a secret and your logger then writes the output to disk, the secret persists in the trace."
3. **"names/named/name" as verbs (7).** "An attack card names one of each" → "cites one entry from each". "the named guardrail" → "the guardrail on the card". "name each outcome" → "Label each outcome". "name one place" → "identify one place".
4. **Idiom and actor removal (STE).** "Order them by what the model cannot talk its way past" → "Order them by strength: a mechanism that no model output can override ranks first." "The judgment is left to you" → "You make the judgment." The passive "can be read later by Langfuse..." became active.
5. **Semicolons in lab steps split** into one instruction per sentence.

## Kept on purpose

- "No claim enters the flight log without a trace or a receipt" and "A transcript is a claim until a span or a receipt agrees with it": these use "claim" in the gzkit sense ("a claim without a receipt"), not as a stand-in for the lecture's thesis.
- "A guardrail is a mechanism at an enforcement locus, not a sentence in a prompt": a rule definition, not a closer.
- Quoted strings ('refused by model; guardrail not exercised', 'the attack failed', 'I thought of it', 'done'), all bracketed [Verify ...] notes, and "Aug 19 changelog update" (a citation date).

## Closer list check (last sentence of each value, out of context)

0 Build: tracing, a cost table, and guardrails that survive five pre-registered attacks · 1 ...the common mistake · 2 So does any attack that is not traceable in the black box... · 3 A transcript is a claim until a span or a receipt agrees with it. · 4 Langfuse, LangSmith, or any OTLP backend can later read a JSONL file... · 5 ...the secret persists in the trace. · 6 ...shows when the provider will stop your requests. · 7 Lists: OWASP Top 10... · 8 Write one card whose delivery is a tool result, not a user turn. · 9 Order them by strength... · 10 Record it as '...', and fly a variant that reaches the guardrail. · 11 What would the deny look like? · 12 A team that builds on the model can draw its red-team attacks directly from that list. · 13 Your attacks differ, so measure your own rate. · 14 His defense: allowlists... in place of blocklists. · 15 [verify] · 16 An attack card cites one entry from each. · 17 Preservation: ask on bash. · 18 [Verify ...] · 19 [Verify ...] · 20 Attacks drawn from imagination alone test only the failures their author expected. · 21 A squawk routed to an ADR amendment · 22 Go by your Chase in the repo · 23 ...so a bash command can still read the canary. · 24 Each of you learns the other's guardrails by attacking them. · 25 Lab: one attack, one guardrail, one exported trace.

Result: no remaining "not X but Y" morals, pseudo-clefts, or reveals. Closer 3 keeps its gzkit-sense "claim". Closer 8 has "not a user turn" as a delivery condition, not a moral.

## Grep battery

Clean. The remaining "names" hits are nouns: "Span names", "Use the names", "field names", "OTel GenAI names", "GenAI names".
