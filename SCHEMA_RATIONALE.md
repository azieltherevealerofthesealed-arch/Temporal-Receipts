# Schema Rationale

Each field in the Temporal Receipt schema exists to support auditability and prevent narrative control.

## Included Fields
- `timestamp_utc`: fixes sequence in universal time
- `event_summary`: minimal human context (strict length limit)
- `sources[]`: explicit evidence references
- `confidence_score`: declared uncertainty
- `hash_prev` / `hash_current`: tamper detection

## Explicitly Excluded Fields
- importance
- impact
- truth
- sentiment
- correctness
- authority
- outcome
- interpretation

Exclusion is a security feature.
