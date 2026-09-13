# AI-LAWS — NB06 Human Sovereignty / Neurotechnology Acquisition Closeout

**UNIT_ID:** `NB-BATCH-NB06-20260913-001`  
**BASE_HEAD:** `b4ece9f817d1b4a3c3498f3b46f948e54dc1cc27`  
**NOTEBOOK_PACK:** `NB06`  
**STATE:** `URL_ACQUISITION_READY / CL-002_FULLTEXT_BLOCKED`  
**AUTO_ADVANCE:** `NO`

## Work performed

- Fresh-read `main` HEAD/TREE before mutation and found no unexplained overlapping drift.
- Rechecked the NB06 pack assignment: `INT-004`, `INT-003`, `EU-004`, `EU-005`, `CL-001`, `CL-002`.
- Resolved the final standalone UNESCO Recommendation on the Ethics of Neurotechnology to UNESCO's certified-copy record `pf0000397812_eng`, published 31 March 2026 after adoption on 11 November 2025.
- Changed `INT-004` from unresolved source-family state to `VERIFIED_OFFICIAL_CERTIFIED_COPY` and `URL_DIRECT_PREFERRED`; repository binary reuse rights remain unpinned.
- Rechecked official EUR-Lex source identity/status for the EU Charter and GDPR and recorded them as URL-direct reuse sources for NB06 rather than creating duplicate binaries.
- Pinned Chile Ley 21.383 to exact official BCN Ley Chile record `idNorma=1166983` and recorded it as URL-direct ready.
- Pinned `Girardi / Emotiv Inc`, Corte Suprema Rol 105.065-2023, to the official Poder Judicial jurisprudence deep link.
- Verified the case identity, parties and date using official Poder Judicial materials, but the official full-text deep link remains blocked by anti-bot/CAPTCHA in this execution environment.
- Preserved secondary copies of the Girardi/Emotiv judgment as supporting-only; no case-law admission or legal conclusion was created.
- Attempted direct acquisition of the UNESCO certified-copy PDF; external binary transfer again failed, so no PDF bytes, SHA-256 or byte-size values are claimed.
- Updated the central source acquisition manifest and central acquisition/validation ledger.
- Added `20_JURISDICTIONS/CL/NB06_SOURCE_PIN_2026-09-13.md`.

## Source state

```text
SOURCE_IDS_TOUCHED = INT-004, INT-003, EU-004, EU-005, CL-001, CL-002
URL_DIRECT_READY = INT-004, INT-003, EU-004, EU-005, CL-001
OFFICIAL_DOCKET_PINNED_FULLTEXT_BLOCKED = CL-002
REPOSITORY_PDF_BINARIES_CREATED = 0
HASHES_RECORDED = 0
NOTEBOOK_UPLOADS = 0
CASE_LAW_ADMISSION = NO
LEGAL_CONCLUSION = NOT_ATTEMPTED
UNKNOWN_PRESERVED = YES
```

## Key authority safeguards

```text
UNESCO_RECOMMENDATION != BINDING_LAW
CHILE_RULE != UNIVERSAL_GLOBAL_RULE
OFFICIAL_DOCKET_IDENTITY != FULL_TEXT_VERIFIED
SECONDARY_FULLTEXT != OFFICIAL_COURT_FULLTEXT
NOTEBOOK_UPLOAD != SOURCE_VERIFICATION
```

## Durable outputs

- updated `86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv`
- updated `86_NOTEBOOKLM/NOTEBOOKLM_ACQUISITION_AND_VALIDATION_LEDGER.csv`
- `20_JURISDICTIONS/CL/NB06_SOURCE_PIN_2026-09-13.md`
- `86_NOTEBOOKLM/acquisition_runs/NB-BATCH-NB06-20260913-001_CLOSEOUT.md`

## Blocker

`CL-002` cannot advance to full-text verified/case-law admitted state until the official judiciary full text, or another source accepted under the project case-law gate, is acquired and checked.

No later source pack or substantive R011 legal analysis is auto-started.

`AUTO_ADVANCE = NO`
