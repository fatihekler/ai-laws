# NB-BATCH-NB03-20260913-001 — Closeout

## Scope

Bounded source-acquisition unit for NB03 — United States AI Law.

This unit was limited to manifest entries marked `PDF_DOWNLOAD_ALLOWED` in NB03 at the start of the unit:

- US-002 — America's AI Action Plan
- US-003 — OMB M-25-21
- US-004 — OMB M-25-22
- US-006 — OMB M-26-04
- US-009 — Utah Artificial Intelligence Policy Act, conditional on currentness recheck

No substantive legal conclusion, Notebook upload, or next bounded unit was authorized.

## Fresh repository baseline

- BASE_HEAD: `8afc291b6ef1ae1d4aec3557eea899fb4b9db860`
- BASE_TREE: `6bc49718a4e75e39dcac8013a184bc56c262cef9`
- unexplained overlapping drift: NO

## Verification results

### US-002

- Official White House release dated 2025-07-23 verified.
- Official PDF URL remains the source identified by the White House.
- Later official White House publications continue to cite that same PDF.
- Rights basis: U.S. Government work framework under 17 U.S.C. § 105 for federal works; embedded third-party elements were not separately assessed.
- Binary acquisition attempt from the official host failed in the current execution environment.
- No local file, repository binary, byte size, or SHA-256 is claimed.

### US-003 — OMB M-25-21

- Current OMB memorandum index still lists M-25-21 dated 2025-04-03.
- Official PDF first-page identity and date verified.
- Rights basis: U.S. Government work framework under 17 U.S.C. § 105 for federal works; embedded third-party elements were not separately assessed.
- Binary acquisition attempt from the official host failed in the current execution environment.
- No local file, repository binary, byte size, or SHA-256 is claimed.

### US-004 — OMB M-25-22

- Current OMB memorandum index still lists M-25-22 dated 2025-04-03.
- Official PDF first-page identity and date verified.
- Rights basis: U.S. Government work framework under 17 U.S.C. § 105 for federal works; embedded third-party elements were not separately assessed.
- Binary acquisition attempt from the official host failed in the current execution environment.
- No local file, repository binary, byte size, or SHA-256 is claimed.

### US-006 — OMB M-26-04

- Current OMB memorandum index still lists M-26-04 dated 2025-12-11.
- Official PDF first-page identity and date verified.
- Rights basis: U.S. Government work framework under 17 U.S.C. § 105 for federal works; embedded third-party elements were not separately assessed.
- Binary acquisition attempt from the official host failed in the current execution environment.
- No local file, repository binary, byte size, or SHA-256 is claimed.

### US-009 — Utah Artificial Intelligence Policy Act

- The manifest's 2024 whole-chapter PDF is not safe to use as a current-law snapshot.
- Official Utah Legislature material verifies that current Section 13-72-101 is effective 2026-05-06 and was amended by Chapter 127, 2026 General Session.
- The 2024 version is marked superseded by the official Utah source.
- A current exact whole-chapter acquisition target was not pinned in this bounded unit.
- Therefore US-009 was not downloaded or vendored.

## Binary-transfer result

The current execution environment could verify official web/PDF identity but could not transfer the external White House PDF bytes into the GitHub binary-write path. The repository must therefore preserve:

`WEB_IDENTITY_VERIFIED != LOCAL_FILE_ACQUIRED`

`PDF_URL_ACCESSIBLE_TO_RESEARCH_TOOL != PDF_BYTES_TRANSFERRED_TO_GITHUB`

`NO_SHA256 != HASH_UNKNOWN_FOR_EXISTING_LOCAL_FILE`; here no local file exists.

No placeholder, reconstructed PDF, screenshot-derived substitute, fabricated byte size, or fabricated hash was created.

## Required closeout fields

```text
UNIT_ID = NB-BATCH-NB03-20260913-001
BASE_HEAD = 8afc291b6ef1ae1d4aec3557eea899fb4b9db860
FINAL_HEAD = TO_BE_FRESH_VERIFIED_AFTER_THIS_COMMIT
JURISDICTION = US / US-UT
SOURCE_IDS_TOUCHED = US-002, US-003, US-004, US-006, US-009
NEW_SOURCES = 0 repository binary source files
UPDATED_SOURCES = 5 acquisition-ledger records
DOWNLOADS_COMPLETED = 0
HASHES_RECORDED = 0
NOTEBOOK_PACK = NB03
NOTEBOOK_UPLOADS = 0
NOTEBOOK_SOURCE_CHECKS = NOT_RUN
CLAIMS_EXTRACTED = 0
CLAIMS_RECHECKED = 0
CONFLICTS = 0
UNKNOWNS = external-binary-transfer capability; exact current whole-chapter US-009 acquisition target; any embedded third-party rights inside federal PDFs
HUMAN_REVIEW_REQUIRED = NO for source identity; YES before assuming rights in embedded third-party material or vendoring a current Utah whole-chapter snapshot
NEXT_BOUNDED_UNIT = UNSET — requires explicit authorization
AUTO_ADVANCE = NO
```

## Invariants

```text
LEGAL_ADVICE = NO
MODEL_OUTPUT_CANONICAL = NO
NOTEBOOK_OUTPUT_CANONICAL = NO
UNKNOWN_PRESERVED = YES
AUTO_ADVANCE = NO
```
