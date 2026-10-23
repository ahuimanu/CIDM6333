#!/usr/bin/env python3
"""codec.py: encode and decode text with simple schemes. See codec-spec.md.

Interactive:  python3 codec.py
CLI:          python3 codec.py <scheme> <encode|decode> "<text>"
Self-test:    python3 codec.py --selftest
"""
import base64
import codecs
import sys


# --- schemes -------------------------------------------------------------

def rot13_encode(s: str) -> str:
    return codecs.encode(s, "rot_13")


def rot13_decode(s: str) -> str:
    return codecs.decode(s, "rot_13")


def base64_encode(s: str) -> str:
    return base64.b64encode(s.encode("utf-8")).decode("ascii")


def base64_decode(s: str) -> str:
    return base64.b64decode(s.encode("ascii")).decode("utf-8")


# registry: scheme name -> (encode, decode)
SCHEMES = {
    "rot13": (rot13_encode, rot13_decode),
    "base64": (base64_encode, base64_decode),
}

# --- self-test -----------------------------------------------------------

SELFTEST_INPUTS = ["", "a", "Hello, World!", "The quick brown fox", "café — üñ"]


def selftest() -> int:
    """Round-trip every scheme on the fixed inputs. Return 0 only if all pass."""
    failures = 0
    for name, (enc, dec) in SCHEMES.items():
        ok = all(dec(enc(s)) == s for s in SELFTEST_INPUTS)
        if name == "rot13":
            ok = ok and all(enc(enc(s)) == s for s in SELFTEST_INPUTS)
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        failures += 0 if ok else 1
    return 0 if failures == 0 else 1


# --- modes ---------------------------------------------------------------

def run(scheme: str, direction: str, text: str) -> str:
    if scheme not in SCHEMES:
        print(f"error: unknown scheme '{scheme}'; choose from {', '.join(SCHEMES)}", file=sys.stderr)
        sys.exit(2)
    if direction not in ("encode", "decode"):
        print(f"error: direction must be encode or decode, not '{direction}'", file=sys.stderr)
        sys.exit(2)
    enc, dec = SCHEMES[scheme]
    return enc(text) if direction == "encode" else dec(text)


def interactive() -> None:
    print("codec · schemes: " + ", ".join(SCHEMES) + " · q to quit")
    while True:
        scheme = input("scheme> ").strip()
        if scheme == "q":
            return
        direction = input("encode or decode> ").strip()
        if direction == "q":
            return
        text = input("text> ")
        if scheme not in SCHEMES or direction not in ("encode", "decode"):
            print("unknown scheme or direction; try again")
            continue
        try:
            print(run(scheme, direction, text))
        except Exception as e:  # a bad decode input, for example
            print(f"could not {direction}: {e}")


def main(argv: list[str]) -> int:
    if len(argv) == 1:
        interactive()
        return 0
    if argv[1] == "--selftest":
        return selftest()
    if len(argv) != 4:
        print(__doc__, file=sys.stderr)
        return 2
    print(run(argv[1], argv[2], argv[3]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
