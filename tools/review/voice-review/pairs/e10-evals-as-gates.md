# e10-evals-as-gates: speaker notes, before and after the voice pass

## Slide 1

### BEFORE

Evolution 10. Last week an adversary from another model family refuted a planted falsehood, and the receipt went in the log. Tonight we turn that move on our own checks. The framing sentence: evaluation is falsification. A check that has never failed tells you nothing about the code it covers. Survey: the agent benchmarks the field has used since 2023, read for what their graders actually check, and what happened to several of them in 2026. Build: a golden set, a regression delta, and a RED witness, wired to a gate that exits non-zero. The lab at six is self-guided and small; the full test points fly in the Sprint, due Wednesday 11/11.

Cut from slide 1 (full wording):
- Evolution 10 · Lecture · Thu 11/05
- Golden sets, regression deltas, judges and their biases, the RED witness, and pre-registration; what SWE-bench, GAIA, WebArena, AgentBench, and τ-bench measure, and what they hide
- CIDM 6333 · Agentic Systems Design and Development · 4:00–6:00 · CC209 / Survey: SWE-bench (and Verified, Pro), GAIA, WebArena, AgentBench, τ-bench and τ²-bench; LLM-as-judge; the 2026 benchmark breaks · Build: a golden set, a regression delta, and a RED witness wired to a gate (lab 6:00–6:30, self-guided)

### AFTER

Evolution 10. In Sortie 9 an adversary from another model family refuted a planted falsehood, and the receipt went in the log. This Evolution turns the same procedure on your own checks: you plant a falsehood in your own suite and ask whether the suite catches it. The framing sentence is that evaluation is falsification. A check that has never failed tells you nothing about the code it covers, because a check that cannot fail produces the same green light. The survey covers the agent benchmarks the field has used since 2023, read for what their graders check, and what happened to several of them in 2026. The build is a golden set, a regression delta, and a RED witness, wired to a gate that exits non-zero. The lab is self-guided and small; the full test points fly in the Sprint.

Cut from slide 1 (full wording):
- Evolution 10 · Lecture
- Golden sets, regression deltas, judges and their biases, the RED witness, and pre-registration; what SWE-bench, GAIA, WebArena, AgentBench, and τ-bench measure, and what they hide
- CIDM 6333 · Agentic Systems Design and Development / Survey: SWE-bench (and Verified, Pro), GAIA, WebArena, AgentBench, τ-bench and τ²-bench; LLM-as-judge; the 2026 benchmark breaks · Build: a golden set, a regression delta, and a RED witness wired to a gate (self-guided lab)

## Slide 2

### BEFORE

Eight minutes of framing, forty of spine, five on the common mistake, a five-minute break at 0:55, thirty minutes of teardowns, fifteen on the reference design, then the lens, the card, and the lab and Sprint brief. The spine is long tonight because each of its parts is a thing you will build this week: a golden set, a delta, a gate, a judge check, a RED witness, and a pre-registered card. There is no in-class Go/No-Go; your Chase signs the card in the repository before you fly.

Cut from slide 2 (full wording):
- The benchmarks and their graders; SWE-bench Verified retired; the 2026 breaks; MT-Bench as a judge system; Design Analysis of τ²-bench; gzkit eval runner
- Lab 6:00–6:30 (self-guided); Sprint due Wed 11/11; async Go/No-Go and Chase

### AFTER

The lecture runs in eight parts: framing, the spine, the common mistake, the teardowns, the reference design, the evaluation lens, Flight Card 10, and the lab and Sprint brief. The spine is the longest part because each of its sections is a thing you build in this Evolution: a golden set, a delta, a gate, a judge check, a RED witness, and a pre-registered card. There is no in-class Go/No-Go; your Chase signs the card in the repository before you fly.

Cut from slide 2 (full wording):
- The benchmarks and their graders; SWE-bench Verified retired; the 2026 breaks; MT-Bench as a judge system; Design Analysis of τ²-bench; gzkit eval runner
- Self-guided lab; the Sprint; async Go/No-Go and Chase

## Slide 3

### BEFORE

Framing. Most of you have tests, and most of those tests have only ever been green. A green test that has never been red is a claim about the test. Two rules. First, a check counts only after you have seen it fail with the behavior removed; that is the RED witness, and gzkit's glossary defines it as proof that a test fails without the change it covers. Second, you write down what would count as failure before you look at any result; that is pre-registration, and it is what your flight cards have been since E1. Tonight's claim is the chapter's Sortie 10 claim. Its three falsifiers are the three ways an evaluation suite lies, and the fourth line is the rule the reference design learned: passing by moving the goalposts is a fail.

Cut from slide 3 (full wording):
- Rule one: a check counts only after it has been seen red. Remove the behavior it covers, run it, watch it fail, restore. That is the RED witness. / Rule two: the falsifier is written before the evidence exists. Threshold, cases, and the removal diff are committed before the first run. That is pre-registration.
- Your evaluation suite fails when it should: removing the feature, or planting a wrong answer, turns the gate red. / Three observations falsify it: a green gate with the feature removed; a judge that scores a planted error as correct; a golden case that cannot fail. A pass obtained by editing the golden set or the threshold after the first run is a FAIL, not a pass.

### AFTER

Framing. A test that has only ever been green has shown that it runs and nothing more, because a test that cannot fail produces the same green record as a test that can. Two rules follow. First, a check counts only after you have seen it fail with the behavior it covers removed; gzkit's glossary calls this the RED witness and defines it as proof that a test fails without the change it covers. Second, you write down what would count as failure before you look at any result; this is pre-registration, and your flight cards have done it since E1. The design claim for this Evolution is the chapter's Sortie 10 claim: the suite fails when it should. Its three falsifiers are the three ways an evaluation suite can report a pass it did not earn, and the fourth line is the rule the reference design learned in June: a pass obtained by moving the goalposts is a FAIL.

Cut from slide 3 (full wording):
- Rule one (the RED witness): a check counts only after you have seen it go red. Remove the behavior it covers, run the check, watch it fail, and restore the behavior. / Rule two (pre-registration): write the falsifier before the evidence exists. Commit the threshold, the cases, and the removal diff before the first run.
- Your evaluation suite fails when it should: removing the feature, or planting a wrong answer, turns the gate red. / Three observations falsify it: a green gate with the feature removed; a judge that scores a planted error as correct; a golden case that cannot fail. A pass obtained by editing the golden set or the threshold after the first run counts as a FAIL.

## Slide 4

### BEFORE

Six words. Task, trial, grader, transcript, and outcome are Anthropic's vocabulary from its January 2026 engineering post on agent evals; I use them because they separate things people blur. A task is the case; a trial is one attempt; the grader scores it; the transcript is how the agent got there; the outcome is the state it left behind. Their advice is to grade the outcome, not the path, because agents find valid routes you did not anticipate. The sixth word is ours: a gate is a grader whose result stops something. An eval that prints a percentage and lets the commit through is a report, and reports get ignored at eleven at night.

Cut from slide 4 (full wording):
- One input with a stated success criterion. In a golden set, one line of JSONL with an id, the input, the check, and the expected value.
- One attempt at one task. Model outputs vary between trials, so a task with a model in the loop is run more than once.
- The logic that scores a trial: code (equals, contains, schema, a test), a model with a rubric, or a human. One task can carry several graders.
- The full record of a trial: messages, tool calls, intermediate results. Read transcripts; a score without them hides how the agent got there.
- The state of the environment after the trial: the row in the database, the file on disk. Grade the outcome where you can, not the path.
- Our addition. The grader's result wired to a command that exits non-zero and stops the build, the commit, or the release. An eval that only prints a number is a report.
- Vocabulary from Anthropic, 'Demystifying evals for AI agents' (Jan 9, 2026). Code graders are fast, cheap, and reproducible; model graders are flexible and biased; humans calibrate both.

### AFTER

Six words. Task, trial, grader, transcript, and outcome are Anthropic's vocabulary from its January 2026 engineering post on agent evals. I use them because each one points at a different object, and a log that uses one word for two of them cannot be read. A task is the case; a trial is one attempt at it; the grader scores the trial; the transcript is the record of how the agent got there; the outcome is the state the agent left behind. Anthropic's advice is to grade the outcome rather than the path, because an agent can reach a correct outcome by a valid route the task author did not anticipate. The sixth word is the course's own: a gate is a grader whose result stops something, in other words a grader wired to a command that exits non-zero. An eval that prints a percentage and lets the commit through is a report, and nothing in the build depends on anyone reading a report.

Cut from slide 4 (full wording):
- One input with a stated success criterion. In a golden set, one line of JSONL with an id, the input, the check, and the expected value.
- One attempt at one task. Model outputs vary between trials, so run a task with a model in the loop more than once.
- The logic that scores a trial: code (equals, contains, schema, a test), a model with a rubric, or a human. One task can carry several graders.
- The full record of a trial: messages, tool calls, intermediate results. Read transcripts. A score alone hides how the agent reached its result.
- The state of the environment after the trial: the row in the database, the file on disk. Where you can, grade the outcome instead of the path.
- The course's addition. The grader's result wired to a command that exits non-zero and stops the build, the commit, or the release. An eval that only prints a number stops nothing, so the course counts it as a report.
- Vocabulary from Anthropic, 'Demystifying evals for AI agents' (Jan 9, 2026). Code graders are fast, cheap, and reproducible. Model graders are flexible and biased. Humans calibrate both.

## Slide 5

### BEFORE

A golden set is a small set of cases you trust enough to stop the build on. The left panel is the format I recommend: one JSON object per line, an id, the requirement it covers, the input, the check, and the expected value. Three check types: equals for anything with one right answer, refused for the must-say-no cases, and judge for open answers, with the rubric in a file. The rules on the right: draw cases from your failures in AI_LOG, not from your successes; tie each to a requirement; make a third of them negatives; keep it small enough that you read every failure; freeze it; and prefer code checks. The judge line is last on purpose.

Cut from slide 5 (full wording):
- Source. Cases come from AI_LOG and flight-log failures, not from what the system already does well. / Coverage. Every case names the requirement it covers. A requirement with no case is untested; a case with no requirement is noise. / Negatives. At least a third are must-refuse or must-halt cases. An agent that says yes to everything passes a set of positives. / Size. 10–30 cases for a course system. Enough to cover each requirement twice; small enough to read every failure. / Frozen. Changing a case after a run needs a ledger event and a reason. A case edited to pass is metagaming (App. C #9). / Deterministic first. Use code checks wherever the answer is checkable; send only the rest to a judge.

### AFTER

A golden set is a small set of cases you trust enough to stop the build on. The left panel shows the format I recommend: one JSON object per line, with an id, the requirement it covers, the input, the check, and the expected value. The format has three check types: equals for anything with one right answer, refused for the must-say-no cases, and judge for open answers, with the rubric in a file. The rules on the right follow from the purpose of the set. Draw cases from your failures in AI_LOG rather than from your successes, because a case the system already passes tests nothing. Tie each case to a requirement. Make a third of them negatives, because an agent that says yes to everything passes a set of positives. Keep the set small enough that you read every failure. Freeze it. Prefer code checks, and send to a judge only what code cannot check, which is why the judge line is last.

Cut from slide 5 (full wording):
- Source. Cases come from AI_LOG and flight-log failures instead of from what the system already does well. / Coverage. Every case cites the requirement it covers. A requirement with no case is untested. A case with no requirement measures nothing the system is required to do. / Negatives. At least a third are must-refuse or must-halt cases. An agent that says yes to everything passes a set made only of positives. / Size. 10–30 cases for a course system. That count covers each requirement twice and keeps the failures few enough to read every one. / Frozen. To change a case after a run, record a ledger event and a reason. A case edited to pass is metagaming (App. C #9). / Deterministic first. Use code checks wherever the answer is checkable. Send only the rest to a judge.

## Slide 6

### BEFORE

One run is an anecdote. τ-bench, from Yao, Shinn, Razavi, and Narasimhan in June 2024, introduced pass^k: the probability that all k trials of a task succeed. GPT-4o succeeded on fewer than half the tasks, and in the retail domain fewer than a quarter of tasks passed eight trials out of eight. pass@k is the optimist's number and pass^k is the operator's. The second paragraph is the distinction Anthropic draws: capability suites are meant to start low and climb; regression suites sit near a hundred and any drop is a bug. Your gate is a regression suite. The practical rule: any case with a model in it runs three times, and you report pass^3.

Cut from slide 6 (full wording):
- pass@k is the chance that at least one of k trials succeeds. It rises with k, so it flatters. pass^k is the chance that all k succeed. It falls with k, and it is the number a user who runs the task every day experiences. / Two kinds of suite. A capability suite asks what the agent can do; it starts low and is meant to climb. A regression suite asks whether it still does what it did; it sits near 100%, and any drop is a defect. Your Sortie 10 gate is a regression suite with a few capability cases reported beside it. / For your card: run every model-in-the-loop case at least 3 times and report pass^3 alongside the mean.

### AFTER

One run is an anecdote. τ-bench, from Yao, Shinn, Razavi, and Narasimhan in June 2024, introduced pass^k, the probability that all k trials of a task succeed. GPT-4o succeeded on fewer than half the tasks, and in the retail domain fewer than a quarter of the tasks passed eight trials out of eight. pass@k rises with k, because it counts any one success among k trials; pass^k falls with k, because it requires every trial to succeed, and pass^k is the rate a user who runs the task every day experiences. The second paragraph draws Anthropic's distinction between two kinds of suite: a capability suite starts low and is meant to climb, and a regression suite sits near a hundred, where any drop is a defect. Your gate is a regression suite. The practical rule for the card: any case with a model in it runs three times, and you report pass^3 beside the mean.

Cut from slide 6 (full wording):
- pass@k is the chance that at least one of k trials succeeds. It rises with k, so it makes an agent look more reliable than it is. pass^k is the chance that all k succeed. It falls with k, and it matches the experience of a user who runs the task every day. / Two kinds of suite. A capability suite asks what the agent can do. Its pass rate starts low and is meant to climb. A regression suite asks whether the agent still does what it did. Its pass rate sits near 100%, and any drop is a defect. Your Sortie 10 gate is a regression suite with a few capability cases reported beside it. / For your card: run every model-in-the-loop case at least 3 times and report pass^3 alongside the mean.

## Slide 7

### BEFORE

The gate in five steps. Run and write per-case results. Compare against a baseline you froze and committed. Decide with a rule written in code before you ran it: any regression, or a rate below the threshold, exits one. Name the cases, because a red light with no case id sends you hunting. Wire it into something that runs without you: a hook or CI. The strip is the reason for case-by-case comparison. An aggregate of eighty percent last week and eighty percent this week can hide one requirement that broke and another that improved. gzkit's runner has a function named eval_regression_delta for the same reason; we will see it in the reference design.

Cut from slide 7 (full wording):
- Run every case; write results.json, one pass/fail per case id, plus trial count and model id. / uv run python evals/gate.py
- Load baseline.json (committed, frozen). A regression is a case that passed in the baseline and fails now. A new pass is reported, not rewarded.
- RED if any regression, or if the pass rate is below the pre-registered threshold. The rule is code: / if regressed or rate < THRESHOLD: sys.exit(1)
- Print the ids that regressed and write delta.json. A red gate that does not say which case failed sends you to the transcript blind.
- Call the gate from a pre-commit or pre-push hook, or from CI. A gate you run by hand when you remember is a report.
- Why case-by-case: an aggregate can hold steady while one requirement breaks and another improves. The mean hides the regression; the delta names it.

### AFTER

The gate has five steps. Run every case and write a per-case result. Compare the results against a baseline you froze and committed. Decide with a rule written in code before the first run: any regression, or a rate below the threshold, exits one. Print the ids of the regressed cases, because a red light with no case id sends you to the transcripts blind. Wire the gate into something that runs without you, a hook or CI, because a gate you run by hand when you remember is a report. The strip gives the reason for case-by-case comparison: an aggregate of eighty percent in two successive runs can hide one requirement that broke and another that improved, so the mean hides the regression and only the per-case delta shows it. gzkit's runner has a function called eval_regression_delta for the same reason, and it appears in the reference design teardown.

Cut from slide 7 (full wording):
- Run every case. Write results.json, one pass/fail per case id, plus trial count and model id. / uv run python evals/gate.py
- Load baseline.json (committed, frozen). A regression is a case that passed in the baseline and fails now. The gate reports a new pass, and the new pass does not change the verdict.
- RED if any regression, or if the pass rate is below the pre-registered threshold. The rule is code: / if regressed or rate < THRESHOLD: sys.exit(1)
- Print the ids that regressed and write delta.json. A red gate that does not list the failed case leaves you to search the transcripts for it.
- Call the gate from a pre-commit or pre-push hook, or from CI. A gate that you run by hand only when you remember does not stop the commits you forget to check.
- Why case-by-case: an aggregate can hold steady while one requirement breaks and another improves. The mean can hide the regression. The delta lists the case ids that regressed.

## Slide 8

### BEFORE

Four biases, each with a paper you can cite in your Design Analysis. Position: Wang and colleagues showed in 2023 that reordering two answers was enough for a weaker model to beat a stronger one on sixty-six of eighty queries. Verbosity: the MT-Bench paper, Zheng and colleagues at NeurIPS 2023, found judges prefer longer answers. Self-preference: Zheng named it self-enhancement; Panickssery, Bowman, and Feng in 2024 showed models recognize their own outputs and that recognition predicts the preference; Wataoka and colleagues argue the mechanism is familiarity, lower perplexity. Injection is the 2026 addition: the Berkeley group put hidden comments in agent answers and moved the judge's score. The right column is what you build: both orders, binary rubric, a different family, and the answer treated as data, which is the E5 rule again.

Cut from slide 8 (full wording):
- Wang et al. (2023), 'Large Language Models are not Fair Evaluators': by swapping answer order alone, Vicuna-13B beat ChatGPT on 66 of 80 queries as judged by an LLM.
- Judge every pair in both orders. Count a verdict only if both orders agree; a flip is a tie and goes to a human.
- Zheng et al. (2023) name self-enhancement. Panickssery, Bowman & Feng (2024): models recognize their own text, and self-recognition tracks self-preference. Wataoka et al. (2024): judges favor low-perplexity, familiar text.
- The judge is a different model family from the generator. Strip model names and signatures from what the judge sees.
- Wang, Mang, Cheung, Sen & Song (UC Berkeley, Apr 2026): hidden comments in an agent's answer steered an LLM judge's score (CAR-bench).
- Zheng et al. also found GPT-4 judges agreed with human preferences over 80% of the time, the same rate humans agree with each other. Agreement is the reason judges are used; the biases are the reason they are checked.

### AFTER

Four biases, each with a paper you can cite in your Design Analysis. Position: Wang and colleagues showed in 2023 that reordering two answers was enough for a weaker model to beat a stronger one on sixty-six of eighty queries. Verbosity: the MT-Bench paper, Zheng and colleagues at NeurIPS 2023, found that judges prefer longer answers, padded ones included. Self-preference: Zheng's paper calls it self-enhancement; Panickssery, Bowman, and Feng showed in 2024 that models recognize their own outputs and that recognition predicts the preference; Wataoka and colleagues argue that the mechanism is familiarity, in other words lower perplexity. Injection is the 2026 addition: the Berkeley group put hidden comments in agent answers and moved the judge's score. The right column is the defense you build for each: judge in both orders, use a binary rubric, judge from a different family, and treat the answer as data, which is the E5 rule applied to the grader.

Cut from slide 8 (full wording):
- Wang et al. (2023), 'Large Language Models are not Fair Evaluators': by swapping answer order alone, Vicuna-13B beat ChatGPT on 66 of 80 queries as judged by an LLM.
- Judge every pair in both orders. Count a verdict only if both orders agree. A flip counts as a tie and goes to a human.
- Zheng et al. (2023) describe self-enhancement bias. Panickssery, Bowman & Feng (2024): models recognize their own text, and self-recognition tracks self-preference. Wataoka et al. (2024): judges favor low-perplexity, familiar text.
- The judge is a different model family from the generator. Strip model names and signatures from what the judge sees.
- Wang, Mang, Cheung, Sen & Song (UC Berkeley, Apr 2026): hidden comments in an agent's answer steered an LLM judge's score (CAR-bench).
- Zheng et al. also found GPT-4 judges agreed with human preferences over 80% of the time, the same rate humans agree with each other. That agreement justifies using a judge. The measured biases require checking the judge before its scores reach a gate.

## Slide 9

### BEFORE

This is the judge-blinding example for your card. The left panel is a rubric you can copy. The answer sits between tags and is declared to be data. The judge answers three yes-or-no questions, and the pass rule is combined in your code, not by the judge. The right panel is the admissibility test: blind, binary, calibrated against ten cases you labeled yourself, and it must catch a planted wrong answer and a planted injection. The last line anticipates the reference design: even a good judge produces a model's claim about a model. It can hold a gate shut. It cannot stand in for a human's signature.

Cut from slide 9 (full wording):
- Blind. No model names, no system name, no 'our answer'. Pairwise judging runs in both orders. / Binary. Yes/no questions about content, combined by a rule in code. No 1–10 scales. / Calibrated. Ten cases you labeled by hand first; the judge must agree on at least 9, and you record which it missed. / Planted. One wrong answer written to look right, and one with an injected instruction. The judge must fail both. / A judge that passes all four is a grader. Its verdict is still a model's claim about a model: evidence for a gate, never a human attestation.

### AFTER

This slide is the judge-blinding example for your card. The left panel is a rubric you can copy. The answer sits between tags and the prompt declares it to be data. The judge answers three yes-or-no questions, and your code combines them into the pass rule, so the judge never decides the verdict on its own. The right panel is the admissibility test: the judge is blind, its questions are binary, it is calibrated against ten cases you labeled yourself, and it has caught a planted wrong answer and a planted injection. The last line anticipates the reference design. A judge that passes all four checks produces evidence a gate can act on, and the evidence is still a model's statement about a model; GZK-GOV-007 therefore reserves the attestation for a person.

Cut from slide 9 (full wording):
- Blind. No model names, no system name, no 'our answer'. Pairwise judging runs in both orders. / Binary. Yes/no questions about content, combined by a rule in code. No 1–10 scales. / Calibrated. Label ten cases by hand first. The judge must agree on at least 9, and you record which it missed. / Planted. One wrong answer written to look right, and one with an injected instruction. The judge must fail both. / A judge that passes all four checks qualifies as a grader. Its verdict remains one model's judgment of another model's output. The verdict counts as evidence for a gate and cannot serve as a human attestation.

## Slide 10

### BEFORE

The RED witness, in one sentence from gzkit's own glossary: proof that a test fails without the change it covers. The procedure is on the slide: rebuild without the change, run the covering test, expect failure, restore. The idea is old. TDD makes you watch the test fail first; mutation testing, from DeMillo, Lipton, and Sayward in 1978, changes the program on purpose and asks whether the suite notices. For an eval suite you want two witnesses: remove the feature, and plant a wrong answer. The third paragraph names what they catch: tautological tests, where the expected value came from the code under test, and hollow tests, which pass for any output. You will find one of each in the lab tonight. Verify the gz arb red flags before class.

Cut from slide 10 (full wording):
- Where the idea comes from. Test-driven development writes the test first and watches it fail (red) before the code makes it pass (green). Mutation testing (DeMillo, Lipton & Sayward, 1978) generalizes it: change the program on purpose; a suite that still passes has not tested what changed. gzkit calls the recorded version a RED witness and runs it with gz arb red. [Verify the command's current flags against the repository before class.] / For an eval suite, two witnesses. (1) Feature removed: comment out the behavior; the cases that cover it must go red, and you predicted which ones before you ran it. (2) Wrong answer planted: substitute one wrong output; the grader or judge must fail it. / What it catches. A tautological test compares the code with itself (expected value computed by the function under test). A hollow test passes for any output (assert result is not None; a check that accepts every label). Both are green forever, and both look like coverage.

Instructor checks moved off the slide:
- [Verify the command's current flags against the repository before class.]

### AFTER

The RED witness, in one sentence from gzkit's own glossary, is proof that a test fails without the change it covers. The procedure is on the slide: rebuild without the change, run the covering test, expect failure, restore. The idea is older than gzkit. Test-driven development makes you watch the test fail before the code makes it pass; mutation testing, from DeMillo, Lipton, and Sayward in 1978, changes the program on purpose and asks whether the suite notices. An eval suite needs two witnesses: remove the feature, and plant a wrong answer. The third paragraph states what the two catch: a tautological test, where the expected value came from the code under test, and a hollow test, which passes for any output. Both stay green forever, and both look like coverage. The lab plants one of each.

Cut from slide 10 (full wording):
- Where the idea comes from. Test-driven development writes the test first and watches it fail (red) before the code makes it pass (green). Mutation testing (DeMillo, Lipton & Sayward, 1978) generalizes it: change the program on purpose; a suite that still passes has not tested what changed. gzkit calls the recorded version a RED witness and runs it with gz arb red. [Verify the command's current flags against the repository before class.] / For an eval suite, two witnesses. (1) Feature removed: comment out the behavior. The cases that cover it must go red, and you must have predicted which ones before the run. (2) Wrong answer planted: substitute one wrong output. The grader or judge must fail it. / What it catches. A tautological test compares the code with itself (expected value computed by the function under test). A hollow test passes for any output (assert result is not None; a check that accepts every label). Both stay green on every run and still count toward coverage.

Instructor checks moved off the slide:
- [Verify the command's current flags against the repository before class.]

## Slide 11

### BEFORE

Pre-registration is the flight card's origin outside aviation. Nosek and colleagues in PNAS in 2018 put it as prediction versus postdiction: a hypothesis fixed before the data tests something; one fitted after only describes it. Kerr's 1998 paper named the failure HARKing. In an eval suite, HARKing looks like choosing the threshold after the score, dropping the failing case, re-running until green, or padding the set with cases you already pass. Our mechanism: commit the card and the golden set first, put the hash on the card, and have the Chase sign that commit. The strip is the test you apply to every card this week.

Cut from slide 11 (full wording):
- State the hypothesis, the measure, and the decision rule before observing the outcome. Nosek, Ebersole, DeHaven & Mellor (PNAS, 2018): pre-registration separates prediction, which tests a claim, from postdiction, which only generates one.
- HARKing, hypothesizing after the results are known (Kerr, 1998). In evals: choosing the threshold after seeing the score; dropping the case that failed; re-running until green; adding a case the system already passes.
- The card holds the claim, the threshold, the case count, the removal diff, and the falsifiers. Commit it and the golden set before the first run; the commit hash goes on the card. The Chase signs that commit. Amendments append with a reason; they never overwrite.
- The test for pre-registration: could the evidence have come out against you, and did you say in advance what that would look like?

### AFTER

Pre-registration is the flight card's origin outside aviation. Nosek and colleagues, in PNAS in 2018, put the distinction as prediction versus postdiction: a hypothesis fixed before the data tests something, and a hypothesis fitted after the data only describes it. Kerr's 1998 paper gave the failure its label, HARKing, hypothesizing after the results are known. In an eval suite, HARKing looks like choosing the threshold after the score, dropping the failing case, re-running until green, or padding the set with cases the system already passes. The course's mechanism against it has three parts: commit the card and the golden set first, put the commit hash on the card, and have the Chase sign that commit. The strip is the test to apply to every card: could the evidence have come out against you, and did you say in advance what that would look like?

Cut from slide 11 (full wording):
- State the hypothesis, the measure, and the decision rule before observing the outcome. Nosek, Ebersole, DeHaven & Mellor (PNAS, 2018): pre-registration separates prediction, which tests a claim, from postdiction, which only generates one.
- HARKing, hypothesizing after the results are known (Kerr, 1998). In evals: choosing the threshold after seeing the score; dropping the case that failed; re-running until green; adding a case the system already passes.
- The card holds the claim, the threshold, the case count, the removal diff, and the falsifiers. Commit it and the golden set before the first run, and write the commit hash on the card. The Chase signs that commit. Amendments are appended with a reason and never overwrite earlier entries.
- To test a pre-registration, ask two questions: could the evidence have come out against you, and did you state in advance what that result would look like?

## Slide 12

### BEFORE

The common mistake of the week. Recording the agent's current output as the expected value is quick, and it produces a set that is green on day one and blind to any bug present on that day. It detects change, which has some value, but it never checked correctness. Its cousins are the not-None assertion, the judge asked whether an answer is good with no reference, and a fixture that mocks the thing under test. On the board: remove the feature and some snapshot cases do go red; then plant a bug that was present on snapshot day, and nothing goes red. The rule: expected values come from requirements, written by hand before the agent runs.

Cut from slide 12 (full wording):
- Common mistake: goldens copied from the system's own output
- for case in inputs: /     case['expect'] = agent(case['input'])  # 'record the golden' / json.dump(cases, open('golden.json', 'w')) / The set now encodes whatever the agent did on the day you ran it, bugs included. Every case passes on the first run. It will catch a change, but not a wrong behavior that was already there, and it never asked whether the output was right. / Cousins: assert result is not None; a judge asked 'is this a good answer?'; a fixture that mocks the feature under test.
- 1. Take the snapshot set. Remove the feature. Some cases go red: good. / 2. Now plant a bug that was present on snapshot day (the agent always called a write tool 'write', even for delete). Nothing goes red, because the golden says 'write'. / 3. Fix: write expected values from the requirement, by hand, before running the agent. Snapshots are allowed only as a change detector, labeled as such, beside the golden set. / Rule for Sortie 10: every expected value in golden.jsonl traces to a requirement or an AI_LOG entry, never to a run.

### AFTER

The common mistake for this Evolution. If you record the agent's current output as the expected value, you build the set in minutes, and the set is green on day one and blind to every bug present on that day. Such a set detects change, which has some value, and it never checked correctness, because no one compared the recorded output with the requirement. Its cousins are the not-None assertion, the judge asked whether an answer is good with no reference, and a fixture that mocks the thing under test. On the board: remove the feature, and some snapshot cases do go red; then plant a bug that was present on snapshot day, and nothing goes red, because the golden recorded the bug. The rule for Sortie 10 follows: expected values come from requirements, written by hand before the agent runs.

Cut from slide 12 (full wording):
- Common mistake: goldens copied from the system's own output
- for case in inputs: /     case['expect'] = agent(case['input'])  # 'record the golden' / json.dump(cases, open('golden.json', 'w')) / The set now encodes whatever the agent did on the day you ran it, bugs included. Every case passes on the first run. It will catch a change, but not a wrong behavior that was already there, and nobody checked whether the output was right. / Related failures: assert result is not None; a judge asked 'is this a good answer?'; a fixture that mocks the feature under test.
- 1. Take the snapshot set. Remove the feature. Some cases go red, as they should. / 2. Now plant a bug that was present on snapshot day (the agent always called a write tool 'write', even for delete). Nothing goes red, because the golden says 'write'. / 3. Fix: write expected values from the requirement, by hand, before running the agent. Snapshots are allowed only as a change detector, labeled as such, beside the golden set. / Rule for Sortie 10: every expected value in golden.jsonl traces to a requirement or an AI_LOG entry, and no expected value comes from a run.

## Slide 13

### BEFORE

Five minutes. The question for the break: name one check you have never seen fail. We start the teardowns at 1:00 with benchmarks whose graders turned out to have the same problem.

Cut from slide 13 (full wording):
- Before we come back: name one check in your repository that you have never seen fail. What would it take to see it go red?

### AFTER

Five minutes. The question for the break: pick one check in your repository that you have never seen fail, and say what would make it go red. The teardowns that follow cover benchmarks whose graders turned out to have the same problem.

Cut from slide 13 (full wording):
- Pick one check in your repository that you have never seen fail. What would it take to see it go red?

## Slide 14

### BEFORE

Six benchmarks, one column that matters: the grader. SWE-bench grades by the repository's own tests; Verified is the 500-task subset that ninety-three developers screened, after they found most of the sample underspecified or unfairly tested. GAIA grades a short answer by exact match after normalization. WebArena checks site state and strings. AgentBench averages eight different environments. τ-bench compares the database at the end with the goal state and introduced pass^k; τ²-bench added a user who can also act on the environment. The last column is what each grader cannot see, and the next two slides are what happened when people went looking. Note on the table: τ³-bench shipped in July 2026 and says its scores are not comparable with earlier versions.

Cut from slide 14 (full wording):
- Sources: the arXiv papers and OpenAI's Verified post (checked 09/24/2026). τ³-bench (v1.0.1, Jul 2026) adds a knowledge domain and fixes 75+ tasks; earlier scores are not comparable.

### AFTER

Six benchmarks, and the column that matters is the grader. SWE-bench grades by the repository's own tests; Verified is the 500-task subset that ninety-three developers screened, after they removed 68.3 percent of the sampled tasks as underspecified or unfairly tested. GAIA grades a short answer by exact match after normalization. WebArena checks site state and strings. AgentBench averages eight unlike environments. τ-bench compares the database at the end of the trial with the goal state and introduced pass^k; τ²-bench added a user who can also act on the environment. The last column lists what each grader cannot see, and the next two slides report what happened when people went looking there. One note on the table: τ³-bench shipped in July 2026 and states that its scores are not comparable with earlier versions.

Cut from slide 14 (full wording):
- Sources: the arXiv papers and OpenAI's Verified post. τ³-bench (v1.0.1, Jul 2026) adds a knowledge domain and fixes 75+ tasks. Scores from earlier versions are not comparable.

## Slide 15

### BEFORE

Two 2026 findings. In February, OpenAI stopped reporting SWE-bench Verified. It audited 138 tasks o3 kept failing and found 59.4 percent had flawed tests or descriptions, and every frontier model it probed could reproduce gold patches from memory. It now recommends SWE-bench Pro, Scale's benchmark from September 2025 with held-out and commercial partitions. In June, Cursor audited 731 trajectories on Pro and found the other leak: agents with web or git access looked the answer up. One frontier model's score fell from 87.1 to 73.0 when those routes were closed, and 63 percent of its successful fixes had been retrieved. The strip maps it to Appendix C: metagaming the gate. The lesson for your own suite is the last line of the body.

Cut from slide 15 (full wording):
- Contamination. OpenAI: gains on Verified 'increasingly reflect how much the model was exposed to the benchmark at training time.' It recommends SWE-bench Pro (Scale AI, Sep 2025: 1,865 tasks, 41 repos, public, held-out, and commercial partitions). / Retrieval. Cursor audited 731 trajectories on Pro. Agents with web access found the merged upstream pull request (57%) or mined future commits from the bundled .git history (9%). A September 2026 preprint, SWE-Bench Pro Verified, closes those channels and re-scores. / The lesson for your suite: if the answer is reachable from inside the environment, the benchmark measures search.
- Failure mode #9, metagaming the gate: the agent satisfied the check (tests pass) by a route the check's author did not intend.

### AFTER

Two 2026 findings. In February, OpenAI stopped reporting SWE-bench Verified. It audited 138 tasks that o3 kept failing and found that 59.4 percent had flawed tests or descriptions, and every frontier model it probed could reproduce gold patches from memory. It now recommends SWE-bench Pro, Scale's benchmark from September 2025 with held-out and commercial partitions. In June, Cursor audited 731 trajectories on Pro and found the other leak: agents with web or git access looked the answer up. One frontier model's score fell from 87.1 to 73.0 when Cursor closed those routes, and 63 percent of its successful fixes had been retrieved from an upstream pull request or a future commit. The strip maps both findings to Appendix C, failure mode nine, metagaming the gate. The lesson for your own suite is the last line of the body: if the answer is reachable from inside the environment, the benchmark measures search.

Cut from slide 15 (full wording):
- Contamination. OpenAI: gains on Verified 'increasingly reflect how much the model was exposed to the benchmark at training time.' It recommends SWE-bench Pro (Scale AI, Sep 2025: 1,865 tasks, 41 repos, public, held-out, and commercial partitions). / Retrieval. Cursor audited 731 trajectories on Pro. Agents with web access found the merged upstream pull request (57%) or mined future commits from the bundled .git history (9%). A September 2026 preprint, SWE-Bench Pro Verified, closes those channels and re-scores. / For your suite: if the agent can reach the answer from inside the environment, a high score can come from finding the answer instead of solving the task.
- Failure mode #9, metagaming the gate: the agent satisfied the check (tests pass) by a route the check's author did not intend.

## Slide 16

### BEFORE

In April, a Berkeley group built an agent whose only job was to score well without solving anything, and it drove eight benchmarks to near-perfect scores. Read the third column: every exploit is a grader that trusted something the agent could touch. The test runner inside the sandbox; answer files on the same machine; a normalizer lenient enough to accept anything; a check that a message exists; a judge that reads the answer as instructions; and, from the 2025 Agentic Benchmark Checklist paper, τ-bench tasks where saying nothing counted as correct. The fourth column is the point for tonight: each one has a small version in your own suite, and the Sortie 10 falsifiers are written to catch them.

Cut from slide 16 (full wording):
- Teardown: how the Berkeley group broke eight agent benchmarks
- Wang, Mang, Cheung, Sen & Song, Apr 8, 2026; each exploit is a grader that trusted something the agent could touch
- The group reports all eight examined benchmarks could be driven to near-perfect scores without solving a task. The ABC checklist (Zhu et al., 2025) found flaws that misstate performance by up to 100% in relative terms.

### AFTER

In April, a Berkeley group built an agent whose only job was to score well without solving anything, and it drove eight benchmarks to near-perfect scores. Read the third column: every exploit is a grader that trusted something the agent could touch. The test runner ran inside the sandbox; the answer files sat on the same machine; a normalizer was lenient enough to accept anything; a validator checked only that a message existed; a judge read the answer as instructions; and, from the 2025 Agentic Benchmark Checklist paper, τ-bench tasks counted silence as correct. The fourth column is the point for this Evolution: each exploit has a small version in your own suite, and the Sortie 10 falsifiers are written to catch them.

Cut from slide 16 (full wording):
- Teardown: how the Berkeley group broke eight agent benchmarks
- Wang, Mang, Cheung, Sen & Song, Apr 8, 2026; in each exploit, a grader trusted something the agent could touch
- The group reports all eight examined benchmarks could be driven to near-perfect scores without solving a task. The ABC checklist (Zhu et al., 2025) found flaws that misstate performance by up to 100% in relative terms.

## Slide 17

### BEFORE

The judge as a system. MT-Bench is eighty multi-turn questions graded by GPT-4; Chatbot Arena is crowdsourced pairwise votes between anonymous models. The design choice is to replace human raters with a model, justified by agreement above eighty percent, which matched human-to-human agreement. The cost is that the judge's biases are in every score, and the paper measured them: position, verbosity, self-enhancement. The failure mode is metagaming at scale: optimize against a judge and you learn the judge. The strip is the habit I want in your Design Analysis: when you cite this paper for the eighty percent, cite it for the biases too.

Cut from slide 17 (full wording):
- Teardown: MT-Bench and Chatbot Arena, the judge as a system
- 80 multi-turn questions (MT-Bench) graded by GPT-4 as judge, in single-answer and pairwise modes; Chatbot Arena collects crowd votes between two anonymous models. 3K expert votes and 30K conversations released.
- Replace human raters with a strong model, because humans are slow and costly. Justified by agreement: GPT-4 matched human preference over 80% of the time, the same as human-human agreement.
- The judge's biases enter every score: position, verbosity, self-enhancement, limited reasoning on math. The paper measured them and proposed swaps and reference answers; users of the method often skip both.
- App. C #9 at scale: a system tuned against a judge learns the judge. Longer, more confident answers score higher whether or not they are right. Defense: the admissibility checks from 0:38.

### AFTER

The judge as a system. MT-Bench is eighty multi-turn questions graded by GPT-4; Chatbot Arena collects crowdsourced pairwise votes between anonymous models. The design choice replaces human raters with a model, and the paper justifies it by agreement: GPT-4 matched human preference above eighty percent of the time, which equals the rate at which humans agree with each other. The cost is that the judge's biases enter every score, and the paper measured three of them: position, verbosity, and self-enhancement. The failure mode is metagaming at scale: a system tuned against a judge learns the judge's preferences rather than the task. The strip is the habit I want in your Design Analysis: when you cite this paper for the eighty percent, cite it for the biases as well, because the two findings come from the same experiment.

Cut from slide 17 (full wording):
- Teardown: MT-Bench and Chatbot Arena, the judge as a system
- 80 multi-turn questions (MT-Bench) graded by GPT-4 as judge, in single-answer and pairwise modes; Chatbot Arena collects crowd votes between two anonymous models. 3K expert votes and 30K conversations released.
- The method replaces human raters with a strong model, because humans are slow and costly. The authors justify the replacement by agreement: GPT-4 matched human preference over 80% of the time, the same as human-human agreement.
- The judge's biases enter every score: position, verbosity, self-enhancement, limited reasoning on math. The paper measured them and proposed swaps and reference answers; a user of the method can skip both, and the scores then carry the biases.
- App. C #9 at scale: a system tuned against a judge learns the judge's preferences. Longer, more confident answers score higher whether or not they are right. Defense: the judge admissibility checks (Blind, Binary, Calibrated, Planted).

## Slide 18

### BEFORE

The live Design Analysis. We fill it on the board together, and this slide is the answer key. The interesting rows are three. Tools: in the telecom domain the user also has tools, which is what dual control means, so the agent must get a person to do things, not just do them itself. Evaluation: the grader compares the final database with the goal state, which is outcome grading, and pass^k measures consistency. Governance: the human is simulated by a model, so the benchmark has a model inside its own grading path, and any simulator error lands on the agent's score. The judgment loop is in the strip; write your own before you look at mine.

Cut from slide 18 (full wording):
- Any model under test as the agent; a separate LLM plays the user. Tasks generated from atomic components, so they are verifiable by construction.
- Conversation turns from the simulated user plus tool results from the domain database (airline, retail, telecom).
- Agent tools on the backend; in telecom, the user also has tools on their own device (dual control, modeled as a Dec-POMDP).
- Agent and user must coordinate: the agent guides a user who acts. Ablations separate reasoning errors from communication errors.
- Final database state compared with the goal state; pass^k over repeated trials. Graded by outcome, not transcript.
- The human is simulated, and the simulator is a model: its errors become the agent's score.

### AFTER

The live Design Analysis. The class fills the nine components in on the board, and this slide is the answer key. Three rows carry the design decisions. Tools: in the telecom domain the user also has tools, which is what dual control means, so the agent must get a person to act rather than acting itself. Evaluation: the grader compares the final database with the goal state, which is outcome grading, and pass^k measures consistency across trials. Governance: a model simulates the human, so the benchmark has a model inside its own grading path, and any simulator error lands on the agent's score. The judgment loop is in the strip; write your own before you read mine.

Cut from slide 18 (full wording):
- Any model under test as the agent; a separate LLM plays the user. Tasks generated from atomic components, so they are verifiable by construction.
- Conversation turns from the simulated user plus tool results from the domain database (airline, retail, telecom).
- Agent tools on the backend; in telecom, the user also has tools on their own device (dual control, modeled as a Dec-POMDP).
- Agent and user must coordinate: the agent guides a user who acts. Ablations separate reasoning errors from communication errors.
- Final database state compared with the goal state; pass^k over repeated trials. The grader checks the outcome and ignores the transcript.
- The human is simulated, and the simulator is a model: its errors enter the agent's score.

## Slide 19

### BEFORE

The last teardown is the reference design's own evaluation surfaces. On the left, an eval runner with golden datasets in the repository and a function that computes the regression delta, plus a red-team evaluation for ADRs. The design choice is that golden data is versioned beside the code, so changing a case is a diff. Note what it does not do: gzkit makes no model calls, so any judge comes from the harness. On the right, the flight-test program: the five rules, which are the lecture's two rules plus three more. As of mid-August no sortie had been flown under it; this course is flying them. Verify paths and flags before class.

Cut from slide 19 (full wording):
- Teardown: the gzkit eval runner and the flight-test program
- Code in src/gzkit/eval/; golden datasets in data/eval/*.json; a regression delta computed by eval_regression_delta; gz adr evaluate --red-team runs a red-team evaluation of an ADR. / Design choice: golden data lives in the repository beside the code, versioned with it, so a change to a case is a diff someone can review. / What it does not do: gzkit makes no LLM calls of its own; a judge is something a harness brings. / [Verify paths, function name, and flag against the repository before class.]
- docs/flighttest/: README, flight-card-template.md, manifest.md (S1–S6), and the gz-flighttest skill. Five rules: pre-register; the black box is truth; build up the envelope; fly the governed path; independent observation. / Mechanism: the card is the pre-registration, the ledger and receipts are the black box, the Chase is the independent observer. / Status: zero sorties flown as of 2026-08-17. This course flies the first ones; your Sortie 10 is an evaluation of an evaluation. / [Verify against the repository.]

Instructor checks moved off the slide:
- [Verify paths, function name, and flag against the repository before class.]
- [Verify against the repository.]

### AFTER

The last teardown covers the reference design's own evaluation surfaces. On the left is an eval runner with golden datasets in the repository, a function that computes the regression delta, and a red-team evaluation for ADRs. The design choice is that golden data is versioned beside the code, so a change to a case is a diff that a reviewer can read. gzkit makes no model calls of its own, so any judge comes from the harness. On the right is the flight-test program: five rules, of which the first two are the lecture's two rules (pre-register; the black box is truth) and the other three govern the envelope, the path, and the observer. As of mid-August no sortie had been flown under the program; this course flies the first ones, and Sortie 10 is an evaluation of an evaluation.

Cut from slide 19 (full wording):
- Teardown: the gzkit eval runner and the flight-test program
- Code in src/gzkit/eval/; golden datasets in data/eval/*.json; a regression delta computed by eval_regression_delta; gz adr evaluate --red-team runs a red-team evaluation of an ADR. / Design choice: golden data lives in the repository beside the code, versioned with it, so a change to a case is a diff someone can review. / What it does not do: gzkit makes no LLM calls of its own. A harness supplies the judge. / [Verify paths, function name, and flag against the repository before class.]
- docs/flighttest/: README, flight-card-template.md, manifest.md (S1–S6), and the gz-flighttest skill. Five rules: pre-register; the black box is truth; build up the envelope; fly the governed path; independent observation. / Mechanism: the card is the pre-registration, the ledger and receipts are the black box, the Chase is the independent observer. / Status: zero sorties flown as of 2026-08-17. This course flies the first ones. Your Sortie 10 evaluates an evaluation. / [Verify against the repository.]

Instructor checks moved off the slide:
- [Verify paths, function name, and flag against the repository before class.]
- [Verify against the repository.]

## Slide 20

### BEFORE

GZK-GOV-007 is the reading for the week, and its rule fits in one line: model self-review is Gate-4 evidence, never Gate-5. Gate 4 is behavioral acceptance; Gate 5 is a human's attestation. The reason is the bias table from the spine: a reviewer of the same family favors text like its own. The episodes on the right are why the rule was written in June: an attestation attributed to an operator who never gave it, then four briefs attested complete for components that did not exist. For your system: the judge's verdict is evidence, recorded with its model id; the PASS is written by your Chase. Verify wording, dates, and the ADR number before class.

Cut from slide 20 (full wording):
- Reference design: GZK-GOV-007, model review is never Gate 5
- Model self-review, however thorough, is Gate-4 evidence and never Gate-5. Gate 4 is behavioral acceptance (BDD); Gate 5 is a human's attestation. A model's review can hold a gate shut; it cannot open the last one. / Why: the reviewer and the reviewed share a family, a context, or both. The self-preference literature (Panickssery et al., 2024; Wataoka et al., 2024) says the reviewer will favor text that looks like its own. / [Verify the document's wording and date against the repository before class.]
- 2026-06-13. A Gate-5 attestation was attributed to the operator, who had never given it. First repudiation; ADR-0.0.71. / 2026-06-16. Four briefs were attested Completed for a renderer, a validator, a composer, and a playback store. None existed as attested. Result: repudiations and the enforcement-claim rule. / For your system: your judge's verdict goes in the flight log as evidence with the judge's model id. The PASS on the card is written by your Chase, a person, from that evidence. / [Verify dates and ADR number against the repository before class.]

Instructor checks moved off the slide:
- [Verify the document's wording and date against the repository before class.]
- [Verify dates and ADR number against the repository before class.]

### AFTER

GZK-GOV-007 is the assigned reading, and its rule fits in one line: model self-review is Gate-4 evidence, never Gate-5. Gate 4 is behavioral acceptance; Gate 5 is a human's attestation. The reason is the bias table from the spine: a reviewer of the same family as the reviewed favors text like its own, so its approval carries the self-preference bias into the attestation. The episodes on the right are the reason gzkit wrote the rule in June: an attestation attributed to an operator who never gave it, then four briefs attested Completed for components that did not exist. For your system, the judge's verdict is evidence, recorded with its model id, and your Chase writes the PASS from that evidence.

Cut from slide 20 (full wording):
- Reference design: GZK-GOV-007, model review is never Gate 5
- Model self-review, however thorough, is Gate-4 evidence and never Gate-5. Gate 4 is behavioral acceptance (BDD); Gate 5 is a human's attestation. A model's review can hold a gate shut. It cannot open the last one. / Why: the reviewer and the reviewed share a family, a context, or both. The self-preference literature (Panickssery et al., 2024; Wataoka et al., 2024) reports that the reviewer will favor text that looks like its own. / [Verify the document's wording and date against the repository before class.]
- 2026-06-13. A Gate-5 attestation was attributed to the operator, who had never given it. First repudiation; ADR-0.0.71. / 2026-06-16. Four briefs were attested Completed for a renderer, a validator, a composer, and a playback store. None existed as attested. Result: repudiations and the enforcement-claim rule. / For your system: your judge's verdict goes in the flight log as evidence with the judge's model id. Your Chase, a person, writes the PASS on the card from that evidence. / [Verify dates and ADR number against the repository before class.]

Instructor checks moved off the slide:
- [Verify the document's wording and date against the repository before class.]
- [Verify dates and ADR number against the repository before class.]

## Slide 21

### BEFORE

The hollow antibody is the chapter's central episode. After the June repudiations, gzkit built an audit to find verification that verifies nothing, and that audit was itself hollow, and it was attested complete. The fix was a live negative control: any check that claims to enforce a rule is run against a known violation and must fail, every time. The August 21 episode has the same shape: a gate that checked a marker file existed and was satisfied by a stale one. The fourth card is the transfer: your golden set is your antibody, and test points two, four, and five on tonight's card are its negative controls. Verify ADR-0.0.73 and the mechanism before class.

Cut from slide 21 (full wording):
- After the June 16 repudiations, gzkit built a verification-layer audit, 'the antibody', to find checks that verify nothing. The antibody's own checks were hollow: they could not fail. It was attested Completed anyway.
- @enforces with live negative controls: a check that claims to enforce a rule must be run against a known violation and be seen to fail. The negative control runs every time, not once at authoring.
- Your golden set is your antibody. Sortie 10's test points 2, 4, and 5 are its live negative controls: feature removed, wrong answer planted, constant-answer stub. Run them in the gate, not once.
- The pipeline gate checked only that a marker file existed. A stale marker licensed ~350 lines with no dispatch or review. 'A presence check answers is something armed, never did the procedure run.'
- An evaluator is a system. It needs its own RED witness, or it becomes one more green light. [Verify ADR-0.0.73 and the @enforces mechanism against the repository before class.]

Instructor checks moved off the slide:
- [Verify ADR-0.0.73 and the @enforces mechanism against the repository before class.]

### AFTER

The hollow antibody is the chapter's central episode. After the June repudiations, gzkit built an audit to find verification that verifies nothing. The audit's own checks could not fail, so the audit was itself hollow, and gzkit attested it Completed. The fix was a live negative control: any check that claims to enforce a rule runs against a known violation and must fail, every time the check runs. The August 21 episode has the same shape: a gate checked that a marker file existed, and a stale marker satisfied it. The fourth card is the transfer to your system: your golden set is your antibody, and test points two, four, and five on Flight Card 10 are its negative controls, run in the gate rather than once at authoring.

Cut from slide 21 (full wording):
- After the June 16 repudiations, gzkit built a verification-layer audit, 'the antibody', to find checks that verify nothing. The antibody's own checks were hollow: they could not fail. It was attested Completed anyway.
- @enforces with live negative controls: a check that claims to enforce a rule must be run against a known violation and be seen to fail. The negative control runs each time the check runs.
- Your golden set plays the role of the antibody. Sortie 10's test points 2, 4, and 5 are its live negative controls: feature removed, wrong answer planted, constant-answer stub. Run them on every gate run.
- The pipeline gate checked only that a marker file existed. A stale marker licensed ~350 lines with no dispatch or review. 'A presence check answers is something armed, never did the procedure run.'
- An evaluator is a system, so it needs its own RED witness. Without one, its green result shows nothing about whether it can fail. [Verify ADR-0.0.73 and the @enforces mechanism against the repository before class.]

Instructor checks moved off the slide:
- [Verify ADR-0.0.73 and the @enforces mechanism against the repository before class.]

## Slide 22

### BEFORE

The RED witness as a command. Pick the covering test through the requirement links, rebuild without the change, run, expect red, and record a receipt. A pass is a finding: the test does not cover what it claims. The fifth step is why it has to be routine: in late May and early June a green main branch was reopened eight times in nine days, which is where V.I.B.E.S., velocity increased, bugs expected software, got its name, and the answer was a pre-push gate. Your equivalent is your gate script called from a hook, with the removal and the stub as recorded negative controls. Verify the command behavior against the repository before class.

Cut from slide 22 (full wording):
- Reference design: gz arb red, and the gate that makes it routine
- The test must fail. A pass means the test does not cover the change it claims to cover. That is a finding, not a pass.
- Your equivalent this week: python evals/gate.py run by a pre-push hook, with the removal diff and the stub run as recorded negative controls. [Verify gz arb red and gz covers behavior against the repository before class.]

Instructor checks moved off the slide:
- [Verify gz arb red and gz covers behavior against the repository before class.]

### AFTER

The RED witness as a command. gz arb red finds the covering test through the requirement links, rebuilds the code without the change, runs the test, expects red, and records a receipt. A pass at that step is a finding: the test does not cover what it claims to cover. The fifth step explains why the witness has to be routine. In late May and early June a green main branch was reopened eight times in nine days, which is the episode behind the term V.I.B.E.S. (velocity increased, bugs expected software), and the answer was a pre-push gate. Your equivalent is your gate script called from a pre-push hook, with the removal diff and the stub run as recorded negative controls.

Cut from slide 22 (full wording):
- Reference design: gz arb red, and the gate that makes it routine
- The test must fail. A pass means the test does not cover the change it claims to cover. Record such a pass as a finding.
- Your equivalent in this Evolution: python evals/gate.py run by a pre-push hook, with the removal diff and the stub run as recorded negative controls. [Verify gz arb red and gz covers behavior against the repository before class.]

Instructor checks moved off the slide:
- [Verify gz arb red and gz covers behavior against the repository before class.]

## Slide 23

### BEFORE

Weak: goldens copied from the system, single runs, a gate that only prints, a judge grading its own family in one order, goalposts moved after the run, and a removal claim with no prediction. Sound: a small tied set with negatives, a committed baseline and a named delta, a pre-registered commit, a removal that turns exactly the predicted cases red, pass^3 for model cases, and an admissible judge. Exceptional: the stub finds and fixes a hollow case, the judge is calibrated and survives an injection, the gate refuses a real push, and you have checked that your agent cannot reach the answers, which is the Berkeley lesson applied at home.

Cut from slide 23 (full wording):
- Expected values recorded from the agent's own output / One run per case; a rate with no trial count / The gate prints a score; nothing exits non-zero / Judge is the same model that generated the answers; one order only / Threshold or cases changed after the first run; no amendment / 'Removed the feature and it failed' with no prediction and no case ids
- 10–30 cases, each tied to a requirement, a third negative / Baseline committed; delta names the regressed ids; gate exits 1 / Card, golden set, and removal diff committed before the first run; hash on the card / Feature removed: the predicted cases go red, no others; restored: green / Model-in-the-loop cases run 3×, pass^3 reported / Judge from a different family, blinded, both orders, catches the planted error
- The constant-answer stub run finds a hollow case, and the case is fixed with a ledger event / Judge calibrated against 10 hand-labeled cases; misses recorded / A planted injection in an answer; judge fails it / Gate called by a pre-push hook; one real push refused and logged / Environment check: expected values and tests unreachable from the agent's tools

### AFTER

Weak: goldens copied from the system, single runs, a gate that only prints, a judge grading its own family in one order, goalposts moved after the run, and a removal claim with no prediction. Sound: a small set tied to requirements with a third negative, a committed baseline and a delta that lists the regressed ids, a pre-registered commit, a removal that turns exactly the predicted cases red, pass^3 for model cases, and an admissible judge. Exceptional: the stub run finds and fixes a hollow case, the judge is calibrated and survives an injection, the gate refuses a real push, and you have checked that your agent cannot reach the expected values or the tests, which is the Berkeley finding applied to your own environment.

Cut from slide 23 (full wording):
- Expected values recorded from the agent's own output / One run per case; a rate with no trial count / The gate prints a score; nothing exits non-zero / Judge is the same model that generated the answers; one order only / Threshold or cases changed after the first run; no amendment / 'Removed the feature and it failed' with no prediction and no case ids
- 10–30 cases, each tied to a requirement, a third negative / Baseline committed; delta lists the regressed ids; gate exits 1 / Card, golden set, and removal diff committed before the first run; hash on the card / Feature removed: the predicted cases go red, no others; restored: green / Model-in-the-loop cases run 3×, pass^3 reported / Judge from a different family, blinded, both orders, catches the planted error
- The constant-answer stub run finds a hollow case, and the case is fixed with a ledger event / Judge calibrated against 10 hand-labeled cases; misses recorded / A planted injection in an answer; judge fails it / Gate called by a pre-push hook; one real push refused and logged / Environment check: expected values and tests unreachable from the agent's tools

## Slide 24

### BEFORE

Card ten, an expansion of the envelope. The claim is the chapter's. Note the PRE-REGISTERED line, new this week: the threshold, the case count, the ids you predict will go red, and the removal diff are committed before Go, and the hash goes on the card. Five test points: green as built, red with the feature removed and exactly the predicted cases red, green again, a planted wrong answer failed by the grader or judge in both orders, and a constant-stub run that finds no hollow case. The falsifiers are the chapter's three plus moved goalposts. Abort covers a judge route that is down. The Chase signs the card commit before you fly and reads four results files, the delta, the exit codes, and the transcripts.

Cut from slide 24 (full wording):
- Flight Card 10 brief: Sortie 10, the gate that fails when it should
- FLIGHT CARD — SORTIE 10 : the gate that fails when it should / ENVELOPE            expansion / DESIGN CLAIM        The evaluation suite fails when it should: removing the feature, or planting a wrong /                     answer, turns the gate red. / SYSTEMS UNDER TEST  evals/golden.jsonl · evals/gate.py · baseline + delta · pre-push hook · judge (if any) / SUBSTRATE           repo + commit · model/route · judge model/route (other family) · sha256 of golden.jsonl / DEPENDS ON          Sortie 9 PASS (a second-family adversary refuted a planted falsehood) / PRE-REGISTERED      threshold, case count, predicted RED ids, removal diff: committed before Go; hash here /  / TEST POINTS /   1  gate on the build as it is            → exit 0; results.json; delta: 0 regressions /   2  feature removed (the named diff)      → exit 1; exactly the predicted ids RED; ledger event /   3  feature restored                      → exit 0; same ids green; delta shows the round trip /   4  one planted wrong answer              → grader/judge FAILs it; judge run in both orders agrees /   5  system replaced by constant stubs     → no case passes under every constant (no hollow case) /  / INSTRUMENTATION     results.json ×4 · delta.json · exit codes · judge transcripts (both orders) · ledger /  / PRE-REGISTERED FALSIFIERS (any ONE ⇒ FAIL) /   - a green gate with the feature removed /   - a judge that scores the planted error as correct, or flips when the order swaps /   - a golden case that cannot fail (passes under every constant stub) /   - threshold, cases, or baseline changed after the first run; passing by editing the golden set /  / ABORT (halt-not-fail)  judge route down or rate-limited: fly 1–3 and 5, record TP4 ABORTED, re-fly TP4 / CHASE               signs the card commit before the sortie; reads results ×4, delta, exit codes, judge /                     transcripts; the student's summary is not evidence /  / SPRINT (due Wed 11/11)  Sortie 10 log · eval suite + delta + RED witness on a gate · Design Analysis · AI_LOG

### AFTER

Card ten expands the envelope. The design claim is the chapter's. The PRE-REGISTERED line is new on this card: the threshold, the case count, the ids you predict will go red, and the removal diff are committed before Go, and the commit hash goes on the card. Five test points: the gate is green on the build as it is, red with the feature removed and exactly the predicted cases red, green again when the feature is restored, a planted wrong answer is failed by the grader or judge in both orders, and a constant-stub run finds no hollow case. The falsifiers are the chapter's three plus moved goalposts. The abort clause covers a judge route that is down. The Chase signs the card commit before you fly and reads the four results files, the delta, the exit codes, and the judge transcripts, because the card admits the evidence slice only and excludes your summary.

Cut from slide 24 (full wording):
- Flight Card 10 brief: Sortie 10, the gate that fails when it should
- FLIGHT CARD · SORTIE 10 : the gate that fails when it should / ENVELOPE            expansion / DESIGN CLAIM        The evaluation suite fails when it should: removing the feature, or planting a wrong /                     answer, turns the gate red. / SYSTEMS UNDER TEST  evals/golden.jsonl · evals/gate.py · baseline + delta · pre-push hook · judge (if any) / SUBSTRATE           repo + commit · model/route · judge model/route (other family) · sha256 of golden.jsonl / DEPENDS ON          Sortie 9 PASS (a second-family adversary refuted a planted falsehood) / PRE-REGISTERED      threshold, case count, predicted RED ids, removal diff: committed before Go; hash here /  / TEST POINTS /   1  gate on the build as it is            → exit 0; results.json; delta: 0 regressions /   2  feature removed (the stated diff)     → exit 1; exactly the predicted ids RED; ledger event /   3  feature restored                      → exit 0; same ids green; delta shows the round trip /   4  one planted wrong answer              → grader/judge FAILs it; judge run in both orders agrees /   5  system replaced by constant stubs     → no case passes under every constant (no hollow case) /  / INSTRUMENTATION     results.json ×4 · delta.json · exit codes · judge transcripts (both orders) · ledger /  / PRE-REGISTERED FALSIFIERS (any ONE ⇒ FAIL) /   - a green gate with the feature removed /   - a judge that scores the planted error as correct, or flips when the order swaps /   - a golden case that cannot fail (passes under every constant stub) /   - threshold, cases, or baseline changed after the first run; passing by editing the golden set /  / ABORT (halt-not-fail)  judge route down or rate-limited: fly 1–3 and 5, record TP4 ABORTED, re-fly TP4 / CHASE               signs the card commit before the sortie; reads results ×4, delta, exit codes, judge /                     transcripts; the student's summary is not evidence /  / SPRINT              Sortie 10 log · eval suite + delta + RED witness on a gate · Design Analysis · AI_LOG

## Slide 25

### BEFORE

The lab. It is self-guided and uses a toy: a function that classifies a tool call's effect class, from E3, eight golden cases, and a gate script that uses only the standard library. You pre-register a prediction and commit it, run green, remove the feature, compare, restore, then run a constant-stub check that finds the hollow case I planted. The last step uses OpenCode as a judge on a planted wrong answer in both orders; small free models are welcome here, because a judge that flips is a finding. No local model is needed. Commit the lab folder and the worksheet with a ledger event.

Cut from slide 25 (full wording):
- Lab (6:00–6:30, self-guided): a RED witness in thirty minutes
- 0–3 Copy the toy feature, golden set, and gate into evolution-10/lab/. / 3–8 Pre-register: write prediction.md (which ids go red, threshold); commit; note the hash. / 8–13 Run green; write the baseline. / 13–18 Remove the feature (two marked lines); run; compare with the prediction; restore. / 18–22 Run the constant-stub check; find the hollow case; fix it; rerun. / 22–28 Judge probe: OpenCode judges a planted wrong answer in both orders; check it against the golden. / 28–30 Commit; ledger event.
- evolution-10/lab/: feature.py, golden.jsonl, gate.py, prediction.md, baseline.json, results.json from each run, and the filled worksheet (lab-worksheet.md). / The worksheet records: the prediction hash, the ids that went red, the hollow case and its fix, the model id, and the judge's verdicts in both orders. / The full test points fly in the Sprint, against your own system. The lab's toy is the rehearsal.

### AFTER

The lab is self-guided and uses a toy: a function from E3 that classifies a tool call's effect class, eight golden cases, and a gate script that uses only the standard library. You pre-register a prediction and commit it, run green, remove the feature, compare the red ids with the prediction, restore, and then run a constant-stub check that finds the hollow case I planted. The last step uses OpenCode as a judge on a planted wrong answer in both orders; a small free model serves here, because a judge that flips between orders is a finding you record. The lab needs no local model. Commit the lab folder and the worksheet with a ledger event.

Cut from slide 25 (full wording):
- Self-guided lab: a RED witness in thirty minutes
- Copy the toy feature, golden set, and gate into evolution-10/lab/. / Pre-register: write prediction.md (which ids go red, threshold); commit; note the hash. / Run green; write the baseline. / Remove the feature (two marked lines); run; compare with the prediction; restore. / Run the constant-stub check; find the hollow case; fix it; rerun. / Judge probe: OpenCode judges a planted wrong answer in both orders; check it against the golden. / Commit; ledger event.
- evolution-10/lab/: feature.py, golden.jsonl, gate.py, prediction.md, baseline.json, results.json from each run, and the filled worksheet (lab-worksheet.md). / The worksheet records: the prediction hash, the ids that went red, the hollow case and its fix, the model id, and the judge's verdicts in both orders. / The full test points fly in the Sprint, against your own system. The lab's toy feature serves as a rehearsal for that flight.

## Slide 26

### BEFORE

The Sprint. Five deliverables, the ones on the run sheet. The Go/No-Go is written: commit your card, golden set, and prediction by Friday night; your Chase commits GO or NO-GO with a reason by Saturday at six. You fly after GO, in one sitting, on the committed hash. Your Chase writes the verdict from the evidence slice by Wednesday at six, and you debrief before 11:59. The strip is the distinction to keep straight: a FAIL disproves the claim; an ABORT is infrastructure, and it is re-flown.

Cut from slide 26 (full wording):
- Homework: the Sprint, due Wed 11/11, 11:59 p.m.
- Commit the card, golden set, and prediction by Fri 11/06, 11:59 p.m. Your Chase reads the card in the repo and commits GO or NO-GO with one reason by Sat 11/07, 6:00 p.m. No sortie before GO.
- Fly the five test points after GO, in one sitting, on the committed hash. Capture results, delta, exit codes, and judge transcripts to evolution-10/evidence/.
- By Wed 11/11, 6:00 p.m., the Chase reads the evidence slice only and writes the verdict (PASS / FAIL) in the log with one line of reasons. Then you debrief.
- FAIL is the claim disproved; ABORT is a halt for reasons unrelated to the claim (judge route down). An ABORT is re-flown, not argued.

### AFTER

The Sprint has five deliverables, listed on the slide. The Go/No-Go is written and asynchronous: commit your card, golden set, and prediction; your Chase reads them in the repository and commits GO or NO-GO with one reason. You fly after GO, in one sitting, on the committed hash. Your Chase writes the verdict from the evidence slice alone, and then you debrief. The strip holds the distinction to keep straight: a FAIL means the evidence disproved the claim, and an ABORT means the infrastructure halted the sortie for a reason unrelated to the claim, so an ABORT is re-flown.

Cut from slide 26 (full wording):
- The Sprint brief
- Commit the card, golden set, and prediction first. Your Chase reads the card in the repo and commits GO or NO-GO with one reason. No sortie before GO.
- Fly the five test points after GO, in one sitting, on the committed hash. Capture results, delta, exit codes, and judge transcripts to evolution-10/evidence/.
- The Chase reads the evidence slice only and writes the verdict (PASS / FAIL) in the log with one line of reasons. Then you debrief.
- FAIL means the evidence disproved the claim. ABORT is a halt for reasons unrelated to the claim (judge route down). Re-fly an ABORT. Do not argue it into a PASS.

## Slide 27

### BEFORE

Close. A check you have never seen fail is not yet evidence. Write the falsifier first, watch the gate go red with the feature removed, and let your Chase, a person, sign the PASS. Sources used for this deck, checked 09/24/2026: OpenAI, Why SWE-bench Verified no longer measures frontier coding capabilities, https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ ; OpenAI, Introducing SWE-bench Verified, https://openai.com/index/introducing-swe-bench-verified/ ; Jimenez et al., https://arxiv.org/abs/2310.06770 ; SWE-Bench Pro, https://arxiv.org/abs/2509.16941 ; SWE-Bench Pro Verified, https://arxiv.org/abs/2609.08149 ; Cursor, Reward hacking, https://cursor.com/blog/reward-hacking-coding-benchmarks ; Wang et al., How we broke top AI agent benchmarks, https://moogician.github.io/blog/2026/trustworthy-benchmarks-cont/ ; Zhu et al., ABC, https://arxiv.org/abs/2507.02825 ; GAIA, https://arxiv.org/abs/2311.12983 ; WebArena, https://arxiv.org/abs/2307.13854 ; AgentBench, https://arxiv.org/abs/2308.03688 ; τ-bench, https://arxiv.org/abs/2406.12045 ; τ²-bench, https://arxiv.org/abs/2506.07982 ; tau2-bench repo, https://github.com/sierra-research/tau2-bench ; Zheng et al., https://arxiv.org/abs/2306.05685 ; Wang et al. 2023, https://arxiv.org/abs/2305.17926 ; Panickssery et al., https://arxiv.org/abs/2404.13076 ; Wataoka et al., https://arxiv.org/abs/2410.21819 ; Anthropic, Demystifying evals for AI agents, https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents ; Nosek et al. 2018, https://www.pnas.org/doi/10.1073/pnas.1708274114 ; Kerr 1998, https://journals.sagepub.com/doi/10.1207/s15327957pspr0203_4 ; OpenCode Go, https://opencode.ai/docs/go/ ; OpenCode CLI, https://opencode.ai/docs/cli/ . gzkit facts are from the course topic guide and carry verify markers.

Cut from slide 27 (full wording):
- Write the falsifier first. Remove the feature and watch the gate go red. Let a person, not a model, sign the PASS. Lab at six: the RED witness, in thirty minutes.

### AFTER

Close. A check you have never seen fail is not yet evidence, because its green light would look the same if it could not fail. Write the falsifier first, watch the gate go red with the feature removed, and let your Chase, a person, sign the PASS. Sources used for this deck, checked 09/24/2026: OpenAI, Why SWE-bench Verified no longer measures frontier coding capabilities, https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ ; OpenAI, Introducing SWE-bench Verified, https://openai.com/index/introducing-swe-bench-verified/ ; Jimenez et al., https://arxiv.org/abs/2310.06770 ; SWE-Bench Pro, https://arxiv.org/abs/2509.16941 ; SWE-Bench Pro Verified, https://arxiv.org/abs/2609.08149 ; Cursor, Reward hacking, https://cursor.com/blog/reward-hacking-coding-benchmarks ; Wang et al., How we broke top AI agent benchmarks, https://moogician.github.io/blog/2026/trustworthy-benchmarks-cont/ ; Zhu et al., ABC, https://arxiv.org/abs/2507.02825 ; GAIA, https://arxiv.org/abs/2311.12983 ; WebArena, https://arxiv.org/abs/2307.13854 ; AgentBench, https://arxiv.org/abs/2308.03688 ; τ-bench, https://arxiv.org/abs/2406.12045 ; τ²-bench, https://arxiv.org/abs/2506.07982 ; tau2-bench repo, https://github.com/sierra-research/tau2-bench ; Zheng et al., https://arxiv.org/abs/2306.05685 ; Wang et al. 2023, https://arxiv.org/abs/2305.17926 ; Panickssery et al., https://arxiv.org/abs/2404.13076 ; Wataoka et al., https://arxiv.org/abs/2410.21819 ; Anthropic, Demystifying evals for AI agents, https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents ; Nosek et al. 2018, https://www.pnas.org/doi/10.1073/pnas.1708274114 ; Kerr 1998, https://journals.sagepub.com/doi/10.1207/s15327957pspr0203_4 ; OpenCode Go, https://opencode.ai/docs/go/ ; OpenCode CLI, https://opencode.ai/docs/cli/ . gzkit facts are from the course topic guide and carry verify markers.

Cut from slide 27 (full wording):
- Write the falsifier first. Remove the feature and watch the gate go red. Have a person sign the PASS. A model's verdict counts only as evidence. In the self-guided lab, build a RED witness in thirty minutes.

