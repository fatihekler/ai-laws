import csv
import hashlib
import re
import subprocess
from pathlib import Path

ROOT = Path('.')
D = ROOT / '86_NOTEBOOKLM' / 'downloads'
TODAY = '2026-09-14'
BATCH = 'NB-BATCH-NB01-20260914-003'
BASE_HEAD = 'c4b016f3ec7cc262f7a8bc1754dc14091b441b7c'
INT004 = 'INT-004'
INT007 = 'INT-007'
INT004_URL = 'https://unesdoc.unesco.org/ark:/48223/pf0000397812_eng'
INT007_VIEWER = 'https://docs.un.org/en/A/RES/79/1'
INT007_API = 'https://documents.un.org/api/symbol/access?s=A/RES/79/1&l=en&t=pdf'
INT007_PDF = 'https://documents.un.org/doc/undoc/gen/n24/272/22/pdf/n2427222.pdf'
INT007_SHA = '0c3968d0ce8d55cf107309794adea6879d70f9aea60e6d6d64e3a8da4b028336'
INT007_BYTES = 649956
INT007_PAGES = 56
INT007_TEXT_CHARS = 249568


def sh(cmd):
    return subprocess.check_output(cmd, text=True, errors='replace').strip()


def read_csv(path):
    with path.open(newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def write_csv(path, fields, rows):
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def curl(url, out):
    p = Path('/tmp') / out
    cp = subprocess.run([
        'curl', '-L', '--silent', '--show-error', '--connect-timeout', '20',
        '--max-time', '120', '--retry', '2', '--retry-delay', '2',
        '-A', 'Mozilla/5.0 AI-LAWS source verification', '-o', str(p),
        '-w', '%{http_code}|%{content_type}|%{url_effective}', url
    ], text=True, capture_output=True, check=False)
    b = p.read_bytes() if p.exists() else b''
    return cp.returncode, cp.stdout.strip(), cp.stderr.strip(), b, p


def replace_once(text, old, new, label):
    count = text.count(old)
    assert count == 1, f'{label}: expected one match, got {count}'
    return text.replace(old, new, 1)


# Fail closed on overlapping drift before any durable write.
sh(['git', 'fetch', 'origin', 'main'])
head = sh(['git', 'rev-parse', 'HEAD'])
origin = sh(['git', 'rev-parse', 'origin/main'])
assert head == origin, (head, origin)
run_base_head = head

# Re-verify exact official A/RES/79/1 bytes immediately before persistence.
rc7, meta7, err7, b7, p7 = curl(INT007_API, 'r032-int007.pdf')
assert rc7 == 0, err7
status7, ctype7, final7 = meta7.split('|', 2)
assert status7 == '200'
assert ctype7.startswith('application/pdf')
assert final7 == INT007_PDF, final7
assert len(b7) == INT007_BYTES, len(b7)
assert sha256(b7) == INT007_SHA
info7 = sh(['pdfinfo', str(p7)])
txt7 = sh(['pdftotext', '-layout', str(p7), '-'])
pages7 = int(re.search(r'^Pages:\s+(\d+)', info7, re.M).group(1))
assert pages7 == INT007_PAGES
assert 'A/RES/79/1' in txt7
assert 'The Pact for the Future' in txt7 or 'Pact for the Future' in txt7
assert 'Global Digital Compact' in txt7
assert '22 September 2024' in txt7

# INT-004: access recheck only. Prior official certified-copy pin remains authoritative.
rc4, meta4, err4, b4, p4 = curl(INT004_URL, 'r032-int004.html')
assert rc4 == 0
status4, ctype4, final4 = meta4.split('|', 2)
assert status4 in {'200', '403'}, status4
if status4 == '200':
    visible4 = ' '.join(re.sub(r'<[^>]+>', ' ', b4.decode('utf-8', 'replace')).split())
    assert 'Recommendation on the Ethics of Neurotechnology' in visible4
    int004_access_state = 'FRESH_OFFICIAL_RECORD_ACCESSIBLE_2026-09-14'
else:
    int004_access_state = 'GITHUB_RUNNER_ACCESS_RECHECK_BLOCKED_403_2026-09-14'

# Manifest reconciliation.
manifest_path = ROOT / '86_NOTEBOOKLM' / 'NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv'
mf, mr = read_csv(manifest_path)
manifest = {r['source_id']: r for r in mr if r['source_id'] in {INT004, INT007}}
assert set(manifest) == {INT004, INT007}

m4 = manifest[INT004]
assert m4['official_url'] == INT004_URL
if status4 == '403':
    if 'R032 GitHub runner recheck returned HTTP 403' not in m4['notes']:
        m4['notes'] += ' R032 GitHub runner recheck returned HTTP 403 on 2026-09-14; preserve the prior verified certified-copy pin and do not claim fresh R032 content-body verification.'
    m4['verification_state'] = 'VERIFIED_OFFICIAL_CERTIFIED_COPY_PRIOR_PIN; R032_GITHUB_RUNNER_ACCESS_BLOCKED_403'
else:
    m4['verification_state'] = 'VERIFIED_OFFICIAL_CERTIFIED_COPY; R032_OFFICIAL_RECORD_ACCESS_RECHECKED'
    m4['last_verified'] = TODAY

m7 = manifest[INT007]
m7['official_url'] = INT007_VIEWER
m7['verification_state'] = 'VERIFIED_OFFICIAL_EXACT_A_RES_79_1_SOURCE_R032'
m7['last_verified'] = TODAY
m7['rights_or_use_state'] = 'OFFICIAL_PUBLIC_URL_REPRODUCTION_PERMISSION_NOT_ESTABLISHED'
m7['notes'] = (
    'Use adopted official A/RES/79/1 source, not draft revisions. R032 resolved the official UN viewer and PDF chain: '
    f'{INT007_VIEWER} -> {INT007_PDF}; 56 pages; {INT007_BYTES} bytes; SHA-256 {INT007_SHA}; '
    'A/RES/79/1, Pact for the Future and Global Digital Compact markers verified. Prefer URL ingestion; no public-repository vendoring right inferred.'
)
write_csv(manifest_path, mf, mr)

# Repository binary registry reconciliation. The repository binaries themselves are not replaced.
reg_path = D / 'DOWNLOADS_REGISTRY.csv'
rf, rr = read_csv(reg_path)
reg = {r['manifest_source_id']: r for r in rr if r['manifest_source_id'] in {INT004, INT007}}
assert set(reg) == {INT004, INT007}

r4 = reg[INT004]
r4['binary_variant'] = 'LEGACY_43GC_RESOLUTIONS_VOLUME'
r4['content_identity_state'] = 'SUPERSEDED_SOURCE'
r4['currentness_state'] = f'LEGACY_43GC_SOURCE_IDENTITY_VERIFIED; CERTIFIED_COPY_PRIMARY_PRIOR_PIN; {int004_access_state}'
r4['notebook_ingest_mode'] = 'DO_NOT_UPLOAD_AS_CURRENT_PRIMARY; USE_CERTIFIED_COPY_URL_pf0000397812_eng; HISTORICAL_SUPPORTING_ONLY_IF_NEEDED'
r4['action'] = (
    'R032 official-source recheck: current certified-copy identity remains pinned to '
    f'{INT004_URL}. GitHub runner access state on {TODAY}: HTTP {status4}. '
    'Repository 43GC resolutions PDF remains a genuine legacy/superseded variant and must not replace the certified-copy primary source.'
)

r7 = reg[INT007]
r7['binary_variant'] = 'UN_SUMMIT_OUTCOME_DOCUMENT_BUNDLE'
r7['content_identity_state'] = 'CONTENT_IDENTITY_PARTIAL'
r7['currentness_state'] = 'REPOSITORY_BUNDLE_IDENTITY_VERIFIED; EXACT_OFFICIAL_A_RES_79_1_PDF_RESOLVED_2026-09-14; REPOSITORY_BUNDLE_NOT_EXACT_RESOLUTION'
r7['notebook_ingest_mode'] = 'OFFICIAL_A_RES_79_1_URL_PRIMARY; REPOSITORY_OUTCOME_BUNDLE_SUPPORTING_ONLY'
r7['action'] = (
    f'R032 resolved exact official A/RES/79/1: viewer {INT007_VIEWER}; direct PDF {INT007_PDF}; '
    f'SHA256 {INT007_SHA}; {INT007_BYTES} bytes; {INT007_PAGES} pages; native searchable text. '
    'Repository 64-page Summit outcome bundle remains CONTENT_IDENTITY_PARTIAL relative to exact A/RES/79/1 and is supporting-only.'
)
write_csv(reg_path, rf, rr)

# NB01 binary/source results reconciliation.
res_path = D / 'NB01_CONTENT_IDENTITY_RESULTS.csv'
nf, nr = read_csv(res_path)
nb = {r['source_id']: r for r in nr if r['source_id'] in {INT004, INT007}}
assert set(nb) == {INT004, INT007}

e4 = nb[INT004]
e4['content_identity_state'] = 'SUPERSEDED_SOURCE'
e4['currentness_state'] = f'LEGACY_43GC_SOURCE_IDENTITY_VERIFIED; CERTIFIED_COPY_PRIMARY_PRIOR_PIN; {int004_access_state}'
e4['notebook_upload_eligibility'] = 'DO_NOT_UPLOAD_AS_CURRENT_PRIMARY; USE_CERTIFIED_COPY_URL_pf0000397812_eng; HISTORICAL_SUPPORTING_ONLY_IF_NEEDED'
e4['notes'] = (
    'R027 verified the 137-page 43GC resolutions volume as a genuine legacy source. R032 preserved the prior certified-copy primary pin '
    f'{INT004_URL}; fresh GitHub-runner access returned HTTP {status4} on {TODAY}, so no fresh R032 certified-copy content-body verification is claimed.'
)

e7 = nb[INT007]
e7['content_identity_state'] = 'CONTENT_IDENTITY_PARTIAL'
e7['currentness_state'] = 'OUTCOME_DOCUMENT_BUNDLE_IDENTITY_VERIFIED; EXACT_OFFICIAL_A_RES_79_1_SOURCE_VERIFIED_R032'
e7['notebook_upload_eligibility'] = 'REPOSITORY_BUNDLE_SUPPORTING_ONLY; OFFICIAL_A_RES_79_1_URL_PRIMARY_VERIFIED'
e7['notes'] = (
    'Repository file remains a 64-page Summit outcome-document bundle and is not the exact resolution binary. R032 verified the exact official '
    f'A/RES/79/1 PDF at {INT007_PDF}: {INT007_PAGES} pages; {INT007_BYTES} bytes; SHA-256 {INT007_SHA}; '
    'native text contains A/RES/79/1, Pact for the Future and Global Digital Compact. Use the official source for primary resolution identity.'
)
write_csv(res_path, nf, nr)

# Compact R032 residual results matrix.
residual_fields = [
    'source_id','repository_variant','repository_content_identity_state','official_primary_url','direct_official_pdf_url',
    'official_access_state','official_sha256','official_byte_size','official_pages','official_text_state','resolution_state',
    'notebook_use','rights_state','notes'
]
residual_rows = [
    {
        'source_id': INT004,
        'repository_variant': 'LEGACY_43GC_RESOLUTIONS_VOLUME',
        'repository_content_identity_state': 'SUPERSEDED_SOURCE',
        'official_primary_url': INT004_URL,
        'direct_official_pdf_url': '',
        'official_access_state': int004_access_state,
        'official_sha256': '',
        'official_byte_size': '',
        'official_pages': '',
        'official_text_state': 'NOT_FRESHLY_REVERIFIED_BY_R032' if status4 == '403' else 'OFFICIAL_RECORD_HTML_IDENTITY_RECHECKED',
        'resolution_state': 'PRIOR_CERTIFIED_COPY_PIN_PRESERVED; FRESH_ACCESS_BLOCKER_RECORDED' if status4 == '403' else 'CERTIFIED_COPY_OFFICIAL_RECORD_RECHECKED',
        'notebook_use': 'CERTIFIED_COPY_URL_PRIMARY; REPOSITORY_LEGACY_VOLUME_SUPPORTING_ONLY',
        'rights_state': m4['rights_or_use_state'],
        'notes': 'No new UNESCO binary was vendored. R032 does not infer redistribution rights or fresh content verification from a blocked request.' if status4 == '403' else 'No new UNESCO binary was vendored; certified-copy official record was accessible during R032.'
    },
    {
        'source_id': INT007,
        'repository_variant': 'UN_SUMMIT_OUTCOME_DOCUMENT_BUNDLE',
        'repository_content_identity_state': 'CONTENT_IDENTITY_PARTIAL',
        'official_primary_url': INT007_VIEWER,
        'direct_official_pdf_url': INT007_PDF,
        'official_access_state': 'HTTP_200_APPLICATION_PDF_VERIFIED_2026-09-14',
        'official_sha256': INT007_SHA,
        'official_byte_size': str(INT007_BYTES),
        'official_pages': str(INT007_PAGES),
        'official_text_state': 'NATIVE_SEARCHABLE_TEXT_MARKERS_VERIFIED',
        'resolution_state': 'EXACT_OFFICIAL_A_RES_79_1_SOURCE_RESOLVED',
        'notebook_use': 'OFFICIAL_URL_PRIMARY; REPOSITORY_BUNDLE_SUPPORTING_ONLY',
        'rights_state': 'OFFICIAL_PUBLIC_URL_REPRODUCTION_PERMISSION_NOT_ESTABLISHED',
        'notes': 'Exact official UN resolution source resolved without vendoring the third-party PDF into the repository.'
    }
]
write_csv(D / 'NB01_RESIDUAL_OFFICIAL_SOURCE_RESULTS.csv', residual_fields, residual_rows)

# Append R032 acquisition/validation ledger rows without changing R027 history.
ledger_path = ROOT / '86_NOTEBOOKLM' / 'NOTEBOOKLM_ACQUISITION_AND_VALIDATION_LEDGER.csv'
lf, lr = read_csv(ledger_path)
lr = [r for r in lr if r.get('batch_id') != BATCH]

row4 = {k: '' for k in lf}
row4.update({
    'batch_id': BATCH,
    'source_id': INT004,
    'notebook_pack': 'NB01;NB06',
    'jurisdiction': 'UNESCO',
    'title': 'Recommendation on the Ethics of Neurotechnology',
    'document_id': 'UNESCO 43rd General Conference Recommendation 2025 / certified copy 2026',
    'issuing_authority': 'UNESCO General Conference',
    'authority_class': 'SOFT_LAW_RECOMMENDATION',
    'binding_state': 'nonbinding recommendation',
    'official_url': INT004_URL,
    'retrieval_date': TODAY,
    'version_state': f'PRIOR_CERTIFIED_COPY_PIN_PRESERVED; {int004_access_state}',
    'adoption_date': '2025-11-11',
    'publication_date': '2026-03-31',
    'authentic_language': 'English certified-copy record previously pinned',
    'translation_state': 'NOT_APPLICABLE',
    'rights_state': m4['rights_or_use_state'],
    'acquisition_method': 'URL_DIRECT_PREFERRED; NO_NEW_BINARY_VENDORING',
    'local_filename_or_url': INT004_URL,
    'content_type': ctype4,
    'content_identity_checked': 'PRIOR_OFFICIAL_IDENTITY_PRESERVED_NO_FRESH_CONTENT_BODY_R032' if status4 == '403' else 'OFFICIAL_RECORD_IDENTITY_RECHECKED_R032',
    'notebook_ingest_state': 'NOT_RUN',
    'notebook_locator_test': 'NOT_RUN',
    'primary_source_recheck_state': int004_access_state,
    'refresh_trigger': 'UNESCO source accessibility/version/licence change or material neurotechnology claim',
    'human_review_required': 'YES_BEFORE_MATERIAL_LEGAL_OR_RIGHTS_CONCLUSION',
    'notes': 'R032 did not vendor a new UNESCO binary. Prior certified-copy identity remains the source-of-truth; fresh GitHub-runner content recheck was blocked by HTTP 403.' if status4 == '403' else 'R032 rechecked the official certified-copy record but did not vendor a new binary.'
})
lr.append(row4)

row7 = {k: '' for k in lf}
row7.update({
    'batch_id': BATCH,
    'source_id': INT007,
    'notebook_pack': 'NB01',
    'jurisdiction': 'UN',
    'title': 'Pact for the Future including Global Digital Compact',
    'document_id': 'A/RES/79/1',
    'issuing_authority': 'United Nations General Assembly',
    'authority_class': 'TREATY_OR_INTERNATIONAL_INSTRUMENT',
    'binding_state': 'UN General Assembly outcome document; not treaty',
    'official_url': INT007_VIEWER,
    'retrieval_date': TODAY,
    'version_state': 'EXACT_OFFICIAL_A_RES_79_1_PDF_RESOLVED_AND_HASHED_R032',
    'adoption_date': '2024-09-22',
    'publication_date': '2024-09-22',
    'authentic_language': 'English official UN document',
    'translation_state': 'NOT_APPLICABLE',
    'rights_state': 'OFFICIAL_PUBLIC_URL_REPRODUCTION_PERMISSION_NOT_ESTABLISHED',
    'acquisition_method': 'URL_DIRECT_PREFERRED_OFFICIAL_PDF_HASH_CAPTURE_NO_REPO_VENDORING',
    'local_filename_or_url': INT007_PDF,
    'sha256': INT007_SHA,
    'byte_size': str(INT007_BYTES),
    'content_type': 'application/pdf',
    'content_identity_checked': 'EXACT_OFFICIAL_DOCUMENT_IDENTITY_VERIFIED',
    'notebook_ingest_state': 'NOT_RUN',
    'notebook_locator_test': 'NOT_RUN',
    'primary_source_recheck_state': 'A_RES_79_1_OFFICIAL_PDF_RECHECKED_2026-09-14',
    'refresh_trigger': 'UN document correction/replacement or material claim requiring source recheck',
    'human_review_required': 'YES_BEFORE_MATERIAL_LEGAL_CONCLUSION',
    'notes': f'R032 verified official PDF chain {INT007_VIEWER} -> {INT007_PDF}; {INT007_PAGES} pages; {INT007_BYTES} bytes; SHA-256 {INT007_SHA}; native text markers A/RES/79/1, Pact for the Future and Global Digital Compact all present. No binary vendored.'
})
lr.append(row7)
write_csv(ledger_path, lf, lr)

# Update downloaded-source README warnings.
readme_path = D / 'README.md'
readme = readme_path.read_text(encoding='utf-8')
old4 = "The repository file named `Recommendation on the Ethics of Neurotechnology (2025)  43rd General Conference resolutions source.pdf` is a legacy source variant. The current preferred primary Notebook source is UNESCO's certified-copy record `pf0000397812_eng` identified in the acquisition manifest and NB06 closeout. Do not load the legacy PDF as the primary/current source."
new4 = old4 + f" R032 rechecked the certified-copy URL from GitHub; the runner received HTTP {status4} on 2026-09-14. This access result does not invalidate the prior official certified-copy pin, but fresh R032 content-body verification is not claimed while access is blocked."
readme = replace_once(readme, old4, new4, 'downloads README INT004')
old7 = "R027 verified the repository file as a 64-page Summit of the Future outcome-document bundle containing the Pact for the Future and Global Digital Compact. The extracted text does not contain the exact `A/RES/79/1` identifier, so it is `CONTENT_IDENTITY_PARTIAL` for the manifest source and must not replace the exact adopted-resolution source."
new7 = old7 + f" R032 resolved the exact adopted source through `{INT007_VIEWER}` to the official 56-page PDF `{INT007_PDF}`; SHA-256 `{INT007_SHA}`. Use that official source for primary resolution identity; keep the repository bundle supporting-only."
readme = replace_once(readme, old7, new7, 'downloads README INT007')
readme_path.write_text(readme, encoding='utf-8')

# Update Notebook upload plan NB01 state without changing repository binary counts.
plan_path = D / 'NOTEBOOK_UPLOAD_PLAN.md'
plan = plan_path.read_text(encoding='utf-8')
old_metrics = '''NB01_CORE_REPOSITORY_PDFS_INSPECTED = 8 / 8
NATIVE_SEARCHABLE_TEXT_LAYER = 8 / 8
CONTENT_IDENTITY_VERIFIED = 6
CONTENT_IDENTITY_PARTIAL = 1  # INT-007 outcome bundle, not exact A/RES/79/1 file
SUPERSEDED_SOURCE = 1         # INT-004 legacy 43GC volume
DERIVED_MARKDOWN_REQUIRED = 0
NOTEBOOK_UPLOADS = 0'''
new_metrics = old_metrics + '''
INT007_EXACT_OFFICIAL_A_RES_79_1_SOURCE = VERIFIED_R032
INT004_CERTIFIED_COPY_R032_ACCESS = BLOCKED_403_PRIOR_PIN_PRESERVED'''
if status4 == '200':
    new_metrics = new_metrics.replace('BLOCKED_403_PRIOR_PIN_PRESERVED', 'OFFICIAL_RECORD_ACCESS_RECHECKED')
plan = replace_once(plan, old_metrics, new_metrics, 'NB01 plan metrics')
old_bullet7 = '- `INT-007` Pact for the Future / Global Digital Compact — repository PDF is a verified outcome-document bundle but not the exact A/RES/79/1 file; UN official adopted source required for primary resolution identity.'
new_bullet7 = f'- `INT-007` Pact for the Future / Global Digital Compact — repository PDF remains a verified supporting outcome-document bundle, but R032 resolved the exact adopted source at `{INT007_VIEWER}` and official 56-page PDF `{INT007_PDF}` (SHA-256 `{INT007_SHA}`). Use the official source for primary resolution identity.'
plan = replace_once(plan, old_bullet7, new_bullet7, 'NB01 plan INT007 bullet')
old_primary4 = '- repository `INT-004` legacy 43rd General Conference resolutions PDF. Replace the primary Notebook source with the current certified-copy UNESCO source recorded in the manifest.'
new_primary4 = old_primary4 + f' R032 GitHub-runner access to the certified-copy URL returned HTTP {status4}; preserve the prior pin and do not infer source invalidity from the runner access block.'
plan = replace_once(plan, old_primary4, new_primary4, 'NB01 plan INT004 primary warning')
plan_path.write_text(plan, encoding='utf-8')

# Update download/upload list exact source pointers.
list_path = ROOT / '86_NOTEBOOKLM' / 'NOTEBOOKLM_DOWNLOAD_AND_UPLOAD_LIST.md'
dl = list_path.read_text(encoding='utf-8')
old_dl4 = '''- `INT-004` Recommendation on the Ethics of Neurotechnology  
  **Current preferred certified-copy source:**  
  https://unesdoc.unesco.org/ark:/48223/pf0000397812_eng  
  **Use state:** official certified-copy URL preferred. The repository PDF derived from the 43rd General Conference resolutions source is a legacy source variant and must not be loaded as the current primary source.'''
new_dl4 = '''- `INT-004` Recommendation on the Ethics of Neurotechnology
  **Current preferred certified-copy source:**
  https://unesdoc.unesco.org/ark:/48223/pf0000397812_eng
  **Use state:** official certified-copy URL preferred. The repository PDF derived from the 43rd General Conference resolutions source is a legacy source variant and must not be loaded as the current primary source.
  **R032 access state:** GitHub runner returned HTTP ''' + status4 + ''' on 2026-09-14; prior official certified-copy pin preserved; fresh R032 content-body verification not claimed while blocked.'''
dl = replace_once(dl, old_dl4, new_dl4, 'download list INT004')
old_dl7 = '''- `INT-007` Pact for the Future / Global Digital Compact — A/RES/79/1 source family  
  https://www.un.org/pact-for-the-future/en  
  **R027 repository file state:** 64-page Summit of the Future outcome-document bundle verified; exact `A/RES/79/1` identifier is absent from the PDF, so use the adopted official source for primary resolution identity.'''
new_dl7 = f'''- `INT-007` Pact for the Future / Global Digital Compact — A/RES/79/1
  **Official viewer:** {INT007_VIEWER}
  **Official PDF:** {INT007_PDF}
  **R032 official PDF state:** 56 pages; {INT007_BYTES} bytes; SHA-256 `{INT007_SHA}`; `A/RES/79/1`, Pact for the Future and Global Digital Compact markers verified.
  **Repository file state:** 64-page Summit outcome-document bundle remains `CONTENT_IDENTITY_PARTIAL` relative to the exact resolution and is supporting-only.'''
dl = replace_once(dl, old_dl7, new_dl7, 'download list INT007')
list_path.write_text(dl, encoding='utf-8')

# R032 closeout.
closeout_path = ROOT / '86_NOTEBOOKLM' / 'acquisition_runs' / 'AI-LAWS-R032_NB01_RESIDUAL_OFFICIAL_SOURCE_VALIDATION_CLOSEOUT_2026-09-14.md'
closeout = f'''# AI-LAWS — R032 / NB01 Residual Official-Source Validation Closeout

**UNIT_ID:** `AI-LAWS-R032 / {BATCH}`
**DATE:** {TODAY}
**BASE_HEAD_BEFORE_R032:** `{BASE_HEAD}`
**PERSIST_RUN_BASE_HEAD:** `{run_base_head}`
**EXECUTION_CHANNEL:** GitHub / GitHub Actions only
**ZIP_OR_ARTIFACT_CREATED:** NO
**AUTO_ADVANCE:** NO

## Scope

This bounded unit handled only the residual official-source routing for `INT-004` and `INT-007`. It did not start substantive `AI-LAWS-R004`, `AI-LAWS-R011`, Notebook ingestion, or legal analysis.

## INT-007 — A/RES/79/1

R032 resolved the exact official United Nations document chain:

```text
OFFICIAL_VIEWER = {INT007_VIEWER}
OFFICIAL_PDF = {INT007_PDF}
HTTP = 200
CONTENT_TYPE = application/pdf
PAGES = {INT007_PAGES}
BYTE_SIZE = {INT007_BYTES}
SHA256 = {INT007_SHA}
A_RES_79_1_MARKER = YES
PACT_FOR_THE_FUTURE_MARKER = YES
GLOBAL_DIGITAL_COMPACT_MARKER = YES
NATIVE_SEARCHABLE_TEXT = YES
```

The existing 64-page repository PDF remains a genuine Summit outcome-document bundle but is not the exact resolution binary. It therefore remains `CONTENT_IDENTITY_PARTIAL / SUPPORTING_ONLY` relative to `A/RES/79/1`.

No UN PDF was newly vendored because public-repository redistribution permission was not established; official URL ingestion is preferred.

## INT-004 — UNESCO Neurotechnology

The previously verified official certified-copy pin remains:

`{INT004_URL}`

R032 GitHub-runner access state was HTTP `{status4}`. Because the runner did not obtain the substantive certified-copy body when blocked, R032 does not claim a fresh content-body re-verification. The existing 137-page repository 43GC resolutions volume remains a genuine legacy source and `SUPERSEDED_SOURCE` for current primary use.

```text
PRIOR_CERTIFIED_COPY_PIN = PRESERVED
FRESH_R032_CONTENT_BODY_VERIFIED = {'YES' if status4 == '200' else 'NO'}
REPOSITORY_LEGACY_PDF_PRIMARY = NO
NEW_UNESCO_BINARY_VENDORED = NO
```

## Firewalls

```text
OFFICIAL_URL_RESOLVED != REPOSITORY_VENDORING_RIGHT
REPOSITORY_OUTCOME_BUNDLE != EXACT_A_RES_79_1_BINARY
HTTP_403 != SOURCE_INVALID
PRIOR_VERIFIED_SOURCE_PIN != FRESH_CONTENT_RECHECK
SOFT_LAW_RECOMMENDATION != STATUTE
UNGA_OUTCOME_DOCUMENT != TREATY
SOURCE_IDENTITY_VERIFIED != LEGAL_CONCLUSION
```

`NOTEBOOK_UPLOADS = 0`
`DERIVED_MARKDOWN_CREATED = 0`
`LEGAL_CONCLUSION = NOT_ATTEMPTED`
`UNKNOWN_PRESERVED = YES`
`AUTO_ADVANCE = NO`
'''
closeout_path.write_text(closeout, encoding='utf-8')

# Research queue R032 row.
queue_path = ROOT / '90_RESEARCH_QUEUE' / 'INITIAL_RESEARCH_QUEUE.csv'
qf, qr = read_csv(queue_path)
qr = [r for r in qr if r['work_item_id'] != 'AI-LAWS-R032']
qrow = {k: '' for k in qf}
qrow.update({
    'work_item_id': 'AI-LAWS-R032',
    'priority': 'P0',
    'workstream': 'Notebook NB01 residual official-source validation',
    'scope': 'Resolve exact A/RES/79/1 official source and recheck UNESCO Neurotechnology certified-copy access without promoting legacy repository variants',
    'state': 'COMPLETE_SUPPORT_SOURCE_VALIDATION',
    'dependencies': 'R027 COMPLETE + prior NB06 INT-004 certified-copy pin',
    'expected_output': '86_NOTEBOOKLM/downloads/NB01_RESIDUAL_OFFICIAL_SOURCE_RESULTS.csv; updated manifest/registry/ledger/upload controls; R032 closeout',
    'stop_condition': 'INT-007 exact official source resolved; INT-004 fresh GitHub access blocker preserved without invalidating prior pin; no Notebook upload or substantive R004/R011 auto-started'
})
qr.append(qrow)
write_csv(queue_path, qf, qr)

# Current context reconciliation.
ctx_path = ROOT / '00_CONTROL' / 'CURRENT_CONTEXT_AND_NEXT_ACTION.md'
ctx = ctx_path.read_text(encoding='utf-8')
ctx = replace_once(
    ctx,
    '/ R031_NB03_RESIDUAL_SOURCE_VALIDATION_COMPLETE / LEGAL_RESEARCH_ACTIVE',
    '/ R031_NB03_RESIDUAL_SOURCE_VALIDATION_COMPLETE / R032_NB01_RESIDUAL_OFFICIAL_SOURCE_VALIDATION_COMPLETE / LEGAL_RESEARCH_ACTIVE',
    'current context state header'
)
ctx = replace_once(
    ctx,
    'AI-LAWS-R031 = COMPLETE_SUPPORT_SOURCE_VALIDATION\n```',
    'AI-LAWS-R031 = COMPLETE_SUPPORT_SOURCE_VALIDATION\nAI-LAWS-R032 = COMPLETE_SUPPORT_SOURCE_VALIDATION\n```',
    'current context completed list'
)
old_nb01 = '''NB01_CORE_PDF_CONTENT_IDENTITY_VERIFIED = 6 / 8
NB01_INT007_CONTENT_IDENTITY = PARTIAL_OUTCOME_BUNDLE
NB01_INT004_PRIMARY_STATE = SUPERSEDED_SOURCE_USE_CERTIFIED_COPY_URL
NB01_NATIVE_TEXT_LAYER = 8 / 8
NB01_DERIVED_MARKDOWN_REQUIRED = 0
NB01_NOTEBOOK_UPLOADS = 0'''
new_nb01 = old_nb01 + f'''\nNB01_INT007_EXACT_OFFICIAL_A_RES_79_1_SOURCE = VERIFIED_R032
NB01_INT007_OFFICIAL_PDF_SHA256 = {INT007_SHA}
NB01_INT004_R032_FRESH_ACCESS = {'BLOCKED_403_PRIOR_PIN_PRESERVED' if status4 == '403' else 'OFFICIAL_RECORD_ACCESS_RECHECKED'}'''
ctx = replace_once(ctx, old_nb01, new_nb01, 'current context NB01 state')
old_prior_nb01 = '`NB-BATCH-NB01-20260913-001` completed source-rights/acquisition-state reconciliation. The user later added repository PDFs; R027 validated the eight core `INT-001..INT-008` binaries and corrected their repository routing semantics. Six are `CONTENT_IDENTITY_VERIFIED`, `INT-007` is `CONTENT_IDENTITY_PARTIAL` as an outcome-document bundle rather than the exact resolution file, and `INT-004` is a genuine but superseded legacy source for primary use.'
new_prior_nb01 = old_prior_nb01 + f' R032 subsequently resolved the exact official `A/RES/79/1` viewer/PDF chain (56 pages; SHA-256 `{INT007_SHA}`) while preserving the repository outcome bundle as supporting-only. The `INT-004` certified-copy pin remains authoritative, but R032 GitHub-runner access returned HTTP {status4}, so no fresh certified-copy content-body verification is claimed.'
ctx = replace_once(ctx, old_prior_nb01, new_prior_nb01, 'current context prior NB01 paragraph')
marker = '### R029 — NB08 repository incident-source validation\n'
r032_section = f'''### R032 — NB01 residual official-source validation

R032 resolved the exact official `A/RES/79/1` source while preserving the correct legacy/supporting boundaries for the existing NB01 repository files.

```text
INT007_OFFICIAL_VIEWER = {INT007_VIEWER}
INT007_OFFICIAL_PDF = {INT007_PDF}
INT007_OFFICIAL_PDF_PAGES = {INT007_PAGES}
INT007_OFFICIAL_PDF_BYTES = {INT007_BYTES}
INT007_OFFICIAL_PDF_SHA256 = {INT007_SHA}
INT007_REPOSITORY_BUNDLE_STATE = CONTENT_IDENTITY_PARTIAL_SUPPORTING_ONLY
INT004_CERTIFIED_COPY_PRIMARY_PIN = PRESERVED
INT004_R032_GITHUB_ACCESS = HTTP_{status4}
INT004_REPOSITORY_43GC_STATE = SUPERSEDED_SOURCE
NOTEBOOK_UPLOADS = 0
DERIVED_MARKDOWN_CREATED = 0
```

No new UN/UNESCO binary was committed. Exact official URLs and verification metadata were recorded instead.

'''
assert marker in ctx
ctx = ctx.replace(marker, r032_section + marker, 1)
old_lane = 'R029 completed the NB08 repository incident-source classification. The primary PDF packs NB01, NB02, NB03, NB04 and NB08 now have repository-level validation results. NB02 is `10/10` exact official EUR-Lex bytes; NB03 has seven exact-official PDF matches plus the intentionally supporting-only `US-001` White House HTML-print snapshot; NB05 has no dedicated primary binary set. No Notebook ingestion or substantive incident/legal analysis is auto-started.'
new_lane = old_lane + f' R032 also resolved the exact official `A/RES/79/1` source for NB01; the repository `INT-007` bundle remains supporting-only, and `INT-004` continues to use the prior UNESCO certified-copy pin with current GitHub-runner access state HTTP {status4}.'
ctx = replace_once(ctx, old_lane, new_lane, 'current context Notebook lane')
ctx = replace_once(
    ctx,
    'R031_NB03_US001_SUPPORTING_PRINT_STATE_PRESERVED = YES\n',
    'R031_NB03_US001_SUPPORTING_PRINT_STATE_PRESERVED = YES\n'
    'R032_NB01_INT007_EXACT_OFFICIAL_SOURCE_VERIFIED = YES\n'
    f'R032_NB01_INT007_OFFICIAL_SHA256 = {INT007_SHA}\n'
    f'R032_NB01_INT004_FRESH_GITHUB_ACCESS = HTTP_{status4}\n'
    'R032_NEW_THIRD_PARTY_BINARIES_VENDORED = 0\n',
    'current context integrity R032'
)
ctx_path.write_text(ctx, encoding='utf-8')

# Basic structural assertions after writing.
assert (D / 'NB01_RESIDUAL_OFFICIAL_SOURCE_RESULTS.csv').exists()
assert closeout_path.exists()
assert 'AI-LAWS-R032' in queue_path.read_text(encoding='utf-8')
assert 'R032_NB01_INT007_EXACT_OFFICIAL_SOURCE_VERIFIED = YES' in ctx_path.read_text(encoding='utf-8')
assert INT007_SHA in manifest_path.read_text(encoding='utf-8')
assert BATCH in ledger_path.read_text(encoding='utf-8')

print('R032_PERSIST_ASSERTIONS=PASS')
print('INT007_EXACT_OFFICIAL_SHA256=' + INT007_SHA)
print('INT007_EXACT_OFFICIAL_BYTES=' + str(INT007_BYTES))
print('INT004_ACCESS_STATE=' + int004_access_state)
print('NEW_THIRD_PARTY_BINARY_VENDORED=NO')
print('ZIP_OR_ARTIFACT_CREATED=NO')
