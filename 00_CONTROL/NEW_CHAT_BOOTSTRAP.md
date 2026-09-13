# AI-LAWS — NEW CHAT BOOTSTRAP

**STATE:** ACTIVE
**REPOSITORY:** `fatihekler/ai-laws`
**BRANCH:** `main`
**AUTO_ADVANCE:** NO

## Purpose

Every new AI-LAWS chat starts by reconstructing current repository state from GitHub rather than relying on memory or another project.

## Mandatory startup order

1. Fresh-read `main` HEAD and TREE.
2. Read `README_START_HERE.md`.
3. Read this file.
4. Read `00_CONTROL/AI_LAWS_MASTER_RESEARCH_NOTEBOOK_ORCHESTRATION.md`.
5. Read `00_CONTROL/PROJECT_CHARTER.md`.
6. Read `00_CONTROL/SOURCE_OF_TRUTH_AND_AUTHORITY.md`.
7. Read `00_CONTROL/RESEARCH_MUTATION_AND_ACCEPTANCE_GATE.md`.
8. Read `00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md`.
9. Read `10_TAXONOMY/LEGAL_DOMAIN_TAXONOMY.csv` and `10_TAXONOMY/CLAIM_EVIDENCE_AND_AUTHORITY_CLASSES.md`.
10. Read `20_JURISDICTIONS/JURISDICTION_RESEARCH_REGISTRY.csv` and `20_JURISDICTIONS/GLOBAL_JURISDICTION_RESEARCH_PROTOCOL.md`.
11. If Grok/model collaboration is in scope, read `85_RESEARCH_ASSISTANTS/GROK_CHATGPT_COLLABORATION_PROTOCOL.md`, the Grok master instruction and model handoff schema.
12. If NotebookLM/Gemini Notebook or source acquisition is in scope, read the complete `86_NOTEBOOKLM` control set, including `NOTEBOOKLM_END_TO_END_EXECUTION_RUNBOOK.md` and `NOTEBOOKLM_ACQUISITION_AND_VALIDATION_LEDGER.csv`.
13. Read `90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv`.
14. Read the exact jurisdiction/domain/case-law/cross-repo protocol relevant to the requested bounded unit.
15. Fresh-read any primary legal source whose current status materially affects the answer.
16. Before mutation/download/upload, fresh-read HEAD/TREE again and stop on overlapping drift.

## Source precedence

```text
CURRENT_OFFICIAL_PRIMARY_SOURCE
>
CURRENT_AI_LAWS_GITHUB_STATE_AND_VERIFIED_SOURCE_RECORDS
>
CURRENT_VERIFIED_SECONDARY_SOURCE
>
CURRENT_VERIFIED_INCIDENT_EVIDENCE
>
CURRENT_CROSS_REPO_EVIDENCE_OR_PROPOSAL
>
LLM_OR_NOTEBOOK_OUTPUT
>
CHAT_MEMORY
```

## Authority firewall

Do not import another repository's PASS, APPROVED, CANONICAL, blocker closure, pointer or human-review completion as AI-LAWS legal authority.

Do not export AI-LAWS research as another project's automatic technical, ethical, theological or engineering acceptance.

```text
AI_LAWS_FINDING != OWASP_FINDING
AI_LAWS_FINDING != ENGINEERING_OS_ACCEPTANCE
AI_LAWS_FINDING != ETHICAL_AI_ACCEPTANCE
AI_LAWS_FINDING != ESMA_THEOLOGICAL_VALIDATION
AI_LAWS_FINDING != APESTEORI_CANONICAL_STATE
```

## Model / Notebook firewall

```text
GROK_OUTPUT != LEGAL_AUTHORITY
CHATGPT_OUTPUT != LEGAL_AUTHORITY
NOTEBOOK_OUTPUT != LEGAL_AUTHORITY
YARGIGPT_OUTPUT != COURT_DECISION
MULTIPLE_MODELS_AGREE != FACT_PROVEN
```

Model output must route back to current primary/official/independent sources before it can support a verified AI-LAWS claim.

## Legal integrity rules

- official source unavailable => preserve UNKNOWN;
- no verified full text => no court-case corpus entry;
- search failure => research interruption, not negative legal finding;
- current law and policy proposal must be separated;
- allegation and proven fact must be separated;
- source date, effective date, amendment/consolidation state and jurisdiction must be recorded;
- translation must not silently replace the authentic text;
- legal analogy must state its limit;
- conflicting authorities remain explicit until resolved by proper legal review;
- downloaded source identity, rights/use state and currentness must be logged before Notebook ingestion;
- Notebook source identity must be tested before substantive analysis;
- material Notebook claims require primary-source recheck.

## Broad commands

A broad instruction such as “research everything, create needed documents and continue” authorizes at most one bounded repository unit unless the current gate explicitly says otherwise.

```text
USER_SAYS_CONTINUE != UNLIMITED_AUTO_ADVANCE
BROAD_RESEARCH != AUTOMATIC_CANONICALIZATION
AUTO_ADVANCE = NO
```
