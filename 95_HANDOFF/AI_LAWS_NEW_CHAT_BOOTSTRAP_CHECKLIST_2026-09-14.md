# AI-LAWS — NEW CHAT BOOTSTRAP CHECKLIST

**STATE:** ACTIVE
**DATE:** 2026-09-14
**REPOSITORY:** `fatihekler/ai-laws`
**BRANCH:** `main`

## A. Preferred mode — new chat has @GitHub access

No repository file upload is required.

User action:

- open a new chat in the same AI-LAWS project;
- ensure GitHub access is available;
- paste the contents of `95_HANDOFF/READY_TO_PASTE_NEW_CHAT_PROMPT.txt`;
- optionally attach/export the previous chat only as supplemental history.

Assistant action before any mutation:

- [ ] fresh-read `main` HEAD/TREE;
- [ ] read `README_START_HERE.md`;
- [ ] read `00_CONTROL/NEW_CHAT_BOOTSTRAP.md`;
- [ ] read `95_HANDOFF/CURRENT_HANDOFF_POINTER.md`;
- [ ] follow pointer `CURRENT_MASTER`;
- [ ] follow pointer `CURRENT_CHECKLIST`;
- [ ] follow pointer `CURRENT_STATUS_FORMAT`;
- [ ] read master orchestration, authority, mutation gate, current context and queue;
- [ ] read domain/jurisdiction/source files required by the selected bounded unit;
- [ ] return the first continuity status block before mutation;
- [ ] wait for/consume one explicit user bounded-unit instruction;
- [ ] fresh-read HEAD/TREE again immediately before mutation;
- [ ] stop on unexplained overlapping drift.

## B. Fallback mode — GitHub access unavailable

Do not create a ZIP. Upload the following files individually.

### Minimal mandatory continuity packet

- [ ] `README_START_HERE.md`
- [ ] `00_CONTROL/NEW_CHAT_BOOTSTRAP.md`
- [ ] `95_HANDOFF/CURRENT_HANDOFF_POINTER.md`
- [ ] `95_HANDOFF/AI_LAWS_NEW_CHAT_CONTINUITY_MASTER_2026-09-14.md`
- [ ] `95_HANDOFF/AI_LAWS_NEW_CHAT_BOOTSTRAP_CHECKLIST_2026-09-14.md`
- [ ] `95_HANDOFF/AI_LAWS_NEW_CHAT_STATUS_FORMAT_2026-09-14.md`
- [ ] `00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md`
- [ ] `90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv`

### Mandatory governance extension

- [ ] `00_CONTROL/AI_LAWS_MASTER_RESEARCH_NOTEBOOK_ORCHESTRATION.md`
- [ ] `00_CONTROL/PROJECT_CHARTER.md`
- [ ] `00_CONTROL/SOURCE_OF_TRUTH_AND_AUTHORITY.md`
- [ ] `00_CONTROL/RESEARCH_MUTATION_AND_ACCEPTANCE_GATE.md`
- [ ] `10_TAXONOMY/LEGAL_DOMAIN_TAXONOMY.csv`
- [ ] `10_TAXONOMY/CLAIM_EVIDENCE_AND_AUTHORITY_CLASSES.md`
- [ ] `20_JURISDICTIONS/JURISDICTION_RESEARCH_REGISTRY.csv`
- [ ] `20_JURISDICTIONS/GLOBAL_JURISDICTION_RESEARCH_PROTOCOL.md`

### If continuing with R012 comparative liability

- [ ] `40_LIABILITY/AI_LIABILITY_CAUSATION_AND_REMEDY_TAXONOMY.md`
- [ ] `50_RIGHTS/AI-LAWS-R011_HUMAN_SOVEREIGNTY_COMPARATIVE_LEGAL_MAP_2026-09-14.md`
- [ ] `50_RIGHTS/AI-LAWS-R011_HUMAN_SOVEREIGNTY_RIGHTS_MATRIX_2026-09-14.csv`
- [ ] `50_RIGHTS/AI-LAWS-R011_SOURCE_AUTHORITY_AND_SCOPE_MATRIX_2026-09-14.csv`
- [ ] `95_RESEARCH/RIGHTS/AI-LAWS-R011_CLOSEOUT_2026-09-14.md`
- [ ] `20_JURISDICTIONS/EU/EU_AI_ACT_CURRENT_CONSOLIDATED_PHASED_APPLICATION_MAP_2026-09-14.md`
- [ ] `20_JURISDICTIONS/US/US_AI_LAW_INVENTORY_ARCHITECTURE_2026-09-14.md`
- [ ] `95_RESEARCH/GROK/AI-LAWS-R001_CLAIM_AND_ROUTING_MATRIX.csv`

### If Notebook/source acquisition is in scope

Upload/read the relevant files from `86_NOTEBOOKLM/`, especially:

- [ ] `86_NOTEBOOKLM/README.md`
- [ ] `86_NOTEBOOKLM/NOTEBOOKLM_CORPUS_ARCHITECTURE.md`
- [ ] `86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_ACQUISITION_POLICY.md`
- [ ] `86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv`
- [ ] `86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_PACK_ASSIGNMENTS.csv`
- [ ] `86_NOTEBOOKLM/NOTEBOOKLM_END_TO_END_EXECUTION_RUNBOOK.md`
- [ ] `86_NOTEBOOKLM/NOTEBOOKLM_ACQUISITION_AND_VALIDATION_LEDGER.csv`

Do not upload the entire `86_NOTEBOOKLM/downloads/` directory blindly.

## C. Previous-chat export

A chat export is optional and supplemental.

If provided:

- [ ] label it `CHAT_EXPORT_SUPPORTING_ONLY`;
- [ ] use it to recover rationale/history only;
- [ ] do not use it to override current GitHub state;
- [ ] do not treat uncommitted chat plans as completed repository work;
- [ ] if chat export conflicts with GitHub, report the conflict and use current GitHub.

## D. First-response verification checklist

Before research or mutation, the new assistant must verify:

- [ ] repository = `fatihekler/ai-laws`;
- [ ] branch = `main`;
- [ ] current HEAD read fresh;
- [ ] current TREE read fresh;
- [ ] current handoff pointer read;
- [ ] current context read;
- [ ] research queue read;
- [ ] R011 durable state read;
- [ ] R005 blocker preserved;
- [ ] R006 blocker preserved;
- [ ] `AUTO_ADVANCE = NO`;
- [ ] no mutation performed during continuity reconstruction.

## E. Bounded-unit execution checklist

For each user command such as `devam`, `araştır ve gerçekleştir`, or `tüm işlemlere devam et`:

- [ ] authorize at most one bounded unit;
- [ ] name `UNIT_ID` and scope before mutation;
- [ ] read relevant source/control files;
- [ ] fresh-check current official sources where material;
- [ ] fresh-read HEAD/TREE immediately before mutation;
- [ ] stop on overlapping unexplained drift;
- [ ] preserve binding law / guidance / policy / incident / allegation separation;
- [ ] preserve UNKNOWN where source access/currentness/full text is unresolved;
- [ ] if GitHub Actions helpers are created, remove temporary helpers after the unit;
- [ ] do not create ZIP/artifact for transport unless explicitly requested;
- [ ] update durable queue/context/closeout only after assertions pass;
- [ ] stop before the next bounded unit.

## F. File-format rules

Use:

```text
Markdown control/research docs = .md
Structured registries/matrices = .csv
Machine schemas = .yaml when already defined that way
Ready-to-paste chat prompts = .txt
```

Naming conventions:

```text
AI-LAWS-R###_<DESCRIPTIVE_NAME>_YYYY-MM-DD.md
AI-LAWS-R###_<MATRIX_NAME>_YYYY-MM-DD.csv
NB-BATCH-<PACK>-<YYYYMMDD>-<NNN>
```

Do not rename existing canonical files merely for style consistency.

## G. First continuity response format

Use exactly the template in:

`95_HANDOFF/AI_LAWS_NEW_CHAT_STATUS_FORMAT_2026-09-14.md`

The continuity response is observational only. It must not itself start R012, R019, Notebook ingestion or another mutation.

## H. Current handoff stop state

```text
R011 = COMPLETE_RESEARCH_BASELINE_L1_L2_RIGHTS_MAP_SCOPE_LIMITS_OPEN
PRIMARY_SEQUENTIAL_CANDIDATE = R012
R002 = READY_RESEARCH
R005 = PARTIAL / LIVE OFFICIAL RECHECK BLOCKED
R006 = BLOCKED_BY_OFFICIAL_SOURCE_AVAILABILITY
R019 = READY_FOR_EXPLICIT_AUTHORIZATION
AUTO_ADVANCE = NO
STOP = YES
```
