# AI-LAWS-R002 — Jurisdiction Registry Closeout

**UNIT_ID:** `AI-LAWS-R002`
**DATE:** 2026-09-14
**BASE_HEAD:** `59016d0337a3ccdec746ef73c5b686f42db1cafc`
**REGISTRY_ACQUISITION_INITIAL_COMMIT:** `d4b565ab42b13d1c84168a1eedc2e1a05e13cee1`
**REGISTRY_ACQUISITION_FINAL_COMMIT:** `16ab3623cba3d8f8047c71086f557e3d454cb5f9`
**R002_RESEARCH_COMMIT:** `PENDING_RECONCILIATION`
**STATE:** `COMPLETE_REGISTRY_BASELINE_L1_GLOBAL_COUNTRY_AREA_US_STATE_TERRITORY_MATERIAL_SUBNATIONAL_METHOD`
**LEGAL_ADVICE:** NO
**AUTO_ADVANCE:** NO

## Scope completed

R002 expanded the jurisdiction registry from a seed into a source-backed global coverage baseline while preserving existing research states.

Durable outputs:

- `20_JURISDICTIONS/JURISDICTION_RESEARCH_REGISTRY.csv`
- `20_JURISDICTIONS/R002_JURISDICTION_COVERAGE_METHOD_2026-09-14.md`
- `20_JURISDICTIONS/R002_MATERIAL_SUBNATIONAL_TRIGGER_MATRIX_2026-09-14.csv`
- `20_JURISDICTIONS/R002_SOURCE_ACQUISITION_RESULTS_2026-09-14.csv`
- `20_JURISDICTIONS/R002_REGISTRY_VALIDATION_SUMMARY_2026-09-14.csv`
- `95_RESEARCH/JURISDICTION_REGISTRY/AI-LAWS-R002_CLOSEOUT_2026-09-14.md`

## Verification record

```text
UN_M49_COUNTRY_AREA_ROWS = 247
US_CENSUS_STATE_EQUIVALENT_ROWS = 57
US_NONSTATE_TERRITORY_OR_EQUIVALENT_ROWS = 6
TOTAL_REGISTRY_ROWS = 313
DUPLICATE_JURISDICTION_IDS = 0
SUBSTANTIVE_LAW_FINDINGS_FOR_NEW_ROWS = 0
UN_M49_HTTP = 200
US_CENSUS_HTTP = 200
UN_M49_SHA256 = b9048114f6e7f2abda83bf03d4263c9d7cd1bd7230e3d0461025ee7839a7a1fb
US_CENSUS_SHA256 = bea4e03f71a1fa0045ae732aabad11fa541e5932b071c2369bb0d325e8cba5a0
ZIP_OR_ARTIFACT_CREATED = NO
NOTEBOOK_UPLOADS = 0
```

## Correction applied

The first deterministic merge correctly returned 57 U.S. Census rows but initially classified `US-UM — U.S. Minor Outlying Islands` as `SUBNATIONAL_US_STATE_OR_DISTRICT`. Validation caught the arithmetic mismatch between 57 total rows and the expected state/DC/non-state split. The final pass corrected `US-UM` to `SUBNATIONAL_US_TERRITORY_OR_STATISTICAL_EQUIVALENT` and verified six non-state rows: `AS`, `GU`, `MP`, `PR`, `UM`, `VI`.

No substantive legal conclusion was affected.

## Core boundaries

```text
REGISTRY_PRESENCE != SUBSTANTIVE_LAW_RESEARCHED
UN_M49_COUNTRY_OR_AREA != SOVEREIGNTY_DETERMINATION
CENSUS_STATE_EQUIVALENT != IDENTICAL_LEGAL_STATUS
UNLISTED_SUBNATIONAL != OUT_OF_SCOPE
MATERIAL_SUBNATIONAL_TRIGGER != LEGAL_CLAIM_PROVEN
SOURCE_ENUMERATION != APPLICABLE_LAW
SOURCE_ENUMERATION != FORUM
SOURCE_ENUMERATION != ENFORCEMENT
```

## Preserved state

Existing jurisdiction research states were preserved rather than downgraded by enumeration. This includes the controlled EU/CoE, Türkiye, U.S., China, United Kingdom, Korea, Japan and other previously seeded records, plus R007 state-level states such as Utah and Texas.

R005 and R006 blockers are unchanged. R019 remains `READY_FOR_EXPLICIT_AUTHORIZATION` and was not started.

## R018 dependency effect

R002 now supplies the explicit global jurisdiction universe and material-subnational admission method required by the R018 dependency line. This does **not** auto-start R018 and does not predetermine any forum, governing law, recognition, enforcement, extraterritoriality or cross-border-remedy conclusion.

## Stop

```text
R002_GLOBAL_ENUMERATION = COMPLETE_BASELINE
R002_MATERIAL_SUBNATIONAL_METHOD = ACTIVE
R002_SUBSTANTIVE_LEGAL_ANALYSIS = NOT_ATTEMPTED
R018 = NOT_STARTED
R019 = NOT_STARTED
NEXT_BOUNDED_UNIT = NONE_AUTO_SELECTED
UNKNOWN_PRESERVED = YES
AUTO_ADVANCE = NO
STOP = YES
```
