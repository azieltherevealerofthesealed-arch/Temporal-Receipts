#!/usr/bin/env python3
import json, hashlib, sys

def canonical_json(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def main():
    if len(sys.argv) != 2:
        print("Usage: python tools/hash_receipt.py <path_to_receipt.json>", file=sys.stderr)
        sys.exit(2)

    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        receipt = json.load(f)

    base = {k: v for k, v in receipt.items() if k != "hash_current"}
    h = sha256_hex(canonical_json(base))
    print(h)

if __name__ == "__main__":
    main()
