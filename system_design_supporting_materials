# System Design Fundamentals: Supporting Materials & Study Questions

Companion to *System Design Fundamentals: A Beginner's Syllabus*. For each concept: a one-line orientation, external reading (Wikipedia-first, with a canonical non-wiki source where it genuinely adds something), and questions. Questions are tiered: **Check** (comprehension), **Apply** (transfer to the photo app or a new scenario), **Stretch** (discussion-grade, suitable for seminar or interview prep).

**Two book-length references that back the whole course:**
- Kleppmann, *Designing Data-Intensive Applications* — the standard deep treatment of replication, partitioning, consistency, and transactions.
- [The System Design Primer](https://github.com/donnemartin/system-design-primer) (GitHub) — free, exhaustive, interview-oriented.

---

## Unit 1 — Orientation

**Systems design** — the discipline of defining architecture, components, and data flow to satisfy requirements.
→ [Systems design](https://en.wikipedia.org/wiki/Systems_design)

**Server** — a computer whose job is answering requests; nothing more exotic than that.
→ [Server (computing)](https://en.wikipedia.org/wiki/Server_(computing)) · [Data center](https://en.wikipedia.org/wiki/Data_center)

**Questions**
- *Check:* Why does the course insist that a single-server deployment is the correct starting point rather than a naive one?
- *Apply:* Name one product you use that almost certainly still runs on a handful of servers. What signals tell you?
- *Stretch:* The junior→senior progression is framed as feature → problem → system. Where does responsibility for *cost* enter that progression, and why is it usually last?

---

## Unit 2 — The Three Founding Failures

**Single point of failure** — any component whose death takes the whole system with it.
→ [Single point of failure](https://en.wikipedia.org/wiki/Single_point_of_failure)

**Scalability** — a system's ability to handle growth by adding resources.
→ [Scalability](https://en.wikipedia.org/wiki/Scalability)

**Object storage** — storage architecture for large immutable blobs (photos), with built-in redundancy.
→ [Object storage](https://en.wikipedia.org/wiki/Object_storage) · [Amazon S3](https://en.wikipedia.org/wiki/Amazon_S3)

**Questions**
- *Check:* List the three failures and the component each one justifies.
- *Apply:* Your app stores uploaded photos on the app server's local disk. Which of the three failures does this worsen, and what is the first migration you'd make?
- *Stretch:* "Every fix brings a new problem" is presented as the engine of the course. Is this regress infinite? What actually terminates it in practice?

---

## Unit 3 — HLD vs. LLD

**High-level vs. low-level design** — boxes-and-arrows vs. classes-and-functions.
→ [High-level design](https://en.wikipedia.org/wiki/High-level_design) · [Low-level design](https://en.wikipedia.org/wiki/Low-level_design) · [Software architecture](https://en.wikipedia.org/wiki/Software_architecture)

**Questions**
- *Check:* "Design a rate limiter" — HLD, LLD, or does it depend? On what?
- *Apply:* Rewrite "Design Instagram" as three distinct LLD questions.
- *Stretch:* Why do interviewers let candidates spend twenty minutes at the wrong altitude rather than correcting them? What is that silence measuring?

---

## Unit 4 — Functional vs. Non-Functional Requirements

**Functional requirement** — what the system must do; testable behavior.
→ [Functional requirement](https://en.wikipedia.org/wiki/Functional_requirement)

**Non-functional requirement** — how well it must do it; the qualities (latency, durability, availability, cost).
→ [Non-functional requirement](https://en.wikipedia.org/wiki/Non-functional_requirement) · [Availability](https://en.wikipedia.org/wiki/Availability) · [Durability (database systems)](https://en.wikipedia.org/wiki/Durability_(database_systems))

**Questions**
- *Check:* The family photo app and Instagram share a feature list. Name four NFRs on which they differ by orders of magnitude.
- *Apply:* Write one functional and one non-functional requirement for the *upload* path specifically. Which one drives more architecture?
- *Stretch:* NFRs "fight with each other." Pick two that conflict and describe the mechanism of the conflict, not just its existence.

---

## Unit 5 — The Five Questions

**Latency** — time per round trip.
→ [Latency (engineering)](https://en.wikipedia.org/wiki/Latency_(engineering))

**Capacity planning** — sizing for the users you're heading toward, not the ones you have.
→ [Capacity planning](https://en.wikipedia.org/wiki/Capacity_planning)

**Questions**
- *Check:* Why does read-heavy vs. write-heavy get asked *before* any database is chosen?
- *Apply:* Answer the five questions for a ride-hailing app. Which answers flip relative to the photo app?
- *Stretch:* Question 3 (what can you never lose?) implicitly prices data classes differently. Sketch how you'd translate "never lose photos, tolerate like-count drift" into two different storage budgets.

---

## Unit 6 — Monolith vs. Microservices

**Monolithic application** — one codebase, one deployment.
→ [Monolithic application](https://en.wikipedia.org/wiki/Monolithic_application)

**Microservices** — many small independently deployed services communicating over a network.
→ [Microservices](https://en.wikipedia.org/wiki/Microservices) · [Conway's law](https://en.wikipedia.org/wiki/Conway%27s_law) (the team-size argument, formalized) · Fowler, ["MonolithFirst"](https://martinfowler.com/bliki/MonolithFirst.html)

**Questions**
- *Check:* State the only two reasons given for splitting a monolith. Why is "microservices are modern" not on the list?
- *Apply:* The photo app's feed needs 10 servers; uploads need 2. Which service do you extract first, and what new failure modes do you sign up for the moment you do?
- *Stretch:* The five-person startup with 30 microservices spent more time on the network between services than on the product. Diagnose this with Conway's law — what organizational structure was that architecture pretending to have?

---

## Unit 7 — Vertical vs. Horizontal Scaling

**Scaling up vs. scaling out** — bigger box vs. more boxes.
→ [Scalability § Horizontal and vertical scaling](https://en.wikipedia.org/wiki/Scalability#Horizontal_(scale_out)_and_vertical_scaling_(scale_up))

**Questions**
- *Check:* Vertical scaling has three limits named in the lecture. What are they?
- *Apply:* A 50-user internal tool is slow. Defend vertical scaling in two sentences, including what you're buying with the simplicity.
- *Stretch:* Horizontal scaling "has no upper limit" is a first-approximation claim. What eventually does limit it? (Consider coordination, data locality, and Amdahl's law.)
→ [Amdahl's law](https://en.wikipedia.org/wiki/Amdahl%27s_law)

---

## Unit 8 — Anatomy of a Request

**DNS** — the internet's phone book: name → IP address.
→ [Domain Name System](https://en.wikipedia.org/wiki/Domain_Name_System) · [IP address](https://en.wikipedia.org/wiki/IP_address)

**HTTP / HTTPS / TLS** — the shared request/response language, and the lock on it.
→ [HTTP](https://en.wikipedia.org/wiki/HTTP) · [HTTPS](https://en.wikipedia.org/wiki/HTTPS) · [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security)

**Latency vs. bandwidth** — round-trip time vs. pipe width; the feed is slow because of trips, not payload.
→ [Round-trip delay](https://en.wikipedia.org/wiki/Round-trip_delay) · [Bandwidth (computing)](https://en.wikipedia.org/wiki/Bandwidth_(computing))

**Questions**
- *Check:* Walk the full path from typing `photoapp.com` to pixels on screen, naming every lookup and hop.
- *Apply:* The feed fetches 30 thumbnails. Propose two changes that reduce round trips *without* touching bandwidth.
- *Stretch:* Why is "add more bandwidth" so often the wrong fix for a slow app? Construct a scenario where latency dominates completely.

---

## Unit 9 — Load Balancers

**Load balancing** — distributing requests across servers; algorithms include round-robin, least connections, weighted.
→ [Load balancing (computing)](https://en.wikipedia.org/wiki/Load_balancing_(computing))

**Reverse proxy** — the general category: any server that fronts other servers.
→ [Reverse proxy](https://en.wikipedia.org/wiki/Reverse_proxy)

**Implementations** — NGINX, HAProxy, cloud LBs.
→ [Nginx](https://en.wikipedia.org/wiki/Nginx) · [HAProxy](https://en.wikipedia.org/wiki/HAProxy)

**Questions**
- *Check:* Distinguish "reverse proxy" from "load balancer." Which is the genus, which the species?
- *Apply:* Two of your ten servers are twice the size of the rest. Which algorithm do you configure, and what do you set?
- *Check:* How does the load balancer discover a dead server, and what does the user experience during the seconds before it does?
- *Stretch:* The load balancer is itself a SPOF, fixed by running several. What now decides which load balancer a request hits? (Follow the recursion one level and see where it grounds out — DNS, anycast, VRRP.)
→ [Virtual Router Redundancy Protocol](https://en.wikipedia.org/wiki/Virtual_Router_Redundancy_Protocol) · [Anycast](https://en.wikipedia.org/wiki/Anycast)

---

## Unit 10 — Stateless vs. Stateful

**State** — information a server retains between requests.
→ [State (computer science)](https://en.wikipedia.org/wiki/State_(computer_science)) · [Stateless protocol](https://en.wikipedia.org/wiki/Stateless_protocol)

**Session** — the login note; the one thing that genuinely needs memory between requests.
→ [Session (computer science)](https://en.wikipedia.org/wiki/Session_(computer_science))

**Shared-nothing architecture** — the design ideal the disposable-server rule points toward.
→ [Shared-nothing architecture](https://en.wikipedia.org/wiki/Shared-nothing_architecture)

**Questions**
- *Check:* State the diagnostic question from the lecture that decides whether a server is stateful.
- *Check:* Why does storing photos in S3 *not* make the app stateful?
- *Apply:* A teammate proposes sticky sessions to fix the logout bug. Write the two-sentence rejection, including both costs.
- *Stretch:* Sessions could also live in a signed token on the client (e.g., JWT) instead of a shared store. What does that trade — and what does "log out this user everywhere, now" cost under each design?
→ [JSON Web Token](https://en.wikipedia.org/wiki/JSON_Web_Token)

---

## Unit 11 — Data Modeling from Access Patterns

**Data modeling** — deciding what to store and how pieces connect, before any technology choice.
→ [Data modeling](https://en.wikipedia.org/wiki/Data_modeling) · [Entity–relationship model](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model)

**Questions**
- *Check:* Recite the ordering rule: what comes first, second, last — and what goes wrong when it's inverted?
- *Apply:* Add "save a photo to a private collection" to the app. Write the access pattern as a user question, then the record shape as IDs-plus-metadata.
- *Stretch:* "Show me my home feed" touches follows, photos, and a sort. This one pattern will later justify caching, replicas, and possibly precomputed feeds (fan-out on write). Trace how a single access pattern can dominate an entire architecture.

---

## Unit 12 — SQL vs. NoSQL

**Relational / SQL** — fixed-shape tables, joins, transactions.
→ [Relational database](https://en.wikipedia.org/wiki/Relational_database) · [SQL](https://en.wikipedia.org/wiki/SQL) · [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL)

**ACID and transactions** — all-or-nothing units of work.
→ [ACID](https://en.wikipedia.org/wiki/ACID) · [Database transaction](https://en.wikipedia.org/wiki/Database_transaction)

**NoSQL** — flexible shapes, built to spread wide.
→ [NoSQL](https://en.wikipedia.org/wiki/NoSQL) · [MongoDB](https://en.wikipedia.org/wiki/MongoDB) · [Document-oriented database](https://en.wikipedia.org/wiki/Document-oriented_database)

**Using both** — polyglot persistence.
→ Fowler, [PolyglotPersistence](https://martinfowler.com/bliki/PolyglotPersistence.html)

**Questions**
- *Check:* The photo-deletion example groups three deletes into one transaction. Which letter of ACID is doing the work there, and what state does it prevent?
- *Apply:* Derive the SQL choice for the photo app in two sentences that mention only access patterns — no product names until the last word.
- *Stretch:* "NoSQL because it scales" is banned. Steelman it anyway: under exactly what data shape and access pattern does that slogan become a correct argument?

---

## Unit 13 — Indexing

**Database index** — the book-index structure that trades write work for read speed.
→ [Database index](https://en.wikipedia.org/wiki/Database_index) · [B-tree](https://en.wikipedia.org/wiki/B-tree) (what most indexes actually are)

**Questions**
- *Check:* Why not index every column? Name the specific cost incurred on every write.
- *Apply:* The lecture indexes `posted_by` and `upload_time`. Which single access pattern from Unit 11 might want a *composite* index on both, and in which order?
- *Stretch:* "Do not guess which column to index — find slow queries first" is an empirical discipline. What tooling does that presuppose, and what does the equivalent discipline look like for caching decisions in Unit 14?

---

## Unit 14 — Caching

**Cache** — small, fast store of popular answers in front of the database.
→ [Cache (computing)](https://en.wikipedia.org/wiki/Cache_(computing)) · [Redis](https://en.wikipedia.org/wiki/Redis)

**TTL** — expiry-based freshness; lazy and honest about it.
→ [Time to live](https://en.wikipedia.org/wiki/Time_to_live)

**Cache invalidation** — active deletion on write; correct and laborious.
→ [Cache invalidation](https://en.wikipedia.org/wiki/Cache_invalidation)

**Cache stampede** — a hot entry expires and a thousand identical misses hit the database at once.
→ [Cache stampede](https://en.wikipedia.org/wiki/Cache_stampede) · [Thundering herd problem](https://en.wikipedia.org/wiki/Thundering_herd_problem)

**Eviction** — what to delete when full; LRU as the default answer.
→ [Cache replacement policies](https://en.wikipedia.org/wiki/Cache_replacement_policies)

**Questions**
- *Check:* State the three properties that make data cache-worthy, and give one example from the app that fails each property.
- *Check:* Why do privacy settings get active invalidation and *no* TTL, while the trending list gets a 60-second TTL and no invalidation?
- *Apply:* Design the stampede defense for Messi's new post: which of the three defenses (single rebuilder, early refresh, TTL jitter) would you combine, and why isn't jitter alone enough here?
- *Stretch:* "The worst bugs are when the cache is confidently wrong." Connect this to the two-copies problem in Unit 15 — replication lag and stale cache are the same disease. What is the general name for it, and can any system with two copies fully escape it?

---

## Unit 15 — Replication

**Replication** — keeping full copies of the database on multiple machines; reads spread out, writes to one primary.
→ [Replication (computing)](https://en.wikipedia.org/wiki/Replication_(computing))

**Replication lag & consistency** — replicas trail the primary by design.
→ [Eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency) · [Consistency model](https://en.wikipedia.org/wiki/Consistency_model) · [CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem) (the formal ceiling on wanting everything at once)

**Failover** — promoting a replica when the primary dies.
→ [Failover](https://en.wikipedia.org/wiki/Failover)

**Backup ≠ replication** — replicas copy your mistakes at wire speed; only snapshots stored apart survive a bad DELETE.
→ [Backup](https://en.wikipedia.org/wiki/Backup)

**Questions**
- *Check:* Why must writes go to exactly one place? Reconstruct the X=9 vs. X=13 conflict from memory.
- *Check:* Alan uploads a photo and refreshes; it's missing. Was data lost? What routing rule fixes his experience without routing *everyone's* reads to the primary?
- *Apply:* Classify each of these as needing strong or eventual consistency, with one clause of justification: follower count, password change, like count, blocked-user list.
- *Stretch:* The read-your-own-writes fix pushes load back onto the primary — the exact load replicas exist to remove. At what fraction of "own-data reads" does the replica architecture stop paying for itself? What would you measure to find out?

---

## Unit 16 — Sharding

**Sharding / partitioning** — splitting data across machines when it no longer fits on one.
→ [Shard (database architecture)](https://en.wikipedia.org/wiki/Shard_(database_architecture)) · [Partition (database)](https://en.wikipedia.org/wiki/Partition_(database))

**Consistent hashing** — routing that survives adding a shard without moving nearly everything.
→ [Consistent hashing](https://en.wikipedia.org/wiki/Consistent_hashing)

**Questions**
- *Check:* Recompute Alan's shard (user ID 10) under 4 shards and under 5 with naive modulo. How many of your users move, roughly, and why is the answer "almost all"?
- *Check:* Why can't replication solve the doesn't-fit-on-one-machine problem, given that it solved the read-load and SPOF problems?
- *Apply:* User ID as shard key put all celebrities' *data* in predictable places but not their *load*. Propose a shard key or scheme that spreads celebrity read load, and name what it costs the "show me all of Alan's photos" query.
- *Stretch:* "Shard as late as possible" and "design for the millions you're heading toward" (Unit 5) are in tension. Resolve it: what should you do *early* that makes late sharding survivable, without actually sharding early?

---

## Capstone Questions

1. For every box in the final diagram, complete the sentence three ways: *This exists because ___ failed; it serves the requirement that ___; it introduced the new problem of ___.*
2. Delete one component of your choice from the finished design. Narrate the first hour of the outage.
3. The course never rewrote application code. Identify the one unit where that claim quietly stops being true, and defend your pick. (Candidates: stateless refactor in Unit 10; read-routing logic in Unit 15; shard-key awareness in Unit 16.)
4. An interviewer asks: "Your photo app works. Traffic doubles every three months. What breaks first, second, and third?" Answer using only the vocabulary checklist.
