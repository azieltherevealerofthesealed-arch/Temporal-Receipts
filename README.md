# Temporal Receipts

An open-source, append-only system for recording events in time **without interpretation**.

Temporal Receipts record:
- **when** something was observed,
- **what** was observed (brief summary),
- **what evidence** supports the observation,
- a **confidence score**,
- and a **cryptographic link** to prior receipts.

## What This Is
A neutral way to log that something occurred at a specific time, with evidence and lineage.

## What This Is Not
- Not a prediction engine
- Not an intelligence product
- Not a narrative or “importance” ranking system
- Not an authority on truth

## Repo Contents
- `whitepaper/` — public whitepaper (Markdown)
- `schema/` — JSON schema for receipts
- `examples/` — example receipts (normal, dispute, correction)
- `tools/` — hashing + chain verification scripts
- `ui/` — minimal static web UI (viewer + submit + verify)
- `cloudflare/` — optional Workers API for submit/list (can be read-only)

## License
MIT
