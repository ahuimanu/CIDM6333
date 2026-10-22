# mini-attention-2017: speaker notes, before and after the voice pass

## Slide 1

### BEFORE

Twenty minutes on one paper. We read "Attention Is All You Need" the way we read every system in this course: as a design document. What constraint did the authors face, what did they trade, and what evidence did they offer? The model behind OpenCode and Big Pickle is a descendant of this design. The three explainer figures on the course site carry everything I show tonight, so you can step through them later.

### AFTER

This mini lecture spends twenty minutes on one paper. It reads "Attention Is All You Need" the way this course reads every system, as a design document, which means asking three questions of it: what constraint the authors faced, what they traded to escape it, and what evidence they offered for the trade. The model behind OpenCode and Big Pickle descends from this design, so the answers describe the thing your harness calls. The three explainer figures on the course site carry every picture in this lecture, so you can step through each one later at your own pace.

## Slide 2

### BEFORE

Five moves. The constraint first, because a design makes sense only against the problem it answers. Then the mechanism, then the evidence, which is the part most summaries skip. Then what chat models kept from the 2017 design, and finally why any of it matters to someone building a harness.

### AFTER

The lecture runs in five parts. The constraint comes first, because a design makes sense only against the problem it answers. The mechanism comes second and the evidence third. The evidence gets a part of its own because the paper's tables, rather than its diagram, are what this course reuses. The fourth part states what chat models kept from the 2017 design, and the fifth draws five lines from the paper to the Evolutions that depend on it.

## Slide 3

### BEFORE

Read the highlighted row against the recurrent row. Self-attention gives up a constant amount of sequential work and a constant path length between any two words, which is why it trains fast on GPUs and why distant words can affect each other. The price is n squared times d per layer. The paper argues that price is fine when n is smaller than d, which was true of 2017 sentences. Keep that sentence in mind: it stopped being true when context windows reached a million tokens, and that is the cost Evolution 6 asks you to budget.

Cut from slide 3 (full wording):
- What the authors faced / A recurrent network reads token 1, then token 2, then token 3. Each step waits for the one before it, so training cannot spread a sentence across a GPU. / The paper's trade: let every position look at every other position at once. The sequential chain drops from O(n) to O(1); the compute per layer grows with n².

### AFTER

Read the highlighted row against the recurrent row. Self-attention spends a constant number of sequential steps per layer and keeps a constant path length between any two words, which is why it trains fast on GPUs and why distant words can affect each other. The price is n squared times d of compute per layer. The paper argues that the price is acceptable when n is smaller than d, and in 2017 a sentence of about 30 tokens against a width of 512 met that condition. The condition no longer holds. A context window of a million tokens puts n far past d, and the n squared term becomes the cost Evolution 6 asks you to budget.

Cut from slide 3 (full wording):
- What the authors faced / A recurrent network reads token 1, then token 2, then token 3. Each step waits for the one before it, so training cannot spread a sentence across a GPU. / The authors let every position attend to every other position at once. This change cuts the sequential chain from O(n) to O(1), and in exchange the compute per layer grows with n².

## Slide 4

### BEFORE

This is the paper's Figure 1 redrawn. The left stack reads the source sentence; the right stack writes the target. Each stack repeats one layer six times. Notice there is no arrow from the top back to the bottom in the paper, yet section 3 says the model is auto-regressive: it consumes what it generated. That missing arrow is the inner loop from Figure 01, Two Loops. Figure 01b on the course site steps through every box with the paper's own words.

Cut from slide 4 (full wording):
- Figure 1, redrawn: two stacks and a loop the paper describes

### AFTER

The slide redraws the paper's Figure 1. The left stack, the encoder, reads the source sentence, and the right stack, the decoder, writes the target one token per pass. Each stack repeats one layer six times. The paper's figure draws no arrow from the top of the decoder back to its bottom, yet section 3 says the model is auto-regressive, consuming the symbols it has already generated as input for the next. The dashed arrow on the slide draws that return path, and it is the inner loop of Figure 01, Two Loops. Figure 01b on the course site steps through every box with the paper's own words.

Cut from slide 4 (full wording):
- Figure 1, redrawn: two stacks and a loop the paper describes

## Slide 5

### BEFORE

One line of math. Queries, keys, and values are three projections of the same input. The dot product of a query with every key gives a score; softmax turns scores into weights; the weights mix the values. The paper makes two choices worth naming. It divides by the square root of d_k because large dot products saturate softmax. And in the decoder it masks the future by setting those scores to minus infinity. The grid on the right uses random vectors, so it shows the arithmetic, not meaning. In Figure 01b, switch scaling off and raise d_k: the rows collapse onto one key, which is the saturation the paper describes.

### AFTER

The mechanism is one line of math. In self-attention the queries, keys, and values are three projections of the same input. The dot product of a query with every key gives a score, softmax turns the scores into weights that sum to one, and the weights mix the values into the output for that query. The paper makes two choices inside that line, and each has a reason. It divides the scores by the square root of d_k because large dot products push softmax into regions where the gradients are too small to train on. In the decoder it sets the scores for later positions to minus infinity before softmax, so each position predicts from earlier positions only. The grid on the right is computed from random vectors, so it shows the arithmetic of the weights and nothing about language. In Figure 01b you can switch scaling off and raise d_k, and the rows then collapse onto one key, which is the saturation the paper describes.

## Slide 6

### BEFORE

Two more pieces. Multi-head attention runs eight smaller attentions side by side, each 64 wide, so the total work equals one 512-wide head; the heads can specialize. Table 3 tested this: one head loses 0.9 BLEU, and too many heads also hurt. Second, attention by itself has no idea of word order. The paper adds a fixed pattern of waves to each token vector, fast waves in the low dimensions and slow waves in the high ones. Learned positions worked about as well. Many newer models encode position differently, but the problem is the same one.

Cut from slide 6 (full wording):
- Eight heads at once, and word order written in waves

### AFTER

Two more pieces complete the mechanism. Multi-head attention runs eight smaller attentions side by side, each 64 wide, so the total work equals one 512-wide head, and each head can learn a different pattern of attention. Table 3 row A tests the count: one head loses 0.9 BLEU against the base model, and 32 heads also score lower. Second, attention by itself has no notion of word order, because the weighted sum treats the positions as a set. The paper therefore adds a fixed pattern of sine and cosine waves to each token vector, fast waves in the low dimensions and slow waves in the high ones, so that each position carries a distinct signature. Table 3 row E shows that learned positions scored about the same. Later models encode position by other methods (rotary embeddings, for example), and the reason for adding a position signal is unchanged.

Cut from slide 6 (full wording):
- Eight attention heads, and word order encoded as sine and cosine waves

## Slide 7

### BEFORE

Table 2 is the headline. The big Transformer scores 28.4 BLEU on English to German, more than two points above everything before it, ensembles included. The base model already beats them. Now look at how the paper reports cost: it does not claim a measured number. It multiplies training time by the number of GPUs by each GPU's rated throughput, and it prints the rated throughputs in a footnote. You can recompute it: 12 hours times 3600 times 8 GPUs times 9.5 teraflops is about 3.3 times ten to the eighteenth. A number with its method beside it is a receipt. And notice the French result: the table says 41.8 and the text says 41.0. Even a famous paper has a mismatch; the table is the table of record. Figure 01c on the course site plots this against cost on a log scale.

Cut from slide 7 (full wording):
- Evidence 1: better translations at a fraction of the training cost

### AFTER

Table 2 carries the headline result. The big Transformer scores 28.4 BLEU on English to German, more than 2.0 BLEU above every earlier result, ensembles included, and the base model already beats them. The paper reports cost by a method this course reuses. The authors do not claim a measured FLOP count. They multiply training time by the number of GPUs by each GPU's rated throughput, and they print the rated throughputs in a footnote. You can recompute the base figure: 12 hours times 3600 seconds times 8 GPUs times 9.5 teraflops is about 3.3 times ten to the eighteenth. A number with its method printed beside it is what this course calls a receipt. The French result gives a second lesson in reading tables. Table 2 says 41.8 and the text of section 6.1 says 41.0, and when a table and its text disagree, cite the table and record the discrepancy beside it, as the slide does. Figure 01c on the course site plots BLEU against cost on a log scale.

Cut from slide 7 (full wording):
- Evidence 1: translation quality and training cost

## Slide 8

### BEFORE

Table 3 is my favorite part of the paper because it is an evaluation design. Each row changes one thing against the same base model, and every score comes from a development set, not the test set used in Table 2. Read the bars: two layers instead of six costs 2.1 BLEU; turning off dropout costs 1.2; one head costs 0.9; a bigger model gains a little. Learned positions change almost nothing. That is the shape of the delta gate you build in Evolution 10: fixed baseline, one change, held-out set, and a threshold you commit to before you look. Ask yourself which of these rows you would believe from a single run.

Cut from slide 8 (full wording):
- Evidence 2: change one thing, measure against a fixed base

### AFTER

Table 3 is an evaluation design, and it is the part of the paper this course reuses most directly. Each row changes one thing against the same base model, and every score comes from the development set, newstest2013, rather than the test set Table 2 reports on. Read the bars: two layers instead of six cost 2.1 BLEU, dropout turned off costs 1.2, one head costs 0.9, and the big model gains a little. Learned positions change almost nothing. That is the shape of the delta gate you build in Evolution 10: a fixed baseline, one change at a time, a held-out set, and a threshold you commit to before you look at the result. The table reports one number per row and no measure of run-to-run noise, so before you trust a row, decide which of these deltas you would accept from a single run.

Cut from slide 8 (full wording):
- Evidence 2: one change at a time, measured against a fixed base model

## Slide 9

### BEFORE

The architecture does not train itself. Equation 3 raises the learning rate in a straight line for the first 4,000 steps and then lets it fall with the inverse square root of the step. The grey line shows a longer warmup: a lower peak, reached later. The rest of the recipe matters as much: Adam with an unusual beta two of 0.98, dropout everywhere, and label smoothing, which the paper admits makes perplexity worse while BLEU improves. When you compare models in Evolution 10, you compare recipes too.

Cut from slide 9 (full wording):
- The rest of the recipe / Adam with β₁ = 0.9, β₂ = 0.98, ε = 10⁻⁹. / Dropout 0.1 on every sub-layer output and on the embeddings. / Label smoothing 0.1: it "hurts perplexity, as the model learns to be more unsure, but improves accuracy and BLEU score." / Base: 100,000 steps. Big: 300,000 steps.

### AFTER

The results in Tables 2 and 3 depend on a training recipe as much as on the architecture. Equation 3 raises the learning rate in a straight line for the first 4,000 warmup steps and then lets it fall with the inverse square root of the step number. The grey line on the slide shows a longer warmup, which reaches a lower peak later. The rest of the recipe sits in section 5: Adam with beta two set to 0.98 rather than the usual 0.999, dropout of 0.1 on every sub-layer output and on the embeddings, and label smoothing of 0.1, which the paper says hurts perplexity while it improves accuracy and BLEU. A reported result is therefore the architecture plus its recipe, and when you compare two models in Evolution 10 you compare two recipes as well.

Cut from slide 9 (full wording):
- The rest of the recipe / Adam with β₁ = 0.9, β₂ = 0.98, ε = 10⁻⁹. / Dropout 0.1 on every sub-layer output and on the embeddings. / Label smoothing 0.1: it "hurts perplexity, as the model learns to be more unsure, but improves accuracy and BLEU score." / Base: 100,000 steps. Big: 300,000 steps.

## Slide 10

### BEFORE

Here is the same figure with the encoder faded out. GPT in 2018 kept only the right-hand column: embeddings, masked self-attention, feed-forward, add and norm, and the softmax head. The prompt and the reply become one sequence. Two other changes matter to you. Chat models sample their next token instead of running beam search, so output varies from run to run; that is why one run is an anecdote in Evolution 10. And most later models move the normalization step before each sub-layer, which trains more stably at depth.

### AFTER

The slide shows the same figure with the encoder faded out. GPT (Radford et al., 2018) kept only the right-hand column: token embeddings with position, masked self-attention, the feed-forward layer with add and norm, and the linear and softmax head over the vocabulary. The prompt and the reply become one sequence, and the model reads all of it and writes the next token on each pass. Two further changes reach your harness. Chat models sample the next token instead of running beam search, so the same prompt can produce different output from run to run, and for this reason one run counts as an anecdote in Evolution 10. GPT-2 (Radford et al., 2019) moved the normalization step to the input of each sub-layer, and the models that followed kept that placement because it trains more stably at depth.

## Slide 11

### BEFORE

Five lines from the paper to this course. The n squared term is your context budget. The softmax at the top of Figure 1 is where the paper stops and your harness starts: reading the reply, gating the tool call, feeding the result back, deciding when to halt. Sampling is why you run evals more than once. Table 3 is the model for your delta gate. And the cost estimate is a model for every number you put in a flight log: show the method so your Chase can recompute it.

Cut from slide 11 (full wording):
- A tool call is text the model wrote. Only your harness runs it, after the gate.
- One run is an anecdote. Run the golden set several times and gate on the delta.

### AFTER

The last slide draws five lines from the paper to this course. The n squared term in Table 1 is the context budget of Evolution 6, because every token you add to the window raises the cost of every later call. The output probabilities at the top of Figure 1 are where the paper stops and your harness starts: the harness reads the reply, gates any tool call the model wrote, feeds the result back as the next input, and decides when to halt (Evolutions 1 and 3). Sampling is the reason Evolution 10 has you run the golden set more than once and gate on the delta. Table 3 supplies the shape of that delta gate: one change, a fixed base, a held-out set, and a threshold fixed in advance. The paper's cost estimate supplies the shape of every number in a flight log (Evolution 11): print the method beside the number so your Chase can recompute it.

Cut from slide 11 (full wording):
- A tool call is text the model wrote. Only your harness runs it, after the gate.
- A single run cannot separate a real change from run-to-run variation. For this reason, run the golden set several times and gate on the delta.

## Slide 12

### BEFORE

One sentence to carry out: a design document names its constraint, its trade, and its evidence. Use that test on every system in your Design Analysis this week. The three figures on the course site let you step through everything we covered at your own pace. Read the paper itself too; it is fifteen pages, and Table 3 alone is worth the time.

Cut from slide 12 (full wording):
- A design document names its constraint, its trade, and its evidence. This one did all three.
- Figure 01 · Two Loops: the model inside the agent loop / Figure 01b · The 2017 Transformer: Figure 1 step by step, decoder-only switch, live attention / Figure 01c · The Transformer's Evidence: Tables 2–4, the schedule, the attention pictures / ahuimanu.github.io/CIDM6333 · Vaswani et al. (2017), arXiv:1706.03762

### AFTER

This lecture applied one test to the paper, and the test transfers: a design document states its constraint, its trade, and its evidence, and "Attention Is All You Need" did all three. Apply the same test to each system in your Design Analysis. The three figures on the course site let you step through every picture from this lecture at your own pace. Read the paper itself as well: it runs fifteen pages, and Table 3 is the part the delta gate of Evolution 10 is modeled on.

Cut from slide 12 (full wording):
- A design document states its constraint, its trade, and its evidence, and Vaswani et al. state all three.
- Figure 01 · Two Loops: the model inside the agent loop / Figure 01b · The 2017 Transformer: Figure 1 step by step, decoder-only switch, live attention / Figure 01c · The Transformer's Evidence: Tables 2–4, the schedule, the attention pictures / ahuimanu.github.io/CIDM6333 · Vaswani et al. (2017), arXiv:1706.03762

