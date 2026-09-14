#!/usr/bin/env python3
from pathlib import Path
import csv, io

ROOT = Path('.')
CTX = ROOT / '00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md'
QUEUE = ROOT / '90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv'
CLOSE = ROOT / '95_RESEARCH/NOTEBOOK_READINESS/AI-LAWS-R034_CLOSEOUT_2026-09-14.md'
BASE_HEAD = 'dfdfd5fa868b5ddc8ecbecb0c803a2b08c0012ca'
NAMESPACE_COMMIT = '7c3c7163ed473a41b4d5ce8549c1d46344ad565e'
STATE = 'COMPLETE_HUMAN_READABLE_NAMESPACE_AND_NOTEBOOK_READINESS'

# Queue: append exactly once without reserializing prior rows.
q = QUEUE.read_text(encoding='utf-8')
if 'AI-LAWS-R034,' not in q:
    out = io.StringIO()
    w = csv.writer(out, lineterminator='\n')
    w.writerow([
        'AI-LAWS-R034','P0','Notebook namespace/readiness',
        'Human-readable canonical filename normalization, rename audit, source catalog, Notebook labels and pack readiness',
        STATE,
        'R023-R033 source labeling/validation state; R019 not required',
        '86_NOTEBOOKLM/downloads/RENAME_MANIFEST.csv; 86_NOTEBOOKLM/downloads/ORIGINAL_FILENAME_INDEX.csv; 86_NOTEBOOKLM/downloads/NOTEBOOK_SOURCE_LABELS.csv; 86_NOTEBOOKLM/downloads/MANUAL_DOWNLOAD_AND_UPLOAD_REQUESTS.csv; 86_NOTEBOOKLM/SOURCE_CATALOG.md; 86_NOTEBOOKLM/NOTEBOOK_READINESS_MATRIX.csv; 86_NOTEBOOKLM/AI-LAWS-R034_NAMESPACE_AND_NOTEBOOK_READINESS_ASSESSMENT_2026-09-14.md; 95_RESEARCH/NOTEBOOK_READINESS/AI-LAWS-R034_CLOSEOUT_2026-09-14.md',
        '38 repository PDFs renamed with identical pre/post SHA-256; core Notebook ingestion ready; stop before Notebook ingestion; R019 remains explicit-only'
    ])
    if q and not q.endswith('\n'):
        q += '\n'
    QUEUE.write_text(q + out.getvalue(), encoding='utf-8')
else:
    assert STATE in q

# Current context: state + completed unit + explicit R034 section.
text = CTX.read_text(encoding='utf-8')
state_token = ' / LEGAL_RESEARCH_ACTIVE'
if 'R034_NAMESPACE_NOTEBOOK_READINESS_COMPLETE' not in text.split('\n', 8)[5]:
    assert state_token in text
    text = text.replace(state_token, ' / R034_NAMESPACE_NOTEBOOK_READINESS_COMPLETE' + state_token, 1)

completed = 'AI-LAWS-R034 = COMPLETE_HUMAN_READABLE_NAMESPACE_AND_NOTEBOOK_READINESS'
if completed not in text:
    anchor = 'AI-LAWS-R033 = COMPLETE_SUPPORT_SOURCE_VALIDATION'
    assert anchor in text
    text = text.replace(anchor, anchor + '\n' + completed, 1)

section = '''\n### R034 — Human-readable namespace and Notebook readiness\n\nR034 normalized the repository source namespace without changing PDF bytes or legal/source classifications. All 38 repository PDFs were renamed using human-readable SOURCE_ID + jurisdiction + institution + document-type + version/document-ID prefixes while preserving the human title. The pre/post SHA-256 value matched for every file.\n\n```text\nR034_REPOSITORY_PDF_COUNT = 38\nR034_CONTENT_IDENTITY_VERIFIED_COUNT = 33\nR034_CONTENT_IDENTITY_PARTIAL_COUNT = 4\nR034_SUPERSEDED_COUNT = 1\nR034_PDF_FILES_RENAMED = 38\nR034_PDF_FILES_CONTENT_CHANGED = 0\nR034_MANIFEST_SOURCE_COUNT = 73\nR034_MANUAL_DOWNLOAD_REQUEST_ROWS = 12\nR034_CORE_NOTEBOOK_INGESTION_READY = YES\n```\n\nNotebook readiness is now explicit: NB00 ready; NB01 ready with URL routing/superseded exclusion; NB02 ready as 10/10 verified official PDF snapshots; NB03 ready as 7 verified PDFs plus one live-URL/supporting-print source; NB04 ready with currentness warnings; NB05 ready from official URL sets; NB06 core ready with CL-002 case-layer hold; NB07 ready by reusing verified sources; NB08 partially ready with INC-001 hold for a fully verified pack.\n\nManual user-assist requests are separated from blockers. `TR-001..TR-008` are optional live-currentness refreshes and do not block NB04 snapshot ingestion. `CL-002` blocks the NB06 case layer. `INC-001` blocks a fully verified NB08 primary-disclosure layer. `INT-004` local download is only a fallback if certified-copy URL ingestion fails. `TR-009` PDF capture is optional policy context.\n\n```text\nOPEN_RESEARCH != NOTEBOOK_UPLOAD_BLOCKER\nPDF_TO_MD_BULK_CONVERSION = NOT_REQUIRED\nCORE_NOTEBOOK_INGESTION_READY = YES\nNEXT_BOUNDED_UNIT = AI-LAWS NOTEBOOK PACK INGESTION\nR019 = READY_FOR_EXPLICIT_AUTHORIZATION\nAUTO_ADVANCE = NO\n```\n\nDurable navigation and audit files are under `86_NOTEBOOKLM/` and `86_NOTEBOOKLM/downloads/`; no Notebook ingestion was performed by R034.\n'''
if '### R034 — Human-readable namespace and Notebook readiness' not in text:
    text += section
CTX.write_text(text.rstrip() + '\n', encoding='utf-8')

CLOSE.parent.mkdir(parents=True, exist_ok=True)
close = f'''# AI-LAWS-R034 — Human-Readable Namespace and Notebook Readiness Closeout\n\n**UNIT_ID:** `AI-LAWS-R034`\n**DATE:** 2026-09-14\n**UNIT_TYPE:** `HUMAN_READABLE_NAMESPACE_AND_NOTEBOOK_READINESS`\n**BASE_HEAD:** `{BASE_HEAD}`\n**R034_NAMESPACE_COMMIT:** `{NAMESPACE_COMMIT}`\n**STATE:** `{STATE}`\n**LEGAL_ADVICE:** NO\n**MODEL_OUTPUT_CANONICAL:** NO\n**NOTEBOOK_OUTPUT_CANONICAL:** NO\n**AUTO_ADVANCE:** NO\n\n## Exact result\n\n```text\nPDF_FILES_CONSIDERED = 38\nPDF_FILES_RENAMED = 38\nPDF_FILES_CONTENT_CHANGED = 0\n\nCONTENT_IDENTITY_VERIFIED_COUNT = 33\nCONTENT_IDENTITY_PARTIAL_COUNT = 4\nSUPERSEDED_COUNT = 1\n\nSOURCE_IDS_CHANGED = 0\nAUTHORITY_CLASSES_CHANGED = 0\nLEGAL_CLAIMS_CREATED = 0\nPDF_CONTENT_MODIFIED = 0\n\nSOURCE_CATALOG_CREATED = YES\nORIGINAL_FILENAME_INDEX_CREATED = YES\nRENAME_MANIFEST_CREATED = YES\nNOTEBOOK_SOURCE_LABELS_CREATED = YES\nMANUAL_DOWNLOAD_REQUEST_LIST_CREATED = YES\nNOTEBOOK_READINESS_MATRIX_CREATED = YES\n\nNB00_READY = READY\nNB01_READY = READY_WITH_URL_ROUTING_AND_SUPERSEDED_EXCLUSION\nNB02_READY = READY_PDF\nNB03_READY = READY_MIXED\nNB04_READY = READY_WITH_CURRENTNESS_WARNING\nNB05_READY = READY_URL_WITH_CURRENTNESS_WARNINGS\nNB06_READY = READY_WITH_HOLD_CL002\nNB07_READY = READY_REUSE_VERIFIED_SOURCES\nNB08_READY = PARTIAL_READY_HOLD_INC001\n\nCORE_NOTEBOOK_INGESTION_READY = YES\nNEXT_BOUNDED_UNIT = AI-LAWS NOTEBOOK PACK INGESTION\n```\n\n## Rename integrity\n\n`86_NOTEBOOKLM/downloads/RENAME_MANIFEST.csv` records every old/new filename and pre/post SHA-256. All 38 rows are `content_changed=NO` and `rename_state=RENAMED_VERIFIED`. The operation was namespace normalization only; PDF bytes were not rewritten.\n\n## Human navigation\n\n- `86_NOTEBOOKLM/SOURCE_CATALOG.md` — readable source library/catalog.\n- `86_NOTEBOOKLM/downloads/ORIGINAL_FILENAME_INDEX.csv` — old-to-new filename lookup.\n- `86_NOTEBOOKLM/downloads/NOTEBOOK_SOURCE_LABELS.csv` — shorter Notebook source labels.\n- `86_NOTEBOOKLM/NOTEBOOK_READINESS_MATRIX.csv` — pack-level readiness.\n- `86_NOTEBOOKLM/downloads/MANUAL_DOWNLOAD_AND_UPLOAD_REQUESTS.csv` — exact user-assist/download list with blocker classification.\n\n## Manual download distinction\n\n```text\nACTUAL_CORE_INGESTION_BLOCKERS = 0\nNB06_CASE_LAYER_BLOCKER = CL-002_OFFICIAL_FULLTEXT\nFULL_NB08_BLOCKER = INC-001_OFFICIAL_SOURCE_RECHECK\nTR001_TR008_LIVE_RECHECK = OPTIONAL_FOR_INGESTION_REQUIRED_BEFORE_MATERIAL_CURRENT_LAW_CONCLUSION\nINT004_LOCAL_FILE = FALLBACK_ONLY\nTR009_POLICY_PDF = OPTIONAL\n```\n\n## Preserved controls\n\n- R005 remains live-official-currentness blocked; existing Türkiye repository snapshots remain usable only with warnings.\n- R006 remains blocked by official decision-source availability.\n- R019 remains `READY_FOR_EXPLICIT_AUTHORIZATION` and was not started.\n- No bulk PDF-to-Markdown conversion was performed.\n- No OCR was performed.\n- No Notebook ingestion was performed.\n- No ZIP or workflow artifact was created.\n- No substantive legal research or legal conclusion was created by R034.\n\n```text\nLEGAL_ADVICE = NO\nMODEL_OUTPUT_CANONICAL = NO\nNOTEBOOK_OUTPUT_CANONICAL = NO\nUNKNOWN_PRESERVED = YES\nAUTO_ADVANCE = NO\nSTOP = YES\n```\n'''
CLOSE.write_text(close, encoding='utf-8')

print('R034_RECONCILED=YES')
print(f'R034_NAMESPACE_COMMIT={NAMESPACE_COMMIT}')
print('PDF_FILES_RENAMED=38')
print('PDF_FILES_CONTENT_CHANGED=0')
print('CORE_NOTEBOOK_INGESTION_READY=YES')
print('R019_STATE=READY_FOR_EXPLICIT_AUTHORIZATION')
print('AUTO_ADVANCE=NO')
