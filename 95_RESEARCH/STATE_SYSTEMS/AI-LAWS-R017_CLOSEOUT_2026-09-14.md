# AI-LAWS-R017 — State Systems Closeout

**UNIT_ID:** `AI-LAWS-R017`  
**DATE:** 2026-09-14  
**BASE_HEAD:** `64fb024dc837d9b3fc90ea9ed6082de4ba101f74`  
**SOURCE_ACQUISITION_INITIAL_COMMIT:** `6010327390b2dec45a3f3765ec2ce126c07bdfbe`  
**SOURCE_ACQUISITION_FINAL_COMMIT:** `135ad2fbf0be38c193c1e1e6f86b8d956a57439d`  
**R017_RESEARCH_COMMIT:** `PENDING_RECONCILIATION`  
**STATE:** `COMPLETE_RESEARCH_BASELINE_L1_L2_STATE_SYSTEMS_EU_US_OVERSIGHT_IMMUNITY_SCOPE_LIMITS_OPEN`  
**LEGAL_ADVICE:** NO  
**AUTO_ADVANCE:** NO

## Scope completed

R017 established a bounded public-source baseline for AI-related national-security/defence scope exclusions, alternative human-rights layers, U.S. federal executive AI governance, national-security-system definition, sovereign-immunity/judicial-review/remedy architecture, intelligence-community Inspector General oversight and one blocked DoD operational-policy candidate.

It did not investigate classified facts, decide legality of any state system, or infer that exclusion from one AI instrument means exclusion from all law.

## Durable outputs

- `77_STATE_SYSTEMS/AI-LAWS-R017_STATE_SYSTEMS_ACCOUNTABILITY_BASELINE_2026-09-14.md`
- `77_STATE_SYSTEMS/AI-LAWS-R017_ACCOUNTABILITY_GAP_MATRIX_2026-09-14.csv`
- `77_STATE_SYSTEMS/AI-LAWS-R017_SOURCE_AND_CURRENTNESS_MATRIX_2026-09-14.csv`
- `77_STATE_SYSTEMS/source_acquisition/AI-LAWS-R017_SOURCE_ACQUISITION_RESULTS_2026-09-14.csv`
- `95_RESEARCH/STATE_SYSTEMS/AI-LAWS-R017_CLOSEOUT_2026-09-14.md`

## Verification record

```text
R017_SOURCE_RECORDS = 12
R017_BODY_MARKER_VERIFIED = 11
R017_DOD300009_RUNNER_STATE = HTTP_403_BODY_NOT_VERIFIED
R017_AI_ACT_CONTROLLED_SHA256 = 1ccd38d1c78482cf2053b70110115adcc5080700acc8bd7bead8cb3579143ccf
R017_CETS225_CONTROLLED_SHA256 = 1ac6c8a85f55446cdb53697b57c6be3ce8757068043992955eda571e7fe52f23
R017_OMB_M2521_REPOSITORY_SHA256 = 0aab0aa4eaeac969ed93894d3940c5dc9d0b7377048171b164a439e8b9e49813
R017_OMB_M2521_LIVE_SHA256 = 0aab0aa4eaeac969ed93894d3940c5dc9d0b7377048171b164a439e8b9e49813
R017_OMB_M2521_EXACT_LIVE_REPOSITORY_MATCH = YES
R017_ECHR_OFFICIAL_PDF = HTTP_200_MARKERS_VERIFIED
R017_44_USC_3552 = HTTP_200_MARKERS_VERIFIED
R017_5_USC_702 = HTTP_200_MARKERS_VERIFIED
R017_28_USC_1346B = HTTP_200_MARKERS_VERIFIED
R017_28_USC_2674 = HTTP_200_MARKERS_VERIFIED
R017_28_USC_2680 = HTTP_200_MARKERS_VERIFIED
R017_50_USC_3033 = HTTP_200_MARKERS_VERIFIED
R017_NOTEBOOK_UPLOADS = 0
R017_NEW_THIRD_PARTY_BINARIES_VENDORED = 0
R017_ZIP_OR_WORKFLOW_ARTIFACT_CREATED = NO
```

## Core boundaries

```text
EXEMPT_FROM_AI_ACT != EXEMPT_FROM_ALL_LAW
NATIONAL_SECURITY_LABEL != CLASSIFIED_FACT_PROVEN
CLASSIFIED_OR_SECRET != UNREGULATED
SOVEREIGN_IMMUNITY != NO_DUTY
WAIVER_OF_IMMUNITY != AUTOMATIC_REMEDY
APA_702 != REVIEWABILITY_OR_SUCCESS_PROVEN
FTCA_WAIVER != CLAIM_WITHIN_SCOPE_PROVEN
FTCA_EXCEPTION != MERITS_DECISION
INSPECTOR_GENERAL_OVERSIGHT != PRIVATE_RIGHT_OF_ACTION
TREATY_TEXT != TREATY_IN_FORCE
PUBLIC_SOURCE_GAP != ACTUAL_OVERSIGHT_GAP
RUNNER_ACCESS_FAILURE != SOURCE_ABSENCE
```

## Material results

- The current controlled AI Act Article 2 text contains national-security/military/defence scope boundaries. R017 records an AI-Act scope result only and does not infer general immunity or absence of other law.
- CETS 225 Article 3 national-security/national-defence structure was verified from the controlled treaty text, but R004's entry-into-force gate remains controlling; no current domestic treaty obligation is inferred.
- The current official ECHR PDF verifies a selected Article 8 privacy/national-security limitation layer and Article 13 remedy layer, subject to jurisdiction, admissibility and merits analysis.
- OMB M-25-21 was freshly rechecked at the live official White House PDF and exactly matches the repository copy. Its verified scope is directed to Executive Branch departments/agencies including independent regulatory agencies. R017 did not verify the initially hypothesized distinct `44 U.S.C. §3552 national-security-system exclusion` inside M-25-21 and therefore does not state one.
- 44 U.S.C. §3552 supplies the national-security-system definition layer; it does not itself create an AI exemption or remedy.
- 5 U.S.C. §702 supplies a nonmoney-relief/judicial-review sovereign-immunity layer, while preserving other review limitations.
- 28 U.S.C. §§1346(b), 2674 and 2680 establish a bounded FTCA jurisdiction/liability/exception architecture. R017 does not complete administrative exhaustion, case law or military-specific doctrine.
- 50 U.S.C. §3033 verifies an Intelligence Community Inspector General statutory oversight layer. Oversight is not converted into a private cause of action or public-transparency guarantee.
- The official DoD Directive 3000.09 candidate URL returned HTTP 403 to the GitHub-hosted runner. No detailed directive-body finding is admitted.

## Preserved blockers and UNKNOWNs

- R005 remains unchanged and blocked at live Türkiye official-source recheck.
- R006 remains blocked by official decision-source availability.
- R019 remains `READY_FOR_EXPLICIT_AUTHORIZATION` and was not started.
- Concrete AI Act national-security/military/defence classification remains fact-specific and unattempted.
- EU Member-State national-security, constitutional and procedural remedies remain open.
- ECHR secret-surveillance/national-security case law remains unresearched in R017.
- APA reviewability, state-secrets/classified-information procedure and national-security case law remain open.
- FTCA administrative exhaustion, military doctrines, contractors and claim-specific exceptions remain open.
- DoD Directive 3000.09 current body remains runner-blocked.
- Actual classified AI deployments, capabilities, incidents, targets and controls remain `UNKNOWN_NOT_INFERRED`.
- Other jurisdictions' sovereign-immunity and state-system regimes remain open.

## Source-acquisition discipline

No third-party source binary was committed solely because it was downloadable. Official web/PDF sources were downloaded transiently in GitHub Actions for HTTP/body/hash/marker verification. Existing controlled repository PDFs were read in place. Only the acquisition CSV and durable research/control records are retained.

## Stop

```text
R017_CLASSIFIED_FACT_FINDINGS = 0
R017_CONCRETE_STATE_AI_LEGALITY_FINDINGS = 0
R017_SOVEREIGN_IMMUNITY_CASE_OUTCOME = NOT_ATTEMPTED
R017_LEGAL_CONCLUSION = NOT_ATTEMPTED
NEXT_BOUNDED_UNIT = NONE_AUTO_SELECTED
UNKNOWN_PRESERVED = YES
AUTO_ADVANCE = NO
STOP = YES
```