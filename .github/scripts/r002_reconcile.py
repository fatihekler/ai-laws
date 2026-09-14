from pathlib import Path
import csv

RESEARCH_SHA='5011f3f8aeb7c00bf8010d9f1d7284f5221e6972'
STATE='COMPLETE_REGISTRY_BASELINE_L1_GLOBAL_COUNTRY_AREA_US_STATE_TERRITORY_MATERIAL_SUBNATIONAL_METHOD'

# Queue reconciliation via CSV, preserving all other work items exactly by field semantics.
qpath=Path('90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv')
with qpath.open(encoding='utf-8',newline='') as f:
    rows=list(csv.DictReader(f)); fields=list(rows[0].keys())
found=0
for r in rows:
    if r['work_item_id']=='AI-LAWS-R002':
        assert r['state']=='READY_RESEARCH', r['state']
        r['state']=STATE
        r['dependencies']='NONE'
        r['expected_output']='20_JURISDICTIONS/JURISDICTION_RESEARCH_REGISTRY.csv; 20_JURISDICTIONS/R002_JURISDICTION_COVERAGE_METHOD_2026-09-14.md; 20_JURISDICTIONS/R002_MATERIAL_SUBNATIONAL_TRIGGER_MATRIX_2026-09-14.csv; 20_JURISDICTIONS/R002_SOURCE_ACQUISITION_RESULTS_2026-09-14.csv; 20_JURISDICTIONS/R002_REGISTRY_VALIDATION_SUMMARY_2026-09-14.csv; 95_RESEARCH/JURISDICTION_REGISTRY/AI-LAWS-R002_CLOSEOUT_2026-09-14.md'
        r['stop_condition']='global UN M49 country/area + U.S. Census state/statistical-equivalent enumeration and material-subnational admission method complete; stop before substantive law for unresearched jurisdictions, sovereignty determinations or R018 forum/applicable-law analysis'
        found+=1
assert found==1
# Preserve gates.
r018=[r for r in rows if r['work_item_id']=='AI-LAWS-R018'][0]
r019=[r for r in rows if r['work_item_id']=='AI-LAWS-R019'][0]
assert r018['state']=='READY_RESEARCH'
assert r019['state']=='READY_FOR_EXPLICIT_AUTHORIZATION'
with qpath.open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n'); w.writeheader(); w.writerows(rows)

# Current context reconciliation.
cpath=Path('00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md')
c=cpath.read_text(encoding='utf-8')
old='R001_COMPLETE / R003_EU_AI_ACT_L1_L2_COMPLETE'
new='R001_COMPLETE / R002_JURISDICTION_REGISTRY_BASELINE_COMPLETE / R003_EU_AI_ACT_L1_L2_COMPLETE'
assert old in c and 'R002_JURISDICTION_REGISTRY_BASELINE_COMPLETE' not in c
c=c.replace(old,new,1)
old2='AI-LAWS-R001 = COMPLETE_SUPPORTING_RESEARCH_IMPORT\nAI-LAWS-R003 = COMPLETE_RESEARCH_BASELINE_L1_L2'
new2='AI-LAWS-R001 = COMPLETE_SUPPORTING_RESEARCH_IMPORT\nAI-LAWS-R002 = '+STATE+'\nAI-LAWS-R003 = COMPLETE_RESEARCH_BASELINE_L1_L2'
assert old2 in c
c=c.replace(old2,new2,1)
section='''### R002 — Global jurisdiction registry baseline\n\n```text\nAI-LAWS-R002 — JURISDICTION REGISTRY\nSTATE = COMPLETE_REGISTRY_BASELINE_L1_GLOBAL_COUNTRY_AREA_US_STATE_TERRITORY_MATERIAL_SUBNATIONAL_METHOD\nNEXT_BOUNDED_UNIT = NONE_AUTO_SELECTED\n```\n\nR002 replaced the seed-only world-coverage state with a deterministic live-source registry baseline. The live United Nations Statistics Division M49 table supplied 247 country/area rows carrying ISO alpha-2 codes. Existing AI-LAWS research states were preserved; newly enumerated rows are routing records only and default to `REGISTRY_ENUMERATED_RESEARCH_NOT_STARTED`.\n\nThe live U.S. Census state/statistical-equivalent list supplied 57 `US-XX` rows. Existing R007 state/DC research states were preserved. Six non-state territory/statistical-equivalent rows are separately classified: `US-AS`, `US-GU`, `US-MP`, `US-PR`, `US-UM`, `US-VI`. The validation pass specifically corrected `US-UM` from an initial provisional state/district class.\n\n```text\nUN_M49_COUNTRY_AREA_ROWS = 247\nUS_CENSUS_STATE_EQUIVALENT_ROWS = 57\nUS_NONSTATE_TERRITORY_OR_EQUIVALENT_ROWS = 6\nTOTAL_REGISTRY_ROWS = 313\nDUPLICATE_JURISDICTION_IDS = 0\nSUBSTANTIVE_LAW_FINDINGS_FOR_NEW_ROWS = 0\n```\n\nR002 also creates a material-subnational admission method. Unlisted provinces/cantons/emirates/free zones/special jurisdictions are not treated as out of scope; they are added when separate competence, legal system, enacted divergent law, regulator/enforcement authority, cross-border relevance, special regime or treaty/constitutional status is verified. `UN_M49_COUNTRY_OR_AREA != SOVEREIGNTY_DETERMINATION` and `REGISTRY_PRESENCE != SUBSTANTIVE_LAW_RESEARCHED` remain controlling.\n\nR002 satisfies the registry-side dependency needed before a later R018 cross-border bounded unit, but R018 was not started.\n\n'''
marker='### R003 — EU AI Act current consolidated / phased-application legal map'
assert marker in c and '### R002 — Global jurisdiction registry baseline' not in c
c=c.replace(marker,section+marker,1)
cpath.write_text(c,encoding='utf-8')

# Closeout SHA.
ppath=Path('95_RESEARCH/JURISDICTION_REGISTRY/AI-LAWS-R002_CLOSEOUT_2026-09-14.md')
p=ppath.read_text(encoding='utf-8')
assert '**R002_RESEARCH_COMMIT:** `PENDING_RECONCILIATION`' in p
p=p.replace('**R002_RESEARCH_COMMIT:** `PENDING_RECONCILIATION`','**R002_RESEARCH_COMMIT:** `'+RESEARCH_SHA+'`',1)
ppath.write_text(p,encoding='utf-8')

assert '**AUTO_ADVANCE:** NO' in c
print('R002_RECONCILED=YES')
print('R002_RESEARCH_COMMIT='+RESEARCH_SHA)
print('R018_STATE=READY_RESEARCH')
print('R019_STATE=READY_FOR_EXPLICIT_AUTHORIZATION')
print('AUTO_ADVANCE=NO')
