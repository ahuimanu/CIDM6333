# Glossary source audit — 2026-10-22

64 non-course entries of `tools/sitekit/glossary_data.py` checked against primary sources by a review agent. All ten FIX items below were applied the same day; minor notes applied where marked.

## Applied fixes
| Entry | Was | Now | Source |
|---|---|---|---|
| OpenCode | "SST, 2025" | Launched June 2025 by Anomaly (former SST team); MIT; repo anomalyco/opencode | opencode.ai/docs; github.com/anomalyco/opencode |
| A2A | "v1.0 added signed cards" | v0.3 (mid-2025) added signed Agent Cards and gRPC; v1.0 March 2026; joined AAIF Aug 2026 | a2a-protocol.org spec v1.0.0 §8.4; aaif.io/blog/a2a-joins-aaif |
| Linux Foundation | A2A donated to AAIF June 2025 | AAIF formed Dec 9 2025 (MCP, goose, AGENTS.md); A2A to LF June 2025, joined AAIF Aug 17 2026 | blog.modelcontextprotocol.io 2025-12-09; aaif.io |
| OWASP | "insecure output handling" (2023 name) | 2025 list: LLM05 Improper Output Handling; src genai.owasp.org | promptfoo OWASP LLM Top 10 page |
| Degani & Wiener | "(1997)" paper | Chapter in *Aviation Psychology in Practice* (Avebury 1994; Routledge 1997); NASA CR-177642 (1994) is the open copy; the 1997 IEEE paper is a different work | ntrs.nasa.gov/citations/19940029437 |
| Berkeley benchmark exploits | blog only, 5 authors, 8 benchmarks | arXiv:2605.12673 (May 2026; +Hanchen Li; 10 benchmarks, 219 flaws); blog April 2026 | arxiv.org/abs/2605.12673 |
| Claude Code src | docs.claude.com (redirects) | code.claude.com/docs | hooks ref confirms SessionStart, PreToolUse, PostToolUse, PreCompact |
| Codex src | developers.openai.com/codex (redirects) | openai.com/codex/ | Codex CLI Apr 16 2025; cloud May 16 2025 |
| Cognition src | cognition.ai (redirects) | cognition.com/blog/dont-build-multi-agents | Yan June 12 2025; Anthropic post June 13 2025 |
| FIPA src | http | https://www.fipa.org; formed 1996; IEEE CS standards committee 2005 | fipa.org/about/fipa_and_ieee.html |

## Minor notes applied
BabyAGI: March 2023 (not April). ADR: Nygard's sections are title/context/decision/status/consequences; course adds intent and alternatives; src cognitect.com 2011-11-15. Judge biases: added arXiv ids 2305.17926 (Wang 2023) and 2410.21819 (Wataoka 2024). ToolBench: the paper is ToolLLM (2307.16789). Pydantic AI src → pydantic.dev/docs/ai/overview/.

## Unverified
Pydantic AI release year ("2024 onward") — no primary page states it.

## Verified OK (facts and sources)
Claude Code dates (preview Feb 24 2025, GA May 22 2025); Codex dates; Cursor; GitHub Copilot (preview Jun 29 2021; agent mode Feb 2025; coding agent May 2025); Gemini CLI (Jun 25 2025); AGENTS.md; Agent Skills (Oct 16 2025); OpenCode plugin hook tool.execute.before; function calling Jun 13 2023; MCP Nov 25 2024, Streamable HTTP 2025-03-26, OAuth 2.1, AAIF Dec 9 2025; JSON-RPC 2.0 (2010-03-26); PKCE RFC 7636 (Sep 2015); Smith 1980 (IEEE Trans. Computers C-29(12):1104–1113); Rao & Georgeff ICMAS-95 pp. 312–319; ReAct 2210.03629 ICLR 2023; CoT 2201.11903; ToT 2305.10601; Toolformer 2302.04761; Reflexion 2303.11366; Generative Agents 2304.03442 (25 agents); MemGPT 2310.08560; RAG 2005.11401; AutoGPT Mar 30 2023; CAMEL 2303.17760; MetaGPT 2308.00352; AutoGen 2308.08155; CrewAI (João Moura, PyPI Dec 4 2023); LangChain Oct 2022, LangGraph Jan 2024; Ollama /api/embed; Langfuse MIT; OpenAI Practical Guide 2025; Invariant Labs Apr 1 2025; SWE-bench (12 repos), SWE-agent NeurIPS 2024, Agentless 2024; HumanEval 164; GAIA 2311.12983; WebArena; MT-Bench 2306.05685; Panickssery 2404.13076; BLEU P02-1040; MAST 2503.13657 (14 modes, 3 categories, >1,600 traces); Transformer 1706.03762; the five workflow patterns; Anthropic post dates (Dec 19 2024; Jun 13 2025; Sep 29 2025; Nov 26 2025; Oct 16 2025); AP2 Sep 2025.
