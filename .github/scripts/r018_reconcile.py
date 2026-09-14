from pathlib import Path

RESEARCH='4f897f0f195933f8a974ef3cbb50a62e5cb5b152'
STATE='COMPLETE_RESEARCH_BASELINE_L1_L2_CROSS_BORDER_US_FEDERAL_EU_SCOPE_PIL_BODY_ACCESS_LIMITS_OPEN'

q=Path('90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv')
s=q.read_text()
old='AI-LAWS-R018,P1,Cross-border,"Jurisdiction, applicable law, enforcement and cross-border AI harm",READY_RESEARCH,R002 plus national profiles,conflict-of-laws matrix,no universal forum rule'
new='AI-LAWS-R018,P1,Cross-border,"Jurisdiction, applicable law, enforcement and cross-border AI harm",'+STATE+',R002 plus national profiles,78_CROSS_BORDER/AI-LAWS-R018_CROSS_BORDER_JURISDICTION_APPLICABLE_LAW_ENFORCEMENT_BASELINE_2026-09-14.md; 78_CROSS_BORDER/AI-LAWS-R018_CONFLICT_OF_LAWS_AND_ENFORCEMENT_MATRIX_2026-09-14.csv; 78_CROSS_BORDER/AI-LAWS-R018_SOURCE_AND_CURRENTNESS_MATRIX_2026-09-14.csv; 95_RESEARCH/CROSS_BORDER/AI-LAWS-R018_CLOSEOUT_2026-09-14.md,"bounded U.S. federal + EU regulatory-scope cross-border baseline complete; EU Brussels/Rome primary bodies remain runner-blocked; U.S. state recognition/long-arm, EU/Member-State case law, HCCH/treaty and concrete scenario analysis remain open; no universal forum/applicable-law/enforcement rule"'
assert old in s
q.write_text(s.replace(old,new))

c=Path('00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md')
s=c.read_text()
old_state='R017_STATE_SYSTEMS_BASELINE_COMPLETE_SCOPE_LIMITS_OPEN / R021_COMPLETE'
assert old_state in s
s=s.replace(old_state,'R017_STATE_SYSTEMS_BASELINE_COMPLETE_SCOPE_LIMITS_OPEN / R018_CROSS_BORDER_BASELINE_COMPLETE_SCOPE_LIMITS_OPEN / R021_COMPLETE',1)
old_completed='AI-LAWS-R017 = COMPLETE_RESEARCH_BASELINE_L1_L2_STATE_SYSTEMS_EU_US_OVERSIGHT_IMMUNITY_SCOPE_LIMITS_OPEN\nAI-LAWS-R021'
assert old_completed in s
s=s.replace(old_completed,'AI-LAWS-R017 = COMPLETE_RESEARCH_BASELINE_L1_L2_STATE_SYSTEMS_EU_US_OVERSIGHT_IMMUNITY_SCOPE_LIMITS_OPEN\nAI-LAWS-R018 = '+STATE+'\nAI-LAWS-R021',1)
marker='### Notebook/source-processing lane'
assert marker in s
section='''### R018 cross-border baseline\n\n```text\nAI-LAWS-R018 — CROSS-BORDER JURISDICTION / APPLICABLE LAW / ENFORCEMENT\nSTATE = '''+STATE+'''\nNEXT_BOUNDED_UNIT = NONE_AUTO_SELECTED\n```\n\nR018 separates regulatory territorial scope, forum/personal jurisdiction, service, venue, applicable law, evidence cooperation, judgment and recognition/enforcement. GDPR territorial-scope markers and selected U.S. federal procedural/statutory sources were verified; AI Act third-country/Union-use scope is reused only from R003's controlled Article 2 map.\n\nThe current FRCP pamphlet, 28 U.S.C. §1391 and 28 U.S.C. §1782 were live official-source marker-verified. Venue is not personal jurisdiction; evidence assistance is not judgment recognition.\n\nBrussels I bis, Rome I and Rome II official identities were targeted, but all EUR-Lex/data.europa.eu variants returned HTTP 202 challenge bodies to GitHub runners, while e-Justice fallbacks returned HTTP 403. No article-level proposition from those instruments was admitted by R018. U.S. state foreign-country judgment recognition, constitutional personal-jurisdiction case law, state long-arm law, HCCH treaty interfaces and concrete cross-border scenarios remain open.\n\nDurable outputs are under `78_CROSS_BORDER/` and `95_RESEARCH/CROSS_BORDER/`. No universal forum, applicable-law or enforcement rule was inferred.\n\n'''
s=s.replace(marker,section+marker,1)
c.write_text(s)

co=Path('95_RESEARCH/CROSS_BORDER/AI-LAWS-R018_CLOSEOUT_2026-09-14.md')
s=co.read_text(); assert '`TO_BE_RECONCILED`' in s
co.write_text(s.replace('`TO_BE_RECONCILED`','`'+RESEARCH+'`',1))

# fail closed on control markers
assert 'AI-LAWS-R018 = '+STATE in c.read_text()
assert 'R019 remains `READY_FOR_EXPLICIT_AUTHORIZATION`' in co.read_text()
assert '**AUTO_ADVANCE:** NO' in c.read_text()
print('R018_RECONCILED=YES')
print('R018_RESEARCH_COMMIT='+RESEARCH)
print('AUTO_ADVANCE=NO')
