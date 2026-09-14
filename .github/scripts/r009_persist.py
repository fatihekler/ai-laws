from pathlib import Path
import csv
import io

ROOT = Path('.')
DATE = '2026-09-14'
BATCH = 'NB-BATCH-NB05-20260914-002'

SOURCES = [
    dict(source_id='GB-001', title='United Kingdom General Data Protection Regulation (UK GDPR)', document_id='Regulation (EU) 2016/679 — United Kingdom General Data Protection Regulation', authority='UK legislation / legislation.gov.uk', authority_class='STATUTE_OR_REGULATION', binding_state='binding UK data-protection law; exact provision-level effect/currentness must be rechecked', url='https://www.legislation.gov.uk/eur/2016/679/contents', enactment='2016-04-27', currentness='LATEST_AVAILABLE_REVISED_OFFICIAL_PAGE_SECTION_LEVEL_CURRENTNESS_RECHECK_REQUIRED', domain='DATA_PROTECTION', requirement='REQUIRED', reason='Core UK data-protection baseline', priority='P1', notes='Official legislation.gov.uk title explicitly identifies the United Kingdom General Data Protection Regulation. XML enactment-date attribute verified as 2016-04-27. Do not infer UK domestic commencement or current effect of every provision from that date.'),
    dict(source_id='GB-002', title='Data Protection Act 2018', document_id='2018 c. 12', authority='UK Parliament / legislation.gov.uk', authority_class='STATUTE_OR_REGULATION', binding_state='binding UK Act; exact provision-level effect/currentness must be rechecked', url='https://www.legislation.gov.uk/ukpga/2018/12/contents', enactment='2018-05-23', currentness='LATEST_AVAILABLE_REVISED_OFFICIAL_PAGE_SECTION_LEVEL_CURRENTNESS_RECHECK_REQUIRED', domain='DATA_PROTECTION', requirement='REQUIRED', reason='UK data-protection statutory baseline', priority='P1', notes='Official latest-available revised page and XML enactment-date attribute verified. Commencement is not inferred from enactment date.'),
    dict(source_id='GB-003', title='Data (Use and Access) Act 2025', document_id='2025 c. 18', authority='UK Parliament / legislation.gov.uk', authority_class='STATUTE_OR_REGULATION', binding_state='binding UK Act with provision-specific commencement/currentness dependencies', url='https://www.legislation.gov.uk/ukpga/2025/18/contents', enactment='2025-06-19', currentness='LATEST_AVAILABLE_REVISED_OFFICIAL_PAGE_STAGED_COMMENCEMENT_RECHECK_REQUIRED', domain='DATA_PROTECTION_AND_DIGITAL', requirement='REQUIRED', reason='Current UK data-use/data-protection reform layer', priority='P1', notes='Official latest-available revised page and XML enactment-date attribute verified. R009 does not normalize section-by-section commencement or amendment effects.'),
    dict(source_id='GB-004', title='Online Safety Act 2023', document_id='2023 c. 50', authority='UK Parliament / legislation.gov.uk', authority_class='STATUTE_OR_REGULATION', binding_state='binding UK Act with provision-specific commencement and secondary/regulator implementation dependencies', url='https://www.legislation.gov.uk/ukpga/2023/50/contents', enactment='2023-10-26', currentness='LATEST_AVAILABLE_REVISED_OFFICIAL_PAGE_STAGED_COMMENCEMENT_AND_OFCOM_IMPLEMENTATION_RECHECK_REQUIRED', domain='ONLINE_SAFETY', requirement='REQUIRED', reason='Core UK online-safety statutory layer', priority='P1', notes='Official latest-available revised page and XML enactment-date attribute verified. Ofcom online-safety hub returned HTTP 403 to the GitHub runner; that access failure is not source absence.'),
    dict(source_id='GB-005', title='Digital Markets, Competition and Consumers Act 2024', document_id='2024 c. 13', authority='UK Parliament / legislation.gov.uk', authority_class='STATUTE_OR_REGULATION', binding_state='binding UK Act with provision-specific commencement/currentness dependencies', url='https://www.legislation.gov.uk/ukpga/2024/13/contents', enactment='2024-05-24', currentness='LATEST_AVAILABLE_REVISED_OFFICIAL_PAGE_SECTION_LEVEL_CURRENTNESS_RECHECK_REQUIRED', domain='COMPETITION_AND_CONSUMER', requirement='REQUIRED', reason='Digital markets competition and consumer enforcement baseline', priority='P1', notes='Official latest-available revised page and XML enactment-date attribute verified. R009 does not map every Part commencement or CMA enforcement procedure.'),
    dict(source_id='GB-006', title='Consumer Rights Act 2015', document_id='2015 c. 15', authority='UK Parliament / legislation.gov.uk', authority_class='STATUTE_OR_REGULATION', binding_state='binding UK Act; application to a concrete AI product/service depends on facts and provision', url='https://www.legislation.gov.uk/ukpga/2015/15/contents', enactment='2015-03-26', currentness='LATEST_AVAILABLE_REVISED_OFFICIAL_PAGE_SECTION_LEVEL_CURRENTNESS_RECHECK_REQUIRED', domain='CONSUMER', requirement='RECOMMENDED', reason='Consumer contract/service/digital-content baseline', priority='P1', notes='Official latest-available revised page and XML enactment-date attribute verified. No AI-specific duty is inferred from source identity alone.'),
    dict(source_id='GB-007', title='Consumer Protection Act 1987', document_id='1987 c. 43', authority='UK Parliament / legislation.gov.uk', authority_class='STATUTE_OR_REGULATION', binding_state='binding UK Act; product-liability application to AI remains a separate legal analysis', url='https://www.legislation.gov.uk/ukpga/1987/43/contents', enactment='1987-05-15', currentness='LATEST_AVAILABLE_REVISED_OFFICIAL_PAGE_SECTION_LEVEL_CURRENTNESS_RECHECK_REQUIRED', domain='PRODUCT_LIABILITY', requirement='RECOMMENDED', reason='UK product-liability baseline', priority='P1', notes='Official latest-available revised page and XML enactment-date attribute verified. R009 does not conclude that a model/software output is a defective product or that liability exists.'),
    dict(source_id='GB-008', title='Product Regulation and Metrology Act 2025', document_id='2025 c. 20', authority='UK Parliament / legislation.gov.uk', authority_class='STATUTE_OR_REGULATION', binding_state='binding UK Act/enabling product-regulation framework; concrete duties may depend on secondary regulations and commencement', url='https://www.legislation.gov.uk/ukpga/2025/20/contents', enactment='2025-07-21', currentness='LATEST_AVAILABLE_REVISED_OFFICIAL_PAGE_SECONDARY_REGULATION_AND_SECTION_LEVEL_RECHECK_REQUIRED', domain='PRODUCT_REGULATION', requirement='RECOMMENDED', reason='Current product-regulation enabling framework relevant to AI-enabled products', priority='P1', notes='Official latest-available revised page and XML enactment-date attribute verified. R009 does not infer secondary regulations or product-specific AI duties that were not separately checked.'),
    dict(source_id='GB-009', title='AI Growth Lab', document_id='GOV.UK call for evidence — AI Growth Lab', authority='UK Government / Department for Science, Innovation and Technology', authority_class='POLICY_PROPOSAL', binding_state='closed call for evidence / proposed regulatory sandbox modifications; nonbinding; not enacted law', url='https://www.gov.uk/government/calls-for-evidence/ai-growth-lab', enactment='2025-10-21', currentness='OFFICIAL_GOVUK_CURRENT_PAGE_VERIFIED_NONBINDING_PROPOSAL_UPDATED_2025-12-18', domain='AI_GOVERNANCE_POLICY', requirement='RECOMMENDED', reason='Newer AI-regulation policy proposal layer; must remain separate from law', priority='P1', notes='GOV.UK Content API exact identity verified. Page states the proposed AI Growth Lab would support targeted regulatory modifications under safeguards. Proposal/call for evidence is not current binding law.'),
    dict(source_id='GB-010', title='Regulators’ strategic approaches to AI', document_id='GOV.UK regulator-strategy notice 2024', authority='UK Government / cross-regulator coordination', authority_class='OFFICIAL_GUIDANCE', binding_state='official nonbinding notice/coordination record; not statute', url='https://www.gov.uk/government/publications/regulators-strategic-approaches-to-ai', enactment='2024-05-01', currentness='OFFICIAL_GOVUK_PAGE_VERIFIED_NONBINDING_REGULATOR_STRATEGY_SNAPSHOT', domain='AI_GOVERNANCE_REGULATORS', requirement='RECOMMENDED', reason='Cross-regulator sectoral AI-governance architecture', priority='P1', notes='GOV.UK Content API exact identity verified. Notice records strategic AI approaches requested from key regulators; it does not itself create statutory AI duties.'),
    dict(source_id='GB-011', title='Artificial intelligence — ICO guidance hub', document_id='ICO AI guidance hub', authority='Information Commissioner’s Office', authority_class='REGULATORY_GUIDANCE', binding_state='official regulator guidance; nonbinding as guidance; underlying UK GDPR/DPA duties remain separate legal authority', url='https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/', enactment='UNKNOWN', currentness='OFFICIAL_ICO_AI_HUB_ACCESSIBLE_CURRENTNESS_DATE_NOT_NORMALIZED_R009', domain='DATA_PROTECTION_AI_GUIDANCE', requirement='RECOMMENDED', reason='ICO AI/data-protection guidance and explanation resources', priority='P1', notes='Official ICO AI hub returned HTTP 200 and references UK GDPR plus AI decision-explanation resources. R009 did not normalize the publication/update date or verify every linked guidance page.'),
    dict(source_id='GB-012', title='AI Foundation Models: initial review', document_id='CMA AI Foundation Models initial review', authority='Competition and Markets Authority', authority_class='REGULATORY_GUIDANCE', binding_state='official regulator market-study/review material; not statute or court holding', url='https://www.gov.uk/cma-cases/ai-foundation-models-initial-review', enactment='2023-05-04', currentness='OFFICIAL_GOVUK_CMA_PAGE_VERIFIED_UPDATED_2024-04-16_NONBINDING_REVIEW', domain='COMPETITION_AI', requirement='RECOMMENDED', reason='Competition/foundation-model regulator context', priority='P1', notes='GOV.UK Content API exact page identity verified; first published 2023-05-04 and public update 2024-04-16. Do not convert market-review findings into binding duties.'),
    dict(source_id='GB-013', title='AI Opportunities Action Plan: government response', document_id='UK Government response to AI Opportunities Action Plan 2025', authority='UK Government', authority_class='OFFICIAL_GUIDANCE', binding_state='government policy paper; nonbinding; not statute', url='https://www.gov.uk/government/publications/ai-opportunities-action-plan-government-response', enactment='2025-01-13', currentness='OFFICIAL_GOVUK_POLICY_PAPER_PAGE_VERIFIED_NONBINDING', domain='AI_POLICY', requirement='RECOMMENDED', reason='National AI strategy/policy context separated from binding law', priority='P1', notes='GOV.UK Content API exact identity verified; policy paper published 2025-01-13. Later AI Growth Lab/regulatory-policy materials exist, so this is not treated as the sole current AI-regulation source.'),
]

MANIFEST_PATH = ROOT/'86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv'
PACK_PATH = ROOT/'86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_PACK_ASSIGNMENTS.csv'
LEDGER_PATH = ROOT/'86_NOTEBOOKLM/NOTEBOOKLM_ACQUISITION_AND_VALIDATION_LEDGER.csv'
REGISTRY_PATH = ROOT/'20_JURISDICTIONS/JURISDICTION_RESEARCH_REGISTRY.csv'
QUEUE_PATH = ROOT/'90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv'
CONTEXT_PATH = ROOT/'00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md'
DOWNLOAD_LIST_PATH = ROOT/'86_NOTEBOOKLM/NOTEBOOKLM_DOWNLOAD_AND_UPLOAD_LIST.md'


def read_csv(path):
    with path.open('r', encoding='utf-8-sig', newline='') as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def write_csv(path, fields, rows):
    buf = io.StringIO(newline='')
    w = csv.DictWriter(buf, fieldnames=fields, lineterminator='\n', extrasaction='ignore')
    w.writeheader(); w.writerows(rows)
    path.write_text(buf.getvalue(), encoding='utf-8')


def upsert(rows, key_fields, new_row):
    key = tuple(new_row.get(k, '') for k in key_fields)
    for i,row in enumerate(rows):
        if tuple(row.get(k, '') for k in key_fields) == key:
            merged = dict(row); merged.update(new_row); rows[i] = merged; return
    rows.append(new_row)

# ---- Durable jurisdiction research artifacts ----
gbdir = ROOT/'20_JURISDICTIONS/GB'; gbdir.mkdir(parents=True, exist_ok=True)
rdir = ROOT/'95_RESEARCH/GB'; rdir.mkdir(parents=True, exist_ok=True)

inventory_fields = ['source_id','title','domain','authority','authority_class','official_url','document_id','enactment_or_publication_date','binding_state','currentness_state','primary_source_state','notebook_pack','caveat']
inventory_rows=[]
for s in SOURCES:
    inventory_rows.append({
        'source_id':s['source_id'],'title':s['title'],'domain':s['domain'],'authority':s['authority'],'authority_class':s['authority_class'],
        'official_url':s['url'],'document_id':s['document_id'],'enactment_or_publication_date':s['enactment'],'binding_state':s['binding_state'],
        'currentness_state':s['currentness'],'primary_source_state':'VERIFIED_OFFICIAL_SOURCE_IDENTITY_R009','notebook_pack':'NB05','caveat':s['notes']
    })
write_csv(gbdir/'GB_PRIMARY_SOURCE_INVENTORY_2026-09-14.csv', inventory_fields, inventory_rows)

matrix_fields=['source_id','layer','official_page_state','enactment_or_publication_date','commencement_or_application_state','binding_state','r009_use_state','required_next_recheck']
matrix_rows=[]
for s in SOURCES:
    if s['source_id'] <= 'GB-008':
        app='SECTION_OR_PROVISION_LEVEL_NOT_NORMALIZED_R009'
        nextcheck='Recheck exact provision text, amendments, commencement, territorial extent and any secondary instrument before material legal claim.'
    elif s['source_id']=='GB-009':
        app='NOT_APPLICABLE_POLICY_PROPOSAL'
        nextcheck='Recheck whether proposal was adopted, modified, closed or implemented; do not treat call for evidence as law.'
    else:
        app='NOT_APPLICABLE_NONBINDING_SOURCE'
        nextcheck='Recheck regulator/government update, replacement or withdrawal and underlying binding-law locator before material duty claim.'
    matrix_rows.append({'source_id':s['source_id'],'layer':s['domain'],'official_page_state':s['currentness'],'enactment_or_publication_date':s['enactment'],'commencement_or_application_state':app,'binding_state':s['binding_state'],'r009_use_state':'ELIGIBLE_WITH_STATED_LIMITS','required_next_recheck':nextcheck})
write_csv(gbdir/'GB_CURRENTNESS_AND_BINDING_STATE_MATRIX.csv', matrix_fields, matrix_rows)

map_md = '''# AI-LAWS — United Kingdom Sectoral AI / Data / Online Safety / Product Regulatory Map

**WORK_ITEM:** `AI-LAWS-R009`  
**RESEARCH_DATE:** 2026-09-14  
**LEVEL:** L1/L2 sectoral source architecture baseline  
**JURISDICTION_ID:** `GB` (repository identifier for United Kingdom)  
**LEGAL_ADVICE:** NO  
**AUTO_ADVANCE:** NO

## 1. Authority and method

R009 uses official UK sources only for the controlled baseline: `legislation.gov.uk`, GOV.UK, the Information Commissioner's Office and the Competition and Markets Authority. Ofcom's online-safety hub was probed but returned HTTP 403 to the GitHub runner; this is an access blocker, not evidence that the source or duties do not exist.

```text
EU_AI_ACT != UK_DOMESTIC_AI_STATUTE
POLICY_PROPOSAL != CURRENT_LAW
REGULATOR_GUIDANCE != STATUTE
ENACTMENT_DATE != UNIVERSAL_COMMENCEMENT_DATE
LATEST_AVAILABLE_REVISED != EVERY_PROVISION_CURRENTLY_IN_FORCE
SEARCH_FAILURE != NO_RULE
```

## 2. Controlled source baseline

The controlled inventory is `GB_PRIMARY_SOURCE_INVENTORY_2026-09-14.csv` and contains 13 official URL sources:

- `GB-001` UK GDPR;
- `GB-002` Data Protection Act 2018;
- `GB-003` Data (Use and Access) Act 2025;
- `GB-004` Online Safety Act 2023;
- `GB-005` Digital Markets, Competition and Consumers Act 2024;
- `GB-006` Consumer Rights Act 2015;
- `GB-007` Consumer Protection Act 1987;
- `GB-008` Product Regulation and Metrology Act 2025;
- `GB-009` AI Growth Lab call for evidence;
- `GB-010` Regulators' strategic approaches to AI;
- `GB-011` ICO Artificial Intelligence guidance hub;
- `GB-012` CMA AI Foundation Models initial review;
- `GB-013` AI Opportunities Action Plan: government response.

The first eight are binding-law source records. `GB-009..GB-013` are policy/regulator sources and must not be converted into statutory duties.

## 3. Binding-law layer

Official `legislation.gov.uk` identity and the `Latest available (Revised)` representation were verified for `GB-001..GB-008`. XML enactment-date attributes were separately verified:

```text
GB-001 = 2016-04-27
GB-002 = 2018-05-23
GB-003 = 2025-06-19
GB-004 = 2023-10-26
GB-005 = 2024-05-24
GB-006 = 2015-03-26
GB-007 = 1987-05-15
GB-008 = 2025-07-21
```

R009 does **not** infer commencement/application of every provision from these enactment dates. The official legislation pages expose changes/currentness/commencement material; exact section-level date state remains a later gate.

## 4. AI-governance policy and regulator layer

`GB-009` is a closed call for evidence for the proposed AI Growth Lab. Its official text describes targeted regulatory modifications under safeguards and monitoring. It is a **proposal/policy-development source**, not enacted law.

`GB-010` records strategic AI approaches requested from key regulators and is useful for mapping the sectoral regulator architecture, but it is not itself a statute.

`GB-011` is the ICO's official AI hub. It is regulator guidance and points to AI/decision-explanation/data-protection materials. The underlying UK GDPR/DPA provisions remain the legal authority.

`GB-012` is the CMA's official Foundation Models review page. It is regulatory/competition context, not a court holding or standalone binding AI law.

`GB-013` is a government AI policy paper. Later 2025/2026 regulation-policy materials also exist, so R009 does not freeze the 2025 Action Plan response as the sole current AI-regulation policy.

A 2026 GOV.UK page titled `Response to the AI Growth Lab call for evidence` was inspected and **not** promoted into the government-policy baseline: its body identifies it as the Biometrics and Surveillance Camera Commissioner's response to the call for evidence, not the government's own adoption decision.

## 5. Online safety and Ofcom limitation

The Online Safety Act source identity is verified. The Ofcom online-safety hub returned HTTP 403 from the GitHub Actions runner during R009. Therefore:

```text
OFCOM_HUB_ACCESS_STATE = HTTP_403_GITHUB_RUNNER
OFCOM_GUIDANCE_CURRENTNESS = NOT_VERIFIED_R009
OFCOM_ACCESS_FAILURE != NO_OFCOM_RULES
```

Provision-specific Online Safety Act duties, Ofcom codes/guidance, commencement regulations and enforcement procedure require a separate current-source recheck.

## 6. Product / consumer limitation

The Consumer Rights Act 2015, Consumer Protection Act 1987 and Product Regulation and Metrology Act 2025 establish relevant source layers. R009 does not decide whether any AI model, software, service or output is a product, digital content, service, unsafe product or defective product, and does not infer liability.

## 7. Territorial and devolution boundary

Repository jurisdiction ID `GB` labels the United Kingdom profile, but R009 does not assume every provision has identical territorial extent or effect across England and Wales, Scotland and Northern Ireland. Provision-specific extent, devolved competence and Northern-Ireland interfaces remain open where material.

## 8. Negative-findings boundary

R009 did not add a comprehensive UK AI statute to the controlled source set. This is **not** a definitive negative-law finding that no such law, bill, sector rule or later instrument exists.

```text
BOUNDED_SOURCE_MAP != EXHAUSTIVE_NEGATIVE_LEGAL_FINDING
NO_CONTROLLED_GENERAL_AI_ACT_SOURCE != NO_AI_LAW
```

## 9. Notebook routing

`GB-001..GB-013` are routed to `NB05_ASIA_AND_COMPARATIVE` for URL-direct ingestion. No repository binary, OCR derivative or Notebook upload is created by R009.

```text
NB05_UK_OFFICIAL_URL_SOURCE_SET = READY_13_WITH_LIMITS
NEW_BINARY_DOWNLOADS = 0
DERIVED_MARKDOWN_CREATED = 0
NOTEBOOK_UPLOADS = 0
CASE_LAW = NOT_ATTEMPTED
LIABILITY_CONCLUSION = NOT_ATTEMPTED
AUTO_ADVANCE = NO
```
'''
(gbdir/'GB_AI_DATA_ONLINE_SAFETY_PRODUCT_REGULATORY_MAP_2026-09-14.md').write_text(map_md,encoding='utf-8')

closeout='''# AI-LAWS-R009 — United Kingdom Sectoral Regulatory Baseline Closeout

**UNIT_ID:** `AI-LAWS-R009`  
**RESEARCH_DATE:** 2026-09-14  
**AUTO_ADVANCE:** NO

## Result

```text
CONTROLLED_OFFICIAL_URL_SOURCES = 13
BINDING_LEGISLATION_SOURCE_RECORDS = 8
POLICY_OR_REGULATOR_SOURCE_RECORDS = 5
LEGISLATION_ENACTMENT_DATE_ATTRIBUTES_VERIFIED = 8
SECTION_LEVEL_COMMENCEMENT_NORMALIZED = 0
OFCOM_ONLINE_SAFETY_HUB = HTTP_403_GITHUB_RUNNER
OFCOM_ACCESS_FAILURE_INTERPRETED_AS_SOURCE_ABSENCE = NO
AI_GROWTH_LAB = POLICY_PROPOSAL / CLOSED_CALL_FOR_EVIDENCE
AI_GROWTH_LAB_COMMISSIONER_RESPONSE_MISCLASSIFIED_AS_GOVERNMENT_RESPONSE = NO
EU_AI_ACT_IMPORTED_AS_UK_LAW = NO
COMPREHENSIVE_AI_ACT_NEGATIVE_FINDING = NOT_ATTEMPTED
NB05_UK_OFFICIAL_URL_SOURCE_SET = READY_13_WITH_LIMITS
NEW_BINARY_DOWNLOADS = 0
DERIVED_MARKDOWN_CREATED = 0
NOTEBOOK_UPLOADS = 0
CASE_LAW = NOT_ATTEMPTED
LIABILITY_CONCLUSION = NOT_ATTEMPTED
ZIP_OR_ARTIFACT_CREATED = NO
AUTO_ADVANCE = NO
```

## Safeguards

- Enactment date is not treated as universal provision commencement.
- `Latest available (Revised)` is not treated as proof that every provision is currently in force without qualification.
- AI Growth Lab material remains proposal/policy-development material.
- ICO/CMA materials remain regulator guidance/review, not statutes or court holdings.
- Ofcom HTTP 403 is preserved as an access blocker.
- EU AI Act is not imported into UK domestic law.
- Product/consumer source identity is not converted into AI defect, breach, causation or liability findings.
- Territorial/devolution questions and section-level currentness remain open where material.

## Stop condition

R009 stops at the L1/L2 sectoral source-architecture baseline.

```text
STOP = YES
AUTO_ADVANCE = NO
```
'''
(rdir/'AI-LAWS-R009_CLOSEOUT_2026-09-14.md').write_text(closeout,encoding='utf-8')

# ---- Manifest ----
fields, rows = read_csv(MANIFEST_PATH)
for s in SOURCES:
    upsert(rows,['source_id'],{
        'source_id':s['source_id'],'primary_pack':'NB05','jurisdiction':'GB','title':s['title'],'document_id':s['document_id'],
        'authority_class':s['authority_class'],'binding_state':s['binding_state'],'official_url':s['url'],'preferred_ingest':'URL_DIRECT_PREFERRED',
        'priority':s['priority'],'verification_state':'VERIFIED_OFFICIAL_URL_IDENTITY_R009_WITH_STATED_CURRENTNESS_LIMITS','last_verified':DATE,
        'rights_or_use_state':'OFFICIAL_PUBLIC_URL_REPO_VENDORING_RIGHTS_NOT_ASSESSED_R009','notes':s['notes']
    })
write_csv(MANIFEST_PATH,fields,rows)

# ---- Pack assignments ----
fields, rows = read_csv(PACK_PATH)
for s in SOURCES:
    upsert(rows,['pack_id','source_id'],{'pack_id':'NB05','source_id':s['source_id'],'requirement':s['requirement'],'reason':s['reason']})
write_csv(PACK_PATH,fields,rows)

# ---- Acquisition ledger ----
fields, rows = read_csv(LEDGER_PATH)
for s in SOURCES:
    if s['source_id'] <= 'GB-008':
        version='Official legislation.gov.uk Latest available (Revised) page verified; exact provision-level amendments/commencement/extent remain to be rechecked.'
        app='SECTION_LEVEL_NOT_NORMALIZED_R009'
        entry='SECTION_LEVEL_NOT_NORMALIZED_R009'
        content='WEB_OFFICIAL_IDENTITY_LATEST_AVAILABLE_REVISED_PAGE_VERIFIED'
        refresh='UK legislation amendment commencement extent secondary instrument or legislation.gov.uk revision'
    elif s['source_id']=='GB-009':
        version='Official GOV.UK closed call-for-evidence page verified; proposal/policy-development source only.'
        app='NOT_APPLICABLE_POLICY_PROPOSAL'; entry='NOT_APPLICABLE_POLICY_PROPOSAL'; content='WEB_OFFICIAL_GOVUK_CONTENT_IDENTITY_VERIFIED'
        refresh='Government adoption modification withdrawal implementation legislation or replacement AI Growth Lab policy'
    else:
        version='Official government/regulator page identity verified; nonbinding source; underlying law requires separate locator recheck.'
        app='NOT_APPLICABLE_NONBINDING'; entry='NOT_APPLICABLE_NONBINDING'; content='WEB_OFFICIAL_SOURCE_IDENTITY_VERIFIED'
        refresh='Government/regulator update replacement withdrawal or underlying-law change'
    upsert(rows,['batch_id','source_id'],{
        'batch_id':BATCH,'source_id':s['source_id'],'notebook_pack':'NB05','jurisdiction':'GB','title':s['title'],'document_id':s['document_id'],
        'issuing_authority':s['authority'],'authority_class':s['authority_class'],'binding_state':s['binding_state'],'official_url':s['url'],
        'retrieval_date':DATE,'version_state':version,'adoption_date':s['enactment'],'publication_date':s['enactment'],
        'entry_into_force_date':entry,'application_date':app,'authentic_language':'English','translation_state':'NOT_APPLICABLE',
        'rights_state':'OFFICIAL_PUBLIC_URL_REPO_VENDORING_RIGHTS_NOT_ASSESSED_R009','acquisition_method':'URL_DIRECT_PREFERRED','local_filename_or_url':s['url'],
        'sha256':'','byte_size':'','content_type':'text/html official URL source','content_identity_checked':content,'notebook_name':'NB05_ASIA_AND_COMPARATIVE',
        'notebook_ingest_date':'','notebook_ingest_state':'NOT_RUN','notebook_locator_test':'NOT_RUN','primary_source_recheck_state':'REQUIRED_BEFORE_MATERIAL_CLAIM',
        'refresh_trigger':refresh,'human_review_required':'NO_FOR_L1_SOURCE_MAP; YES_BEFORE_MATERIAL_LEGAL_CONCLUSION','notes':s['notes']
    })
write_csv(LEDGER_PATH,fields,rows)

# ---- Jurisdiction registry ----
fields, rows = read_csv(REGISTRY_PATH)
for i,row in enumerate(rows):
    if row.get('jurisdiction_id')=='GB':
        row['research_state']='SECTORAL_AI_DATA_ONLINE_SAFETY_PRODUCT_L1_L2_BASELINE_COMPLETE_SECTION_LEVEL_CURRENTNESS_OPEN'
        row['notes']='R009 completed 2026-09-14: 13-source official URL baseline across UK GDPR/data, online safety, competition/consumer, product regulation and nonbinding AI policy/regulator layers. Section-level commencement/currentness, Ofcom guidance (runner HTTP 403), devolved/NI extent, sector rules, case law and liability remain open. EU AI Act is not treated as UK domestic law.'
        rows[i]=row
        break
write_csv(REGISTRY_PATH,fields,rows)

# ---- Queue ----
fields, rows = read_csv(QUEUE_PATH)
for i,row in enumerate(rows):
    if row.get('work_item_id')=='AI-LAWS-R009':
        row['state']='COMPLETE_RESEARCH_BASELINE_L1_L2_SECTORAL_MAP_CURRENTNESS_OPEN'
        row['expected_output']='20_JURISDICTIONS/GB/GB_AI_DATA_ONLINE_SAFETY_PRODUCT_REGULATORY_MAP_2026-09-14.md; 20_JURISDICTIONS/GB/GB_PRIMARY_SOURCE_INVENTORY_2026-09-14.csv; 20_JURISDICTIONS/GB/GB_CURRENTNESS_AND_BINDING_STATE_MATRIX.csv; 95_RESEARCH/GB/AI-LAWS-R009_CLOSEOUT_2026-09-14.md'
        row['stop_condition']='L1/L2 sectoral source architecture complete; stop before section-level commencement/currentness normalization, Ofcom code/guidance verification, devolved/NI analysis, exhaustive sector law, case law, comprehensive-AI-statute negative finding or liability conclusions'
        rows[i]=row
        break
write_csv(QUEUE_PATH,fields,rows)

# ---- Current context ----
ctx=CONTEXT_PATH.read_text(encoding='utf-8')
ctx=ctx.replace('R008_CN_PRIMARY_SOURCE_MAP_L1_COMPLETE / R021_COMPLETE','R008_CN_PRIMARY_SOURCE_MAP_L1_COMPLETE / R009_UK_SECTORAL_L1_L2_COMPLETE / R021_COMPLETE',1)
ctx=ctx.replace('AI-LAWS-R008 = COMPLETE_RESEARCH_BASELINE_L1_PRIMARY_SOURCE_MAP\n','AI-LAWS-R008 = COMPLETE_RESEARCH_BASELINE_L1_PRIMARY_SOURCE_MAP\nAI-LAWS-R009 = COMPLETE_RESEARCH_BASELINE_L1_L2_SECTORAL_MAP_CURRENTNESS_OPEN\n',1)
r009_section='''### R009 — United Kingdom sectoral AI / data / online-safety / product baseline

R009 established a 13-source official URL baseline across binding UK legislation and explicitly nonbinding AI policy/regulator sources.

```text
GB_CONTROLLED_OFFICIAL_URL_SOURCES = 13
GB_BINDING_LEGISLATION_SOURCE_RECORDS = 8
GB_POLICY_OR_REGULATOR_SOURCE_RECORDS = 5
GB_LEGISLATION_ENACTMENT_DATES_VERIFIED = 8
GB_SECTION_LEVEL_COMMENCEMENT_NORMALIZED = 0
GB_OFCOM_HUB_ACCESS = HTTP_403_GITHUB_RUNNER
GB_AI_GROWTH_LAB = POLICY_PROPOSAL / CLOSED_CALL_FOR_EVIDENCE
GB_EU_AI_ACT_IMPORTED_AS_DOMESTIC_LAW = NO
GB_COMPREHENSIVE_AI_ACT_NEGATIVE_FINDING = NOT_ATTEMPTED
NB05_UK_OFFICIAL_URL_SOURCE_SET = READY_13_WITH_LIMITS
CASE_LAW = NOT_ATTEMPTED
LIABILITY_CONCLUSION = NOT_ATTEMPTED
```

Durable outputs are under `20_JURISDICTIONS/GB/` plus `95_RESEARCH/GB/AI-LAWS-R009_CLOSEOUT_2026-09-14.md`.

`ENACTMENT_DATE != UNIVERSAL_COMMENCEMENT_DATE`, `POLICY_PROPOSAL != CURRENT_LAW`, `REGULATOR_GUIDANCE != STATUTE`, and `EU_AI_ACT != UK_DOMESTIC_AI_STATUTE` remain controlling boundaries.

'''
if '### R009 — United Kingdom sectoral' not in ctx:
    marker='### R021\n'
    if marker not in ctx: raise SystemExit('CURRENT_CONTEXT insertion marker missing')
    ctx=ctx.replace(marker,r009_section+marker,1)
CONTEXT_PATH.write_text(ctx,encoding='utf-8')

# ---- Human-readable Notebook URL list ----
dl=DOWNLOAD_LIST_PATH.read_text(encoding='utf-8')
uk_section='''## E3. NB05 — Comparative / United Kingdom URL source set

R009 established a 13-source official URL baseline for the United Kingdom. Use URL-direct ingestion. No dedicated repository binary set is created by R009.

- `GB-001` https://www.legislation.gov.uk/eur/2016/679/contents
- `GB-002` https://www.legislation.gov.uk/ukpga/2018/12/contents
- `GB-003` https://www.legislation.gov.uk/ukpga/2025/18/contents
- `GB-004` https://www.legislation.gov.uk/ukpga/2023/50/contents
- `GB-005` https://www.legislation.gov.uk/ukpga/2024/13/contents
- `GB-006` https://www.legislation.gov.uk/ukpga/2015/15/contents
- `GB-007` https://www.legislation.gov.uk/ukpga/1987/43/contents
- `GB-008` https://www.legislation.gov.uk/ukpga/2025/20/contents
- `GB-009` https://www.gov.uk/government/calls-for-evidence/ai-growth-lab
- `GB-010` https://www.gov.uk/government/publications/regulators-strategic-approaches-to-ai
- `GB-011` https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/
- `GB-012` https://www.gov.uk/cma-cases/ai-foundation-models-initial-review
- `GB-013` https://www.gov.uk/government/publications/ai-opportunities-action-plan-government-response

```text
NB05_UK_OFFICIAL_URL_SOURCE_SET = READY_13_WITH_LIMITS
BINDING_LAW_AND_POLICY_SEPARATED = YES
SECTION_LEVEL_CURRENTNESS_RECHECK_REQUIRED = YES
OFCOM_HUB = HTTP_403_GITHUB_RUNNER
REPOSITORY_BINARY_SET = NONE
NOTEBOOK_UPLOAD = NOT_RUN
```

Do not use enactment date as universal commencement. Do not treat AI Growth Lab, ICO/CMA material or government policy papers as statutes. Do not import the EU AI Act as UK domestic law.

---

'''
if '## E3. NB05 — Comparative / United Kingdom URL source set' not in dl:
    marker='## F. NB06 — Human sovereignty / neurotechnology'
    if marker not in dl: raise SystemExit('DOWNLOAD list insertion marker missing')
    dl=dl.replace(marker,uk_section+marker,1)
DOWNLOAD_LIST_PATH.write_text(dl,encoding='utf-8')

# ---- Assertions ----
assert len(SOURCES)==13
assert all(s['source_id'].startswith('GB-') for s in SOURCES)
assert len({s['source_id'] for s in SOURCES})==13
assert 'AI-LAWS-R009 = COMPLETE_RESEARCH_BASELINE_L1_L2_SECTORAL_MAP_CURRENTNESS_OPEN' in CONTEXT_PATH.read_text(encoding='utf-8')
assert 'GB-013' in MANIFEST_PATH.read_text(encoding='utf-8')
assert 'NB05,GB-013' in PACK_PATH.read_text(encoding='utf-8')
assert BATCH in LEDGER_PATH.read_text(encoding='utf-8')
print('R009_DURABLE_GENERATION=PASS')
print('CONTROLLED_SOURCES=13')
print('ZIP_OR_ARTIFACT_CREATED=NO')
print('AUTO_ADVANCE=NO')
