# Independent review of the voice pass (Oct 22, 2026)

You are reviewing, not editing. Do not change any file except your own findings file. The course is Jeffry Babb's CIDM 6333 (Agentic Systems Design and Development, West Texas A&M). Its text was co-written with AI and has just been revised by a chain of agents running three style skills: humaniser (strips AI writing patterns), ste-voice (actor, action, object; no gerund subjects; noun clusters of three at most), and scholarly-voice (plain deductive academic register after Allen S. Lee: reasons attached, terms stipulated, significance derived rather than asserted). You did not do that work. Judge it cold.

Read these first:
- `/root/.claude/skills/synced/5be94afe-931f-4e50-9eb7-2c854097b334_977856c7-71a7-4075-bc14-9b42ecb2650e/humaniser/references/shape-patterns.md` (the shape patterns #29 to #40)
- `/home/claude/site/tools/review/voice-pass/BRIEF.md` (the house rules the revisers followed)

## What to find (in this priority order)

1. **Facts added or changed by the revision.** Compare BEFORE and AFTER. Any number, date, name, attribution, causal statement, or frequency claim in AFTER that is not in BEFORE, or that BEFORE states differently. Report each with both versions. Mark it ADDED, CHANGED, or DROPPED. Dropped facts, conditions, and scope qualifiers count too.
2. **Internal contradictions.** Within a deck, the lecture paragraph and its "Cut from slide N (full wording)" section, or two slides, disagree on a number or a statement.
3. **Surviving AI shapes in AFTER** that a lexical grep misses: epigram or moral landings at paragraph end (#36), teaser closers ("The reference design met that gap in August."), reveal frames ("The lesson is...", "The point is..."), decorative metaphor carrying an argument ("hooks are the membrane"), definition-colon ledes (#35), templated sibling openings (#38), invented authority (#37: "most", "every", "usually" with no source), antithesis cadence, rule-of-three lists for rhythm.
4. **Meaning damage.** A rewrite that is now vaguer, wrong, or harder to follow than BEFORE, or a slide that lost its substance when schedule text was removed.

Do not report: em dashes inside cited titles, "Completed — Partial" (gzkit status), "typed claim"/"design claim"/a flight card's claim (course vocabulary), "names" as a noun, bracketed "[verify ...]" notes (the build drops them), or the removal of dates, times, rooms, and "tonight" (deliberate).

## Output

Write `/home/claude/site/tools/review/voice-review/<your-scope>.md`: one finding per entry, most serious first, each with: location (deck and slide, or file), category (1 to 4 above), the BEFORE text and the AFTER text quoted (short), what is wrong in one sentence, and a suggested fix in one sentence. Cap at 40 findings; if there are more, keep the most serious and give a count of the rest by category. Report back in under 200 words: counts by category and the three most serious findings quoted.
