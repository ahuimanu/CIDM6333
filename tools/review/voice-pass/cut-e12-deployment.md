# Cut pass log: e12-deployment (Oct 22, 2026)

File: /home/claude/site/tools/review/voice-pass/cut/e12-deployment.json
Edits: 33 Edit calls touching 20 of 25 values. Keys and first lines unchanged; JSON valid; " / " counts unchanged in every value. Two whole schedule-only lines deleted (key 24 "- 6:00–6:30"; key 25 "- The E12 Sprint closes on Monday, not Wednesday, because the ceremonies start Tuesday.").

## Dominant patterns

1. Schedule asides (keys 0, 12, 22, 23, 24, 25, 26): dates, clock times, CC209, Calendly, "tonight", "last week", lab minute offsets removed; substantive content kept.
   - "Lab tonight (6:00–6:30): release, break, roll back" -> "Lab: release, break, roll back"
   - "Card signed by Friday, code frozen Monday, ceremony booked tonight." -> "Get the flight card signed, freeze the code, and book the ceremony."
2. Antithesis / mirrored closers (keys 2, 3, 6, 7, 9, 10, 14, 15, 18, 19):
   - "A version number is a name. The hash is the release." -> "A version number is a label that a later build can reuse; the hash identifies the release."
   - "Attribution answers who asked; it does not answer who checked." -> "The attribution records who asked for the work. Only the PR review records who checked it."
   - "The release is a thing, not a moment." -> "The release is a built artifact (a wheel or an image) that carries a version and a hash."
3. "names" as a verb (keys 2, 9, 18, 21, plus "must be named" in 14): -> "records" / "state" / "called".
4. Definition-colon epigram and actorless judgments (keys 3, 7, 18): "A backfilled release is an admission: ..." -> "A backfilled release shows that ..."; "A retried POST must not run the agent twice: idempotency key" -> "An idempotency key keeps a retried POST from running the agent twice".
5. Frequency claims removed: "Most course systems are jobs..." -> "A course system can be a job..."; "Small and free models will name failure cases" -> "can invent failure cases".

## Kept on purpose
- "Completed — Partial" (gzkit status, the only em dash left).
- Quoted routine-docs text, "'loose in the bay, hard at the door.'", "'Count what we CLOSE, not what we book.'", V.I.B.E.S. expansion, all bracketed [Verify ...] notes (including "before class" inside them).
- "the model's claim", "Test its claim", "Run each claim" (the model's assertion, not a thesis stand-in).
- "(names only)" in key 11 (noun).
- "30–40 minutes" in key 23 (ceremony length, a fact, not a clock time).
- Remaining "every" hits are universal rules (every request, every gate, every copy), not frequency claims.

## Battery result (final)
Em dash: only "Completed — Partial". names/named/naming verb: none. Intensifier and AI-vocabulary greps: none. not-X-but-Y grep: none. Schedule grep (clock times, dates, tonight/this week/last week, Calendly, CC209): none outside bracketed notes and "since 04/2026" (a fact date).

## Closer list check
Last sentences of each line read in isolation: no shared cadence, no aphorism landings left. Closers now carry a mechanism (who records, who checks, which command refuses) instead of a moral.
