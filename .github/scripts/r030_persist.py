import csv
import hashlib
import os
import re
import subprocess
from pathlib import Path

root = Path('.')
d = root / '86_NOTEBOOKLM/downloads'
ids = [f'EU-{i:03d}' for i in range(1, 11)]
pdf_urls = {
    'EU-001': 'https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:02024R1689-20260727',
    'EU-002': 'https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32026R1744',
    'EU-003': 'https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32024L2853',
    'EU-004': 'https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:12016P/TXT',
    'EU-005': 'https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32016R0679',
    'EU-006': 'https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32022R2065',
    'EU-007': 'https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32023R2854',
    'EU-008': 'https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32022R0868',
    'EU-009': 'https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32022L2555',
    'EU-010': 'https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32024R2847',
}
markers = {
    'EU-001': ['2024/1689', '27.07.2026', 'artificial intelligence'],
    'EU-002': ['2026/1744', 'digital omnibus'],
    'EU-003': ['2024/2853', 'defective products'],
    'EU-004': ['charter of fundamental rights'],
    'EU-005': ['2016/679', 'personal data'],
    'EU-006': ['2022/2065', 'digital services'],
    'EU-007': ['2023/2854', 'fair access to and use of data'],
    'EU-008': ['2022/868', 'data governance'],
    'EU-009': ['2022/2555', 'cybersecurity'],
    'EU-010': ['2024/2847', 'cyber resilience'],
}

def read_csv(path):
    with path.open(newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)

def write_csv(path, fields, rows):
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
        w.writeheader()
        w.writerows(rows)

def run(cmd):
    return subprocess.check_output(cmd, text=True, errors='replace')

def fetch(url, out):
    subprocess.check_call([
        'curl', '-L', '--silent', '--show-error', '--fail-with-body',
        '--connect-timeout', '15', '--max-time', '90', '--retry', '1',
        '-A', 'Mozilla/5.0 AI-LAWS source verification', '-o', str(out), url
    ])
    return out.read_bytes()

reg_fields, reg_rows = read_csv(d / 'DOWNLOADS_REGISTRY.csv')
reg = {r['manifest_source_id']: r for r in reg_rows if r['manifest_source_id'] in ids}
man_fields, man_rows = read_csv(root / '86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv')
man = {r['source_id']: r for r in man_rows if r['source_id'] in ids}
assert set(reg) == set(ids)
assert set(man) == set(ids)

result_fields = [
    'source_id', 'repo_filename', 'repo_git_blob_sha', 'repo_sha256',
    'repo_byte_size', 'pages', 'text_chars', 'text_layer_state',
    'official_pdf_url', 'official_pdf_sha256', 'official_exact_byte_match',
    'content_identity_state', 'currentness_state', 'derivation_required',
    'notebook_upload_eligibility', 'notes'
]
results = []
verified = {}

for sid in ids:
    rr = reg[sid]
    p = d / rr['repo_filename']
    assert p.exists(), (sid, p)
    rb = p.read_bytes()
    rsha = hashlib.sha256(rb).hexdigest()
    blob = run(['git', 'hash-object', str(p)]).strip()
    info = run(['pdfinfo', str(p)])
    txt = run(['pdftotext', '-layout', str(p), '-'])
    norm = ' '.join(txt.lower().split())
    pages_m = re.search(r'^Pages:\s+(\d+)', info, re.M)
    assert pages_m
    pages = int(pages_m.group(1))
    assert len(txt) > 1000
    for marker in markers[sid]:
        assert marker.lower() in norm, (sid, marker)
    op = Path('/tmp') / (sid + '.pdf')
    ob = fetch(pdf_urls[sid], op)
    osha = hashlib.sha256(ob).hexdigest()
    assert ob == rb, (sid, rsha, osha, len(rb), len(ob))
    verified[sid] = (rsha, blob, len(rb), pages, len(txt), osha)

    if sid == 'EU-001':
        variant = 'OFFICIAL_EUR_LEX_CONSOLIDATED_PDF_EXACT_MATCH'
        ingest = 'VERIFIED_OFFICIAL_PDF_ELIGIBLE_WITH_VERSION_LABEL; LIVE_EUR_LEX_RECHECK_REQUIRED_FOR_CURRENTNESS'
    elif sid in ('EU-003', 'EU-009'):
        variant = 'OFFICIAL_EUR_LEX_CELEX_PDF_EXACT_MATCH'
        ingest = 'VERIFIED_OFFICIAL_PDF_ELIGIBLE; DIRECTIVE_NATIONAL_TRANSPOSITION_RECHECK_REQUIRED'
    elif sid == 'EU-010':
        variant = 'OFFICIAL_EUR_LEX_CELEX_PDF_EXACT_MATCH'
        ingest = 'VERIFIED_OFFICIAL_PDF_ELIGIBLE; PHASED_APPLICATION_LABEL_REQUIRED'
    else:
        variant = 'OFFICIAL_EUR_LEX_CELEX_PDF_EXACT_MATCH'
        ingest = 'VERIFIED_OFFICIAL_PDF_ELIGIBLE; LIVE_EUR_LEX_RECHECK_REQUIRED_FOR_CURRENTNESS'

    rr['binary_variant'] = variant
    rr['content_identity_state'] = 'CONTENT_IDENTITY_VERIFIED'
    rr['notebook_ingest_mode'] = ingest
    rr['action'] = (
        f'R030 GitHub validation: SHA256 {rsha}; {pages} pages; native searchable text; '
        f'exact byte match to {pdf_urls[sid]} on 2026-09-14. '
        'Currentness/application/transposition labels remain mandatory.'
    )
    results.append({
        'source_id': sid,
        'repo_filename': rr['repo_filename'],
        'repo_git_blob_sha': blob,
        'repo_sha256': rsha,
        'repo_byte_size': len(rb),
        'pages': pages,
        'text_chars': len(txt),
        'text_layer_state': 'NATIVE_SEARCHABLE_TEXT_LAYER_VERIFIED',
        'official_pdf_url': pdf_urls[sid],
        'official_pdf_sha256': osha,
        'official_exact_byte_match': 'YES',
        'content_identity_state': 'CONTENT_IDENTITY_VERIFIED',
        'currentness_state': rr['currentness_state'],
        'derivation_required': 'NO',
        'notebook_upload_eligibility': ingest,
        'notes': (
            'Current consolidated AI Act snapshot 02024R1689-20260727 exact official EUR-Lex bytes; live currentness remains temporal.'
            if sid == 'EU-001'
            else 'Exact official EUR-Lex CELEX PDF bytes verified; legal application/transposition/currentness state remains source-specific.'
        ),
    })

assert len(results) == 10
write_csv(d / 'NB02_REPOSITORY_PDF_VALIDATION_RESULTS.csv', result_fields, results)
write_csv(d / 'DOWNLOADS_REGISTRY.csv', reg_fields, reg_rows)

ledger_path = root / '86_NOTEBOOKLM/NOTEBOOKLM_ACQUISITION_AND_VALIDATION_LEDGER.csv'
lf, lr = read_csv(ledger_path)
batch = 'NB-BATCH-NB02-20260914-002'
lr = [r for r in lr if r.get('batch_id') != batch]
for sid in ids:
    m = man[sid]
    rr = reg[sid]
    rsha, blob, size, pages, tchars, osha = verified[sid]
    row = {k: '' for k in lf}
    row.update({
        'batch_id': batch,
        'source_id': sid,
        'notebook_pack': 'NB02',
        'jurisdiction': 'EU',
        'title': m.get('title', ''),
        'document_id': m.get('document_id', ''),
        'issuing_authority': 'European Union / EUR-Lex',
        'authority_class': m.get('authority_class', ''),
        'binding_state': m.get('binding_state', ''),
        'official_url': m.get('official_url', ''),
        'retrieval_date': '2026-09-14',
        'version_state': rr.get('currentness_state', '') + '; REPOSITORY_PDF_EXACT_OFFICIAL_BYTE_MATCH_2026-09-14',
        'authentic_language': 'English official EUR-Lex text',
        'translation_state': 'OFFICIAL_ENGLISH_TEXT_USED',
        'rights_state': 'OFFICIAL_PUBLIC_EUR_LEX_SOURCE',
        'acquisition_method': 'REPOSITORY_PDF_VALIDATED_AGAINST_OFFICIAL_EUR_LEX_PDF',
        'local_filename_or_url': rr['repo_filename'],
        'sha256': rsha,
        'byte_size': str(size),
        'content_type': 'application/pdf',
        'content_identity_checked': 'CONTENT_IDENTITY_VERIFIED_EXACT_OFFICIAL_BYTE_MATCH',
        'notebook_ingest_state': 'NOT_RUN',
        'notebook_locator_test': 'NOT_RUN',
        'primary_source_recheck_state': 'OFFICIAL_EUR_LEX_PDF_EXACT_MATCH_2026-09-14',
        'refresh_trigger': 'EUR-Lex correction/amendment/consolidation or application/transposition-state change',
        'human_review_required': 'YES_BEFORE_MATERIAL_LEGAL_CONCLUSION',
        'notes': (
            f'R030 GitHub-only validation: {pages} pages; native searchable text; exact byte match to {pdf_urls[sid]}. '
            'Snapshot identity verification does not replace temporal currentness, phased-application or national-transposition analysis.'
        ),
    })
    lr.append(row)
write_csv(ledger_path, lf, lr)

plan_path = d / 'NOTEBOOK_UPLOAD_PLAN.md'
plan = plan_path.read_text(encoding='utf-8')
new_nb02 = """## NB02 — European Union AI Law

R030 validated all ten `EU-001..EU-010` repository PDFs inside GitHub against official EUR-Lex PDF endpoints. No ZIP/artifact, derived Markdown or Notebook upload was created.

```text
NB02_REPOSITORY_PDFS_INSPECTED = 10 / 10
NB02_NATIVE_SEARCHABLE_TEXT_LAYER = 10 / 10
NB02_CONTENT_IDENTITY_VERIFIED = 10 / 10
NB02_OFFICIAL_EUR_LEX_EXACT_BYTE_MATCH = 10 / 10
NB02_DERIVED_MARKDOWN_REQUIRED = 0
NB02_NOTEBOOK_UPLOADS = 0
```

`EU-001` exactly matches the current consolidated EUR-Lex PDF `CELEX:02024R1689-20260727` dated `2026-07-27`. `EU-002..EU-010` exactly match their corresponding official EUR-Lex CELEX PDFs.

The repository PDFs are therefore eligible as **verified official snapshots**, but official EUR-Lex URLs remain required for temporal currentness and legal-effect checks.

Special labels remain mandatory:

- `EU-001` is a consolidated temporal snapshot; a newer consolidation supersedes it for current-law use.
- `EU-003` and `EU-009` are directives; national transposition must be checked for Member-State-specific duties.
- `EU-010` has phased application: Chapter IV from `2026-06-11`, Article 14 from `2026-09-11`, general application from `2027-12-11`.
- `EU-007` generally applies from `2025-09-12`, with provision-specific dates.

```text
EXACT_OFFICIAL_PDF_BYTES != PERMANENT_CURRENT_LAW
DIRECTIVE_TEXT_VERIFIED != NATIONAL_IMPLEMENTATION_VERIFIED
CONSOLIDATED_SNAPSHOT_VERIFIED != FUTURE_CURRENTNESS_GUARANTEED
```

"""
plan2 = re.sub(r'## NB02 — European Union AI Law\n.*?(?=## NB03 — United States\n)', new_nb02, plan, flags=re.S)
assert plan2 != plan
plan_path.write_text(plan2, encoding='utf-8')

list_path = root / '86_NOTEBOOKLM/NOTEBOOKLM_DOWNLOAD_AND_UPLOAD_LIST.md'
text = list_path.read_text(encoding='utf-8')
marker = '### R030 repository-PDF verification state'
if marker not in text:
    m = re.search(r'(## C\. NB02 — European Union AI law\n.*?)(?=\n## D\.)', text, flags=re.S)
    assert m
    addition = """

### R030 repository-PDF verification state

All ten `EU-001..EU-010` repository PDFs are native-searchable and exact-byte matches to the appropriate official EUR-Lex PDFs as rechecked on 2026-09-14. `EU-001` uses consolidated `CELEX:02024R1689-20260727`; directives and phased-application/currentness labels remain mandatory. No Notebook upload was performed by R030.
"""
    block = m.group(1) + addition
    text = text[:m.start(1)] + block + text[m.end(1):]
    list_path.write_text(text, encoding='utf-8')

qpath = root / '90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv'
qf, qr = read_csv(qpath)
first_col = qf[0]
if not any(r.get('research_id') == 'AI-LAWS-R030' or r.get(first_col) == 'AI-LAWS-R030' for r in qr):
    row = {k: '' for k in qf}
    vals = [
        'AI-LAWS-R030', 'P0', 'Notebook NB02 repository PDF validation',
        'Validate EU-001..EU-010 repository PDF bodies/text layers and exact-byte identity against the correct official EUR-Lex PDFs without starting substantive EU legal analysis',
        'COMPLETE_SUPPORT_SOURCE_VALIDATION',
        'R024/R025 COMPLETE + repository PDFs present',
        '86_NOTEBOOKLM/downloads/NB02_REPOSITORY_PDF_VALIDATION_RESULTS.csv; updated registry/ledger/upload plan/download list; R030 closeout',
        '10/10 exact official EUR-Lex PDF matches; currentness/transposition/phased-application labels preserved; no Notebook upload or R003 auto-started',
    ]
    for k, v in zip(qf, vals):
        row[k] = v
    qr.append(row)
    write_csv(qpath, qf, qr)

cpath = root / '00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md'
c = cpath.read_text(encoding='utf-8')
state_old = 'R029_NB08_REPOSITORY_INCIDENT_SOURCE_VALIDATION_COMPLETE / LEGAL_RESEARCH_ACTIVE'
if 'R030_NB02_REPOSITORY_PDF_VALIDATION_COMPLETE' not in c[:1500]:
    assert state_old in c
    c = c.replace(state_old, 'R029_NB08_REPOSITORY_INCIDENT_SOURCE_VALIDATION_COMPLETE / R030_NB02_REPOSITORY_PDF_VALIDATION_COMPLETE / LEGAL_RESEARCH_ACTIVE', 1)
if 'AI-LAWS-R030 = COMPLETE_SUPPORT_SOURCE_VALIDATION' not in c:
    assert 'AI-LAWS-R029 = COMPLETE_SUPPORT_SOURCE_VALIDATION\n```' in c
    c = c.replace('AI-LAWS-R029 = COMPLETE_SUPPORT_SOURCE_VALIDATION\n```', 'AI-LAWS-R029 = COMPLETE_SUPPORT_SOURCE_VALIDATION\nAI-LAWS-R030 = COMPLETE_SUPPORT_SOURCE_VALIDATION\n```', 1)
if '### R030 — NB02 repository PDF validation' not in c:
    anchor = '### R025 — NB02 remaining EU source validation\n'
    assert anchor in c
    sec = """### R030 — NB02 repository PDF validation

R030 inspected `EU-001..EU-010` inside GitHub and compared every repository PDF byte-for-byte with the appropriate official EUR-Lex PDF endpoint.

```text
NB02_REPOSITORY_PDFS_INSPECTED = 10 / 10
NB02_NATIVE_SEARCHABLE_TEXT_LAYER = 10 / 10
NB02_CONTENT_IDENTITY_VERIFIED = 10 / 10
NB02_OFFICIAL_EUR_LEX_EXACT_BYTE_MATCH = 10 / 10
NB02_DERIVED_MARKDOWN = 0
NB02_NOTEBOOK_UPLOADS = 0
```

`EU-001` exactly matches consolidated `CELEX:02024R1689-20260727`; `EU-002..EU-010` exactly match their official CELEX PDFs. Exact snapshot identity does not eliminate currentness, national-transposition or phased-application checks.

Durable output: `86_NOTEBOOKLM/downloads/NB02_REPOSITORY_PDF_VALIDATION_RESULTS.csv` plus registry/ledger/upload-plan/download-list/queue reconciliation.

"""
    c = c.replace(anchor, sec + anchor, 1)
c = re.sub(
    r'### NB02 current ingest state\n\n```text\n.*?```',
    """### NB02 current ingest state

```text
NB02_OFFICIAL_URL_SOURCE_SET = READY
NB02_REPOSITORY_PDF_CONTENT_IDENTITY_VERIFIED = 10 / 10
NB02_OFFICIAL_EUR_LEX_EXACT_BYTE_MATCH = 10 / 10
NB02_NATIVE_TEXT_LAYER = 10 / 10
NB02_REPOSITORY_PDF_UPLOAD_SET = ELIGIBLE_AS_VERIFIED_OFFICIAL_SNAPSHOTS_WITH_DATE_STATE_LABELS
NB02_DERIVED_MARKDOWN_REQUIRED = 0
NB02_NOTEBOOK_UPLOADS = 0
```""",
    c,
    count=1,
    flags=re.S,
)
c = c.replace('NB02_REPOSITORY_PDF_CONTENT_IDENTITY_PARTIAL = 10', 'R025_NB02_REPOSITORY_PDF_CONTENT_IDENTITY_PARTIAL = 10')
integrity_anchor = 'R028_NB03_NATIVE_TEXT_LAYER_VERIFIED = 8\n'
r030_lines = (
    'R030_NB02_REPOSITORY_PDFS_INSPECTED = 10\n'
    'R030_NB02_CONTENT_IDENTITY_VERIFIED = 10\n'
    'R030_NB02_OFFICIAL_EUR_LEX_EXACT_BYTE_MATCH = 10\n'
    'R030_NB02_NATIVE_TEXT_LAYER_VERIFIED = 10\n'
)
if 'R030_NB02_REPOSITORY_PDFS_INSPECTED = 10' not in c:
    assert integrity_anchor in c
    c = c.replace(integrity_anchor, integrity_anchor + r030_lines, 1)
cpath.write_text(c, encoding='utf-8')

close = root / '86_NOTEBOOKLM/acquisition_runs/AI-LAWS-R030_NB02_REPOSITORY_PDF_VALIDATION_CLOSEOUT_2026-09-14.md'
close.write_text(f"""# AI-LAWS — R030 / NB02 Repository PDF Validation Closeout

**UNIT_ID:** `AI-LAWS-R030 / NB-BATCH-NB02-20260914-002`
**DATE:** 2026-09-14
**BASE_HEAD_BEFORE_R030:** `113f7c85889fbeee9d3d315dfefcf97e7ec201c1`
**SUCCESSFUL_INSPECTION_COMMIT / RUN:** `9086ca08acf580a837bcf2ca55af92741c768b26` / `34810764927`
**EU001_CONSOLIDATED_RESOLVER_COMMIT / RUN:** `e6004133edb8f53b672c9aa3b55a6b840f7238be` / `34810853144`
**DURABLE_RUN:** `{os.environ.get('GITHUB_RUN_ID', 'UNKNOWN')}`
**EXECUTION_CHANNEL:** GitHub only
**ZIP_OR_ARTIFACT_CREATED:** NO
**AUTO_ADVANCE:** NO

## Result

```text
NB02_REPOSITORY_PDFS_INSPECTED = 10 / 10
NATIVE_SEARCHABLE_TEXT_LAYER = 10 / 10
CONTENT_IDENTITY_VERIFIED = 10 / 10
OFFICIAL_EUR_LEX_EXACT_BYTE_MATCH = 10 / 10
DERIVED_MARKDOWN_CREATED = 0
NOTEBOOK_UPLOADS = 0
ZIP_OR_ARTIFACT_CREATED = 0
```

`EU-001` exactly matches the current consolidated EUR-Lex PDF `CELEX:02024R1689-20260727`. `EU-002..EU-010` exactly match their corresponding official EUR-Lex CELEX PDFs.

## Legal/currentness firewall

```text
EXACT_OFFICIAL_PDF_BYTES != PERMANENT_CURRENT_LAW
CONSOLIDATED_SNAPSHOT_VERIFIED != FUTURE_CURRENTNESS_GUARANTEED
DIRECTIVE_TEXT_VERIFIED != NATIONAL_IMPLEMENTATION_VERIFIED
PHASED_APPLICATION != GENERAL_APPLICATION
NOTEBOOK_UPLOAD != LEGAL_VERIFICATION
```

R003 substantive EU AI Act legal analysis was not started. No legal conclusion was created.

`LEGAL_CONCLUSION = NOT_ATTEMPTED`
`UNKNOWN_PRESERVED = YES`
`AUTO_ADVANCE = NO`
""", encoding='utf-8')

assert len(results) == 10
assert all(r['official_exact_byte_match'] == 'YES' for r in results)
assert sum(1 for r in reg_rows if r.get('manifest_source_id') in ids and r.get('content_identity_state') == 'CONTENT_IDENTITY_VERIFIED') == 10
assert sum(1 for r in lr if r.get('batch_id') == batch) == 10
assert 'R030_NB02_CONTENT_IDENTITY_VERIFIED = 10' in cpath.read_text(encoding='utf-8')
assert 'AI-LAWS-R030' in qpath.read_text(encoding='utf-8')
print('R030_DURABLE_STATE_READY=YES')
