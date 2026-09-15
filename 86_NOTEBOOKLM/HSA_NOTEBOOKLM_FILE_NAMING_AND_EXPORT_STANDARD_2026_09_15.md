# HSA / AI-LAWS NotebookLM File Naming and Export Standard

DATE: 2026-09-15
STATE: PROPOSAL / NONCANONICAL UNTIL ACCEPTED
PROJECT: AI-LAWS / HSA
AUTO_ADVANCE: NO

## 1. Purpose

NotebookLM outputs must be identifiable after download without reopening the Notebook conversation.

A Notebook answer in chat is not sufficient when the requested result is intended to become a durable HSA/AI-LAWS research artifact.

Every run must use deterministic filenames and stable run metadata.

## 2. Core filename pattern

Single-source artifact:

```text
AI-LAWS__<PACK_ID>__<SOURCE_ID>__<SHORT_TITLE>__<ARTIFACT_TYPE>__<RUN_ID>.<ext>
```

Pack-level artifact:

```text
AI-LAWS__<PACK_ID>__PACK__<PACK_SHORT_TITLE>__<ARTIFACT_TYPE>__<RUN_ID>.<ext>
```

Cross-pack artifact:

```text
AI-LAWS__CROSSPACK__ALL__HSA__<ARTIFACT_TYPE>__<RUN_ID>.<ext>
```

## 3. RUN_ID

Format:

```text
RUN-YYYYMMDD-NNN
```

Examples:

```text
RUN-20260915-001
RUN-20260915-002
```

The RUN_ID must be unique within the date and must be repeated inside every output artifact header/metadata block.

## 4. PACK_ID

Allowed values:

```text
NB00
NB01
NB02
NB03
NB04
NB05
NB06
NB07
NB08
NB09
CROSSPACK
```

## 5. SOURCE_ID

Use the exact AI-LAWS owner-native source ID from `86_NOTEBOOKLM/NOTEBOOK_UPLOAD_SELECTION.csv`.

Examples:

```text
EU-001
TR-002
INT-004
INC-001
US-003
CN-004
GB-011
JP-001
KR-001
```

Do not invent or renumber SOURCE_ID values.

## 6. SHORT_TITLE

SHORT_TITLE is human-readable and short.

Rules:

- 2-8 meaningful words/tokens when practical;
- uppercase ASCII preferred for filename portability;
- spaces converted to hyphens;
- no slashes, colon, question mark, asterisk, quotation mark or filesystem-reserved characters;
- do not replace the legal identity; SOURCE_ID remains controlling;
- keep recognisable abbreviations such as AI-ACT, GDPR, KVKK, NIS2, CRA, AI-RMF.

Examples:

```text
AI-ACT
PRODUCT-LIABILITY-DIRECTIVE
GDPR
KVKK
TURK-CYBERSECURITY-LAW
OPENAI-HF-INCIDENT
ANTHROPIC-THREAT-INTELLIGENCE
UNESCO-NEUROTECH-RECOMMENDATION
```

## 7. Mandatory artifact types for a single-source run

Every completed single-source investigation should produce the following artifact set unless the source type makes a table inapplicable. If inapplicable, still create the run manifest and analysis report and mark the omitted artifact `NOT_APPLICABLE` in the manifest.

```text
RUN-MANIFEST.csv
SOURCE-IDENTITY-CARD.md
SOURCE-ANALYSIS.md
ACTOR-DUTY-SAFEGUARD-MATRIX.csv
HSA-THREAT-CROSSWALK.csv
EVIDENCE-ACCOUNTABILITY-MATRIX.csv
UNKNOWN-CONFLICT-REGISTER.csv
ENGINEERING-CANDIDATES.csv
```

Example filenames for EU-001:

```text
AI-LAWS__NB02__EU-001__AI-ACT__RUN-MANIFEST__RUN-20260915-001.csv
AI-LAWS__NB02__EU-001__AI-ACT__SOURCE-IDENTITY-CARD__RUN-20260915-001.md
AI-LAWS__NB02__EU-001__AI-ACT__SOURCE-ANALYSIS__RUN-20260915-001.md
AI-LAWS__NB02__EU-001__AI-ACT__ACTOR-DUTY-SAFEGUARD-MATRIX__RUN-20260915-001.csv
AI-LAWS__NB02__EU-001__AI-ACT__HSA-THREAT-CROSSWALK__RUN-20260915-001.csv
AI-LAWS__NB02__EU-001__AI-ACT__EVIDENCE-ACCOUNTABILITY-MATRIX__RUN-20260915-001.csv
AI-LAWS__NB02__EU-001__AI-ACT__UNKNOWN-CONFLICT-REGISTER__RUN-20260915-001.csv
AI-LAWS__NB02__EU-001__AI-ACT__ENGINEERING-CANDIDATES__RUN-20260915-001.csv
```

## 8. Pack-level mandatory artifact types

After source-by-source analysis of a pack, create:

```text
PACK-RUN-MANIFEST.csv
SOURCE-AUTHORITY-MATRIX.csv
ACTOR-DUTY-RIGHTS-MATRIX.csv
HSA-THREAT-SOURCE-CROSSWALK.csv
EVIDENCE-REQUIREMENT-MATRIX.csv
EXCEPTION-DEFENCE-MATRIX.csv
CONFLICT-UNKNOWN-REGISTER.csv
CONTROL-TEST-CANDIDATES.csv
RESEARCH-BACKLOG.csv
PACK-SYNTHESIS.md
```

Example:

```text
AI-LAWS__NB02__PACK__EU-AI-LAW__ACTOR-DUTY-RIGHTS-MATRIX__RUN-20260915-010.csv
AI-LAWS__NB02__PACK__EU-AI-LAW__PACK-SYNTHESIS__RUN-20260915-010.md
```

## 9. Cross-pack mandatory artifacts

After all authorised pack runs:

```text
GLOBAL-AUTHORITY-MAP.csv
GLOBAL-ACTOR-DUTY-CROSSWALK.csv
GLOBAL-HSA-THREAT-COVERAGE.csv
GLOBAL-EVIDENCE-GAP-MATRIX.csv
GLOBAL-CONFLICT-UNKNOWN-REGISTER.csv
GLOBAL-RESEARCH-BACKLOG.csv
GLOBAL-CONTROL-TEST-CANDIDATES.csv
GLOBAL-GAP-SYNTHESIS.md
```

## 10. Mandatory header inside every Markdown artifact

```yaml
project: AI-LAWS
program: HSA
run_id: RUN-YYYYMMDD-NNN
notebook_pack: NBxx
source_id: <SOURCE_ID or MULTI>
source_title: <human title>
artifact_type: <ARTIFACT_TYPE>
created_date: YYYY-MM-DD
canonical: false
promotion_state: SUPPORTING_RESEARCH
primary_source_recheck_required: true|false
selected_sources_only: true
```

## 11. Mandatory columns in RUN-MANIFEST.csv

```text
RUN_ID
PACK_ID
SOURCE_ID
SHORT_TITLE
ARTIFACT_TYPE
EXPECTED_FILENAME
FORMAT
PRODUCTION_STATE
NOT_APPLICABLE_REASON
SOURCE_SELECTION_CONFIRMED
CANONICAL
PROMOTION_STATE
NOTES
```

`CANONICAL` must always be `FALSE` for raw NotebookLM outputs.

## 12. File-production rule

If the Notebook interface supports creating downloadable files, reports, tables or artifacts, create the requested artifacts using the exact filename or exact filename stem above.

If the interface cannot directly create the requested `.csv` or `.md` file type:

1. do not silently fall back to one conversational answer;
2. create one separate report/table/artifact per required output where the interface permits;
3. title each artifact with the exact filename stem;
4. begin each artifact with `TARGET_FILENAME: <exact filename>`;
5. preserve CSV as RFC-4180-style comma-separated tabular content where possible;
6. preserve Markdown as Markdown, not prose commentary around Markdown;
7. mark `EXPORT_REQUIRED_BY_WORK = YES` in the run manifest;
8. ChatGPT Work will export/normalize the artifact without changing source-derived meaning.

## 13. No-copy-from-chat rule

The normal success condition is not `ANSWERED_IN_CHAT`.

Preferred states:

```text
FILE_CREATED
REPORT_CREATED_FOR_EXPORT
TABLE_CREATED_FOR_EXPORT
```

Only if the product surface genuinely cannot create a durable artifact may the state be:

```text
CHAT_ONLY_FALLBACK
```

When `CHAT_ONLY_FALLBACK`, the answer must still be divided into exact artifact sections with `TARGET_FILENAME` markers so Work can extract them deterministically.

## 14. Promotion firewall

```text
NOTEBOOK_FILE_CREATED != VERIFIED_FINDING
NOTEBOOK_TABLE_CREATED != CANONICAL_DATABASE_ROW
NOTEBOOK_SYNTHESIS != LEGAL_AUTHORITY
FILE_NAME != SOURCE_AUTHORITY
```

Notebook artifacts remain noncanonical until destination-local verification and Engineering OS reconciliation.

## 15. Special-source rules

- `CL-002`: HOLD; official full text unavailable. Do not generate verified case-law artifacts.
- `INT-004`: use current UNESCO certified-copy source; legacy 43GC PDF is not current primary.
- Türkiye snapshot sources: include `CURRENTNESS-RECHECK` in analysis limitations; material legal claims require live official recheck.
- `INC-*`: distinguish factual observation, company/vendor attribution, independent corroboration and hypothesis.
- `INC-004`: context/policy only, not incident evidence.
- `STD-*`: metadata/current official standard reference only unless licensed full text is lawfully available.

AUTO_ADVANCE = NO
