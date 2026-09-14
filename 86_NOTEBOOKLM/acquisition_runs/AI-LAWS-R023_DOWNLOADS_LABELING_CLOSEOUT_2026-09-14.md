# AI-LAWS — R023 Downloaded PDF Labeling Closeout

**UNIT_ID:** `AI-LAWS-R023`  
**DATE:** 2026-09-14  
**BASE_HEAD:** `4a38eaefe7de4e1d6ed2da166549daac8f2454cd`  
**USER_BINARY_COMMIT:** `4a38eaefe7de4e1d6ed2da166549daac8f2454cd` (`pdf document downloads`)  
**SCOPE:** downloaded binary inventory / source-label mapping / Notebook ingest safety  
**AUTO_ADVANCE:** NO

## Repository binary inventory

The user-upload commit added 38 PDF files under:

`86_NOTEBOOKLM/downloads/`

R023 mapped those filenames to existing AI-LAWS source identities and Notebook packs without treating filename similarity as legal/source verification.

## Durable outputs

- `86_NOTEBOOKLM/downloads/README.md`
- `86_NOTEBOOKLM/downloads/DOWNLOADS_REGISTRY.csv`
- `86_NOTEBOOKLM/downloads/NOTEBOOK_UPLOAD_PLAN.md`
- `86_NOTEBOOKLM/PDF_CONTENT_IDENTITY_AND_DERIVED_TEXT_PROTOCOL.md`
- updated `86_NOTEBOOKLM/NOTEBOOKLM_DOWNLOAD_AND_UPLOAD_LIST.md`
- updated `00_CONTROL/NEW_CHAT_BOOTSTRAP.md`
- updated `90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv`

## Core result

```text
REPOSITORY_PDF_BINARIES_PRESENT = 38
BINARY_FILENAME_TO_SOURCE_ID_MAPPING_CREATED = YES
INSTITUTION_LABELS_CREATED = YES
AUTHORITY_CLASS_LABELS_CREATED = YES
NOTEBOOK_PACK_ROUTING_CREATED = YES
RECOMMENDED_NOTEBOOK_LABELS_CREATED = YES
RECOMMENDED_CANONICAL_LOCAL_FILENAMES_CREATED = YES
BULK_PDF_TO_MARKDOWN_CONVERSION_RECOMMENDED = NO
BULK_NOTEBOOK_UPLOAD_RECOMMENDED = NO
CONTENT_IDENTITY_VERIFIED_COUNT = 0
CURRENTNESS_VERIFIED_BY_R023_COUNT = 0
NOTEBOOK_UPLOADS_BY_R023 = 0
NOTEBOOK_LOCATOR_TESTS_BY_R023 = 0
LEGAL_CONCLUSIONS_CREATED = 0
```

## Important classifications

### UNESCO Neurotechnology legacy binary

The repository PDF:

`Recommendation on the Ethics of Neurotechnology (2025)  43rd General Conference resolutions source.pdf`

maps to `INT-004` as a **legacy source variant**. It is not the preferred current primary source. The acquisition manifest/NB06 closeout identifies UNESCO certified copy `pf0000397812_eng` as the preferred source.

```text
LEGACY_43GC_PDF != CURRENT_PRIMARY_CERTIFIED_COPY
```

### CETS treaty-status PDF

The treaty-status PDF is a dynamic-page snapshot and cannot establish current signatures/ratifications/reservations/declarations. The live Council of Europe treaty-status page remains the currentness source.

### Türkiye PDFs

`TR-001` through `TR-008` are now physically present in the repository, but remain content/currentness-unverified under R023. Before Notebook use, exact law number/title/current consolidated state must be compared with the official source-pin records.

`TR-008` requires special confirmation that Law No. 7590 amendments effective 2026-07-31 are reflected.

### Incident PDFs

```text
INC-001 = COMPANY_INCIDENT_DISCLOSURE
INC-002 = INDEPENDENT_INVESTIGATION
INC-003 = VENDOR_THREAT_INTELLIGENCE
INC-004 = POLICY_FORECAST_CONTEXT
```

These categories must remain distinct inside NB08.

## Conversion decision

Direct PDF/official-URL ingestion is the default.

Derived Markdown is permitted only when:

- native PDF text extraction is materially inadequate;
- OCR is needed;
- layout causes retrieval problems;
- controlled diffing/page-locator support is needed.

Derived Markdown must be `NONCANONICAL_DERIVATIVE` and preserve provenance/page markers.

## What R023 did not prove

R023 did not prove that:

- every PDF came from the official host;
- every PDF is the current version;
- every PDF is complete;
- every PDF may be redistributed/re-uploaded under all licence terms;
- Notebook can ingest every PDF correctly;
- any legal proposition is correct.

Those checks remain source-by-source and pack-by-pack.

## Next work distinction

Two separate lanes remain:

```text
NEXT_SUBSTANTIVE_LEGAL_RESEARCH = AI-LAWS-R003 (EU AI Act current/phased map)
NEXT_NOTEBOOK_ACQUISITION_PACK = NB07 (Liability / Evidence / Financial Responsibility), subject to explicit authorization and reuse of already pinned sources
```

Before NB07 or any other pack is loaded, the selected existing PDFs must pass content-identity checks under the new protocol.

`AUTO_ADVANCE = NO`
