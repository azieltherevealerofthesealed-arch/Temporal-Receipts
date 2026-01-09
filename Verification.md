# Verification

Verification is deterministic and offline-capable.

To verify a chain:
1. Canonicalize receipt JSON (sorted keys)
2. Recompute SHA-256 hash
3. Confirm `hash_current`
4. Confirm `hash_prev` matches prior receipt

No server is required.
No authority is required.
Anyone can verify independently.
