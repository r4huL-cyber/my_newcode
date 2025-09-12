
from __future__ import annotations
import argparse
import textwrap
o = "hellogys"

def to_hex_continuous(s: str) -> str:
    return s.encode("utf-8").hex()

def to_hex_spaced(s: str) -> str:
    raw = to_hex_continuous(s)
    # split into bytes
    return " ".join(raw[i:i+2] for i in range(0, len(raw), 2))

def to_hex_0x(s: str) -> str:
    return " ".join("0x" + raw[i:i+2] for i in range(0, len(raw := s.encode("utf-8").hex()), 2))

def from_hex(hex_str: str) -> str:
    # Accepts continuous hex or spaced hex
    cleaned = "".join(hex_str.split()).replace("0x", "")
    return bytes.fromhex(cleaned).decode("utf-8", errors="replace")

def main():
    p = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Print a fake flag in various hex formats.",
        epilog=textwrap.dedent("""\
            Examples:
              python print_hex_flag.py
              python print_hex_flag.py --format spaced
              python print_hex_flag.py --format 0x
              python print_hex_flag.py --decode
        """)
    )
    p.add_argument("--format", choices=["continuous", "spaced", "0x"], default="continuous",
                   help="Which hex format to print (default: continuous).")
    p.add_argument("--decode", action="store_true",
                   help="Also decode and print the ASCII flag (for testing).")
    args = p.parse_args()

    if args.format == "continuous":
        out = to_hex_continuous(FLAG)
    elif args.format == "spaced":
        out = to_hex_spaced(FLAG)
    else:  # "0x"
        out = to_hex_0x(FLAG)

    print(out)

    if args.decode:
        # decode from the continuous hex form to be deterministic
        decoded = from_hex(to_hex_continuous(FLAG))
        print("\n# decoded:")
        print(decoded)

if __name__ == "__main__":
    main()
