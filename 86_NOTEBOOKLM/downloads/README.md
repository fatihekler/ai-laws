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

### INT-001 — CETS No.225 treaty status page

The PDF is a time snapshot. Current signatures, ratifications, reservations and declarations must come from the live Council of Europe treaty-status page.

### INT-004 — UNESCO Neurotechnology

The repository file named `Recommendation on the Ethics of Neurotechnology (2025)  43rd General Conference resolutions source.pdf` is a legacy source variant. The current preferred primary Notebook source is UNESCO's certified-copy record `pf0000397812_eng` identified in the acquisition manifest and NB06 closeout. Do not load the legacy PDF as the primary/current source.

### EU-001 — AI Act

A consolidated PDF is only a snapshot. Before a current-law conclusion, verify the current consolidated version and amendment state in EUR-Lex.

### EU directives

A Directive is not proof of identical domestic implementation in every Member State. National transposition must be checked when the legal conclusion is country-specific.

### TR-001 through TR-008

The files were manually added after the prior acquisition closeouts. Treat them as `REPOSITORY_BINARY_PRESENT / CONTENT_IDENTITY_UNVERIFIED` until title, law number, current consolidated state and official-source identity are checked. `TR-008` requires special confirmation that Law No. 7590 amendments effective 2026-07-31 are reflected.

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
