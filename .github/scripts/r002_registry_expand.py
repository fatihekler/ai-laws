from pathlib import Path
import csv, hashlib, io, re, urllib.request
import pandas as pd

DATE='2026-09-14'
REG=Path('20_JURISDICTIONS/JURISDICTION_RESEARCH_REGISTRY.csv')
SRC=Path('20_JURISDICTIONS/R002_SOURCE_ACQUISITION_RESULTS_2026-09-14.csv')
VAL=Path('20_JURISDICTIONS/R002_REGISTRY_VALIDATION_SUMMARY_2026-09-14.csv')
UN_URL='https://unstats.un.org/unsd/methodology/m49/overview/'
CENSUS_URL='https://www2.census.gov/geo/docs/reference/state.txt'
FIELDS=['jurisdiction_id','name','jurisdiction_type','region','research_state','priority','initial_focus','notes']
US_NONSTATE={'AS','GU','MP','PR','UM','VI'}

def fetch(url):
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 AI-LAWS-R002-registry-verification'})
    with urllib.request.urlopen(req,timeout=180) as r:
        body=r.read(); status=getattr(r,'status',200); ctype=r.headers.get('Content-Type','')
    return status,ctype,body

def flat_cols(df):
    cols=[]
    for c in df.columns:
        if isinstance(c,tuple):
            s=' '.join(str(x) for x in c if str(x)!='nan').strip()
        else: s=str(c)
        cols.append(re.sub(r'\s+',' ',s).strip())
    df=df.copy(); df.columns=cols; return df

existing=[]
with REG.open(encoding='utf-8',newline='') as f:
    existing=list(csv.DictReader(f))
existing_by_id={r['jurisdiction_id']:r for r in existing}

# UN M49 live official table.
un_status,un_ct,un_body=fetch(UN_URL)
un_sha=hashlib.sha256(un_body).hexdigest()
html=un_body.decode('utf-8',errors='ignore')
tables=pd.read_html(io.StringIO(html))
selected=None
for t in tables:
    t=flat_cols(t)
    cols=[c.lower() for c in t.columns]
    if any('country or area' in c for c in cols) and any('m49 code' in c for c in cols):
        selected=t; break
if selected is None:
    raise SystemExit('UN M49 country/area table not found')

def findcol(key):
    for c in selected.columns:
        if key in c.lower(): return c
    return None
c_name=findcol('country or area'); c_m49=findcol('m49 code'); c_a2=findcol('iso-alpha2'); c_region=findcol('region name'); c_sub=findcol('sub-region name')
assert all([c_name,c_m49,c_a2]), (c_name,c_m49,c_a2,list(selected.columns))

un_rows=[]
for _,r in selected.iterrows():
    name=str(r[c_name]).strip(); m49=str(r[c_m49]).strip(); a2=str(r[c_a2]).strip().upper()
    if not name or name.lower()=='nan' or not a2 or a2.lower()=='nan' or len(a2)!=2: continue
    m49=re.sub(r'\.0$','',m49).zfill(3)
    region='GLOBAL'
    if c_region:
        rr=str(r[c_region]).strip()
        if rr and rr.lower()!='nan': region=rr
    if c_sub:
        sr=str(r[c_sub]).strip()
        if sr and sr.lower()!='nan': region=f'{region} / {sr}' if region!='GLOBAL' else sr
    if a2 in existing_by_id:
        out=dict(existing_by_id[a2])
        # Avoid repeated confirmation strings on controlled reruns.
        if f'UN M49 {m49} live enumeration confirmed {DATE}' not in out.get('notes',''):
            out['notes']=(out.get('notes','').rstrip() + f' UN M49 {m49} live enumeration confirmed {DATE}; M49 country/area label does not itself decide sovereignty or treaty status.').strip()
    else:
        out={
          'jurisdiction_id':a2,
          'name':name,
          'jurisdiction_type':'UN_M49_COUNTRY_OR_AREA',
          'region':region,
          'research_state':'REGISTRY_ENUMERATED_RESEARCH_NOT_STARTED',
          'priority':'P2',
          'initial_focus':'baseline legal-system/source mapping; AI/data/privacy/cyber/consumer/product/public-law interfaces',
          'notes':f'UN M49 {m49} live country/area enumeration confirmed {DATE}. Enumeration does not decide sovereignty, recognition, treaty status, applicable law or domestic competence.'
        }
    un_rows.append(out)
assert len(un_rows) >= 240, len(un_rows)
assert len({r['jurisdiction_id'] for r in un_rows})==len(un_rows)

# U.S. Census state/statistical-equivalent list.
cs,cc,cb=fetch(CENSUS_URL)
csha=hashlib.sha256(cb).hexdigest()
text=cb.decode('utf-8-sig',errors='strict')
reader=csv.DictReader(io.StringIO(text),delimiter='|')
us_rows=[]
for r in reader:
    ab=r['STUSAB'].strip().upper(); name=r['STATE_NAME'].strip(); fips=r['STATE'].strip(); jid='US-'+ab
    if jid in existing_by_id:
        out=dict(existing_by_id[jid])
        if f'U.S. Census state/statistical-equivalent code {fips} live list confirmed {DATE}' not in out.get('notes',''):
            out['notes']=(out.get('notes','').rstrip()+f' U.S. Census state/statistical-equivalent code {fips} live list confirmed {DATE}.').strip()
        # Correct any prior provisional class on the six non-state entries.
        if ab in US_NONSTATE:
            out['jurisdiction_type']='SUBNATIONAL_US_TERRITORY_OR_STATISTICAL_EQUIVALENT'
    else:
        jtype='SUBNATIONAL_US_TERRITORY_OR_STATISTICAL_EQUIVALENT' if ab in US_NONSTATE else 'SUBNATIONAL_US_STATE_OR_DISTRICT'
        out={
          'jurisdiction_id':jid,
          'name':name,
          'jurisdiction_type':jtype,
          'region':'NORTH_AMERICA',
          'research_state':'R002_ENUMERATED_SUBNATIONAL_RESEARCH_REQUIRED',
          'priority':'P1',
          'initial_focus':'AI-specific statutes; privacy/biometrics; consumer; employment; public-sector use; sector law; federal/preemption interfaces',
          'notes':f'U.S. Census state/statistical-equivalent code {fips} live list confirmed {DATE}. Enumeration does not establish AI-specific law or legal equivalence among states, district and territories/statistical equivalents.'
        }
    us_rows.append(out)
assert len(us_rows)==57, len(us_rows)
assert sum(r['jurisdiction_id'].split('-',1)[1] in US_NONSTATE for r in us_rows)==6

# Preserve non-country/non-US-subnational rows from existing registry (meta/org/regional union, etc.).
un_ids={x['jurisdiction_id'] for x in un_rows}; us_ids={x['jurisdiction_id'] for x in us_rows}
preserve=[]
for r in existing:
    jid=r['jurisdiction_id']
    if jid in un_ids: continue
    if jid.startswith('US-') and jid in us_ids: continue
    if jid=='GLOBAL-ALL': continue
    preserve.append(r)

meta={
 'jurisdiction_id':'GLOBAL-ALL',
 'name':'All jurisdictions — explicit global registry coverage meta',
 'jurisdiction_type':'COVERAGE_META',
 'region':'GLOBAL',
 'research_state':'GLOBAL_COUNTRY_AREA_ENUMERATION_COMPLETE_MATERIAL_SUBNATIONAL_METHOD_ACTIVE',
 'priority':'P0',
 'initial_focus':'UN M49 country/area inventory + legally material subnational expansion triggers',
 'notes':'R002 enumerates the live UN M49 country/area universe and the complete U.S. Census state/statistical-equivalent set. Unlisted subnational jurisdictions remain in scope and are added when competence, separate legal system, enacted AI/data/privacy/consumer rules, case-law system, enforcement or cross-border relevance makes them material. Registry presence != substantive law researched.'
}
orgs=[r for r in preserve if r['jurisdiction_type'] in {'INTERNATIONAL_ORGANIZATION','SUPRANATIONAL_UNION','REGIONAL_INTERNATIONAL_ORGANIZATION','REGIONAL_UNION','REGIONAL_ORGANIZATION'}]
other=[r for r in preserve if r not in orgs]
final=[meta]+sorted(orgs,key=lambda r:r['jurisdiction_id'])+sorted(un_rows,key=lambda r:r['jurisdiction_id'])+sorted(us_rows,key=lambda r:r['jurisdiction_id'])+sorted(other,key=lambda r:r['jurisdiction_id'])
ids=[r['jurisdiction_id'] for r in final]
assert len(ids)==len(set(ids)), [x for x in set(ids) if ids.count(x)>1]

with REG.open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=FIELDS,lineterminator='\n'); w.writeheader(); w.writerows(final)
with SRC.open('w',encoding='utf-8',newline='') as f:
    cols=['source_id','authority','official_url','http_status','content_type','byte_size','sha256','parsed_records','verification_state','critical_limit']
    w=csv.DictWriter(f,fieldnames=cols,lineterminator='\n'); w.writeheader()
    w.writerow({'source_id':'R002-UN-M49','authority':'United Nations Statistics Division','official_url':UN_URL,'http_status':un_status,'content_type':un_ct,'byte_size':len(un_body),'sha256':un_sha,'parsed_records':len(un_rows),'verification_state':'LIVE_OFFICIAL_BODY_PARSED_AND_ENUMERATION_VALIDATED','critical_limit':'UN M49 country/area terminology does not decide sovereignty, recognition, treaty status or legal competence'})
    w.writerow({'source_id':'R002-US-CENSUS-STATE','authority':'U.S. Census Bureau','official_url':CENSUS_URL,'http_status':cs,'content_type':cc,'byte_size':len(cb),'sha256':csha,'parsed_records':len(us_rows),'verification_state':'LIVE_OFFICIAL_BODY_PARSED_AND_ENUMERATION_VALIDATED','critical_limit':'Census state/statistical-equivalent enumeration does not establish substantive AI law or equal legal status'})
with VAL.open('w',encoding='utf-8',newline='') as f:
    cols=['metric','value','state_or_limit']; w=csv.DictWriter(f,fieldnames=cols,lineterminator='\n'); w.writeheader()
    vals=[
      ('UN_M49_COUNTRY_AREA_ROWS',len(un_rows),'LIVE_OFFICIAL_PARSED'),
      ('US_CENSUS_STATE_EQUIVALENT_ROWS',len(us_rows),'LIVE_OFFICIAL_PARSED'),
      ('US_NONSTATE_TERRITORY_OR_EQUIVALENT_ROWS',sum(r['jurisdiction_id'].split('-',1)[1] in US_NONSTATE for r in us_rows),'AS_GU_MP_PR_UM_VI'),
      ('TOTAL_REGISTRY_ROWS',len(final),'DETERMINISTIC_MERGE'),
      ('DUPLICATE_JURISDICTION_IDS',len(ids)-len(set(ids)),'MUST_BE_ZERO'),
      ('SUBSTANTIVE_LAW_FINDINGS_FOR_NEW_ROWS',0,'NOT_ATTEMPTED'),
      ('UNLISTED_SUBNATIONALS_OUT_OF_SCOPE','NO','MATERIALITY_TRIGGER_METHOD'),
    ]
    for m,v,s in vals: w.writerow({'metric':m,'value':v,'state_or_limit':s})
print('UN_M49_ROWS=',len(un_rows))
print('US_CENSUS_ROWS=',len(us_rows))
print('US_NONSTATE_ROWS=',sum(r['jurisdiction_id'].split('-',1)[1] in US_NONSTATE for r in us_rows))
print('TOTAL_REGISTRY_ROWS=',len(final))
print('UN_SHA256=',un_sha)
print('CENSUS_SHA256=',csha)
print('SUBSTANTIVE_LAW_FINDINGS_FOR_NEW_ROWS=0')
print('ZIP_OR_ARTIFACT_CREATED=NO')
print('AUTO_ADVANCE=NO')
