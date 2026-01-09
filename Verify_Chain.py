#!/usr/bin/env python3
import json, hashlib, sys, glob, os

def canonical_json(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def load_receipts(paths):
    receipts = []
    for p in paths:
        with open(p, "r", encoding="utf-8") as f:
            receipts.append((p, json.load(f)))
    receipts.sort(key=lambda x: (x[1].get("timestamp_utc",""), x[1].get("receipt_id","")))
    return receipts

def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/verify_chain.py <receipt1.json> <receipt2.json> ...", file=sys.stderr)
        print("Tip: python tools/verify_chain.py examples/*.json", file=sys.stderr)
        sys.exit(2)

    expanded = []
    for arg in sys.argv[1:]:
        expanded.extend(glob.glob(arg) if any(ch in arg for ch in "*?[]") else [arg])
    paths = [p for p in expanded if os.path.isfile(p)]
    if not paths:
        print("No receipt files found.", file=sys.stderr)
        sys.exit(2)

    receipts = load_receipts(paths)

    ok = True
    prev_hash = None
    for i, (path, r) in enumerate(receipts):
        base = {k: v for k, v in r.items() if k != "hash_current"}
        computed = sha256_hex(canonical_json(base))

        if computed != r.get("hash_current"):
            print(f"[FAIL] {path}: hash_current mismatch")
            ok = False

        if i == 0:
            prev_hash = r.get("hash_current")
            continue

        if r.get("hash_prev") != prev_hash:
            print(f"[FAIL] {path}: hash_prev mismatch")
            print(f"       expected: {prev_hash}")
            print(f"       claimed : {r.get('hash_prev')}")
            ok = False

        prev_hash = r.get("hash_current")

    if ok:
        print("[OK] Chain verified for provided receipts.")
        sys.exit(0)
    sys.exit(1)

if __name__ == "__main__":
    main()
