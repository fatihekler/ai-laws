# AI-LAWS-R018 — Cross-Border Closeout

**UNIT_ID:** `AI-LAWS-R018`
**DATE:** 2026-09-14
**BASE_HEAD:** `9a4d51a19f3e027a1fa7aeda42fd0a1d6022d6e1`
**SOURCE_ACQUISITION_INITIAL_COMMIT:** `0ce5ecab186efce9b8d272244948ce9aeda35371`
**SOURCE_ACQUISITION_FINAL_COMMIT:** `694feb7078b56bb70a148fcbd48373d859e66f59`
**R018_RESEARCH_COMMIT:** `TO_BE_RECONCILED`
**STATE:** `COMPLETE_RESEARCH_BASELINE_L1_L2_CROSS_BORDER_US_FEDERAL_EU_SCOPE_PIL_BODY_ACCESS_LIMITS_OPEN`
**LEGAL_ADVICE:** NO
**AUTO_ADVANCE:** NO

## Scope completed

R018 created a bounded cross-border analysis architecture separating territorial regulatory scope, forum/personal jurisdiction, service, venue, applicable law, evidence cooperation, judgment and recognition/enforcement.

Durable outputs:

- `78_CROSS_BORDER/AI-LAWS-R018_CROSS_BORDER_JURISDICTION_APPLICABLE_LAW_ENFORCEMENT_BASELINE_2026-09-14.md`
- `78_CROSS_BORDER/AI-LAWS-R018_CONFLICT_OF_LAWS_AND_ENFORCEMENT_MATRIX_2026-09-14.csv`
- `78_CROSS_BORDER/AI-LAWS-R018_SOURCE_AND_CURRENTNESS_MATRIX_2026-09-14.csv`
- `78_CROSS_BORDER/source_acquisition/AI-LAWS-R018_SOURCE_ACQUISITION_RESULTS_2026-09-14.csv`
- `95_RESEARCH/CROSS_BORDER/AI-LAWS-R018_CLOSEOUT_2026-09-14.md`

## Verification record

```text
R018_SOURCE_RECORDS = 11
R018_BODY_MARKER_VERIFIED_DIRECT_OR_CONTROLLED = 4
R018_US_FRCP = HTTP_200_BODY_MARKERS_VERIFIED
R018_US_1391 = HTTP_200_BODY_MARKERS_VERIFIED
R018_US_1782 = HTTP_200_BODY_MARKERS_VERIFIED
R018_GDPR_CONTROLLED = BODY_MARKERS_VERIFIED
R018_AI_ACT = REUSE_R003_PRIOR_VERIFIED_SCOPE_MAP
R018_BRUSSELS1_RUNNER = HTTP_202_CHALLENGE_BODY_NOT_VERIFIED
R018_ROME1_RUNNER = HTTP_202_CHALLENGE_BODY_NOT_VERIFIED
R018_ROME2_RUNNER = HTTP_202_CHALLENGE_BODY_NOT_VERIFIED
R018_EJUSTICE_FALLBACK = HTTP_403_BODY_NOT_VERIFIED
ZIP_OR_ARTIFACT_CREATED = NO
NOTEBOOK_UPLOADS = 0
```

## Material results

- GDPR territorial-scope concepts were verified from the controlled primary PDF; territorial scope is not treated as forum or applicable-law selection.
- AI Act third-country/Union-use scope is reused only from R003's controlled verified Article 2 map; R018 did not independently re-admit the body.
- Current FRCP Rule 4 source markers verify the service/personal-jurisdiction procedural interface, including foreign service and territorial limits of effective service. Constitutional due-process and state long-arm analysis remain open.
- 28 U.S.C. §1391 current body was marker-verified as federal venue law. Venue is not personal jurisdiction.
- 28 U.S.C. §1782 current body was marker-verified as an evidence-assistance statute. Full case-law scope and concrete entitlement remain open.
- Brussels I bis, Rome I and Rome II official instrument identities were targeted, but all official body variants returned EUR-Lex challenge bodies to the runner. No article-level legal proposition from those three instruments is admitted by R018.
- U.S. foreign-country judgment recognition remains an open state-law/treaty/case-law dependency; no universal federal recognition rule is inferred.

## Core boundaries

```text
EXTRATERRITORIAL_SCOPE != FORUM
FORUM != APPLICABLE_LAW
SERVICE != PERSONAL_JURISDICTION_PROVEN
VENUE != PERSONAL_JURISDICTION
APPLICABLE_LAW != LIABILITY
EVIDENCE_ASSISTANCE != JUDGMENT_RECOGNITION
JUDGMENT != AUTOMATIC_FOREIGN_ENFORCEMENT
OFFICIAL_INSTRUMENT_IDENTITY != ARTICLE_TEXT_VERIFIED
RUNNER_ACCESS_FAILURE != SOURCE_ABSENCE
```

## Preserved blockers and UNKNOWNs

- R005 remains unchanged and blocked at live Türkiye official-source recheck.
- R006 remains blocked by official decision-source availability.
- R019 remains `READY_FOR_EXPLICIT_AUTHORIZATION` and was not started.
- Brussels I bis, Rome I and Rome II exact primary bodies remain GitHub-runner blocked in R018.
- EU/Member-State jurisdiction, conflict-of-laws and enforcement case law remain open.
- U.S. constitutional personal-jurisdiction case law and state long-arm statutes remain open.
- U.S. state foreign-country judgment recognition law remains open.
- HCCH service/evidence/choice-of-court/judgments participation and applicability remain open.
- Arbitration, forum-selection, public-law cooperation and concrete incident facts remain open.

## Stop

```text
R018_GLOBAL_FORUM_RULE = NOT_INFERRED
R018_GLOBAL_APPLICABLE_LAW_RULE = NOT_INFERRED
R018_GLOBAL_ENFORCEMENT_RULE = NOT_INFERRED
R018_LEGAL_CONCLUSION = NOT_ATTEMPTED
NEXT_BOUNDED_UNIT = NONE_AUTO_SELECTED
UNKNOWN_PRESERVED = YES
AUTO_ADVANCE = NO
STOP = YES
```
