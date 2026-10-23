# CIDM 6333 site: handoff (October 22, 2026)

Live: https://ahuimanu.github.io/CIDM6333/ · repo ahuimanu/CIDM6333 (master) · local clone ~/Documents/Courses/CIDM6333

## State

- Voice chain (humaniser, STE, scholarly-voice, humaniser check) run over all course text: decks (slide wording via `tools/sitekit/voice/<slug>.json`), speaker notes (`tools/sitekit/notes.json`), textbook (`topic-guide.md`, `readings.md`), glossary (`glossary_data.py`), figures, exercises, index pages.
- Independent review found 289 findings (about half were facts the pass had added, changed or dropped). Repair pass restored them to the pre-pass wording. Logs: `tools/review/voice-review/<scope>.md` (findings + "Repair log").
- WT brand colours (no logo, by ruling): `tools/sitekit/brand.py`. Body text is Avenir Next; headings, labels and all SVG figure text stay in Barlow Condensed (Avenir Next Condensed as fallback) because the figure geometry was measured in it. A regular-width face made labels spill out of their boxes; six overflowing mono labels in Three Drawers, Pilot and Planter, Skill on Demand and Memory Is a Claim were fitted with textLength.
- Course-administration specifics removed so the materials stay reusable (LMS, submission mechanics, late policy, office hours, Calendly, Discord, rooms, phone, dates, times).
- Build order: `textbook.py → voice_apply.py → reader.py → deck.py docs <web-native slug> → glossary.py → nav.py → brand.py` (from `tools/sitekit`, docs = `../../docs`).
- Push: device-code login (client id 178c6fc778ccc68e1d6a, scope repo) → token at /tmp/gh_tok in the Mac VM; push from the clone with `http.extraheader`.

## Standing rules from this session

- Every style pass carries "never add a fact" and is diffed against the pre-pass text before publishing.
- No course-administration specifics anywhere (enduring, reusable materials).
- Sortie environment: OpenCode and Big Pickle only. No local token issuer, no local OAuth server.

## Done Oct 23: all decks web-native

All 15 pptx decks are built by `deck.py` (DECK_META holds each deck's title and slide-to-figure links). Run-of-show, break, lab and Sprint slides are dropped by `reader.DROP_TITLE`; term footers ("CIDM 6333 · Fall 2026") are dropped. Overlong slide bodies shrink to fit (down to 72%); three slides still scroll (E0 16 and 19, E1 4) because the pptx layout puts a tall side panel in the first row. "As presented" images and the PDF still show the pptx wording.

## Small tasks (no ruling needed)

- Done Oct 23: Sortie 5 no longer tests authorization (Jeffry: drop it). Card keeps the honest read, the poisoned resource, and the pin check; the lecture still teaches the authorization flow as background. `deck.py`: a voice override of "" drops the line.
- Done Oct 23: E0/E2 workflow paraphrase checked against "Building Effective Agents" (matches: workflows for well-defined tasks, agents where the number of steps cannot be predicted); E8 three-level nesting default confirmed in the Claude Code sub-agents docs (retrieved Oct 23, 2026); glossary chapters fixed (JADE entry 4, 6, 7; ToolBench 6, 12). HumanEval appears in no chapter; its ch=19 stays.

## Questions for Jeffry

All resolved Oct 22–23, 2026. Rulings, in order: Raji/Groves citation; E2 workflow line = Anthropic's advice; E10 shares only pre-registration with the five flight-test rules; E8 falsifier one; E8 80% = BrowseComp; E1 Kojima; submission/LMS/office-hours/late-policy specifics dropped; Sortie 5 drops authorization; E5 recap points to E4; no mentions of time; E0 'done' gets a reason (closed attestation vocabulary); gzkit = a custom harness on top of a vendor harness (Figure 17); E2 amended miss is still a FAIL, the amended ADR earns the exceptional mark; E3 gate code: attestation for irreversible, confirm for write; E4 close names discovery, negotiation, transport independence; "membrane" replaced by the mechanism; E9 "before you fly" stays; E11 slide 3 matches the card; textbook is a living document (status lines removed); preface in first person; Ch. 9 twenty-one incidents; closeout: student presents, instructor executes, observes, attests; cognitive surrender / mediated observation / governance theater are three related failures; flight-card headers use a plain hyphen (normal hyphens are always fine; only the em dash is banned); persona order claim dropped; Skill on Demand: Final System V&V must show the skill call; glossary citations Beck 2002, North 2006, FIPS 180-2 restored after checking; receipt = command, exit code, commit, output hash, time; E1 AutoGPT stars sentence cut.
