# AI-LAWS / HSA — NotebookLM Output Artifact Contract

**DOCUMENT_ID:** AI-LAWS-HSA-NBLM-OUTPUT-CONTRACT-2026-09-15
**STATE:** PROPOSAL / NONCANONICAL RESEARCH OUTPUT CONTRACT

## 1. Principle

Preserve raw Notebook output first. Normalize second. Verify against original source third. Promote only through destination-local governance.

```text
RAW_NOTEBOOK_OUTPUT
!= NORMALIZED_RECORD
!= VERIFIED_FINDING
!= ACCEPTED_REQUIREMENT
```

## 2. Run identity

Each execution receives:

```text
RUN_ID = RUN-YYYYMMDD-###
NOTEBOOK_PACK = NB01..NB09
RUN_MODE = SINGLE_SOURCE | PACK | CROSS_PACK
SELECTED_SOURCE_IDS
PROMPT_VERSION
RUN_DATE
OPERATOR
```

## 3. Raw storage

ChatGPT Work stores raw Notebook exports under the HSA Drive `02_NOTEBOOK_OUTPUTS_RAW/` area without rewriting the source text.

Recommended filename:

```text
<RUN_ID>__<PACK>__<MODE>__RAW.md
```

If one source was selected:

```text
<RUN_ID>__<PACK>__<SOURCE_ID>__RAW.md
```

## 4. Normalized files

### `NBLM_RUN_MANIFEST.csv`
Fields:
`run_id,run_date,notebook_pack,run_mode,selected_source_ids,prompt_version,operator,raw_output_path,normalization_state,verification_state,notes`

### `NBLM_SOURCE_IDENTITY_AND_AUTHORITY_MATRIX.csv`
Fields:
`record_id,run_id,qualified_source_id,source_id,title,institution,jurisdiction,authority_class,binding_state,document_number,publication_date,effective_date,version_date,currentness_state,source_locator,identity_confidence,limitations,primary_source_recheck_required`

### `NBLM_ACTOR_DUTY_RIGHTS_MATRIX.csv`
Fields:
`record_id,run_id,qualified_source_id,actor,system_or_conduct,right_or_interest,duty_or_prohibition,condition,exception,remedy_or_enforcement,source_locator,evidence_state,unknown,limitations,promotion_state,destination_repo`

### `NBLM_HSA_THREAT_SOURCE_CROSSWALK.csv`
Fields:
`record_id,run_id,qualified_source_id,threat_id,relationship,direct_or_analogical,source_locator,known,unknown,limitations,review_owner`

`direct_or_analogical` allowed values:
`DIRECT_EXPLICIT | ANALOGICAL | CONTEXT_ONLY | NO_EXPLICIT_SUPPORT_FOUND`.

### `NBLM_EVIDENCE_REQUIREMENT_MATRIX.csv`
Fields:
`record_id,run_id,qualified_source_id,actor,duty_or_issue,evidence_needed,evidence_holder,integrity_requirement,retention_or_timing_issue,source_locator,unknown,legal_review_required`

### `NBLM_EXCEPTION_DEFENCE_MATRIX.csv`
Fields:
`record_id,run_id,qualified_source_id,actor,duty_or_claim,exception_or_defence,conditions,source_locator,materiality,unknown`

### `NBLM_CONFLICT_UNKNOWN_REGISTER.csv`
Fields:
`item_id,run_id,type,qualified_source_ids,description,materiality,blocks_legal_conclusion,blocks_requirement_promotion,resolution_evidence_needed,owner,status`

Use HSA `CON-######` / `UNK-######` only after Engineering OS/HSA coordination admits the normalized item. Raw Notebook output does not self-assign final program IDs.

### `NBLM_CASE_CANDIDATE_MATRIX.csv`
Fields:
`record_id,run_id,case_source_id,official_fulltext_state,court_or_forum,docket,date,actor,duty,possible_breach,causation,damage,standing_or_forum,remedy,evidence_gaps,analogy_limit,admission_state`

Admission rule:
`NO_OFFICIAL_FULL_TEXT => NO_VERIFIED_CASE_CORPUS_ENTRY`.

### `NBLM_CONTROL_TEST_CANDIDATES.csv`
Fields:
`record_id,run_id,source_finding_ref,threat_id,control_candidate,control_owner,test_candidate,expected_evidence,stop_threshold,destination_repo,promotion_state`

Every row begins as `CANDIDATE`; NotebookLM cannot mark implementation/effectiveness.

## 5. Pack narrative synthesis

For each pack create:

```text
NBLM_PACK_SYNTHESIS_<NBxx>.md
```

Required sections:
1. Sources selected / excluded / held.
2. Authority hierarchy.
3. Main source-supported findings.
4. Actor/duty/right matrix summary.
5. HSA threat coverage.
6. Evidence requirements.
7. Exceptions/defences.
8. Conflicts.
9. Unknowns.
10. Candidate controls/tests.
11. Original-source rechecks required.
12. Questions for destination repositories.

## 6. Cross-pack synthesis

`NBLM_CROSS_PACK_GAP_SYNTHESIS.md` must contain only cross-source/cross-jurisdiction comparison and research gaps. It may not replace local legal analysis.

## 7. Promotion rules

Allowed initial states:
- `QUESTION`
- `SUPPORTING_RESEARCH`
- `FINDING_CANDIDATE`
- `HOLD`

Prohibited Notebook-assigned terminal states:
- `VERIFIED_FINDING`
- `ACCEPTED_REQUIREMENT`
- `PASS`
- `LEGAL_VIOLATION`
- `LIABILITY_ESTABLISHED`

## 8. Data quality gates

A normalized record is invalid if any mandatory material claim lacks:
- source ID;
- source locator;
- authority class;
- jurisdiction;
- date/currentness state where relevant;
- known/unknown separation;
- limitations.

Do not repair missing Notebook evidence by model inference. Mark UNKNOWN and route for research.
