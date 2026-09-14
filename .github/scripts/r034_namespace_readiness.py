#!/usr/bin/env python3
import csv, hashlib, os, re, sys
from pathlib import Path
from collections import defaultdict

ROOT = Path('.').resolve()
D = ROOT / '86_NOTEBOOKLM' / 'downloads'
REG = D / 'DOWNLOADS_REGISTRY.csv'
MAN = ROOT / '86_NOTEBOOKLM' / 'NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv'
ASSIGN = ROOT / '86_NOTEBOOKLM' / 'NOTEBOOKLM_SOURCE_PACK_ASSIGNMENTS.csv'
UPLOAD_PLAN = D / 'NOTEBOOK_UPLOAD_PLAN.md'
README = D / 'README.md'

BASE_HEAD = 'dfdfd5fa868b5ddc8ecbecb0c803a2b08c0012ca'
DATE = '2026-09-14'

OUT_RENAME = D / 'RENAME_MANIFEST.csv'
OUT_INDEX = D / 'ORIGINAL_FILENAME_INDEX.csv'
OUT_LABELS = D / 'NOTEBOOK_SOURCE_LABELS.csv'
OUT_MANUAL = D / 'MANUAL_DOWNLOAD_AND_UPLOAD_REQUESTS.csv'
OUT_READY = ROOT / '86_NOTEBOOKLM' / 'NOTEBOOK_READINESS_MATRIX.csv'
OUT_CATALOG = ROOT / '86_NOTEBOOKLM' / 'SOURCE_CATALOG.md'
OUT_ASSESS = ROOT / '86_NOTEBOOKLM' / 'AI-LAWS-R034_NAMESPACE_AND_NOTEBOOK_READINESS_ASSESSMENT_2026-09-14.md'

WINDOWS_BAD = re.compile(r'[<>:"/\\|?*]')

def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1024*1024), b''):
            h.update(b)
    return h.hexdigest()

def clean(s):
    s = (s or '').strip()
    s = WINDOWS_BAD.sub('-', s)
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r'-{3,}', '--', s)
    return s.rstrip(' .')

def read_csv(path):
    with open(path, newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))

def write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader(); w.writerows(rows)

registry = read_csv(REG)
manifest = read_csv(MAN)
assignments = read_csv(ASSIGN)
manifest_by_id = {r['source_id']: r for r in manifest}
reg_by_old = {r['repo_filename']: r for r in registry}
reg_by_id = {r['manifest_source_id']: r for r in registry}
packs_by_id = defaultdict(list)
for a in assignments:
    if a['pack_id'] not in packs_by_id[a['source_id']]:
        packs_by_id[a['source_id']].append(a['pack_id'])

pdfs = sorted([p for p in D.iterdir() if p.is_file() and p.suffix.lower()=='.pdf'], key=lambda p: p.name.lower())
if len(pdfs) != len(registry):
    raise SystemExit(f'PDF/registry count mismatch: pdf={len(pdfs)} registry={len(registry)}')
unregistered = [p.name for p in pdfs if p.name not in reg_by_old]
missing = [r['repo_filename'] for r in registry if not (D/r['repo_filename']).exists()]
if unregistered or missing:
    raise SystemExit(f'unregistered={unregistered} missing={missing}')

VERSION = {
'INT-001':'CETS-225-TREATY-TEXT-2024-09-05','INT-002':'CETS-225-EXPLANATORY','INT-003':'41C-RECOMMENDATION-2021','INT-004':'43GC-LEGACY-SUPERSEDED','INT-005':'OECD-AI-PRINCIPLES-2024','INT-006':'A-RES-78-265','INT-007':'A-RES-79-1-SUPPORTING-BUNDLE','INT-008':'UN-AI-ADVISORY-2024',
'EU-001':'SNAPSHOT-2026-07-27','EU-002':'2026-1744','EU-003':'2024-2853','EU-004':'2016-C-202-02','EU-005':'2016-679','EU-006':'2022-2065','EU-007':'2023-2854','EU-008':'2022-868','EU-009':'2022-2555','EU-010':'2024-2847',
'US-001':'EO-14179-WEBPAGE-PRINT-SUPPORTING','US-002':'2025-07','US-003':'M-25-21','US-004':'M-25-22','US-005':'EO-14365-FEDERAL-REGISTER','US-006':'M-26-04','US-007':'NIST-AI-100-1','US-008':'NIST-AI-600-1',
'TR-001':'2709-SNAPSHOT','TR-002':'6698-SNAPSHOT','TR-003':'6098-SNAPSHOT','TR-004':'4721-SNAPSHOT','TR-005':'5237-SNAPSHOT','TR-006':'6502-SNAPSHOT','TR-007':'5651-SNAPSHOT','TR-008':'7545-AMENDED-7590-2026-07-31',
'INC-001':'2026-08-26-PARTIAL','INC-002':'2026-08-26','INC-003':'2026-09-10','INC-004':'2026-09-12-SUPPORTING'
}

def doc_type(r):
    sid=r['manifest_source_id']; ac=r['authority_class']; did=r['document_id'].lower()
    if sid=='INC-001': return 'COMPANY-INCIDENT-DISCLOSURE'
    if sid=='INC-002': return 'INDEPENDENT-INVESTIGATION'
    if sid=='INC-003': return 'VENDOR-THREAT-INTELLIGENCE'
    if sid=='INC-004': return 'POLICY-ESSAY'
    if ac=='CONSTITUTIONAL_TEXT': return 'CONSTITUTION'
    if ac=='STATUTE_OR_REGULATION':
        if did.startswith('directive'): return 'DIRECTIVE'
        if did.startswith('regulation'): return 'REGULATION'
        if 'executive order' in did: return 'EXECUTIVE-ORDER'
        return 'LAW'
    if ac=='TREATY_OR_INTERNATIONAL_INSTRUMENT':
        if 'a/res/' in did: return 'UN-RESOLUTION'
        return 'TREATY'
    if ac=='BINDING_COURT_DECISION': return 'COURT-DECISION'
    if ac=='REGULATORY_DECISION': return 'REGULATOR-DECISION'
    if ac=='REGULATORY_GUIDANCE':
        if 'omb' in did or sid in {'US-003','US-004','US-006'}: return 'GOVERNMENT-MEMO'
        return 'REGULATORY-GUIDANCE'
    if ac=='OFFICIAL_GUIDANCE': return 'OFFICIAL-GUIDANCE'
    if ac=='SOFT_LAW_RECOMMENDATION': return 'SOFT-LAW'
    if ac=='OFFICIAL_STANDARD_OR_FRAMEWORK': return 'FRAMEWORK'
    if ac=='TECHNICAL_STANDARD': return 'STANDARD'
    if ac=='OFFICIAL_COMPANY_STATEMENT': return 'COMPANY-INCIDENT-DISCLOSURE'
    if ac=='INDEPENDENT_REPORTING': return 'INDEPENDENT-INVESTIGATION'
    if ac=='POLICY_PROPOSAL': return 'POLICY-ESSAY'
    return 'OFFICIAL-GUIDANCE'

def institution_short(r):
    sid=r['manifest_source_id']; inst=r['institution']
    if sid.startswith('EU-'): return 'EUR-Lex'
    if sid in {'US-001','US-002','US-005'}: return 'White House'
    if sid in {'US-003','US-004','US-006'}: return 'OMB'
    if sid in {'US-007','US-008'}: return 'NIST'
    if sid.startswith('TR-'): return 'Mevzuat-Resmi Gazete'
    if sid=='INT-001': return 'Council of Europe Treaty Office'
    if sid=='INT-002': return 'Council of Europe'
    if sid in {'INT-003','INT-004'}: return 'UNESCO'
    if sid=='INT-005': return 'OECD'
    if sid in {'INT-006','INT-007','INT-008'}: return 'United Nations'
    if sid=='INC-001': return 'OpenAI'
    if sid=='INC-002': return 'METR-Redwood Research'
    if sid=='INC-003': return 'Anthropic'
    if sid=='INC-004': return 'Dario Amodei'
    return inst

def version_token(r):
    return VERSION.get(r['manifest_source_id'], clean(r['document_id']))

def filename_for(r):
    sid=r['manifest_source_id']; jur=clean(r['jurisdiction']); inst=clean(institution_short(r)); dt=doc_type(r); ver=clean(version_token(r))
    human=clean(Path(r['repo_filename']).stem)
    name=f'{sid} [{jur}] [{inst}] [{dt}] [{ver}] — {human}.pdf'
    if len(name.encode('utf-8')) > 245:
        inst = clean(inst[:24]); ver = clean(ver[:32])
        name=f'{sid} [{jur}] [{inst}] [{dt}] [{ver}] — {human}.pdf'
    if len(name.encode('utf-8')) > 245:
        raise SystemExit(f'canonical filename too long while preserving human title: {sid} {name}')
    return name

def local_readiness(r):
    sid=r['manifest_source_id']; state=r['content_identity_state']; mode=r['notebook_ingest_mode']
    if state=='SUPERSEDED_SOURCE' or 'SUPERSEDED' in mode: return 'SUPERSEDED_DO_NOT_UPLOAD'
    if sid=='INC-001': return 'HOLD'
    if sid in {'INT-007','US-001','INC-004'}: return 'READY_URL'
    if sid.startswith('TR-') or sid=='INT-001': return 'READY_WITH_CURRENTNESS_WARNING'
    if state=='CONTENT_IDENTITY_VERIFIED': return 'READY_PDF'
    if state=='CONTENT_IDENTITY_PARTIAL' and 'URL' in mode: return 'READY_URL'
    return 'HOLD'

def status_tag(r):
    st=r['content_identity_state']
    if st=='SUPERSEDED_SOURCE': return 'SUPERSEDED'
    if st=='CONTENT_IDENTITY_PARTIAL': return 'PARTIAL'
    if r['manifest_source_id'].startswith('TR-'): return 'VERIFIED-SNAPSHOT'
    if st=='CONTENT_IDENTITY_VERIFIED': return 'VERIFIED-SNAPSHOT'
    return st

rename_rows=[]; index_rows=[]; label_rows=[]
pre = {}
for p in pdfs: pre[p.name]=sha256(p)
new_names={}
for r in registry:
    new=filename_for(r)
    if new in new_names: raise SystemExit(f'duplicate canonical filename {new}')
    new_names[new]=r['manifest_source_id']
    rename_rows.append({
        'source_id':r['manifest_source_id'],'jurisdiction':r['jurisdiction'],'institution':institution_short(r),'document_type':doc_type(r),'document_id':r['document_id'],
        'original_filename':r['repo_filename'],'canonical_readable_filename':new,'pre_rename_sha256':pre[r['repo_filename']],'post_rename_sha256':'PENDING','content_changed':'PENDING',
        'verification_state':r['content_identity_state'],'notebook_packs':';'.join(packs_by_id.get(r['manifest_source_id'], [r['primary_pack']])),'rename_state':'PLANNED','notes':status_tag(r)
    })
# Rename only after complete collision/mapping validation.
for row in rename_rows:
    old=D/row['original_filename']; new=D/row['canonical_readable_filename']
    if old.name==new.name: continue
    if new.exists(): raise SystemExit(f'target exists {new}')
    old.rename(new)
for row in rename_rows:
    new=D/row['canonical_readable_filename']; post=sha256(new)
    row['post_rename_sha256']=post
    row['content_changed']='NO' if post==row['pre_rename_sha256'] else 'YES'
    row['rename_state']='RENAMED_VERIFIED' if row['content_changed']=='NO' else 'HASH_MISMATCH_STOP'
if any(r['content_changed']!='NO' for r in rename_rows):
    raise SystemExit('HASH MISMATCH: PDF content changed')

# Update registry current namespace and Notebook label, retaining all legal/source state fields.
for r in registry:
    old=r['repo_filename']; rr=next(x for x in rename_rows if x['source_id']==r['manifest_source_id'])
    r['repo_filename']=rr['canonical_readable_filename']
    r['recommended_canonical_filename']=rr['canonical_readable_filename']
    m=manifest_by_id.get(r['manifest_source_id'], {})
    human=m.get('title') or Path(old).stem
    r['recommended_notebook_label']=f"{r['manifest_source_id']} | {r['jurisdiction']} | {doc_type(r)} | {institution_short(r)} | {human} | {version_token(r)}"

write_csv(REG, list(registry[0].keys()), registry)
write_csv(OUT_RENAME, ['source_id','jurisdiction','institution','document_type','document_id','original_filename','canonical_readable_filename','pre_rename_sha256','post_rename_sha256','content_changed','verification_state','notebook_packs','rename_state','notes'], rename_rows)
for row in rename_rows:
    index_rows.append({'source_id':row['source_id'],'original_filename':row['original_filename'],'canonical_filename':row['canonical_readable_filename'],'current_repository_path':f"86_NOTEBOOKLM/downloads/{row['canonical_readable_filename']}"})
write_csv(OUT_INDEX,['source_id','original_filename','canonical_filename','current_repository_path'],index_rows)

# All-source Notebook labels/catalog.
def source_inst(m):
    sid=m['source_id']; url=m['official_url']
    if sid.startswith('EU-'): return 'EUR-Lex'
    if sid.startswith('US-'):
        if sid in {'US-003','US-004','US-006'}: return 'OMB'
        if sid in {'US-007','US-008'}: return 'NIST'
        if sid.startswith('US-'): return 'US official source'
    if sid.startswith('TR-'): return 'Türkiye official source'
    if sid.startswith('CN-'): return 'CAC/NPC/State Council'
    if sid.startswith('GB-'): return 'UK official source'
    if sid.startswith('KR-'): return 'Republic of Korea official source'
    if sid.startswith('JP-'): return 'Japan official source'
    if sid.startswith('CL-'): return 'Chile official source'
    if sid.startswith('INT-001') or sid.startswith('INT-002'): return 'Council of Europe'
    if sid in {'INT-003','INT-004'}: return 'UNESCO'
    if sid=='INT-005': return 'OECD'
    if sid.startswith('INT-'): return 'United Nations'
    if sid=='INC-001': return 'OpenAI'
    if sid=='INC-002': return 'METR / Redwood Research'
    if sid=='INC-003': return 'Anthropic'
    if sid=='INC-004': return 'Dario Amodei'
    if sid.startswith('STD-'): return 'ISO/IEC'
    return url.split('/')[2] if '://' in url else 'UNKNOWN'

def manifest_doc_type(m):
    sid=m['source_id']; ac=m['authority_class']; did=m['document_id'].lower()
    fake={'manifest_source_id':sid,'authority_class':ac,'document_id':m['document_id']}
    if sid in reg_by_id:
        return doc_type(reg_by_id[sid])
    if ac in {'NATIONAL_LAW'}: return 'LAW'
    if ac in {'ADMINISTRATIVE_REGULATION','DEPARTMENTAL_REGULATION','DEPARTMENTAL_REGULATION_OR_MEASURE','DEPARTMENTAL_REGULATORY_MEASURE'}: return 'REGULATION'
    if ac=='CONSTITUTIONAL_TEXT': return 'CONSTITUTION'
    if ac=='BINDING_COURT_DECISION': return 'COURT-DECISION'
    if ac=='TECHNICAL_STANDARD': return 'STANDARD'
    if ac=='POLICY_PROPOSAL': return 'POLICY-ESSAY'
    if ac=='OFFICIAL_GUIDANCE': return 'OFFICIAL-GUIDANCE'
    if ac=='REGULATORY_GUIDANCE': return 'REGULATORY-GUIDANCE'
    if ac=='SOFT_LAW_RECOMMENDATION': return 'SOFT-LAW'
    if ac=='STATUTE_OR_REGULATION':
        if did.startswith('directive'): return 'DIRECTIVE'
        if did.startswith('regulation'): return 'REGULATION'
        if 'executive order' in did: return 'EXECUTIVE-ORDER'
        return 'LAW'
    if ac=='TREATY_OR_INTERNATIONAL_INSTRUMENT': return 'UN-RESOLUTION' if 'a/res/' in did else 'TREATY'
    if ac=='OFFICIAL_STANDARD_OR_FRAMEWORK': return 'FRAMEWORK'
    if ac=='OFFICIAL_COMPANY_STATEMENT': return 'COMPANY-INCIDENT-DISCLOSURE'
    if ac=='INDEPENDENT_REPORTING': return 'INDEPENDENT-INVESTIGATION'
    return ac.replace('_','-')

def manifest_readiness(m):
    sid=m['source_id']; pref=m['preferred_ingest']; ver=m['verification_state']
    if sid in reg_by_id: return local_readiness(reg_by_id[sid])
    if pref=='PAYWALLED_DO_NOT_VENDOR': return 'HOLD'
    if pref=='MANUAL_DOWNLOAD_REQUIRED': return 'HOLD'
    if pref=='OFFICIAL_SOURCE_NEEDS_VERIFICATION': return 'HOLD'
    if pref=='URL_DIRECT_PREFERRED' and 'VERIFIED' in ver: return 'READY_URL'
    if pref=='PDF_DOWNLOAD_ALLOWED' and 'VERIFIED' in ver: return 'READY_URL'
    return 'READY_WITH_CURRENTNESS_WARNING' if 'VERIFIED' in ver else 'HOLD'

def related_research(sid):
    if sid.startswith('EU-'): return '20_JURISDICTIONS/EU/EU_AI_ACT_CURRENT_CONSOLIDATED_PHASED_APPLICATION_MAP_2026-09-14.md; 95_RESEARCH/EU/AI-LAWS-R003_CLOSEOUT_2026-09-14.md'
    if sid.startswith('US-'): return '20_JURISDICTIONS/US/US_AI_LAW_INVENTORY_ARCHITECTURE_2026-09-14.md; 95_RESEARCH/US/AI-LAWS-R007_CLOSEOUT_2026-09-14.md'
    if sid.startswith('TR-'): return '20_JURISDICTIONS/TR/R005_PRIMARY_SOURCE_PIN_2026-09-13.md'
    if sid.startswith('CN-'): return '20_JURISDICTIONS/CN/CN_AI_DATA_CYBER_PRIMARY_SOURCE_MAP_2026-09-14.md; 95_RESEARCH/CN/AI-LAWS-R008_CLOSEOUT_2026-09-14.md'
    if sid.startswith('GB-'): return '20_JURISDICTIONS/GB/GB_AI_DATA_ONLINE_SAFETY_PRODUCT_REGULATORY_MAP_2026-09-14.md; 95_RESEARCH/GB/AI-LAWS-R009_CLOSEOUT_2026-09-14.md'
    if sid.startswith('KR-'): return '20_JURISDICTIONS/KR/KR_AI_DATA_PRIMARY_SOURCE_MAP_2026-09-14.md; 95_RESEARCH/ASIA/AI-LAWS-R010_CLOSEOUT_2026-09-14.md'
    if sid.startswith('JP-'): return '20_JURISDICTIONS/JP/JP_AI_POLICY_DATA_PRIMARY_SOURCE_MAP_2026-09-14.md; 95_RESEARCH/ASIA/AI-LAWS-R010_CLOSEOUT_2026-09-14.md'
    if sid.startswith('CL-') or sid in {'INT-003','INT-004'}: return '50_RIGHTS/AI-LAWS-R011_HUMAN_SOVEREIGNTY_COMPARATIVE_LEGAL_MAP_2026-09-14.md; 95_RESEARCH/RIGHTS/AI-LAWS-R011_CLOSEOUT_2026-09-14.md'
    if sid in {'INT-001','INT-002'}: return '20_JURISDICTIONS/COE/CETS_225_CURRENT_TREATY_STATUS_MAP_2026-09-14.md; 95_RESEARCH/COE/AI-LAWS-R004_CLOSEOUT_2026-09-14.md'
    if sid.startswith('INC-'): return '86_NOTEBOOKLM/downloads/NB08_CONTENT_IDENTITY_RESULTS.csv; 86_NOTEBOOKLM/NOTEBOOK_UPLOAD_PLAN.md'
    return '86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv'

for m in manifest:
    sid=m['source_id']; packs=';'.join(packs_by_id.get(sid,[m['primary_pack']]))
    inst=source_inst(m); dt=manifest_doc_type(m); ver=VERSION.get(sid, clean(m['document_id']))
    label=f"{sid} | {m['jurisdiction']} | {dt} | {inst} | {m['title']} | {ver}"
    repo=f"86_NOTEBOOKLM/downloads/{reg_by_id[sid]['repo_filename']}" if sid in reg_by_id else ''
    label_rows.append({'source_id':sid,'primary_pack':m['primary_pack'],'notebook_packs':packs,'notebook_source_label':label,'preferred_ingest':m['preferred_ingest'],'repository_path':repo,'readiness':manifest_readiness(m),'verification_state':m['verification_state']})
write_csv(OUT_LABELS,['source_id','primary_pack','notebook_packs','notebook_source_label','preferred_ingest','repository_path','readiness','verification_state'],label_rows)

# Manual-download/user-assist queue. It distinguishes upload blockers from optional currentness refresh.
manual=[]
def add_manual(sid, request_class, blocker, action, notes):
    m=manifest_by_id[sid]
    suggested=''
    if sid in reg_by_id: suggested=reg_by_id[sid]['repo_filename']
    manual.append({'source_id':sid,'notebook_pack':m['primary_pack'],'title':m['title'],'official_url':m['official_url'],'current_acquisition_method':m['preferred_ingest'],'request_class':request_class,'notebook_upload_blocker':blocker,'suggested_user_action':action,'suggested_upload_filename':suggested,'target_repository_path_if_authorized':('86_NOTEBOOKLM/downloads/'+suggested if suggested else 'UPLOAD_FOR_IDENTITY_CHECK_FIRST'),'state':'OPEN_USER_ASSIST_OPTION','notes':notes})
for sid in [f'TR-00{i}' for i in range(1,9)]:
    add_manual(sid,'OPTIONAL_TO_RESOLVE_R005_LIVE_CURRENTNESS','NO','If the official portal is accessible to you, download the current official consolidated source without modifying it and provide the exact original file.','Existing repository snapshot is already Notebook-usable with currentness warning; this manual download is for live official recheck, not required for core ingestion.')
add_manual('CL-002','REQUIRED_TO_COMPLETE_NB06_CASE_LAYER','YES_FOR_CL002_CASE_LAYER','Download the exact official Supreme Court full-text decision from the pinned Poder Judicial source if the portal permits it; do not substitute a secondary copy.','Official decision identity is pinned but full text is blocked by anti-bot/CAPTCHA in this environment.')
add_manual('INC-001','REQUIRED_TO_COMPLETE_FULL_NB08_PRIMARY_DISCLOSURE','YES_FOR_FULL_NB08','If OpenAI exposes an official downloadable original for the incident disclosure, provide that exact file; otherwise preserve the official URL and do not create a browser-print as if it were an official binary.','Existing repository report is PARTIAL because official OpenAI URLs returned 403 to GitHub runner.')
add_manual('INT-004','FALLBACK_IF_NOTEBOOK_URL_IMPORT_FAILS','NO','Prefer the certified-copy UNESCO URL. Download a local copy only if Notebook URL ingestion fails and the intended use is permitted; do not vendor it to the public repo without rights review.','Current primary is the certified-copy URL; legacy 43GC repository PDF is superseded.')
add_manual('TR-009','OPTIONAL_POLICY_PDF_CAPTURE','NO','If the Ministry page exposes the official 2026-2030 action-plan PDF in your browser, provide the exact original PDF for identity checking.','Policy source is optional/nonbinding; current official identity is already verified, PDF body remains unresolved in GitHub runner.')
write_csv(OUT_MANUAL,['source_id','notebook_pack','title','official_url','current_acquisition_method','request_class','notebook_upload_blocker','suggested_user_action','suggested_upload_filename','target_repository_path_if_authorized','state','notes'],manual)

ready_rows=[
{'pack':'NB00','readiness':'READY','mode':'REPOSITORY_NATIVE','blockers':'NONE','notes':'Control/method files can be loaded directly from GitHub.'},
{'pack':'NB01','readiness':'READY_WITH_URL_ROUTING_AND_SUPERSEDED_EXCLUSION','mode':'PDF+URL','blockers':'INT-004 legacy PDF excluded; use certified-copy URL','notes':'Do not wait for all global-jurisdiction research.'},
{'pack':'NB02','readiness':'READY_PDF','mode':'10 VERIFIED OFFICIAL PDF SNAPSHOTS','blockers':'NONE_FOR_INGESTION','notes':'10/10 exact official EUR-Lex snapshots; preserve temporal/currentness labels.'},
{'pack':'NB03','readiness':'READY_MIXED','mode':'7 VERIFIED PDF + 1 LIVE URL/SUPPORTING PRINT','blockers':'NONE_FOR_CORE_INGESTION','notes':'US-001 live White House URL primary; print snapshot supporting.'},
{'pack':'NB04','readiness':'READY_WITH_CURRENTNESS_WARNING','mode':'8 VERIFIED REPOSITORY SNAPSHOTS','blockers':'NONE_FOR_INGESTION; R005 LIVE RECHECK OPEN','notes':'Material legal conclusions still require live official currentness recheck.'},
{'pack':'NB05','readiness':'READY_URL_WITH_CURRENTNESS_WARNINGS','mode':'OFFICIAL URL SETS','blockers':'NONE_FOR_BASELINE_INGESTION','notes':'China/UK/Korea/Japan URL sources; authentic-language/currentness limits preserved.'},
{'pack':'NB06','readiness':'READY_WITH_HOLD','mode':'URL+VERIFIED PDF','blockers':'CL-002 FULL TEXT HOLD FOR CASE LAYER','notes':'Core dignity/neurotech sources can be ingested now; hold Girardi/Emotiv until official full text.'},
{'pack':'NB07','readiness':'READY_REUSE_VERIFIED_SOURCES','mode':'REUSE NB02/NB03 VERIFIED SOURCES','blockers':'NONE_FOR_CORE_INGESTION','notes':'ISO standards remain metadata-only unless licensed.'},
{'pack':'NB08','readiness':'PARTIAL_READY_WITH_HOLD','mode':'INC-002/003 READY; INC-004 URL CONTEXT','blockers':'INC-001 OFFICIAL-SOURCE RECHECK FOR FULL PACK','notes':'Do not conflate company disclosure, independent investigation, vendor TI, policy essay.'},
{'pack':'NB09','readiness':'READY_METADATA_AND_REQUIREMENT_CANDIDATES','mode':'R020 CANDIDATES + METADATA','blockers':'DESTINATION_ACCEPTANCE_NOT_RUN','notes':'Not part of requested core ingestion order.'},
]
write_csv(OUT_READY,['pack','readiness','mode','blockers','notes'],ready_rows)

# Human catalog.
lines=['# AI-LAWS — Human Source Catalog','',f'**Generated:** {DATE}  ',f'**Unit:** AI-LAWS-R034  ','**Purpose:** human navigation and Notebook source selection; not legal authority.','', '```text','FILENAME = HUMAN NAVIGATION','SOURCE_CATALOG = HUMAN NAVIGATION','REGISTRY/MANIFEST = PROVENANCE','NOTEBOOK_UPLOAD != LEGAL_VERIFICATION','```','']
by_pack=defaultdict(list)
for m in manifest: by_pack[m['primary_pack']].append(m)
for pack in sorted(by_pack):
    lines += [f'## {pack}','']
    for m in sorted(by_pack[pack], key=lambda x:(x['jurisdiction'],x['source_id'])):
        sid=m['source_id']; reg=reg_by_id.get(sid); repo=(f"86_NOTEBOOKLM/downloads/{reg['repo_filename']}" if reg else '— (URL/metadata source; no repository PDF)')
        canon=(reg['repo_filename'] if reg else '—')
        packs=', '.join(packs_by_id.get(sid,[m['primary_pack']]))
        warn='Recheck currentness before material claim.'
        if sid=='INT-004': warn='Certified-copy URL primary; legacy repository PDF is SUPERSEDED.'
        elif sid=='CL-002': warn='Official full text blocked; case layer HOLD.'
        elif sid=='INC-001': warn='Official-source recheck blocked; repository file PARTIAL.'
        elif sid.startswith('TR-'): warn='Repository snapshot may be ingested with currentness warning; live official recheck remains open.'
        elif 'currentness' in m['notes'].lower() or 'recheck' in m['notes'].lower(): warn='Currentness/provision-level state must be rechecked when material.'
        lines += [f"### {sid} — {m['title']}",f"- **Canonical filename:** `{canon}`",f"- **Jurisdiction:** `{m['jurisdiction']}`",f"- **Institution:** {source_inst(m)}",f"- **Document type:** `{manifest_doc_type(m)}`",f"- **Authority class:** `{m['authority_class']}`",f"- **Document ID:** `{m['document_id']}`",f"- **Binding state:** {m['binding_state']}",f"- **Verification state:** `{m['verification_state']}`",f"- **Readiness:** `{manifest_readiness(m)}`",f"- **Currentness warning:** {warn}",f"- **Official URL:** {m['official_url']}",f"- **Repository PDF path:** `{repo}`",f"- **Notebook packs:** `{packs}`",f"- **Related AI-LAWS research:** `{related_research(sid)}`",f"- **Important limitations:** {m['notes']}",'']
OUT_CATALOG.write_text('\n'.join(lines)+'\n', encoding='utf-8')

# Current README policy supersedes prior no-rename rule with this controlled one-time namespace normalization.
text=README.read_text(encoding='utf-8')
start=text.index('## Existing PDF naming')
end=text.index('## State tags')
replacement='''## Existing PDF naming — R034 controlled namespace\n\nR034 supersedes the earlier appearance-only no-rename preference for one controlled repository-wide namespace normalization. Existing PDFs may be renamed only when a pre/post SHA-256 equality check proves binary content is unchanged.\n\nCanonical readable filename format:\n\n```text\n<SOURCE_ID> [<JURISDICTION>] [<INSTITUTION>] [<DOCUMENT_TYPE>] [<VERSION_OR_DOCUMENT_ID>] — <ORIGINAL_HUMAN_TITLE>.pdf\n```\n\nMandatory invariants:\n\n```text\nORIGINAL_HUMAN_TITLE = PRESERVE\nPRE_RENAME_SHA256 == POST_RENAME_SHA256\nPDF_CONTENT_MODIFIED = NO\nSOURCE_ID_CHANGED = NO\nAUTHORITY_CLASS_CHANGED = NO\n```\n\nUse `RENAME_MANIFEST.csv` for the audited mapping and `ORIGINAL_FILENAME_INDEX.csv` for backward lookup. The shorter Notebook title is stored in `NOTEBOOK_SOURCE_LABELS.csv`.\n\n'''
README.write_text(text[:start]+replacement+text[end:], encoding='utf-8')

up=UPLOAD_PLAN.read_text(encoding='utf-8')
up=up.replace('3. rename only the **local Notebook-upload copy** using `recommended_canonical_filename` if useful;','3. preserve the R034 canonical readable repository filename; use `NOTEBOOK_SOURCE_LABELS.csv` for a shorter Notebook title when useful;')
UPLOAD_PLAN.write_text(up, encoding='utf-8')

counts=defaultdict(int)
for r in registry: counts[r['content_identity_state']]+=1
assessment=f'''# AI-LAWS-R034 — Namespace and Notebook Readiness Assessment\n\n**DATE:** {DATE}\n**BASE_HEAD:** `{BASE_HEAD}`\n**UNIT_TYPE:** `HUMAN_READABLE_NAMESPACE_AND_NOTEBOOK_READINESS`\n\n## Current repository PDF state\n\n```text\nREPOSITORY_PDF_COUNT = {len(pdfs)}\nCONTENT_IDENTITY_VERIFIED_COUNT = {counts['CONTENT_IDENTITY_VERIFIED']}\nCONTENT_IDENTITY_PARTIAL_COUNT = {counts['CONTENT_IDENTITY_PARTIAL']}\nSUPERSEDED_COUNT = {counts['SUPERSEDED_SOURCE']}\nPDF_FILES_RENAMED = {len(rename_rows)}\nPDF_FILES_CONTENT_CHANGED = 0\n```\n\n## Notebook readiness\n\n```text\nNB00_READY = READY\nNB01_READY = READY_WITH_URL_ROUTING_AND_SUPERSEDED_EXCLUSION\nNB02_READY = READY_PDF_10_OF_10\nNB03_READY = READY_MIXED_7_PDF_PLUS_1_URL\nNB04_READY = READY_WITH_CURRENTNESS_WARNING_8_OF_8_SNAPSHOTS\nNB05_READY = READY_URL_WITH_CURRENTNESS_WARNINGS\nNB06_READY = READY_WITH_HOLD_CL002\nNB07_READY = READY_REUSE_VERIFIED_SOURCES\nNB08_READY = PARTIAL_READY_HOLD_INC001\nCORE_NOTEBOOK_INGESTION_READY = YES\n```\n\n## What actually blocks upload\n\n- `CL-002` blocks the **case layer** of NB06, not the rest of NB06.\n- `INC-001` blocks a **fully verified NB08 pack**, not ingestion of INC-002/INC-003 or other core packs.\n- `R005` live Türkiye currentness recheck does **not** block NB04 snapshot ingestion when currentness warnings are retained.\n- Open worldwide jurisdiction research does **not** block core Notebook ingestion.\n- Paywalled ISO full text remains metadata-only and is not an ingestion blocker.\n\n## Open items that do not prevent core Notebook upload\n\n- Türkiye live official exact-byte/currentness recheck (`R005`).\n- `INT-004` GitHub-runner 403; certified-copy official URL remains primary.\n- `TR-009` optional 2026–2030 policy PDF body.\n- Currentness/provision-level refresh work in jurisdiction-specific research.\n- R019 incident corpus, which remains explicit-only and is not required to begin pack ingestion.\n\n## Remaining workflow size\n\nThe source-normalization problem is finite: this unit covers {len(pdfs)} repository PDFs plus the manifest/catalog layer. After R034, the next distinct operation is Notebook pack ingestion/locator testing, not another bulk PDF-to-Markdown conversion campaign.\n\n```text\nOPEN_RESEARCH != NOTEBOOK_UPLOAD_BLOCKER\nCORE_NOTEBOOK_INGESTION_READY = YES\nNEXT_BOUNDED_UNIT = AI-LAWS NOTEBOOK PACK INGESTION\nAUTO_ADVANCE = NO\n```\n'''
OUT_ASSESS.write_text(assessment, encoding='utf-8')

print(f'REPOSITORY_PDF_COUNT={len(pdfs)}')
print(f"CONTENT_IDENTITY_VERIFIED_COUNT={counts['CONTENT_IDENTITY_VERIFIED']}")
print(f"CONTENT_IDENTITY_PARTIAL_COUNT={counts['CONTENT_IDENTITY_PARTIAL']}")
print(f"SUPERSEDED_COUNT={counts['SUPERSEDED_SOURCE']}")
print(f'PDF_FILES_RENAMED={len(rename_rows)}')
print('PDF_FILES_CONTENT_CHANGED=0')
print(f'MANIFEST_SOURCE_COUNT={len(manifest)}')
print(f'MANUAL_DOWNLOAD_REQUEST_ROWS={len(manual)}')
print('CORE_NOTEBOOK_INGESTION_READY=YES')
print('AUTO_ADVANCE=NO')
