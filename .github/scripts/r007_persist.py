from pathlib import Path
import csv, io

DATE='2026-09-14'

states=[
('US-AL','Alabama'),('US-AK','Alaska'),('US-AZ','Arizona'),('US-AR','Arkansas'),('US-CA','California'),('US-CO','Colorado'),('US-CT','Connecticut'),('US-DE','Delaware'),('US-FL','Florida'),('US-GA','Georgia'),('US-HI','Hawaii'),('US-ID','Idaho'),('US-IL','Illinois'),('US-IN','Indiana'),('US-IA','Iowa'),('US-KS','Kansas'),('US-KY','Kentucky'),('US-LA','Louisiana'),('US-ME','Maine'),('US-MD','Maryland'),('US-MA','Massachusetts'),('US-MI','Michigan'),('US-MN','Minnesota'),('US-MS','Mississippi'),('US-MO','Missouri'),('US-MT','Montana'),('US-NE','Nebraska'),('US-NV','Nevada'),('US-NH','New Hampshire'),('US-NJ','New Jersey'),('US-NM','New Mexico'),('US-NY','New York'),('US-NC','North Carolina'),('US-ND','North Dakota'),('US-OH','Ohio'),('US-OK','Oklahoma'),('US-OR','Oregon'),('US-PA','Pennsylvania'),('US-RI','Rhode Island'),('US-SC','South Carolina'),('US-SD','South Dakota'),('US-TN','Tennessee'),('US-TX','Texas'),('US-UT','Utah'),('US-VT','Vermont'),('US-VA','Virginia'),('US-WA','Washington'),('US-WV','West Virginia'),('US-WI','Wisconsin'),('US-WY','Wyoming'),('US-DC','District of Columbia')]

Path('20_JURISDICTIONS/US').mkdir(parents=True, exist_ok=True)
Path('95_RESEARCH/US').mkdir(parents=True, exist_ok=True)

federal_rows=[
['US-001','Executive Order 14179 — Removing Barriers to American Leadership in Artificial Intelligence','EXECUTIVE_ORDER','FEDERAL_EXECUTIVE_DIRECTIVE_NOT_ACT_OF_CONGRESS','LIVE_WHITE_HOUSE_HTML_RECHECKED_2026-09-14','repository print snapshot supporting-only; live HTML controls current text','Do not label as an Act of Congress'],
['US-002',"America's AI Action Plan",'OFFICIAL_POLICY_PLAN','NONBINDING_EXECUTIVE_POLICY_PLAN','OFFICIAL_WHITE_HOUSE_PDF_EXACT_MATCH_R028','verified official PDF snapshot','Policy plan != statute'],
['US-003','OMB M-25-21','OMB_MEMORANDUM','EXECUTIVE_BRANCH_OPERATIONAL_MEMORANDUM_WITHIN_SCOPE','OFFICIAL_OMB_PDF_EXACT_MATCH_R028','verified official PDF snapshot','Agency-scope memorandum != generally applicable federal statute'],
['US-004','OMB M-25-22','OMB_MEMORANDUM','FEDERAL_ACQUISITION_MEMORANDUM_WITHIN_SCOPE','OFFICIAL_OMB_PDF_EXACT_MATCH_R028','verified official PDF snapshot','Procurement memorandum != Act of Congress'],
['US-005','Executive Order 14365 — Ensuring a National Policy Framework for Artificial Intelligence','EXECUTIVE_ORDER','FEDERAL_EXECUTIVE_DIRECTIVE_NOT_ACT_OF_CONGRESS','OFFICIAL_GOVINFO_FEDERAL_REGISTER_PDF_EXACT_MATCH_R031','Federal Register document 2025-23092 exact bytes verified','Executive order != statute enacted by Congress'],
['US-006','OMB M-26-04','OMB_MEMORANDUM','EXECUTIVE_BRANCH_OPERATIONAL_MEMORANDUM_WITHIN_SCOPE','OFFICIAL_OMB_PDF_EXACT_MATCH_R028','verified official PDF snapshot','Agency memorandum != generally applicable federal statute'],
['US-007','NIST AI RMF 1.0','VOLUNTARY_FRAMEWORK','VOLUNTARY_OFFICIAL_FRAMEWORK','OFFICIAL_NIST_PDF_EXACT_MATCH_R028_AND_LIVE_PAGE_RECHECKED_R007','NIST states revision activity; refresh before material use','Framework != statute or automatic standard of care'],
['US-008','NIST AI RMF Generative AI Profile','VOLUNTARY_PROFILE','VOLUNTARY_OFFICIAL_PROFILE','OFFICIAL_NIST_PDF_EXACT_MATCH_R028','verified official PDF snapshot','Profile != statute or automatic legal duty'],
]
with open('20_JURISDICTIONS/US/US_FEDERAL_AI_SOURCE_CLASSIFICATION_2026-09-14.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f,lineterminator='\n')
    w.writerow(['source_id','title','instrument_class','binding_or_operational_state','verification_state','current_source_note','claim_limit'])
    w.writerows(federal_rows)

state_rows=[]
for jid,name in states:
    if jid=='US-UT':
        state_rows.append([jid,name,'SUBNATIONAL_STATE','CURRENT_AI_SPECIFIC_STATUTE_SOURCE_VERIFIED_L1','Utah Code Title 13 Chapter 72 — Artificial Intelligence Policy Act','https://le.utah.gov/xcode/Title13/Chapter72/13-72.html','Section 13-72-101 current version C13-72-S101_2026050620260506 verified; effective 2026-05-06; affected by 63I-2-213 on 2027-07-01','CURRENT_CHAPTER_IDENTITY_AND_SECTION101_BODY_VERIFIED_WHOLE_CHAPTER_SECTION_BY_SECTION_OPEN',DATE,'Old 2024 whole-chapter PDF is not current-law authority; concrete duties require section-by-section currentness recheck'])
    elif jid=='US-TX':
        state_rows.append([jid,name,'SUBNATIONAL_STATE','OFFICIAL_CODE_PORTAL_REACHABLE_CONTENT_UNRESOLVED','Candidate Texas Business & Commerce Code Chapter 552 endpoint','https://statutes.capitol.texas.gov/Docs/BC/htm/BC.552.htm','Official portal returned client-rendered shell; substantive chapter identity/effective state not admitted by R007','RESEARCH_REQUIRED',DATE,'Reachable portal != verified enacted/current AI-law content'])
    else:
        jtype='FEDERAL_DISTRICT' if jid=='US-DC' else 'SUBNATIONAL_STATE'
        state_rows.append([jid,name,jtype,'ENUMERATED_RESEARCH_REQUIRED','','','','RESEARCH_REQUIRED',DATE,'No negative inference: unverified in R007 does not mean no AI-related law exists'])
with open('20_JURISDICTIONS/US/US_STATE_AI_LAW_RESEARCH_REGISTRY.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f,lineterminator='\n')
    w.writerow(['jurisdiction_id','name','jurisdiction_type','r007_state','verified_instrument_or_candidate','official_source','verified_date_or_version_signal','verification_state','last_checked','notes'])
    w.writerows(state_rows)

architecture='''# AI-LAWS — United States Federal + State AI-Law Inventory Architecture\n\n**WORK_ITEM:** `AI-LAWS-R007`\n**RESEARCH_DATE:** 2026-09-14\n**LEVEL:** L1 inventory architecture + bounded current-source verification\n**LEGAL_ADVICE:** NO\n**AUTO_ADVANCE:** NO\n\n## 1. Purpose\n\nR007 establishes a federal/state source architecture without collapsing executive orders, OMB memoranda, voluntary NIST frameworks, enacted statutes, pending bills and unverified search results into one category.\n\n```text\nEXECUTIVE_ORDER != ACT_OF_CONGRESS\nOMB_MEMORANDUM != GENERALLY_APPLICABLE_FEDERAL_STATUTE\nNIST_FRAMEWORK != STATUTE\nPROPOSED_BILL != ENACTED_LAW\nSTATE_PORTAL_REACHABLE != STATE_LAW_CURRENTNESS_VERIFIED\nSEARCH_FAILURE != NO_STATE_AI_LAW\n```\n\n## 2. Federal controlled-source layer\n\n`US_FEDERAL_AI_SOURCE_CLASSIFICATION_2026-09-14.csv` classifies the existing controlled `US-001..US-008` source set. R007 does not claim that those eight sources exhaust all federal statutes, regulations, agency rules or sector-specific law that may govern AI.\n\nThe controlled federal layer contains executive orders, executive policy/guidance, OMB memoranda and voluntary NIST frameworks/profiles. None is relabeled as an Act of Congress. Sectoral statutes and regulations remain separate research work.\n\n## 3. State architecture\n\n`US_STATE_AI_LAW_RESEARCH_REGISTRY.csv` enumerates all 50 States plus the District of Columbia. Enumeration is coverage architecture, not a claim that each jurisdiction has or lacks an AI-specific statute.\n\nAs of this bounded unit:\n\n```text\nSTATE_OR_DC_JURISDICTIONS_ENUMERATED = 51\nCURRENT_AI_SPECIFIC_STATUTE_SOURCE_VERIFIED_L1 = 1  # Utah\nOFFICIAL_CODE_PORTAL_REACHABLE_CONTENT_UNRESOLVED = 1  # Texas candidate endpoint\nRESEARCH_REQUIRED = 49\n```\n\n## 4. Utah current-law pin\n\nThe Utah Legislature Xcode current wrapper identifies Title 13 Chapter 72. The current-version body for Section 13-72-101 is `C13-72-S101_2026050620260506.html` and states:\n\n- Chapter 72: Artificial Intelligence Policy Act;\n- Section 13-72-101: Definitions;\n- effective date: 5/6/2026;\n- affected by Section 63I-2-213 on 7/1/2027.\n\nR007 therefore resolves the prior `US-009` currentness blocker at the chapter-identity / Section 101 level. It does **not** claim that every section in Chapter 72 was independently re-read and currentness-verified in this unit.\n\n```text\nUS009_CURRENT_CHAPTER_IDENTITY = VERIFIED\nUS009_SECTION_101_CURRENT_BODY = VERIFIED\nUS009_SECTION_101_EFFECTIVE_DATE = 2026-05-06\nUS009_FUTURE_CHANGE_SIGNAL = 2027-07-01\nUS009_WHOLE_CHAPTER_SECTION_BY_SECTION_CURRENTNESS = OPEN\n```\n\n## 5. Texas boundary\n\nThe official Texas statutes endpoint tested by R007 returned a client-rendered shell. R007 therefore does not infer title, content, effective date or enacted/current status from that endpoint. Texas remains `RESEARCH_REQUIRED`.\n\n## 6. Federal-state conflict boundary\n\nR007 records federal executive policy sources but does not decide constitutional preemption, Supremacy Clause questions, validity of state-law restrictions, private rights of action, enforcement authority or litigation outcomes. Those questions require instrument-specific law and facts.\n\n## 7. Stop boundary\n\nR007 stops before:\n\n- an exhaustive 50-state substantive law survey;\n- sector-by-sector federal statutory/regulatory analysis;\n- pending-bill tracking across every legislature;\n- case law;\n- preemption conclusions;\n- compliance advice, breach, liability, remedies or sanctions.\n\n```text\nR007_US_INVENTORY_ARCHITECTURE = COMPLETE_L1\nFEDERAL_CONTROLLED_SOURCE_CLASSIFICATION = COMPLETE_FOR_US001_US008\nSTATE_JURISDICTIONS_ENUMERATED = 51\nSTATE_CURRENT_LAW_CONTENT = PARTIAL\nUTAH_US009_CURRENTNESS = VERIFIED_AT_CHAPTER_IDENTITY_SECTION101_LEVEL\nCASE_LAW = NOT_ATTEMPTED\nLIABILITY_CONCLUSION = NOT_ATTEMPTED\nZIP_OR_ARTIFACT_CREATED = NO\nAUTO_ADVANCE = NO\n```\n'''
Path('20_JURISDICTIONS/US/US_AI_LAW_INVENTORY_ARCHITECTURE_2026-09-14.md').write_text(architecture,encoding='utf-8')

utah='''# AI-LAWS — Utah Artificial Intelligence Policy Act Current Codification Pin\n\n**SOURCE_ID:** `US-009`\n**RESEARCH_DATE:** 2026-09-14\n**AUTHORITY:** Utah Legislature / Utah Code Xcode\n**LEGAL_ADVICE:** NO\n\nOfficial current chapter wrapper:\n`https://le.utah.gov/xcode/Title13/Chapter72/13-72.html`\n\nVerified current Section 13-72-101 body:\n`https://le.utah.gov/xcode/Title13/Chapter72/C13-72-S101_2026050620260506.html`\n\nThe official current-version body identifies Chapter 72 as the **Artificial Intelligence Policy Act**, Section 13-72-101 as **Definitions**, and states **Effective 5/6/2026**. It also carries a future-change signal: **Affected by 63I-2-213 on 7/1/2027**.\n\n```text\nCURRENT_CHAPTER_IDENTITY = VERIFIED\nSECTION_101_CURRENT_VERSION_ID = C13-72-S101_2026050620260506\nSECTION_101_EFFECTIVE_DATE = 2026-05-06\nFUTURE_CHANGE_SIGNAL = 2027-07-01\nWHOLE_CHAPTER_SECTION_BY_SECTION_CURRENTNESS = NOT_EXHAUSTIVELY_RECHECKED\nOLD_2024_WHOLE_CHAPTER_PDF = SUPERSEDED_FOR_CURRENT_LAW_USE\n```\n\nThis record does not infer the current text/effective date of every other Chapter 72 section. Concrete legal analysis must open the current section-specific Xcode body at the time of use.\n'''
Path('20_JURISDICTIONS/US/UTAH_AIPA_CURRENT_CODIFICATION_2026-09-14.md').write_text(utah,encoding='utf-8')

closeout='''# AI-LAWS-R007 — United States Federal + State Inventory Architecture Closeout\n\n**UNIT_ID:** `AI-LAWS-R007`\n**RESEARCH_DATE:** 2026-09-14\n**ROLE:** LEGAL_ANALYST / RESEARCHER\n**AUTO_ADVANCE:** NO\n\n## Result\n\n```text\nFEDERAL_CONTROLLED_SOURCES_CLASSIFIED = 8\nSTATE_PLUS_DC_JURISDICTIONS_ENUMERATED = 51\nUTAH_CURRENT_CHAPTER_IDENTITY_VERIFIED = YES\nUTAH_SECTION101_CURRENT_BODY_VERIFIED = YES\nUTAH_SECTION101_EFFECTIVE_DATE = 2026-05-06\nUTAH_FUTURE_CHANGE_SIGNAL = 2027-07-01\nTEXAS_OFFICIAL_PORTAL_REACHABLE = YES\nTEXAS_SUBSTANTIVE_CURRENT_LAW_CONTENT_VERIFIED = NO\nOTHER_STATE_SUBSTANTIVE_CURRENT_LAW_RESEARCH = OPEN\nFEDERAL_ACT_OF_CONGRESS_EXHAUSTIVE_INVENTORY = NOT_ATTEMPTED\nCASE_LAW = NOT_ATTEMPTED\nPREEMPTION_CONCLUSION = NOT_ATTEMPTED\nLIABILITY_CONCLUSION = NOT_ATTEMPTED\nNEW_BINARY_DOWNLOADS = 0\nNOTEBOOK_UPLOADS = 0\nZIP_OR_ARTIFACT_CREATED = NO\nAUTO_ADVANCE = NO\n```\n\nR007 is complete as an L1 federal/state inventory architecture. It does not represent a complete 50-state substantive AI-law survey.\n\n## Stop condition\n\nNo state is labeled `NO_LAW` because R007 did not verify an AI-specific statute. No proposal is treated as enacted law. No executive order, OMB memorandum or NIST framework is treated as an Act of Congress.\n'''
Path('95_RESEARCH/US/AI-LAWS-R007_CLOSEOUT_2026-09-14.md').write_text(closeout,encoding='utf-8')

# Patch jurisdiction registry: enumerate all states + DC, update US row and US-UT if present.
reg=Path('20_JURISDICTIONS/JURISDICTION_RESEARCH_REGISTRY.csv')
rows=list(csv.DictReader(reg.open(encoding='utf-8'))); fields=list(rows[0].keys())
byid={r['jurisdiction_id']:r for r in rows}
if 'US' in byid:
    byid['US']['research_state']='FEDERAL_STATE_INVENTORY_ARCHITECTURE_L1_COMPLETE_STATE_LAW_CONTENT_OPEN'
    byid['US']['notes']='R007 enumerated all 50 states plus DC and classified controlled federal US-001..US-008. Utah current Chapter 72 identity / Section 13-72-101 current body verified 2026-09-14; other state-law content remains source-by-source research. Executive orders/OMB/NIST are not Acts of Congress.'
for jid,name in states:
    rec=byid.get(jid,{k:'' for k in fields})
    rec['jurisdiction_id']=jid; rec['name']=name
    rec['jurisdiction_type']='FEDERAL_DISTRICT' if jid=='US-DC' else 'SUBNATIONAL_STATE'
    rec['region']='NORTH_AMERICA'; rec['priority']='P0' if jid in ('US-CA','US-CO','US-TX','US-UT','US-NY') else 'P1'
    rec['initial_focus']='AI-specific statutes; privacy/biometrics; consumer; employment; sector law; preemption interfaces'
    if jid=='US-UT':
        rec['research_state']='R007_CURRENT_AI_SPECIFIC_STATUTE_SOURCE_VERIFIED_L1'
        rec['notes']='Utah Code Title 13 Chapter 72 current identity verified; Section 13-72-101 current version C13-72-S101_2026050620260506 effective 2026-05-06; future-change signal 2027-07-01; whole chapter section-by-section currentness remains open.'
    elif jid=='US-TX':
        rec['research_state']='R007_OFFICIAL_CODE_PORTAL_REACHABLE_CONTENT_UNRESOLVED'
        rec['notes']='Candidate official Business & Commerce Code Chapter 552 endpoint reachable but client-rendered shell prevented substantive identity/currentness verification; preserve RESEARCH_REQUIRED.'
    else:
        rec['research_state']='R007_ENUMERATED_STATE_RESEARCH_REQUIRED'
        rec['notes']='Enumerated for 50-state + DC coverage. No negative inference; R007 did not verify whether an AI-specific statute is enacted/current here.'
    byid[jid]=rec
# preserve existing order, then append missing US subjurisdictions in state-list order
out=[]; seen=set()
for r in rows:
    jid=r['jurisdiction_id']
    out.append(byid[jid]); seen.add(jid)
for jid,_ in states:
    if jid not in seen: out.append(byid[jid])
with reg.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n'); w.writeheader(); w.writerows(out)

# Patch acquisition manifest US-009.
manifest=Path('86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv')
mr=list(csv.DictReader(manifest.open(encoding='utf-8'))); mf=list(mr[0].keys())
found=False
for r in mr:
    if r['source_id']=='US-009':
        found=True
        r['title']='Utah Artificial Intelligence Policy Act — current codification'
        r['document_id']='Utah Code Title 13 Chapter 72'
        r['official_url']='https://le.utah.gov/xcode/Title13/Chapter72/13-72.html'
        r['preferred_ingest']='URL_DIRECT_PREFERRED'
        r['verification_state']='CURRENT_CHAPTER_IDENTITY_AND_SECTION101_VERSION_VERIFIED_2026-09-14_WHOLE_CHAPTER_SECTION_BY_SECTION_OPEN'
        r['last_verified']=DATE
        r['notes']='Current chapter wrapper verified. Section 13-72-101 current version C13-72-S101_2026050620260506 states Effective 5/6/2026 and future-change signal 7/1/2027. Prior 2024 whole-chapter PDF is superseded for current-law use; recheck each material section before legal conclusions.'
assert found
with manifest.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=mf,lineterminator='\n'); w.writeheader(); w.writerows(mr)

# Append R007 US-009 ledger row if not already present.
ledger=Path('86_NOTEBOOKLM/NOTEBOOKLM_ACQUISITION_AND_VALIDATION_LEDGER.csv')
lr=list(csv.DictReader(ledger.open(encoding='utf-8'))); lf=list(lr[0].keys())
batch='R007-US-STATE-20260914-001'
if not any(r['batch_id']==batch and r['source_id']=='US-009' for r in lr):
    rec={k:'' for k in lf}
    rec.update({
      'batch_id':batch,'source_id':'US-009','notebook_pack':'NB03','jurisdiction':'US-UT','title':'Utah Artificial Intelligence Policy Act — current codification','document_id':'Utah Code Title 13 Chapter 72','issuing_authority':'Utah Legislature','authority_class':'STATUTE_OR_REGULATION','binding_state':'state statute; section-specific effective/currentness state required','official_url':'https://le.utah.gov/xcode/Title13/Chapter72/13-72.html','retrieval_date':DATE,'version_state':'Current chapter identity verified; Section 13-72-101 current version C13-72-S101_2026050620260506','application_date':'SECTION_101_EFFECTIVE_2026-05-06; WHOLE_CHAPTER_NOT_EXHAUSTIVELY_VERIFIED','authentic_language':'English','translation_state':'NOT_APPLICABLE','rights_state':'OFFICIAL_PUBLIC_URL','acquisition_method':'URL_DIRECT_PREFERRED','local_filename_or_url':'https://le.utah.gov/xcode/Title13/Chapter72/13-72.html','content_type':'text/html','content_identity_checked':'CURRENT_CHAPTER_IDENTITY_AND_SECTION101_BODY_VERIFIED','notebook_ingest_state':'NOT_RUN','notebook_locator_test':'NOT_RUN','primary_source_recheck_state':'R007_CURRENTNESS_PIN_SECTION101','refresh_trigger':'Utah Xcode version change; material section use; 2027-07-01 future-change signal','human_review_required':'YES_FOR_CONCRETE_DUTY_OR_ENFORCEMENT_CONCLUSION','notes':'R007 resolved prior currentness blocker at chapter identity / Section 101 level. Old 2024 whole-chapter snapshot must not be treated as current law. No whole-chapter section-by-section currentness claim.'})
    lr.append(rec)
with ledger.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=lf,lineterminator='\n'); w.writeheader(); w.writerows(lr)

# Patch research queue R007 only.
q=Path('90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv')
qr=list(csv.DictReader(q.open(encoding='utf-8'))); qf=list(qr[0].keys())
for r in qr:
    if r['work_item_id']=='AI-LAWS-R007':
        r['state']='COMPLETE_RESEARCH_ARCHITECTURE_L1_STATE_LAW_CONTENT_OPEN'
        r['expected_output']='20_JURISDICTIONS/US/US_AI_LAW_INVENTORY_ARCHITECTURE_2026-09-14.md; 20_JURISDICTIONS/US/US_FEDERAL_AI_SOURCE_CLASSIFICATION_2026-09-14.csv; 20_JURISDICTIONS/US/US_STATE_AI_LAW_RESEARCH_REGISTRY.csv; 20_JURISDICTIONS/US/UTAH_AIPA_CURRENT_CODIFICATION_2026-09-14.md; 95_RESEARCH/US/AI-LAWS-R007_CLOSEOUT_2026-09-14.md'
        r['stop_condition']='Federal/state architecture complete; Utah current source pinned at chapter identity/Section101 level; stop before exhaustive 50-state law content, case law, preemption or liability conclusions'
        break
else: raise SystemExit('R007 row missing')
with q.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=qf,lineterminator='\n'); w.writeheader(); w.writerows(qr)

# Patch current context with compact durable section.
ctx=Path('00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md')
s=ctx.read_text(encoding='utf-8')
s=s.replace('R004_CETS225_L1_L2_COMPLETE / R021_COMPLETE','R004_CETS225_L1_L2_COMPLETE / R007_US_INVENTORY_ARCHITECTURE_L1_COMPLETE / R021_COMPLETE',1)
s=s.replace('AI-LAWS-R004 = COMPLETE_RESEARCH_BASELINE_L1_L2\n','AI-LAWS-R004 = COMPLETE_RESEARCH_BASELINE_L1_L2\nAI-LAWS-R007 = COMPLETE_RESEARCH_ARCHITECTURE_L1_STATE_LAW_CONTENT_OPEN\n',1)
anchor='### R021\n'
section='''### R007 — United States federal + state AI-law inventory architecture\n\nR007 enumerated all 50 States plus the District of Columbia and classified the controlled federal `US-001..US-008` source set without converting executive/guidance/framework sources into Acts of Congress.\n\n```text\nUS_STATE_PLUS_DC_JURISDICTIONS_ENUMERATED = 51\nUS_FEDERAL_CONTROLLED_SOURCES_CLASSIFIED = 8\nUS009_UTAH_CURRENT_CHAPTER_IDENTITY = VERIFIED\nUS009_UTAH_SECTION101_CURRENT_VERSION = C13-72-S101_2026050620260506\nUS009_UTAH_SECTION101_EFFECTIVE_DATE = 2026-05-06\nUS009_UTAH_FUTURE_CHANGE_SIGNAL = 2027-07-01\nUS009_WHOLE_CHAPTER_SECTION_BY_SECTION_CURRENTNESS = OPEN\nTEXAS_CANDIDATE_OFFICIAL_CODE_PORTAL = REACHABLE_CONTENT_UNRESOLVED\nOTHER_STATE_SUBSTANTIVE_CURRENT_LAW_RESEARCH = OPEN\nCASE_LAW = NOT_ATTEMPTED\nPREEMPTION_CONCLUSION = NOT_ATTEMPTED\nLIABILITY_CONCLUSION = NOT_ATTEMPTED\n```\n\nDurable outputs are under `20_JURISDICTIONS/US/` plus `95_RESEARCH/US/AI-LAWS-R007_CLOSEOUT_2026-09-14.md`.\n\n`EXECUTIVE_ORDER != ACT_OF_CONGRESS`, `PROPOSED_BILL != ENACTED_LAW`, and `SEARCH_FAILURE != NO_STATE_AI_LAW` remain controlling boundaries.\n\n'''
if section not in s:
    if anchor not in s: raise SystemExit('context anchor missing')
    s=s.replace(anchor,section+anchor,1)
# integrity counters before NOTEBOOK_UPLOAD_COUNT
needle='NOTEBOOK_UPLOAD_COUNT = 0\n'
insert='''R007_US_STATE_PLUS_DC_ENUMERATED = 51\nR007_US_FEDERAL_CONTROLLED_SOURCES_CLASSIFIED = 8\nR007_US009_UTAH_CURRENT_SECTION101_VERIFIED = YES\nR007_US009_UTAH_SECTION101_EFFECTIVE_DATE = 2026-05-06\nR007_US009_UTAH_FUTURE_CHANGE_SIGNAL = 2027-07-01\nR007_US009_WHOLE_CHAPTER_SECTION_BY_SECTION_CURRENTNESS = OPEN\n'''
if insert not in s:
    if needle not in s: raise SystemExit('integrity anchor missing')
    s=s.replace(needle,insert+needle,1)
ctx.write_text(s,encoding='utf-8')

# Assertions
assert len(state_rows)==51
assert sum(1 for r in state_rows if r[0]=='US-UT')==1
assert 'COMPLETE_RESEARCH_ARCHITECTURE_L1_STATE_LAW_CONTENT_OPEN' in q.read_text(encoding='utf-8')
assert 'R007_US_INVENTORY_ARCHITECTURE_L1_COMPLETE' in ctx.read_text(encoding='utf-8')
print('R007_PERSIST_ASSERTIONS=PASS')
print('STATE_PLUS_DC=51')
print('FEDERAL_CONTROLLED_SOURCES=8')
print('US009_SECTION101_EFFECTIVE=2026-05-06')
print('ZIP_OR_ARTIFACT_CREATED=NO')
print('AUTO_ADVANCE=NO')
