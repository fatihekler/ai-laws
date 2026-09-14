from pathlib import Path
import csv, io

ROOT=Path('.')
DATE='2026-09-14'
BATCH='NB-BATCH-NB05-20260914-001'

sources=[
 dict(source_id='CN-001',title_zh='互联网信息服务算法推荐管理规定',title_en='Provisions on the Administration of Algorithmic Recommendations in Internet Information Services',document_id='CAC/MIIT/MPS/SAMR Order No. 9',authority='CAC; MIIT; MPS; SAMR',authority_class='DEPARTMENTAL_REGULATION',binding_state='binding departmental regulation; effective 2022-03-01',official_url='https://www.cac.gov.cn/2022-01/04/c_1642894606364259.htm',publication_date='2021-12-31',effective_date='2022-03-01',verification_state='VERIFIED_OFFICIAL_IDENTITY_EFFECTIVE_DATE_CURRENTNESS_RECHECK_REQUIRED',currentness='EFFECTIVE_DATE_VERIFIED_CURRENTNESS_RECHECK_REQUIRED',note='Official CAC text and commencement verified; no separate repeal/supersession search completed in R008.'),
 dict(source_id='CN-002',title_zh='互联网信息服务深度合成管理规定',title_en='Provisions on the Administration of Deep Synthesis Internet Information Services',document_id='CAC/MIIT/MPS Order No. 12',authority='CAC; MIIT; MPS',authority_class='DEPARTMENTAL_REGULATION',binding_state='binding departmental regulation; effective 2023-01-10',official_url='https://www.cac.gov.cn/2022-12/11/c_1672221949354811.htm',publication_date='2022-11-25',effective_date='2023-01-10',verification_state='VERIFIED_OFFICIAL_IDENTITY_EFFECTIVE_DATE_CURRENTNESS_RECHECK_REQUIRED',currentness='EFFECTIVE_DATE_VERIFIED_CURRENTNESS_RECHECK_REQUIRED',note='Official CAC text and commencement verified; no separate repeal/supersession search completed in R008.'),
 dict(source_id='CN-003',title_zh='生成式人工智能服务管理暂行办法',title_en='Interim Measures for the Management of Generative Artificial Intelligence Services',document_id='Multi-agency Order No. 15',authority='CAC-led multi-agency issuance',authority_class='DEPARTMENTAL_REGULATION_OR_MEASURE',binding_state='binding regulatory measure; effective 2023-08-15',official_url='https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm',publication_date='2023-07-10',effective_date='2023-08-15',verification_state='VERIFIED_OFFICIAL_IDENTITY_EFFECTIVE_DATE_CURRENTNESS_RECHECK_REQUIRED',currentness='EFFECTIVE_DATE_VERIFIED_CURRENTNESS_RECHECK_REQUIRED',note='Official CAC text identifies Order No. 15 and commencement; exact duty/application analysis remains separate.'),
 dict(source_id='CN-004',title_zh='中华人民共和国个人信息保护法',title_en='Personal Information Protection Law of the PRC',document_id='NPC FLK bbbs ff8081817b6472a3017b656cc2040044',authority='NPC Standing Committee',authority_class='NATIONAL_LAW',binding_state='binding national law; current/effective in NPC database',official_url='https://flk.npc.gov.cn/law-search/search/flfgDetails?bbbs=ff8081817b6472a3017b656cc2040044',publication_date='2021-08-20',effective_date='2021-11-01',verification_state='VERIFIED_OFFICIAL_CURRENT_NPC_DATABASE',currentness='CURRENT_EFFECTIVE_NPC_DATABASE_SXX3',note='NPC National Laws and Regulations Database exact-title search and detail record verified; status sxx=3 (effective/current).'),
 dict(source_id='CN-005',title_zh='中华人民共和国数据安全法',title_en='Data Security Law of the PRC',document_id='NPC FLK bbbs ff80818179f5e0800179f885c7e70392',authority='NPC Standing Committee',authority_class='NATIONAL_LAW',binding_state='binding national law; current/effective in NPC database',official_url='https://flk.npc.gov.cn/law-search/search/flfgDetails?bbbs=ff80818179f5e0800179f885c7e70392',publication_date='2021-06-10',effective_date='2021-09-01',verification_state='VERIFIED_OFFICIAL_CURRENT_NPC_DATABASE',currentness='CURRENT_EFFECTIVE_NPC_DATABASE_SXX3',note='NPC National Laws and Regulations Database exact-title search and detail record verified; status sxx=3 (effective/current).'),
 dict(source_id='CN-006',title_zh='中华人民共和国网络安全法',title_en='Cybersecurity Law of the PRC — current revised record',document_id='NPC FLK bbbs 021e7d7684474107b8f3febbb1c4f8b5',authority='NPC Standing Committee',authority_class='NATIONAL_LAW',binding_state='binding national law; current revised record effective 2026-01-01',official_url='https://flk.npc.gov.cn/law-search/search/flfgDetails?bbbs=021e7d7684474107b8f3febbb1c4f8b5',publication_date='2025-10-28',effective_date='2026-01-01',verification_state='VERIFIED_OFFICIAL_CURRENT_NPC_DATABASE_REVISED_2025',currentness='CURRENT_EFFECTIVE_NPC_DATABASE_SXX3_2016_RECORD_MODIFIED',note='NPC exact-title search distinguishes the 2025-10-28 current record (sxx=3) from the 2016 record (sxx=2, modified); amendment decision bbbs 621d029681d4457ab5fc56ec7c7464a1 is linked supporting authority.'),
 dict(source_id='CN-007',title_zh='网络数据安全管理条例',title_en='Network Data Security Management Regulation',document_id='State Council network-data regulation',authority='State Council',authority_class='ADMINISTRATIVE_REGULATION',binding_state='binding administrative regulation; effective 2025-01-01',official_url='https://www.gov.cn/zhengce/content/202409/content_6977766.htm',publication_date='UNKNOWN',effective_date='2025-01-01',verification_state='VERIFIED_OFFICIAL_IDENTITY_EFFECTIVE_DATE_CURRENTNESS_RECHECK_REQUIRED',currentness='EFFECTIVE_DATE_VERIFIED_CURRENTNESS_RECHECK_REQUIRED',note='Official Gov.cn identity and 2025-01-01 commencement verified; publication/promulgation date not normalized by R008.'),
 dict(source_id='CN-008',title_zh='人工智能生成合成内容标识办法',title_en='Measures for Labeling Artificial-Intelligence-Generated and Synthetic Content',document_id='2025 AI-generated-content labeling measure',authority='CAC-led multi-agency issuance',authority_class='DEPARTMENTAL_REGULATORY_MEASURE',binding_state='binding regulatory measure; effective 2025-09-01',official_url='https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm',publication_date='2025-03-14',effective_date='2025-09-01',verification_state='VERIFIED_OFFICIAL_IDENTITY_EFFECTIVE_DATE_CURRENTNESS_RECHECK_REQUIRED',currentness='EFFECTIVE_DATE_VERIFIED_CURRENTNESS_RECHECK_REQUIRED',note='Official CAC notice identifies the measure and 2025-09-01 commencement; exact co-issuer metadata is not expanded beyond verified CAC-led multi-agency characterization in R008.'),
]

def read_csv(path):
    with open(path,encoding='utf-8-sig',newline='') as f:
        r=csv.DictReader(f); return r.fieldnames,list(r)

def write_csv(path,fields,rows):
    buf=io.StringIO(newline='')
    w=csv.DictWriter(buf,fieldnames=fields,lineterminator='\n',extrasaction='ignore')
    w.writeheader(); w.writerows(rows)
    Path(path).write_text(buf.getvalue(),encoding='utf-8',newline='')

# Jurisdiction registry
p='20_JURISDICTIONS/JURISDICTION_RESEARCH_REGISTRY.csv'
f,rows=read_csv(p)
found=False
for r in rows:
    if r['jurisdiction_id']=='CN':
        r['research_state']='PRIMARY_SOURCE_MAP_L1_COMPLETE_TRANSLATION_AND_APPLICATION_OPEN'
        r['notes']='R008 verified an eight-source central official baseline for algorithm recommendation, deep synthesis, generative AI, PIPL, Data Security Law, current revised Cybersecurity Law, Network Data Security Regulation and AI-generated-content labeling. Authentic Chinese primary sources control; translations, sector-specific application, enforcement and case law remain open.'
        found=True
assert found
write_csv(p,f,rows)

# Research queue
p='90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv'
f,rows=read_csv(p)
found=False
for r in rows:
    if r['work_item_id']=='AI-LAWS-R008':
        r['state']='COMPLETE_RESEARCH_BASELINE_L1_PRIMARY_SOURCE_MAP'
        r['expected_output']='20_JURISDICTIONS/CN/CN_AI_DATA_CYBER_PRIMARY_SOURCE_MAP_2026-09-14.md; 20_JURISDICTIONS/CN/CN_PRIMARY_SOURCE_INVENTORY_2026-09-14.csv; 20_JURISDICTIONS/CN/CN_CURRENTNESS_AND_BINDING_STATE_MATRIX.csv; 95_RESEARCH/CN/AI-LAWS-R008_CLOSEOUT_2026-09-14.md'
        r['stop_condition']='L1 central primary-source map complete; stop before unofficial translation controls, sector-specific duty/application conclusions, enforcement/case law, Hong Kong/Macau treatment or liability conclusions'
        found=True
assert found
write_csv(p,f,rows)

# Source manifest
p='86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv'
f,rows=read_csv(p)
assert not any(r.get('source_id','').startswith('CN-') for r in rows), 'CN source IDs already exist'
for s in sources:
    rows.append(dict(source_id=s['source_id'],primary_pack='NB05',jurisdiction='CN',title=s['title_en'],document_id=s['document_id'],authority_class=s['authority_class'],binding_state=s['binding_state'],official_url=s['official_url'],preferred_ingest='URL_DIRECT_PREFERRED',priority='P0',verification_state=s['verification_state'],last_verified=DATE,rights_or_use_state='OFFICIAL_PUBLIC_URL_REPRODUCTION_PERMISSION_NOT_ESTABLISHED',notes=s['note']+' Authentic Chinese source controls; no controlled official English translation pinned; no repository binary vendored.'))
write_csv(p,f,rows)

# Pack assignments
p='86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_PACK_ASSIGNMENTS.csv'
f,rows=read_csv(p)
existing={(r['pack_id'],r['source_id']) for r in rows}
for s in sources:
    if ('NB05',s['source_id']) not in existing:
        rows.append(dict(pack_id='NB05',source_id=s['source_id'],requirement='REQUIRED',reason='China central primary-source baseline; authentic Chinese official URL; R008'))
write_csv(p,f,rows)

# Acquisition ledger
p='86_NOTEBOOKLM/NOTEBOOKLM_ACQUISITION_AND_VALIDATION_LEDGER.csv'
f,rows=read_csv(p)
existing={(r['batch_id'],r['source_id']) for r in rows}
for s in sources:
    key=(BATCH,s['source_id'])
    if key in existing: continue
    rows.append(dict(batch_id=BATCH,source_id=s['source_id'],notebook_pack='NB05',jurisdiction='CN',title=s['title_en'],document_id=s['document_id'],issuing_authority=s['authority'],authority_class=s['authority_class'],binding_state=s['binding_state'],official_url=s['official_url'],retrieval_date=DATE,version_state=s['verification_state'],adoption_date='UNKNOWN',publication_date=s['publication_date'],entry_into_force_date=s['effective_date'],application_date=s['effective_date'],authentic_language='Chinese',translation_state='NO_CONTROLLED_OFFICIAL_ENGLISH_TRANSLATION_PINNED',rights_state='OFFICIAL_PUBLIC_URL_REPRODUCTION_PERMISSION_NOT_ESTABLISHED',acquisition_method='URL_DIRECT_PREFERRED',local_filename_or_url=s['official_url'],sha256='',byte_size='',content_type='text/html or official database JSON; URL-direct',content_identity_checked='WEB_IDENTITY_VERIFIED_OFFICIAL_PRIMARY_SOURCE',notebook_name='',notebook_ingest_date='',notebook_ingest_state='NOT_RUN',notebook_locator_test='NOT_RUN',primary_source_recheck_state='R008_PRIMARY_SOURCE_IDENTITY_VERIFIED',refresh_trigger='official source replacement amendment repeal or currentness change',human_review_required='YES_BEFORE_MATERIAL_LEGAL_CLAIM',notes=s['note']+' No local binary and no translation authority claimed.'))
write_csv(p,f,rows)

# Durable China inventory
Path('20_JURISDICTIONS/CN').mkdir(parents=True,exist_ok=True)
inv_fields=['source_id','title_zh','title_en','authority','authority_class','official_url','publication_or_promulgation_date','effective_date','binding_state','currentness_state','authentic_language','translation_state','primary_source_state','caveat']
inv=[]
for s in sources:
    inv.append(dict(source_id=s['source_id'],title_zh=s['title_zh'],title_en=s['title_en'],authority=s['authority'],authority_class=s['authority_class'],official_url=s['official_url'],publication_or_promulgation_date=s['publication_date'],effective_date=s['effective_date'],binding_state=s['binding_state'],currentness_state=s['currentness'],authentic_language='Chinese',translation_state='NO_CONTROLLED_OFFICIAL_ENGLISH_TRANSLATION_PINNED',primary_source_state='VERIFIED_OFFICIAL_PRIMARY_SOURCE_R008',caveat=s['note']))
write_csv('20_JURISDICTIONS/CN/CN_PRIMARY_SOURCE_INVENTORY_2026-09-14.csv',inv_fields,inv)

mat_fields=['source_id','regulatory_layer','binding_class','effective_date','currentness_admission','application_scope_status','translation_control','r008_claim_state']
layer={'CN-001':'ALGORITHMIC_RECOMMENDATION','CN-002':'DEEP_SYNTHESIS','CN-003':'GENERATIVE_AI','CN-004':'PERSONAL_INFORMATION','CN-005':'DATA_SECURITY','CN-006':'CYBERSECURITY','CN-007':'NETWORK_DATA_SECURITY','CN-008':'AI_GENERATED_CONTENT_LABELING'}
mat=[]
for s in sources:
    mat.append(dict(source_id=s['source_id'],regulatory_layer=layer[s['source_id']],binding_class=s['authority_class'],effective_date=s['effective_date'],currentness_admission=s['currentness'],application_scope_status='SOURCE_SCOPE_IDENTIFIED_DETAIL_APPLICATION_REQUIRES_INSTRUMENT_SPECIFIC_ANALYSIS',translation_control='AUTHENTIC_CHINESE_CONTROLS',r008_claim_state='L1_PRIMARY_SOURCE_BASELINE_ONLY'))
write_csv('20_JURISDICTIONS/CN/CN_CURRENTNESS_AND_BINDING_STATE_MATRIX.csv',mat_fields,mat)

map_md='''# AI-LAWS — China AI / Data / Cyber Primary-Source Map\n\n**WORK_ITEM:** `AI-LAWS-R008`\n**RESEARCH_DATE:** 2026-09-14\n**LEVEL:** L1 central primary-source baseline\n**AUTHENTIC_LANGUAGE:** Chinese\n**LEGAL_ADVICE:** NO\n**AUTO_ADVANCE:** NO\n\n## 1. Method and authority boundary\n\nR008 uses central official Chinese sources only: the Cyberspace Administration of China, the State Council / China Government portal, and the National Laws and Regulations Database of the National People's Congress. Search engines are not legal authority. No unofficial English translation is promoted into authoritative text.\n\n```text\nOFFICIAL_CHINESE_PRIMARY_TEXT > UNOFFICIAL_TRANSLATION\nSEARCH_RESULT != LEGAL_AUTHORITY\nEFFECTIVE_DATE_VERIFIED != REPEAL_CHECK_COMPLETE\nADMINISTRATIVE_RULE != NATIONAL_STATUTE\nREGULATORY_LAYER != UNIVERSAL_AI_CODE\n```\n\n## 2. Controlled eight-source baseline\n\nThe controlled source inventory is `CN_PRIMARY_SOURCE_INVENTORY_2026-09-14.csv`. It covers:\n\n- `CN-001` algorithmic recommendation provisions — effective 2022-03-01;\n- `CN-002` deep-synthesis provisions — effective 2023-01-10;\n- `CN-003` interim generative-AI service measures — effective 2023-08-15;\n- `CN-004` Personal Information Protection Law — NPC database current/effective; effective 2021-11-01;\n- `CN-005` Data Security Law — NPC database current/effective; effective 2021-09-01;\n- `CN-006` Cybersecurity Law current revised record — published 2025-10-28 and effective 2026-01-01;\n- `CN-007` Network Data Security Management Regulation — effective 2025-01-01;\n- `CN-008` AI-generated/synthetic-content labeling measure — effective 2025-09-01.\n\nThese instruments form a layered regulatory baseline; R008 does not infer a single comprehensive Chinese AI Act.\n\n## 3. Current Cybersecurity Law correction\n\nThe NPC official database exact-title search returned a current Cybersecurity Law record with `bbbs=021e7d7684474107b8f3febbb1c4f8b5`, publication date 2025-10-28, effective date 2026-01-01 and status `sxx=3` (effective/current). The 2016 record is returned separately with `sxx=2` (modified). The official amendment decision is `bbbs=621d029681d4457ab5fc56ec7c7464a1`.\n\n```text\nCSL_2016_RECORD != CURRENT_2026_TEXT\nCURRENT_CSL_BBBS = 021e7d7684474107b8f3febbb1c4f8b5\nCURRENT_CSL_EFFECTIVE_DATE = 2026-01-01\n```\n\n## 4. Currentness and translation boundary\n\nPIPL, Data Security Law and the current Cybersecurity Law were verified through the NPC database current-status layer. For the CAC/State-Council measures, official identity and commencement were verified, but R008 did not perform a separate exhaustive repeal/supersession search. They therefore remain tagged `CURRENTNESS_RECHECK_REQUIRED` before material future conclusions.\n\nAuthentic Chinese text controls. R008 does not create or certify an English legal translation. Any later English-language claim matrix must preserve the Chinese locator and recheck the exact provision.\n\n## 5. Scope / territorial boundary\n\nR008 maps central PRC source layers only. It does not determine Hong Kong or Macao law, cross-border conflicts, extraterritorial reach for a specific actor, sectoral licensing, enforcement practice, private rights of action, administrative penalty outcomes or case law.\n\n## 6. Notebook routing\n\n`CN-001..CN-008` are assigned to `NB05_ASIA_AND_COMPARATIVE` as URL-direct sources. No local binary, OCR, derived Markdown or Notebook upload was created in R008.\n\n```text\nNB05_CN_OFFICIAL_URL_SOURCE_SET = READY_8\nNEW_BINARY_DOWNLOADS = 0\nNOTEBOOK_UPLOADS = 0\nDERIVED_MARKDOWN_CREATED = 0\nCASE_LAW = NOT_ATTEMPTED\nLIABILITY_CONCLUSION = NOT_ATTEMPTED\nAUTO_ADVANCE = NO\n```\n'''
Path('20_JURISDICTIONS/CN/CN_AI_DATA_CYBER_PRIMARY_SOURCE_MAP_2026-09-14.md').write_text(map_md,encoding='utf-8')

# Notebook URL list
p=Path('86_NOTEBOOKLM/NOTEBOOKLM_DOWNLOAD_AND_UPLOAD_LIST.md')
t=p.read_text(encoding='utf-8')
marker='## F. NB06 — Human sovereignty / neurotechnology'
assert marker in t
if '## E2. NB05 — Asia and Comparative / China URL source set' not in t:
    sec='''## E2. NB05 — Asia and Comparative / China URL source set\n\nR008 established an eight-source China primary-source baseline. Use official URLs directly; no repository binary set exists. Authentic Chinese text controls and translation/currentness caveats remain mandatory.\n\n- `CN-001` https://www.cac.gov.cn/2022-01/04/c_1642894606364259.htm\n- `CN-002` https://www.cac.gov.cn/2022-12/11/c_1672221949354811.htm\n- `CN-003` https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm\n- `CN-004` https://flk.npc.gov.cn/law-search/search/flfgDetails?bbbs=ff8081817b6472a3017b656cc2040044\n- `CN-005` https://flk.npc.gov.cn/law-search/search/flfgDetails?bbbs=ff80818179f5e0800179f885c7e70392\n- `CN-006` https://flk.npc.gov.cn/law-search/search/flfgDetails?bbbs=021e7d7684474107b8f3febbb1c4f8b5\n- `CN-007` https://www.gov.cn/zhengce/content/202409/content_6977766.htm\n- `CN-008` https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm\n\n```text\nNB05_CN_OFFICIAL_URL_SOURCE_SET = READY_8\nREPOSITORY_BINARY_SET = NONE\nNOTEBOOK_UPLOAD = NOT_RUN\nPRIMARY_SOURCE_RECHECK_REQUIRED_BEFORE_MATERIAL_CLAIM = YES\n```\n\n---\n\n'''
    t=t.replace(marker,sec+marker)
p.write_text(t,encoding='utf-8')

# Current context
p=Path('00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md')
t=p.read_text(encoding='utf-8')
t=t.replace('R007_US_INVENTORY_ARCHITECTURE_L1_COMPLETE / R021_COMPLETE','R007_US_INVENTORY_ARCHITECTURE_L1_COMPLETE / R008_CN_PRIMARY_SOURCE_MAP_L1_COMPLETE / R021_COMPLETE')
t=t.replace('AI-LAWS-R007 = COMPLETE_RESEARCH_ARCHITECTURE_L1_STATE_LAW_CONTENT_OPEN\n','AI-LAWS-R007 = COMPLETE_RESEARCH_ARCHITECTURE_L1_STATE_LAW_CONTENT_OPEN\nAI-LAWS-R008 = COMPLETE_RESEARCH_BASELINE_L1_PRIMARY_SOURCE_MAP\n')
if '### R008 — China central primary-source baseline' not in t:
    anchor='### R021\n'
    assert anchor in t
    sec='''### R008 — China central primary-source baseline\n\nR008 pinned an eight-source central PRC baseline from CAC, Gov.cn and the NPC National Laws and Regulations Database.\n\n```text\nCN_CONTROLLED_PRIMARY_SOURCES = 8\nCN_ALGORITHM_RULE_EFFECTIVE = 2022-03-01\nCN_DEEP_SYNTHESIS_RULE_EFFECTIVE = 2023-01-10\nCN_GENAI_INTERIM_MEASURES_EFFECTIVE = 2023-08-15\nCN_PIPL_CURRENT_NPC_STATUS = EFFECTIVE\nCN_DATA_SECURITY_LAW_CURRENT_NPC_STATUS = EFFECTIVE\nCN_CYBERSECURITY_LAW_CURRENT_RECORD = 2025-10-28 / EFFECTIVE_2026-01-01\nCN_NETWORK_DATA_REGULATION_EFFECTIVE = 2025-01-01\nCN_AI_CONTENT_LABELING_EFFECTIVE = 2025-09-01\nNB05_CN_OFFICIAL_URL_SOURCE_SET = READY_8\nTRANSLATION_CONTROL = AUTHENTIC_CHINESE_PRIMARY_TEXT\nSECTOR_APPLICATION = NOT_ATTEMPTED\nCASE_LAW = NOT_ATTEMPTED\nLIABILITY_CONCLUSION = NOT_ATTEMPTED\n```\n\nDurable outputs are under `20_JURISDICTIONS/CN/` plus `95_RESEARCH/CN/AI-LAWS-R008_CLOSEOUT_2026-09-14.md`.\n\n'''
    t=t.replace(anchor,sec+anchor)
p.write_text(t,encoding='utf-8')

# Closeout
Path('95_RESEARCH/CN').mkdir(parents=True,exist_ok=True)
close='''# AI-LAWS-R008 — China Primary-Source Map Closeout\n\n**UNIT_ID:** `AI-LAWS-R008`\n**RESEARCH_DATE:** 2026-09-14\n**AUTO_ADVANCE:** NO\n\n## Result\n\n```text\nCENTRAL_OFFICIAL_PRIMARY_SOURCE_RECORDS = 8\nCAC_AI_REGULATORY_SOURCES = 4\nNPC_CURRENT_NATIONAL_LAW_RECORDS = 3\nSTATE_COUNCIL_NETWORK_DATA_REGULATION = 1\nNPC_CURRENT_STATUS_VERIFIED = CN-004; CN-005; CN-006\nCN006_CURRENT_REVISED_CYBERSECURITY_LAW_EFFECTIVE = 2026-01-01\nNB05_CN_OFFICIAL_URL_SOURCE_SET = READY_8\nAUTHENTIC_LANGUAGE = CHINESE\nCONTROLLED_OFFICIAL_ENGLISH_TRANSLATION_PINNED = NO\nNEW_BINARY_DOWNLOADS = 0\nNOTEBOOK_UPLOADS = 0\nDERIVED_MARKDOWN_CREATED = 0\nZIP_OR_ARTIFACT_CREATED = NO\nCASE_LAW = NOT_ATTEMPTED\nLIABILITY_CONCLUSION = NOT_ATTEMPTED\nAUTO_ADVANCE = NO\n```\n\n## Safeguards\n\n- The 2016 Cybersecurity Law record is not used as the current 2026 text; the NPC database marks it modified and exposes a 2025 revised record effective 2026-01-01.\n- CAC/State-Council instrument identity and commencement are verified, but R008 does not overclaim an exhaustive repeal/supersession review.\n- Authentic Chinese primary sources control. No unofficial English translation is treated as legal authority.\n- A layered source map is not a finding that China has one unified AI statute.\n- Scope, actor classification, enforcement practice, penalties, judicial review, Hong Kong/Macao law and concrete liability remain outside R008.\n\n## Stop condition\n\nR008 stops at the L1 central primary-source baseline.\n\n```text\nSTOP = YES\nAUTO_ADVANCE = NO\n```\n'''
Path('95_RESEARCH/CN/AI-LAWS-R008_CLOSEOUT_2026-09-14.md').write_text(close,encoding='utf-8')

# Assertions
assert len(sources)==8
for path in ['20_JURISDICTIONS/CN/CN_PRIMARY_SOURCE_INVENTORY_2026-09-14.csv','20_JURISDICTIONS/CN/CN_CURRENTNESS_AND_BINDING_STATE_MATRIX.csv']:
    _,rr=read_csv(path); assert len(rr)==8
f,man=read_csv('86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv')
assert sum(1 for r in man if r['source_id'].startswith('CN-'))==8
f,pa=read_csv('86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_PACK_ASSIGNMENTS.csv')
assert sum(1 for r in pa if r['pack_id']=='NB05' and r['source_id'].startswith('CN-'))==8
f,led=read_csv('86_NOTEBOOKLM/NOTEBOOKLM_ACQUISITION_AND_VALIDATION_LEDGER.csv')
assert sum(1 for r in led if r['batch_id']==BATCH and r['source_id'].startswith('CN-'))==8
print('R008_PERSIST_GENERATION_OK')
