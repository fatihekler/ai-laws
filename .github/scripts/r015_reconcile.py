from pathlib import Path
import csv
import io

RESEARCH_COMMIT = "df24133cfb59e6e5a6f1239119f6c1b23da45bb5"

qpath = Path("90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv")
rows = list(csv.reader(qpath.read_text(encoding="utf-8").splitlines()))
hits = [i for i, row in enumerate(rows) if row and row[0] == "AI-LAWS-R015"]
if len(hits) != 1:
    raise SystemExit(f"R015 queue row count unexpected: {len(hits)}")
rows[hits[0]] = [
    "AI-LAWS-R015",
    "P1",
    "Corporate governance",
    "Board/officer risk oversight, disclosure and organizational responsibility for frontier/high-risk AI",
    "COMPLETE_RESEARCH_BASELINE_L1_L2_CORPORATE_GOVERNANCE_EU_US_DELAWARE_DISCLOSURE_SCOPE_LIMITS_OPEN",
    "NONE",
    "75_CORPORATE_GOVERNANCE/AI-LAWS-R015_CORPORATE_GOVERNANCE_BASELINE_2026-09-14.md; 75_CORPORATE_GOVERNANCE/AI-LAWS-R015_GOVERNANCE_DUTY_MATRIX_2026-09-14.csv; 75_CORPORATE_GOVERNANCE/AI-LAWS-R015_SOURCE_AND_CURRENTNESS_MATRIX_2026-09-14.csv; 30_CASE_LAW/US-DE/US-DE-CASE-001_MARCHAND_V_BARNHILL.yaml; 30_CASE_LAW/US-DE/US-DE-CASE-002_MCDONALDS_OFFICER_OVERSIGHT.yaml; 30_CASE_LAW/US-DE/US-DE-CASE-003_MCDONALDS_DIRECTOR_DISMISSAL.yaml; 95_RESEARCH/CORPORATE_GOVERNANCE/AI-LAWS-R015_CLOSEOUT_2026-09-14.md",
    "bounded EU AI-provider + Delaware board/officer oversight + U.S. issuer disclosure + NIST governance baseline complete; no personal liability, universal AI mission-critical status, dedicated AI committee mandate or global board duty inferred; state/EU-national/sector maps remain open",
]
buf = io.StringIO()
csv.writer(buf, lineterminator="\n").writerows(rows)
qpath.write_text(buf.getvalue(), encoding="utf-8")

cpath = Path("00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md")
ctx = cpath.read_text(encoding="utf-8")

old = " / R014_EVIDENCE_PROCEDURE_BASELINE_COMPLETE_SCOPE_LIMITS_OPEN / R021_COMPLETE"
new = " / R014_EVIDENCE_PROCEDURE_BASELINE_COMPLETE_SCOPE_LIMITS_OPEN / R015_CORPORATE_GOVERNANCE_BASELINE_COMPLETE_SCOPE_LIMITS_OPEN / R021_COMPLETE"
if old not in ctx:
    raise SystemExit("context state marker missing")
ctx = ctx.replace(old, new, 1)

old = "AI-LAWS-R014 = COMPLETE_RESEARCH_BASELINE_L1_L2_EVIDENCE_PROCEDURE_EU_US_FEDERAL_SCOPE_LIMITS_OPEN\nAI-LAWS-R021 = COMPLETE_SUPPORT_INFRASTRUCTURE"
new = "AI-LAWS-R014 = COMPLETE_RESEARCH_BASELINE_L1_L2_EVIDENCE_PROCEDURE_EU_US_FEDERAL_SCOPE_LIMITS_OPEN\nAI-LAWS-R015 = COMPLETE_RESEARCH_BASELINE_L1_L2_CORPORATE_GOVERNANCE_EU_US_DELAWARE_DISCLOSURE_SCOPE_LIMITS_OPEN\nAI-LAWS-R021 = COMPLETE_SUPPORT_INFRASTRUCTURE"
if old not in ctx:
    raise SystemExit("completed-unit marker missing")
ctx = ctx.replace(old, new, 1)

section_lines = [
    "### R015 corporate governance baseline",
    "",
    "```text",
    "AI-LAWS-R015 — CORPORATE GOVERNANCE",
    "STATE = COMPLETE_RESEARCH_BASELINE_L1_L2_CORPORATE_GOVERNANCE_EU_US_DELAWARE_DISCLOSURE_SCOPE_LIMITS_OPEN",
    "NEXT_BOUNDED_UNIT = NONE_AUTO_SELECTED",
    "```",
    "",
    "R015 separates AI-provider/entity organizational duties, Delaware board fiduciary oversight, Delaware officer oversight, U.S. securities risk/governance disclosure, and voluntary NIST operational governance. The controlled EU AI Act verifies Article 17 quality-management-system duties for high-risk AI providers and Article 55 systemic-risk GPAI provider obligations; neither was converted into automatic director/officer personal liability or a universal dedicated board AI-committee mandate.",
    "",
    "Delaware current statutory sources for DGCL §§ 141–142 were verified. Three official Delaware opinions were admitted only as `ANALOGICAL_PRECEDENT`: `Marchand v. Barnhill`, the January 26, 2023 McDonald's officer-oversight opinion, and the March 1, 2023 companion director-dismissal opinion. The cases preserve the demanding good-faith/bad-faith, remit, red-flags, response and procedural-posture distinctions. AI is not automatically `mission-critical`, and survival of a motion to dismiss is not final personal liability.",
    "",
    "For issuer disclosure, Regulation S-K Item 105 was mapped as a material-risk-factor framework, while the official SEC adopting release verifies Item 407(h)'s board risk-oversight disclosure architecture. GitHub-runner eCFR bodies for §§ 229.303 and 229.407 were not admitted as verified section text. NIST AI RMF 1.0 remains voluntary/nonbinding and is currently being revised.",
    "",
    "Durable outputs are under `75_CORPORATE_GOVERNANCE/`, `30_CASE_LAW/US-DE/`, and `95_RESEARCH/CORPORATE_GOVERNANCE/`. No global AI board duty or personal-liability conclusion was inferred.",
    "",
]
marker = "### Notebook/source-processing lane\n"
if marker not in ctx:
    raise SystemExit("notebook lane marker missing")
ctx = ctx.replace(marker, "\n".join(section_lines) + "\n" + marker, 1)

old = "R014_LEGAL_CONCLUSION = NOT_ATTEMPTED\nNOTEBOOK_UPLOAD_COUNT = 0"
integrity_lines = [
    "R014_LEGAL_CONCLUSION = NOT_ATTEMPTED",
    "R015_SOURCE_ACQUISITION_COMMIT = d30a38a029eae1a8ba3080be052ca853f40d0757",
    "R015_SOURCE_CORRECTION_COMMIT = 2aaea3fc1d62511229df8a7fbf7a8498409d7ae8",
    f"R015_RESEARCH_COMMIT = {RESEARCH_COMMIT}",
    "R015_EU_AI_ACT_ART17_QMS = VERIFIED_CURRENT_CONTROLLED_TEXT",
    "R015_EU_AI_ACT_ART55_SYSTEMIC_RISK_GOVERNANCE = VERIFIED_CURRENT_CONTROLLED_TEXT",
    "R015_DE_DGCL_141_142 = VERIFIED_CURRENT_OFFICIAL_SOURCE",
    "R015_DE_CASES_OFFICIAL_FULL_TEXT_VERIFIED = 3",
    "R015_DE_CASES_RELEVANCE_CLASS = ANALOGICAL_PRECEDENT",
    "R015_DE_CASE_PDF_REPOSITORY_SNAPSHOTS = 0",
    "R015_DE_CASE_GITHUB_RUNNER_BODY = HTTP_200_NON_PDF_244_BYTE_HTML",
    "R015_SEC_ITEM105 = VERIFIED_BOUNDED_CURRENT_SOURCE",
    "R015_SEC_ITEM407H_ADOPTION = VERIFIED_OFFICIAL_SEC_SOURCE",
    "R015_SEC_ECFR_229_303_GITHUB_BODY = NOT_SECTION_VERIFIED",
    "R015_SEC_ECFR_229_407_GITHUB_BODY = NOT_SECTION_VERIFIED",
    "R015_NIST_AI_RMF_BINDING_STATE = VOLUNTARY_NONBINDING",
    "R015_NIST_AI_RMF_REVISION_STATE = REVISED_VERSION_IN_PROGRESS",
    "R015_DEDICATED_BOARD_AI_COMMITTEE_MANDATE = NOT_ESTABLISHED",
    "R015_AI_ALWAYS_MISSION_CRITICAL = NOT_INFERRED",
    "R015_PERSONAL_LIABILITY_CONCLUSION = NOT_ATTEMPTED",
    "R015_GLOBAL_AI_BOARD_DUTY = NOT_INFERRED",
    "R015_NOTEBOOK_UPLOADS = 0",
    "R015_ZIP_OR_WORKFLOW_ARTIFACT_CREATED = NO",
    "R015_LEGAL_CONCLUSION = NOT_ATTEMPTED",
    "NOTEBOOK_UPLOAD_COUNT = 0",
]
if old not in ctx:
    raise SystemExit("integrity marker missing")
ctx = ctx.replace(old, "\n".join(integrity_lines), 1)
cpath.write_text(ctx, encoding="utf-8")

close_path = Path("95_RESEARCH/CORPORATE_GOVERNANCE/AI-LAWS-R015_CLOSEOUT_2026-09-14.md")
close = close_path.read_text(encoding="utf-8")
placeholder = "`PENDING_R015_RESEARCH_COMMIT`"
if placeholder not in close:
    raise SystemExit("closeout placeholder missing")
close = close.replace(placeholder, f"`{RESEARCH_COMMIT}`", 1)
close = "\n".join(line.rstrip() for line in close.splitlines()) + "\n"
close_path.write_text(close, encoding="utf-8")
