## Lectures: speaker notes and slide wording (15 lectures)

Files: `review/voice-review/fix/<slug>.json` (notes) and `sitekit/voice/<slug>.json` (slide wording, values only). The array lengths and keys did not change. All 30 files parse as JSON, and the original serialization (indent 1, no ASCII escaping) is kept.

### Counts

- Speaker notes: 59 strings changed in 14 lectures (mini-attention-2017 needed no change).
  - 40 "Instructor checks moved off the slide:" blocks deleted, 3 of them in the published lecture paragraph (e6 #9, e8 #4, e12 #13).
  - 97 bracketed production notes deleted, counting the ones inside those blocks ("[Verify ... before class.]", "[verify]", "[Quote from genesis.md ...]", "[Summarized from the ADR's title and the book's outline ...]"). 21 of them were in lecture paragraphs.
  - 7 source trailers deleted ("gzkit facts come only from the course topic guide and carry verify markers", "gzkit items are cited from the course topic guide, and the repository is the authority where the two differ", "... must be verified against the repository", "gzkit facts come from the course topic guide only"). The sources lists and retrieval dates stay.
  - 10 references to "the deck" or "this deck" changed to "lecture" (orientation, e0, e6 x3, e7, e10, e12).
  - 4 other rewordings: e5 #4 (the "earlier version of this slide" note), e11 #7 ("instructor's mapping"), e12 #18 ("I treat both with care because the topic guide lists them..."), e7 #21 ("I have not described them beyond what the topic guide states").
- Slide wording: 9 values changed in 8 lectures. 2 bracketed notes now "" (the line is dropped), plus "(verify)", "paths from the course topic guide", "Re-check the week of class", "instructor's mapping", "orientation deck" and 2 WTClass references.

### Five examples

1. e6 notes #0: "The framing sentence of the deck is that the window is an artifact..." became "The framing sentence of the lecture is that the window is an artifact..."
2. e1 notes #9: "...all three, or the loop drifts. [Verify the quote against genesis.md.] The additions..." became "...all three, or the loop drifts. The additions..."
3. e5 notes #4: "...still a SHOULD, so the wording on the earlier version of this slide, that issuer validation became required, is true for the client side only." became "...still a SHOULD, so issuer validation is required on the client side only."
4. e11 notes #25: "...export.ts. gzkit items are cited from the course topic guide, and the repository is the authority where the two differ." became "...export.ts."
5. e9 slide: "Example model (verify)" became "Example model".

### Kept on purpose

- Reader-facing checks such as "Verify the prices on the Go page before you fly" and "Check the Python SDK version you pinned...".
- References to the Course Topic Guide that point students to a document they have ("Full mapping: the Course Topic Guide, §4.1", "Source: Appendix G of the topic guide", "The gzkit episodes are from the course topic guide, Appendix G, and chapter 18").
- "we" meaning the instructor and the class.
- Timing cues such as "[~2 min]".
- The em dash in the attestation vocabulary "Completed — Partial", which is course vocabulary.
- e6 #5 "[verify on your version]" became "; check this on your version", because this note is advice to the student.
