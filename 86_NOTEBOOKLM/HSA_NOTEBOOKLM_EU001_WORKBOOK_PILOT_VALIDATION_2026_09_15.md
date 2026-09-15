# HSA / AI-LAWS NotebookLM — EU-001 Workbook Pilot Validation

DATE: 2026-09-15
SOURCE_FOLDER: `86_NOTEBOOKLM/downloads-notebooklm/AI-LAWS__EU__EU-001 new/`
SOURCE_ID: `EU-001`
EXPECTED_PACK_ID: `NB02`
STATE: `FORMAT_ACCEPTED_WITH_PROMPT_V2_HARDENING`
CANONICAL: `FALSE`

## Observed pilot structure

The pilot folder contains exactly two deliverables:

- one `.xlsx` workbook
- one `.md` source-analysis report

The XLSX binary contains eight worksheet parts, matching the intended multi-tab workbook architecture. The Markdown report contains S1–S7 source analysis and preserves source locators.

This confirms that the preferred human-operational output model should be:

```text
ONE XLSX MULTI-TAB WORKBOOK
+
ONE MD SOURCE ANALYSIS
```

The prior 6–8 separate CSV/MD output model remains a fallback/normalized-exchange model only.

## Required corrections before using this format for all sources

### 1. Filename traceability
The pilot filenames were truncated and did not preserve the expected RUN_ID suffix. Use the shorter V2 filename contract:

```text
AILAWS__<PACK_ID>__<SOURCE_ID>__<SHORT_TITLE>__<RUN_ID>.xlsx
AILAWS__<PACK_ID>__<SOURCE_ID>__<SHORT_TITLE>__<RUN_ID>.md
```

### 2. PACK_ID must not be inferred from jurisdiction
The pilot Markdown records `PACK_ID=EU`; the AI-LAWS routing source places `EU-001` in `NB02`.

Required:

```text
PACK_ID = value from NOTEBOOK_UPLOAD_SELECTION.csv
EU-001 => NB02
```

### 3. HSA IDs must not be invented
The previous legacy pilot generated its own THR-ID/name meanings. The new pilot improved this by using textual threat descriptions. Continue to enforce:

```text
NO AUTHORITATIVE HSA TAXONOMY IN SELECTED SOURCES
=> THREAT_ID=UNKNOWN
```

NotebookLM must not create or redefine threat/control/test IDs.

### 4. Promotion and source recheck
NotebookLM output remains supporting research. Default:

```text
PROMOTION_STATE=SUPPORTING_RESEARCH
```

`PRIMARY_SOURCE_RECHECK_REQUIRED` must be `TRUE` when currentness/authority is uncertain or the AI-LAWS source-control record requires a currentness check. NotebookLM may not infer `FALSE` merely because the loaded PDF appears official/current.

### 5. Destination/reviewer fields
Do not fabricate repository/lane names or working groups.

For AI-LAWS source analysis:

```text
DESTINATION_REPO=fatihekler/ai-laws (or REPO-LAW)
REVIEW_OWNER=AI-LAWS
```

If a qualified human/external reviewer is required but not already assigned:

```text
REVIEW_OWNER=HUMAN_REVIEW_REQUIRED
```

### 6. EEA wording firewall
`Text with EEA relevance` does not by itself establish direct applicability in every EEA state. Do not convert EEA relevance into binding/applicability claims without a selected EEA incorporation/authority source.

### 7. Source-required vs research-useful engineering evidence
NotebookLM must not upgrade an engineering best practice into a legal source requirement. Example:

```text
SOURCE EXPLICITLY REQUIRES INTEGRITY FEATURE => SOURCE_REQUIRED
OTHERWISE => RESEARCH_USEFUL
```

### 8. Engineering IDs
NotebookLM may suggest textual control/test candidates but must not assign destination control/test IDs.

```text
CONTROL_ID/TEST_ID assignment belongs to destination governance / Engineering OS.
```

## Preferred workbook tabs

```text
00_MANIFEST
01_SOURCE_IDENTITY
02_ACTOR_DUTY
03_HSA_THREATS
04_EVIDENCE
05_UNKNOWN_CONFLICT
06_ENGINEERING
07_LOCATOR_INDEX
```

## Decision

The 1-XLSX + 1-MD format is accepted as the preferred NotebookLM single-source working format, subject to the V2 prompt rules above.

Use:

`86_NOTEBOOKLM/HSA_NOTEBOOKLM_SINGLE_SOURCE_WORKBOOK_PROMPT_V2_2026_09_15.txt`

for the next pilot/source.

Do not retrospectively delete the legacy EU-001 files; retain them as audit evidence.

AUTO_ADVANCE = NO
