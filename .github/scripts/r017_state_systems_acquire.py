from pathlib import Path
import csv, hashlib, os, re, subprocess, tempfile

OUT = Path('77_STATE_SYSTEMS/source_acquisition/AI-LAWS-R017_SOURCE_ACQUISITION_RESULTS_2026-09-14.csv')
OUT.parent.mkdir(parents=True, exist_ok=True)
FIELDS = ['source_key','jurisdiction','authority_class','title','official_url','source_mode','http_status','content_type','byte_size','sha256','pages','verification_state','binding_scope','critical_limit','evidence_markers']
rows=[]

def pdf_text_bytes(body):
    sha=hashlib.sha256(body).hexdigest(); size=len(body); pages=''; text=''
    with tempfile.NamedTemporaryFile(delete=False,suffix='.pdf') as f:
        f.write(body); pp=f.name
    tp=pp+'.txt'
    try:
        q=subprocess.run(['pdfinfo',pp],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        m=re.search(r'(?m)^Pages:\s*(\d+)',q.stdout or '')
        pages=m.group(1) if m else ''
        subprocess.run(['pdftotext','-layout',pp,tp],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        if Path(tp).exists(): text=Path(tp).read_text(encoding='utf-8',errors='ignore')
    finally:
        for x in (pp,tp):
            try: os.unlink(x)
            except FileNotFoundError: pass
    return sha,size,pages,text

def local_controlled(key,jur,aclass_,title,name_tokens,markers,binding,limit,official_url='REPOSITORY_CONTROLLED_SNAPSHOT'):
    pdfs=list(Path('86_NOTEBOOKLM/downloads').glob('*.pdf'))
    chosen=None
    for p in pdfs:
        n=p.name.lower()
        if any(t.lower() in n for t in name_tokens):
            chosen=p; break
    if chosen is None:
        rows.append(dict(source_key=key,jurisdiction=jur,authority_class=aclass_,title=title,official_url=official_url,source_mode='REPOSITORY_CONTROLLED_SNAPSHOT',http_status='N/A',content_type='application/pdf',byte_size='',sha256='',pages='',verification_state='REPOSITORY_SOURCE_NOT_LOCATED',binding_scope=binding,critical_limit=limit,evidence_markers='; '.join(markers)))
        return
    body=chosen.read_bytes(); sha,size,pages,text=pdf_text_bytes(body); low=text.lower()
    ok=all(m.lower() in low for m in markers)
    state='REPOSITORY_CONTROLLED_BODY_AND_MARKERS_VERIFIED' if ok else 'REPOSITORY_BODY_MARKERS_NOT_VERIFIED'
    rows.append(dict(source_key=key,jurisdiction=jur,authority_class=aclass_,title=title,official_url=official_url,source_mode='REPOSITORY_CONTROLLED_SNAPSHOT',http_status='N/A',content_type='application/pdf',byte_size=size,sha256=sha,pages=pages,verification_state=state,binding_scope=binding,critical_limit=limit,evidence_markers='; '.join(markers)))
    print(key,chosen.name,size,pages,state)

def fetch(url):
    with tempfile.NamedTemporaryFile(delete=False) as h, tempfile.NamedTemporaryFile(delete=False) as b:
        hp,bp=h.name,b.name
    try:
        p=subprocess.run(['curl','-L','--connect-timeout','20','--max-time','180','-sS','-A','Mozilla/5.0 AI-LAWS-R017-source-verification','-D',hp,'-o',bp,'-w','%{http_code}',url],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        status=(p.stdout or '').strip()[-3:] if p.stdout else '000'
        body=Path(bp).read_bytes() if Path(bp).exists() else b''
        headers=Path(hp).read_text(encoding='utf-8',errors='ignore') if Path(hp).exists() else ''
        cts=re.findall(r'(?im)^content-type:\s*([^\r\n]+)',headers)
        ctype=cts[-1].strip() if cts else ''
        return status,ctype,body
    finally:
        for x in (hp,bp):
            try: os.unlink(x)
            except FileNotFoundError: pass

def official(key,jur,aclass_,title,url,markers,binding,limit,expected='ANY'):
    status,ctype,body=fetch(url); sha=hashlib.sha256(body).hexdigest(); size=len(body); pages=''; ispdf=body.startswith(b'%PDF-')
    if ispdf:
        sha,size,pages,text=pdf_text_bytes(body)
    else:
        text=body.decode('utf-8',errors='ignore')
        text=re.sub(r'<script[\s\S]*?</script>|<style[\s\S]*?</style>',' ',text,flags=re.I)
        text=re.sub(r'<[^>]+>',' ',text); text=re.sub(r'\s+',' ',text)
    low=text.lower(); ok=all(m.lower() in low for m in markers)
    if status!='200': state=f'ACCESS_HTTP_{status}'
    elif expected=='PDF' and not ispdf: state='HTTP_200_BODY_NOT_PDF'
    elif expected=='HTML' and ispdf: state='HTTP_200_UNEXPECTED_PDF'
    elif ok: state='OFFICIAL_SOURCE_BODY_AND_MARKERS_VERIFIED'
    else: state='HTTP_200_BODY_MARKERS_NOT_VERIFIED'
    rows.append(dict(source_key=key,jurisdiction=jur,authority_class=aclass_,title=title,official_url=url,source_mode='LIVE_OFFICIAL',http_status=status,content_type=ctype,byte_size=size,sha256=sha,pages=pages,verification_state=state,binding_scope=binding,critical_limit=limit,evidence_markers='; '.join(markers)))
    print(key,status,ctype,size,pages,state)

# Existing exact/controlled repository snapshots.
local_controlled('EU-STATE-001','EU','STATUTE_OR_REGULATION','Regulation (EU) 2024/1689 — AI Act consolidated Article 2 scope boundaries',['artificial intelligence act','ai act','reg-2024-1689','eu-001'],['national security','military','defence'],'BINDING_EU_REGULATION_WITH_PHASED_APPLICATION','AI Act scope exclusion != exemption from all law','https://eur-lex.europa.eu/eli/reg/2024/1689/oj')
local_controlled('COE-STATE-001','COE','TREATY_TEXT','CETS 225 Framework Convention — Article 3 national-security/defence scope',['cets no.225 treaty status','cets 225 treaty','int-001'],['national security interests','national defence'],'TREATY_TEXT_CURRENT_STATUS_GATE_R004','Treaty text != treaty currently in force for a Party; R004 status controls','https://www.coe.int/en/web/conventions/full-list?module=treaty-detail&treatynum=225')
local_controlled('US-STATE-001','US','OMB_MEMORANDUM','OMB M-25-21 — federal AI governance scope',['m-25-21','us-003'],['national security','44 u.s.c. 3552'],'EXECUTIVE_BRANCH_OPERATIONAL_MEMORANDUM_WITHIN_SCOPE','OMB memorandum != Act of Congress; national-security-system scope must be preserved','https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf')

# Current official public-law / oversight sources.
official('EU-STATE-002','COE','TREATY_PRIMARY','European Convention on Human Rights — Articles 8 and 13','https://www.echr.coe.int/documents/d/echr/convention_eng',['private and family life','national security','effective remedy'],'BINDING_TREATY_FOR_CONTRACTING_PARTIES_SUBJECT_TO_JURISDICTION_AND_RESERVATIONS','ECHR layer is not an AI-specific statute and applicability/remedy is fact- and jurisdiction-specific','PDF')
official('US-STATE-002','US','STATUTE_OR_REGULATION','44 U.S.C. §3552 — national security system definition','https://uscode.house.gov/view.xhtml?edition=prelim&req=granuleid%3AUSC-prelim-title44-section3552',['national security system','intelligence activities','cryptologic activities'],'BINDING_FEDERAL_STATUTE','Definition does not itself create an AI duty or remedy','HTML')
official('US-STATE-003','US','STATUTE_OR_REGULATION','5 U.S.C. §702 — Administrative Procedure Act review / nonmoney relief','https://uscode.house.gov/view.xhtml?edition=prelim&req=granuleid%3AUSC-prelim-title5-section702',['right of review','relief other than money damages','sovereign immunity'],'BINDING_FEDERAL_STATUTE','Waiver/review route remains subject to other limitations on judicial review and applicable causes of action','HTML')
official('US-STATE-004','US','STATUTE_OR_REGULATION','28 U.S.C. §1346(b) — FTCA jurisdictional grant','https://uscode.house.gov/view.xhtml?edition=prelim&req=granuleid%3AUSC-prelim-title28-section1346',['civil actions on claims against the united states','money damages','negligent or wrongful act'],'BINDING_FEDERAL_STATUTE','Jurisdictional waiver conditions require employee/scope/place-law analysis','HTML')
official('US-STATE-005','US','STATUTE_OR_REGULATION','28 U.S.C. §2674 — United States liability under FTCA','https://uscode.house.gov/view.xhtml?edition=prelim&req=granuleid%3AUSC-prelim-title28-section2674',['liable','same manner and to the same extent as a private individual'],'BINDING_FEDERAL_STATUTE','Does not override statutory exceptions or establish AI-specific liability','HTML')
official('US-STATE-006','US','STATUTE_OR_REGULATION','28 U.S.C. §2680 — FTCA exceptions','https://uscode.house.gov/view.xhtml?edition=prelim&req=granuleid%3AUSC-prelim-title28-section2680',['discretionary function','due care','foreign country'],'BINDING_FEDERAL_STATUTE','Exception analysis is claim- and fact-specific; exception != no underlying duty','HTML')
official('US-STATE-007','US','STATUTE_OR_REGULATION','50 U.S.C. §3033 — Inspector General of the Intelligence Community','https://uscode.house.gov/view.xhtml?edition=prelim&req=granuleid%3AUSC-prelim-title50-section3033',['inspector general of the intelligence community','independent and objective','investigations'],'BINDING_FEDERAL_STATUTE','Oversight mechanism != public transparency or private damages remedy','HTML')
official('US-STATE-008','US','OFFICIAL_DEPARTMENTAL_DIRECTIVE','DoD Directive 3000.09 — Autonomy in Weapon Systems','https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodd/300009p.PDF',['autonomy in weapon systems','human judgment','use of force'],'BINDING_OR_OPERATIONAL_DEPARTMENTAL_POLICY_WITHIN_DOD_SCOPE','Autonomous-weapon policy != general rule for all defence AI and != statute','PDF')

OUT.parent.mkdir(parents=True,exist_ok=True)
with OUT.open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=FIELDS,lineterminator='\n'); w.writeheader(); w.writerows(rows)
print('R017_SOURCE_RECORDS=',len(rows))
print('R017_BODY_MARKER_VERIFIED=',sum('BODY_AND_MARKERS_VERIFIED' in r['verification_state'] for r in rows))
print('ZIP_OR_ARTIFACT_CREATED=NO')
print('NOTEBOOK_UPLOADS=0')
print('AUTO_ADVANCE=NO')