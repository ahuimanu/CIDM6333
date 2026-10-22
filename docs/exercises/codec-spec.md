# Codec spec · v1 · 2026-10-22

1. `codec.py` is one file. It uses only the Python standard library.
2. It offers `encode` and `decode` for every supported scheme.
3. Supported schemes: `rot13`, `base64`. (The E8 exercise adds `hex`.)
4. Round trip: for every scheme and every input string `s`, `decode(encode(s)) == s`.
5. `rot13` is its own inverse: `encode(encode(s)) == s`.
6. Interactive mode: run with no arguments. A menu asks for scheme, direction, and text, prints the result, and repeats until `q`.
7. CLI mode: `python3 codec.py <scheme> <encode|decode> "<text>"` prints the result and exits 0.
8. `python3 codec.py --selftest` runs the round-trip check for every scheme on a fixed set of inputs, prints `PASS` or `FAIL` per scheme, and exits 0 only if every scheme passes.
9. An unknown scheme or direction prints an error to stderr and exits 2.
10. A new scheme requires four things: an encode function, a decode function, a registry entry, and selftest coverage. A change that lacks any of the four is incomplete.
