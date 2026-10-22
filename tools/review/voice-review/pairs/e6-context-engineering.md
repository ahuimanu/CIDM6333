# e6-context-engineering: speaker notes, before and after the voice pass

## Slide 1

### BEFORE

Evolution 6. For five weeks the window has filled up behind your back: tool results in E3, MCP resources in E4, the AGENTS.md you measured in E5. Tonight we treat the window as something you design and measure. The framing sentence from the run sheet: the window is an artifact with a budget. Survey: how four harnesses decide what goes in, what gets compacted, and what gets handed off, with Claude Code, Codex, and Cursor read for mechanism and OpenCode read because it is the harness you use. Build: your system gets a budget line on every turn, a compactor that keeps what you declared, a handoff a stranger can resume from, and an append-only ledger. The E5 Sprint asked you to re-measure what your harness loads from AGENTS.md; that number is where tonight starts.

Cut from slide 1 (full wording):
- Evolution 6 · Lecture · Thu 10/08
- CIDM 6333 · Agentic Systems Design and Development · 4:00–6:00 · CC209 / Survey: Claude Code, Codex, Cursor, and OpenCode context surfaces · Anthropic's context-engineering and long-running-harness guidance   ·   Build: a per-turn budget meter, a compactor with a keep list, a handoff a fresh session can resume from, and an append-only ledger (lab 6:00–6:30, self-guided)

### AFTER

Evolution 6. Over the last five Evolutions the window filled without your attention: tool results in E3, MCP resources in E4, the AGENTS.md you measured in E5. This Evolution treats the window as an artifact you design and measure, which is the framing sentence of the deck: the window is an artifact with a budget. The survey covers how four harnesses decide what enters the window, what compaction removes, and what a handoff carries; the teardowns read Claude Code, Codex, and Cursor for mechanism, and OpenCode because it is the harness you fly. The build adds four things to your system: a budget record on every turn, a compactor that keeps what you declared, a handoff a stranger can resume from, and an append-only ledger. The E5 Sprint asked you to re-measure what your harness loads from AGENTS.md. That number is the starting point.

Cut from slide 1 (full wording):
- Evolution 6 · Lecture
- CIDM 6333 · Agentic Systems Design and Development / Survey: Claude Code, Codex, Cursor, and OpenCode context surfaces · Anthropic's context-engineering and long-running-harness guidance   ·   Build: a per-turn budget meter, a compactor with a keep list, a handoff a fresh session can resume from, and an append-only ledger (self-guided lab)

## Slide 2

### BEFORE

Two hours of lecture and a half-hour lab that you run yourselves. Eight minutes of framing; forty-five on a spine with eight parts, which is where the new material lives; a five-minute break; thirty minutes of teardowns, including a Design Analysis we build together on the board; fifteen on the reference design; fifteen on the lens, the card, the lab, and the Sprint. There is no consultation tonight and no in-class Go/No-Go: your Chase signs your card in the repository before you fly, and reads your log after. The homework brief has the dates.

Cut from slide 2 (full wording):
- The run of show; the lab at 6:00 is yours
- What is in the window; why a budget; instrumenting it; compaction; progressive disclosure and subagents; handoffs; layers of truth; the common mistakes
- Claude Code, Codex, Cursor, OpenCode, and Anthropic's long-running harness, each read for mechanism, choice, cost, failure mode; a live Design Analysis
- 6:00

### AFTER

The lecture has six parts, and the lab after it is self-guided. The framing states two rules and the design claim. The spine, in eight parts, carries the new material. After the break, the teardowns read five harnesses for mechanism, choice, cost, and failure mode, with a Design Analysis built on the board in class. The reference design follows, then the lens, the card, the lab, and the Sprint. There is no in-class consultation and no in-class Go/No-Go in this Evolution: your Chase signs your card in the repository before you fly and reads your log after. The homework brief has the dates.

Cut from slide 2 (full wording):
- What is in the window; why a budget; instrumenting it; compaction; progressive disclosure and subagents; handoffs; layers of truth; the common mistakes
- Claude Code, Codex, Cursor, OpenCode, and Anthropic's long-running harness, each read for mechanism, choice, cost, failure mode; a live Design Analysis

## Slide 3

### BEFORE

Framing. On any turn the model has the window and nothing else: the system prompt, the instruction file, the history, the tool results, whatever you retrieved. Two rules for the next two hours. First, measure it every turn, with the provider's own count against a budget you chose; last week some of you reported a file size, and a file size is not what was loaded. Second, what must survive goes to a file, because the conversation is exactly the part that compaction and a new session throw away. The claim is from Chapter 15: a handoff lets a fresh session resume with no loss of intent, measured by one observation, whether the first action is the one the handoff named. Four falsifiers, and the last one is the shortcut every one of you will be tempted by: pasting the transcript is not a handoff.

Cut from slide 3 (full wording):
- Everything the model knows about your task on this turn is in the window. What is not in it does not exist for the model. What is in it by accident still costs attention.
- Measure it on every turn. Log the tokens the provider counted, against a budget you declared, for every call. File size and a session total are not the measure. / What must survive goes to a file. Intent that lives only in the conversation is lost at the next compaction or the next session. Decisions go to the ledger; rules go to canon; the window is rebuilt from them.
- A handoff written at session end lets a fresh session resume with no loss of intent: the fresh session's first action is the one the handoff named. It is falsified if the fresh session asks a question the handoff answered, if a derived view (L3) contradicts the ledger and wins, if any turn has no budget record, or if the pass came from pasting the old transcript into the new session.

### AFTER

Framing. On any turn the model has the window and nothing else: the system prompt, the instruction file, the history, the tool results, whatever you retrieved. Two rules hold for the whole lecture. First, measure the window every turn, with the provider's own count against a budget you chose; in E5 some of you reported a file size, and a file size is not what the model loaded. Second, what must survive goes to a file, because the conversation is the part that compaction and a new session discard. The design claim comes from Chapter 15: a handoff lets a fresh session resume with no loss of intent, measured by one observation, whether the fresh session's first action is the handoff's first next step. The card lists four falsifiers. The last one is the shortcut: pasting the old transcript into the new session fails the test, because the test asks whether the handoff alone carried the intent.

Cut from slide 3 (full wording):
- On any turn, the model knows about your task only what the harness placed in the context window. Text left out of the window does not reach the model, and text placed there by accident still takes a share of the model's attention.
- Measure the window on every turn. For every call, log the tokens the provider counted, against a budget you declared. File size and a session total do not measure the window, because the window is one call's input. / Write to a file whatever must survive. Intent that exists only in the conversation is lost at the next compaction or the next session. Record decisions in the ledger and rules in canon, so that the harness can rebuild the window from them.
- A handoff written at session end lets a fresh session resume with no loss of intent: the fresh session's first action is the one the handoff listed first. It is falsified if the fresh session asks a question the handoff answered, if a derived view (L3) contradicts the ledger and wins, if any turn has no budget record, or if the pass came from pasting the old transcript into the new session.

## Slide 4

### BEFORE

Six categories. The harness writes the system prompt and tool definitions; you write the instruction files and the skills; you and the model together write the history; the tools write the results, and one test run or one log can be tens of thousands of tokens; your code decides what memory comes back. The last column is Claude Code's documented behavior after compaction, and it is the lesson of the night in one column. Files reload from disk. The skill listing does not come back, invoked skills come back capped. The conversation becomes one summary. So a rule you typed in chat on turn three is, after compaction, whatever the summarizer chose to write about it. Codex and OpenCode do not publish this table, which is why the lab measures instead of reading.

Cut from slide 4 (full wording):
- What is in the window, and who put it there
- Source: Claude Code docs, 'Explore the context window' and 'Commands', checked 09/24/2026. Codex and OpenCode do not publish a per-category list; you infer theirs by measurement (tonight's lab).
- The column that matters for Sortie 6 is the last one: anything you said only in conversation is in the row that becomes a summary.

### AFTER

Six categories. The harness writes the system prompt and the tool definitions. You write the instruction files and the skills. You and the model together write the history. The tools write the results, and one test run or one log file can be tens of thousands of tokens. Your code decides what memory comes back. The last column is Claude Code's documented behavior after compaction, and it carries the lesson of the Evolution: files reload from disk; the skill listing does not come back; invoked skills come back capped; the conversation becomes one summary. For this reason a rule you typed in chat on turn three is, after compaction, whatever the summarizer chose to write about it. Codex and OpenCode do not publish this table, so the lab measures their behavior instead of reading it.

Cut from slide 4 (full wording):
- What is in the window, and who put it there
- Source: Claude Code docs, 'Explore the context window' and 'Commands', retrieved September 24, 2026. Codex and OpenCode do not publish a per-category list; you infer theirs by measurement (the Evolution 6 lab).
- For Sortie 6, read the last column: anything you said only in conversation sits in the row that compaction turns into a summary.

## Slide 5

### BEFORE

Why a budget when the context window is a million tokens. Four numbers. Chroma tested eighteen models in July 2025 and found performance becoming less reliable as input length grew, on tasks as plain as finding a sentence. Liu and colleagues showed the U-curve: models use the start and end of a long input better than the middle. Anthropic's framing is an attention budget, because every token relates to every other one. And the payoff number: Anthropic's context editing, clearing stale tool results, cut tokens by eighty-four percent on a hundred-turn search task and let runs finish that otherwise ran out of window. The design consequence is on the slide: the window is the provider's limit, the budget is yours, and for Big Pickle you have no published limit at all, so the budget is the only number you have.

Cut from slide 5 (full wording):
- Why a budget, when the window says one million
- Consequence for your build. Declare a turn budget below the model's window, and decide what the loop does when a turn crosses 80% of it: clear old tool results, compact, delegate, or hand off. Big Pickle's window is unpublished, so for it you cannot read the limit off a spec sheet; you declare a budget and hold yourself to it. / Anthropic's definition (Sep 2025). Context engineering is 'the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference.'

### AFTER

Why a budget when the context window is a million tokens. Four numbers answer. Chroma tested eighteen models in July 2025 and found that performance became less reliable as input length grew, on tasks as plain as finding a sentence. Liu and colleagues (TACL 2024) showed the U-curve: models use the start and the end of a long input better than the middle. Anthropic frames the window as an attention budget, because every token relates to every other token and the pair count grows as n squared. The fourth number is the payoff: Anthropic's context editing, which clears stale tool results, cut tokens by eighty-four percent on a hundred-turn search task and let runs finish that otherwise ran out of window. The design consequence follows: the window is the provider's limit, the budget is your design decision below it, and for Big Pickle there is no published limit at all, so the budget you declare is the only number you have.

Cut from slide 5 (full wording):
- Why a budget, when the window says one million
- Consequence for your build. Declare a turn budget below the model's window, and decide what the loop does when a turn crosses 80% of it: clear old tool results, compact, delegate, or hand off. Big Pickle's window is unpublished, so you cannot read its limit from a specification sheet. Declare a budget for it and keep your loop within that budget. / Anthropic's definition (Sep 2025). Context engineering is 'the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference.'

## Slide 6

### BEFORE

The instrument. Ten lines of Python after every model call: read the usage object the provider returned, compute the total, write a record to an append-only file, and compact when you cross eighty percent. The field names differ by provider, which is the most common bug you will hit: OpenAI-compatible endpoints including Ollama's say prompt and completion tokens; Anthropic's API says input and output and counts cached tokens in separate fields, so a naive sum undercounts. On the right, what the record must answer, and the category breakdown is what separates sound from exceptional. Note the last line: your record is ledger, layer two; the harness's on-screen counter is a derived view, layer three, and we will see tonight that one of those counters is cumulative and not the window at all.

Cut from slide 6 (full wording):
- Which turn, and which session. / How many tokens the provider counted in and out. / The declared budget, and the percentage used. / By category where you can: instructions, history, tool results. Count at assembly time; if you estimate (characters ÷ 4), label it an estimate. / What the loop did about it: nothing, clear, compact, delegate, hand off. / The record is L2: the ledger. The TUI's counter is L3: a view someone else computed.
- If the provider returns no usage fields, the card must declare the fallback count before Go; a missing count discovered in flight is an ABORT.

### AFTER

The instrument. Ten lines of Python run after every model call: read the usage object the provider returned, compute the total, write a record to an append-only file, and compact when the total crosses eighty percent of the budget. The field names differ by provider, and the difference produces a wrong total unless your code checks which fields came back: OpenAI-compatible endpoints, Ollama's included, return prompt and completion tokens; Anthropic's API returns input and output tokens and counts cached tokens in separate fields, so a sum of input and output alone undercounts. The right panel lists what each record must answer; the category breakdown is what separates a sound build from an exceptional one. The last line of that panel matters: your record is the ledger, layer two; the harness's on-screen counter is a derived view, layer three. The OpenCode teardown shows a counter of that kind that is cumulative and not the window at all.

Cut from slide 6 (full wording):
- Which turn, and which session. / How many tokens the provider counted in and out. / The declared budget, and the percentage used. / By category where you can: instructions, history, tool results. Count at assembly time; if you estimate (characters ÷ 4), label it an estimate. / What the loop did about it: nothing, clear, compact, delegate, hand off. / The budget record belongs in the ledger (L2). The TUI's counter is a derived view (L3) that the harness computed, so it does not serve as the record.
- If the provider returns no usage fields, the flight card must declare the fallback count before Go. A missing count discovered in flight is an ABORT.

## Slide 7

### BEFORE

Compaction as four moves in order of cost. Clearing drops stale tool output and keeps the fact that the call happened; it is cheap and it is what bought the eighty-four percent. Summarizing hands the history to a model and gets back a shorter story; it is lossy by design, and if you do not instruct it, the summarizer's taste decides what survives. Keeping verbatim is your countermeasure: a keep list, written before the sortie, of things that pass through untouched. Re-seeding is the move most people forget: after the summary, reload the canon and the ledger tail from disk, so the rules are the file's words and not the summary's paraphrase. The strip lists each harness's controls; your own loop needs all four moves, and Sortie 6 logs an event every time compaction runs.

Cut from slide 7 (full wording):
- Drop old tool results; keep the record that the call happened. Anthropic calls it tool result clearing; OpenCode's compaction.prune removes old tool outputs. Loses raw output only.
- A model writes a structured summary of the history: objective, decisions, files, errors, pending work. Lossy by design, and the summarizer decides what is lost unless you tell it.
- A declared keep list survives untouched: the current objective, the open test point, the last few turns, the pointers to canon. You write the list; the summarizer never sees it as optional.
- After the summary, reload L1 files and the ledger tail. Claude Code reloads CLAUDE.md and re-reads up to five recently modified files; your loop reloads what your README declares.

### AFTER

Compaction as four operations, in order of cost. Clearing drops stale tool output and keeps the record that the call happened; it is cheap, and it is the operation that bought the eighty-four percent. Summarizing hands the history to a model and gets back a shorter account; it is lossy by design, and unless you instruct the summarizer, the summarizer decides what survives. Keeping verbatim is your countermeasure: a keep list, written before the sortie, of items that pass through untouched. Re-seeding is the fourth operation: after the summary, reload the canon and the ledger tail from disk, so that the rules in the window are the file's words and not the summary's paraphrase. The strip at the bottom lists each harness's controls. Your own loop needs all four operations, and Sortie 6 logs an event every time compaction runs.

Cut from slide 7 (full wording):
- Drop old tool results; keep the record that the call happened. Anthropic calls it tool result clearing; OpenCode's compaction.prune removes old tool outputs. Loses raw output only.
- A model writes a structured summary of the history: objective, decisions, files, errors, pending work. Lossy by design, and the summarizer decides what is lost unless you tell it.
- A declared keep list survives untouched: the current objective, the open test point, the last few turns, the pointers to canon. You write the list, and the summarizer never treats it as optional.
- After the summary, reload L1 files and the ledger tail. Claude Code reloads CLAUDE.md and re-reads up to five recently modified files; your loop reloads what your README declares.

## Slide 8

### BEFORE

Four ways to keep tokens out of the window until they earn their place. Skills put a one-line description in context and the body on disk; you did this in E5 and tonight you can count what it saved. Deferred tools do the same for MCP: names first, schemas when needed, and Cursor published an A/B result of about forty-seven percent fewer tokens in runs that used an MCP tool. Just-in-time retrieval is the general form: carry pointers and load on demand, which is exactly how a good handoff should treat evidence. Subagents isolate: the child reads the ten files and returns a thousand-token summary. The cost of that one is the week-nine lesson: the summary is an assertion, and the gzkit casebook has a ten-deep chain where polished summaries became facts.

Cut from slide 8 (full wording):
- Load later, or load elsewhere: progressive disclosure and isolation
- The name and description sit in context; the body loads when the skill is invoked (OpenCode's skill tool; Claude Code). E5 moved procedures out of AGENTS.md into skills; tonight you count what that saved.
- Only MCP tool names enter context until a task needs one (Claude Code default). Cursor's A/B test (Jan 2026): 46.9% fewer agent tokens in runs that called an MCP tool.
- Keep identifiers, not contents: a path, a query, a ledger event id. Load the content at runtime with a tool (Anthropic, Sep 2025). In your system, a handoff should point at evidence, not paste it.
- The verbose work stays in the child's window; a summary returns, often 1,000–2,000 tokens (Anthropic). Cost: the summary is a claim. E9's rule arrives early: a subagent's claim is not evidence.
- Anthropic's name for the whole slide is 'just in time' context. LangChain's four verbs (Jul 2025): write, select, compress, isolate.

### AFTER

Four ways to keep tokens out of the window until they are needed. Skills put a one-line description in context and leave the body on disk; you did this in E5, and the lab lets you count what it saved. Deferred tools do the same for MCP: names enter first, schemas when a task needs them, and Cursor published an A/B result of 46.9 percent fewer agent tokens in runs that called an MCP tool. Just-in-time retrieval is the general form: the window carries pointers and the loop loads content on demand, which is also how a handoff should treat evidence. Subagents isolate: the child reads the ten files and returns a summary of about a thousand tokens. The cost of isolation is the E9 lesson arriving early: the summary is a claim the parent has not checked, and the gzkit casebook holds a chain ten summaries deep in which polished summaries became facts.

Cut from slide 8 (full wording):
- Progressive disclosure and isolation
- The name and description sit in context; the body loads when the skill is invoked (OpenCode's skill tool; Claude Code). In E5 you moved procedures out of AGENTS.md into skills. The Evolution 6 lab counts the tokens that change saved.
- Only MCP tool names enter context until a task needs one (Claude Code default). Cursor's A/B test (Jan 2026): 46.9% fewer agent tokens in runs that called an MCP tool.
- Keep identifiers, not contents: a path, a query, a ledger event id. Load the content at runtime with a tool (Anthropic, Sep 2025). In your system, a handoff should hold a pointer to each piece of evidence (a path or an event id) instead of a pasted copy.
- The verbose work stays in the child's window; a summary returns, often 1,000–2,000 tokens (Anthropic). Cost: the parent receives only the child's summary, which is an assertion without a receipt. The E9 rule applies here already: a subagent's claim is not evidence.
- Anthropic calls these techniques together 'just in time' context. LangChain's four verbs (Jul 2025): write, select, compress, isolate.

## Slide 9

### BEFORE

Handoffs, with the seven sections from the chapter. Read them as questions a stranger asks: what is true now, what will I get wrong, who decided what, what do I do first, what is half done, how do I check your claims, and where is the evidence. Two details carry the grade. The first next step is one action, a command or an edit, not a theme. The evidence section points, it does not paste, which is just-in-time retrieval applied to handoffs. On the right is what makes a handoff load without anyone remembering to paste it: a session-start hook, a rulings store so settled questions stay settled, an exit bookmark. Anthropic's long-running harness from last November is the same design by another name: progress file, feature list, git log, read first every session.

Cut from slide 9 (full wording):
- 1 Current state. What is true now; commit hash. / 2 Important context. What a stranger would get wrong. / 3 Decisions, with attribution. Who decided, when, where recorded. / 4 Next steps. The first one is a single action a stranger can take. / 5 Pending work. Started, not finished; blocked, and on what. / 6 Verification checklist. Commands that prove the state claimed. / 7 Evidence. Paths, ledger event ids, test output; pointers, not pastes.
- Session-start advisement. The harness reads the handoff and orientation before the first turn. Claude Code: a SessionStart hook (matchers startup, resume, clear, compact) whose stdout enters context. / Rulings store. Settled decisions as append-only records, so a fresh session does not re-ask them. / Exit bookmark. The last action taken and the exact point to resume. / In the wild. Anthropic's long-running harness (Nov 2025): each session reads a progress file, a JSON feature list, and the git log before it picks the next feature.
- The test of a handoff: a stranger with no transcript takes the action you named first, and asks nothing you already answered.

### AFTER

Handoffs, with the seven sections from the chapter. Read the sections as the questions a stranger asks: what is true now, what will I get wrong, who decided what, what do I do first, what is half done, how do I check your claims, and where is the evidence. Two details carry the grade. The first next step is one action, a command or an edit, and not a theme. The evidence section points at paths and ledger event ids and does not paste them, which is just-in-time retrieval applied to handoffs. The right panel lists the machinery that loads a handoff without anyone remembering to paste it: a session-start hook, a rulings store so settled questions stay settled, and an exit bookmark. Anthropic's long-running harness (November 2025) is the same design under other labels: a progress file, a feature list, and the git log, read first in every session.

Cut from slide 9 (full wording):
- 1 Current state. What is true now; commit hash. / 2 Important context. What a stranger would get wrong. / 3 Decisions, with attribution. Who decided, when, where recorded. / 4 Next steps. The first one is a single action a stranger can take. / 5 Pending work. Started, not finished; blocked, and on what. / 6 Verification checklist. Commands that prove the state claimed. / 7 Evidence. Paths, ledger event ids, test output, given as pointers instead of pasted copies.
- Session-start advisement. The harness reads the handoff and orientation before the first turn. Claude Code: a SessionStart hook (matchers startup, resume, clear, compact) whose stdout enters context. / Rulings store. Settled decisions as append-only records, so a fresh session does not re-ask them. / Exit bookmark. The last action taken and the exact point to resume. / In the wild. Anthropic's long-running harness (Nov 2025): each session reads a progress file, a JSON feature list, and the git log before it picks the next feature.
- A handoff passes when a stranger with no transcript takes the action you listed first and asks nothing the handoff already answered.

## Slide 10

### BEFORE

The architecture that makes the handoff checkable. Layer one is canon, prose written by people and changed by commit. Layer two is the ledger, events appended by the system when things happened, never edited. Layer three is everything derived: status pages, summaries, frontmatter, the counters on your screen. Precedence runs ledger over canon over derived, and a derived view can never block a gate, because it can be wrong without anyone having lied. Two placements to notice: the compaction summary is layer three, so when it disagrees with the ledger the ledger wins; and a handoff your agent drafted is layer three until you check it against the ledger. Your README declares these paths this week.

Instructor checks moved off the slide:
- [Verify the path and ADR number against the repository before class.]

### AFTER

The architecture that makes the handoff checkable. Layer one is canon: prose written by people and changed by commit. Layer two is the ledger: events the system appended when things happened, never edited. Layer three is everything derived: status pages, summaries, frontmatter, the counters on your screen. Precedence runs ledger over canon over derived, and a derived view can never block a gate, because a derived view can be wrong without anyone having lied. Two placements follow from the definitions. The compaction summary is layer three, so when it disagrees with the ledger the ledger wins. A handoff your agent drafted is layer three until you check it against the ledger. Your README declares these layers, with paths, in the Sprint.

Instructor checks moved off the slide:
- [Verify the path and ADR number against the repository before class.]

## Slide 11

### BEFORE

Three mistakes, each with a failure-mode number. First, the chat is the memory: you correct the agent in conversation, it complies, compaction runs, and the correction becomes a clause in a summary or disappears; that is failure mode five, correction fails, and the fix is to write it where it reloads. Second, the counter is the window: people report file size or a session running total. OpenCode has an open issue showing its session totals accumulate cache reads across turns, so a big number on screen may be a lifetime sum and not the current window; verify that on your version tonight. Third, the handoff is a diary: a friendly paragraph with no next action. That is summary laundering from the human side, and it fails the sortie's one observable.

Cut from slide 11 (full wording):
- A rule typed in conversation lives in history, and history is what compaction summarizes. Claude Code reloads CLAUDE.md from disk after /compact; it does not reload what you typed. / Fix. Put the rule in canon (L1) or the decision in the ledger (L2), then compact and ask for it back.
- File size, or a session's running total, reported as context. OpenCode's session totals add every turn's cache reads (issue #30649); the window is one call's input. [verify on your version] / Fix. Log per call from the provider's usage fields; compare with the counter once.
- ‘Made good progress on the loop; continue tomorrow.’ No next action, no names on decisions, no evidence. The fresh session reconstructs intent from the code, and guesses. / Fix. Seven sections; the first next step is a command a stranger can run.

Instructor checks moved off the slide:
- [verify on your version]

### AFTER

Three mistakes, each with a failure-mode number from Appendix C. First, the chat is the memory: you correct the agent in conversation, it complies, compaction runs, and the correction becomes a clause in a summary or disappears. That is failure mode five, correction fails, and the fix is to write the correction where the harness reloads it. Second, the counter is the window: a build reports file size or a session running total as context. OpenCode has an open issue (#30649) in which session totals accumulate cache reads across turns, so a large number on screen can be a lifetime sum and not the current window; verify this on your version in the lab. Third, the handoff is a diary: a friendly paragraph with no next action. That is summary laundering from the human side, and it fails the sortie's one observable.

Cut from slide 11 (full wording):
- A rule typed in conversation lives in history, and history is what compaction summarizes. Claude Code reloads CLAUDE.md from disk after /compact, but it does not reload what you typed. / Fix. Put the rule in canon (L1) or the decision in the ledger (L2), then compact and ask for it back.
- File size, or a session's running total, reported as context. OpenCode's session totals add every turn's cache reads (issue #30649); the window is one call's input. [verify on your version] / Fix. Log per call from the provider's usage fields; compare with the counter once.
- ‘Made good progress on the loop; continue tomorrow.’ No next action, no names on decisions, no evidence. The fresh session has to reconstruct intent from the code, so it guesses. / Fix. Seven sections; the first next step is a command a stranger can run.

Instructor checks moved off the slide:
- [verify on your version]

## Slide 12

### BEFORE

Five minutes. The question is the one the teardowns answer for four harnesses: what in the window exists nowhere else. Write your answer on a sticky note; we come back to it in the lens.

Cut from slide 12 (full wording):
- Before you sit down: if your current coding session died now, what in its window could you not rebuild from files?

### AFTER

Five minutes. The question on the slide is the one the teardowns answer for four harnesses: what in the window exists nowhere else. Write your answer down; the evaluation lens returns to it.

Cut from slide 12 (full wording):
- Before you sit down: if your current coding session died now, what in its window could you not rebuild from files?

## Slide 13

### BEFORE

The four harnesses in one table, so the next four slides can go deep one at a time. Read across the rows. Instruction files: note the change since the E5 deck, Claude Code now reads AGENTS.md on its own when there is no CLAUDE.md, from version 2.1.277. Codex concatenates from the root down and stops at thirty-two kilobytes. Seeing the window: Claude Code has the best instrument, a per-category grid; Codex reports tokens used and remaining; OpenCode gives you counters and an export you can compute from, which is tonight's lab. Compaction: every one auto-compacts and every one lets you trigger it by hand; only Claude Code gives you a hook that can block it. Keeping things out: Cursor's answer is the most interesting, and it gets its own slide.

Cut from slide 13 (full wording):
- Sources checked 09/24/2026: code.claude.com docs (memory, commands, model-config, hooks); developers.openai.com/codex (slash commands, config sample, AGENTS.md guide); cursor.com docs and blog (Jan 6, 2026); opencode.ai docs (config, TUI, CLI, agents, skills). These change monthly.

Instructor checks moved off the slide:
- [verify before class]

### AFTER

The four harnesses in one table, so that the next four slides can take them one at a time. Read across the rows. Instruction files: Claude Code now reads AGENTS.md on its own when there is no CLAUDE.md, from version 2.1.277, a change since the E5 deck. Codex concatenates AGENTS.md files from the root down and stops at 32 KiB. Seeing the window: Claude Code has the best instrument, a per-category grid; Codex reports tokens used and remaining; OpenCode gives counters and an export you can compute from, which is what the lab does. Compaction: every harness auto-compacts and every harness lets you trigger compaction by hand; only Claude Code gives you a hook that can block it. Keeping things out: Cursor's answer differs from the other three and gets its own slide.

Cut from slide 13 (full wording):
- Sources retrieved September 24, 2026: code.claude.com docs (memory, commands, model-config, hooks); developers.openai.com/codex (slash commands, config sample, AGENTS.md guide); cursor.com docs and blog (Jan 6, 2026); opencode.ai docs (config, TUI, CLI, agents, skills). Recheck these pages before you rely on them, because the vendors revise them.

Instructor checks moved off the slide:
- [verify before class]

## Slide 14

### BEFORE

Claude Code is the reference harness, and its documentation now states exactly what survives compaction. Files reload; recently modified files are re-read; invoked skills return capped; the conversation becomes one summary. That is a design choice stated plainly: the harness assumes whatever mattered was written to a file. The cost is detail, and a less obvious one: compaction is itself a big request because it has to read everything it summarizes. The failure mode is correction fails. The control points are the interesting part for you: focus instructions, a compact-instructions section in CLAUDE.md, a PreCompact hook that can refuse, and a SessionStart hook with the compact matcher that can put your handoff back after every compaction.

Cut from slide 14 (full wording):
- System prompt, CLAUDE.md, auto memory, MCP tool names: reloaded. / Up to five most recently modified files: re-read. / Invoked skills: re-injected, 5,000 tokens each at most. / The skill listing: not reloaded. / The conversation: one structured summary (requests and intent, files, errors and fixes, pending tasks, current work). Full tool outputs and reasoning are gone. / Auto-compaction triggers at the auto-compact window; on the Anthropic API a 1M-window Sonnet 5 session compacts at about 967K by default.
- Design choice. Files are authoritative and reload; conversation is disposable and summarized. The harness assumes what matters was written down. / Cost. A long session's detail is gone after compaction; /compact itself is a large request, because it reads what it summarizes. / Failure mode. #5 correction fails: a correction given only in chat survives as the summarizer's paraphrase. / Control points. /compact Focus on …; a 'Compact instructions' section in CLAUDE.md; PreCompact hook (exit 2 blocks); SessionStart with matcher compact re-injects what you choose.
- The harness already implements rule two: files reload, the chat does not. Your loop should do the same on purpose.

### AFTER

Claude Code is the reference harness, and its documentation now states what survives compaction. Files reload; recently modified files are re-read; invoked skills return capped; the conversation becomes one summary. That is a design choice stated plainly: the harness assumes that whatever mattered was written to a file. The cost is detail, and a second cost is less obvious: compaction is itself a large request, because the compaction call reads everything it summarizes. The failure mode is correction fails. The control points are the part that applies to your build: focus instructions on /compact, a compact-instructions section in CLAUDE.md, a PreCompact hook that can refuse, and a SessionStart hook with the compact matcher that can put your handoff back after every compaction.

Cut from slide 14 (full wording):
- System prompt, CLAUDE.md, auto memory, MCP tool names: reloaded. / Up to five most recently modified files: re-read. / Invoked skills: re-injected, 5,000 tokens each at most. / The skill listing: not reloaded. / The conversation: one structured summary (requests and intent, files, errors and fixes, pending tasks, current work). Full tool outputs and reasoning are gone. / Auto-compaction triggers at the auto-compact window; on the Anthropic API a 1M-window Sonnet 5 session compacts at about 967K by default.
- Design choice. The harness treats files as authoritative and reloads them, and it reduces the conversation to a summary. The design assumes that you wrote down what matters. / Cost. A long session's detail is gone after compaction; /compact itself is a large request, because it reads what it summarizes. / Failure mode. #5 correction fails: a correction given only in chat survives as the summarizer's paraphrase. / Control points. /compact Focus on …; a 'Compact instructions' section in CLAUDE.md; PreCompact hook (exit 2 blocks); SessionStart with matcher compact re-injects what you choose.
- Claude Code already applies the second rule on slide 3 (write to a file whatever must survive): it reloads files and does not reload the chat. Build the same behavior into your loop deliberately.

## Slide 15

### BEFORE

Codex in three cards. Mechanism: instruction files concatenated root to leaf, closer ones later and therefore stronger, with a thirty-two kilobyte cap, and compaction that on the Responses API produces an encrypted item the client must pass back untouched. The choice trades auditability for state: the provider can carry reasoning forward that a text summary could not, and the price is that neither you nor your Chase can read what was kept. The failure mode is mediated observation. That is why your system keeps its own ledger: if the provider's record of intent is opaque, your evidence has to live in a file you control.

Cut from slide 15 (full wording):
- AGENTS.md files from the Git root down to the working directory, concatenated; closer files come later and override. Reading stops at 32 KiB by default. / /compact summarizes; auto-compaction runs at model_auto_compact_token_limit. On the Responses API, compaction returns an encrypted item the client passes back as is.
- Choice. A hard byte cap on instructions, and compaction done server-side, where the provider keeps reasoning state the client never sees. / Cost. Files past the 32 KiB cap are not read; the deepest, most specific guidance goes first. The compaction item is 'opaque and not intended to be human-interpretable': you cannot audit what it kept.
- Human-side: mediated observation. The Chase cannot read the summary, so a pass after compaction rests on what the model says it remembers. / Design Analysis question. If your record of what was kept is unreadable, where does your evidence of intent live? Answer: your own ledger, not the provider's blob.

### AFTER

Codex in three cards. Mechanism: instruction files concatenated from the root to the working directory, the closer files later and therefore overriding, with a 32 KiB cap; and a compaction that, on the Responses API, produces an encrypted item the client passes back untouched. The choice trades auditability for state: the provider can carry reasoning forward that a text summary could not, and the price is that neither you nor your Chase can read what was kept. The failure mode is mediated observation. For this reason your system keeps its own ledger: if the provider's record of intent is opaque, your evidence of intent has to live in a file you control.

Cut from slide 15 (full wording):
- AGENTS.md files from the Git root down to the working directory, concatenated; closer files come later and override. Reading stops at 32 KiB by default. / /compact summarizes; auto-compaction runs at model_auto_compact_token_limit. On the Responses API, compaction returns an encrypted item the client passes back as is.
- Choice. A hard byte cap on instructions, and compaction done server-side, where the provider keeps reasoning state the client never sees. / Cost. Files past the 32 KiB cap are not read, so the deepest and most specific guidance is the first to be dropped. The compaction item is 'opaque and not intended to be human-interpretable': you cannot audit what it kept.
- Human-side: mediated observation. The Chase cannot read the summary, so a pass after compaction rests on what the model says it remembers. / Design Analysis question. If your record of what was kept is unreadable, where does your evidence of intent live? Answer: in your own ledger, because the provider's compaction item is not human-readable.

## Slide 16

### BEFORE

Cursor's January post is the cleanest statement of a design choice this year: do not throw context away, move it to files and let the agent search. Long outputs, terminals, MCP descriptions, even the chat history during summarization, all become files. The measured gain was about forty-seven percent fewer tokens in runs that used MCP tools. The cost is that recovery depends on the model deciding to look, and the same dependency shows up in Cursor's rules: an intelligently applied rule loads when the model thinks it is relevant. So a must-hold rule in that mode is the wishful rule from your AGENTS.md probes, and the failure is skipped cheap verification.

Cut from slide 16 (full wording):
- Long tool outputs are written to files instead of truncated; terminal sessions sync to files; MCP tool descriptions sync to a folder and the agent sees names first; during summarization the agent can search the chat history as a file.
- Project rules in .cursor/rules as .mdc: Always Apply, Apply Intelligently (by description), Apply to Specific Files (globs), Apply Manually (@-mention). 'Keep rules under 500 lines.' Nested AGENTS.md also applies.
- Choice. Nothing is dropped; it moves to disk and the agent greps for it. 46.9% fewer tokens in runs that called an MCP tool. / Cost. Every recovery is a tool call the model must think to make.
- 'Apply Intelligently' loads a rule only when the model judges it relevant. A rule that must hold on every turn, placed there, is a wishful rule (E5 Probe 2). App. C #4: the model skips the cheap lookup.

### AFTER

Cursor's January post states one design choice: do not discard context, move it to files and let the agent search. Long outputs, terminal sessions, MCP descriptions, and the chat history during summarization all become files. The measured gain was 46.9 percent fewer tokens in runs that used MCP tools. The cost is that recovery depends on the model deciding to look, and the same dependency appears in Cursor's rules: a rule set to Apply Intelligently loads when the model judges it relevant. A rule that must hold on every turn, placed in that mode, is the wishful rule from your E5 AGENTS.md probes, and the failure is Appendix C number four, the cheap verification skipped.

Cut from slide 16 (full wording):
- Long tool outputs are written to files instead of truncated; terminal sessions sync to files; MCP tool descriptions sync to a folder and the agent sees names first; during summarization the agent can search the chat history as a file.
- Project rules in .cursor/rules as .mdc: Always Apply, Apply Intelligently (by description), Apply to Specific Files (globs), Apply Manually (@-mention). 'Keep rules under 500 lines.' Nested AGENTS.md also applies.
- Choice. Cursor drops nothing. It moves long content to disk, and the agent greps for it. 46.9% fewer tokens in runs that called an MCP tool. / Cost. Every recovery is a tool call the model must think to make.
- 'Apply Intelligently' loads a rule only when the model judges it relevant. A rule that must hold on every turn, placed there, is a wishful rule (E5 Probe 2). App. C #4: the model skips the cheap lookup.

## Slide 17

### BEFORE

OpenCode, because it is what you fly. The configuration is three keys in version one: auto, prune, reserved; the version two beta renames them, so check your version before you edit anything. Measurement is weaker than Claude Code's: there is no per-category grid, but the export gives you per-message token counts, and that is enough to compute a budget per turn, which the lab does. Isolation comes from subagents in child sessions. The open question is a good one for your Design Analysis: auto-compaction is keyed to the model's context limit, and Big Pickle does not publish one. Find out what OpenCode assumes; treat any answer the model gives you about its own window as a claim to check.

Cut from slide 17 (full wording):
- Measure. No /context grid. You get the TUI's counters, opencode stats, and opencode export <session-id>, whose JSON carries token counts per assistant message. Tonight's lab computes a per-turn budget from it. / Isolate. Explore and general subagents run in child sessions with their own windows. / Open question. Auto-compaction fires when tokens exceed the model's limit minus its output reserve. For Big Pickle, whose window is unpublished, what limit does OpenCode use? Find out; do not assume.
- A free model with an unpublished window makes the lesson unavoidable: the only budget you can trust is the one you declared and logged.

### AFTER

OpenCode, because it is the harness you fly. The configuration is three keys in version one, auto, prune, and reserved; the version two beta renames them, so check your version before you edit. Measurement is weaker than Claude Code's: there is no per-category grid, but opencode export gives per-message token counts, and that is enough to compute a budget per turn, which the lab does. Isolation comes from the explore and general subagents, which run in child sessions. The open question suits a Design Analysis: auto-compaction is keyed to the model's context limit, and Big Pickle publishes none. Find out what OpenCode assumes, and treat any answer the model gives about its own window as a claim to check against the export.

Cut from slide 17 (full wording):
- Measure. No /context grid. You get the TUI's counters, opencode stats, and opencode export <session-id>, whose JSON carries token counts per assistant message. The Evolution 6 lab computes a per-turn budget from it. / Isolate. Explore and general subagents run in child sessions with their own windows. / Open question. Auto-compaction fires when tokens exceed the model's limit minus its output reserve. For Big Pickle, whose window is unpublished, what limit does OpenCode use? Find out by measurement instead of assuming a value.
- Because Big Pickle's window is unpublished, the only budget you can check is the one you declared and logged.

## Slide 18

### BEFORE

Anthropic's harness for long-running agents, from November. The sentence to remember is theirs: compaction is not sufficient. So they design every session to begin as a stranger and give it a fixed way to catch up: read the git log, read the progress file, run the smoke test, pick one failing feature. The choice of JSON over Markdown for the feature list is a mechanism against metagaming: the model edits prose freely and structured files less. This is Sortie 6 at production scale: a handoff, a resume procedure, and a ledger, which here is git.

Cut from slide 18 (full wording):
- “Compaction isn’t sufficient.” The harness makes every session start as a stranger and gives it a way to catch up.
- Mechanism. An initializer agent writes init.sh, a claude-progress.txt file, a JSON list of 200+ features all marked failing, and a first commit. Every later session checks the directory, reads the git log and the progress file, picks the highest-priority failing feature, runs init.sh to check the basics, works one feature, commits, and updates the progress file. / Choice and cost. JSON, because 'the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files.' One feature per session costs throughput and buys a clean state at every boundary. / Failure mode it defends. App. C #9, metagaming the gate: a model that can edit the checklist can mark a feature passing. The feature list is L1 the model may flip a status on, never rewrite.

### AFTER

Anthropic's harness for long-running agents, from November 2025. The sentence to carry is theirs: compaction is not sufficient. The harness therefore treats every session as a stranger and gives it a fixed way to catch up: read the git log, read the progress file, run the smoke test, pick one failing feature. The choice of JSON over Markdown for the feature list is a mechanism against metagaming, because the model edits prose freely and structured files less. This is Sortie 6 at production scale: a handoff, a resume procedure, and a ledger, which in that harness is git.

Cut from slide 18 (full wording):
- “Compaction isn’t sufficient.” The harness makes every session start as a stranger and gives it a way to catch up.
- Mechanism. An initializer agent writes init.sh, a claude-progress.txt file, a JSON list of 200+ features all marked failing, and a first commit. Every later session checks the directory, reads the git log and the progress file, picks the highest-priority failing feature, runs init.sh to check the basics, works one feature, commits, and updates the progress file. / Choice and cost. JSON, because 'the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files.' Working one feature per session lowers throughput, and in return each session ends in a clean state. / Failure mode it defends. App. C #9, metagaming the gate: a model that can edit the checklist can mark a feature passing. The feature list is L1: the model may change a feature's status but may not rewrite the list.

## Slide 19

### BEFORE

Build this one with me; the second column is a draft and your job is to argue with it. Most of the words go to memory and context, where the mechanism is the reload list, to governance, where two hooks let you control compaction, and to coordination, where subagents are the isolation tool. Then the judgment loop at the bottom: the decision is that files are truth and chat is disposable, it privileges a small fresh window, it costs detail and an expensive compaction request, it leaves correction-fails as the failure mode, and it is preserved by the documented reload list and the hooks. Your Sprint Design Analysis does the same for one of the four harnesses.

Cut from slide 19 (full wording):
- CLAUDE.md hierarchy (and AGENTS.md); auto memory (first 200 lines or 25KB); /context; /compact [focus]; files reload after compaction, chat does not
- Judgment loop on the board: Decision (files reload, chat is summarized) · Characteristics privileged (a small, fresh window) · Cost (detail; an expensive compaction call) · Failure mode (#5) · Preservation mechanism (the reload list; the hooks).

### AFTER

Build this analysis in class; the second column is a draft, and your job is to argue with it. The components with the most to say are memory and context, where the mechanism is the reload list; governance, where two hooks let you control compaction; and coordination, where subagents are the isolation tool. The judgment loop at the bottom reads as follows. The decision is that files are truth and chat is disposable. The characteristic privileged is a small fresh window. The cost is detail and an expensive compaction request. The failure mode left open is correction fails. The preservation mechanism is the documented reload list and the hooks. Your Sprint Design Analysis does the same for one of the four harnesses.

Cut from slide 19 (full wording):
- CLAUDE.md hierarchy (and AGENTS.md); auto memory (first 200 lines or 25KB); /context; /compact [focus]; files reload after compaction, chat does not
- Judgment loop on the board: Decision (files reload, chat is summarized) · Characteristics privileged (a small, fresh window) · Cost (detail; an expensive compaction call) · Failure mode (#5) · Preservation mechanism (the reload list; the hooks).

## Slide 20

### BEFORE

The reference design's version of tonight. The state doctrine names the three layers and the precedence, and its one-line summary is the one to quote in your README: frontmatter can lie, the ledger is the truth. On the right, the machinery: a handoff command with the seven sections, a rulings store kept as append-only JSON lines, and a session-orientation script that runs before the first turn. The count of a hundred and sixteen handoffs by June is from the casebook's utter-shambles entry and is a warning as much as a feature: handoffs accumulate, and a pile of them is its own context problem. Verify the ADR number and the paths against the repository before class.

Cut from slide 20 (full wording):
- L1 canon: Markdown (ADRs, briefs, rules, AGENTS.md). / L2 ledger: append-only events; the runtime truth. / L3 derived: status views, markers, frontmatter. / Precedence L2 > L1 > L3. L3 can never block a gate. / 'Frontmatter can lie; the ledger is the truth.' / The Design Analysis question for your system: which of your files is L3 and currently treated as truth?
- gz handoff create / resume: the seven-section handoff. / .gzkit/handoffs/rulings.jsonl: settled rulings as append-only records. / scripts/session_orientation.py: what a session reads before turn one. / By 2026-06-20 the repository held 116 handoffs; the 'utter shambles' audit counted them. / [Verify ADR numbers, file paths, and commands against the repository before class.]

Instructor checks moved off the slide:
- [Verify ADR numbers, file paths, and commands against the repository before class.]

### AFTER

The reference design's version of this Evolution. The state doctrine defines the three layers and the precedence, and its one-line summary is the sentence to quote in your README: frontmatter can lie, the ledger is the truth. The right panel lists the machinery: a handoff command with the seven sections, a rulings store kept as append-only JSON lines, and a session-orientation script that runs before the first turn. The count of 116 handoffs by June 2026 comes from the casebook's 'utter shambles' entry, and it is a warning as much as a feature: handoffs accumulate, and a pile of them is itself a context problem.

Cut from slide 20 (full wording):
- L1 canon: Markdown (ADRs, briefs, rules, AGENTS.md). / L2 ledger: append-only events; the runtime truth. / L3 derived: status views, markers, frontmatter. / Precedence L2 > L1 > L3. L3 can never block a gate. / 'Frontmatter can lie; the ledger is the truth.' / The Design Analysis question for your system: which of your files is L3 and currently treated as truth?
- gz handoff create / resume: the seven-section handoff. / .gzkit/handoffs/rulings.jsonl: settled rulings as append-only records. / scripts/session_orientation.py: what a session reads before turn one. / By 2026-06-20 the repository held 116 handoffs; the 'utter shambles' audit counted them. / [Verify ADR numbers, file paths, and commands against the repository before class.]

Instructor checks moved off the slide:
- [Verify ADR numbers, file paths, and commands against the repository before class.]

## Slide 21

### BEFORE

The incident Chapter 15 is built around. A session oriented itself on a clone that was ten commits behind; the reconciliation was a hard reset and about two hundred fifteen lines were lost. The mechanism that resulted is small and exactly right: at session start, report ahead and behind before any work, and make orientation state how fresh it is. For your build the translation is one line in the resume procedure: the handoff names a commit, and the fresh session checks where the tree is relative to it before its first action. Verify the numbers against the casebook before class.

Cut from slide 21 (full wording):
- What happened. A session worked from a local clone ten commits behind its remote. Reconciling it with a hard reset discarded about 215 lines. / What resulted. A SessionStart check that reports ahead/behind before any work, and a freshness rule for orientation: the session states how current its picture is. / For your system. Your handoff names a commit. The resume step checks that the working tree is at that commit, or says how far it has moved, before the first action.

Instructor checks moved off the slide:
- [Verify the date, counts, and hook name against the repository before class.]

### AFTER

Chapter 15 is built around this incident. A session oriented itself on a clone ten commits behind its remote; a hard reset reconciled the clone and discarded about 215 lines. The mechanism that resulted is small: at session start, report ahead and behind before any work, and make orientation state how fresh its picture is. For your build the translation is one line in the resume procedure: the handoff records a commit, and the fresh session checks where the working tree sits relative to that commit before its first action.

Cut from slide 21 (full wording):
- What happened. A session worked from a local clone ten commits behind its remote. Reconciling it with a hard reset discarded about 215 lines. / What resulted. A SessionStart check that reports ahead/behind before any work, and a freshness rule for orientation: the session states how current its picture is. / For your system. Your handoff records a commit. The resume step checks that the working tree is at that commit, or says how far it has moved, before the first action.

Instructor checks moved off the slide:
- [Verify the date, counts, and hook name against the repository before class.]

## Slide 22

### BEFORE

Three more episodes, briefly. In August an agent put three rulings the operator had already made back to the operator as multiple choice; the rule that came out is that a settled question is a drift vector, and the fix is a store that loads at start. In May four questions went to the operator in one prompt, and the rule is economy of the human's effort, which is also the measure of your fresh session: it should ask nothing the handoff answered. And AGENTS.md as a derived view, rendered and trusted least, which closes the loop with last week's exhaustion. Verify the ADR numbers.

Cut from slide 22 (full wording):
- AGENTS.md rendered from the corpus (ADR-0.0.37), with the 'lowest amount of faith in AGENTS.md'; map, not encyclopedia (ADR-0.0.54) after the 258K exhaustion in E5.
- An agent re-elicited three settled rulings from the operator by multiple choice. Rule: 'A settled question is a drift vector.' Settled answers live in the rulings store and load at session start.
- Four questions bundled into one prompt to the operator. Result: operator economy of effort, one question at a time, and only questions the record cannot answer.

Instructor checks moved off the slide:
- [Verify ADR numbers before class.]

### AFTER

Three more episodes. In August 2026 an agent put three rulings the operator had already made back to the operator as multiple choice; the rule that came out is that a settled question is a drift vector, and the fix is a rulings store that loads at session start. In May 2026 four questions went to the operator in one prompt; the rule is economy of the operator's effort, which is also the measure of your fresh session: it asks nothing the handoff answered. The third episode is AGENTS.md as a derived view, rendered from the corpus and trusted least, which connects to the 258K exhaustion in E5.

Cut from slide 22 (full wording):
- AGENTS.md rendered from the corpus (ADR-0.0.37), with the 'lowest amount of faith in AGENTS.md'; map, not encyclopedia (ADR-0.0.54) after the 258K exhaustion in E5.
- An agent re-elicited three settled rulings from the operator by multiple choice. Rule: 'A settled question is a drift vector.' Settled answers live in the rulings store and load at session start.
- Four questions bundled into one prompt to the operator. Result: operator economy of effort, one question at a time, and only questions the record cannot answer.

Instructor checks moved off the slide:
- [Verify ADR numbers before class.]

## Slide 23

### BEFORE

Weak: a size where a per-turn count belongs, a default compaction with no record, a diary for a handoff, a transcript pasted in, and a README that says ledger with no path. Sound: a budget record every turn from the provider's own fields; compaction that keeps what you declared and logs what it did; seven sections with an action first; a fresh session that does what you named and asks nothing you answered; three layers declared and a stale view that loses. Exceptional: the budget by category with one category cut, the summary audited against the ledger, a handoff derived from the ledger, a ruling that stays settled, and a second model family resuming from the same file. That last one is cheap if you have a Go subscription; with Big Pickle alone, say so and skip it.

Cut from slide 23 (full wording):
- Budget reported as file size or one session total / Compaction left at the harness default; no event, no keep list / Handoff is a paragraph: no next action, no names on decisions / Resume 'tested' by pasting the old transcript / README says 'the ledger is the truth' with no paths and no precedence
- One budget record per turn from provider usage fields, against a declared budget / Compaction with a declared keep list; an event with tokens before and after / Seven-section handoff; the first next step is one action / Fresh session's first action matches; no question the handoff answered / L1/L2/L3 declared with paths; a planted stale L3 view loses to the ledger
- Budget broken down by category; one category cut, with before and after numbers / Compaction summary checked against the ledger; a dropped decision found and pinned / Handoff generated from the ledger (L3 of L2) and checked for fidelity / A settled ruling stays settled: B does not re-ask it / Same handoff resumed on a second model family, with the difference explained

### AFTER

Weak: a size where a per-turn count belongs, a default compaction with no record, a diary for a handoff, a transcript pasted in, and a README that says ledger with no path. Sound: a budget record every turn from the provider's own fields; compaction that keeps what you declared and logs what it did; seven sections with an action first; a fresh session that takes the action you listed and asks nothing you answered; three layers declared with paths, and a planted stale view that loses to the ledger. Exceptional: the budget by category with one category cut, the summary audited against the ledger, a handoff derived from the ledger, a ruling that stays settled, and a second model family resuming from the same file. The last item costs little with a Go subscription; with Big Pickle alone, state that and skip it.

Cut from slide 23 (full wording):
- Budget reported as file size or one session total / Compaction left at the harness default; no event, no keep list / Handoff is a paragraph: no next action, no names on decisions / Resume 'tested' by pasting the old transcript / README says 'the ledger is the truth' with no paths and no precedence
- One budget record per turn from provider usage fields, against a declared budget / Compaction with a declared keep list; an event with tokens before and after / Seven-section handoff; the first next step is one action / Fresh session's first action matches; no question the handoff answered / L1/L2/L3 declared with paths; a planted stale L3 view loses to the ledger
- Budget broken down by category; one category cut, with before and after numbers / Compaction summary checked against the ledger; a dropped decision found and pinned / Handoff generated from the ledger (L3 of L2) and checked for fidelity / A settled ruling stays settled: B does not re-ask it / Same handoff resumed on a second model family, with the difference explained

## Slide 24

### BEFORE

Card six, back to expansion after last week's corner. Five test points: a budget record on every call, a compaction that logs itself and keeps what you declared, a handoff with a hash, a fresh session that takes the named action and asks nothing already answered, and a stale derived view that loses to the ledger. To force test point two inside one session, set a low turn budget for the sortie, for example eight or sixteen thousand tokens, and say so on the card. The falsifiers include the two shortcuts: pasting the transcript, and fixing the handoff after the fresh session has started. Go is asynchronous this term: your Chase signs the card in the repository by Monday night, and you do not fly before that signature.

Cut from slide 24 (full wording):
- ENVELOPE            expansion / DESIGN CLAIM        A handoff written at session end lets a fresh session resume with no loss of intent: /                     the fresh session's first action is the one the handoff named. / SYSTEMS UNDER TEST  budget meter · compactor + keep list · handoff writer · resume loader · runtime ledger /                     · layers-of-truth declaration (README) / SUBSTRATE           repo + commit · model/route + declared turn budget · harness + version / DEPENDS ON          Sortie 5 PASS (server hardened; AGENTS.md under budget and measured) /  / TEST POINTS /   1  session A runs a bounded task, >= 6 turns   → one turn_budget record per call {turn, in, out, total, budget} /   2  context crosses the compaction threshold     → compaction event {before, after, kept[]}; objective and L1 /                                                      pointers present after; task continues /   3  session A ends                               → handoff.md (7 sections) + handoff_written event with hash /   4  fresh session B loads handoff + L1 + ledger  → first action == handoff NEXT STEP 1; zero questions the /      (no transcript)                                 handoff answered; session_resumed event /   5  planted stale L3 view contradicts ledger     → B follows the ledger; conflict logged; L3 blocks nothing /  / INSTRUMENTATION     budget log (every call) · ledger diff (compaction, handoff_written, session_resumed) /                     · handoff.md + hash · B's first two turns captured verbatim /  / PRE-REGISTERED FALSIFIERS (any ONE ⇒ FAIL) /   - B asks a question the handoff answered, or takes a first action the handoff did not name /   - an L3 view contradicts the ledger and wins /   - any call with no budget record, or a compaction with no event /   - passing by pasting A's transcript into B, or by editing the handoff after B starts /  / ABORT (halt-not-fail)  provider returns no usage fields and no fallback count declared; model unavailable / CHASE               reads budget log, ledger diff, handoff.md, B's first two turns; never the author's summary / GO/NO-GO            Chase signs GO in the repo by Mon 10/12 11:59 p.m.; no sortie before GO /  / SPRINT (due Wed 10/14)  Sortie 6 log · budget + compaction + handoff + ledger · layers in README · DA · AI_LOG

### AFTER

Card six returns to the expansion envelope after the corner in E5. Five test points: a budget record on every call, a compaction that logs itself and keeps what you declared, a handoff with a hash, a fresh session that takes the listed action and asks nothing already answered, and a stale derived view that loses to the ledger. To force test point two inside one session, set a low turn budget for the sortie, eight or sixteen thousand tokens for example, and state it on the card. The falsifiers include the two shortcuts: pasting the transcript, and editing the handoff after the fresh session has started. Go is asynchronous this term: your Chase signs the card in the repository by the date in the course calendar, and you do not fly before that signature.

Cut from slide 24 (full wording):
- ENVELOPE            expansion / DESIGN CLAIM        A handoff written at session end lets a fresh session resume with no loss of intent: /                     the fresh session's first action is the handoff's first next step. / SYSTEMS UNDER TEST  budget meter · compactor + keep list · handoff writer · resume loader · runtime ledger /                     · layers-of-truth declaration (README) / SUBSTRATE           repo + commit · model/route + declared turn budget · harness + version / DEPENDS ON          Sortie 5 PASS (server hardened; AGENTS.md under budget and measured) /  / TEST POINTS /   1  session A runs a bounded task, >= 6 turns   → one turn_budget record per call {turn, in, out, total, budget} /   2  context crosses the compaction threshold     → compaction event {before, after, kept[]}; objective and L1 /                                                      pointers present after; task continues /   3  session A ends                               → handoff.md (7 sections) + handoff_written event with hash /   4  fresh session B loads handoff + L1 + ledger  → first action == handoff NEXT STEP 1; zero questions the /      (no transcript)                                 handoff answered; session_resumed event /   5  planted stale L3 view contradicts ledger     → B follows the ledger; conflict logged; L3 blocks nothing /  / INSTRUMENTATION     budget log (every call) · ledger diff (compaction, handoff_written, session_resumed) /                     · handoff.md + hash · B's first two turns captured verbatim /  / PRE-REGISTERED FALSIFIERS (any ONE ⇒ FAIL) /   - B asks a question the handoff answered, or takes a first action the handoff did not list /   - an L3 view contradicts the ledger and wins /   - any call with no budget record, or a compaction with no event /   - passing by pasting A's transcript into B, or by editing the handoff after B starts /  / ABORT (halt-not-fail)  provider returns no usage fields and no fallback count declared; model unavailable / CHASE               reads budget log, ledger diff, handoff.md, B's first two turns; never the author's summary / GO/NO-GO            Chase signs GO in the repo; no sortie before GO /  / SPRINT              Sortie 6 log · budget + compaction + handoff + ledger · layers in README · DA · AI_LOG

## Slide 25

### BEFORE

The lab, which you run on your own at six. It is Sortie 6 at small scale in the harness you already have: fly a short read-only session, export it, compute the budget per turn with the ten-line script in the handout, write a handoff by hand, and see whether a fresh session takes the action you named. One step uses the model as a witness against itself: ask it how full its context is and compare with the export; small free models will guess, and the guess is the lesson. Commit the table, the handoff, and the resume check, not the raw export, which holds your file contents. The Sprint puts the same meter inside your own agent loop.

Cut from slide 25 (full wording):
- Lab tonight (6:00–6:30, self-guided): measure a session, resume it
- 0–3   Set up evolution-06/lab/; record opencode --version and the model id; declare a turn budget. / 3–10  Fly session A: a bounded, read-only task in your repo, five or six turns. Ask the model how many tokens its context holds; write the claim down. / 10–17 Measure: opencode export <id> to a local file; run budget.py; per-turn table; compare the model's claim with the export. Fallback: read the TUI counter by hand each turn. / 17–25 Write handoff.md by hand, seven sections, first next step one action. / 25–29 Fresh session B (/new): it reads only the handoff and states its first action and its questions. Match or no match. / 29–30 Commit; ledger event.
- evolution-06/lab/budget.md: the per-turn table, your declared budget, turns over budget. / evolution-06/lab/handoff.md. / evolution-06/lab/resume-check.md: B's first action and questions, verbatim, and your verdict. / One line: the model's claim about its context against the measured number. / Do not commit the raw export; it contains file contents. Commit the table.

### AFTER

The lab, which you run on your own. It is Sortie 6 at small scale in the harness you already have: fly a short read-only session, export it, compute the budget per turn with the script in the handout, write a handoff by hand, and see whether a fresh session takes the action you listed. One step uses the model as a witness against itself: ask it how full its context is and compare the answer with the export. A small free model guesses, and the gap between the guess and the export is the lesson. Commit the table, the handoff, and the resume check. Do not commit the raw export, because it holds your file contents. The Sprint puts the same meter inside your own agent loop.

Cut from slide 25 (full wording):
- Lab (self-guided): measure a session, then resume it
- Set up evolution-06/lab/. Record opencode --version and the model id. Declare a turn budget. / Fly session A: a bounded, read-only task in your repo, five or six turns. Ask the model how many tokens its context holds, and write its answer down. / Measure: export with opencode export <id> to a local file. Run budget.py to build the per-turn table. Compare the model's answer with the export. Fallback: read the TUI counter by hand each turn. / Write handoff.md by hand, in seven sections, with a first next step that is one action. / Start fresh session B (/new). It reads only the handoff and states its first action and its questions. Record match or no match. / Commit, and append a ledger event.
- evolution-06/lab/budget.md: the per-turn table, your declared budget, turns over budget. / evolution-06/lab/handoff.md. / evolution-06/lab/resume-check.md: B's first action and questions, verbatim, and your verdict. / One line: the model's stated token count against the measured number. / Do not commit the raw export, because it contains file contents. Commit the table.

## Slide 26

### BEFORE

The Sprint in three cards. What you hand in is the run sheet's list: the log, the four mechanisms plus the ledger with tests, the layers in your README, a Design Analysis of one of tonight's four harnesses, and your AI log. Go and No-Go move out of the classroom: commit the card by Sunday, and your Chase signs in the repository by Monday night. After you fly, the Chase reads the evidence slice, never your narrative, and writes a one-line verdict by Thursday noon. The strip is the distinction to keep: a fail disproves the claim; an abort means the flight did not happen for a reason outside the claim.

Cut from slide 26 (full wording):
- Homework: the Sprint, due Wed 10/14, 11:59 p.m.
- Sortie 6 flight log / Budget meter, compactor with keep list, handoff writer, resume loader, runtime ledger, with tests / README: layers of truth, with paths and precedence / Design Analysis: Claude Code, Codex, Cursor, or OpenCode context system / AI_LOG entry
- Commit evolution-06/flight-card.md by Sun 10/11. Your Chase reads it and signs GO or NO-GO with one reason by Mon 10/12 11:59 p.m. No signature, no sortie. A NO-GO names the field to fix; you amend and ask again.
- The Chase reads the budget log, the ledger diff, handoff.md, and B's first two turns, and nothing you wrote about them. One-line verdict, PASS or FAIL with the falsifier quoted, by Thu 10/15 noon.
- FAIL is the claim disproved. ABORT is the flight not flown for a reason unrelated to the claim. Log both honestly.

### AFTER

The Sprint in three cards. You hand in the log, the four mechanisms plus the ledger with tests, the layers in your README, a Design Analysis of one of the four harnesses, and your AI log. Go and No-Go move out of the classroom: commit the card by the date in the course calendar, and your Chase signs in the repository. After you fly, the Chase reads the evidence slice and never your narrative, and writes a one-line verdict with the falsifier quoted. The strip at the bottom holds the distinction to keep: FAIL means the sortie disproved the design claim; ABORT means the flight did not happen for a reason outside the claim.

Cut from slide 26 (full wording):
- Homework: the Sprint
- Sortie 6 flight log / Budget meter, compactor with keep list, handoff writer, resume loader, runtime ledger, with tests / README: layers of truth, with paths and precedence / Design Analysis: Claude Code, Codex, Cursor, or OpenCode context system / AI_LOG entry
- Commit evolution-06/flight-card.md. Your Chase reads it and signs GO or NO-GO with one reason. Without a signature, you do not fly the sortie. A NO-GO identifies the field to fix. Amend the card and ask again.
- The Chase reads the budget log, the ledger diff, handoff.md, and B's first two turns, and nothing you wrote about them. One-line verdict, PASS or FAIL with the falsifier quoted.
- FAIL means the flight card's claim was disproved. ABORT means the flight was not flown, for a reason unrelated to that claim. Record either outcome in the flight log.

## Slide 27

### BEFORE

Close. Intent that lives only in the window dies with the window. Measure every turn, decide what compaction may lose before it runs, and write the handoff for a stranger. Lab at six. Sources checked 09/24/2026: Anthropic, Effective context engineering for AI agents (Sep 29, 2025), https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents ; Anthropic, Effective harnesses for long-running agents (Nov 26, 2025), https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents ; Anthropic, Managing context on the Claude Developer Platform, https://www.anthropic.com/news/context-management ; Claude Code docs: https://code.claude.com/docs/en/costs , https://code.claude.com/docs/en/commands , https://code.claude.com/docs/en/model-config , https://code.claude.com/docs/en/hooks , https://code.claude.com/docs/en/memory , https://code.claude.com/docs/en/context-window , https://code.claude.com/docs/en/sub-agents ; OpenAI: https://developers.openai.com/api/docs/guides/compaction , https://developers.openai.com/codex/cli/slash-commands , https://developers.openai.com/codex/config-sample , https://learn.chatgpt.com/docs/agent-configuration/agents-md ; Cursor: https://cursor.com/blog/dynamic-context-discovery , https://cursor.com/docs/context/rules ; OpenCode: https://opencode.ai/docs/config/ , https://opencode.ai/docs/tui/ , https://opencode.ai/docs/cli/ , https://opencode.ai/docs/agents/ , https://opencode.ai/docs/skills/ , https://opencode.ai/v2/docs/compaction , https://github.com/anomalyco/opencode/releases , https://github.com/anomalyco/opencode/issues/30649 , https://opencode.ai/docs/go/ ; Chroma, Context Rot (Jul 14, 2025), https://www.trychroma.com/research/context-rot ; Liu et al., Lost in the Middle, TACL 2024, https://aclanthology.org/2024.tacl-1.9/ ; LangChain, Context engineering for agents (Jul 2, 2025), https://www.langchain.com/blog/context-engineering-for-agents . gzkit items come from the course topic guide and must be verified against the repository.

Cut from slide 27 (full wording):
- Measure every turn, decide what compaction may lose before it runs, and hand off to a stranger. Lab at six: measure one session and resume it from your own handoff.

### AFTER

Close. Intent kept only in the window is lost at the next compaction or the next session. Measure every turn, decide what compaction may lose before it runs, and write the handoff for a stranger. Sources checked 09/24/2026: Anthropic, Effective context engineering for AI agents (Sep 29, 2025), https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents ; Anthropic, Effective harnesses for long-running agents (Nov 26, 2025), https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents ; Anthropic, Managing context on the Claude Developer Platform, https://www.anthropic.com/news/context-management ; Claude Code docs: https://code.claude.com/docs/en/costs , https://code.claude.com/docs/en/commands , https://code.claude.com/docs/en/model-config , https://code.claude.com/docs/en/hooks , https://code.claude.com/docs/en/memory , https://code.claude.com/docs/en/context-window , https://code.claude.com/docs/en/sub-agents ; OpenAI: https://developers.openai.com/api/docs/guides/compaction , https://developers.openai.com/codex/cli/slash-commands , https://developers.openai.com/codex/config-sample , https://learn.chatgpt.com/docs/agent-configuration/agents-md ; Cursor: https://cursor.com/blog/dynamic-context-discovery , https://cursor.com/docs/context/rules ; OpenCode: https://opencode.ai/docs/config/ , https://opencode.ai/docs/tui/ , https://opencode.ai/docs/cli/ , https://opencode.ai/docs/agents/ , https://opencode.ai/docs/skills/ , https://opencode.ai/v2/docs/compaction , https://github.com/anomalyco/opencode/releases , https://github.com/anomalyco/opencode/issues/30649 , https://opencode.ai/docs/go/ ; Chroma, Context Rot (Jul 14, 2025), https://www.trychroma.com/research/context-rot ; Liu et al., Lost in the Middle, TACL 2024, https://aclanthology.org/2024.tacl-1.9/ ; LangChain, Context engineering for agents (Jul 2, 2025), https://www.langchain.com/blog/context-engineering-for-agents . gzkit items come from the course topic guide and must be verified against the repository.

Cut from slide 27 (full wording):
- Measure every turn, decide what compaction may lose before it runs, and hand off to a stranger. In the lab, measure one session and resume it from your own handoff.

