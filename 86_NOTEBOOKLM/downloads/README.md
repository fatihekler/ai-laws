# AI-LAWS — Downloaded PDF Labeling and Notebook Ingest Standard

**STATE:** CONTROLLED_LABELING_LAYER  
**SCOPE:** `86_NOTEBOOKLM/downloads/`  
**AUTO_ADVANCE:** NO

## Purpose

The files in this directory are repository binaries/snapshots. Their physical presence does **not** by itself prove:

- official source identity;
- currentness;
- legal authority class;
- permission to redistribute or re-upload;
- correct NotebookLM pack;
- successful text ingestion;
- substantive legal validity.

Always consult:

- `../NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv`
- `DOWNLOADS_REGISTRY.csv`
- the relevant jurisdiction/source-pin record
- the relevant acquisition closeout

before Notebook use.

## Core invariant

```text
REPOSITORY_BINARY_PRESENT
!=
SOURCE_IDENTITY_VERIFIED
!=
CURRENT_LAW_VERIFIED
!=
NOTEBOOK_READY
!=
LEGAL_CONCLUSION
```

## Notebook display-label format

Use this format whenever NotebookLM allows the source title to be controlled, or keep it in the notebook's source index if the UI preserves the original filename:

```text
SOURCE_ID | JURISDICTION | AUTHORITY_CLASS_SHORT | ISSUER | DOCUMENT_ID | SHORT_TITLE | STATE_TAG
```

Examples:

```text
EU-001 | EU | REGULATION | EUR-Lex | 2024/1689 | AI Act | CONSOLIDATED-SNAPSHOT
TR-002 | TR | STATUTE | TBMM/Mevzuat | 6698 | KVKK | CURRENTNESS-RECHECK
INC-001 | US-GLOBAL | COMPANY_INCIDENT_DISCLOSURE | OpenAI | 2026-08-26 | HF Incident | NON-COURT
INC-002 | US-GLOBAL | INDEPENDENT_INVESTIGATION | Redwood/METR | 2026-08-26 | HF Incident | SUPPORTING
INT-004-LEGACY | UNESCO | SOFT-LAW | UNESCO | 43GC | Neurotechnology | SUPERSEDED-SOURCE
```

## Institution labels

Use stable institution labels rather than informal names:

```text
COE = Council of Europe
UNESCO = United Nations Educational, Scientific and Cultural Organization
OECD = Organisation for Economic Co-operation and Development
UN = United Nations
UNGA = United Nations General Assembly
EU = European Union / EUR-Lex
US-WH = The White House
US-OMB = Office of Management and Budget
US-NIST = National Institute of Standards and Technology
TR = Türkiye
TR-TBMM = Türkiye Büyük Millet Meclisi
TR-MEVZUAT = Mevzuat Bilgi Sistemi
TR-RG = Resmî Gazete
OPENAI = OpenAI
ANTHROPIC = Anthropic
REDWOOD-METR = Redwood Research / METR
DARIO-AMODEI = policy essay source, not regulator/court
```

## Authority-class short labels

```text
CONSTITUTION
REGULATION
DIRECTIVE
STATUTE
TREATY
COURT_DECISION
REGULATORY_GUIDANCE
OFFICIAL_GUIDANCE
VOLUNTARY_FRAMEWORK
SOFT_LAW
COMPANY_INCIDENT_DISCLOSURE
INDEPENDENT_INVESTIGATION
VENDOR_TI
POLICY_ESSAY
ALLEGATION
UNKNOWN
```

Do not collapse these labels into a single `LAW` label.

## Existing PDF naming

Do **not** rename the existing binaries in GitHub merely to improve appearance. Renaming binary files creates unnecessary history churn and can break references.

Instead:

1. keep the current repository filename;
2. use `DOWNLOADS_REGISTRY.csv` as the canonical mapping layer;
3. if a local copy is prepared for Notebook upload, rename that local copy using the `recommended_canonical_filename` field;
4. preserve the repository path and Git blob identity in any derived-text record.

## Canonical local filename format

```text
SOURCE_ID__JURISDICTION__DOCUMENT_ID__VERSION_OR_STATE.ext
```

Examples:

```text
EU-001__EU__REG-2024-1689__CONSOLIDATED-2026-07-27.pdf
US-003__US__OMB__M-25-21.pdf
TR-002__TR__LAW-6698__KVKK__CURRENT-SNAPSHOT.pdf
INC-002__US-GLOBAL__REDWOOD-METR__HF-INCIDENT__2026-08-26.pdf
```

## State tags

Every source loaded into Notebook should expose one of these states in its source index/notes:

```text
CURRENT_VERIFIED
CURRENTNESS_RECHECK
DYNAMIC_STATUS_SNAPSHOT
TRANSPOSITION_DEPENDENT
NATIONAL_IMPLEMENTATION_REQUIRED
OFFICIAL_URL_PREFERRED
PDF_CONTENT_CHECK_REQUIRED
SUPPORTING_ONLY
VENDOR_ATTRIBUTION
INDEPENDENT_INVESTIGATION
SUPERSEDED_SOURCE
BLOCKED
UNKNOWN
```

## Important source-specific warnings

### INT-001 — CETS No.225 repository PDF

R027 verified that the repository PDF is the **12-page treaty text itself**, not a treaty-status-page print. The repository filename is therefore misleading and the registry mapping has been corrected. Current signatures, ratifications, reservations and declarations must still come from the live Council of Europe Treaty Office page.

### INT-004 — UNESCO Neurotechnology

The repository file named `Recommendation on the Ethics of Neurotechnology (2025)  43rd General Conference resolutions source.pdf` is a legacy source variant. The current preferred primary Notebook source is UNESCO's certified-copy record `pf0000397812_eng` identified in the acquisition manifest and NB06 closeout. Do not load the legacy PDF as the primary/current source. R032 rechecked the certified-copy URL from GitHub; the runner received HTTP 403 on 2026-09-14. This access result does not invalidate the prior official certified-copy pin, but fresh R032 content-body verification is not claimed while access is blocked.

### INT-005 — OECD AI Principles

R027 verified the repository PDF as the 12-page `Recommendation of the Council on Artificial Intelligence` with 2024 update signal. It is not a webpage-print snapshot. The current OECD page remains preferred for currentness.

### INT-007 — Pact / Global Digital Compact

R027 verified the repository file as a 64-page Summit of the Future outcome-document bundle containing the Pact for the Future and Global Digital Compact. The extracted text does not contain the exact `A/RES/79/1` identifier, so it is `CONTENT_IDENTITY_PARTIAL` for the manifest source and must not replace the exact adopted-resolution source. R032 resolved the exact adopted source through `https://docs.un.org/en/A/RES/79/1` to the official 56-page PDF `https://documents.un.org/doc/undoc/gen/n24/272/22/pdf/n2427222.pdf`; SHA-256 `0c3968d0ce8d55cf107309794adea6879d70f9aea60e6d6d64e3a8da4b028336`. Use that official source for primary resolution identity; keep the repository bundle supporting-only.

### EU-001 — AI Act

A consolidated PDF is only a snapshot. Before a current-law conclusion, verify the current consolidated version and amendment state in EUR-Lex.

### EU directives

A Directive is not proof of identical domestic implementation in every Member State. National transposition must be checked when the legal conclusion is country-specific.

### TR-001 through TR-008

R026 verified repository-snapshot content identity and native searchable text for all eight files. `TR-008` includes Law No. 7590 effects effective 2026-07-31. Live official Mevzuat exact-byte/currentness recheck remains required before material legal conclusions.

### Incident sources

```text
INC-001 = OpenAI company incident disclosure
INC-002 = independent Redwood/METR investigation
INC-003 = Anthropic vendor threat-intelligence report
INC-004 = Dario Amodei policy/forecast essay
```

Never merge these evidence classes.

## Upload rule

Do **not** upload the entire directory blindly.

Use `DOWNLOADS_REGISTRY.csv` and upload pack-by-pack only after:

1. file/source identity check;
2. currentness check where applicable;
3. rights/use check;
4. authority-label check;
5. pack assignment check.

`AUTO_ADVANCE = NO`
