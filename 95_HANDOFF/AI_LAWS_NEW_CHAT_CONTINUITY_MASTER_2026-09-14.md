# AI-LAWS — NEW CHAT CONTINUITY MASTER

**DOCUMENT_ID:** `AI-LAWS-NEW-CHAT-CONTINUITY-2026-09-14`
**STATE:** CURRENT_HANDOFF_MASTER
**DATE:** 2026-09-14
**REPOSITORY:** `fatihekler/ai-laws`
**BRANCH:** `main`
**LEGAL_ADVICE:** NO
**MODEL_OUTPUT_CANONICAL:** NO
**NOTEBOOK_OUTPUT_CANONICAL:** NO
**AUTO_ADVANCE:** NO

## 1. Purpose

This file is the durable continuity master for opening a new ChatGPT conversation for the same `ai-laws` project without losing the current repository context.

The new chat must reconstruct state from current GitHub, not from model memory, prior chat summaries, another repository, NotebookLM, Grok, YargıGPT, Notion or a downloaded chat export.

A downloaded copy of the prior chat may be supplied as supplemental history, but it never overrides current GitHub state.

```text
CURRENT_GITHUB_STATE
>
CURRENT_CONTROL_POINTERS_AND_QUEUE
>
CURRENT_DATED_HANDOFF
>
CHAT_EXPORT
>
MODEL_MEMORY
```

## 2. Handoff baseline

The handoff package was prepared after the R011 cleanup state:

```text
HANDOFF_BASE_HEAD = 4e23cbfa8448f3316ab44f82c809ccf448bdd7aa
HANDOFF_BASE_TREE = dd85468d005a5bf7cf7addb282719e712ef811a8
HANDOFF_BASE_COMMIT = chore(r011): remove temporary human-sovereignty workflows
```

This is a historical baseline only. The new chat must fresh-read the actual current `main` HEAD/TREE because the continuity package itself creates a later commit.

## 3. Durable project state at handoff

Completed substantive/support units relevant to continuity:

```text
R001 = COMPLETE_SUPPORTING_RESEARCH_IMPORT
R003 = COMPLETE_RESEARCH_BASELINE_L1_L2
R004 = COMPLETE_RESEARCH_BASELINE_L1_L2
R007 = COMPLETE_RESEARCH_ARCHITECTURE_L1_STATE_LAW_CONTENT_OPEN
R008 = COMPLETE_RESEARCH_BASELINE_L1_PRIMARY_SOURCE_MAP
R009 = COMPLETE_RESEARCH_BASELINE_L1_L2_SECTORAL_MAP_CURRENTNESS_OPEN
R010 = COMPLETE_RESEARCH_BASELINE_L1_L2_CURRENTNESS_OPEN
R011 = COMPLETE_RESEARCH_BASELINE_L1_L2_RIGHTS_MAP_SCOPE_LIMITS_OPEN
R021-R023 = COMPLETE_SUPPORT_INFRASTRUCTURE
R024-R033 = COMPLETE_SUPPORT_SOURCE_VALIDATION / SOURCE_PROCESSING UNITS AS RECORDED IN QUEUE
```

Open/blocker states that must be preserved:

```text
R002 = READY_RESEARCH
R005 = PARTIAL_SOURCE_PIN_REPOSITORY_PDF_CONTENT_VERIFIED_OFFICIAL_LIVE_RECHECK_BLOCKED
R006 = BLOCKED_BY_OFFICIAL_SOURCE_AVAILABILITY
R012 = READY_RESEARCH
R013-R018 = READY_RESEARCH subject to dependencies
R019 = READY_FOR_EXPLICIT_AUTHORIZATION
R020 = READY_AFTER_LEGAL_VERIFICATION
```

No open state may be silently converted into COMPLETE.

## 4. R011 exact handoff state

R011 is complete at its bounded L1/L2 comparative-rights baseline, not globally exhaustive.

Durable outputs:

- `50_RIGHTS/AI-LAWS-R011_HUMAN_SOVEREIGNTY_COMPARATIVE_LEGAL_MAP_2026-09-14.md`
- `50_RIGHTS/AI-LAWS-R011_HUMAN_SOVEREIGNTY_RIGHTS_MATRIX_2026-09-14.csv`
- `50_RIGHTS/AI-LAWS-R011_SOURCE_AUTHORITY_AND_SCOPE_MATRIX_2026-09-14.csv`
- `95_RESEARCH/RIGHTS/AI-LAWS-R011_CLOSEOUT_2026-09-14.md`

Key R011 controls:

```text
R011_CONTROLLED_SOURCE_RECORDS = 8
R011_EU_BINDING_PRIMARY_SOURCES = 3
R011_CHILE_BINDING_PRIMARY_SOURCE_ANCHORS = 1
R011_UNESCO_SOFT_LAW_SOURCES = 2
R011_CL002_CASE_LAW_ADMISSION = BLOCKED
R011_UNIVERSAL_COGNITIVE_LIBERTY_RIGHT = NOT_INFERRED
R011_NOTEBOOK_UPLOADS = 0
R011_LIABILITY_CONCLUSION = NOT_ATTEMPTED
AUTO_ADVANCE = NO
```

Do not reopen or broaden R011 merely because a new chat begins.

## 5. Current next-unit discipline

The queue is authoritative. After R011, the primary sequential candidate is:

```text
AI-LAWS-R012 — Comparative liability
STATE = READY_RESEARCH
```

However `R002` and other READY items also remain open. Therefore the new chat must:

1. fresh-read `90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv`;
2. read `00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md`;
3. select at most one bounded unit only after the user explicitly authorizes continuation;
4. never auto-start R012 merely because this master names it as the primary sequential candidate.

## 6. Mandatory source-of-truth rules

```text
CURRENT_AUTHENTIC_PRIMARY_LEGAL_SOURCE / COURT / TREATY / REGULATOR
>
CURRENT_AI_LAWS_GITHUB_STATE_AND_VERIFIED_SOURCE_RECORDS
>
CURRENT_VERIFIED_SECONDARY_LEGAL_SOURCE
>
CURRENT_VERIFIED_INCIDENT_EVIDENCE
>
CURRENT_CROSS_REPO_EVIDENCE_OR_PROPOSAL
>
GROK / CHATGPT / NOTEBOOKLM / YARGIGPT OUTPUT
>
CHAT MEMORY
```

Mandatory non-equivalence:

```text
MODEL_OUTPUT != LEGAL_AUTHORITY
MULTIPLE_MODELS_AGREE != FACT_PROVEN
NOTEBOOK_OUTPUT != LEGAL_AUTHORITY
YARGIGPT_OUTPUT != COURT_DECISION
SEARCH_FAILURE != NO_CASE
ALLEGATION != VIOLATION
INCIDENT != LIABILITY
HARM != AUTOMATIC_CAUSATION
PUBLIC_KNOWLEDGE != ACTOR_SPECIFIC_LEGAL_KNOWLEDGE
ANALOGICAL_PRECEDENT != DIRECT_AI_PRECEDENT
POLICY_PROPOSAL != CURRENT_LAW
SOFT_LAW != BINDING_LAW
STANDARD != STATUTE
GUIDANCE != COURT_HOLDING
UNKNOWN != NO_RISK
NO_PRECEDENT_FOUND != NO_RIGHT
RESEARCH_FINDING != LEGAL_CONCLUSION
```

## 7. Mandatory read order for a new chat

The new chat must not mutate before completing this sequence:

1. Fresh-read `main` HEAD/TREE.
2. `README_START_HERE.md`
3. `00_CONTROL/NEW_CHAT_BOOTSTRAP.md`
4. `95_HANDOFF/CURRENT_HANDOFF_POINTER.md`
5. pointer `CURRENT_MASTER`
6. pointer `CURRENT_CHECKLIST`
7. pointer `CURRENT_STATUS_FORMAT`
8. `00_CONTROL/AI_LAWS_MASTER_RESEARCH_NOTEBOOK_ORCHESTRATION.md`
9. `00_CONTROL/PROJECT_CHARTER.md`
10. `00_CONTROL/SOURCE_OF_TRUTH_AND_AUTHORITY.md`
11. `00_CONTROL/RESEARCH_MUTATION_AND_ACCEPTANCE_GATE.md`
12. `00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md`
13. `10_TAXONOMY/LEGAL_DOMAIN_TAXONOMY.csv`
14. `10_TAXONOMY/CLAIM_EVIDENCE_AND_AUTHORITY_CLASSES.md`
15. `20_JURISDICTIONS/JURISDICTION_RESEARCH_REGISTRY.csv`
16. `20_JURISDICTIONS/GLOBAL_JURISDICTION_RESEARCH_PROTOCOL.md`
17. `30_CASE_LAW/CASE_LAW_CORPUS_SCHEMA.yaml`
18. `40_LIABILITY/AI_LIABILITY_CAUSATION_AND_REMEDY_TAXONOMY.md`
19. `50_RIGHTS/HUMAN_SOVEREIGNTY_COGNITIVE_LIBERTY_AND_DIGNITY_FRAME.md`
20. `60_INCIDENTS/INCIDENT_TO_LEGAL_ANALYSIS_SCHEMA.yaml`
21. `70_FINANCIAL_RESPONSIBILITY/AI_FINANCIAL_RESPONSIBILITY_RESEARCH_FRAME.md`
22. `80_CROSS_REPO/CROSS_REPO_AUTHORITY_AND_ROUTING.md`
23. `80_CROSS_REPO/PROJECT_ROUTING_MATRIX.csv`
24. relevant `85_RESEARCH_ASSISTANTS/*` controls if a model/Grok workflow is in scope
25. complete relevant `86_NOTEBOOKLM/*` controls if source acquisition/Notebook work is in scope
26. `90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv`
27. exact jurisdiction/domain/research closeout files for the selected bounded unit
28. fresh current official sources where currentness materially affects the unit
29. fresh-read HEAD/TREE again immediately before mutation/download/upload

Overlapping unexplained drift => STOP.

## 8. R012-specific read extension if R012 is explicitly selected

Read at minimum:

- `40_LIABILITY/AI_LIABILITY_CAUSATION_AND_REMEDY_TAXONOMY.md`
- `50_RIGHTS/AI-LAWS-R011_HUMAN_SOVEREIGNTY_COMPARATIVE_LEGAL_MAP_2026-09-14.md`
- `50_RIGHTS/AI-LAWS-R011_HUMAN_SOVEREIGNTY_RIGHTS_MATRIX_2026-09-14.csv`
- `50_RIGHTS/AI-LAWS-R011_SOURCE_AUTHORITY_AND_SCOPE_MATRIX_2026-09-14.csv`
- `95_RESEARCH/RIGHTS/AI-LAWS-R011_CLOSEOUT_2026-09-14.md`
- `20_JURISDICTIONS/EU/EU_AI_ACT_CURRENT_CONSOLIDATED_PHASED_APPLICATION_MAP_2026-09-14.md`
- `20_JURISDICTIONS/US/US_AI_LAW_INVENTORY_ARCHITECTURE_2026-09-14.md`
- `95_RESEARCH/GROK/AI-LAWS-R001_CLAIM_AND_ROUTING_MATRIX.csv`
- `86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_PACK_ASSIGNMENTS.csv`
- `86_NOTEBOOKLM/NOTEBOOKLM_ACQUISITION_AND_VALIDATION_LEDGER.csv`
- exact current primary-law sources used for any material liability claim

If a listed path has changed, discover the current path from GitHub; do not guess.

## 9. Liability chain firewall

For R012 or any liability work keep exact separation:

```text
ACTOR
DUTY
BREACH
CAUSATION
DAMAGE
REMEDY
DEFENCE
EVIDENCE
JURISDICTION
DATE_STATE
```

No missing element may be inferred from another element.

```text
REGULATORY_BREACH != AUTOMATIC_CIVIL_LIABILITY
STANDARD_NONCOMPLIANCE != AUTOMATIC_LEGAL_BREACH
STANDARD_COMPLIANCE != AUTOMATIC_DEFENCE
INCIDENT != LIABILITY
```

## 10. GitHub-only execution preference

For project mutations requested by the user:

```text
PREFERRED_EXECUTION = GITHUB_ONLY
ZIP_OR_ARTIFACT_FOR_USER = DO_NOT_CREATE_UNLESS_EXPLICITLY_REQUESTED
TEMPORARY_GITHUB_HELPERS = REMOVE_AFTER_UNIT
AUTO_ADVANCE = NO
```

GitHub Actions may be used for controlled source verification when appropriate, but temporary workflows/scripts must be cleaned after the bounded unit and artifact creation must not be introduced merely for transport.

## 11. Manual upload policy for a new chat

### Preferred mode — GitHub connected

If the new chat has access to `@GitHub`, the user does not need to upload repository files manually. Paste only:

`95_HANDOFF/READY_TO_PASTE_NEW_CHAT_PROMPT.txt`

The assistant must then read all required files directly from GitHub.

### Fallback mode — GitHub unavailable

Upload the exact minimal continuity packet listed in:

`95_HANDOFF/AI_LAWS_NEW_CHAT_BOOTSTRAP_CHECKLIST_2026-09-14.md`

A prior-chat export may be included as supplemental history only.

## 12. Required first continuity response

Before any mutation, the new chat must return the fields defined in:

`95_HANDOFF/AI_LAWS_NEW_CHAT_STATUS_FORMAT_2026-09-14.md`

At minimum it must report fresh:

```text
REPOSITORY
BRANCH
CURRENT_HEAD
CURRENT_TREE
CURRENT_PROJECT_STATE
CURRENT_HANDOFF_POINTER
R011_STATE
R005_STATE
R006_STATE
QUEUE_NEXT_CANDIDATES
SELECTED_BOUNDED_UNIT = NONE
LEGAL_ADVICE = NO
MODEL_OUTPUT_CANONICAL = NO
NOTEBOOK_OUTPUT_CANONICAL = NO
UNKNOWN_PRESERVED = YES
AUTO_ADVANCE = NO
```

Only after that continuity response and a user instruction may one bounded mutation/research unit begin.
