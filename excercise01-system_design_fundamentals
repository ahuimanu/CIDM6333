# System Design Fundamentals: A Beginner's Syllabus

**Format:** Case-driven — one application (a photo-sharing app) is designed and progressively hardened. Every component is introduced only when a concrete failure demands it.

**Pedagogical thread:** Failure → named problem → fix → new problem introduced by the fix. Students learn by watching the system break, not by memorizing diagrams.

**Course-level outcomes.** By the end, a student should be able to:

1. Explain what system design is and why it becomes the engineer's job as seniority increases.
2. Derive architecture decisions from requirements and access patterns rather than from buzzwords.
3. Trace a request end-to-end from a user's device to a database and back.
4. Justify each component (load balancer, cache, replica, shard) by naming the failure it addresses and the new trade-off it introduces.
5. Answer common system design interview questions at the correct "altitude."

---

## Unit 1 — Orientation: What System Design Is

**Topics**
- System design defined: choosing the right components and placing them correctly to solve a software problem
- Role progression: junior (build a feature) → mid (solve a problem within a system) → senior (design the system)
- The starting point: one server, one codebase, everything on one box — and why that's the *correct* starting point

**Key idea:** Most apps should begin simple. Complexity is earned by failure, not assumed up front.

---

## Unit 2 — The Three Founding Failures

The single-server app gets featured; 10,000 users arrive. Each failure names a fix that becomes a course unit later.

| Failure | Name | Fix (previewed) |
|---|---|---|
| CPU/RAM exhaustion | Overload | Second server + **load balancer** |
| Repeated identical queries | Database overload | **Cache** |
| The machine dies | **Single point of failure (SPOF)** | **Replication**, object storage (S3), backups |

**Key idea:** None of the fixes rewrote the code. System design is deciding where pieces live — and every fix introduces a new problem (the load balancer can die; the cache can go stale; the replica can lag).

---

## Unit 3 — Altitude: HLD vs. LLD

**Topics**
- High-level design: components, data flow, trade-offs ("Design Instagram")
- Low-level design: classes, functions, data structures ("Design the like button," "Design an in-memory cache")

**Interview checkpoint #1:** State your altitude before answering. Mismatched altitude is a top cause of failed interviews — interviewers rarely correct you; they let you spend 20 minutes at the wrong height.

---

## Unit 4 — Requirements: Functional vs. Non-Functional

**Topics**
- Functional requirements: testable features (sign up, upload, follow, feed, like/comment)
- Non-functional requirements: qualities — speed, durability, scale, availability, cost
- Why two apps with identical feature lists (family photo app vs. Instagram) are completely different systems
- NFRs conflict with each other: faster costs more; higher availability means idle machines

**Key idea:** Users never ask for a cache. They ask for a fast app. Every component in the design exists to satisfy a non-functional requirement.

---

## Unit 5 — The Five Questions Before You Design Anything

1. How many users, and how fast are they growing?
2. Read-heavy or write-heavy?
3. What can you never lose vs. afford to lose?
4. How much latency can each path tolerate?
5. What does it cost?

**Applied answers for the photo app:** design for millions; heavily read-dominant; photos must never be lost (like counts can drift briefly); feed must feel instant (~200 ms) while uploads may take seconds; keep the bill sane.

**Interview checkpoint #2:** The first five minutes are not design — they're requirements-gathering. Every later component is justified by pointing back at an answer ("I'm adding a cache because we said reads dominate").

---

## Unit 6 — Monolith vs. Microservices

**Topics**
- Monolith: one codebase, one deployment, function calls, one log — the correct choice at small scale
- Microservices: separate programs, separate deployments, network calls between them
- The only two valid reasons to split: **independent scaling** (feed needs 10 servers; uploads need 2) and **team size** (deployment contention)
- Costs of splitting: network failures, distributed debugging
- Reality: most companies run a monolith plus a few satellites

**Anti-pattern case:** the five-person startup running 30 microservices.

---

## Unit 7 — Scaling: Vertical vs. Horizontal

**Topics**
- Vertical: bigger box; zero code changes; but a hard ceiling, non-linear pricing, and still a SPOF
- Horizontal: many small machines; no upper limit, no SPOF — but raises two new problems (traffic distribution; shared data)
- Rule of thumb: scale up first because it's simple; scale out when you hit the ceiling or can't tolerate the SPOF

**Interview checkpoint #3:** "Why not just buy a bigger server?" — answer with the trade-off sequence and give scale-specific examples (50-user internal tool vs. consumer app heading to a million users).

---

## Unit 8 — Anatomy of a Request

**Topics**
- Servers and IP addresses; DNS as the internet's phone book
- HTTP request/response; HTTPS and why the "S" matters (coffee-shop Wi-Fi threat model)
- **Latency** (round-trip time) vs. **bandwidth** (pipe width)
- Why a 30-thumbnail feed is slow: round trips, not payload size — foreshadowing cache and CDN

---

## Unit 9 — Load Balancers

**Topics**
- DNS points at the load balancer, not at app servers
- The load balancer is just software on a server; the general category is **reverse proxy**
- Health checks: detecting and routing around dead servers
- Distribution algorithms: round-robin, least connections, weighted distribution
- Off-the-shelf options: NGINX, HAProxy, AWS ELB
- The recursive problem: the load balancer is itself a SPOF → run multiple

**Lab 1:** Two containers behind NGINX; kill one mid-traffic and observe failover.

---

## Unit 10 — Stateless vs. Stateful Servers

**Topics**
- The random-logout bug: sessions in local server memory + a load balancer
- Stateful defined: the server keeps information inside itself (memory or local disk)
- The fix: move session state to a shared store; servers become disposable
- Sticky sessions as the tempting wrong answer (uneven load; sessions still die with the server)
- The diagnostic question: *if this server vanished right now, would any user lose something?*
- Clarification: storing photos in a database or S3 does not make the app stateful

**Interview checkpoint #4:** "You scaled from two servers to five and users are getting logged out." Give cause, fix, and preemptively name and reject sticky sessions.

---

## Unit 11 — Data Modeling from Access Patterns

**Topics**
- Access patterns first: write the app down as the questions users will ask thousands of times a day
- The photo app's seven patterns (profile, user's photos, home feed, upload, like, comment, follow)
- The five entities: users, photos, likes, comments, follows — connections as ID pairs plus a little metadata
- Image files live outside the record; the record stores a pointer
- The home feed as the hard path: touches follows + photos + sorting
- Ordering discipline: **questions first, data shape second, technology last**

---

## Unit 12 — SQL vs. NoSQL

**Topics**
- SQL: fixed-shape tables, joins for relational questions, transactions and ACID (the delete-photo-with-likes-and-comments example)
- NoSQL: flexible shapes, horizontal spread, high-volume lookups (user behavior, preferences)
- The decision for the photo app: relational, join-heavy core → PostgreSQL; unstructured preferences/behavior → MongoDB
- Real systems use both; routing is just a conditional in application code
- Default guidance: when unsure, start with SQL

**Interview checkpoint #5:** Derive the choice from access patterns; never say "NoSQL because it scales." Know what ACID guarantees.

---

## Unit 13 — Indexing

**Topics**
- Full-table scans and why queries slow as rows grow
- The book-index analogy; indexing `posted_by` and `upload_time`
- The write cost: every insert must update every index — so don't index everything
- Method: start with zero indexes, find slow queries, index those columns (typically 3–5 per table)

**Lab 2:** 5M-row table; run a slow query, add one index, re-run and compare.

---

## Unit 14 — Caching

**Topics**
- The celebrity-post problem: millions of identical reads
- Redis in front of the database; cache hit vs. cache miss; ~1 ms vs. 20–30 ms
- What to cache: small, read constantly, changes rarely (trending photos, profile cards)
- Redis's dual role: hot-data cache + shared session store (closing the loop from Unit 10)
- The consistency problem: two copies of the same data
- **TTL** (lazy expiry, staggered to avoid simultaneous death) vs. **active invalidation** (immediate, but more work)
- **Cache stampede** and defenses: single-rebuilder, early refresh, TTL jitter
- Eviction: **LRU**
- Industry defaults: feed ~30 s TTL; profile cards minutes; trending ~60 s; anything security-shaped gets active invalidation only
- The worst bug is not an empty cache — it's a cache confidently serving wrong data

**Interview checkpoint #6:** Eviction policy, stampede handling, and cache/DB consistency. Raising the stampede unprompted is a strong hire signal.

**Lab 3:** Redis in front of the database; measure the speedup, then mutate the database and watch the app serve stale data.

---

## Unit 15 — Replication

**Topics**
- The database as SPOF; industry standard of one primary + two replicas
- Reads distributed across all three (with a load balancer); **writes go only to the primary** (the conflicting-writes thought experiment)
- Streaming replication and **replication lag**
- **Eventual consistency** vs. **strong consistency**; the read-your-own-writes bug and its fix (route a user's reads of their own fresh data to the primary)
- **Failover**: promoting a replica
- The dangerous misconception: replicas faithfully copy your mistakes — a bad DELETE propagates in milliseconds. Replication ≠ backup; snapshots stored away from the system are non-negotiable.

**Lab 4:** Primary + replica; observe lag, perform failover, and watch a delete replicate.

---

## Unit 16 — Sharding

**Topics**
- When replication can't help: every replica holds the full dataset; the data no longer fits one machine
- Shards as horizontal slices; the **shard key** (user ID for the photo app)
- Naive modulo routing and its two failure modes:
  - **Hot shards** (all celebrities land together) → pick a key that spreads load
  - Re-sharding catastrophe (adding a fifth shard moves nearly everything) → **consistent hashing** (each shard owns a range; adding a shard moves only one neighbor's slice)
- Discipline: shard as late as possible — it's the hardest decision to undo; prefer databases with built-in sharding

---

## Capstone Review — The Full Architecture

Trace one request through the completed design:

User → DNS → **load balancer** → one of 10 **stateless app servers** → **Redis** (sessions + hot-data cache, kept in sync via TTL and invalidation) → **PostgreSQL** (indexed; 1 primary for writes, 2 replicas for reads behind a read load balancer) and **MongoDB** (preferences/behavior) → with **sharding** held in reserve for when data outgrows one machine.

**Final assessment prompt:** For each component in the diagram, state (a) the failure that justified it, (b) the requirement it serves, and (c) the new problem it introduced.

---

## Vocabulary Checklist

Load balancer · reverse proxy · health check · round-robin · least connections · single point of failure · vertical/horizontal scaling · stateless/stateful · sticky sessions · DNS · latency · bandwidth · access pattern · data model · ACID · transaction · index · cache hit/miss · TTL · cache invalidation · cache stampede · LRU · replication · replication lag · eventual/strong consistency · failover · backup · shard · shard key · hot shard · consistent hashing · HLD/LLD · functional/non-functional requirements

## Interview Bytes (cross-cutting)

1. Declare your altitude (HLD vs. LLD) before answering.
2. Spend the first five minutes on requirements; justify every component with an earlier answer.
3. Vertical-first, then horizontal — with the trade-offs and scale-specific examples.
4. Diagnose the logout-on-scale-out bug; reject sticky sessions with reasons.
5. Derive SQL vs. NoSQL from access patterns, not slogans.
6. Volunteer the cache stampede before being asked.
