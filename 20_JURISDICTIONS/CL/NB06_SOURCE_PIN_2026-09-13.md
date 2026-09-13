# AI-LAWS — NB06 Chile Neurotechnology Source Pin

**UNIT_ID:** `NB-BATCH-NB06-20260913-001`  
**DATE:** 2026-09-13  
**STATE:** SOURCE_PIN_COMPLETE_FOR_CL-001 / CL-002_FULLTEXT_BLOCKED  
**CANONICAL_LEGAL_CONCLUSION:** FALSE  
**LEGAL_ADVICE:** NO

## Scope

This record pins the Chile primary-law and court-source identities needed by NB06 Human Sovereignty / Neurotechnology. It does not generalize Chile-specific rules into universal rights and it does not admit a court precedent without an official or otherwise accepted full text.

```text
NO_PRECEDENT_FOUND != NO_RIGHT
OFFICIAL_DOCKET_IDENTITY != FULL_TEXT_VERIFIED
ANALOGICAL_PRECEDENT != DIRECT_AI_PRECEDENT
CHILE_RULE != UNIVERSAL_GLOBAL_RULE
```

## CL-001 — Ley 21.383

**Official source:** Biblioteca del Congreso Nacional de Chile — Ley Chile  
**Exact record:** `https://www.bcn.cl/leychile/navegar?idNorma=1166983`  
**Document:** Ley N° 21.383  
**Promulgated:** 2021-10-14  
**Published:** 2021-10-25  
**Authority class:** CONSTITUTIONAL_TEXT / CONSTITUTIONAL_AMENDMENT  
**Acquisition:** URL_DIRECT_PREFERRED

The official Ley Chile record states that the reform modifies Article 19 No. 1 of the Constitution and adds language requiring scientific and technological development to serve persons and respect life and physical and psychological integrity, with the law to regulate requirements, conditions and restrictions for use on persons while especially safeguarding brain activity and information derived from it.

The current official Constitution record's amendment history continues to identify Ley 21.383. This is enough to pin the source identity for NB06, but current constitutional text must be rechecked before any material jurisdiction-wide conclusion.

## CL-002 — Girardi / Emotiv Inc

**Court:** Corte Suprema de Chile  
**Rol:** 105.065-2023 / 105065-2023  
**Decision date:** 2023-08-09  
**Case:** Girardi / Emotiv Inc  
**Official jurisprudence deep link:** `https://juris.pjud.cl/busqueda/u?c5762`  
**Authority class:** BINDING_COURT_DECISION within the Chilean legal system  
**Acquisition:** MANUAL_DOWNLOAD_REQUIRED

Official Poder Judicial materials independently confirm the docket identity, parties and decision date. Poder Judicial's human-rights jurisprudence material also quotes and attributes the relevant holdings to Corte Suprema Rol N° 105.065-2023.

The official jurisprudence deep link is currently protected by anti-bot/CAPTCHA in this execution environment. Therefore:

```text
OFFICIAL_DOCKET_IDENTITY_VERIFIED = YES
OFFICIAL_FULL_TEXT_ACQUIRED = NO
FULL_TEXT_HASHED = NO
CASE_LAW_ADMISSION = BLOCKED
LEGAL_CONCLUSION_FROM_CASE = NOT_ATTEMPTED
```

Secondary full-text copies located at academic/legal portals are supporting evidence only and must not silently replace the official judiciary source.

## UNESCO certified source correction used by NB06

The final standalone source for the UNESCO Recommendation on the Ethics of Neurotechnology is now pinned to the certified-copy record:

`https://unesdoc.unesco.org/ark:/48223/pf0000397812_eng`

UNESCO states that the Recommendation was adopted on 11 November 2025; the certified copy was published on 31 March 2026. This supersedes use of the 43rd-session resolutions volume as the preferred NB06 source identity.

Repository binary vendoring rights for this certified copy were not independently pinned in this unit, so NB06 uses URL_DIRECT_PREFERRED rather than asserting a vendored PDF.

## EU source reuse

NB06 reuses the already controlled official source IDs rather than duplicating binaries:

- `EU-004` — Charter of Fundamental Rights of the European Union — official EUR-Lex ELI; status rechecked as in force.
- `EU-005` — GDPR — official EUR-Lex ELI; official page rechecked as in force/current-source record.
- `INT-003` — UNESCO Recommendation on the Ethics of Artificial Intelligence — existing verified source record.

## Acquisition result

```text
SOURCE_IDS_TOUCHED = INT-004, INT-003, EU-004, EU-005, CL-001, CL-002
URL_DIRECT_READY = INT-004, INT-003, EU-004, EU-005, CL-001
OFFICIAL_DOCKET_PINNED_FULLTEXT_BLOCKED = CL-002
REPOSITORY_PDF_BINARIES_CREATED = 0
SHA256_RECORDED = 0
NOTEBOOK_UPLOADS = 0
UNKNOWN_PRESERVED = YES
AUTO_ADVANCE = NO
```
