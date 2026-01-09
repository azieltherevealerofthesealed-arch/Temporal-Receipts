# Decision Log

This file records major design decisions.

## Decisions
- Append-only chosen over mutable records
- Forks allowed by default
- Confidence explicit, not inferred
- No ranking or trending
- No identity enforcement

Rejected alternatives are documented to prevent revisionism.

update 0.1 pre launch
## Genesis Artifact Hashing

Decision: Include a cryptographic hash of the genesis artifact.

Rationale:
- Prevent silent replacement
- Enable independent verification
- Preserve neutrality (hash asserts integrity, not meaning)

Rejected:
- Storing artifact without hash (insufficient transparency)
