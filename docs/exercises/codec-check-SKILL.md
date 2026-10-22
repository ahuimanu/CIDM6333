---
name: codec-check
description: Check the course codec against its spec and report line by line. Use when asked to check, verify, or review the codec against codec-spec.md.
---
# Codec check

1. Run `python3 evolution-08/exercise/codec.py --selftest` and keep the output.
2. Read `evolution-08/exercise/codec-spec.md`. It has ten numbered lines.
3. For each of the ten lines, report `met` or `not met`. Give the evidence for each line: a self-test output line, a function name in `codec.py`, or a command you ran. Do not report a line as met without evidence.
4. End with one sentence: how many of the ten lines are met. Do not change any file.
