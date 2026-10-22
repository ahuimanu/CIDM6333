# Adversarial review brief for the CIDM 6333 course site

You are reviewing a static course website (GitHub Pages, repo root `docs/`) for a graduate course, *Agentic Systems Design and Development*. Build scripts are in `tools/sitekit/`. Treat everything here as a draft that must survive a hostile reader: a student who did not attend, an external examiner, and a security reviewer.

## What to attack

1. **Factual claims.** Every date, number, author, and vendor behavior in `tools/sitekit/glossary_data.py`, the figure captions (`docs/figures/*.html`, the `STEPS` arrays), and the lecture notes (`tools/sitekit/notes.json`). Verify against primary sources; report every error with the correct fact and a URL.
2. **Cryptic content.** Slides and notes that presuppose unstated context. For each, quote the phrase, name the page, and write the one sentence that would fix it.
3. **Internal contradictions.** Terms defined differently in two places (glossary vs. notes vs. textbook outline); status values, field names, or file paths that differ between decks and exercises (e.g. `bash` vs `shell` in OpenCode permission blocks; `evolution-07/lab/recall.py` paths; flight-card field names).
4. **Runnable instructions.** Every command in `docs/exercises/*.html` and the textbook appendices: would it run as typed on macOS and Windows/WSL? Flag anything that depends on an unstated install, a path that may not exist, or a tool version.
5. **Build scripts.** `tools/sitekit/*.py`: idempotence (run twice, same output), injection safety (HTML escaping of notes and glossary text), regexes that could match the wrong block, and anything that would break when a new lecture or figure is added.
6. **Site mechanics.** Broken links (internal and external), the htmx nav fragment on every page, dark mode, keyboard operation of the figure players, mobile layout.
7. **Schedule leaks.** The site must carry no dates, times, rooms, or due dates (those live in Canvas). Find any that remain.

## Ground rules

- Do not praise. Report defects, ranked by impact, each with location, evidence, and the fix.
- Do not edit `docs/` by hand; propose changes to `tools/sitekit/` sources or to the Dropbox originals (decks, markdown) so the build stays reproducible.
- If a claim cannot be verified, say so; do not supply a plausible replacement.

## Output

A single Markdown report, `tools/review/codex-review-<date>.md`, with sections matching the seven attack areas, then a ranked top-20 list.
