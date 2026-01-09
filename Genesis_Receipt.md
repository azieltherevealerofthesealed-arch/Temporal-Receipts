# Genesis Receipt

This document records the **genesis receipt** for the Temporal Receipts project.

The genesis receipt anchors the lineage of Temporal Receipts to a **real, pre-existing, publicly verifiable historical artifact**, rather than to a declaration, institution, or maintainer.

No endorsement, interpretation, or authority is implied.

---

## Genesis Artifact

**Artifact Type:** Historical newspaper clipping  
**Title:** “The Truth No Defense”  
**Publication:** New York Evening World  
**Date:** August 3, 1926  

The artifact documents a judicial position asserting that *truth is not a defense* in certain contempt proceedings. The clipping is preserved as a scanned image.

The artifact exists independently of this project and predates all contributors by decades.

---

## Why This Artifact Was Chosen

This artifact satisfies all criteria for a legitimate genesis receipt:

- It is **externally verifiable**
- It is **immutable**
- It is **non-symbolic by design**
- It asserts **no truth claim on behalf of this project**
- It documents a historical moment where **authority and truth diverged**, without requiring agreement

Temporal Receipts does not judge the artifact.
It records its existence in time.

---

## What This Does *Not* Mean

Using this artifact as the genesis receipt does **not** mean:

- The project endorses the article
- The project asserts the article is correct
- The project claims moral or legal authority
- The project takes a political or judicial position

The artifact is used solely as a **temporal anchor**.

---

## Canonical Genesis Receipt (JSON)

```json
{
  "receipt_id": "TR-1926-08-03-000001",
  "timestamp_utc": "1926-08-03T00:00:00Z",
  "event_type": "historical_artifact",
  "event_summary": "Newspaper clipping titled 'The Truth No Defense' documenting a court position that truth is not a defense in contempt proceedings",
  "location": "United States",
  "sources": [
    {
      "type": "artifact",
      "reference": "Scanned newspaper clipping dated August 3, 1926 (image file: truth_is_no_defense.png)",
      "confidence": 1.0
    }
  ],
  "confidence_score": 1.0,
  "hash_prev": null,
  "notes": "Genesis receipt anchored to a historical artifact. No endorsement, interpretation, or claim beyond existence and date."
}

## Artifact Integrity

Artifact file: `truth_is_no_defense.png`  
SHA-256:

2149adc3933e34978696af94287743056908bd0acb6d47e04f645c798de69a04
