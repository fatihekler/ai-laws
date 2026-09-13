# AI-LAWS — NotebookLM Upload and Refresh Checklist

**DOCUMENT_ID:** AI-LAWS-R021-NB-CHECKLIST-1.0  
**STATE:** ACTIVE_CHECKLIST  
**DATE:** 2026-09-13

Use this checklist every time a source pack is created or materially refreshed.

## A. Before download/import

- [ ] Identify the target notebook/pack (`NB00`–`NB09`).
- [ ] Confirm the source exists in `NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv` or create a candidate record first.
- [ ] Confirm jurisdiction.
- [ ] Confirm document ID / CELEX / treaty / case / memorandum number.
- [ ] Confirm authority class.
- [ ] Confirm current binding state.
- [ ] Confirm publication/adoption date.
- [ ] Confirm entry-into-force/application date if relevant.
- [ ] Confirm current amendment/consolidation state.
- [ ] Confirm source is official/primary or label it otherwise.
- [ ] Confirm license/use right.
- [ ] Confirm the source does not contain restricted/private/privileged material.

## B. Download/import choice

Choose one:

- [ ] `URL_DIRECT_PREFERRED`
- [ ] `PDF_DOWNLOAD_ALLOWED`
- [ ] `MANUAL_DOWNLOAD_REQUIRED`
- [ ] `METADATA_ONLY`
- [ ] `DO_NOT_UPLOAD`

If URL import is used:

- [ ] verify Notebook can extract the material text;
- [ ] verify annexes/tables are not silently omitted;
- [ ] record retrieval date.

If PDF/local file is used:

- [ ] download from official source;
- [ ] calculate SHA-256;
- [ ] record byte size;
- [ ] verify file opens;
- [ ] verify title/document ID inside the file;
- [ ] verify expected version date;
- [ ] preserve page numbering if locators matter.

## C. Notebook capacity

Google's standard/free source limit is currently 50 sources per notebook; product limits can change.

- [ ] Recheck current product limit before a major build.
- [ ] Keep routine pack target at 35–40 sources.
- [ ] Leave headroom for amendments/cases/challenge sources.
- [ ] Split notebook instead of merging unrelated documents merely to save source slots.

## D. Source-class integrity

For each source:

- [ ] `PRIMARY_LAW`
- [ ] `TREATY`
- [ ] `COURT_DECISION`
- [ ] `REGULATORY_DECISION`
- [ ] `GUIDANCE`
- [ ] `SOFT_LAW`
- [ ] `TECHNICAL_FRAMEWORK`
- [ ] `SCHOLARSHIP`
- [ ] `COMPANY_STATEMENT`
- [ ] `INDEPENDENT_INVESTIGATION`
- [ ] `REPORTING`
- [ ] `MODEL_SUPPORTING_ONLY`

Never mix these without labels.

## E. Model-output firewall

- [ ] Grok answer is not in the primary-law source group.
- [ ] ChatGPT synthesis is not in the primary-law source group.
- [ ] Notebook's own prior report is not being re-uploaded as proof.
- [ ] YargıGPT summary is not treated as an official decision.
- [ ] If model output is loaded for critique it is prefixed `MODEL_SUPPORTING_ONLY__`.

## F. Currentness checks by source family

### EU law

- [ ] current consolidated/version date checked;
- [ ] amending instrument checked;
- [ ] phased application checked;
- [ ] Directive national-transposition dependency recorded.

### Treaties

- [ ] entry-into-force condition checked;
- [ ] party/signature/ratification state checked;
- [ ] reservations/declarations checked;
- [ ] domestic effect not assumed.

### U.S. federal

- [ ] EO/memo currentness checked;
- [ ] revoked/superseded instruments identified;
- [ ] federal vs state authority separated.

### Türkiye

- [ ] official Mevzuat/Resmî Gazete text pinned;
- [ ] amendment/consolidation currentness checked;
- [ ] case law only from verified full text;
- [ ] policy/strategy separated from statute.

### Case law

- [ ] official/accepted authoritative source verified;
- [ ] court identity verified;
- [ ] docket/decision/date verified;
- [ ] full text verified;
- [ ] relevance class assigned;
- [ ] analogy limit recorded if analogical.

## G. Research prompt integrity

Before asking Notebook:

- [ ] name the exact source subset;
- [ ] name jurisdiction/date cutoff;
- [ ] request source locators/citations;
- [ ] require `UNKNOWN` where source support is absent;
- [ ] ask for contrary/conflicting sources;
- [ ] forbid universalization across jurisdictions;
- [ ] forbid legal-advice conclusion.

## H. After Notebook output

- [ ] save output only as supporting research;
- [ ] extract claim IDs;
- [ ] verify material claims against original source;
- [ ] preserve conflicts;
- [ ] route to AI-LAWS work item;
- [ ] require human legal review where material;
- [ ] do not modify another repository's state automatically.

## I. Refresh triggers

Refresh the pack when any of these occurs:

- [ ] amendment/corrigendum;
- [ ] new consolidated text;
- [ ] new application date reached;
- [ ] treaty status change;
- [ ] new authoritative court/regulator interpretation;
- [ ] material source URL/version drift;
- [ ] new incident evidence changes factual account;
- [ ] Grok/ChatGPT identifies possible stale material;
- [ ] scheduled periodic review.

## J. Final pack record

Record:

```text
PACK_ID
PACK_VERSION
BUILD_DATE
SOURCE_COUNT
SOURCE_IDS
SOURCE_MANIFEST_COMMIT
NOTEBOOK_OWNER
CONFIDENTIALITY_CLASS
DATE_CUTOFF
KNOWN_GAPS
NEXT_REFRESH_TRIGGER
CANONICAL = FALSE
```
