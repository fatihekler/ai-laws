from __future__ import annotations

import csv
import io
import subprocess
from pathlib import Path

ROOT = Path('.')
DATE = '2026-09-14'
BATCH = 'NB-BATCH-NB04-20260914-002'
SOURCE_ID = 'TR-009'
OFFICIAL_PAGE = 'https://www.sanayi.gov.tr/plan-program-raporlar-ve-yayinlar/strateji-belgeleri'
OFFICIAL_ANNOUNCEMENT = 'https://www.sanayi.gov.tr/medya/haber/turkiye-yapay-zek%C3%A2-eylem-plani-aciklandi'
TITLE = 'Türkiye Yapay Zekâ Eylem Planı (2026-2030)'
DOC_ID = 'Türkiye Yapay Zekâ Eylem Planı 2026-2030'
AUTHORITY = 'T.C. Sanayi ve Teknoloji Bakanlığı'


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding='utf-8')


def write_text(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding='utf-8', newline='')


def read_csv(path: str):
    text = read_text(path)
    reader = csv.DictReader(io.StringIO(text))
    rows = list(reader)
    return reader.fieldnames, rows


def write_csv(path: str, fields, rows) -> None:
    out = io.StringIO(newline='')
    w = csv.DictWriter(out, fieldnames=fields, lineterminator='\n')
    w.writeheader()
    w.writerows(rows)
    write_text(path, out.getvalue())


def exactly_one(rows, key, value):
    hits = [r for r in rows if r.get(key) == value]
    if len(hits) != 1:
        raise SystemExit(f'expected exactly one {key}={value}, got {len(hits)}')
    return hits[0]


# 1) Manifest: move TR-009 from unidentified current policy source to the current 2026-2030 plan.
manifest_path = '86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv'
fields, rows = read_csv(manifest_path)
r = exactly_one(rows, 'source_id', SOURCE_ID)
r.update({
    'title': TITLE,
    'document_id': DOC_ID,
    'authority_class': 'OFFICIAL_GUIDANCE',
    'binding_state': 'national AI policy/action plan; nonbinding policy source; not statute',
    'official_url': OFFICIAL_PAGE,
    'preferred_ingest': 'URL_DIRECT_PREFERRED',
    'priority': 'P1',
    'verification_state': 'CURRENT_OFFICIAL_ACTION_PLAN_IDENTITY_VERIFIED_2026_2030; OFFICIAL_PDF_BODY_UNRESOLVED_IN_GITHUB_RUNNER',
    'last_verified': DATE,
    'rights_or_use_state': 'OFFICIAL_PUBLIC_URL; REPOSITORY_BINARY_VENDORING_RIGHTS_NOT_EVALUATED',
    'notes': (
        'Current Ministry strategy-document index identifies Türkiye Yapay Zekâ Eylem Planı (2026-2030). '
        'Official Ministry announcement dated 13 Jun 2026 confirms the plan and its Fark Et / İstifade Et / Üret / Yönet policy axes. '
        'The 2021-2025 strategy and 2024-2025 action-plan materials are historical context, not the current primary policy plan. '
        'GitHub-runner direct requests to the Ministry site returned a generic HTML shell and did not expose the exact downloadable PDF body; '
        'therefore no PDF SHA-256, byte size, content-identity verification or repository binary is claimed. Policy/guidance is not binding law.'
    ),
})
write_csv(manifest_path, fields, rows)


# 2) Pack assignment: preserve OPTIONAL status, make current source semantics explicit.
pack_path = '86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_PACK_ASSIGNMENTS.csv'
fields, rows = read_csv(pack_path)
r = exactly_one(rows, 'source_id', SOURCE_ID)
if r.get('pack_id') != 'NB04':
    raise SystemExit('TR-009 pack drift')
r['requirement'] = 'OPTIONAL_AFTER_R005'
r['reason'] = 'Current 2026-2030 national AI action-plan policy context; nonbinding guidance/policy, not statute'
write_csv(pack_path, fields, rows)


# 3) Acquisition/validation ledger: append one fail-closed source-pin record.
ledger_path = '86_NOTEBOOKLM/NOTEBOOKLM_ACQUISITION_AND_VALIDATION_LEDGER.csv'
fields, rows = read_csv(ledger_path)
if not any(x.get('batch_id') == BATCH and x.get('source_id') == SOURCE_ID for x in rows):
    row = {f: '' for f in fields}
    row.update({
        'batch_id': BATCH,
        'source_id': SOURCE_ID,
        'notebook_pack': 'NB04',
        'jurisdiction': 'TR',
        'title': TITLE,
        'document_id': DOC_ID,
        'issuing_authority': AUTHORITY,
        'authority_class': 'OFFICIAL_GUIDANCE',
        'binding_state': 'national policy/action plan; nonbinding; not statute',
        'official_url': OFFICIAL_PAGE,
        'retrieval_date': DATE,
        'version_state': 'CURRENT_2026_2030_ACTION_PLAN_IDENTITY_VERIFIED; EXACT_OFFICIAL_PDF_BODY_UNRESOLVED_IN_GITHUB_RUNNER',
        'adoption_date': 'UNKNOWN_NOT_REQUIRED_FOR_POLICY_IDENTITY_PIN',
        'publication_date': '2026-06-13_OFFICIAL_ANNOUNCEMENT',
        'entry_into_force_date': 'NOT_APPLICABLE_POLICY_SOURCE',
        'application_date': '2026-2030_POLICY_HORIZON',
        'authentic_language': 'Turkish',
        'translation_state': 'NOT_APPLICABLE',
        'rights_state': 'OFFICIAL_PUBLIC_URL; REPOSITORY_BINARY_VENDORING_RIGHTS_NOT_EVALUATED',
        'acquisition_method': 'URL_DIRECT_PREFERRED',
        'local_filename_or_url': OFFICIAL_PAGE,
        'sha256': '',
        'byte_size': '',
        'content_type': 'official Ministry web source; exact PDF body not acquired',
        'content_identity_checked': 'WEB_OFFICIAL_CURRENT_POLICY_IDENTITY_VERIFIED; PDF_BODY_UNRESOLVED',
        'notebook_name': '',
        'notebook_ingest_date': '',
        'notebook_ingest_state': 'NOT_RUN',
        'notebook_locator_test': 'NOT_RUN',
        'primary_source_recheck_state': 'OFFICIAL_POLICY_PAGE_AND_ANNOUNCEMENT_IDENTITY_VERIFIED; PDF_BINARY_NOT_VERIFIED',
        'refresh_trigger': 'Ministry replacement revision new action plan or 2030 horizon/current-policy change',
        'human_review_required': 'YES_BEFORE_ANY_BINDING_LEGAL_EFFECT_CLAIM',
        'notes': (
            'R033 current-policy source pin. Official Ministry strategy-document listing identifies the 2026-2030 Türkiye Yapay Zekâ Eylem Planı; '
            'official 13 Jun 2026 announcement confirms release. Four policy axes are Fark Et, İstifade Et, Üret, Yönet. '
            'Current source is policy/guidance, not statute. GitHub runner received a generic Ministry HTML shell and could not obtain the exact PDF body, '
            'so PDF hash/byte size/content identity remain UNKNOWN and no binary was vendored.'
        ),
    })
    rows.append(row)
write_csv(ledger_path, fields, rows)


# 4) Dedicated durable results table.
results_path = '86_NOTEBOOKLM/downloads/TR009_CURRENT_POLICY_SOURCE_RESULTS.csv'
results_fields = [
    'source_id','current_title','policy_period','issuing_authority','authority_class','binding_state',
    'official_strategy_page','official_announcement_url','official_identity_state','github_runner_access_state',
    'official_pdf_body_state','official_pdf_sha256','official_pdf_byte_size','repository_binary_vendored',
    'notebook_ingest_state','historical_source_state','notes'
]
results_rows = [{
    'source_id': SOURCE_ID,
    'current_title': TITLE,
    'policy_period': '2026-2030',
    'issuing_authority': AUTHORITY,
    'authority_class': 'OFFICIAL_GUIDANCE',
    'binding_state': 'NONBINDING_POLICY_NOT_STATUTE',
    'official_strategy_page': OFFICIAL_PAGE,
    'official_announcement_url': OFFICIAL_ANNOUNCEMENT,
    'official_identity_state': 'CURRENT_OFFICIAL_ACTION_PLAN_IDENTITY_VERIFIED_2026_2030',
    'github_runner_access_state': 'MINISTRY_ENDPOINTS_RETURNED_GENERIC_HTML_SHELL_FOR_DIRECT_CURL',
    'official_pdf_body_state': 'UNRESOLVED_NOT_ACQUIRED',
    'official_pdf_sha256': '',
    'official_pdf_byte_size': '',
    'repository_binary_vendored': 'NO',
    'notebook_ingest_state': 'NOT_RUN',
    'historical_source_state': '2021-2025_STRATEGY_AND_2024-2025_ACTION_PLAN_HISTORICAL_CONTEXT_NOT_CURRENT_PRIMARY',
    'notes': 'Do not infer absence of a PDF from runner access failure. Do not infer binding duties from policy publication. Exact PDF URL/hash remain UNKNOWN until a binary-readable official-source channel resolves them.'
}]
write_csv(results_path, results_fields, results_rows)


# 5) Download/upload list: append current policy routing if not already recorded.
download_list_path = '86_NOTEBOOKLM/NOTEBOOKLM_DOWNLOAD_AND_UPLOAD_LIST.md'
text = read_text(download_list_path)
marker = '## R033 — TR-009 current Türkiye AI policy source'
section = f'''\n\n{marker}\n\n- `TR-009` — **Türkiye Yapay Zekâ Eylem Planı (2026-2030)**  \n  Official strategy-document index: {OFFICIAL_PAGE}  \n  Official release announcement (13 June 2026): {OFFICIAL_ANNOUNCEMENT}  \n  **Authority:** `OFFICIAL_GUIDANCE` / national policy-action plan.  \n  **Binding state:** nonbinding policy source; **not statute**.  \n  **Ingest:** `URL_DIRECT_PREFERRED`.  \n  **R033 binary state:** exact official PDF body was not exposed to the GitHub runner; SHA-256/byte size remain `UNKNOWN`; no repository binary was vendored.  \n  **Historical boundary:** 2021-2025 strategy and 2024-2025 action-plan sources remain historical context and must not replace the current 2026-2030 plan.\n'''
if marker not in text:
    text = text.rstrip() + section + '\n'
write_text(download_list_path, text)


# 6) Current context: register completion and fail-closed source state.
context_path = '00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md'
text = read_text(context_path)
old_state = 'R032_NB01_RESIDUAL_OFFICIAL_SOURCE_VALIDATION_COMPLETE / LEGAL_RESEARCH_ACTIVE'
new_state = 'R032_NB01_RESIDUAL_OFFICIAL_SOURCE_VALIDATION_COMPLETE / R033_TR009_CURRENT_POLICY_SOURCE_VALIDATION_COMPLETE / LEGAL_RESEARCH_ACTIVE'
if old_state in text:
    text = text.replace(old_state, new_state, 1)
elif 'R033_TR009_CURRENT_POLICY_SOURCE_VALIDATION_COMPLETE' not in text:
    raise SystemExit('current-context state marker drift')

if 'AI-LAWS-R033 = COMPLETE_SUPPORT_SOURCE_VALIDATION' not in text:
    anchor = 'AI-LAWS-R032 = COMPLETE_SUPPORT_SOURCE_VALIDATION\n```'
    if anchor not in text:
        raise SystemExit('current-context completed-unit marker drift')
    text = text.replace(anchor, 'AI-LAWS-R032 = COMPLETE_SUPPORT_SOURCE_VALIDATION\nAI-LAWS-R033 = COMPLETE_SUPPORT_SOURCE_VALIDATION\n```', 1)

r033_section = f'''\n\n### R033 — TR-009 current Türkiye AI policy source\n\nR033 resolved the current national AI-policy identity without converting policy into binding law.\n\n```text\nTR009_CURRENT_POLICY_TITLE = Türkiye Yapay Zekâ Eylem Planı\nTR009_CURRENT_POLICY_PERIOD = 2026-2030\nTR009_ISSUING_AUTHORITY = T.C. Sanayi ve Teknoloji Bakanlığı\nTR009_AUTHORITY_CLASS = OFFICIAL_GUIDANCE\nTR009_BINDING_LAW = NO\nTR009_OFFICIAL_STRATEGY_PAGE = {OFFICIAL_PAGE}\nTR009_OFFICIAL_RELEASE_ANNOUNCEMENT = 2026-06-13\nTR009_OFFICIAL_PDF_BODY_ACQUIRED = NO\nTR009_OFFICIAL_PDF_SHA256 = UNKNOWN\nTR009_REPOSITORY_BINARY_VENDORED = NO\nTR009_NOTEBOOK_UPLOADS = 0\n```\n\nThe Ministry's current strategy-document layer identifies the 2026-2030 action plan, and its 13 June 2026 announcement confirms release. The earlier 2021-2025 strategy and 2024-2025 action-plan materials are historical context. Direct GitHub-runner requests returned a generic HTML shell rather than the downloadable PDF body, so R033 records no PDF hash, byte size or exact-binary claim.\n\n```text\nOFFICIAL_POLICY_IDENTITY_VERIFIED != PDF_BINARY_VERIFIED\nOFFICIAL_POLICY_GUIDANCE != STATUTE\nRUNNER_ACCESS_FAILURE != SOURCE_ABSENCE\n```\n'''
if '### R033 — TR-009 current Türkiye AI policy source' not in text:
    anchor = 'No new UN/UNESCO binary was committed. Exact official URLs and verification metadata were recorded instead.\n'
    if anchor not in text:
        raise SystemExit('R032 section anchor drift')
    text = text.replace(anchor, anchor + r033_section, 1)

nb04_block = '''NB04_REPOSITORY_PDF_UPLOAD_SET = ELIGIBLE_AS_VERIFIED_SNAPSHOTS_WITH_DATE_STATE_LABELS\nNB04_OFFICIAL_LIVE_MEVZUAT_EXACT_BYTE_RECHECK = BLOCKED\nPRIMARY_SOURCE_RECHECK_REQUIRED_BEFORE_MATERIAL_LEGAL_CLAIM = YES'''
nb04_new = nb04_block + '''\nTR009_CURRENT_POLICY_IDENTITY = VERIFIED_2026_2030\nTR009_CURRENT_POLICY_CLASS = OFFICIAL_GUIDANCE_NONBINDING\nTR009_OFFICIAL_PDF_BODY_STATE = UNRESOLVED\nTR009_NOTEBOOK_UPLOADS = 0'''
if nb04_block in text and 'TR009_CURRENT_POLICY_IDENTITY = VERIFIED_2026_2030' not in text:
    text = text.replace(nb04_block, nb04_new, 1)

lane_anchor = '`TR-001` through `TR-008` now have verified repository-snapshot content identity. `TR-008` is confirmed to include Law No. 7590 effects. The remaining gate is live official Mevzuat currentness/exact-byte recheck before material legal conclusions; `TR-007` also requires date-aware handling of provisions recorded with future `2026-11-01` effect.'
lane_new = lane_anchor + ' R033 additionally pins `TR-009` to the current **Türkiye Yapay Zekâ Eylem Planı (2026-2030)** as nonbinding `OFFICIAL_GUIDANCE`; exact PDF binary identity remains unresolved and is not required to treat the stable official Ministry URL as the current policy pointer.'
if lane_anchor in text and 'R033 additionally pins `TR-009`' not in text:
    text = text.replace(lane_anchor, lane_new, 1)

integrity_anchor = 'R032_NEW_THIRD_PARTY_BINARIES_VENDORED = 0'
integrity_add = integrity_anchor + '''\nR033_TR009_CURRENT_POLICY_IDENTITY = VERIFIED_2026_2030\nR033_TR009_BINDING_LAW = NO\nR033_TR009_OFFICIAL_PDF_BODY_ACQUIRED = NO\nR033_TR009_OFFICIAL_PDF_SHA256 = UNKNOWN\nR033_TR009_REPOSITORY_BINARY_VENDORED = 0'''
if integrity_anchor in text and 'R033_TR009_CURRENT_POLICY_IDENTITY = VERIFIED_2026_2030' not in text:
    text = text.replace(integrity_anchor, integrity_add, 1)
write_text(context_path, text)


# 7) Research queue: one completed support-source-validation row.
queue_path = '90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv'
fields, rows = read_csv(queue_path)
if not any(x.get('work_item_id') == 'AI-LAWS-R033' for x in rows):
    rows.append({
        'work_item_id': 'AI-LAWS-R033',
        'priority': 'P0',
        'workstream': 'Türkiye current AI policy source validation',
        'scope': 'Resolve TR-009 current official national AI strategy/action-plan identity and preserve policy-vs-law boundary without inventing unavailable PDF binary metadata',
        'state': 'COMPLETE_SUPPORT_SOURCE_VALIDATION',
        'dependencies': 'R026 COMPLETE + TR-009 manifest candidate',
        'expected_output': 'TR009 current-policy results; updated manifest/ledger/pack routing/current context; R033 closeout',
        'stop_condition': 'current 2026-2030 official policy identity pinned; exact PDF body unresolved preserved; no Notebook upload or substantive R005 legal analysis auto-started',
    })
write_csv(queue_path, fields, rows)


# 8) Closeout.
closeout_path = '86_NOTEBOOKLM/acquisition_runs/AI-LAWS-R033_TR009_CURRENT_POLICY_SOURCE_CLOSEOUT_2026-09-14.md'
closeout = f'''# AI-LAWS — R033 / TR-009 Current Türkiye AI Policy Source Closeout\n\n**UNIT_ID:** `AI-LAWS-R033 / {BATCH}`  \n**DATE:** {DATE}  \n**SCOPE:** current official source identity for `TR-009` only  \n**EXECUTION_CHANNEL:** GitHub / GitHub Actions for repository operations  \n**ZIP_OR_ARTIFACT_CREATED:** NO  \n**AUTO_ADVANCE:** NO\n\n## Result\n\nThe current national AI-policy source is pinned as:\n\n```text\nSOURCE_ID = TR-009\nTITLE = Türkiye Yapay Zekâ Eylem Planı (2026-2030)\nISSUING_AUTHORITY = T.C. Sanayi ve Teknoloji Bakanlığı\nAUTHORITY_CLASS = OFFICIAL_GUIDANCE\nBINDING_STATE = NONBINDING_POLICY_NOT_STATUTE\nOFFICIAL_STRATEGY_PAGE = {OFFICIAL_PAGE}\nOFFICIAL_ANNOUNCEMENT = {OFFICIAL_ANNOUNCEMENT}\nOFFICIAL_RELEASE_ANNOUNCEMENT_DATE = 2026-06-13\nPOLICY_PERIOD = 2026-2030\n```\n\nThe current official Ministry layer identifies the 2026-2030 action plan. Earlier 2021-2025 strategy and 2024-2025 action-plan material remains historical context and is not the current primary policy pointer.\n\n## Binary/PDF boundary\n\nGitHub-runner direct requests to Ministry endpoints returned a small generic HTML shell rather than the substantive strategy page/PDF response that a normal indexed browser surface exposes. Guessed PDF paths were rejected as evidence. Therefore:\n\n```text\nOFFICIAL_POLICY_IDENTITY_VERIFIED = YES\nEXACT_OFFICIAL_PDF_URL_VERIFIED_BY_GITHUB_RUNNER = NO\nOFFICIAL_PDF_BODY_ACQUIRED = NO\nOFFICIAL_PDF_SHA256 = UNKNOWN\nOFFICIAL_PDF_BYTE_SIZE = UNKNOWN\nREPOSITORY_BINARY_VENDORED = NO\nPDF_CONTENT_IDENTITY_VERIFIED = NO\n```\n\nThis is fail-closed: inability of the runner to obtain the binary is an access/execution limitation, not evidence that the official plan does not exist.\n\n## Authority firewall\n\n```text\nOFFICIAL_POLICY_GUIDANCE != STATUTE\nPOLICY_ACTION != LEGAL_DUTY_WITHOUT_SEPARATE_BINDING_AUTHORITY\nOFFICIAL_PAGE_IDENTITY_VERIFIED != PDF_BINARY_VERIFIED\nRUNNER_ACCESS_FAILURE != SOURCE_ABSENCE\nCURRENT_POLICY_POINTER != CURRENT_CONSOLIDATED_LAW\n```\n\n## Operations\n\n```text\nNOTEBOOK_UPLOADS = 0\nDERIVED_MARKDOWN_CREATED = 0\nNEW_THIRD_PARTY_BINARY_VENDORED = 0\nLEGAL_CONCLUSION = NOT_ATTEMPTED\nR005_SUBSTANTIVE_RESEARCH_STARTED = NO\nUNKNOWN_PRESERVED = YES\nAUTO_ADVANCE = NO\n```\n'''
write_text(closeout_path, closeout)


# Assertions.
fields, rows = read_csv(manifest_path)
r = exactly_one(rows, 'source_id', SOURCE_ID)
assert r['title'] == TITLE
assert '2026_2030' in r['verification_state']
assert r['authority_class'] == 'OFFICIAL_GUIDANCE'
assert 'not statute' in r['binding_state']
fields, rows = read_csv(queue_path)
assert sum(x.get('work_item_id') == 'AI-LAWS-R033' for x in rows) == 1
fields, rows = read_csv(ledger_path)
assert sum(x.get('batch_id') == BATCH and x.get('source_id') == SOURCE_ID for x in rows) == 1
assert Path(results_path).exists()
assert Path(closeout_path).exists()

print('R033_PERSIST_ASSERTIONS=PASS')
print('TR009_CURRENT_POLICY_IDENTITY=VERIFIED_2026_2030')
print('TR009_AUTHORITY_CLASS=OFFICIAL_GUIDANCE')
print('TR009_BINDING_LAW=NO')
print('TR009_OFFICIAL_PDF_BODY_ACQUIRED=NO')
print('TR009_OFFICIAL_PDF_SHA256=UNKNOWN')
print('TR009_REPOSITORY_BINARY_VENDORED=NO')
print('NOTEBOOK_UPLOADS=0')
print('ZIP_OR_ARTIFACT_CREATED=NO')
print('AUTO_ADVANCE=NO')
