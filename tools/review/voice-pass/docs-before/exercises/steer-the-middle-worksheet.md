# Worksheet — Steer the middle

Student: · Date: 2026-10-22 · `opencode --version`: · Model id: · Codec: mine / reference

## One line per step

| Step | Record | Value |
|---|---|---|
| E1 | tool calls before the answer · first tool | · |
| E2 | steps in the plan · round-trip rule named? | · yes/no |
| E3 | self-test command the model ran, verbatim · prompt appeared? | · yes/no |
| E3 (optional) | custom tool loaded? · the model called it? | yes/no/skipped · yes/no |
| E4 | MCP server name, or none | |
| E5 | `wc -c AGENTS.md` · skill prompt appeared? · spec lines marked met | · yes/no · /10 |
| E6 | `read` call ran? · source the model named | no/yes · |
| E7 | record id, or no retriever | |
| E8 | verdict · findings (count, each with a location?) · `git status` · "fix it" outcome | · · · refused/denied/edited |
| Close | evicted id · commit hash | · |

## The inventory · one row per outer-ring item

A: file path in your repository. B: what reads it. C: when it is read. D: the trace you saw tonight. E: was it in your repository before tonight?

| Item | A · file | B · read by | C · when | D · trace tonight | E · before tonight? |
|---|---|---|---|---|---|
| Rules | `AGENTS.md` | | | | yes/no |
| Permissions | `opencode.json` → `permission` | | | | yes/no |
| Tool | `.opencode/tools/codec.ts` → `codec.py` | | | | yes/no/skipped |
| MCP server | `opencode.json` → `mcp` | | | | yes/no/none |
| Skill | `.opencode/skills/codec-check/SKILL.md` | | | | yes/no |
| Instructions | `opencode.json` → `instructions` | | | | yes/no |
| Memory | `evolution-07/lab/memory.jsonl` | | | | yes/no |
| Agent | `.opencode/agents/reviewer.md` | | | | yes/no |

## Finding

One row you could not fill, or one trace that did not match the claim, in two sentences: what you expected, what came back.
