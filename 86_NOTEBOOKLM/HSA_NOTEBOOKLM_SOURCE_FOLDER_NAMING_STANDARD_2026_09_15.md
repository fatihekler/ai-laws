# AI-LAWS / HSA — NOTEBOOKLM SOURCE FOLDER NAMING STANDARD

**DATE:** 2026-09-15  
**STATE:** WORKING STANDARD / NONCANONICAL UNTIL PR ACCEPTANCE

For all subsequent single-source NotebookLM exports, store the two-file pair under:

```text
86_NOTEBOOKLM/downloads-notebooklm/AI-LAWS__<PACK_ID>__<SOURCE_ID>/
```

Examples:

```text
AI-LAWS__NB02__EU-001/
AI-LAWS__NB02__EU-002/
AI-LAWS__NB04__TR-002/
AI-LAWS__NB08__INC-001/
```

Inside each folder, use the approved pair:

```text
AILAWS__<PACK_ID>__<SOURCE_ID>__<SHORT_TITLE>__<RUN_ID>.xlsx
AILAWS__<PACK_ID>__<SOURCE_ID>__<SHORT_TITLE>__<RUN_ID>.md
```

Rules:

```text
PACK_ID = exact AI-LAWS Notebook pack ID
SOURCE_ID = existing owner-native AI-LAWS source ID
RUN_ID = RUN-YYYYMMDD-NNN
FOLDER NAME != LEGAL CONCLUSION
FOLDER NAME != PROMOTION STATE
```

Do not append `new`, `v2`, `final`, `final2`, or similar ad-hoc suffixes for normal production runs. Version/run identity belongs in `RUN_ID` inside the filenames. Test/pilot folders may retain historical suffixes for audit evidence but should not establish the production convention.

Each production source folder should normally contain exactly:

```text
1 x XLSX
1 x MD
```

Separate CSV files are fallback-only under the approved single-source workbook standard.
