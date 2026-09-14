from pathlib import Path
import csv
import io

RESEARCH_COMMIT = 'f2b6bf03fa756f71c219b82d3b12e26f84bc57f9'
SOURCE_INITIAL = 'd35f672e927c83b2dfa09fa5bc0e8609a0949c80'
SOURCE_FINAL = '56cee0b39931738dda14f671a6a190ba696055e5'

# Queue reconciliation.
qpath = Path('90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv')
rows = list(csv.reader(qpath.read_text(encoding='utf-8').splitlines()))
hits = [i for i, row in enumerate(rows) if row and row[0] == 'AI-LAWS-R016']
if len(hits) != 1:
    raise SystemExit(f'R016 queue row count unexpected: {len(hits)}')
rows[hits[0]] = [
    'AI-LAWS-R016',
    'P1',
    'Competition',
    'Safety coordination, oligopoly, antitrust, regulatory capture and market-entry implications',
    'COMPLETE_RESEARCH_BASELINE_L1_L2_COMPETITION_EU_US_COORDINATION_MARKET_STRUCTURE_SCOPE_LIMITS_OPEN',
    'NONE',
    '76_COMPETITION/AI-LAWS-R016_COMPETITION_COORDINATION_AND_MARKET_STRUCTURE_BASELINE_2026-09-14.md; 76_COMPETITION/AI-LAWS-R016_COMPETITION_LAW_POLICY_MATRIX_2026-09-14.csv; 76_COMPETITION/AI-LAWS-R016_SOURCE_AND_CURRENTNESS_MATRIX_2026-09-14.csv; 95_RESEARCH/COMPETITION/AI-LAWS-R016_CLOSEOUT_2026-09-14.md',
    'bounded EU + U.S. federal competition baseline complete; public alignment, safety coordination, standards, concentration, partnerships and regulatory-capture hypotheses remain fact-specific; no cartel, monopolization, merger-violation or capture finding; other jurisdictions and case law remain open'
]
buf = io.StringIO()
csv.writer(buf, lineterminator='\n').writerows(rows)
qpath.write_text(buf.getvalue(), encoding='utf-8')

# Current context reconciliation.
cpath = Path('00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md')
ctx = cpath.read_text(encoding='utf-8')

old = ' / R015_CORPORATE_GOVERNANCE_BASELINE_COMPLETE_SCOPE_LIMITS_OPEN / R021_COMPLETE'
new = ' / R015_CORPORATE_GOVERNANCE_BASELINE_COMPLETE_SCOPE_LIMITS_OPEN / R016_COMPETITION_BASELINE_COMPLETE_SCOPE_LIMITS_OPEN / R021_COMPLETE'
if old not in ctx:
    raise SystemExit('R016 context state insertion marker missing')
ctx = ctx.replace(old, new, 1)

old = 'AI-LAWS-R015 = COMPLETE_RESEARCH_BASELINE_L1_L2_CORPORATE_GOVERNANCE_EU_US_DELAWARE_DISCLOSURE_SCOPE_LIMITS_OPEN\nAI-LAWS-R021 = COMPLETE_SUPPORT_INFRASTRUCTURE'
new = 'AI-LAWS-R015 = COMPLETE_RESEARCH_BASELINE_L1_L2_CORPORATE_GOVERNANCE_EU_US_DELAWARE_DISCLOSURE_SCOPE_LIMITS_OPEN\nAI-LAWS-R016 = COMPLETE_RESEARCH_BASELINE_L1_L2_COMPETITION_EU_US_COORDINATION_MARKET_STRUCTURE_SCOPE_LIMITS_OPEN\nAI-LAWS-R021 = COMPLETE_SUPPORT_INFRASTRUCTURE'
if old not in ctx:
    raise SystemExit('R016 completed-unit insertion marker missing')
ctx = ctx.replace(old, new, 1)

section_lines = [
    '### R016 competition baseline',
    '',
    '```text',
    'AI-LAWS-R016 — COMPETITION / COORDINATION / MARKET STRUCTURE',
    'STATE = COMPLETE_RESEARCH_BASELINE_L1_L2_COMPETITION_EU_US_COORDINATION_MARKET_STRUCTURE_SCOPE_LIMITS_OPEN',
    'NEXT_BOUNDED_UNIT = NONE_AUTO_SELECTED',
    '```',
    '',
    'R016 separates competitor coordination, standardisation/information sharing, dominance/monopolization, merger/partnership review, digital gatekeeper contestability, market-entry hypotheses and regulatory-capture claims. It does not convert public AI-safety alignment into an agreement, concentrated market structure into monopolization, or policy/staff concerns into violation findings.',
    '',
    'The bounded EU layer covers TFEU Articles 101–102, the EU Merger Regulation, the Digital Markets Act, the 2023 Horizontal Cooperation Guidelines, the Commission generative-AI competition policy brief and the joint EC/CMA/DOJ/FTC generative-AI competition statement. Five direct EUR-Lex PDF probes returned HTTP 202 with empty bodies to the GitHub runner; current official EUR-Lex pages were separately rechecked and the runner access limit is preserved.',
    '',
    'The bounded U.S. layer marker-verified Sherman Act §§ 1–2, Clayton Act § 7 and FTC Act § 5 from the current Office of Law Revision Counsel pages. It also verified the nonbinding 2023 Merger Guidelines, the 2014 cybersecurity information-sharing statement, the FTC AI partnerships 6(b) staff report, the December 2024 withdrawal of the 2000 competitor-collaboration guidelines, and the 2026 public inquiry/extension for possible replacement guidance. The inquiry is not final guidance.',
    '',
    'Durable outputs are under `76_COMPETITION/` and `95_RESEARCH/COMPETITION/`. No cartel, monopolization, merger-violation, regulatory-capture or named-firm liability finding was made.',
    ''
]
marker = '### Notebook/source-processing lane\n'
if marker not in ctx:
    raise SystemExit('Notebook lane marker missing')
ctx = ctx.replace(marker, '\n'.join(section_lines) + '\n' + marker, 1)

old = 'R015_LEGAL_CONCLUSION = NOT_ATTEMPTED\nNOTEBOOK_UPLOAD_COUNT = 0'
integrity_lines = [
    'R015_LEGAL_CONCLUSION = NOT_ATTEMPTED',
    f'R016_SOURCE_ACQUISITION_INITIAL_COMMIT = {SOURCE_INITIAL}',
    f'R016_SOURCE_ACQUISITION_FINAL_COMMIT = {SOURCE_FINAL}',
    f'R016_RESEARCH_COMMIT = {RESEARCH_COMMIT}',
    'R016_SOURCE_RECORDS = 17',
    'R016_GITHUB_RUNNER_BODY_MARKER_VERIFIED = 12',
    'R016_EURLEX_GITHUB_RUNNER_HTTP202_EMPTY = 5',
    'R016_EURLEX_OFFICIAL_BROWSER_RECHECKED = 5',
    'R016_US_FEDERAL_STATUTORY_MARKER_VERIFIED = 4',
    'R016_US_2023_MERGER_GUIDELINES = VERIFIED_NONBINDING_GUIDANCE',
    'R016_US_CYBER_INFO_SHARING = VERIFIED_GUIDANCE_ANALOGY_ONLY',
    'R016_US_2000_COLLABORATION_GUIDELINES = WITHDRAWN_DECEMBER_2024',
    'R016_US_2026_REPLACEMENT_GUIDANCE = PUBLIC_INQUIRY_NOT_FINAL_GUIDANCE',
    'R016_FTC_AI_PARTNERSHIP_REPORT = VERIFIED_STAFF_REPORT_NOT_VIOLATION_FINDING',
    'R016_PUBLIC_ALIGNMENT_AS_COLLUSION = NOT_INFERRED',
    'R016_REGULATORY_CAPTURE = NOT_PROVEN',
    'R016_COMPETITION_VIOLATION_FINDINGS = 0',
    'R016_NEW_THIRD_PARTY_BINARIES_VENDORED = 0',
    'R016_NOTEBOOK_UPLOADS = 0',
    'R016_ZIP_OR_WORKFLOW_ARTIFACT_CREATED = NO',
    'R016_LEGAL_CONCLUSION = NOT_ATTEMPTED',
    'NOTEBOOK_UPLOAD_COUNT = 0'
]
if old not in ctx:
    raise SystemExit('R016 integrity insertion marker missing')
ctx = ctx.replace(old, '\n'.join(integrity_lines), 1)
cpath.write_text(ctx, encoding='utf-8')

# Closeout commit pin.
close_path = Path('95_RESEARCH/COMPETITION/AI-LAWS-R016_CLOSEOUT_2026-09-14.md')
close = close_path.read_text(encoding='utf-8')
placeholder = '`PENDING_R016_RESEARCH_COMMIT`'
if placeholder not in close:
    raise SystemExit('R016 closeout placeholder missing')
close = close.replace(placeholder, f'`{RESEARCH_COMMIT}`', 1)
close_path.write_text('\n'.join(line.rstrip() for line in close.splitlines()) + '\n', encoding='utf-8')
