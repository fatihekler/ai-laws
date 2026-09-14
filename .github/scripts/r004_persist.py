from pathlib import Path
import csv
import io

ROOT = Path('.')
DATE = '2026-09-14'
STATUS_AS_OF = '2026-09-12'

signatories = [
    ('Albania','COE_MEMBER','2026-06-15','','SIGNED_NOT_RATIFIED','NO'),
    ('Andorra','COE_MEMBER','2024-09-05','','SIGNED_NOT_RATIFIED','NO'),
    ('Armenia','COE_MEMBER','2026-01-27','','SIGNED_NOT_RATIFIED','NO'),
    ('Bosnia and Herzegovina','COE_MEMBER','2025-12-09','','SIGNED_NOT_RATIFIED','NO'),
    ('Georgia','COE_MEMBER','2024-09-05','','SIGNED_NOT_RATIFIED','NO'),
    ('Iceland','COE_MEMBER','2024-09-05','','SIGNED_NOT_RATIFIED','NO'),
    ('Liechtenstein','COE_MEMBER','2025-02-27','','SIGNED_NOT_RATIFIED','NO'),
    ('Montenegro','COE_MEMBER','2024-11-05','','SIGNED_NOT_RATIFIED','NO'),
    ('North Macedonia','COE_MEMBER','2026-05-08','','SIGNED_NOT_RATIFIED','NO'),
    ('Norway','COE_MEMBER','2024-09-05','','SIGNED_NOT_RATIFIED','YES'),
    ('Republic of Moldova','COE_MEMBER','2024-09-05','','SIGNED_NOT_RATIFIED','NO'),
    ('San Marino','COE_MEMBER','2024-09-05','','SIGNED_NOT_RATIFIED','NO'),
    ('Switzerland','COE_MEMBER','2025-03-27','','SIGNED_NOT_RATIFIED','NO'),
    ('Ukraine','COE_MEMBER','2025-05-15','','SIGNED_NOT_RATIFIED','YES'),
    ('United Kingdom','COE_MEMBER','2024-09-05','','SIGNED_NOT_RATIFIED','NO'),
    ('Canada','NON_MEMBER_PARTICIPANT','2025-02-11','','SIGNED_NOT_RATIFIED','NO'),
    ('European Union','INTERNATIONAL_ORGANISATION','2024-09-05','2026-05-15','APPROVAL_DEPOSITED_TREATY_NOT_YET_IN_FORCE','YES'),
    ('Israel','NON_MEMBER_PARTICIPANT','2024-09-05','','SIGNED_NOT_RATIFIED','NO'),
    ('Japan','NON_MEMBER_PARTICIPANT','2025-02-11','','SIGNED_NOT_RATIFIED','NO'),
    ('United States of America','NON_MEMBER_PARTICIPANT','2024-09-05','','SIGNED_NOT_RATIFIED','NO'),
    ('Uruguay','NON_MEMBER_PARTICIPANT','2025-09-02','','SIGNED_NOT_RATIFIED','NO'),
]

assert len(signatories) == 21
assert sum(1 for r in signatories if r[3]) == 1
assert sum(1 for r in signatories if r[1] == 'COE_MEMBER' and r[3]) == 0

sources = {
    'detail': 'https://www.coe.int/en/web/conventions/full-list?module=treaty-detail&treatynum=225',
    'status': 'https://www.coe.int/en/web/conventions/full-list?module=signatures-by-treaty&treatynum=225',
    'declarations': 'https://www.coe.int/en-GB/web/conventions/full-list?codeNature=0&module=declarations-by-treaty&numSte=225',
    'overview': 'https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence',
    'text': 'https://rm.coe.int/1680afae3c',
    'explanatory': 'https://rm.coe.int/1680afae67',
}

map_md = f'''# AI-LAWS — CETS No. 225 Current Treaty-Status / Declaration / Implementation Map

**WORK_ITEM:** `AI-LAWS-R004`  
**RESEARCH_DATE:** {DATE}  
**OFFICIAL_TREATY_OFFICE_STATUS_AS_OF:** {STATUS_AS_OF}  
**JURISDICTION:** Council of Europe treaty system  
**LEVEL:** L1/L2 treaty-status baseline  
**LEGAL_ADVICE:** NO  
**AUTO_ADVANCE:** NO

## 1. Controlled source set

Primary official sources for this bounded unit:

- Treaty detail: {sources['detail']}
- Signature/ratification chart: {sources['status']}
- Reservations/declarations page: {sources['declarations']}
- Council of Europe AI Convention overview: {sources['overview']}
- Official treaty text: {sources['text']}
- Official Explanatory Report: {sources['explanatory']}

Repository source `INT-001` remains a verified 12-page treaty-text snapshot. It is **not** a current party-status snapshot. Dynamic signature, ratification, declaration, reservation and entry-into-force claims must use the live Treaty Office layer.

```text
REPOSITORY_TREATY_TEXT != LIVE_TREATY_STATUS
SIGNATURE != RATIFICATION_OR_APPROVAL
RATIFICATION_BY_ONE_ENTITY != TREATY_ENTRY_INTO_FORCE
LEGALLY_BINDING_TREATY_FORM != CURRENTLY_IN_FORCE
DECLARATION_AT_SIGNATURE != DOMESTIC_IMPLEMENTATION_VERIFIED
```

## 2. Instrument identity and entry-into-force rule

CETS No. 225 is the **Council of Europe Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law**. It was adopted by the Committee of Ministers on 17 May 2024 and opened for signature in Vilnius on 5 September 2024.

Article 30 makes the Convention subject to ratification, acceptance or approval. Under Article 30(3), treaty-wide entry into force requires five Signatories to express consent to be bound, including at least three Council of Europe member States; entry into force then occurs on the first day of the month after expiry of three months from the fifth qualifying consent.

As of the official Treaty Office status snapshot `{STATUS_AS_OF}`:

```text
TOTAL_SIGNATORIES = 21
SIGNATURES_NOT_FOLLOWED_BY_RATIFICATION_OR_APPROVAL = 20
RATIFICATIONS_OR_APPROVALS = 1
QUALIFYING_COE_MEMBER_RATIFICATIONS = 0
ONLY_APPROVAL_DEPOSITED = EUROPEAN_UNION_2026-05-15
ENTRY_INTO_FORCE_THRESHOLD_MET = NO
TREATY_WIDE_ENTRY_INTO_FORCE = NOT_YET
```

The current Council of Europe AI overview separately lists the European Union under “Parties” and lists the 21 signatories. R004 preserves the controlling Article 30 threshold and Treaty Office status: one deposited approval does not satisfy the five-consent / three-member-State threshold.

## 3. Current signatory set

The exact 21-row status matrix is stored in `CETS_225_SIGNATURE_RATIFICATION_MATRIX.csv`.

Council of Europe member-State signatories (15): Albania, Andorra, Armenia, Bosnia and Herzegovina, Georgia, Iceland, Liechtenstein, Montenegro, North Macedonia, Norway, Republic of Moldova, San Marino, Switzerland, Ukraine and the United Kingdom.

Non-member participants that have signed (5): Canada, Israel, Japan, United States of America and Uruguay.

International organisation signatory/approver (1): European Union.

No Council of Europe member State has deposited ratification/acceptance/approval in the current Treaty Office snapshot.

## 4. Reservations and declarations

The current Treaty Office reservations/declarations page displays declarations for three entities and no reservation entries for CETS No. 225 in the retrieved current result.

### European Union

On 15 May 2026, with its instrument of approval, the European Union deposited:

- an Article 3(1)(b) declaration stating that, for relevant private-actor activities, it will apply Chapters II to VI through implementation of Regulation (EU) 2024/1689 (the EU AI Act), with other relevant Union acquis potentially also contributing; and
- an Article 32(1) territorial-scope declaration tying application, within Union competence, to the territories in which the EU Treaties apply under the stated EU Treaty rules.

This declaration records the EU's implementation route. It does not convert the CETS 225 treaty into an already-entered-into-force instrument.

### Norway

At signature on 5 September 2024, Norway declared under Article 3(1)(b) that it shall apply the principles and obligations in Chapters II to VI to private-actor activities.

Norway remains signed but not ratified in the current Treaty Office status. R004 therefore treats this as a recorded prospective treaty-scope declaration, not proof that CETS 225 is already in force domestically for Norway.

### Ukraine

At signature on 15 May 2025, Ukraine deposited:

- an Article 3(1)(b) declaration choosing the “other appropriate measures” route for private entities not covered by Article 3(1)(a); and
- an Article 32(1) territorial declaration concerning territory temporarily occupied by the Russian Federation, under the conditions stated in the declaration.

Ukraine remains signed but not ratified in the current Treaty Office status. Domestic implementation and legal effect are not inferred by R004.

### Reservation state

Article 34 allows only the reservation contemplated by Article 33(1) and excludes reservations to other provisions. The current Treaty Office result retrieved for CETS 225 displays no reservation entries. Because the Treaty Office is dynamic, this is recorded as a dated current-source state, not an immutable proposition.

## 5. Implementation-status boundary

R004 maps **treaty participation and declared implementation route**, not national implementing law.

- European Union: approval deposited; Article 3 private-actor route declared through the AI Act and relevant Union acquis; CETS 225 itself has not yet entered into force.
- Norway: signature only; Article 3 declaration selects direct application of Chapters II–VI to private actors if/when treaty obligations become operative; domestic implementation not verified here.
- Ukraine: signature only; Article 3 declaration selects other appropriate measures; territorial declaration recorded; domestic implementation not verified here.
- Remaining signatories: signature dates verified; no current CETS 225 declaration displayed for them in the Treaty Office result used by R004; domestic implementation not researched.

The EU AI Act and other domestic/regional laws may already create independent obligations. Their independent legal force must not be attributed to CETS 225 while the Framework Convention remains not yet in force.

```text
EU_AI_ACT_APPLICABLE != CETS225_IN_FORCE
NATIONAL_AI_LAW_OR_POLICY != CETS225_IMPLEMENTATION_PROVEN
SIGNATORY_STATUS != DOMESTIC_DIRECT_EFFECT
NO_DECLARATION_DISPLAYED != NO_DOMESTIC_MEASURES
```

## 6. Monitoring / follow-up state

The Convention provides a follow-up mechanism in Chapter VII, but the Conference of the Parties cannot be treated as an already-operational treaty body before the Convention enters into force. The current Council of Europe digital-governance layer identifies CDNET as custodian of the Framework Convention until the Conference of the Parties is established.

R004 does not infer enforcement powers, individual complaint rights or civil-liability consequences from the Convention.

## 7. R004 stop boundary

R004 does **not** determine:

- the domestic legal effect of signature under each signatory's constitutional/treaty law;
- general international-law consequences of signature pending entry into force;
- national ratification procedures currently underway but not deposited with the Treaty Office;
- national implementing legislation, regulations, administrative measures or voluntary measures;
- ECHR case-law implications or interaction with existing Council of Europe instruments;
- concrete actor classification, breach, causation, damages, sanctions or remedies;
- whether any State will ratify in the future or when the Article 30 threshold will be met.

```text
R004_CETS225_L1_L2_STATUS_BASELINE = COMPLETE
TREATY_WIDE_ENTRY_INTO_FORCE = NO
DOMESTIC_IMPLEMENTATION_MAP = NOT_ATTEMPTED_BEYOND_OFFICIAL_DECLARED_ROUTE
CASE_LAW = NOT_ATTEMPTED
LIABILITY_CONCLUSION = NOT_ATTEMPTED
NEW_BINARY_DOWNLOADS = 0
NOTEBOOK_UPLOADS = 0
DERIVED_MARKDOWN_CREATED = 0
ZIP_OR_ARTIFACT_CREATED = NO
AUTO_ADVANCE = NO
```
'''

# Signature / ratification matrix
buf = io.StringIO()
w = csv.writer(buf, lineterminator='\n')
w.writerow(['entity','entity_class','signature_date','ratification_acceptance_or_approval_date','treaty_entry_into_force_for_entity','status_2026_09_14','declaration_displayed','domestic_effect_state','official_status_as_of','claim_state'])
for entity, cls, sig, rat, status, decl in signatories:
    domestic = 'NOT_VERIFIED'
    if entity == 'European Union':
        domestic = 'EU_IMPLEMENTATION_ROUTE_DECLARED_VIA_AI_ACT_AND_RELEVANT_ACQUIS_TREATY_EFFECT_NOT_YET_IN_FORCE'
    elif entity == 'Norway':
        domestic = 'ARTICLE_3_ROUTE_DECLARED_DOMESTIC_EFFECT_NOT_VERIFIED'
    elif entity == 'Ukraine':
        domestic = 'ARTICLE_3_AND_TERRITORIAL_ROUTE_DECLARED_DOMESTIC_EFFECT_NOT_VERIFIED'
    w.writerow([entity, cls, sig, rat, '', status, decl, domestic, STATUS_AS_OF, 'VERIFIED_CURRENT_TREATY_OFFICE_BASELINE'])
sig_csv = buf.getvalue()

# Declaration / reservation matrix
buf = io.StringIO()
w = csv.writer(buf, lineterminator='\n')
w.writerow(['record_id','entity','record_type','deposit_or_signature_date','article','route_or_subject','current_participation_state','source_status_as_of','claim_state','caveat'])
w.writerow(['R004-DEC-001','European Union','DECLARATION','2026-05-15','Article 3(1)(b)','Apply Chapters II-VI to relevant private-actor activities through Regulation (EU) 2024/1689 and other relevant Union acquis','APPROVAL_DEPOSITED_TREATY_NOT_YET_IN_FORCE',STATUS_AS_OF,'VERIFIED_PRIMARY','Implementation route declaration does not itself establish treaty entry into force'])
w.writerow(['R004-DEC-002','European Union','DECLARATION','2026-05-15','Article 32(1)','Territorial scope tied to territories where EU Treaties apply under stated EU Treaty rules','APPROVAL_DEPOSITED_TREATY_NOT_YET_IN_FORCE',STATUS_AS_OF,'VERIFIED_PRIMARY','Territorial declaration recorded; concrete territorial application may require EU-law analysis'])
w.writerow(['R004-DEC-003','Norway','DECLARATION','2024-09-05','Article 3(1)(b)','Apply Chapters II-VI to activities of private actors','SIGNED_NOT_RATIFIED',STATUS_AS_OF,'VERIFIED_PRIMARY','Prospective treaty-scope declaration; domestic treaty effect not verified'])
w.writerow(['R004-DEC-004','Ukraine','DECLARATION','2025-05-15','Article 3(1)(b)','Take other appropriate measures for private entities not covered by Article 3(1)(a)','SIGNED_NOT_RATIFIED',STATUS_AS_OF,'VERIFIED_PRIMARY','Prospective treaty-scope declaration; domestic implementation not verified'])
w.writerow(['R004-DEC-005','Ukraine','DECLARATION','2025-05-15','Article 32(1)','Territorial non-application to temporarily occupied territory under conditions stated in declaration','SIGNED_NOT_RATIFIED',STATUS_AS_OF,'VERIFIED_PRIMARY','Record declaration text/conditions exactly from Treaty Office before country-specific use'])
w.writerow(['R004-RES-001','CURRENT_CETS225_TREATY_OFFICE_RESULT','RESERVATION_STATUS_SUMMARY',STATUS_AS_OF,'Article 34 / Article 33(1)','No reservation entry displayed in current Treaty Office result; declaration entries displayed for EU, Norway and Ukraine','DYNAMIC_SOURCE_STATE',STATUS_AS_OF,'VERIFIED_CURRENT_PAGE_OUTPUT','Recheck dynamic Treaty Office before future country-effect statement'])
decl_csv = buf.getvalue()

# Implementation-status matrix
buf = io.StringIO()
w = csv.writer(buf, lineterminator='\n')
w.writerow(['entity','consent_state','cets225_in_force_for_entity','article3_private_actor_route','territorial_declaration','domestic_implementation_state','independent_law_note','claim_state'])
for entity, cls, sig, rat, status, decl in signatories:
    route = 'NO_CURRENT_DECLARATION_DISPLAYED'
    territorial = 'NO_CURRENT_DECLARATION_DISPLAYED'
    independent = 'NOT_RESEARCHED_IN_R004'
    if entity == 'European Union':
        route = 'CHAPTERS_II_VI_VIA_EU_AI_ACT_AND_OTHER_RELEVANT_UNION_ACQUIS'
        territorial = 'ARTICLE_32_1_EU_TREATY_TERRITORIAL_SCOPE_DECLARATION'
        independent = 'EU_AI_ACT_AND_OTHER_UNION_LAW_MAY_APPLY_INDEPENDENTLY_OF_CETS225_ENTRY_INTO_FORCE'
    elif entity == 'Norway':
        route = 'APPLY_CHAPTERS_II_VI_TO_PRIVATE_ACTORS'
    elif entity == 'Ukraine':
        route = 'OTHER_APPROPRIATE_MEASURES_FOR_PRIVATE_ENTITIES'
        territorial = 'ARTICLE_32_1_TEMPORARILY_OCCUPIED_TERRITORY_DECLARATION'
    consent = 'APPROVAL_DEPOSITED' if entity == 'European Union' else 'SIGNATURE_ONLY'
    w.writerow([entity, consent, 'NO_TREATY_WIDE_ENTRY_INTO_FORCE', route, territorial, 'NOT_VERIFIED' if entity != 'European Union' else 'DECLARED_ROUTE_VERIFIED_CONCRETE_TREATY_EFFECT_NOT_YET_IN_FORCE', independent, 'VERIFIED_PARTICIPATION_STATE_DOMESTIC_EFFECT_OPEN'])
impl_csv = buf.getvalue()

closeout_md = f'''# AI-LAWS-R004 — CETS 225 Treaty-Status Baseline Closeout

**UNIT_ID:** `AI-LAWS-R004`  
**ROLE:** LEGAL_ANALYST / RESEARCHER  
**RESEARCH_DATE:** {DATE}  
**OFFICIAL_TREATY_OFFICE_STATUS_AS_OF:** {STATUS_AS_OF}  
**AUTO_ADVANCE:** NO

## Scope

This bounded unit established the current L1/L2 treaty-participation baseline for CETS No. 225 using the live Council of Europe Treaty Office and official Council of Europe AI/treaty materials. It did not perform national implementation research, case-law research, liability analysis, Notebook ingestion or binary vendoring.

## Result

```text
CETS225_SIGNATORIES_TOTAL = 21
SIGNATURES_NOT_FOLLOWED_BY_RATIFICATION_OR_APPROVAL = 20
RATIFICATIONS_OR_APPROVALS = 1
EU_APPROVAL_DATE = 2026-05-15
COE_MEMBER_RATIFICATIONS = 0
ARTICLE30_ENTRY_INTO_FORCE_THRESHOLD_MET = NO
TREATY_WIDE_ENTRY_INTO_FORCE = NO
DECLARING_ENTITIES = 3
DECLARATION_ENTRIES = 5
RESERVATION_ENTRIES_DISPLAYED = 0
DOMESTIC_IMPLEMENTATION_VERIFIED = 0
NEW_BINARY_DOWNLOADS = 0
NOTEBOOK_UPLOADS = 0
DERIVED_MARKDOWN_CREATED = 0
ZIP_OR_ARTIFACT_CREATED = NO
LEGAL_ADVICE = NO
LIABILITY_CONCLUSION = NOT_ATTEMPTED
AUTO_ADVANCE = NO
```

## Critical corrections / safeguards

- CETS 225 is a legally binding treaty instrument **in form**, but it has not yet satisfied Article 30(3)'s entry-into-force threshold.
- The European Union is the only entity with deposited approval in the current Treaty Office snapshot; that alone does not bring the Convention into force.
- No Council of Europe member State has deposited ratification/acceptance/approval in the current status snapshot.
- A signature is not treated as ratification or as verified domestic treaty effect.
- The EU, Norway and Ukraine declarations are preserved exactly as implementation/scope-route evidence; they are not promoted into findings that domestic implementation is complete.
- The current Treaty Office declarations page displays no reservation entries for CETS 225; this remains a dynamic dated source state requiring refresh.
- Existing `INT-001` repository PDF remains treaty text, not a live treaty-status snapshot.

## Durable outputs

- `20_JURISDICTIONS/COE/CETS_225_CURRENT_TREATY_STATUS_MAP_2026-09-14.md`
- `20_JURISDICTIONS/COE/CETS_225_SIGNATURE_RATIFICATION_MATRIX.csv`
- `20_JURISDICTIONS/COE/CETS_225_DECLARATIONS_RESERVATIONS_MATRIX.csv`
- `20_JURISDICTIONS/COE/CETS_225_IMPLEMENTATION_STATUS_MATRIX.csv`
- this closeout
- reconciled jurisdiction registry, research queue, source manifest and current context

## Stop condition

R004 stops before national ratification-procedure research, domestic implementation/effect, general treaty-law consequences of signature, ECHR interaction, case law, concrete classification, breach, causation, remedies or liability.

```text
STOP = YES
AUTO_ADVANCE = NO
```
'''

outputs = {
    '20_JURISDICTIONS/COE/CETS_225_CURRENT_TREATY_STATUS_MAP_2026-09-14.md': map_md,
    '20_JURISDICTIONS/COE/CETS_225_SIGNATURE_RATIFICATION_MATRIX.csv': sig_csv,
    '20_JURISDICTIONS/COE/CETS_225_DECLARATIONS_RESERVATIONS_MATRIX.csv': decl_csv,
    '20_JURISDICTIONS/COE/CETS_225_IMPLEMENTATION_STATUS_MATRIX.csv': impl_csv,
    '95_RESEARCH/COE/AI-LAWS-R004_CLOSEOUT_2026-09-14.md': closeout_md,
}
for rel, content in outputs.items():
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content.rstrip() + '\n', encoding='utf-8')

# Queue reconciliation
q = ROOT / '90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv'
qt = q.read_text(encoding='utf-8')
qlines = qt.splitlines()
found = False
for i, line in enumerate(qlines):
    if line.startswith('AI-LAWS-R004,'):
        assert ',READY_RESEARCH,' in line, line
        qlines[i] = 'AI-LAWS-R004,P0,Council of Europe,"CETS 225 current treaty-status, declarations/reservations and implementation map",COMPLETE_RESEARCH_BASELINE_L1_L2,NONE,20_JURISDICTIONS/COE/CETS_225_CURRENT_TREATY_STATUS_MAP_2026-09-14.md; 20_JURISDICTIONS/COE/CETS_225_SIGNATURE_RATIFICATION_MATRIX.csv; 20_JURISDICTIONS/COE/CETS_225_DECLARATIONS_RESERVATIONS_MATRIX.csv; 20_JURISDICTIONS/COE/CETS_225_IMPLEMENTATION_STATUS_MATRIX.csv; 95_RESEARCH/COE/AI-LAWS-R004_CLOSEOUT_2026-09-14.md,"current treaty participation/declaration baseline complete; stop before domestic effect/implementation law, general treaty-law signature effects, case law or liability conclusions"'
        found = True
        break
assert found
q.write_text('\n'.join(qlines) + '\n', encoding='utf-8')

# Jurisdiction registry reconciliation
jr = ROOT / '20_JURISDICTIONS/JURISDICTION_RESEARCH_REGISTRY.csv'
jt = jr.read_text(encoding='utf-8')
jlines = jt.splitlines()
found = False
for i, line in enumerate(jlines):
    if line.startswith('REG-COE,'):
        jlines[i] = 'REG-COE,Council of Europe,REGIONAL_INTERNATIONAL_ORGANIZATION,EUROPE,CETS225_L1_L2_TREATY_STATUS_BASELINE_COMPLETE_DOMESTIC_EFFECT_OPEN,P0,AI Framework Convention; ECHR rights; rule of law,"R004 current Treaty Office baseline on 2026-09-14 (official status as of 2026-09-12): 21 signatories; 20 signatures not followed by ratification/approval; European Union approval deposited 2026-05-15; 0 CoE member-State ratifications; Article 30 entry-into-force threshold not met. Current declarations displayed for EU, Norway and Ukraine; no reservation entry displayed. Domestic implementation/effect remains unverified per State and must not be inferred from signature."'
        found = True
        break
assert found
jr.write_text('\n'.join(jlines) + '\n', encoding='utf-8')

# Source manifest reconciliation for the dynamic treaty-status source
mf = ROOT / '86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv'
mt = mf.read_text(encoding='utf-8')
mlines = mt.splitlines()
found = False
for i, line in enumerate(mlines):
    if line.startswith('INT-001,'):
        mlines[i] = 'INT-001,NB01,COE,Council of Europe Framework Convention on Artificial Intelligence and Human Rights Democracy and the Rule of Law,CETS No.225,TREATY_OR_INTERNATIONAL_INSTRUMENT,treaty instrument; Article 30 entry-into-force threshold not met as of R004 snapshot,https://www.coe.int/en/web/conventions/full-list?module=treaty-detail&treatynum=225,URL_DIRECT_PREFERRED,P0,VERIFIED_OFFICIAL_CURRENT_TREATY_STATUS_R004,2026-09-14,OFFICIAL_PUBLIC_URL,"R004 live Treaty Office baseline (status as of 2026-09-12): 21 signatories; 20 signature-only; 1 approval/ratification (EU, 2026-05-15); 0 CoE-member ratifications; Article 30 threshold unmet. Current declarations displayed for EU, Norway and Ukraine; no reservation entry displayed. Repository INT-001 binary is treaty text, not live status; recheck dynamic Treaty Office before country-effect claims."'
        found = True
        break
assert found
mf.write_text('\n'.join(mlines) + '\n', encoding='utf-8')

# Current context reconciliation
ctx = ROOT / '00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md'
ct = ctx.read_text(encoding='utf-8')
old_state = '**STATE:** R001_COMPLETE / R003_EU_AI_ACT_L1_L2_COMPLETE / R021_COMPLETE'
new_state = '**STATE:** R001_COMPLETE / R003_EU_AI_ACT_L1_L2_COMPLETE / R004_CETS225_L1_L2_COMPLETE / R021_COMPLETE'
assert old_state in ct
ct = ct.replace(old_state, new_state, 1)
assert 'AI-LAWS-R003 = COMPLETE_RESEARCH_BASELINE_L1_L2\nAI-LAWS-R021' in ct
ct = ct.replace('AI-LAWS-R003 = COMPLETE_RESEARCH_BASELINE_L1_L2\nAI-LAWS-R021', 'AI-LAWS-R003 = COMPLETE_RESEARCH_BASELINE_L1_L2\nAI-LAWS-R004 = COMPLETE_RESEARCH_BASELINE_L1_L2\nAI-LAWS-R021', 1)
marker = 'Durable outputs are under `20_JURISDICTIONS/EU/` plus `95_RESEARCH/EU/AI-LAWS-R003_CLOSEOUT_2026-09-14.md`.\n\n### R021'
assert marker in ct
r004_section = '''Durable outputs are under `20_JURISDICTIONS/EU/` plus `95_RESEARCH/EU/AI-LAWS-R003_CLOSEOUT_2026-09-14.md`.

### R004 — Council of Europe CETS 225 current treaty-status baseline

R004 established the current treaty-participation/declaration baseline from the Council of Europe Treaty Office and official Convention materials.

```text
CETS225_SIGNATORIES_TOTAL = 21
CETS225_SIGNATURE_ONLY = 20
CETS225_RATIFICATIONS_OR_APPROVALS = 1
CETS225_ONLY_APPROVAL = EUROPEAN_UNION_2026-05-15
CETS225_COE_MEMBER_RATIFICATIONS = 0
CETS225_ARTICLE30_ENTRY_INTO_FORCE_THRESHOLD_MET = NO
CETS225_TREATY_WIDE_ENTRY_INTO_FORCE = NO
CETS225_DECLARING_ENTITIES = EU; NORWAY; UKRAINE
CETS225_DECLARATION_ENTRIES = 5
CETS225_RESERVATION_ENTRIES_DISPLAYED = 0
DOMESTIC_IMPLEMENTATION = NOT_VERIFIED
CASE_LAW = NOT_ATTEMPTED
LIABILITY_CONCLUSION = NOT_ATTEMPTED
```

Durable outputs are under `20_JURISDICTIONS/COE/` plus `95_RESEARCH/COE/AI-LAWS-R004_CLOSEOUT_2026-09-14.md`.

`SIGNATURE != RATIFICATION`, `LEGALLY_BINDING_TREATY_FORM != CURRENTLY_IN_FORCE`, and `DECLARATION_AT_SIGNATURE != DOMESTIC_IMPLEMENTATION_VERIFIED` remain controlling boundaries.

### R021'''
ct = ct.replace(marker, r004_section, 1)
old_next = '''### Completed preferred substantive legal-research unit

```text
AI-LAWS-R003 — EU AI ACT CURRENT CONSOLIDATED / PHASED-APPLICATION LEGAL MAP
STATE = COMPLETE_RESEARCH_BASELINE_L1_L2
```

R003 is complete at L1/L2 baseline level. No subsequent substantive research unit is auto-started. Member-State implementation/transposition, case law, delegated/implementing-act refresh and concrete liability/classification questions remain separate bounded work.
'''
assert old_next in ct
new_next = '''### Completed substantive legal-research units

```text
AI-LAWS-R003 — EU AI ACT CURRENT CONSOLIDATED / PHASED-APPLICATION LEGAL MAP
STATE = COMPLETE_RESEARCH_BASELINE_L1_L2

AI-LAWS-R004 — COUNCIL OF EUROPE CETS 225 CURRENT TREATY-STATUS / DECLARATION MAP
STATE = COMPLETE_RESEARCH_BASELINE_L1_L2
```

R003 and R004 are complete at their bounded L1/L2 baseline levels. R004 does not establish domestic treaty effect or national implementation for any signatory. No subsequent substantive research unit is auto-started; the queue remains authoritative for the next explicit bounded selection.
'''
ct = ct.replace(old_next, new_next, 1)
assert 'R003_LIABILITY_CONCLUSION = NOT_ATTEMPTED\nNOTEBOOK_UPLOAD_COUNT = 0' in ct
ct = ct.replace('R003_LIABILITY_CONCLUSION = NOT_ATTEMPTED\nNOTEBOOK_UPLOAD_COUNT = 0', '''R003_LIABILITY_CONCLUSION = NOT_ATTEMPTED
R004_CETS225_BASELINE = COMPLETE_L1_L2
R004_CETS225_TREATY_OFFICE_STATUS_AS_OF = 2026-09-12
R004_CETS225_SIGNATORIES_TOTAL = 21
R004_CETS225_SIGNATURE_ONLY = 20
R004_CETS225_RATIFICATIONS_OR_APPROVALS = 1
R004_CETS225_COE_MEMBER_RATIFICATIONS = 0
R004_CETS225_ENTRY_INTO_FORCE = NO
R004_CETS225_DECLARATION_ENTRIES = 5
R004_CETS225_RESERVATION_ENTRIES_DISPLAYED = 0
R004_DOMESTIC_IMPLEMENTATION = NOT_VERIFIED
R004_CASE_LAW = NOT_ATTEMPTED
R004_LIABILITY_CONCLUSION = NOT_ATTEMPTED
NOTEBOOK_UPLOAD_COUNT = 0''', 1)
ctx.write_text(ct, encoding='utf-8')

# Sanity checks
assert 'European Union,INTERNATIONAL_ORGANISATION,2024-09-05,2026-05-15' in sig_csv
assert 'Ukraine,COE_MEMBER,2025-05-15' in sig_csv
assert 'Norway,COE_MEMBER,2024-09-05' in sig_csv
assert 'Türkiye' not in sig_csv
assert 'COMPLETE_RESEARCH_BASELINE_L1_L2' in q.read_text(encoding='utf-8')
assert 'CETS225_L1_L2_TREATY_STATUS_BASELINE_COMPLETE_DOMESTIC_EFFECT_OPEN' in jr.read_text(encoding='utf-8')
assert 'VERIFIED_OFFICIAL_CURRENT_TREATY_STATUS_R004' in mf.read_text(encoding='utf-8')
assert 'R004_CETS225_L1_L2_COMPLETE' in ctx.read_text(encoding='utf-8')

print('R004_PERSIST_ASSERTIONS=PASS')
print('R004_STATE=COMPLETE_RESEARCH_BASELINE_L1_L2')
print('SIGNATORIES_TOTAL=21')
print('SIGNATURE_ONLY=20')
print('RATIFICATIONS_OR_APPROVALS=1')
print('COE_MEMBER_RATIFICATIONS=0')
print('ENTRY_INTO_FORCE=NO')
print('DECLARATION_ENTRIES=5')
print('RESERVATION_ENTRIES_DISPLAYED=0')
print('NEW_BINARY_DOWNLOADS=0')
print('ZIP_OR_ARTIFACT_CREATED=NO')
print('AUTO_ADVANCE=NO')
