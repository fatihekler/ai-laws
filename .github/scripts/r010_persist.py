from pathlib import Path
import csv
import io

ROOT = Path('.')
DATE = '2026-09-14'
BATCH = 'NB-BATCH-NB05-20260914-003'

SOURCES = [
    {
        'source_id':'KR-001','jurisdiction':'KR','title':'인공지능 발전과 신뢰 기반 조성 등에 관한 기본법','domain':'AI_GOVERNANCE',
        'document_id':'law.go.kr lsId=014820 / lsiSeq=282791 / current selector efYd=20260721 / current revision ancNo=21311 ancYd=20260120',
        'authority':'Republic of Korea National Law Information Center','authority_class':'STATUTE_OR_REGULATION',
        'binding_state':'binding national statute; provision-level amendment/effective-date chain not normalized by R010',
        'url':'https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=282791&chrClsCd=010202&urlMode=lsInfoP&efYd=20260721&ancYnChk=0',
        'date':'2026-07-21','currentness':'OFFICIAL_CURRENT_PAGE_NWYN_Y_CURRENT_SELECTOR_20260721_AMENDMENT_CHAIN_OPEN',
        'language':'Korean','translation':'AUTHENTIC_KOREAN_CONTROLS_NO_AUTHORITATIVE_ENGLISH_TRANSLATION_PINNED_R010',
        'requirement':'REQUIRED','reason':'Republic of Korea AI framework-law baseline','priority':'P1',
        'notes':'Official current page identity verified. Hidden metadata: lsId 014820; lsiSeq 282791; current revision ancNo 21311; ancYd 2026-01-20; nwYn=Y. Name wrapper selected efYd 2026-07-21, while the body also exposed a 2026-01-22 base-effect signal. R010 does not collapse these into one universal commencement date and does not claim ancNo 21311 is the original enactment number.'
    },
    {
        'source_id':'KR-002','jurisdiction':'KR','title':'인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 시행령','domain':'AI_GOVERNANCE_SUBORDINATE_LEGISLATION',
        'document_id':'law.go.kr lsId=015032 / lsiSeq=288781 / current selector efYd=20260820 / current revision ancNo=36580 ancYd=20260818',
        'authority':'Republic of Korea National Law Information Center','authority_class':'STATUTE_OR_REGULATION',
        'binding_state':'binding Presidential Decree subordinate legislation; provision-level application not normalized by R010',
        'url':'https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=288781&chrClsCd=010202&urlMode=lsInfoP&efYd=20260820&ancYnChk=0',
        'date':'2026-08-20','currentness':'OFFICIAL_CURRENT_PAGE_NWYN_Y_CURRENT_SELECTOR_20260820',
        'language':'Korean','translation':'AUTHENTIC_KOREAN_CONTROLS_NO_AUTHORITATIVE_ENGLISH_TRANSLATION_PINNED_R010',
        'requirement':'REQUIRED','reason':'Current subordinate implementation layer for Korea AI Basic Act','priority':'P1',
        'notes':'Official current page identity verified. Hidden metadata: lsId 015032; lsiSeq 288781; current revision ancNo 36580; ancYd 2026-08-18; nwYn=Y; current selector 2026-08-20. R010 does not infer a concrete duty or liability consequence from source identity.'
    },
    {
        'source_id':'KR-003','jurisdiction':'KR','title':'개인정보 보호법','domain':'DATA_PROTECTION',
        'document_id':'law.go.kr lsId=011357 / lsiSeq=283839 / current selector efYd=20260911 / current revision ancNo=21445 ancYd=20260310',
        'authority':'Republic of Korea National Law Information Center','authority_class':'STATUTE_OR_REGULATION',
        'binding_state':'binding national data-protection statute; AI-specific application depends on facts and provisions',
        'url':'https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=283839&chrClsCd=010202&urlMode=lsInfoP&efYd=20260911&ancYnChk=0',
        'date':'2026-09-11','currentness':'OFFICIAL_CURRENT_PAGE_NWYN_Y_CURRENT_SELECTOR_20260911',
        'language':'Korean','translation':'AUTHENTIC_KOREAN_CONTROLS_NO_AUTHORITATIVE_ENGLISH_TRANSLATION_PINNED_R010',
        'requirement':'RECOMMENDED','reason':'Current Korean personal-data baseline relevant to AI processing','priority':'P1',
        'notes':'Official current page identity verified. Hidden metadata: lsId 011357; lsiSeq 283839; current revision ancNo 21445; ancYd 2026-03-10; nwYn=Y; current selector 2026-09-11. No AI-specific breach or compliance conclusion is inferred.'
    },
    {
        'source_id':'JP-001','jurisdiction':'JP','title':'人工知能関連技術の研究開発及び活用の推進に関する法律','domain':'AI_GOVERNANCE',
        'document_id':'e-Gov law 507AC0000000053 / 令和七年法律第五十三号 / current revision 507AC0000000053_20250901_000000000000000',
        'authority':'Japan e-Gov Laws / Cabinet Office','authority_class':'STATUTE_OR_REGULATION',
        'binding_state':'binding national statute; e-Gov current revision status CurrentEnforced',
        'url':'https://laws.e-gov.go.jp/law/507AC0000000053',
        'date':'2025-09-01','currentness':'EGOV_CURRENT_ENFORCED_FULL_EFFECTIVE_20250901_CABINET_OFFICE_CONFIRMED',
        'language':'Japanese','translation':'AUTHENTIC_JAPANESE_CONTROLS_NO_AUTHORITATIVE_ENGLISH_TRANSLATION_PINNED_R010',
        'requirement':'REQUIRED','reason':'Japan AI Act binding-law baseline','priority':'P1',
        'notes':'Official e-Gov API verified law number Reiwa 7 Act No. 53, promulgation 2025-06-04, current revision effective 2025-09-01, status CurrentEnforced. Cabinet Office official AI Act page states partial effect from 2025-06-04 and full effect from 2025-09-01. R010 does not convert statutory principles into a concrete breach/liability finding.'
    },
    {
        'source_id':'JP-002','jurisdiction':'JP','title':'個人情報の保護に関する法律','domain':'DATA_PROTECTION',
        'document_id':'e-Gov law 415AC0000000057 / current revision 415AC0000000057_20260717_508AC0000000062',
        'authority':'Japan e-Gov Laws','authority_class':'STATUTE_OR_REGULATION',
        'binding_state':'binding national data-protection statute; current revision status CurrentEnforced',
        'url':'https://laws.e-gov.go.jp/law/415AC0000000057',
        'date':'2026-07-17','currentness':'EGOV_CURRENT_ENFORCED_REVISION_20260717',
        'language':'Japanese','translation':'AUTHENTIC_JAPANESE_CONTROLS_NO_AUTHORITATIVE_ENGLISH_TRANSLATION_PINNED_R010',
        'requirement':'RECOMMENDED','reason':'Current Japanese personal-data baseline relevant to AI processing','priority':'P1',
        'notes':'Official e-Gov API verified original law number Heisei 15 Act No. 57 and current revision 2026-07-17 under Reiwa 8 Act No. 62; status CurrentEnforced. No AI-specific application conclusion is inferred.'
    },
    {
        'source_id':'JP-003','jurisdiction':'JP','title':'人工知能基本計画（第Ⅱ期）','domain':'AI_POLICY',
        'document_id':'Cabinet Office AI Basic Plan Phase II / Cabinet decision 2026-07-14',
        'authority':'Japan Cabinet Office','authority_class':'OFFICIAL_GUIDANCE',
        'binding_state':'Cabinet-adopted policy plan; nonbinding as policy plan; not statute',
        'url':'https://www8.cao.go.jp/cstp/ai/ai_plan/ai_plan.html',
        'date':'2026-07-14','currentness':'OFFICIAL_CURRENT_PHASE_II_POLICY_PLAN_CABINET_DECISION_20260714',
        'language':'Japanese','translation':'AUTHENTIC_JAPANESE_CONTROLS_NO_AUTHORITATIVE_ENGLISH_TRANSLATION_PINNED_R010',
        'requirement':'REQUIRED','reason':'Current Japanese national AI policy-plan layer separated from binding law','priority':'P1',
        'notes':'Cabinet Office AI hub states the Phase II AI Basic Plan was decided by Cabinet on 2026-07-14. The prior first plan dated 2025-12-23 remains historical context. Policy plan is not treated as statute.'
    },
    {
        'source_id':'JP-004','jurisdiction':'JP','title':'人工知能関連技術の研究開発及び活用の適正性確保に関する指針','domain':'AI_GOVERNANCE_GUIDANCE',
        'document_id':'Cabinet Office / AI Strategy Headquarters guideline decision 2025-12-19',
        'authority':'Japan Cabinet Office / AI Strategy Headquarters','authority_class':'OFFICIAL_GUIDANCE',
        'binding_state':'official AI-governance guideline; nonbinding as guidance unless a separate legal rule incorporates a requirement',
        'url':'https://www8.cao.go.jp/cstp/ai/ai_guideline/ai_guideline.html',
        'date':'2025-12-19','currentness':'OFFICIAL_GUIDELINE_HEADQUARTERS_DECISION_20251219_CURRENT_HUB_RECHECKED_20260914',
        'language':'Japanese','translation':'AUTHENTIC_JAPANESE_CONTROLS_NO_AUTHORITATIVE_ENGLISH_TRANSLATION_PINNED_R010',
        'requirement':'RECOMMENDED','reason':'Official appropriateness-guideline layer required to separate guidance from statute','priority':'P1',
        'notes':'Cabinet Office page states Headquarters decision 2025-12-19 and maintains a current cross-ministry AI guideline inventory. Guidance is not converted into statutory duty.'
    },
    {
        'source_id':'JP-005','jurisdiction':'JP','title':'AI事業者ガイドライン Ver.1.2','domain':'AI_BUSINESS_GUIDANCE',
        'document_id':'AI Guidelines for Business Ver.1.2 / MIC-METI current listing 2026-03-31',
        'authority':'Japan Ministry of Internal Affairs and Communications / Ministry of Economy Trade and Industry','authority_class':'REGULATORY_GUIDANCE',
        'binding_state':'official cross-ministry business guidance; nonbinding as guidance; not statute',
        'url':'https://www.soumu.go.jp/main_sosiki/kenkyu/ai_network/02ryutsu20_04000019.html',
        'date':'2026-03-31','currentness':'MIC_OFFICIAL_PAGE_VERIFIED_VERSION_1_2_20260331_CABINET_OFFICE_CURRENT_HUB_LISTED',
        'language':'Japanese with official English guideline links','translation':'OFFICIAL_ENGLISH_TITLES_LINKED_ON_MIC_PAGE_FULL_TRANSLATION_LEGAL_CONTROL_NOT_NORMALIZED_R010',
        'requirement':'RECOMMENDED','reason':'Current cross-ministry AI business guidance baseline','priority':'P1',
        'notes':'Cabinet Office current guideline hub links both MIC and METI sources and marks the AI Guidelines for Business at R8.3. MIC official page was reachable and showed Ver.1.2 / 2026-03-31 plus official English titles. METI counterpart returned HTTP 403 to the GitHub runner; this is preserved as access state, not source absence.'
    },
]

MANIFEST = ROOT/'86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv'
PACK = ROOT/'86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_PACK_ASSIGNMENTS.csv'
LEDGER = ROOT/'86_NOTEBOOKLM/NOTEBOOKLM_ACQUISITION_AND_VALIDATION_LEDGER.csv'
REGISTRY = ROOT/'20_JURISDICTIONS/JURISDICTION_RESEARCH_REGISTRY.csv'
QUEUE = ROOT/'90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv'
CONTEXT = ROOT/'00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md'
DOWNLOAD_LIST = ROOT/'86_NOTEBOOKLM/NOTEBOOKLM_DOWNLOAD_AND_UPLOAD_LIST.md'


def read_csv(path):
    with path.open('r', encoding='utf-8-sig', newline='') as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def write_csv(path, fields, rows):
    buf = io.StringIO(newline='')
    w = csv.DictWriter(buf, fieldnames=fields, extrasaction='ignore', lineterminator='\n')
    w.writeheader(); w.writerows(rows)
    path.write_text(buf.getvalue(), encoding='utf-8')


def upsert(rows, keys, newrow):
    wanted = tuple(newrow.get(k,'') for k in keys)
    for i,row in enumerate(rows):
        if tuple(row.get(k,'') for k in keys) == wanted:
            merged=dict(row); merged.update(newrow); rows[i]=merged; return
    rows.append(newrow)

# Jurisdiction artifacts
for code in ['KR','JP']:
    (ROOT/f'20_JURISDICTIONS/{code}').mkdir(parents=True, exist_ok=True)
(ROOT/'95_RESEARCH/ASIA').mkdir(parents=True, exist_ok=True)

inv_fields=['source_id','title','domain','authority','authority_class','official_url','document_id','current_effective_or_policy_date','binding_state','currentness_state','authentic_language','translation_state','primary_source_state','notebook_pack','caveat']
for code in ['KR','JP']:
    rows=[]
    for s in [x for x in SOURCES if x['jurisdiction']==code]:
        rows.append({
            'source_id':s['source_id'],'title':s['title'],'domain':s['domain'],'authority':s['authority'],'authority_class':s['authority_class'],
            'official_url':s['url'],'document_id':s['document_id'],'current_effective_or_policy_date':s['date'],'binding_state':s['binding_state'],
            'currentness_state':s['currentness'],'authentic_language':s['language'],'translation_state':s['translation'],
            'primary_source_state':'VERIFIED_OFFICIAL_SOURCE_IDENTITY_R010','notebook_pack':'NB05','caveat':s['notes']
        })
    write_csv(ROOT/f'20_JURISDICTIONS/{code}/{code}_PRIMARY_SOURCE_INVENTORY_2026-09-14.csv',inv_fields,rows)

matrix_fields=['source_id','layer','official_identity_state','current_date_state','binding_state','translation_control','r010_use_state','required_next_recheck']
for code in ['KR','JP']:
    rows=[]
    for s in [x for x in SOURCES if x['jurisdiction']==code]:
        if s['authority_class']=='STATUTE_OR_REGULATION':
            nxt='Recheck exact provision text, amendment chain, commencement/application and sector-specific interaction before a material legal-duty claim.'
        else:
            nxt='Recheck replacement/update status and underlying binding-law locator before treating guidance or policy as legally operative.'
        rows.append({'source_id':s['source_id'],'layer':s['domain'],'official_identity_state':'VERIFIED_R010','current_date_state':s['currentness'],'binding_state':s['binding_state'],'translation_control':s['translation'],'r010_use_state':'ELIGIBLE_WITH_STATED_LIMITS','required_next_recheck':nxt})
    write_csv(ROOT/f'20_JURISDICTIONS/{code}/{code}_CURRENTNESS_AND_BINDING_STATE_MATRIX.csv',matrix_fields,rows)

kr_md='''# AI-LAWS — Republic of Korea AI / Data Primary-Source Map

**WORK_ITEM:** `AI-LAWS-R010`
**RESEARCH_DATE:** 2026-09-14
**LEVEL:** L1/L2 current-source and binding-state baseline
**LEGAL_ADVICE:** NO
**AUTO_ADVANCE:** NO

## Controlled source set

R010 admits three official current `law.go.kr` sources:

- `KR-001` — `인공지능 발전과 신뢰 기반 조성 등에 관한 기본법`;
- `KR-002` — `인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 시행령`;
- `KR-003` — `개인정보 보호법`.

All three current detail pages exposed `nwYn=Y`. Exact current identifiers/date selectors are preserved in `KR_PRIMARY_SOURCE_INVENTORY_2026-09-14.csv`.

## Current-state controls

```text
KR001_LSID = 014820
KR001_LSISEQ = 282791
KR001_CURRENT_WRAPPER_SELECTOR = 2026-07-21
KR001_CURRENT_REVISION_ANCNO = 21311
KR001_CURRENT_REVISION_ANCYD = 2026-01-20
KR001_BODY_BASE_EFFECT_SIGNAL = 2026-01-22
KR001_AMENDMENT_CHAIN_NORMALIZED = NO
KR002_LSISEQ = 288781
KR002_CURRENT_SELECTOR = 2026-08-20
KR003_LSISEQ = 283839
KR003_CURRENT_SELECTOR = 2026-09-11
```

The 2026-07-21 selector and 2026-01-22 body signal for `KR-001` are not collapsed into one universal commencement date. `ancNo=21311` is recorded as current-revision metadata and is not represented as the original enactment number.

## Binding / policy boundary

`KR-001..KR-003` are binding-law sources. R010 did not pin a separate current Korean national AI policy-plan source to the same verification standard.

```text
KOREA_CURRENT_AI_POLICY_PLAN_SOURCE = NOT_PINNED_R010
BINDING_LAW_SOURCE_VERIFIED != POLICY_PLAN_SOURCE_VERIFIED
```

This open policy-source lane does not reduce the verified identity of the three binding sources and does not establish that no current Korean AI policy exists.

## Translation and legal-conclusion boundary

Authentic Korean text controls. R010 did not admit an authoritative English translation as primary legal authority.

```text
TRANSLATION_CONTROL = AUTHENTIC_KOREAN_PRIMARY_TEXT
SOURCE_IDENTITY != DUTY_APPLICATION
DUTY_APPLICATION != BREACH
BREACH != CAUSATION
CASE_LAW = NOT_ATTEMPTED
LIABILITY_CONCLUSION = NOT_ATTEMPTED
NOTEBOOK_UPLOADS = 0
NEW_BINARY_DOWNLOADS = 0
AUTO_ADVANCE = NO
```
'''
(ROOT/'20_JURISDICTIONS/KR/KR_AI_DATA_PRIMARY_SOURCE_MAP_2026-09-14.md').write_text(kr_md,encoding='utf-8')

jp_md='''# AI-LAWS — Japan AI / Policy / Data Primary-Source Map

**WORK_ITEM:** `AI-LAWS-R010`
**RESEARCH_DATE:** 2026-09-14
**LEVEL:** L1/L2 current-source and binding-state baseline
**LEGAL_ADVICE:** NO
**AUTO_ADVANCE:** NO

## Controlled source set

R010 admits five official Japanese sources:

- `JP-001` — AI Act, `人工知能関連技術の研究開発及び活用の推進に関する法律`;
- `JP-002` — APPI, `個人情報の保護に関する法律`;
- `JP-003` — `人工知能基本計画（第Ⅱ期）`;
- `JP-004` — AI R&D/use appropriateness guideline;
- `JP-005` — `AI事業者ガイドライン Ver.1.2`.

## Binding-law layer

Official e-Gov structured data verified:

```text
JP001_LAW_ID = 507AC0000000053
JP001_LAW_NUMBER = 令和七年法律第五十三号
JP001_PROMULGATED = 2025-06-04
JP001_CURRENT_REVISION_EFFECTIVE = 2025-09-01
JP001_CURRENT_REVISION_STATUS = CurrentEnforced
JP001_FULL_EFFECTIVE = 2025-09-01
JP002_LAW_ID = 415AC0000000057
JP002_ORIGINAL_LAW_NUMBER = 平成十五年法律第五十七号
JP002_CURRENT_REVISION_EFFECTIVE = 2026-07-17
JP002_CURRENT_REVISION_STATUS = CurrentEnforced
```

Cabinet Office independently states the AI Act was partially effective from 2025-06-04 and fully effective from 2025-09-01.

## Policy and guidance layer

```text
JP003_AI_BASIC_PLAN_PHASE_II_CABINET_DECISION = 2026-07-14
JP004_APPROPRIATENESS_GUIDELINE_HEADQUARTERS_DECISION = 2025-12-19
JP005_AI_GUIDELINES_FOR_BUSINESS_VERSION = 1.2
JP005_CURRENT_PAGE_DATE = 2026-03-31
JP005_MIC_ACCESS = HTTP_200
JP005_METI_COUNTERPART_ACCESS = HTTP_403_GITHUB_RUNNER
```

`JP-003..JP-005` are not statutes. The Cabinet Office current hub distinguishes the Act, the Phase II Basic Plan and guideline layers. The MIC page for Business Guidelines Ver.1.2 was reachable; the METI counterpart returned 403 from the runner, which is an access state rather than source absence.

## Translation and legal-conclusion boundary

Authentic Japanese text controls for legal meaning. Official English titles/links do not replace Japanese primary text unless a source is expressly authoritative for that purpose.

```text
POLICY_PLAN != STATUTE
OFFICIAL_GUIDANCE != STATUTE
RUNNER_HTTP_403 != SOURCE_ABSENCE
SOURCE_IDENTITY != DUTY_APPLICATION
CASE_LAW = NOT_ATTEMPTED
LIABILITY_CONCLUSION = NOT_ATTEMPTED
NOTEBOOK_UPLOADS = 0
NEW_BINARY_DOWNLOADS = 0
AUTO_ADVANCE = NO
```
'''
(ROOT/'20_JURISDICTIONS/JP/JP_AI_POLICY_DATA_PRIMARY_SOURCE_MAP_2026-09-14.md').write_text(jp_md,encoding='utf-8')

# Registry
fields,rows=read_csv(REGISTRY)
for row in rows:
    if row['jurisdiction_id']=='KR':
        row['research_state']='AI_BASIC_ACT_DECREE_PIPA_L1_L2_CURRENT_BASELINE_COMPLETE_POLICY_PLAN_SOURCE_OPEN'
        row['notes']='R010 verified current official law.go.kr identities for the AI Basic Act, its Enforcement Decree and PIPA. Current revision/date selectors are pinned; authentic Korean controls. A separate current national AI policy-plan source was not pinned in R010. Amendment chains, sector application, case law and liability remain open.'
    if row['jurisdiction_id']=='JP':
        row['research_state']='AI_ACT_APPI_POLICY_GUIDANCE_L1_L2_CURRENT_BASELINE_COMPLETE'
        row['notes']='R010 verified current e-Gov AI Act/APPI law states and separated them from the Cabinet Office Phase II AI Basic Plan and official guidance layers. Authentic Japanese controls. Sector application, case law and liability remain open.'
write_csv(REGISTRY,fields,rows)

# Queue
fields,rows=read_csv(QUEUE)
for row in rows:
    if row['work_item_id']=='AI-LAWS-R010':
        row['state']='COMPLETE_RESEARCH_BASELINE_L1_L2_CURRENTNESS_OPEN'
        row['expected_output']='20_JURISDICTIONS/KR/KR_AI_DATA_PRIMARY_SOURCE_MAP_2026-09-14.md; 20_JURISDICTIONS/KR/KR_PRIMARY_SOURCE_INVENTORY_2026-09-14.csv; 20_JURISDICTIONS/JP/JP_AI_POLICY_DATA_PRIMARY_SOURCE_MAP_2026-09-14.md; 20_JURISDICTIONS/JP/JP_PRIMARY_SOURCE_INVENTORY_2026-09-14.csv; 95_RESEARCH/ASIA/AI-LAWS-R010_CLOSEOUT_2026-09-14.md'
        row['stop_condition']='KR/JP L1/L2 current source and binding-state baseline complete; Korea separate current policy-plan source remains open; stop before sector application, exhaustive negative findings, case law or liability conclusions'
write_csv(QUEUE,fields,rows)

# Manifest
fields,rows=read_csv(MANIFEST)
for s in SOURCES:
    upsert(rows,['source_id'],{
        'source_id':s['source_id'],'primary_pack':'NB05','jurisdiction':s['jurisdiction'],'title':s['title'],'document_id':s['document_id'],
        'authority_class':s['authority_class'],'binding_state':s['binding_state'],'official_url':s['url'],'preferred_ingest':'URL_DIRECT_PREFERRED',
        'priority':s['priority'],'verification_state':'VERIFIED_OFFICIAL_CURRENT_SOURCE_R010','last_verified':DATE,
        'rights_or_use_state':'OFFICIAL_PUBLIC_URL_NO_REPO_VENDORING_ATTEMPTED','notes':s['notes']
    })
write_csv(MANIFEST,fields,rows)

# Pack assignments
fields,rows=read_csv(PACK)
for s in SOURCES:
    upsert(rows,['pack_id','source_id'],{'pack_id':'NB05','source_id':s['source_id'],'requirement':s['requirement'],'reason':s['reason']})
write_csv(PACK,fields,rows)

# Acquisition ledger
fields,rows=read_csv(LEDGER)
for s in SOURCES:
    if s['source_id']=='JP-001':
        adoption=''; publication='2025-06-04'; entry='2025-06-04_PARTIAL'; application='2025-09-01_FULL'
    elif s['source_id']=='JP-002':
        adoption=''; publication='2003-05-30_ORIGINAL'; entry='NOT_NORMALIZED_R010'; application='2026-07-17_CURRENT_REVISION'
    elif s['source_id']=='JP-003':
        adoption='2026-07-14'; publication='2026-07-14'; entry='NOT_APPLICABLE_POLICY'; application='NOT_APPLICABLE_POLICY'
    elif s['source_id']=='JP-004':
        adoption='2025-12-19'; publication='2025-12-19'; entry='NOT_APPLICABLE_GUIDANCE'; application='NOT_APPLICABLE_GUIDANCE'
    elif s['source_id']=='JP-005':
        adoption=''; publication='2026-03-31'; entry='NOT_APPLICABLE_GUIDANCE'; application='NOT_APPLICABLE_GUIDANCE'
    elif s['source_id']=='KR-001':
        adoption='UNKNOWN_ORIGINAL_NOT_NORMALIZED'; publication='2026-01-20_CURRENT_REVISION'; entry='BASE_EFFECT_SIGNAL_2026-01-22'; application='CURRENT_SELECTOR_2026-07-21'
    elif s['source_id']=='KR-002':
        adoption=''; publication='2026-08-18_CURRENT_REVISION'; entry='2026-08-20_CURRENT_SELECTOR'; application='2026-08-20_CURRENT_SELECTOR'
    else:
        adoption=''; publication='2026-03-10_CURRENT_REVISION'; entry='2026-09-11_CURRENT_SELECTOR'; application='2026-09-11_CURRENT_SELECTOR'
    upsert(rows,['batch_id','source_id'],{
        'batch_id':BATCH,'source_id':s['source_id'],'notebook_pack':'NB05','jurisdiction':s['jurisdiction'],'title':s['title'],'document_id':s['document_id'],
        'issuing_authority':s['authority'],'authority_class':s['authority_class'],'binding_state':s['binding_state'],'official_url':s['url'],'retrieval_date':DATE,
        'version_state':s['currentness'],'adoption_date':adoption,'publication_date':publication,'entry_into_force_date':entry,'application_date':application,
        'authentic_language':s['language'],'translation_state':s['translation'],'rights_state':'OFFICIAL_PUBLIC_URL_NO_REPO_VENDORING_ATTEMPTED',
        'acquisition_method':'URL_DIRECT_PREFERRED','local_filename_or_url':s['url'],'sha256':'','byte_size':'','content_type':'official web/API source; no local binary',
        'content_identity_checked':'WEB_IDENTITY_AND_CURRENT_STATE_VERIFIED_NO_LOCAL_FILE_R010','notebook_name':'','notebook_ingest_date':'','notebook_ingest_state':'NOT_RUN',
        'notebook_locator_test':'NOT_RUN','primary_source_recheck_state':'R010_OFFICIAL_SOURCE_RECHECK_COMPLETE_WITH_STATED_LIMITS',
        'refresh_trigger':'official amendment/revision; replacement policy/guideline; material legal claim; Notebook ingestion','human_review_required':'NO_FOR_SOURCE_IDENTITY_YES_FOR_MATERIAL_LEGAL_CONCLUSION',
        'notes':s['notes']+' No binary vendored; no SHA-256 or exact-byte claim; Notebook ingestion not performed.'
    })
write_csv(LEDGER,fields,rows)

# Notebook download/upload list: URL-only section
text=DOWNLOAD_LIST.read_text(encoding='utf-8')
marker='### R010 — NB05 Republic of Korea + Japan official URL source set'
if marker not in text:
    block='''\n\n### R010 — NB05 Republic of Korea + Japan official URL source set\n\nR010 adds URL-direct sources only; no binary download is required for this bounded unit.\n\n- `KR-001` Korea AI Basic Act current official law.go.kr state\n- `KR-002` Korea AI Basic Act Enforcement Decree current official law.go.kr state\n- `KR-003` Korea PIPA current official law.go.kr state\n- `JP-001` Japan AI Act current e-Gov law\n- `JP-002` Japan APPI current e-Gov law\n- `JP-003` Japan AI Basic Plan Phase II, Cabinet decision 2026-07-14\n- `JP-004` Japan AI appropriateness guideline, Headquarters decision 2025-12-19\n- `JP-005` Japan AI Guidelines for Business Ver.1.2, current MIC page 2026-03-31\n\n```text\nNB05_R010_OFFICIAL_URL_SOURCE_SET = READY_8_WITH_LIMITS\nKR_BINDING_SOURCES = 3\nKR_SEPARATE_CURRENT_POLICY_PLAN_SOURCE = NOT_PINNED_R010\nJP_BINDING_SOURCES = 2\nJP_POLICY_GUIDANCE_SOURCES = 3\nBINDING_LAW_AND_POLICY_GUIDANCE_SEPARATED = YES\nNEW_BINARY_DOWNLOADS = 0\nNOTEBOOK_UPLOADS = 0\nAUTO_ADVANCE = NO\n```\n'''
    DOWNLOAD_LIST.write_text(text.rstrip()+block+'\n',encoding='utf-8')

# Current context
text=CONTEXT.read_text(encoding='utf-8')
if 'R010_KR_JP_L1_L2_COMPLETE_KR_POLICY_SOURCE_OPEN' not in text.split('\n',10)[6]:
    text=text.replace('R009_UK_SECTORAL_L1_L2_COMPLETE / R021_COMPLETE','R009_UK_SECTORAL_L1_L2_COMPLETE / R010_KR_JP_L1_L2_COMPLETE_KR_POLICY_SOURCE_OPEN / R021_COMPLETE',1)
if 'AI-LAWS-R010 = COMPLETE_RESEARCH_BASELINE_L1_L2_CURRENTNESS_OPEN' not in text:
    text=text.replace('AI-LAWS-R009 = COMPLETE_RESEARCH_BASELINE_L1_L2_SECTORAL_MAP_CURRENTNESS_OPEN\n','AI-LAWS-R009 = COMPLETE_RESEARCH_BASELINE_L1_L2_SECTORAL_MAP_CURRENTNESS_OPEN\nAI-LAWS-R010 = COMPLETE_RESEARCH_BASELINE_L1_L2_CURRENTNESS_OPEN\n',1)
section='''### R010 — Republic of Korea + Japan current AI law / policy binding-state map\n\nR010 established an eight-source official URL baseline and preserved law/policy/guidance boundaries.\n\n```text\nR010_CONTROLLED_OFFICIAL_URL_SOURCES = 8\nR010_KR_BINDING_SOURCES = 3\nR010_JP_BINDING_SOURCES = 2\nR010_JP_POLICY_GUIDANCE_SOURCES = 3\nKR001_CURRENT_SELECTOR = 2026-07-21\nKR002_CURRENT_SELECTOR = 2026-08-20\nKR003_CURRENT_SELECTOR = 2026-09-11\nKR_SEPARATE_CURRENT_AI_POLICY_PLAN_SOURCE = NOT_PINNED_R010\nJP001_CURRENT_STATUS = CurrentEnforced\nJP001_FULL_EFFECTIVE = 2025-09-01\nJP002_CURRENT_REVISION_EFFECTIVE = 2026-07-17\nJP003_AI_BASIC_PLAN_PHASE_II = 2026-07-14\nJP005_AI_GUIDELINES_FOR_BUSINESS = VER_1_2_2026-03-31\nCASE_LAW = NOT_ATTEMPTED\nLIABILITY_CONCLUSION = NOT_ATTEMPTED\n```\n\nDurable outputs are under `20_JURISDICTIONS/KR/`, `20_JURISDICTIONS/JP/` and `95_RESEARCH/ASIA/AI-LAWS-R010_CLOSEOUT_2026-09-14.md`. Authentic Korean/Japanese texts control. A separate current Korean AI policy-plan source remains an explicit open item rather than an inferred absence.\n\n'''
if '### R010 — Republic of Korea + Japan current AI law / policy binding-state map' not in text:
    text=text.replace('### R021\n',section+'### R021\n',1)
# Expand completed-current-next section and integrity state without auto-starting a new unit.
if 'AI-LAWS-R010 — REPUBLIC OF KOREA + JAPAN CURRENT AI LAW / POLICY BINDING-STATE MAP' not in text:
    needle='AI-LAWS-R004 — COUNCIL OF EUROPE CETS 225 CURRENT TREATY-STATUS / DECLARATION MAP\nSTATE = COMPLETE_RESEARCH_BASELINE_L1_L2\n'
    repl=needle+'\nAI-LAWS-R010 — REPUBLIC OF KOREA + JAPAN CURRENT AI LAW / POLICY BINDING-STATE MAP\nSTATE = COMPLETE_RESEARCH_BASELINE_L1_L2_CURRENTNESS_OPEN\n'
    text=text.replace(needle,repl,1)
if 'R010_CONTROLLED_OFFICIAL_URL_SOURCES = 8' not in text.split('## 10. Current integrity state',1)[1]:
    text=text.replace('R007_US009_WHOLE_CHAPTER_SECTION_BY_SECTION_CURRENTNESS = OPEN\n','R007_US009_WHOLE_CHAPTER_SECTION_BY_SECTION_CURRENTNESS = OPEN\nR010_CONTROLLED_OFFICIAL_URL_SOURCES = 8\nR010_KR_BINDING_SOURCES = 3\nR010_JP_BINDING_SOURCES = 2\nR010_JP_POLICY_GUIDANCE_SOURCES = 3\nR010_KR_POLICY_PLAN_SOURCE = NOT_PINNED\nR010_NEW_BINARY_DOWNLOADS = 0\n',1)
CONTEXT.write_text(text,encoding='utf-8')

closeout='''# AI-LAWS-R010 — Republic of Korea + Japan Current AI Law / Policy Binding-State Map Closeout\n\n**UNIT_ID:** `AI-LAWS-R010`\n**RESEARCH_DATE:** 2026-09-14\n**AUTO_ADVANCE:** NO\n\n## Result\n\n```text\nCONTROLLED_OFFICIAL_URL_SOURCES = 8\nKR_BINDING_SOURCE_RECORDS = 3\nJP_BINDING_SOURCE_RECORDS = 2\nJP_POLICY_OR_GUIDANCE_SOURCE_RECORDS = 3\nKR001_CURRENT_PAGE_NWYN = Y\nKR001_CURRENT_WRAPPER_SELECTOR = 2026-07-21\nKR001_CURRENT_REVISION_ANCNO = 21311\nKR001_CURRENT_REVISION_ANCYD = 2026-01-20\nKR001_BODY_BASE_EFFECT_SIGNAL = 2026-01-22\nKR001_AMENDMENT_CHAIN_NORMALIZED = NO\nKR002_CURRENT_SELECTOR = 2026-08-20\nKR003_CURRENT_SELECTOR = 2026-09-11\nKR_SEPARATE_CURRENT_AI_POLICY_PLAN_SOURCE = NOT_PINNED_R010\nJP001_EGOV_CURRENT_STATUS = CurrentEnforced\nJP001_PROMULGATED = 2025-06-04\nJP001_FULL_EFFECTIVE = 2025-09-01\nJP002_CURRENT_REVISION_EFFECTIVE = 2026-07-17\nJP003_AI_BASIC_PLAN_PHASE_II_CABINET_DECISION = 2026-07-14\nJP004_APPROPRIATENESS_GUIDELINE_DECISION = 2025-12-19\nJP005_AI_GUIDELINES_FOR_BUSINESS = VER_1_2_2026-03-31\nJP005_MIC_ACCESS = HTTP_200\nJP005_METI_COUNTERPART_ACCESS = HTTP_403_GITHUB_RUNNER\nTRANSLATION_CONTROL = AUTHENTIC_KOREAN_AND_JAPANESE_PRIMARY_TEXT\nNEW_BINARY_DOWNLOADS = 0\nDERIVED_MARKDOWN_CREATED = 0\nNOTEBOOK_UPLOADS = 0\nCASE_LAW = NOT_ATTEMPTED\nLIABILITY_CONCLUSION = NOT_ATTEMPTED\nZIP_OR_ARTIFACT_CREATED = NO\nAUTO_ADVANCE = NO\n```\n\n## Safeguards\n\n- Current revision metadata is not represented as original enactment metadata.\n- Korea AI Basic Act wrapper/date signals are preserved separately; no single universal commencement date is inferred.\n- `KR_SEPARATE_CURRENT_AI_POLICY_PLAN_SOURCE = NOT_PINNED_R010` is an explicit research gap, not a negative finding that no policy exists.\n- Japan Cabinet policy plans and official guidelines are not converted into statutes.\n- METI HTTP 403 is an access limitation, not source absence; the Cabinet Office hub and MIC page preserve the current guideline identity.\n- Authentic Korean/Japanese primary text controls over informal translation.\n- No sector application, case-law, breach, causation, damage, remedy or liability conclusion is created.\n\n## Stop condition\n\n```text\nSTOP = YES\nAUTO_ADVANCE = NO\n```\n'''
(ROOT/'95_RESEARCH/ASIA/AI-LAWS-R010_CLOSEOUT_2026-09-14.md').write_text(closeout,encoding='utf-8')

print('R010_DURABLE_GENERATION=PASS')
print('CONTROLLED_SOURCES=8')
print('ZIP_OR_ARTIFACT_CREATED=NO')
print('NEW_BINARY_DOWNLOADS=0')
print('NOTEBOOK_UPLOADS=0')
print('AUTO_ADVANCE=NO')
