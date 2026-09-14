# AI-LAWS-R012 — Comparative Liability Closeout

**UNIT_ID:** `AI-LAWS-R012`  
**DATE:** 2026-09-14  
**BASE_HEAD:** `646a60fe9e05f81a53543c5b862dee3931aede37`  
**R012_RESEARCH_COMMIT:** `PENDING_R012_RESEARCH_COMMIT`  
**STATE:** `COMPLETE_RESEARCH_BASELINE_L1_L2_LIABILITY_MODEL_JURISDICTION_DEPENDENCIES_OPEN`  
**LEGAL_ADVICE:** NO  
**AUTO_ADVANCE:** NO

## Scope completed

R012 produced a bounded EU/US comparative liability baseline using controlled repository sources plus fresh GitHub-runner source probes. It did not attempt a global liability rule, legal advice, or concrete actor-liability determination.

## Durable outputs

- `40_LIABILITY/AI-LAWS-R012_COMPARATIVE_LIABILITY_BASELINE_2026-09-14.md`
- `40_LIABILITY/AI-LAWS-R012_ACTOR_LIABILITY_CHAIN_MATRIX_2026-09-14.csv`
- `40_LIABILITY/AI-LAWS-R012_SOURCE_AND_CURRENTNESS_MATRIX_2026-09-14.csv`
- `95_RESEARCH/LIABILITY/AI-LAWS-R012_CLOSEOUT_2026-09-14.md`
- reconciled `90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv`
- reconciled `00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md`

## Verification record

```text
SOURCE_RECORDS_RECHECKED = 8
EU_EXACT_OFFICIAL_REPOSITORY_SNAPSHOTS_USED = EU-001; EU-003; EU-005
EU_PDF_LIVE_PROBE = HTTP_202_EMPTY_BODY
EU_REPOSITORY_SNAPSHOT_EXTRACTION = SUCCESS
US003_FRESH_ACCESS = HTTP_200_PDF_EXACT_KNOWN_HASH
US004_FRESH_ACCESS = HTTP_200_PDF_EXACT_KNOWN_HASH
US007_FRESH_ACCESS = HTTP_200_OFFICIAL_PAGE
US008_FRESH_ACCESS = HTTP_200_OFFICIAL_PAGE
US009_S101_FRESH_ACCESS = HTTP_200_PDF
NOTEBOOK_UPLOADS = 0
NEW_SOURCE_BINARIES = 0
DERIVED_MARKDOWN_CREATED = 0
ZIP_OR_ARTIFACT_CREATED = NO
```

The live EUR-Lex `202 + empty body` result is preserved as an access/currentness limitation and is not interpreted as a source change. Same-day exact official repository snapshots remain the controlled source bodies for the bounded extraction, subject to future refresh.

## Core findings with limits

```text
EU_PLD_SOFTWARE_AS_PRODUCT = VERIFIED_PRIMARY_TEXT
EU_PLD_ACTOR_DEFECT_CAUSATION_EVIDENCE_REMEDY_ARCHITECTURE = VERIFIED_PRIMARY_TEXT
EU_PLD_TRANSPOSITION_DEADLINE = 2026-12-09
EU_PLD_MEMBER_STATE_TRANSPOSITION_MAP = NOT_ATTEMPTED
GDPR_ARTICLE_82_COMPENSATION_ROUTE = VERIFIED_PRIMARY_TEXT
AI_ACT_ROLE_DEFINITIONS = VERIFIED_CURRENT_CONTROLLED_TEXT
AI_ACT_VIOLATION_EQUALS_CIVIL_LIABILITY = NO_INFERENCE
US_GENERAL_AI_TORT_RULE = NOT_ESTABLISHED_BY_CONTROLLED_R012_SET
GLOBAL_AI_LIABILITY_RULE = NOT_INFERRED
LEGAL_CONCLUSION = NOT_ATTEMPTED
```

## Preserved blockers and UNKNOWNs

- `R005` remains `PARTIAL_SOURCE_PIN_REPOSITORY_PDF_CONTENT_VERIFIED_OFFICIAL_LIVE_RECHECK_BLOCKED`.
- `R006` remains `BLOCKED_BY_OFFICIAL_SOURCE_AVAILABILITY`.
- `R019` remains `READY_FOR_EXPLICIT_AUTHORIZATION` and was not started.
- EU Member-State PLD transposition/current national implementation remains open.
- U.S. state/private tort, product, privacy, consumer, and case-law liability remains open beyond the controlled R012 set.
- concrete actor, duty, breach/defect, causation, damage, defence, evidence, and remedy remain fact- and jurisdiction-specific.

## Drift record

During R012, commit `3173ad70922bcc265a18d850e42193ea5eecfcaf` was added after a fresh-read. Comparison against the preceding R012 helper state showed exactly one non-overlapping added path: `86_NOTEBOOKLM/NOTEBOOKLM_DOWNLOAD_AND_UPLOAD_LIST-old.md`. It did not touch R012 target research/control paths. The current GitHub state was therefore retained rather than overwritten.

## Helper discipline

Temporary GitHub Actions probe/extraction helpers are removed by the final reconciliation/cleanup step. No workflow artifact was produced.

## Stop

```text
NEXT_BOUNDED_UNIT = NONE_AUTO_SELECTED
UNKNOWN_PRESERVED = YES
AUTO_ADVANCE = NO
STOP = YES
```
