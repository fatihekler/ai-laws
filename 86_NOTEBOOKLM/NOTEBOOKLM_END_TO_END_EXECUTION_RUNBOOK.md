# AI-LAWS — NOTEBOOKLM / GEMINI NOTEBOOK END-TO-END EXECUTION RUNBOOK

**DOCUMENT_ID:** AI-LAWS-NB-E2E-RUNBOOK-1.0  
**DATE:** 2026-09-13  
**STATE:** EXECUTION_RUNBOOK  
**AUTO_ADVANCE:** NO

This runbook operationalizes `00_CONTROL/AI_LAWS_MASTER_RESEARCH_NOTEBOOK_ORCHESTRATION.md`.

## Phase 0 — Continuity

- Fresh-read AI-LAWS `main` HEAD/TREE.
- Read current context and queue.
- Identify exactly one bounded jurisdiction/domain/source-pack unit.
- Re-read the master orchestration file and relevant Notebook pack files.
- Stop on unexplained overlapping drift.

## Phase 1 — Build the batch

Create a batch ID:

`NB-BATCH-<PACK>-<YYYYMMDD>-<NNN>`

Record:

- bounded scope;
- jurisdictions;
- source IDs;
- source-count budget;
- acquisition method;
- expected outputs;
- stop condition.

Do not mix unrelated jurisdictions merely to fill capacity.

## Phase 2 — Verify every source before acquisition

For each source:

1. open official source page;
2. verify title/document ID;
3. verify issuing authority;
4. classify authority;
5. verify binding state;
6. verify amendment/consolidation state;
7. verify dates;
8. verify authentic-language/translation state;
9. verify rights/use state;
10. choose acquisition method.

Any unresolved material field => `SOURCE_NOT_READY`.

## Phase 3 — Acquire source

### URL source

- use official URL;
- record retrieval date;
- record exact page/document identity;
- test accessibility;
- assign Notebook pack.

### Downloaded source

- download only where permitted;
- store local filename in ledger;
- compute SHA-256;
- record size/content type;
- open and verify content identity;
- never treat the hash as legal authenticity.

### Manual portal source

- use exact official portal search;
- record search terms/document number;
- record final official identity/URL;
- do not invent a deep link.

### Paywalled/licensed source

- keep metadata only unless the user's license permits the intended upload/use;
- never bypass technical or contractual controls.

## Phase 4 — Update acquisition ledger

A source cannot proceed to Notebook until its ledger row records at least:

```text
SOURCE_ID
BATCH_ID
VERIFICATION_STATE
OFFICIAL_URL
RETRIEVAL_DATE
AUTHORITY_CLASS
BINDING_STATE
VERSION_STATE
RIGHTS_STATE
ACQUISITION_METHOD
LOCAL_FILENAME_OR_URL
SHA256_IF_FILE
CONTENT_IDENTITY_CHECKED
NOTEBOOK_PACK
```

## Phase 5 — Prepare Notebook pack

- use the pack assignment file;
- retain authority labels in source titles;
- exclude unverified and restricted sources;
- leave capacity for amendments/cases/challenge material;
- preserve old versions only when temporal comparison is needed.

Recommended title convention:

`<SOURCE_ID> | <AUTHORITY_CLASS> | <DOCUMENT_ID> | <SHORT_TITLE>`

## Phase 6 — Upload / ingest

- add sources to the designated Notebook;
- record Notebook name and source count;
- record upload/ingest date;
- do not exceed current product limits;
- if Google Drive is used, record whether the source is synchronized or a static upload.

## Phase 7 — Mandatory Notebook ingestion test

Before any legal synthesis ask Notebook:

> List every loaded source with SOURCE_ID, title, document ID, jurisdiction, visible date, authority class, and an exact section/article/page locator that proves you have ingested the expected source. Do not infer missing metadata.

Compare its answer with the GitHub manifest.

Classify each source:

```text
INGEST_VERIFIED
INGEST_PARTIAL
INGEST_MISMATCH
INGEST_FAILED
```

Only `INGEST_VERIFIED` sources are eligible for material analysis.

## Phase 8 — Mandatory authority-separation test

Ask Notebook to separate the source set into:

- binding primary law;
- court/regulatory decisions;
- official guidance;
- soft law;
- technical standards/frameworks;
- policy proposals;
- scholarship;
- incident evidence;
- allegations;
- model-generated supporting research.

If Notebook conflates them, fix source labels/prompting and retest.

## Phase 9 — Analysis questions

Use `NOTEBOOKLM_RESEARCH_QUESTION_CATALOG.md`.

Each answer must identify:

```text
SOURCE_IDS
SOURCE_LOCATORS
JURISDICTION
AUTHORITY_CLASS
LEGAL_DATE_STATE
KNOWN
UNKNOWN
CONFLICT
LIMITATION
```

Never request a single global legal answer where jurisdiction-specific treatment is required.

## Phase 10 — Export findings

Export/copy Notebook findings into an AI-LAWS supporting-research artifact with:

```text
NOTEBOOK_OUTPUT_CLASS = SUPPORTING_RESEARCH
CANONICAL = FALSE
PRIMARY_SOURCE_RECHECK_REQUIRED = YES
```

No model answer becomes law merely because citations are present.

## Phase 11 — Primary-source recheck

For every material finding:

1. reopen cited source;
2. verify cited article/section/holding;
3. verify date/currentness;
4. verify exception/scope/definition;
5. verify translation where relevant;
6. classify finding `VERIFIED / PARTIAL / CONFLICT / UNKNOWN`.

Do not silently repair Notebook mistakes; record them.

## Phase 12 — Claim/evidence record

Only after Phase 11 create/update claim records.

For liability claims keep separate:

`actor → duty → breach → causation → damage → remedy → defence → evidence`.

For rights claims identify the exact legal source and jurisdiction.

For policy proposals label them as proposals.

## Phase 13 — Human review gate

Escalate to qualified human legal review before consequential legal conclusions, filings, accusations, final liability allocation or high-stakes action recommendations.

## Phase 14 — Cross-repo routing

Route verified legal evidence/proposals only:

- OWASP — technical security implications;
- Engineering OS — candidate requirements/controls/tests;
- Ethical-AI — human agency/dignity/appeal implications;
- Esmaul Husna — human-facing reminder candidate only;
- Apesteori — multidimensional challenge/unknown candidate.

Destination repositories must accept independently.

## Phase 15 — Refresh schedule

Set source refresh triggers for:

- amendment/corrigendum;
- new consolidated text;
- effective/application date;
- transposition deadline;
- treaty-status change;
- new court/regulator interpretation;
- source URL replacement;
- assigned freshness interval.

## Phase 16 — Close batch

Record exact:

```text
BATCH_ID
BASE_HEAD
FINAL_HEAD
PACK
SOURCES_PLANNED
SOURCES_READY
SOURCES_ACQUIRED
SOURCES_INGEST_VERIFIED
SOURCES_FAILED
CLAIMS_EXTRACTED
CLAIMS_PRIMARY_RECHECKED
CONFLICTS
UNKNOWNS
HUMAN_REVIEW_ITEMS
NEXT_BOUNDED_UNIT
AUTO_ADVANCE = NO
```

STOP before the next batch unless explicitly authorized.
