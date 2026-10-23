## Figures A: memory-is-a-claim, plan-do-check, trust-boundaries, claim-receipt-verdict

Edits: memory-is-a-claim 18, plan-do-check 24 (5 of them JS sample labels), trust-boundaries 15, claim-receipt-verdict 19. Total 76.

Most edits change "the deck" to "the E5/E7/E8/E9 lecture" or "the lecture". Seven deck "verify against the repository" notes, three "[verify]" tags, and two topic-guide attributions were removed. Slide numbers stay where they help a student find the source. All four pages parse, and `node --check` passes on each extracted script.

Left as is: two JS code comments in plan-do-check that mention "the deck" (readers never see them). claim-receipt-verdict readings item "Course topic guide, chapter 18 and Appendix G (gzkit casebook)" is unchanged because removing "topic guide" would leave the entry with no title. The author should decide whether it should cite the textbook.

Examples (before / after):

1. memory-is-a-claim, gzkit row: "(558 governed course-corrections, per the topic guide) ... The deck marks the count and syntax "verify against the repository."" / "(558 governed course-corrections) ..." (verify note deleted)
2. memory-is-a-claim, stale-fact panel: "Turn on the deck's three fixes one at a time. The record ids, dates, and the unittest command line are constructed for the demo." / "Turn on the three fixes one at a time. The record ids, dates, and the unittest command line are illustrative."
3. plan-do-check, reference panel: "The deck's sources: ... The deck marks the ADR number, stage names, and paths "verify against the repository before class."" / "Sources: ..." (verify note deleted)
4. trust-boundaries, teardown table: "Not documented [verify]" / "Not documented"
5. claim-receipt-verdict, chain panel: "The deck does not quote the chain's text, so the summaries here are illustrative, built on the deck's worked receipt (3 tests run, 1 failure)." / "The summaries here are illustrative, built on the lecture's worked receipt (3 tests run, 1 failure)."
