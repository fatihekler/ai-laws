from pathlib import Path
import csv, sys

ROOT=Path('.')
MASTER=ROOT/'79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_MASTER_REQUIREMENT_CANDIDATE_MATRIX_2026-09-14.csv'
OUTDIR=ROOT/'79_CROSS_REPO_REQUIREMENTS'
OUTDIR.mkdir(parents=True,exist_ok=True)

allowed_dest={'ENGINEERING_OS','OWASP','ETHICAL_AI'}
required_cols=['candidate_id','legal_source_id','legal_duty_id','jurisdiction','authority_class','application_state_2026_09_14','duty_bearer','trigger_scope','requirement_candidate','evidence_required','technical_control_candidate','primary_destination','limitations','destination_acceptance','source_record_path','verification_state']

anchors={
'R020-CAND-001':'R003-EU-003',
'R020-CAND-002':'Article 50',
'R020-CAND-003':'R003-EU-011',
'R020-CAND-004':'Article 53',
'R020-CAND-005':'Article 53',
'R020-CAND-006':'Article 53',
'R020-CAND-007':'R015-GOV-002',
'R020-CAND-008':'R015-GOV-002',
'R020-CAND-009':'R015-GOV-002',
'R020-CAND-010':'R015-GOV-002',
'R020-CAND-011':'R014-EU-GDPR-005-2',
'R020-CAND-012':'R014-EU-GDPR-028-3H',
'R020-CAND-013':'R014-EU-GDPR-030',
'R020-CAND-014':'R014-EU-AIA-012',
'R020-CAND-015':'R014-EU-AIA-019',
'R020-CAND-016':'R014-EU-AIA-026-6',
'R020-CAND-017':'R015-GOV-001',
}

with MASTER.open(encoding='utf-8',newline='') as f:
    rows=list(csv.DictReader(f))
    cols=list(rows[0].keys()) if rows else []
if cols!=required_cols:
    raise SystemExit(f'COLUMN_MISMATCH:{cols}')
if len(rows)!=17:
    raise SystemExit(f'ROW_COUNT:{len(rows)}')
ids=[r['candidate_id'] for r in rows]
if len(set(ids))!=len(ids):
    raise SystemExit('DUPLICATE_CANDIDATE_ID')
if set(ids)!=set(anchors):
    raise SystemExit('CANDIDATE_ID_SET_MISMATCH')

for r in rows:
    if r['destination_acceptance']!='NOT_RUN': raise SystemExit(f"DESTINATION_ACCEPTANCE:{r['candidate_id']}")
    if r['primary_destination'] not in allowed_dest: raise SystemExit(f"DESTINATION:{r['candidate_id']}")
    if not r['authority_class'].startswith('BINDING_'): raise SystemExit(f"NONBINDING_ROW:{r['candidate_id']}")
    if not r['verification_state'].startswith('VERIFIED_'): raise SystemExit(f"UNVERIFIED_ROW:{r['candidate_id']}")
    p=ROOT/r['source_record_path']
    if not p.exists(): raise SystemExit(f"MISSING_SOURCE_PATH:{r['candidate_id']}:{p}")
    text=p.read_text(encoding='utf-8',errors='ignore')
    if anchors[r['candidate_id']] not in text: raise SystemExit(f"SOURCE_ANCHOR_MISSING:{r['candidate_id']}:{anchors[r['candidate_id']]}")
    is_future=r['candidate_id'] in {'R020-CAND-014','R020-CAND-015','R020-CAND-016','R020-CAND-017'}
    if is_future and not r['application_state_2026_09_14'].startswith('FUTURE_'):
        raise SystemExit(f"FUTURE_STATE_MISSING:{r['candidate_id']}")
    if not is_future and r['application_state_2026_09_14'].startswith('FUTURE_'):
        raise SystemExit(f"UNEXPECTED_FUTURE_STATE:{r['candidate_id']}")

# Generate destination packets without changing acceptance state.
for dest,filename in [
    ('ENGINEERING_OS','AI-LAWS-R020_ENGINEERING_OS_REVIEW_PACKET_2026-09-14.csv'),
    ('OWASP','AI-LAWS-R020_OWASP_REVIEW_PACKET_2026-09-14.csv'),
    ('ETHICAL_AI','AI-LAWS-R020_ETHICAL_AI_REVIEW_PACKET_2026-09-14.csv')]:
    subset=[r for r in rows if r['primary_destination']==dest]
    with (OUTDIR/filename).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=required_cols,lineterminator='\n'); w.writeheader(); w.writerows(subset)

# Source/authority matrix is a routing/audit view, not a new authority judgment.
source_groups={}
for r in rows:
    key=(r['legal_source_id'],r['source_record_path'],r['authority_class'],r['verification_state'])
    g=source_groups.setdefault(key,[]); g.append(r['legal_duty_id'])
source_cols=['legal_source_id','source_record_path','authority_class','verification_state','admitted_legal_duty_ids','candidate_count','bounded_use','limits']
with (OUTDIR/'AI-LAWS-R020_SOURCE_AND_AUTHORITY_MATRIX_2026-09-14.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=source_cols,lineterminator='\n'); w.writeheader()
    for (sid,path,auth,ver),duties in sorted(source_groups.items()):
        w.writerow({'legal_source_id':sid,'source_record_path':path,'authority_class':auth,'verification_state':ver,'admitted_legal_duty_ids':';'.join(duties),'candidate_count':len(duties),'bounded_use':'R020 destination-neutral requirement candidate traceability','limits':'Source scope, actor, trigger, temporal state and prior unit limitations remain controlling; destination acceptance not run'})

metrics=[
('CANDIDATE_ROWS',len(rows),'MUST_EQUAL_17'),
('UNIQUE_CANDIDATE_IDS',len(set(ids)),'MUST_EQUAL_CANDIDATE_ROWS'),
('DESTINATION_ACCEPTANCE_NOT_RUN_ROWS',sum(r['destination_acceptance']=='NOT_RUN' for r in rows),'MUST_EQUAL_CANDIDATE_ROWS'),
('ENGINEERING_OS_PACKET_ROWS',sum(r['primary_destination']=='ENGINEERING_OS' for r in rows),'ROUTING_ONLY'),
('OWASP_PACKET_ROWS',sum(r['primary_destination']=='OWASP' for r in rows),'ROUTING_ONLY'),
('ETHICAL_AI_PACKET_ROWS',sum(r['primary_destination']=='ETHICAL_AI' for r in rows),'ROUTING_ONLY'),
('FUTURE_PHASED_ROWS',sum(r['application_state_2026_09_14'].startswith('FUTURE_') for r in rows),'NOT_CURRENT_MANDATORY'),
('NONBINDING_OR_CASE_ROWS',sum(not r['authority_class'].startswith('BINDING_') for r in rows),'MUST_EQUAL_0'),
('SOURCE_PATHS_MISSING',sum(not (ROOT/r['source_record_path']).exists() for r in rows),'MUST_EQUAL_0'),
('DESTINATION_MUTATIONS',0,'MUST_EQUAL_0'),
('NOTEBOOK_UPLOADS',0,'MUST_EQUAL_0'),
('ZIP_OR_ARTIFACT_CREATED',0,'MUST_EQUAL_0'),
]
with (OUTDIR/'AI-LAWS-R020_VALIDATION_SUMMARY_2026-09-14.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.writer(f,lineterminator='\n'); w.writerow(['metric','value','state_or_limit']); w.writerows(metrics)

print('R020_CANDIDATE_ROWS=',len(rows))
print('R020_ENGINEERING_OS_ROWS=',sum(r['primary_destination']=='ENGINEERING_OS' for r in rows))
print('R020_OWASP_ROWS=',sum(r['primary_destination']=='OWASP' for r in rows))
print('R020_ETHICAL_AI_ROWS=',sum(r['primary_destination']=='ETHICAL_AI' for r in rows))
print('R020_FUTURE_PHASED_ROWS=',sum(r['application_state_2026_09_14'].startswith('FUTURE_') for r in rows))
print('DESTINATION_ACCEPTANCE=NOT_RUN')
print('DESTINATION_MUTATIONS=0')
print('ZIP_OR_ARTIFACT_CREATED=NO')
print('AUTO_ADVANCE=NO')
