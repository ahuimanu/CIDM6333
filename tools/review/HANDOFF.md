# CIDM 6333 site: handoff (October 22, 2026)

Live: https://ahuimanu.github.io/CIDM6333/ · repo ahuimanu/CIDM6333 (master, last push d5f69e6) · local clone ~/Documents/Courses/CIDM6333

## State

- Voice chain (humaniser, STE, scholarly-voice, humaniser check) run over all course text: decks (slide wording via `tools/sitekit/voice/<slug>.json`), speaker notes (`tools/sitekit/notes.json`), textbook (`topic-guide.md`, `readings.md`), glossary (`glossary_data.py`), figures, exercises, index pages.
- Independent review found 289 findings (about half were facts the pass had added, changed or dropped). Repair pass restored them to the pre-pass wording. Logs: `tools/review/voice-review/<scope>.md` (findings + "Repair log").
- WT brand colours and fonts (no logo, by ruling): `tools/sitekit/brand.py`.
- Course-administration specifics removed so the materials stay reusable (LMS, submission mechanics, late policy, office hours, Calendly, Discord, rooms, phone, dates, times).
- Build order: `textbook.py → voice_apply.py → reader.py → deck.py docs <web-native slug> → glossary.py → nav.py → brand.py` (from `tools/sitekit`, docs = `../../docs`).
- Push: device-code login (client id 178c6fc778ccc68e1d6a, scope repo) → token at /tmp/gh_tok in the Mac VM; push from the clone with `http.extraheader`.

## Standing rules from this session

- Every style pass carries "never add a fact" and is diffed against the pre-pass text before publishing.
- No course-administration specifics anywhere (enduring, reusable materials).
- Sortie environment: OpenCode and Big Pickle only. No local token issuer, no local OAuth server.

## Next task: convert ALL remaining decks to web-native

Only E8 is web-native. Convert the other 14 (orientation, E0–E7, E9–E12, mini-attention-2017) with `deck.py` (each needs a DECK_META entry; slide wording already lives in `voice/<slug>.json`). After conversion the slide images (which still show pre-pass wording) are no longer the source of what students read.

## Small tasks (no ruling needed)

- E5: remove every mention of a local token issuer / local OAuth server (slides 5 and 24 and notes); replacement waits on question 1.
- Check the E0 paraphrase of Anthropic's "Building Effective Agents" ("use a workflow wherever the path is known in advance, and the open loop only where it is not") against the post.
- Check E8 "Nesting. Three levels deep by default" against the current sub-agents docs.
- Glossary chapter references: JADE/Voyager entry `ch=(7, 8)` (should be 4 and 6), HumanEval, ToolBench.

## Questions for Jeffry (one at a time)

Resolved Oct 22: Raji/Groves citation; E2 workflows line; E10 five rules; E8 falsifier one; E8 BrowseComp; E1 Kojima; submission/LMS references dropped.

1. Sortie 5 authorization with OpenCode and Big Pickle only: stdio with no authorization, or a static bearer token the server checks?
2. E5 slide 1: "In Evolution 3 you put a tool on the wire; in Evolution 4 you tore down the GitHub MCP server". Is E3 right?
3. E0 slide 5: "'done' is the most dangerous word in the course." Add a reason after it, or leave it bare?
4. E0 and E1 slide 2 list minutes per part. Remove them as times?
5. E1 slide 10 says governance arrived "not as a wrapper"; orientation slide 18 says gzkit "wraps them". Which wording?
6. E2 Flight Card: a missing predicted consequence is a FAIL, but the exceptional lens rewards "the predicted consequence did not appear, and the ADR was amended with the evidence". Is an amended miss a FAIL that still earns top marks?
7. E3: slide 5 code accepts a confirm event for every non-read class; slide 4 card says "irreversible: … requires an attestation". Which changes?
8. E4 close: "A protocol is a contract that strangers can discover; that is what it adds", while slide 3 lists three promises. Reword?
9. "membrane" on the E3 and E2 slides ("the membrane a harness puts around every tool", "Hooks as a membrane"). Keep it?
10. E9 slide 3: "you will know before you fly whether your adversary is a real one". The planted falsehood is tested during the sortie. Change "before you fly"?
11. E10: is the file students open the "Sprint brief" or the "homework brief"?
12. E11: slide 3 falsifier ("any guardrail that passes only because the attack was never delivered") vs the slide 23 card ("a guardrail credited when the attack never reached it, or a pass obtained by disabling a check"). Which list is authoritative?
13. Textbook contents note (in `textbook.py`): "The full prose will follow in a later edition." Restore "The prose follows", or "The full prose replaces each outline as the chapter's status advances"?
14. Textbook history passages: first person ("I started the governance kit in January 2026", "I developed Sprint and Drift for CIDM 6330") or passive?
15. Ch. 9 says "Twenty-five dated incidents (Appendix G)"; Appendix G has 21 rows.
16. Ch. 26: "the student executes, the instructor observes and attests" vs §26.3 "the human executes and observes". Who runs the commands at the closeout?
17. Ch. 3: "Cognitive surrender, mediated observation, governance theater: three names for the same failure" vs Appendix C listing them separately.
18. Appendix A flight-card header separator: "FLIGHT CARD · SORTIE <N> : <short name>" (the em dash is banned). Match gzkit's template?
19. Persona order: glossary says anti-trait first; the mini deck says the deny line first; both say "in that order". Which order, or drop the ordering?
20. Is "the V&V must show the skill being called" a Final System requirement?
21. Restore glossary citations removed for lack of a course source: Beck (2002) TDD, North (2006) BDD, NIST SHA-2 (2001)?
22. Receipt fields: glossary (command, exit code, output hash, time) vs E9 (command, exit code, commit, output hash). Which set?
23. E1: "hundreds of thousands of stars in weeks" has no source; keep, source, or cut?
