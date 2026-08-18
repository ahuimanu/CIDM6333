# Vibe Coding the Photo App: Three Approaches for the System Design Learner

Companion to *System Design Fundamentals: A Beginner's Syllabus* and its supporting materials.

## The premise, stated honestly

"Vibe coding" — Karpathy's term for building by prompting an AI, accepting its output largely on trust, and iterating by feel rather than by reading the code — is now how many learners will first encounter every concept in this course. That is neither a catastrophe nor a free lunch. It is a change in *where the learning can happen*.

The course's pedagogy is failure-driven: every component earns its place by fixing a visible failure. Vibe coding threatens that pedagogy in one specific way — **an AI assistant will happily generate the fix before the learner has ever experienced the failure.** Ask for "a photo-sharing app that scales" and you'll receive a load balancer, Redis, and read replicas on day one, unearned. The system works; the learner has no theory of why any of it is there. The three approaches below differ mainly in how they handle this problem: the first ignores it deliberately, the second engineers around it, the third refuses to let it arise.

A second premise: vibe coding does not remove judgment from the loop, it *relocates* it. The judgment moves out of syntax and into specification, verification, and interrogation. Each approach exercises a different one of those three.

---

## The three approaches at a glance

| | **A. The Vibe Sprint** | **B. The Failure Harness** | **C. The Architect's Seat** |
|---|---|---|---|
| One-line description | Generate the whole app fast; iterate by demoing | AI builds the system; *you* build the instruments that break it | You write the spec and interrogate every generated component |
| Primary output | A running prototype | A proof of concept with evidence | Understanding, plus a well-documented system |
| Where your judgment lives | Product feel ("is this right?") | Verification ("is this true?") | Specification ("is this what I meant?") |
| Time to something running | Hours | Days | A week or more |
| Failure visibility | Hidden until real load exists | The entire point | Reasoned about before encountered |
| Learning depth | Shallow but broad; great map, no territory | Deep on operations and non-functional behavior | Deep on structure, trade-offs, and data modeling |
| Course units it serves best | 1–2, 8 (seeing the whole shape) | 7, 9–10, 13–16 (everything with a lab) | 4–6, 11–12 (requirements, modeling, DB choice) |
| Chief risk | Fluent ignorance — you can demo it, not defend it | Harness-building becomes its own rabbit hole | Analysis paralysis; never shipping |
| Best used for | Quick prototype, motivation, scoping | Proof of concept | Durable learning |

These are phases as much as alternatives. A sensible pass through the course uses A once, B repeatedly, and C for the units where the thinking *is* the deliverable.

---

## Approach A — The Vibe Sprint (optimized for the quick prototype)

**What it is.** One session, one prompt lineage, one goal: a photo app you can click. You do not read the generated code except when it breaks. You steer by behavior.

**Principles that make prototypes fast (and honest about being prototypes):**

1. **One box, on purpose.** Constrain the AI to the course's Unit 1 starting point: single process, SQLite or a single Postgres container, local disk for photos. This is not a limitation to apologize for — it is the correct architecture for the requirements you actually have (zero users). Prompting "keep it to one deployable unit, no cloud services" produces dramatically more comprehensible output than "make it scalable."
2. **Regenerate, don't repair.** When a generated feature is wrong, re-prompt from the spec rather than hand-patching. Hand-patching vibe-coded output gives you the worst of both worlds: code you didn't write *and* can no longer regenerate.
3. **Timebox and demo.** Two hours, then show it to someone. The prototype's job is to make the requirements conversation concrete (Unit 4), not to survive.
4. **Fake the scale.** You don't have 10,000 users, but a 20-line load script pretending to be them costs one more prompt. Even in the sprint, ask for it — it's the seed of Approach B.
5. **Declare it disposable — and mean it.** The single most common vibe-coding failure mode is the prototype that quietly becomes production. Write "THROWAWAY" in the README in the first commit. If the prototype turns out to matter, that's your signal to switch to Approach C and re-derive it, not to keep patching.

**Guidance for use.** Run the sprint *before* Unit 1, not after Unit 16. Its pedagogical value is anticipatory: having clicked around your own single-box app, every subsequent failure in the course has a referent. Keep a single artifact from the sprint — the list of things you noticed were slow, ugly, or fragile. That list is your personal version of the course's "three founding failures," and it will make Unit 2 land differently.

**What it cannot give you.** Any defensible answer to "why is this component here?" A learner who stops at Approach A can produce systems and cannot answer for them — precisely the interview failure the course's altitude and requirements bytes warn about.

---

## Approach B — The Failure Harness (optimized for the proof of concept)

**What it is.** An inversion of labor. The AI writes the application and infrastructure; the learner personally builds the *instruments* — load generators, chaos scripts, dashboards, timing probes — and then recreates each of the course's failures against the AI-built system, on schedule, on purpose. Kill a container mid-request (Lab 1). Load five million rows and watch the unindexed query crawl (Lab 2). Expire the hot cache entry under concurrent load and produce your own stampede (Unit 14). Run the bad DELETE and watch the replica obediently destroy itself (Unit 15).

**Why this is the PoC approach.** A proof of concept is not a small prototype; it is an *argument with evidence*. The difference is a falsifiable claim. Principles:

1. **State the claim before building.** Not "add Redis" but "adding a cache with a 60-second TTL will cut p95 feed latency from ~300ms to under 50ms at 200 requests/second, at the cost of up to 60 seconds of staleness." A PoC without a number attached proves only that software can exist.
2. **Instrument before you optimize.** The measurement harness is built and baselined *before* the component under test is added. Otherwise you have no before, and a PoC with no before is a demo.
3. **Real components, minimal everything else.** Use actual Redis, actual Postgres replication, actual NGINX — the behaviors under study (lag, stampedes, failover timing) live in the real implementations and cannot be mocked. But one docker-compose file, seeded synthetic data, no auth, no UI beyond curl.
4. **Reproducibility is the deliverable.** `git clone && docker compose up && make prove` should reproduce the claim on someone else's machine. A PoC that only ran once on your laptop proved a concept to an audience of one.
5. **Document the negative space.** What the PoC deliberately does *not* prove (e.g., "single-node Redis; says nothing about cache cluster behavior"). This is the difference between a PoC and a pitch.

**Guidance for use.** This is the approach for Units 9–16, run as an expansion of the four free labs. The division of labor is the safeguard: because *you* wrote the load generator and the probes, you cannot be fooled by the AI's confident narration of what its own code does — you have independent instruments. When the AI's explanation and your dashboard disagree, believe the dashboard, then make the AI reconcile the two. That reconciliation loop is where most of the learning happens.

**Chief risk and its control.** Harness-building is seductive and can consume the course (a week perfecting the load generator, no failures yet induced). Control it the same way you control the prototype: the harness is also vibe-coded where possible, and each unit's experiment gets a timebox. The learner's hand-built share should be the *smallest* instrument that makes the failure undeniable.

---

## Approach C — The Architect's Seat (optimized for learning how it all works)

**What it is.** The learner never asks for code first. For each unit, the sequence is: write the access patterns and requirements yourself (Units 4–5, 11, longhand); make the design decision yourself and record it with its rejected alternatives; *then* commission the AI to build exactly that, one component at a time; then interrogate what came back until you could re-derive it.

**Principles that convert generation into learning:**

1. **Predict before you run.** Before executing anything generated, write down what will happen — which server answers, what the query plan is, what breaks at 10x load. Prediction converts passive reading into a test of your model, and a wrong prediction is worth more than ten right ones.
2. **The re-explanation gate.** No generated component is accepted until you can explain it to the AI *with the code closed* — and it agrees your account is accurate. What you cannot re-explain, you do not merge. This is the working definition of understanding the course is after: the theory of the system living in a head, not only in a repo.
3. **One component per conversation.** Generating the load balancer config, the session store, and the replica setup in one prompt produces a system; generating them in three interrogated steps produces a systems engineer.
4. **Keep a decision log.** One short record per choice: the question, the options, the trade-off taken, the requirement that justified it (mirroring Interview Byte 2 — every component justified by an earlier answer). Six weeks later this log *is* your interview preparation.
5. **Alternate assisted and unassisted deliberately.** Periodically delete one AI-built component and rewrite it by hand — the session-store logic, or the modulo shard router — then diff yours against the generated one and make the AI adjudicate the differences. Scheduled alternation between assisted and unassisted work is what keeps the theory in your head current with the system on disk; unbroken assistance lets the two quietly diverge until the first real incident reveals the gap.
6. **Use the AI as examiner, not only as builder.** After each unit, have it interrogate *you*: "ask me five hard questions about my replication setup and grade my answers against my own decision log." The same model that hid the failures in Approach A becomes a tireless oral examiner in Approach C.

**Guidance for use.** This is the slow path and the only one that fully survives contact with an interview or an incident. Reserve it for the units where the artifact is a decision rather than a deployment: requirements (4–5), monolith vs. microservices (6), data modeling (11), SQL vs. NoSQL (12), and the sharding decision (16). Running Approach C on *everything* is how learners burn out; running it on nothing is how they become fluent operators of systems they cannot explain.

**Chief risk and its control.** Perfectionism at the spec stage — three days on access patterns, no running system, motivation gone. Control: every Approach C unit ends with commissioned, running code. The seat is only worth sitting in if the building actually gets built.

---

## Comparing the three: what each one actually teaches

**Speed vs. residue.** A is fastest and leaves the least residue in the learner; C is slowest and leaves the most; B sits between, and its residue is of a distinct kind — operational intuition, the feel of a p95 curve bending or a replica falling behind, which neither A nor C produces. A learner who has only done C can *explain* a cache stampede; one who has done B has *caused* one and watched the graph. Interviews reward the first; incidents reward the second.

**Where the AI can fool you.** In A, completely — you have neither spec nor instruments, only vibes. In B, not about behavior — your instruments are independent — but possibly about mechanism (the dashboard shows the fix worked; the AI's story of *why* may still be wrong, so push on it). In C, not about design — the design is yours — but possibly in implementation details you accepted at the re-explanation gate without probing. No approach eliminates verification; each narrows what needs verifying.

**Failure timing.** A defers failures (they arrive later, in production, unnamed). B schedules them (they arrive on Tuesday, instrumented, with a name from the vocabulary checklist). C prevents some and predicts the rest. The course's whole theory is that named, witnessed failure is the unit of learning — which is why B is the spine of this curriculum and the other two are its bookends.

**Honest sequencing for one learner, sixteen units:**

1. **Week 0 — Approach A.** One vibe sprint. Get the map, keep the fragility list, mark it throwaway.
2. **Units 4–6, 11–12 — Approach C.** The decisions. Spec, decide, commission, interrogate, log.
3. **Units 7, 9–10, 13–16 — Approach B.** The failures. For each: claim → baseline → break → fix → measure → reconcile.
4. **Capstone — all three.** Vibe-sprint a *second* app in a different domain (Unit 5's ride-hailing variant works); run only the two Approach B experiments its requirements most demand; write the Approach C decision log from memory first, then check it against the system. The distance between the log and the system is your remaining coursework.

## One closing principle that governs all three

Whatever the approach, the constant is this: **the learner must always own at least one of the three seats — specification, verification, or interrogation — and know which one they're in.** Vibe coding fails learners not when the AI writes the code, but when the learner holds none of the seats and mistakes the ride for the driving. The three approaches are simply three defensible answers to "which seat, when."
