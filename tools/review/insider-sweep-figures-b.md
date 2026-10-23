## Figures B: the-gate-holds, who-owns-the-loop, n-plus-m, rolled-back, window-budget

Edits: the-gate-holds 20, who-owns-the-loop 16, n-plus-m 13, rolled-back 12, window-budget 13 (including 3 "[verify]" tags). Five sentences or list items were deleted outright: verify-flag notes in three "What the figure leaves out" lists, "Card text ... rewrapped to fit", and the window-budget "insights corpus" note. Every "deck" reference outside the Readings lists is gone. Citations in the Readings lists ("CIDM 6333 E3 lecture deck, ...") were left as they are (rule 2). All five pages parse, and `node --check` passes on the extracted inline scripts.

Left as they are: "Completed — Partial" in rolled-back (2 places). It looks like the attestation term, so it was kept as course vocabulary. The SDK meta tags that read "verify against current docs" (who-owns-the-loop) were also kept, because they tell the student to check current docs.

Examples:
1. the-gate-holds: "Table text is the deck's. The deck's sample gate returns the shorter observation `DENIED: confirm first`, which the figure uses." -> "The E3 lecture's sample gate returns the shorter observation `DENIED: confirm first`, and the sequence above shows that form."
2. who-owns-the-loop: "The deck summarizes this ADR from its title and the book's outline, and flags its alternatives and consequences for checking against the ADR text. The stakes are low ..., which is why the deck uses it as the model." -> "The stakes are low and the reasoning is clean, which is why the E2 lecture uses it as the model."
3. n-plus-m: "The sequences are this figure's arrangement of the deck's table. The deck marks the protocol revision of the lab's Python SDK for verification; record yours ..." -> "The protocol revision of the lab's Python SDK is not confirmed; record yours on the card's SUBSTRATE line."
4. rolled-back: "The two hashes and the 0.1 s come from the deck's lab run of 09/24." -> "The two hashes and the 0.1 s come from a lab run."
5. window-budget: "... while the window is one call's input [verify on your version]." -> "... while the window is one call's input. Check this on your version."
