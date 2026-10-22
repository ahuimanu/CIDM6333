# Cut pass: mini-attention-2017 (Oct 22, 2026)

Chain run: humaniser, ste-voice, scholarly-voice, humaniser battery (check only). 6 edits to `cut/mini-attention-2017.json`. Keys, first lines, and line/" / " structure unchanged; JSON valid. Paper quotes, figures, numbers, and the citation untouched.

## Dominant patterns

- Argumentative or cute headings (#32): "Eight heads at once, and word order written in waves" → "Eight attention heads, and word order encoded as sine and cosine waves"; "Evidence 1: better translations at a fraction of the training cost" → "Evidence 1: translation quality and training cost"; "Evidence 2: change one thing, measure against a fixed base" → "Evidence 2: one change at a time, measured against a fixed base model".
- Epigram landings (#36): "One run is an anecdote." → "A single run cannot separate a real change from run-to-run variation. For this reason, run the golden set..."; "This one did all three." folded into "...and Vaswani et al. state all three."
- "names" as a verb: "A design document names its constraint" → "states".
- Definition-colon lede: "The paper's trade: let every position look at every other position at once." → "The authors let every position attend to every other position at once. This change cuts the sequential chain from O(n) to O(1), and in exchange the compute per layer grows with n²."

## Self-audit

- Closer list: no antithesis or caption closers remain ("Only your harness runs it, after the gate." kept: it states a mechanism).
- Claim list: none ("every position", "every sub-layer" describe the architecture).
- Greps: clean.

## ste_check lines declined

Three over-25 hits and one 9-sentence paragraph are splitter artifacts (heading fragments joined across lines). The noun-cluster hit is the URL.
