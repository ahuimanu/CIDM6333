## Scope: text sources (glossary_data.py, topic-guide.md, readings.md, docs/index.html, docs/lectures/index.html)

Counts
- glossary_data.py: 66 string edits. 53 src pointers "Course Topic Guide, X" changed to "Textbook, X"; 3 "of the Course Topic Guide" changed to "of the textbook"; 6 "the decks" attributions changed to "the lectures"; 1 "Every deck" changed to "Every lecture". Python comments left alone (string literals only). The "Course Topic Guide" glossary entry is kept, because the E0 slides use that name and the entry tells the reader it is the textbook. The file still parses (ast.parse OK).
- topic-guide.md: 1 edit. Removed "Seed list; grows with the course." from Appendix D. Line 1 heading/comment and Appendix H not touched. The rest of chapters 1-26 and appendices A-G had no insider text; gzkit source-file pointers and incident quotations kept.
- readings.md: 19 edits. 16 "[outline §x]" markers became "[§x]" ("[outline]" became "[section plan]", the public term the textbook index uses), the legend reworded to match, "The outline is stale on this point." deleted, "cite v3, which holds the taxonomy" reworded.
- docs/index.html: 6 edits; docs/lectures/index.html: 4 edits. "the deck" became "the lecture" / "the E7 lecture" / "the E8 lecture"; "written out from the speaker notes" became "written out beneath them". Both pages parse; no tags, attributes, or scripts changed.

Five examples
1. glossary src: "Course Topic Guide, Appendix D" -> "Textbook, Appendix D"
2. glossary: "The decks cite these gzkit CLI verbs: ..." -> "The lectures cite these gzkit CLI verbs: ..."
3. readings.md: "...extensions (Tasks, Skills over MCP, MCP Apps). The outline is stale on this point. Chapters 7 and 13 describe the 2025 handshake-era protocol, and the 2026-07-28 revision moved to..." -> "Chapters 7 and 13 describe the 2025 handshake-era protocol. The 2026-07-28 revision moved to..."
4. docs/index.html: "Replay the deck's worked trace" -> "Replay the E8 lecture's worked trace"
5. docs/lectures/index.html: "One lecture deck for each Evolution, with the orientation deck and two mini lectures beside them." -> "One lecture for each Evolution, with the orientation lecture and two mini lectures beside them."

Left as is (judgment calls)
- "Completed — Partial" (attestation status, glossary and Appendix D): em dash kept as gzkit vocabulary.
- Em dashes inside cited titles in readings.md kept (citations).
- Glossary src "CIDM6333_Lab_E7_Memory handout" kept as a handout name the student can find.
