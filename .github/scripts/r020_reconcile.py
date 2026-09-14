from pathlib import Path

QUEUE=Path('90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv')
CTX=Path('00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md')
CLOSE=Path('95_RESEARCH/CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_CLOSEOUT_2026-09-14.md')
CLOSE.parent.mkdir(parents=True,exist_ok=True)

STATE='COMPLETE_DESTINATION_NEUTRAL_LEGAL_REQUIREMENT_CANDIDATES_VALIDATED_DESTINATION_ACCEPTANCE_NOT_RUN'
RESEARCH='f62ad7cd716f424f255eb969d4f8ba4dd80de4a4'
STAGE='ad6d82da8b9d08d53f84042da1c248186077ed08'
BASE='f74c6a510071d8a4b04535b4301f4d8c8a2dd0e3'

# Queue: replace only the R020 record, preserving every other line byte-semantically except final newline normalization.
lines=QUEUE.read_text(encoding='utf-8').splitlines()
out=[]; found=False
newrow='AI-LAWS-R020,P1,Cross-repo requirements,Translate verified legal duties into destination-neutral requirement candidates for Engineering OS/OWASP/Ethical-AI review,'+STATE+',R003-R018 as relevant,79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_REQUIREMENT_CANDIDATE_METHOD_2026-09-14.md; 79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_MASTER_REQUIREMENT_CANDIDATE_MATRIX_2026-09-14.csv; 79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_ENGINEERING_OS_REVIEW_PACKET_2026-09-14.csv; 79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_OWASP_REVIEW_PACKET_2026-09-14.csv; 79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_ETHICAL_AI_REVIEW_PACKET_2026-09-14.csv; 79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_SOURCE_AND_AUTHORITY_MATRIX_2026-09-14.csv; 79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_VALIDATION_SUMMARY_2026-09-14.csv; 95_RESEARCH/CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_CLOSEOUT_2026-09-14.md,validated destination-neutral legal-duty candidate packets complete; destination acceptance remains separate and NOT_RUN; no destination repository mutation; R019 remains explicit-only'
for line in lines:
    if line.startswith('AI-LAWS-R020,'):
        out.append(newrow); found=True
    else:
        out.append(line)
if not found: raise SystemExit('R020_QUEUE_ROW_NOT_FOUND')
QUEUE.write_text('\n'.join(out)+'\n',encoding='utf-8')

text=CTX.read_text(encoding='utf-8')
short='R020_CROSS_REPO_REQUIREMENT_CANDIDATES_COMPLETE_DESTINATION_ACCEPTANCE_NOT_RUN'
if short not in text:
    marker='R018_CROSS_BORDER_BASELINE_COMPLETE_SCOPE_LIMITS_OPEN / R021_COMPLETE'
    repl='R018_CROSS_BORDER_BASELINE_COMPLETE_SCOPE_LIMITS_OPEN / '+short+' / R021_COMPLETE'
    if marker not in text: raise SystemExit('CONTEXT_STATE_MARKER_NOT_FOUND')
    text=text.replace(marker,repl,1)

complete_line='AI-LAWS-R020 = '+STATE
if complete_line not in text:
    marker='AI-LAWS-R018 = COMPLETE_RESEARCH_BASELINE_L1_L2_CROSS_BORDER_US_FEDERAL_EU_SCOPE_PIL_BODY_ACCESS_LIMITS_OPEN\nAI-LAWS-R021 = COMPLETE_SUPPORT_INFRASTRUCTURE'
    repl='AI-LAWS-R018 = COMPLETE_RESEARCH_BASELINE_L1_L2_CROSS_BORDER_US_FEDERAL_EU_SCOPE_PIL_BODY_ACCESS_LIMITS_OPEN\n'+complete_line+'\nAI-LAWS-R021 = COMPLETE_SUPPORT_INFRASTRUCTURE'
    if marker not in text: raise SystemExit('CONTEXT_COMPLETED_MARKER_NOT_FOUND')
    text=text.replace(marker,repl,1)

if '### R020 — Destination-neutral cross-repo legal requirement candidates' not in text:
    marker='## 3. Prior source-pack acquisition evidence'
    section='''### R020 — Destination-neutral cross-repo legal requirement candidates

R020 translated only already-verified binding legal duties into implementation candidates for later destination-repository review. No destination repository was modified and no candidate was accepted on behalf of Engineering OS, OWASP or Ethical-AI.

```text
R020_CANDIDATE_ROWS = 17
ENGINEERING_OS_REVIEW_PACKET_ROWS = 11
OWASP_REVIEW_PACKET_ROWS = 3
ETHICAL_AI_REVIEW_PACKET_ROWS = 3
FUTURE_PHASED_HIGH_RISK_ROWS = 4
NONBINDING_OR_CASE_ROWS = 0
DESTINATION_ACCEPTANCE = NOT_RUN
DESTINATION_MUTATIONS = 0
NOTEBOOK_UPLOADS = 0
ZIP_OR_ARTIFACT_CREATED = NO
```

The admitted duty layer is limited to verified EU AI Act and GDPR duties already controlled by R003, R014 and R015. High-risk AI Act logging, retention and QMS candidates preserve the future 2027/2028 phased application states rather than being represented as universally mandatory on 2026-09-14.

```text
LEGAL_DUTY_VERIFIED != DESTINATION_REQUIREMENT_ACCEPTED
TECHNICAL_CONTROL_CANDIDATE != LEGAL_TEXT
POLICY_GUIDANCE != BINDING_DUTY
FUTURE_APPLICATION != CURRENT_MANDATORY_DUTY
DESTINATION_ACCEPTANCE = NOT_RUN
```

Durable outputs are under `79_CROSS_REPO_REQUIREMENTS/` and `95_RESEARCH/CROSS_REPO_REQUIREMENTS/`. R019 remained explicit-only and was not started.

'''
    if marker not in text: raise SystemExit('CONTEXT_INSERT_MARKER_NOT_FOUND')
    text=text.replace(marker,section+marker,1)
CTX.write_text(text,encoding='utf-8')

close=f'''# AI-LAWS-R020 — Cross-Repo Requirement Candidate Closeout

**UNIT_ID:** `AI-LAWS-R020`
**DATE:** 2026-09-14
**BASE_HEAD:** `{BASE}`
**R020_STAGE_COMMIT:** `{STAGE}`
**R020_RESEARCH_COMMIT:** `{RESEARCH}`
**STATE:** `{STATE}`
**LEGAL_ADVICE:** NO
**DESTINATION_MUTATION:** NO
**AUTO_ADVANCE:** NO

## Scope completed

R020 created and deterministically validated a destination-neutral candidate layer from already-verified binding duties. It did not create requirements in Engineering OS, OWASP or Ethical-AI and did not claim destination acceptance.

Durable outputs:

- `79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_REQUIREMENT_CANDIDATE_METHOD_2026-09-14.md`
- `79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_MASTER_REQUIREMENT_CANDIDATE_MATRIX_2026-09-14.csv`
- `79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_ENGINEERING_OS_REVIEW_PACKET_2026-09-14.csv`
- `79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_OWASP_REVIEW_PACKET_2026-09-14.csv`
- `79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_ETHICAL_AI_REVIEW_PACKET_2026-09-14.csv`
- `79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_SOURCE_AND_AUTHORITY_MATRIX_2026-09-14.csv`
- `79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_VALIDATION_SUMMARY_2026-09-14.csv`
- `95_RESEARCH/CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_CLOSEOUT_2026-09-14.md`

## Validation record

```text
CANDIDATE_ROWS = 17
UNIQUE_CANDIDATE_IDS = 17
ENGINEERING_OS_PACKET_ROWS = 11
OWASP_PACKET_ROWS = 3
ETHICAL_AI_PACKET_ROWS = 3
FUTURE_PHASED_ROWS = 4
NONBINDING_OR_CASE_ROWS = 0
SOURCE_PATHS_MISSING = 0
DESTINATION_ACCEPTANCE_NOT_RUN_ROWS = 17
DESTINATION_MUTATIONS = 0
NOTEBOOK_UPLOADS = 0
ZIP_OR_ARTIFACT_CREATED = NO
```

The validator required every candidate to resolve to an existing controlled source record and expected source anchor. Candidate rows are limited to binding EU AI Act/GDPR duty sources used in R003/R014/R015. NIST guidance, policy material, withdrawn proposals and analogical case law were excluded from the binding-duty candidate rows.

## Temporal and authority limits

Four high-risk-AI candidates preserve R003's future/phased date state for Articles 12, 16-19 and 26(6). Their presence in a review packet is not a claim that the relevant duty is universally applicable on 2026-09-14.

Article 50, GPAI Article 53/55 and GDPR candidates retain their actor/scope/transition limitations. Technical-control wording is implementation-candidate language, not substituted statutory text.

## Firewalls preserved

```text
LEGAL_DUTY_VERIFIED != DESTINATION_REQUIREMENT_ACCEPTED
TECHNICAL_CONTROL_CANDIDATE != LEGAL_TEXT
PRIMARY_DESTINATION != DESTINATION_ACCEPTANCE
DESTINATION_REVIEW_PACKET != DESTINATION_MUTATION
POLICY_GUIDANCE != BINDING_DUTY
ANALOGICAL_PRECEDENT != DIRECT_AI_REQUIREMENT
FUTURE_APPLICATION != CURRENT_MANDATORY_DUTY
```

## Preserved state

- R005 remains unchanged and blocked at live Türkiye official-source recheck.
- R006 remains blocked by official decision-source availability.
- R019 remains `READY_FOR_EXPLICIT_AUTHORIZATION` and was not started.
- Destination acceptance for all 17 candidates remains `NOT_RUN`.
- No destination repository was read as source-of-truth or mutated by R020.

## Stop

```text
R020_CANDIDATE_LAYER = COMPLETE_VALIDATED_BASELINE
DESTINATION_ACCEPTANCE = NOT_RUN
DESTINATION_MUTATIONS = 0
R019 = NOT_STARTED
NEXT_BOUNDED_UNIT = NONE_AUTO_SELECTED
UNKNOWN_PRESERVED = YES
AUTO_ADVANCE = NO
STOP = YES
```
'''
CLOSE.write_text(close,encoding='utf-8')

print('R020_RECONCILED=YES')
print('R020_RESEARCH_COMMIT='+RESEARCH)
print('R019_STATE=READY_FOR_EXPLICIT_AUTHORIZATION')
print('DESTINATION_ACCEPTANCE=NOT_RUN')
print('DESTINATION_MUTATIONS=0')
print('AUTO_ADVANCE=NO')
