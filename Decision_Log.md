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

update 0.2 pre launch
"sources": [
  {
    "type": "artifact",
    "reference": "truth_is_no_defense.png",
    "confidence": 1.0,
    "hash_sha256": "2149adc3933e34978696af94287743056908bd0acb6d47e04f645c798de69a04"
  }
]
update 0.3 updated index.html + debugging.
