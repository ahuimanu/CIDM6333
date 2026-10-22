# Voice pass log: scaffolding (Oct 22, 2026)

Files: `docs/index.html`, `docs/lectures/index.html`, `tools/sitekit/readings.md`, and the reader-facing string literals in `tools/sitekit/textbook.py`, `glossary.py`, `reader.py`, `deck.py`.

Edit count: 43 lines changed on the home page (3 ledes, 17 figure cards, 16 lecture cards, 2 exercise cards, 2 reference cards, 1 eyebrow), 2 lines on the lecture index (lede, card row), 16 lines in readings.md, 2 strings in textbook.py, 1 in glossary.py, 3 in reader.py, 2 in deck.py. Tag counts unchanged (203 and 108 start tags); the four Python files parse and import; lecture cards are identical on both pages.

## What changed, by pattern

**#35 definition-colon ledes and slide-outline fragments (dominant).** Nearly every lecture card was a semicolon or middle-dot list copied from a slide outline, and eight figure cards opened "The X, the Y, and a Z." Each became one or two sentences with a verb, grounded in that figure or deck's own lede and section headings.

- "Chunk, represent, store, score, inject: four questions against a five-record store with two retrievers, eviction, and a ledger." → "A memory record is a claim with a source, and forgetting is an event. One record travels from a flight log through retrieval into the window and out again through eviction, and a retrieval lab runs the deck's four questions against a five-record store with two retrievers and a ledger."
- "Workflows versus agents; the five patterns; every framework is a theory of who owns the loop; ADR-1" → "Separates workflows from agents, lays out the five patterns, argues that every framework is a theory of who owns the loop, and ends with the build: the loop refactored into one of the patterns, with the choice recorded in ADR-1."
- Glossary page lede (glossary.py): "Every name that the lectures use without stopping to introduce it: systems, papers, ..." → "The lectures use many names without stopping to introduce them, and this page introduces each one. An entry covers one system, paper, protocol, company, or term of the course's own vocabulary, and says what the thing is, ..."
- Textbook contents note (textbook.py): "Every chapter is an outline edition: learning outcomes, sections, ... The prose follows." → "Each chapter is published here as an outline. The outline carries the learning outcomes, the section plan, ... The full prose will follow in a later edition."
- Reader lede (reader.py, deck.py): "The speaker notes, slide by slide: what the lecture says about each slide, then the slide's own wording." → "The speaker notes follow here slide by slide. Under each slide is what the lecture says about it, and then the slide's own wording."

**#38 templated siblings.** The sibling diff on the first three words of every card now gives 42 distinct openings. Ten lecture cards had settled into "Verb-s the deck" (Treats, Treats, Traces, ...); E3 and E8 were reshaped so no two adjacent cards share the shape. Figure cards vary between a question (Who Owns the Loop), an imperative (The Gate Holds, N×M), a stipulation (Memory Is a Claim, Rolled Back, Skill on Demand), and a description.

**"names" ban.** "The 2017 paper names a constraint" → "the authors state a constraint"; "Every reading the chapters name" → "cite" (readings.md intro and textbook.py link); "the outline names six hook events" → "lists" (two places); "are named in chapter 9's outline" → "are cited"; "Glossary · every named thing" → "every name the lectures use".

**#36 epigram landing.** Attention mini-lecture closer "Every model your harness calls descends from it." kept its fact and gained its reason: "..., which is why the course reads it as the first design record in the lineage."

**Em dashes and semicolons (house rule; STE rule 9 for file lists).** All six em dashes in readings.md annotations became sentences or parentheses; all semicolons in annotations, open items, card text, and injected paragraphs became periods or "and". Em dashes inside chapter headings and cited titles ("Harness Engineering — gzkit Appraisal") are titles and were not touched.

**Actor removal / nominalization (STE rules 2, 3).** "This slide covered the running of the session" → "covered how the session ran"; "Cost is plotted against BLEU, ... each get a working chart" → "The figure plots cost against BLEU, ... and gives ... a working chart each"; "cost and latency are read from it ... are placed" → "come out of it ... belong at".

**#40 instructing.** Both exercise cards now lead with the task in the imperative: "Build AGENTS.md, a skill, and a memory store side by side. Run three probes ..." and "Work E0 to E8 in your own repository. Locate every file on the outer ring, make each one fire, and record the trace."

**Fragments and parts lists in ledes.** "All lecture decks as slide pages, each with ..." → "Every lecture deck is here as a slide page. Each page carries ..."; "Interactive explainers for the course, one or more for each Evolution." → "Each figure is an interactive page that steps through one mechanism from a lecture, and every Evolution has at least one."

## Self-audit artifacts (after the final pass)

**Closer list** (last sentence of every card and lede, home page; the lecture index repeats the lecture cards):

- Below each figure, one or more panels (a simulator, a checker, a sorting task) let you run the mechanism yourself.
- ..., and a temperature sampler and a chart of token cost per turn show what each loop costs.
- A switch removes the encoder to show which half the GPT lineage kept, and panels work the attention, the positional encodings, and Tables 1 and 3.
- The figure plots cost against BLEU, changes one thing at a time against a fixed base, and gives the warmup schedule, the attention pictures, and the parsing task a working chart each.
- A simulator flies scripted episodes through it and shows the budget spiral when the halt check is off.
- ..., and a picker shows which parts of the loop each framework from the E2 teardowns takes from you.
- Pick a tool call (...) and play it through the model, the harness, the permission gate, the human, the tool, and the ledger, on the path E3 prescribes.
- The figure then lays out hosts, clients, and servers, the three server primitives, and one tool call before and after MCP.
- ..., and a live panel pins a tool description to a hash and reports when it changes.
- Run the four compaction moves on a fourteen-turn session, then watch a window reach 258K tokens and run out.
- ..., and a retrieval lab runs the deck's four questions against a five-record store with two retrievers and a ledger.
- Replay the deck's worked trace, then give the reviewer edit rights and see how a pair of agents becomes one agent with extra steps.
- The MAST failure matrix sorts fourteen ways coordination fails, and the ten-deep chain shows how a summary becomes a fact, with receipts and without them.
- The simulator counts how often a gate that sees only a few runs lets a regression through.
- Click a span to read its attributes, set the two accounts side by side, and find the place where the trace contradicts the narrative.
- Step through one release, a broken one, and the way back, break a provider to watch the circuit breaker open, and compare two ways to ship the same release.
- Sort six facts into the right drawer.
- The figure follows one skill, flight-card, from its folder on disk to the turn it runs on, shows the three ways it fails to run, and checks your trigger wording and frontmatter.
- The figure then lays out the three outcomes and ranks the fixes from weakest to strongest.
- Every affordance from E0 to E8 is on its ring, and a checker asks you to place a new one.
- The slides carry no dates, so look in the course calendar for those.
- The Evolutions and the Sprint and Drift rhythm come first, then flight cards and sorties, the Chase, the two toolkit routes, and the Final System.
- (E0) ... and ends with the Degradation Pattern, the covenant, and the five gates that keep the human at Index zero.
- (E1) ... and then sets the loop that has no halt beside the loop that writes a ledger.
- (E2) ... and ends with the build: the loop refactored into one of the patterns, with the choice recorded in ADR-1.
- Hooks sit between the two as a membrane.
- The build is one server that two clients call, with every call logged.
- The deck ends on harness engineering, under the framing sentence that the product is the harness.
- Compaction, progressive disclosure, subagents, handoffs, and the layers of truth each follow from that budget.
- What is kept, who wrote it, how is it found again, and when is it deleted.
- (E8) ..., result contracts that fail closed, two-stage review, and a state graph with a human interrupt.
- (E9) ..., delegation and handoff, and the contracts an agent marketplace would need.
- The second half reads five agent benchmarks for what each one measures and what it hides.
- The nine failure modes become red-team probes, system cards count as evaluation documents, and guardrails belong at an enforcement locus.
- (E12) ... and ends with the Heavy-lane gates and the release ceremony that a release must pass.
- Every model your harness calls descends from this paper, which is why the course reads it as the first design record in the lineage.
- ..., a table separates what OpenCode already has from what you write, and the last slides build the reviewer that cannot edit.
- Then one partner plants a memory record that contradicts the intent file, and the pair finds out whether a stale memory can beat a rule that is in the window.
- Then build a reviewer agent that cannot edit and test it on a codec change.
- A glossary of the names the lectures use, and the textbook the course is written from.
- Lecture transcripts link here on a term's first mention.
- Its twenty-six chapter outlines and the appendices are mapped to the Evolutions, and each lecture page links the chapters it draws on.

None of these works as a caption or a moral out of context; each carries a fact about the page it points to. The two shortest ("Hooks sit between the two as a membrane.", "Sort six facts into the right drawer.") state a position and a task respectively.

**Lede list** (first sentence of every card and lede): 42 entries, 42 distinct openings (listed under the sibling diff in the session transcript; the first three words of each are: Each figure is / A language model / Figure 1 of / Weighs the evidence / The agent loop / Who decides what / Pick a tool / Move two sliders / Two things cross / The context window / A memory record / The controller as / Follows the four / A delta gate / One agent run / A release is / Your harness has / A skill is / Two students share / Three rings and / Every lecture deck / How the course / Starts from the / Builds an agent / Separates workflows from / Each tool is / Why MCP turns / Transports, authorization, and / Treats the context / Defines memory as / Plan, do, check / Opens with the / Golden sets, regression / Traces and receipts / Takes a system / Reads the 2017 / Prepares the follow-along / Build AGENTS.md, a / Work E0 to / A glossary of / Each entry covers / Subtitled The Design). No "X is Y: a, b, c" opening remains.

**Claim list** (frequency or consensus claims):

- "every Evolution has at least one [figure]": checkable against the figure cards (E0 through E12 each appear in at least one Figure eyebrow). Kept.
- "every halt condition has its own labeled exit": the figure's own lede. Kept.
- "argues that every framework is a theory of who owns the loop": attributed to the deck with "argues that". Kept.
- "on every turn the model knows what is in the window and nothing else": the Window Budget figure's lede. Kept.
- "Every model your harness calls descends from this paper": the mini lecture's thesis, carried over from the original card; a fact about transformer lineage rather than a frequency claim. Kept; flagged below as the one I am least sure of.
- "how often a gate that sees only a few runs lets a regression through": names a simulation, not a claim. Kept.
- No "most", "usually", or "often" claim remains on either page or in readings.md.

**Sibling diff:** home-page lecture cards and lecture-index cards are byte-identical per lecture (same lecture, same card, by design); within each set no two cards share a skeleton.

## ste_check lines declined

- 43 sentences over 25 words: all are explanatory card text, where the brief imposes no ceiling. The two exercise cards (instruction register) were split so no instruction sentence exceeds 25 words except "Then one partner plants a memory record that contradicts the intent file, and the pair finds out whether a stale memory can beat a rule that is in the window." (29 words), kept because it carries the condition the exercise tests.
- "affordance" gerund flag: false positive (noun).
- Passives left in place: "are frozen", "is committed" (One Run Is an Anecdote), "is called" (Three Drawers), "is kept ... is deleted" (E7 questions), "is written from", "are mapped", "is cited", "is stewarded", "is pinned", "are cited", "is published". These describe states of a design or a document, not judgments, and the actor is the figure or the chapter already in the sentence.
- Noun-cluster flags: all are list runs ("progressive disclosure subagents handoffs") or a title ("Why Do Multi-Agent LLM Systems Fail"), not clusters.

## Left alone, with reason

- `reader.py` line 80, `REWRITE = [(r"\bTonight's claim\b", "The claim"), ...]`: this list produces the "The claim" phrasing Jeffry flagged on lecture pages, but the brief forbids edits to REWRITE lists. Flagged for the parent.
- `glossary.py` line 4 docstring "every named thing": a module docstring, not injected into any page.
- readings.md line 92 "(re-verify against gzkit 0.34.9)": a maintenance note on a reading entry; left as a fact about verification state rather than a QA aside, but it could be read either way.
- Em dashes in readings.md chapter headings and cited titles: titles, never edited.
- "claim" in "Memory Is a Claim", "a claim with a source", "a typed claim", "Claim, Receipt, Verdict": course vocabulary (record-as-claim, gzkit sense), not the "Tonight's claim" thesis usage.
