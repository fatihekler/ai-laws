# AI-LAWS-R015 — Corporate Governance Closeout

**UNIT_ID:** `AI-LAWS-R015`  
**DATE:** 2026-09-14  
**BASE_HEAD:** `230fc43da2e6dab081ead28482303d6e91fcb8fb`  
**SOURCE_ACQUISITION_COMMIT:** `d30a38a029eae1a8ba3080be052ca853f40d0757`  
**SOURCE_CORRECTION_COMMIT:** `2aaea3fc1d62511229df8a7fbf7a8498409d7ae8`  
**R015_RESEARCH_COMMIT:** `PENDING_R015_RESEARCH_COMMIT`  
**STATE:** `COMPLETE_RESEARCH_BASELINE_L1_L2_CORPORATE_GOVERNANCE_EU_US_DELAWARE_DISCLOSURE_SCOPE_LIMITS_OPEN`  
**LEGAL_ADVICE:** NO  
**AUTO_ADVANCE:** NO

## Scope completed

R015 established a bounded corporate-governance baseline separating AI-provider organizational duties, Delaware board/officer oversight doctrine, U.S. issuer risk/governance disclosure, and voluntary NIST operational governance. It did not infer personal director/officer liability from an entity-level AI obligation or from the mere existence of an AI incident.

## Durable outputs

- `75_CORPORATE_GOVERNANCE/AI-LAWS-R015_CORPORATE_GOVERNANCE_BASELINE_2026-09-14.md`
- `75_CORPORATE_GOVERNANCE/AI-LAWS-R015_GOVERNANCE_DUTY_MATRIX_2026-09-14.csv`
- `75_CORPORATE_GOVERNANCE/AI-LAWS-R015_SOURCE_AND_CURRENTNESS_MATRIX_2026-09-14.csv`
- `75_CORPORATE_GOVERNANCE/source_acquisition/AI-LAWS-R015_SOURCE_ACQUISITION_RESULTS_2026-09-14.csv`
- `30_CASE_LAW/US-DE/US-DE-CASE-001_MARCHAND_V_BARNHILL.yaml`
- `30_CASE_LAW/US-DE/US-DE-CASE-002_MCDONALDS_OFFICER_OVERSIGHT.yaml`
- `30_CASE_LAW/US-DE/US-DE-CASE-003_MCDONALDS_DIRECTOR_DISMISSAL.yaml`
- `95_RESEARCH/CORPORATE_GOVERNANCE/AI-LAWS-R015_CLOSEOUT_2026-09-14.md`

## Verification record

```text
EU_AI_ACT_EXISTING_EXACT_OFFICIAL_SNAPSHOT = VERIFIED
EU_AI_ACT_ART17_QUALITY_MANAGEMENT = VERIFIED
EU_AI_ACT_ART55_SYSTEMIC_RISK_PROVIDER_GOVERNANCE = VERIFIED
DE_DGCL_141_142_CURRENT_OFFICIAL_HTML = VERIFIED_HTTP_200
DE_TITLE8_OFFICIAL_PDF_TRANSIENT_BODY = VERIFIED_HTTP_200_APPLICATION_PDF
DE_TITLE8_PDF_VENDORED = NO
DE_MARCHAND_OFFICIAL_FULL_TEXT = VERIFIED_INDEPENDENT_OFFICIAL_SOURCE
DE_MCDONALDS_OFFICER_OFFICIAL_FULL_TEXT = VERIFIED_INDEPENDENT_OFFICIAL_SOURCE
DE_MCDONALDS_DIRECTOR_OFFICIAL_FULL_TEXT = VERIFIED_INDEPENDENT_OFFICIAL_SOURCE
DE_CASE_PDF_GITHUB_RUNNER = HTTP_200_NON_PDF_244_BYTE_HTML
DE_CASE_PDF_REPOSITORY_SNAPSHOTS = 0
SEC_ITEM105_CURRENT_OFFICIAL_TEXT = VERIFIED_BOUNDED
SEC_ITEM407H_ADOPTING_RELEASE = VERIFIED_OFFICIAL_SEC_SOURCE
SEC_ECFR_229_303_GITHUB_BODY = NOT_SECTION_VERIFIED
SEC_ECFR_229_407_GITHUB_BODY = NOT_SECTION_VERIFIED
SEC_33_9089_GITHUB_RUNNER = HTTP_403
SEC_AI_WASHING_GITHUB_RUNNER = HTTP_403
NIST_AI_RMF_1_0_OFFICIAL_PAGE = VERIFIED_HTTP_200
NIST_AI_RMF_BINDING_STATE = VOLUNTARY_NONBINDING
NIST_AI_RMF_REVISION_STATE = REVISED_VERSION_IN_PROGRESS
NOTEBOOK_UPLOADS = 0
ZIP_OR_ARTIFACT_CREATED = NO
```

## Core legal boundaries

```text
PROVIDER_OR_ENTITY_AI_DUTY != BOARD_FIDUCIARY_BREACH
BOARD_OVERSIGHT_DUTY != OFFICER_OVERSIGHT_DUTY
OFFICER_REMIT_IS_CONTEXT_SPECIFIC
AI_RISK != AUTOMATIC_MISSION_CRITICAL_RISK
AI_INCIDENT != AUTOMATIC_CAREMARK_BREACH
PLEADING_SURVIVAL != FINAL_PERSONAL_LIABILITY
RISK_DISCLOSURE_RULE != UNIVERSAL_AI_DISCLOSURE
NIST_RMF != BINDING_FIDUCIARY_LAW
DEDICATED_BOARD_AI_COMMITTEE_MANDATE = NOT_ESTABLISHED
GLOBAL_AI_BOARD_DUTY = NOT_INFERRED
PERSONAL_LIABILITY_CONCLUSION = NOT_ATTEMPTED
```

## Preserved blockers and UNKNOWNs

- R005 remains blocked on live official Türkiye currentness/exact-byte recheck.
- R006 remains blocked by official Türkiye decision-source availability.
- R019 remains `READY_FOR_EXPLICIT_AUTHORIZATION` and was not started.
- No exhaustive U.S. state corporate-governance survey was attempted.
- No EU Member-State director/officer-duty map was attempted.
- No sector-specific governance-duty map was attempted.
- Later treatment of the three Delaware opinions was not exhaustively researched.
- Exact current eCFR body identity for §§ 229.303 and 229.407 was not established in the GitHub-runner lane.
- Materiality of any concrete AI risk/disclosure remains issuer- and fact-specific.
- Whether a specific company's AI use is mission-critical remains fact-specific.
- No concrete director/officer breach, causation, damage or remedy determination was attempted.

## Source-acquisition anomaly discipline

The GitHub-hosted runner returned `HTTP 200` but a short HTML body for each tested Delaware Courts opinion-download URL. This was preserved as an access/body-type blocker and not converted into a `NO_CASE` result. Independent official-source retrieval verified the full opinions. No false PDF snapshot was created.

The GitHub-runner eCFR probes initially recorded HTTP success without validating section body identity. R015 corrected the acquisition CSV before substantive closeout; HTTP status alone is not treated as legal-text verification.

## Stop

```text
NEXT_BOUNDED_UNIT = NONE_AUTO_SELECTED
UNKNOWN_PRESERVED = YES
AUTO_ADVANCE = NO
STOP = YES
```
