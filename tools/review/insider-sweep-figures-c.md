## Figures C: one-run, receipts, loop-that-halts, transformer-evidence, transformer-2017, three-drawers, skill-on-demand, pilot-and-planter, two-loops, steer-the-middle; exercises/*.html; mini-steer-the-middle lecture

51 edits in 10 files. No changes needed in skill-on-demand.html or figures/steer-the-middle.html.

- one-run-is-an-anecdote: 3 (two "the deck marks ... for verification" sentences deleted; "the deck's gate" changed to "the Sortie 10 gate", which the page already names)
- receipts-over-narrative: 10 ("deck" attributions changed to "the E11 lecture" or dropped; "instructor's mapping" reworded)
- loop-that-halts: 12 ("E1 deck" changed to "E1 lecture" in the prose, the eyebrows and 4 JS quote citations; "the build" and "rewrapped to fit" removed)
- transformer-evidence: 8 ("This page plots" changed to "The chart plots" (x2); E6/E10 "deck" changed to "lecture" (x6))
- transformer-2017: 3 (lede self-description; heading "What this redraw adds or changes" changed to "Notes on the figure", which the step text already points to; re-tint production note deleted)
- three-drawers: 3 ("made up to show the pattern" changed to "illustrative")
- pilot-and-planter: 7 (class-session dates "10/22" removed from the eyebrows, the related list and the step tags; tag changed to "Exercise", which skill-on-demand already uses; scenario dates kept)
- two-loops: 1 ("made up for teaching" changed to "illustrative")
- exercises (both): 2 ("Do not upload files to Canvas." deleted, LMS reference)
- mini-steer-the-middle: 2 ("E8 deck" changed to "E8 lecture"; "takes slides ... out of order" reworded)

Examples:
1. "The deck marks these gzkit names and dates for verification against the repository." -> deleted
2. "The OWASP column is the instructor's mapping for discussion, not OWASP's." -> "The OWASP column is a mapping for discussion, not one that OWASP publishes."
3. "Card text from the E1 deck, slide 13, rewrapped to fit." -> "Card text from the E1 lecture, slide 13."
4. "<h2>What this redraw adds or changes</h2>" -> "<h2>Notes on the figure</h2>" (and "Colors are re-tinted so the figure reads in light and dark themes." deleted)
5. "The numbers are made up to show the pattern." -> "The numbers are illustrative."

Kept on purpose: "E10 slide N" eyebrows (they tell the student where in the lecture the idea is), "redrawn" labels on the Vaswani tables (attribution), the "(Cited in the E10 lecture.)" notes, "The instructor drives at the screen" (an instruction to students), the handout date in the memory-handout citation, and the scenario dates (2026-10-22 and so on).

Checks: every edited page parses with Python's HTMLParser, and `node --check` passes on each page's inline scripts.
