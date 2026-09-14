import csv, hashlib, json, re, subprocess, urllib.request
from pathlib import Path

ROOT = Path('.')
D = ROOT / '86_NOTEBOOKLM' / 'downloads'
TODAY = '2026-09-14'
BATCH = 'NB-BATCH-NB03-20260914-003'
US001 = 'US-001'
US005 = 'US-005'
US001_WH = 'https://www.whitehouse.gov/presidential-actions/2025/01/removing-barriers-to-american-leadership-in-artificial-intelligence/'
US005_WH = 'https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/'
US005_FR_HTML = 'https://www.federalregister.gov/documents/2025/12/16/2025-23092/ensuring-a-national-policy-framework-for-artificial-intelligence'
US005_PDF = 'https://www.govinfo.gov/content/pkg/FR-2025-12-16/pdf/2025-23092.pdf'
EXPECTED_US005_SHA = '5a557f9a153f1f40c7bd885b660ed81f1b26d55a6363b778943dfaa65565e0cb'
EXPECTED_US005_BYTES = 204973


def sh(cmd):
    return subprocess.check_output(cmd, text=True, errors='replace').strip()


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def read_csv(path):
    with path.open(newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def write_csv(path, fields, rows):
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


def fetch(url, binary=True):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 AI-LAWS source verification'})
    last = None
    for _ in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                b = r.read()
                if not b:
                    raise RuntimeError('empty response')
                return r.status, r.headers.get_content_type(), r.geturl(), b
        except Exception as e:
            last = e
    raise RuntimeError(f'fetch failed for {url}: {last}')

# Fail-closed drift check before writing.
sh(['git', 'fetch', 'origin', 'main'])
head = sh(['git', 'rev-parse', 'HEAD'])
origin = sh(['git', 'rev-parse', 'origin/main'])
assert head == origin, (head, origin)
base_head = head

reg_fields, reg_rows = read_csv(D / 'DOWNLOADS_REGISTRY.csv')
reg = {r['manifest_source_id']: r for r in reg_rows if r['manifest_source_id'] in {US001, US005}}
assert set(reg) == {US001, US005}

res_path = D / 'NB03_CONTENT_IDENTITY_RESULTS.csv'
res_fields, res_rows = read_csv(res_path)
res = {r['source_id']: r for r in res_rows if r['source_id'] in {US001, US005}}
assert set(res) == {US001, US005}

# Re-verify repository files.
repo001_path = D / reg[US001]['repo_filename']
repo005_path = D / reg[US005]['repo_filename']
repo001 = repo001_path.read_bytes()
repo005 = repo005_path.read_bytes()
repo001_sha = sha256(repo001)
repo005_sha = sha256(repo005)
assert repo001_sha == '53b1d268c02cddb9eaaf57cf7429c7151cca56c454f9d36126699350c3b9a6ef'
assert repo005_sha == EXPECTED_US005_SHA
assert len(repo005) == EXPECTED_US005_BYTES

# Recheck live White House pages for identity/accessibility only.
status1, mime1, final1, wh001 = fetch(US001_WH)
status5, mime5, final5, wh005 = fetch(US005_WH)
assert status1 == 200 and status5 == 200
v1 = ' '.join(re.sub(r'<[^>]+>', ' ', wh001.decode('utf-8', 'replace')).split())
v5 = ' '.join(re.sub(r'<[^>]+>', ' ', wh005.decode('utf-8', 'replace')).split())
assert 'Removing Barriers to American Leadership in Artificial Intelligence' in v1
assert 'National Artificial Intelligence Policy' in v5 or 'National Policy Framework for Artificial Intelligence' in v5

# Resolve and re-verify the official Federal Register/GovInfo PDF.
status_pdf, mime_pdf, final_pdf, official005 = fetch(US005_PDF)
official005_sha = sha256(official005)
assert status_pdf == 200
assert mime_pdf == 'application/pdf'
assert len(official005) == EXPECTED_US005_BYTES
assert official005_sha == EXPECTED_US005_SHA
assert official005 == repo005

# Federal Register HTML identity.
status_fr, mime_fr, final_fr, fr_html = fetch(US005_FR_HTML)
assert status_fr == 200
fr_visible = ' '.join(re.sub(r'<[^>]+>', ' ', fr_html.decode('utf-8', 'replace')).split())
assert 'Ensuring a National Policy Framework for Artificial Intelligence' in fr_visible
assert '2025-23092' in fr_html.decode('utf-8', 'replace') or '2025-23092' in final_fr

# Update registry while preserving US-001 as intentionally partial/supporting.
r1 = reg[US001]
r1['binary_variant'] = 'WHITE_HOUSE_WEBPAGE_PRINT_SNAPSHOT'
r1['content_identity_state'] = 'CONTENT_IDENTITY_PARTIAL'
r1['currentness_state'] = 'WHITE_HOUSE_OFFICIAL_PAGE_RECHECKED_2026-09-14; REPOSITORY_WEBPAGE_PRINT_SNAPSHOT_2026-09-14; LIVE_URL_PREFERRED'
r1['notebook_ingest_mode'] = 'OFFICIAL_URL_PREFERRED; REPOSITORY_WEBPAGE_PRINT_SUPPORTING_ONLY'
r1['action'] = f'R031 recheck: repository SHA256 {repo001_sha}; 2-page native-searchable White House webpage-print snapshot; live White House HTML returned HTTP 200 and title identity matched on {TODAY}. Exact-byte comparison is NOT_APPLICABLE because the official source is HTML. Preserve CONTENT_IDENTITY_PARTIAL / SUPPORTING_ONLY.'

r5 = reg[US005]
r5['binary_variant'] = 'OFFICIAL_GOVINFO_FEDERAL_REGISTER_PDF_EXACT_MATCH'
r5['content_identity_state'] = 'CONTENT_IDENTITY_VERIFIED'
r5['currentness_state'] = 'EO_14365_IDENTITY_VERIFIED; FEDERAL_REGISTER_DOC_2025-23092_EXACT_BYTE_MATCH_2026-09-14; WHITE_HOUSE_OFFICIAL_PAGE_RECHECKED_2026-09-14'
r5['notebook_ingest_mode'] = 'VERIFIED_OFFICIAL_PDF_ELIGIBLE; LIVE_WHITE_HOUSE_RECHECK_REQUIRED_FOR_CURRENT_STATUS'
r5['action'] = f'R031 GitHub validation: SHA256 {repo005_sha}; 3 pages; native searchable text; exact byte match to official GovInfo Federal Register PDF {US005_PDF} (document 2025-23092) on {TODAY}. White House official page also returned HTTP 200. Exact snapshot identity does not itself prove continuing legal effect.'
write_csv(D / 'DOWNLOADS_REGISTRY.csv', reg_fields, reg_rows)

# Reconcile NB03 results.
e1 = res[US001]
e1['official_source_recheck'] = 'RECHECKED_2026-09-14_WHITE_HOUSE_HTML'
e1['official_exact_byte_match'] = 'NOT_APPLICABLE_HTML_SOURCE'
e1['currentness_state'] = r1['currentness_state']
e1['notebook_upload_eligibility'] = r1['notebook_ingest_mode']
e1['notes'] = 'R031 confirms the repository file is a 2-page native-searchable White House webpage-print snapshot and the live White House HTML identity remains accessible. Different representations make exact-byte comparison inapplicable; keep CONTENT_IDENTITY_PARTIAL / SUPPORTING_ONLY and use the official URL for primary/current-status research.'

e5 = res[US005]
e5['binary_variant'] = r5['binary_variant']
e5['content_identity_state'] = 'CONTENT_IDENTITY_VERIFIED'
e5['official_source_recheck'] = 'RECHECKED_2026-09-14_FEDERAL_REGISTER_GOVINFO_AND_WHITE_HOUSE'
e5['official_exact_byte_match'] = 'YES'
e5['currentness_state'] = r5['currentness_state']
e5['notebook_upload_eligibility'] = r5['notebook_ingest_mode']
e5['notes'] = f'R031 resolved Federal Register document 2025-23092. Repository PDF exactly matches official GovInfo bytes: {EXPECTED_US005_BYTES} bytes; SHA-256 {EXPECTED_US005_SHA}. White House official page also rechecked. Snapshot identity does not establish continuing legal effect or resolve federal-state legal questions.'
write_csv(res_path, res_fields, res_rows)

# Create compact residual-results matrix.
rr_fields = ['source_id','residual_question','resolution_state','official_primary_url','official_pdf_url','repo_sha256','official_sha256','official_exact_byte_match','content_identity_state','notebook_use','notes']
rr_rows = [
    {
        'source_id': US001,
        'residual_question': 'Can the repository webpage-print PDF be promoted to exact-official-PDF identity?',
        'resolution_state': 'RESOLVED_AS_REPRESENTATION_MISMATCH_NOT_A_BINARY_BLOCKER',
        'official_primary_url': US001_WH,
        'official_pdf_url': '',
        'repo_sha256': repo001_sha,
        'official_sha256': '',
        'official_exact_byte_match': 'NOT_APPLICABLE_HTML_SOURCE',
        'content_identity_state': 'CONTENT_IDENTITY_PARTIAL',
        'notebook_use': 'OFFICIAL_URL_PRIMARY; REPOSITORY_PRINT_SUPPORTING_ONLY',
        'notes': 'Live White House HTML identity rechecked. The PDF is a print/export snapshot rather than an official binary publication; do not force exact-byte equivalence across representations.'
    },
    {
        'source_id': US005,
        'residual_question': 'Does the repository Federal Register snapshot exactly match the official Federal Register/GovInfo PDF?',
        'resolution_state': 'RESOLVED_EXACT_OFFICIAL_BYTE_MATCH',
        'official_primary_url': US005_WH,
        'official_pdf_url': US005_PDF,
        'repo_sha256': repo005_sha,
        'official_sha256': official005_sha,
        'official_exact_byte_match': 'YES',
        'content_identity_state': 'CONTENT_IDENTITY_VERIFIED',
        'notebook_use': 'VERIFIED_OFFICIAL_PDF_ELIGIBLE; LIVE_WHITE_HOUSE_RECHECK_REQUIRED_FOR_CURRENT_STATUS',
        'notes': 'Federal Register document 2025-23092; publication date 2025-12-16; exact official GovInfo PDF bytes verified.'
    }
]
write_csv(D / 'NB03_RESIDUAL_VERIFICATION_RESULTS.csv', rr_fields, rr_rows)

# Append controlled ledger rows without rewriting R028 history.
ledger_path = ROOT / '86_NOTEBOOKLM' / 'NOTEBOOKLM_ACQUISITION_AND_VALIDATION_LEDGER.csv'
lf, lr = read_csv(ledger_path)
lr = [r for r in lr if r.get('batch_id') != BATCH]
for sid in (US001, US005):
    row = {k: '' for k in lf}
    if sid == US001:
        row.update({
            'batch_id': BATCH, 'source_id': sid, 'notebook_pack': 'NB03', 'jurisdiction': 'US',
            'title': 'Removing Barriers to American Leadership in Artificial Intelligence', 'document_id': 'Executive Order 14179',
            'issuing_authority': 'The White House', 'authority_class': 'STATUTE_OR_REGULATION',
            'binding_state': 'executive order / federal executive policy; legal effect requires claim-specific current-law recheck',
            'official_url': US001_WH, 'retrieval_date': TODAY,
            'version_state': 'OFFICIAL_WHITE_HOUSE_HTML_IDENTITY_RECHECKED; REPOSITORY_PRINT_SNAPSHOT_SUPPORTING_ONLY',
            'authentic_language': 'English official White House text', 'translation_state': 'NOT_APPLICABLE',
            'rights_state': 'OFFICIAL_PUBLIC_URL', 'acquisition_method': 'REPOSITORY_WEBPAGE_PRINT_SUPPORTING_SNAPSHOT',
            'local_filename_or_url': str(repo001_path), 'sha256': repo001_sha, 'byte_size': str(len(repo001)), 'content_type': 'application/pdf',
            'content_identity_checked': 'CONTENT_IDENTITY_PARTIAL_REPRESENTATION_MISMATCH',
            'notebook_ingest_state': 'NOT_RUN', 'notebook_locator_test': 'NOT_RUN',
            'primary_source_recheck_state': 'WHITE_HOUSE_HTML_IDENTITY_RECHECKED_2026-09-14',
            'refresh_trigger': 'White House page replacement/revocation/supersession or material current-law analysis',
            'human_review_required': 'YES_BEFORE_MATERIAL_LEGAL_CONCLUSION',
            'notes': 'R031 preserves the repository PDF as a supporting webpage-print snapshot. Exact-byte comparison is not applicable because the official source is HTML. No legal-effect conclusion attempted.'
        })
    else:
        row.update({
            'batch_id': BATCH, 'source_id': sid, 'notebook_pack': 'NB03', 'jurisdiction': 'US',
            'title': 'Ensuring a National Policy Framework for Artificial Intelligence', 'document_id': 'Executive Order 14365 / Federal Register document 2025-23092',
            'issuing_authority': 'The White House / Office of the Federal Register / GovInfo', 'authority_class': 'STATUTE_OR_REGULATION',
            'binding_state': 'executive order / federal executive policy; continuing legal effect requires claim-specific current-law recheck',
            'official_url': US005_WH, 'retrieval_date': TODAY,
            'version_state': 'FEDERAL_REGISTER_DOCUMENT_2025-23092_EXACT_OFFICIAL_BYTE_MATCH; WHITE_HOUSE_PAGE_RECHECKED',
            'publication_date': '2025-12-16', 'adoption_date': '2025-12-11',
            'authentic_language': 'English official Federal Register/White House text', 'translation_state': 'NOT_APPLICABLE',
            'rights_state': 'OFFICIAL_PUBLIC_US_GOVERNMENT_SOURCE', 'acquisition_method': 'REPOSITORY_PDF_VALIDATED_AGAINST_OFFICIAL_GOVINFO_PDF',
            'local_filename_or_url': str(repo005_path), 'sha256': repo005_sha, 'byte_size': str(len(repo005)), 'content_type': 'application/pdf',
            'content_identity_checked': 'CONTENT_IDENTITY_VERIFIED_EXACT_OFFICIAL_BYTE_MATCH',
            'notebook_ingest_state': 'NOT_RUN', 'notebook_locator_test': 'NOT_RUN',
            'primary_source_recheck_state': 'FEDERAL_REGISTER_GOVINFO_EXACT_BYTE_MATCH_2026-09-14',
            'refresh_trigger': 'White House/Federal Register legal-status change, revocation/supersession, or material current-law analysis',
            'human_review_required': 'YES_BEFORE_MATERIAL_LEGAL_CONCLUSION',
            'notes': f'R031 GitHub-only recheck: official GovInfo PDF {US005_PDF} exactly matches repository bytes; SHA-256 {repo005_sha}; {len(repo005)} bytes. Exact snapshot identity does not itself prove continuing legal effect.'
        })
    lr.append(row)
write_csv(ledger_path, lf, lr)

# Replace NB03 upload-plan section with reconciled state.
plan_path = D / 'NOTEBOOK_UPLOAD_PLAN.md'
plan = plan_path.read_text(encoding='utf-8')
new_nb03 = '''## NB03 — United States\n\nR028 inspected all eight core `US-001..US-008` repository PDFs. R031 then closed the residual binary/source-routing question for `US-001` and `US-005` without starting substantive R007 research. No ZIP/artifact, derived Markdown or Notebook upload was created.\n\n```text\nNB03_CORE_REPOSITORY_PDFS_INSPECTED = 8 / 8\nNB03_NATIVE_SEARCHABLE_TEXT_LAYER = 8 / 8\nNB03_CONTENT_IDENTITY_VERIFIED = 7 / 8\nNB03_CONTENT_IDENTITY_PARTIAL = 1 / 8   # US-001 webpage-print representation\nNB03_OFFICIAL_EXACT_BYTE_MATCH = 7 / 8  # US-002/003/004/005/006/007/008\nNB03_DERIVED_MARKDOWN_REQUIRED = 0\nNB03_NOTEBOOK_UPLOADS = 0\n```\n\nR031 residual resolution:\n\n- `US-001` remains a verified White House **webpage-print snapshot** and `CONTENT_IDENTITY_PARTIAL / SUPPORTING_ONLY`. This is intentional: the official source is HTML, so byte equality with a printed PDF is not a meaningful authenticity test. Use the live White House URL as the primary source.\n- `US-005` is Federal Register document `2025-23092`, published `2025-12-16`. The repository PDF is an exact byte match to the official GovInfo PDF, SHA-256 `5a557f9a153f1f40c7bd885b660ed81f1b26d55a6363b778943dfaa65565e0cb`, 204,973 bytes. It is eligible as a verified official PDF snapshot.\n\nExisting exact matches also remain: `US-002`, `US-003`, `US-004`, `US-006`, `US-007`, `US-008`.\n\nDo not label executive orders or OMB memoranda as Acts of Congress. NIST sources are voluntary/nonbinding frameworks/profiles. A live White House page or exact Federal Register PDF snapshot does not, by itself, prove continuing legal effect, non-revocation, preemption, or the validity of any federal-state legal theory.\n\n```text\nEXACT_OFFICIAL_PDF_BYTES != PERMANENT_CURRENTNESS\nWEBPAGE_PRINT_SNAPSHOT != LIVE_OFFICIAL_PAGE\nEXECUTIVE_ORDER != ACT_OF_CONGRESS\nSOURCE_IDENTITY_VERIFIED != LEGAL_EFFECT_CONCLUSION\n```\n\n'''
plan2 = re.sub(r'## NB03 — United States\n.*?(?=## NB04 — Türkiye\n)', new_nb03, plan, flags=re.S)
assert plan2 != plan
plan_path.write_text(plan2, encoding='utf-8')

# Add R031 note to master download/upload list.
list_path = ROOT / '86_NOTEBOOKLM' / 'NOTEBOOKLM_DOWNLOAD_AND_UPLOAD_LIST.md'
text = list_path.read_text(encoding='utf-8')
marker = '### R031 NB03 residual verification state'
if marker not in text:
    m = re.search(r'(## D\. NB03.*?)(?=\n## E\.)', text, flags=re.S)
    if not m:
        m = re.search(r'(## .*NB03.*?)(?=\n## .*NB04)', text, flags=re.S)
    assert m, 'NB03 section not found in download/upload list'
    addition = '''\n\n### R031 NB03 residual verification state\n\n`US-005` is now an exact byte match to official GovInfo Federal Register document `2025-23092` (SHA-256 `5a557f9a153f1f40c7bd885b660ed81f1b26d55a6363b778943dfaa65565e0cb`). `US-001` remains a White House HTML print snapshot and supporting-only by design; exact-byte comparison is not applicable across HTML/PDF representations. NB03 official exact-byte count is therefore `7/8`, with the eighth source represented by a live official HTML URL plus supporting print snapshot. No Notebook upload was performed by R031.\n'''
    text = text[:m.end(1)] + addition + text[m.end(1):]
    list_path.write_text(text, encoding='utf-8')

# Research queue append.
qpath = ROOT / '90_RESEARCH_QUEUE' / 'INITIAL_RESEARCH_QUEUE.csv'
qf, qr = read_csv(qpath)
qr = [r for r in qr if r.get('work_item_id') != 'AI-LAWS-R031']
row = {k: '' for k in qf}
row.update({
    'work_item_id': 'AI-LAWS-R031', 'priority': 'P0', 'workstream': 'Notebook NB03 residual source validation',
    'scope': 'Resolve residual US-001 webpage-print representation state and US-005 Federal Register exact-byte identity without starting substantive US legal inventory',
    'state': 'COMPLETE_SUPPORT_SOURCE_VALIDATION', 'dependencies': 'R028 COMPLETE',
    'expected_output': '86_NOTEBOOKLM/downloads/NB03_RESIDUAL_VERIFICATION_RESULTS.csv; updated NB03 results/registry/ledger/upload plan/download list; R031 closeout',
    'stop_condition': 'US-005 exact official GovInfo byte match recorded; US-001 intentionally remains supporting-only HTML print snapshot; no Notebook upload or R007 auto-started'
})
qr.append(row)
write_csv(qpath, qf, qr)

# Current context reconciliation.
cpath = ROOT / '00_CONTROL' / 'CURRENT_CONTEXT_AND_NEXT_ACTION.md'
c = cpath.read_text(encoding='utf-8')
old_state = 'R030_NB02_REPOSITORY_PDF_VALIDATION_COMPLETE / LEGAL_RESEARCH_ACTIVE'
if 'R031_NB03_RESIDUAL_SOURCE_VALIDATION_COMPLETE' not in c.split('\n', 8)[5]:
    assert old_state in c
    c = c.replace(old_state, 'R030_NB02_REPOSITORY_PDF_VALIDATION_COMPLETE / R031_NB03_RESIDUAL_SOURCE_VALIDATION_COMPLETE / LEGAL_RESEARCH_ACTIVE', 1)
if 'AI-LAWS-R031 = COMPLETE_SUPPORT_SOURCE_VALIDATION' not in c:
    c = c.replace('AI-LAWS-R030 = COMPLETE_SUPPORT_SOURCE_VALIDATION\n```', 'AI-LAWS-R030 = COMPLETE_SUPPORT_SOURCE_VALIDATION\nAI-LAWS-R031 = COMPLETE_SUPPORT_SOURCE_VALIDATION\n```', 1)

# Update the NB03 ingest-state block.
old_block = '''NB03_CORE_PDF_CONTENT_IDENTITY_VERIFIED = 7 / 8\nNB03_US001_CONTENT_IDENTITY = PARTIAL_WEBPAGE_PRINT_SUPPORTING_ONLY\nNB03_OFFICIAL_EXACT_BYTE_MATCH = 6 / 8\nNB03_US005_VARIANT = VERIFIED_FEDERAL_REGISTER_PDF_SNAPSHOT_EXACT_BYTE_NOT_RUN\nNB03_NATIVE_TEXT_LAYER = 8 / 8\nNB03_DERIVED_MARKDOWN_REQUIRED = 0\nNB03_NOTEBOOK_UPLOADS = 0'''
new_block = '''NB03_CORE_PDF_CONTENT_IDENTITY_VERIFIED = 7 / 8\nNB03_US001_CONTENT_IDENTITY = PARTIAL_WEBPAGE_PRINT_SUPPORTING_ONLY\nNB03_OFFICIAL_EXACT_BYTE_MATCH = 7 / 8\nNB03_US005_VARIANT = OFFICIAL_GOVINFO_FEDERAL_REGISTER_PDF_EXACT_MATCH\nNB03_US005_FEDERAL_REGISTER_DOCUMENT = 2025-23092\nNB03_NATIVE_TEXT_LAYER = 8 / 8\nNB03_DERIVED_MARKDOWN_REQUIRED = 0\nNB03_NOTEBOOK_UPLOADS = 0'''
assert old_block in c
c = c.replace(old_block, new_block, 1)

if '### R031 — NB03 residual source validation' not in c:
    anchor = '### R029 — NB08 repository incident-source validation\n'
    sec = '''### R031 — NB03 residual source validation\n\nR031 rechecked the two remaining NB03 residual source questions entirely through GitHub.\n\n```text\nUS001_LIVE_WHITE_HOUSE_HTML_IDENTITY = RECHECKED\nUS001_REPOSITORY_VARIANT = WEBPAGE_PRINT_SNAPSHOT_SUPPORTING_ONLY\nUS001_EXACT_BYTE_MATCH = NOT_APPLICABLE_HTML_SOURCE\nUS005_FEDERAL_REGISTER_DOCUMENT = 2025-23092\nUS005_OFFICIAL_GOVINFO_EXACT_BYTE_MATCH = YES\nUS005_SHA256 = 5a557f9a153f1f40c7bd885b660ed81f1b26d55a6363b778943dfaa65565e0cb\nNB03_OFFICIAL_EXACT_BYTE_MATCH = 7 / 8\nNB03_NOTEBOOK_UPLOADS = 0\n```\n\n`US-001` intentionally remains `CONTENT_IDENTITY_PARTIAL / SUPPORTING_ONLY` because its repository file is a print/export of an official HTML page, not an official binary publication. `US-005` is now verified as exact official GovInfo Federal Register bytes. Neither result constitutes a substantive determination of current legal effect.\n\nDurable output: `86_NOTEBOOKLM/downloads/NB03_RESIDUAL_VERIFICATION_RESULTS.csv` plus registry/results/ledger/upload-plan/download-list/queue reconciliation.\n\n'''
    assert anchor in c
    c = c.replace(anchor, sec + anchor, 1)

# Add integrity counters if absent.
needle = 'R030_NB02_NATIVE_TEXT_LAYER_VERIFIED = 10\n'
extra = 'R031_NB03_US005_OFFICIAL_GOVINFO_EXACT_BYTE_MATCH = YES\nR031_NB03_OFFICIAL_EXACT_BYTE_MATCH_TOTAL = 7\nR031_NB03_US001_SUPPORTING_PRINT_STATE_PRESERVED = YES\n'
if 'R031_NB03_US005_OFFICIAL_GOVINFO_EXACT_BYTE_MATCH = YES' not in c:
    assert needle in c
    c = c.replace(needle, needle + extra, 1)

cpath.write_text(c, encoding='utf-8')

# Closeout.
close_path = ROOT / '86_NOTEBOOKLM' / 'acquisition_runs' / 'AI-LAWS-R031_NB03_RESIDUAL_SOURCE_VALIDATION_CLOSEOUT_2026-09-14.md'
close = f'''# AI-LAWS — R031 / NB03 Residual Source Validation Closeout\n\n**UNIT_ID:** `AI-LAWS-R031 / {BATCH}`  \n**DATE:** {TODAY}  \n**BASE_HEAD_BEFORE_R031:** `{base_head}`  \n**INSPECTION_RUN:** `34812176619`  \n**EXECUTION_CHANNEL:** GitHub only  \n**ZIP_OR_ARTIFACT_CREATED:** NO  \n**AUTO_ADVANCE:** NO\n\n## Scope\n\nOnly the residual NB03 source-processing questions for `US-001` and `US-005` were handled. Notebook ingestion and substantive `AI-LAWS-R007` United States legal inventory were not started.\n\n## Result\n\n```text\nUS001_REPOSITORY_FILE = WHITE_HOUSE_WEBPAGE_PRINT_SNAPSHOT\nUS001_CONTENT_IDENTITY = CONTENT_IDENTITY_PARTIAL\nUS001_OFFICIAL_EXACT_BYTE_MATCH = NOT_APPLICABLE_HTML_SOURCE\nUS001_NOTEBOOK_ROLE = SUPPORTING_ONLY_OFFICIAL_URL_PRIMARY\nUS005_FEDERAL_REGISTER_DOCUMENT = 2025-23092\nUS005_PUBLICATION_DATE = 2025-12-16\nUS005_REPOSITORY_SHA256 = {repo005_sha}\nUS005_OFFICIAL_GOVINFO_SHA256 = {official005_sha}\nUS005_BYTE_SIZE = {len(repo005)}\nUS005_OFFICIAL_EXACT_BYTE_MATCH = YES\nNB03_OFFICIAL_EXACT_BYTE_MATCH_TOTAL = 7 / 8\nDERIVED_MARKDOWN_CREATED = 0\nNOTEBOOK_UPLOADS = 0\nZIP_OR_ARTIFACT_CREATED = 0\n```\n\n## Interpretation firewall\n\n`US-001` is not downgraded because the official White House source is HTML; rather, the project preserves the correct representation boundary. The repository PDF is useful only as a supporting snapshot.\n\n`US-005` exactly matches the official GovInfo Federal Register PDF for document `2025-23092`. This proves pinned-file identity, not permanent legal effect.\n\n```text\nWEBPAGE_PRINT_SNAPSHOT != LIVE_OFFICIAL_PAGE\nEXACT_OFFICIAL_PDF_BYTES != PERMANENT_CURRENTNESS\nEXECUTIVE_ORDER != ACT_OF_CONGRESS\nSOURCE_IDENTITY_VERIFIED != LEGAL_EFFECT_CONCLUSION\n```\n\n`LEGAL_CONCLUSION = NOT_ATTEMPTED`  \n`UNKNOWN_PRESERVED = YES`  \n`AUTO_ADVANCE = NO`\n'''
close_path.write_text(close, encoding='utf-8')

# Structural assertions.
rf2, rr2 = read_csv(D / 'DOWNLOADS_REGISTRY.csv')
rrmap = {r['manifest_source_id']: r for r in rr2}
assert rrmap[US005]['binary_variant'] == 'OFFICIAL_GOVINFO_FEDERAL_REGISTER_PDF_EXACT_MATCH'
assert rrmap[US005]['content_identity_state'] == 'CONTENT_IDENTITY_VERIFIED'
assert rrmap[US001]['content_identity_state'] == 'CONTENT_IDENTITY_PARTIAL'
rf3, r3 = read_csv(res_path)
r3map = {r['source_id']: r for r in r3}
assert r3map[US005]['official_exact_byte_match'] == 'YES'
assert r3map[US001]['official_exact_byte_match'] == 'NOT_APPLICABLE_HTML_SOURCE'
lf2, lr2 = read_csv(ledger_path)
assert sum(1 for r in lr2 if r.get('batch_id') == BATCH) == 2
assert 'AI-LAWS-R031' in qpath.read_text(encoding='utf-8')
assert 'R031_NB03_RESIDUAL_SOURCE_VALIDATION_COMPLETE' in cpath.read_text(encoding='utf-8')
assert close_path.exists()
print('R031_PERSIST_ASSERTIONS=PASS')
print(f'US005_EXACT_SHA256={official005_sha}')
print('US001_REPRESENTATION_STATE=SUPPORTING_ONLY_HTML_PRINT')
