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
4. Read `00_CONTROL/PROJECT_CHARTER.md`.
5. Read `00_CONTROL/SOURCE_OF_TRUTH_AND_AUTHORITY.md`.
6. Read `00_CONTROL/RESEARCH_MUTATION_AND_ACCEPTANCE_GATE.md`.
7. Read `00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md`.
8. Read the exact jurisdiction/domain/case-law/cross-repo protocol relevant to the requested bounded unit.
9. Fresh-read any primary legal source whose current status materially affects the answer.
10. Before mutation, fresh-read HEAD/TREE again and stop on overlapping drift.

## Source precedence

```text
CURRENT_OFFICIAL_PRIMARY_SOURCE
>
CURRENT_AI_LAWS_GITHUB_STATE_AND_VERIFIED_SOURCE_RECORDS
>
CURRENT_VERIFIED_SECONDARY_SOURCE
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

## Legal integrity rules

- official source unavailable => preserve UNKNOWN;
- no verified full text => no court-case corpus entry;
- search failure => research interruption, not negative legal finding;
- current law and policy proposal must be separated;
- allegation and proven fact must be separated;
- source date, effective date, amendment/consolidation state and jurisdiction must be recorded;
- translation must not silently replace the authentic text;
- legal analogy must state its limit;
- conflicting authorities remain explicit until resolved by proper legal review.

## Broad commands

A broad instruction such as “research everything, create needed documents and continue” authorizes at most one bounded repository unit unless the current gate explicitly says otherwise.

```text
USER_SAYS_CONTINUE != UNLIMITED_AUTO_ADVANCE
BROAD_RESEARCH != AUTOMATIC_CANONICALIZATION
AUTO_ADVANCE = NO
```
