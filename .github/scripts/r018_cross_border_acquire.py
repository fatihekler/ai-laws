from pathlib import Path
import csv, hashlib, re, subprocess, urllib.request, urllib.error

DATE='2026-09-14'
OUT=Path('78_CROSS_BORDER/source_acquisition/AI-LAWS-R018_SOURCE_ACQUISITION_RESULTS_2026-09-14.csv')
OUT.parent.mkdir(parents=True, exist_ok=True)
UA='Mozilla/5.0 AI-LAWS-R018-cross-border-verifier'

def fetch(url):
    req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept':'text/html,application/xhtml+xml,application/pdf,*/*'})
    try:
        with urllib.request.urlopen(req,timeout=120) as r:
            b=r.read(); return getattr(r,'status',200),r.headers.get('Content-Type',''),b,r.geturl(),''
    except urllib.error.HTTPError as e:
        b=e.read() if hasattr(e,'read') else b''
        return e.code,e.headers.get('Content-Type','') if e.headers else '',b,url,f'HTTPError:{e.code}'
    except Exception as e:
        return 0,'',b'',url,f'{type(e).__name__}:{e}'

def text_from_body(body, ctype, sid):
    if body.startswith(b'%PDF') or 'pdf' in ctype.lower():
        p=Path('/tmp')/f'{sid}.pdf'; t=Path('/tmp')/f'{sid}.txt'; p.write_bytes(body)
        cp=subprocess.run(['pdftotext','-layout',str(p),str(t)],capture_output=True,text=True)
        if cp.returncode!=0: return '',f'PDFTOTEXT_FAIL:{cp.stderr[:120]}'
        return t.read_text(errors='ignore'),'PDF_TEXT_OK'
    try:
        s=body.decode('utf-8',errors='ignore')
    except Exception:
        s=''
    s=re.sub(r'<script.*?</script>|<style.*?</style>',' ',s,flags=re.I|re.S)
    s=re.sub(r'<[^>]+>',' ',s)
    s=re.sub(r'\s+',' ',s)
    return s,'HTML_TEXT_OK'

def norm(s): return re.sub(r'\s+',' ',s).lower()

def verify_markers(text, markers):
    n=norm(text)
    hits=[m for m in markers if norm(m) in n]
    return hits, len(hits)>=max(1,min(2,len(markers)))

sources=[
 ('R018-EU-BRUSSELS1','European Union','Regulation (EU) No 1215/2012 Brussels I bis','BINDING_REGULATION','https://eur-lex.europa.eu/eli/reg/2012/1215/oj/eng',['jurisdiction and the recognition and enforcement of judgments in civil and commercial matters','recognition','enforcement']),
 ('R018-EU-ROME2','European Union','Regulation (EC) No 864/2007 Rome II','BINDING_REGULATION','https://eur-lex.europa.eu/eli/reg/2007/864/oj/eng',['law applicable to non-contractual obligations','damage occurs','product liability']),
 ('R018-EU-ROME1','European Union','Regulation (EC) No 593/2008 Rome I','BINDING_REGULATION','https://eur-lex.europa.eu/eli/reg/2008/593/oj/eng',['law applicable to contractual obligations','freedom of choice','consumer contracts']),
 ('R018-US-FRCP','United States','Federal Rules of Civil Procedure pamphlet Dec. 1 2025','OFFICIAL_CURRENT_RULES_PDF','https://www.uscourts.gov/sites/default/files/document/federal-rules-of-civil-procedure.pdf',['Territorial Limits of Effective Service','Serving an Individual in a Foreign Country','Rule 4. Summons']),
 ('R018-US-1391','United States','28 U.S.C. §1391 Venue generally','BINDING_STATUTE','https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title28-section1391&num=0&edition=prelim',['Venue generally','a civil action may be brought']),
 ('R018-US-1782','United States','28 U.S.C. §1782 Assistance to foreign and international tribunals','BINDING_STATUTE','https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title28-section1782&num=0&edition=prelim',['Assistance to foreign and international tribunals','resides or is found']),
]
rows=[]
for sid,auth,title,sclass,url,markers in sources:
    st,ct,b,final_url,err=fetch(url)
    sha=hashlib.sha256(b).hexdigest() if b else ''
    txt,extract_state=text_from_body(b,ct,sid) if b else ('','NO_BODY')
    hits,ok=verify_markers(txt,markers)
    rows.append({'source_id':sid,'authority':auth,'source_title':title,'source_class':sclass,'official_url':url,'final_url':final_url,'http_status':st,'content_type':ct,'byte_size':len(b),'sha256':sha,'marker_hits':' | '.join(hits),'verification_state':'BODY_MARKERS_VERIFIED' if ok else ('HTTP_BODY_ACQUIRED_MARKERS_NOT_VERIFIED' if b else 'NO_SUBSTANTIVE_BODY'),'extract_state':extract_state,'error':err})

# Controlled repository snapshots: record identity + bounded marker check without network mutation.
controlled=[
 ('R018-EU-AIA','European Union','Regulation (EU) 2024/1689 consolidated 2026-07-27','BINDING_REGULATION','86_NOTEBOOKLM/downloads/Current consolidated AI Act.pdf',['providers and deployers of AI systems that have their place of establishment or are located in a third country','output produced by the system is used in the Union']),
 ('R018-EU-GDPR','European Union','Regulation (EU) 2016/679 GDPR','BINDING_REGULATION','86_NOTEBOOKLM/downloads/GDPR.pdf',['Territorial scope','offering of goods or services','monitoring of their behaviour']),
]
for sid,auth,title,sclass,path,markers in controlled:
    p=Path(path); b=p.read_bytes(); sha=hashlib.sha256(b).hexdigest(); txt,ex=text_from_body(b,'application/pdf',sid); hits,ok=verify_markers(txt,markers)
    rows.append({'source_id':sid,'authority':auth,'source_title':title,'source_class':sclass,'official_url':'CONTROLLED_REPOSITORY_SNAPSHOT','final_url':path,'http_status':'REPOSITORY','content_type':'application/pdf','byte_size':len(b),'sha256':sha,'marker_hits':' | '.join(hits),'verification_state':'CONTROLLED_REPOSITORY_BODY_MARKERS_VERIFIED' if ok else 'CONTROLLED_REPOSITORY_MARKERS_NOT_VERIFIED','extract_state':ex,'error':''})

cols=['source_id','authority','source_title','source_class','official_url','final_url','http_status','content_type','byte_size','sha256','marker_hits','verification_state','extract_state','error']
with OUT.open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols,lineterminator='\n'); w.writeheader(); w.writerows(rows)
print('R018_SOURCE_RECORDS=',len(rows))
print('R018_MARKER_VERIFIED=',sum('VERIFIED' in r['verification_state'] and 'NOT_VERIFIED' not in r['verification_state'] for r in rows))
for r in rows: print(r['source_id'],r['http_status'],r['byte_size'],r['verification_state'],r['sha256'][:16])
print('ZIP_OR_ARTIFACT_CREATED=NO')
print('AUTO_ADVANCE=NO')
