# Cut-section pass: e5-mcp-2-security-harness (Oct 22, 2026)

File: cut/e5-mcp-2-security-harness.json. 49 edits across 24 of 27 values. Keys and first lines unchanged; JSON valid. One whole schedule line deleted (slide 2, "- 6:00"), as CUT-BRIEF allows; all other line counts and " / " separator counts unchanged. The file carried no em dashes before the pass.

## Counts
- "names/named" as verb or modifier: 6 (WWW-Authenticate "carries"; description "mentions" x2; "The file states"; "adversarial client (identified)" x2; "A NO-GO states").
- "the claim" thesis stand-ins: 4 ("OpenAI's claim." -> "OpenAI argues that"; "The claim was never flown." -> "The design claim was never flown."; FAIL/ABORT line -> "design claim" x2; "not the claim" in slide 6 rewritten).
- Schedule removed: dates (Thu 10/01, Sun 10/04, Mon 10/05 x2, Wed 10/07 x2, Thu 10/08, 09/24/2026 check date), times and room (4:00–6:00, CC209, 6:00–6:30, lab minute marks 0–4 ... 27–30), "tonight" x3, "Thursday" x3, "While you stretch", "Lab at six". "09/17 file/lab" (a lab identified by date) -> "E3 lab file" x5; E4 = Thu 09/24 in e4-mcp-1, so 09/17 is E3.
- "we": 1 removed ("we fill it together").

## Dominant patterns
1. Epigram and mirrored-pair closers (#36).
   - "Fine on your laptop; wrong the moment the host is elsewhere." -> "That arrangement suits a server on your laptop. It fails once the server runs on a machine you do not control."
   - "Tool-description pinning defends against a server that lies to the model. It does nothing against a server that is honest to the model and lies to you." -> "Tool-description pinning detects a server that changes what it tells the model. A server whose descriptions stay honest while its code acts against you passes the pin check."
   - "One canon, many renditions: generate them, and the generator is a control surface." -> "Generate the renditions from one canon, and treat the generator as a control surface."
   - "You need both." folded into the prior sentence with its reason.
2. "not X; it is Y" and "X, not Y" cadence.
   - "AGENTS.md is not authored; it is rendered from the corpus" -> "gzkit renders AGENTS.md from the corpus"
   - "The measure is what the harness loads at startup, not the file's length." -> "The measurement counts what the harness loads at startup, imported doctrine included, and the file's own length leaves that out."
   - "'Never push to main' belongs in a deny rule, not in prose." -> "Put 'Never push to main' in a deny rule."
3. Word echo: "drift between mirrors is drift in what the agents believe" -> "a difference between two renditions becomes a difference in what the agents believe" (still parallel; the logic is symmetric).

## Closer list check
Run on every value line out of context. Remaining closers carry facts or instructions. Kept: "A malicious server changes an honest one's behavior." (states the shadowing mechanism), "The May 2025 trace is the confused deputy." (identifies the case).

## Claim list
- "Every harness is the same." (invented authority) -> "The instruction files of the other harnesses are context in the same sense." Still unsourced; flagged for the instructor.
- "Each mistake appeared in a Sortie 4 log or a worksheet" keeps its provenance (course artifacts).
- "60,000+ open-source projects", "150+ organizations by Apr 2026": numbers, not edited.

## Unsure / left
- Slide 1: "harness engineering in 2026: the product is the harness" left as written; it reads as a slogan, but it is a topic line and may echo a source.
- Slide 24 flight card: "SPRINT (due Wed 10/07)" replaced by "SPRINT" padded with spaces to keep the fixed-width column.
- Lab steps (slide 25): minute marks removed; step text kept, plus "One normal read" -> "Make one normal read".

## ste_check declined
Length and paragraph flags come from joined slide lines and the fixed-width flight card. Passives such as "is deprecated", "is scoped", "is logged" carry the actor (spec, host, server) in the same line. Semicolon lists in the OAuth step table and the GitHub teardown cells are labelled fragments in slide register and were kept.
