# Temporal Receipts
## A Neutral, Open-Source Framework for Time-Stamped Event Recording
**Version:** v1.0 (Public Release)  
**License:** MIT

---

## Abstract
Temporal Receipts are an open-source, append-only system for recording **that** something occurred at a specific time, with evidence and a confidence score—without interpretation, narrative, or authority. They preserve **sequence without meaning**, enabling global auditability, fork tolerance, and long-term resistance to historical manipulation.

---

## Problem Statement
Modern records fail in three primary ways:
1. **Narrative overwrite** (history rewritten in-place)
2. **Authority capture** (truth depends on who controls the database)
3. **Interpretation contamination** (facts inseparable from opinion)

Temporal Receipts address this by separating **time + evidence** from **meaning** entirely.

---

## Design Principles
1. **Append-Only** – nothing is deleted or overwritten  
2. **Fork-Permissive** – no “official” timeline  
3. **Evidence-Weighted** – confidence derives from corroboration  
4. **Interpretation-Free** – meaning lives outside the receipt  
5. **Open by Default** – anyone can issue, verify, or fork  

---

## Definitions

### Temporal Receipt
A structured record asserting:
- an event was observed,
- at a specific time,
- with listed sources,
- with an explicit confidence score,
- linked to a prior receipt via cryptographic hashing.

It **does not** assert truth, intent, morality, or implication.

### Lineage
A chain of receipts where each receipt includes `hash_prev` and `hash_current`, making tampering detectable.

---

## Core Schema (v1)
See `schema/temporal_receipt.schema.json`.

Key fields:
- `receipt_id` (string)
- `timestamp_utc` (ISO-8601 UTC)
- `event_type` (enum/string)
- `event_summary` (short text)
- `sources[]` (structured references + per-source confidence)
- `confidence_score` (0..1)
- `hash_prev` (hex string, optional for genesis)
- `hash_current` (hex string)

---

## Confidence Model
Confidence is **explicit**, not implied:
- Increases through corroboration (additional receipts referencing the same event)
- Can decrease through disputes or lack of support (optional decay layer)
- Conflicts create **dispute receipts**, never edits

---

## Forking & Disputes
Forks are not failures; they are governance.
- Divergence is visible
- Lineage remains intact
- Reconciliation requires evidence, not authority

Disputes are new receipts that reference the target receipt.

---

## Security Model
- Hash-chained receipts
- Verification is public and deterministic
- Tampering requires breaking cryptographic continuity

---

## What This System Is Not
- Prediction engine
- Intelligence analysis
- Symbolic/prophetic framework
- Moral or legal judgment
- Consensus engine

Those layers may exist **above** receipts, never inside.

---

## Use Cases
- Journalism & fact auditing
- Legal timelines & custody
- Scientific replication
- AI output accountability
- Conflict escalation tracking
- Historical preservation

---

## License
MIT. Free to use, fork, and build.

