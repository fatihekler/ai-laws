from pathlib import Path

RESEARCH_SHA='8d4fb9affa2bbc7900c2cbb48961b813c6ac6442'
STATE='COMPLETE_RESEARCH_BASELINE_L1_L2_STATE_SYSTEMS_EU_US_OVERSIGHT_IMMUNITY_SCOPE_LIMITS_OPEN'

# Queue reconciliation.
qpath=Path('90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv')
q=qpath.read_text(encoding='utf-8')
old='AI-LAWS-R017,P0,State systems,"National-security, defence, intelligence, sovereign-immunity and oversight gaps for closed/state AI systems",READY_RESEARCH,jurisdiction profiles,state-accountability gap map,do not infer classified facts'
new='AI-LAWS-R017,P0,State systems,"National-security, defence, intelligence, sovereign-immunity and oversight gaps for closed/state AI systems",'+STATE+',jurisdiction profiles,77_STATE_SYSTEMS/AI-LAWS-R017_STATE_SYSTEMS_ACCOUNTABILITY_BASELINE_2026-09-14.md; 77_STATE_SYSTEMS/AI-LAWS-R017_ACCOUNTABILITY_GAP_MATRIX_2026-09-14.csv; 77_STATE_SYSTEMS/AI-LAWS-R017_SOURCE_AND_CURRENTNESS_MATRIX_2026-09-14.csv; 95_RESEARCH/STATE_SYSTEMS/AI-LAWS-R017_CLOSEOUT_2026-09-14.md,"bounded EU/CoE + U.S. federal public-source state-systems baseline complete; classified facts, Member-State/agency-specific law, case law, state-secrets/classified procedure, FTCA exhaustion and DoD 3000.09 body remain open; do not infer classified facts or universal immunity"'
assert old in q, 'R017 queue READY row not found exactly'
q=q.replace(old,new,1)
qpath.write_text(q,encoding='utf-8')

# Current context reconciliation.
cpath=Path('00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md')
c=cpath.read_text(encoding='utf-8')
old_state='R016_COMPETITION_BASELINE_COMPLETE_SCOPE_LIMITS_OPEN / R021_COMPLETE'
new_state='R016_COMPETITION_BASELINE_COMPLETE_SCOPE_LIMITS_OPEN / R017_STATE_SYSTEMS_BASELINE_COMPLETE_SCOPE_LIMITS_OPEN / R021_COMPLETE'
assert old_state in c, 'top STATE insertion marker missing'
c=c.replace(old_state,new_state,1)
old_completed='AI-LAWS-R016 = COMPLETE_RESEARCH_BASELINE_L1_L2_COMPETITION_EU_US_COORDINATION_MARKET_STRUCTURE_SCOPE_LIMITS_OPEN\nAI-LAWS-R021 = COMPLETE_SUPPORT_INFRASTRUCTURE'
new_completed='AI-LAWS-R016 = COMPLETE_RESEARCH_BASELINE_L1_L2_COMPETITION_EU_US_COORDINATION_MARKET_STRUCTURE_SCOPE_LIMITS_OPEN\nAI-LAWS-R017 = '+STATE+'\nAI-LAWS-R021 = COMPLETE_SUPPORT_INFRASTRUCTURE'
assert old_completed in c, 'completed-unit insertion marker missing'
c=c.replace(old_completed,new_completed,1)
section='''### R017 state systems accountability baseline

```text
AI-LAWS-R017 — STATE SYSTEMS / NATIONAL SECURITY / DEFENCE / INTELLIGENCE / IMMUNITY
STATE = COMPLETE_RESEARCH_BASELINE_L1_L2_STATE_SYSTEMS_EU_US_OVERSIGHT_IMMUNITY_SCOPE_LIMITS_OPEN
NEXT_BOUNDED_UNIT = NONE_AUTO_SELECTED
```

R017 maps instrument-specific national-security/defence scope boundaries, selected alternative rights/oversight layers, U.S. federal sovereign-immunity/judicial-review/remedy architecture, and public-evidence limits without inferring classified facts. The controlled AI Act Article 2 national-security/military/defence boundary is treated only as an AI-Act scope rule: `EXEMPT_FROM_AI_ACT != EXEMPT_FROM_ALL_LAW`.

The controlled CETS 225 treaty text verifies its Article 3 national-security/national-defence structure, but R004's treaty-status gate remains controlling and treaty-wide entry into force was not established. The live official ECHR PDF verifies the selected Articles 8/13 rights/remedy layer subject to jurisdiction, admissibility and merits analysis.

For the United States, OMB M-25-21 was freshly rechecked and exactly matches the repository PDF (`SHA-256 0aab0aa4eaeac969ed93894d3940c5dc9d0b7377048171b164a439e8b9e49813`). Its verified scope is directed to Executive Branch departments/agencies including independent regulatory agencies; R017 did not verify the initially hypothesized separate `44 U.S.C. §3552` national-security-system carve-out within M-25-21 and therefore states none. Current 44 U.S.C. §3552, 5 U.S.C. §702, 28 U.S.C. §§1346(b)/2674/2680 and 50 U.S.C. §3033 were live official-source marker-verified as distinct definition, review, FTCA and intelligence-oversight layers.

The official DoD Directive 3000.09 candidate URL returned HTTP 403 to the GitHub runner; no directive-body finding was admitted. Actual classified AI deployments/capabilities/incidents remain `UNKNOWN_NOT_INFERRED`. Durable outputs are under `77_STATE_SYSTEMS/` and `95_RESEARCH/STATE_SYSTEMS/`.

'''
marker='### Notebook/source-processing lane'
assert marker in c, 'R017 section insertion marker missing'
assert '### R017 state systems accountability baseline' not in c, 'R017 context section already present'
c=c.replace(marker,section+marker,1)
cpath.write_text(c,encoding='utf-8')

# Closeout research SHA reconciliation and whitespace normalization.
ppath=Path('95_RESEARCH/STATE_SYSTEMS/AI-LAWS-R017_CLOSEOUT_2026-09-14.md')
p=ppath.read_text(encoding='utf-8')
assert '**R017_RESEARCH_COMMIT:** `PENDING_RECONCILIATION`' in p
p=p.replace('**R017_RESEARCH_COMMIT:** `PENDING_RECONCILIATION`','**R017_RESEARCH_COMMIT:** `'+RESEARCH_SHA+'`',1)
p='\n'.join(line.rstrip() for line in p.splitlines())+'\n'
ppath.write_text(p,encoding='utf-8')

# Fail closed if control invariants were accidentally changed.
assert '**AUTO_ADVANCE:** NO' in c
assert 'AI-LAWS-R019' in q and 'READY_FOR_EXPLICIT_AUTHORIZATION' in q
print('R017_RECONCILED=YES')
print('R017_RESEARCH_COMMIT='+RESEARCH_SHA)
print('AUTO_ADVANCE=NO')