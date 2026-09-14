# AI-LAWS — NEW CHAT STATUS FORMAT

**STATE:** ACTIVE
**DATE:** 2026-09-14

## 1. Mandatory first continuity response

Before any mutation, download, Notebook ingestion, cross-repo write or substantive new bounded unit, return this block with fresh values:

```text
REPOSITORY = fatihekler/ai-laws
BRANCH = main
CURRENT_HEAD = <fresh GitHub SHA>
CURRENT_TREE = <fresh GitHub tree SHA>
CURRENT_PROJECT_STATE = <from 00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md>
CURRENT_HANDOFF_POINTER = 95_HANDOFF/CURRENT_HANDOFF_POINTER.md
CURRENT_HANDOFF_MASTER = <pointer CURRENT_MASTER>
CURRENT_QUEUE = 90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv
R011_STATE = <fresh queue/current-context state>
R005_STATE = <fresh queue state>
R006_STATE = <fresh queue state>
R019_STATE = <fresh queue state>
QUEUE_NEXT_CANDIDATES = <list READY/BLOCKED candidates without auto-selecting>
PRIMARY_SEQUENTIAL_CANDIDATE = <if supported by current queue; otherwise UNKNOWN>
SELECTED_BOUNDED_UNIT = NONE
UNEXPLAINED_DRIFT = NO/YES
LEGAL_ADVICE = NO
MODEL_OUTPUT_CANONICAL = NO
NOTEBOOK_OUTPUT_CANONICAL = NO
UNKNOWN_PRESERVED = YES
AUTO_ADVANCE = NO
```

Then state in one short paragraph whether continuity reconstruction is complete and whether any blocker/conflict was found.

## 2. Bounded-unit opening format

Only after a user explicitly authorizes continuation:

```text
UNIT_ID = <AI-LAWS-R### or registered batch ID>
ROLE = <RESEARCHER / LEGAL_ANALYST / RECONCILER / etc.>
BASE_HEAD = <fresh SHA>
BASE_TREE = <fresh tree SHA>
SCOPE = <one bounded scope>
ALLOWED_PATHS = <exact paths/families>
FORBIDDEN_ACTIONS = <what this unit will not do>
SOURCE_POLICY = <official/current source rules>
EXPECTED_OUTPUTS = <durable GitHub files>
STOP_CONDITION = <exact boundary>
AUTO_ADVANCE = NO
```

A broad user command still authorizes at most one bounded unit.

## 3. Source/result format

For each material source or claim preserve, where applicable:

```text
SOURCE_ID
JURISDICTION
TITLE
DOCUMENT_ID
ISSUING_AUTHORITY
AUTHORITY_CLASS
BINDING_STATE
ADOPTION_DATE
PUBLICATION_DATE
ENTRY_INTO_FORCE_DATE
APPLICATION_DATE
AMENDMENT_OR_CONSOLIDATION_STATE
AUTHENTIC_LANGUAGE
TRANSLATION_STATE
OFFICIAL_URL
RETRIEVAL_DATE
CONTENT_IDENTITY_STATE
CURRENTNESS_STATE
KNOWN
UNKNOWN
LIMITATION
```

Do not fill UNKNOWN fields by inference.

## 4. Liability-analysis format

When liability is in scope, always separate:

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

No omitted element may be silently inferred.

## 5. Bounded-unit closeout format

At the end of a unit, report:

```text
UNIT_ID = ...
BASE_HEAD = ...
DURABLE_COMMIT = ...
FINAL_HEAD = ...
FINAL_TREE = ...
OUTPUTS_CREATED_OR_UPDATED = [...]
SOURCE_RECORDS_VERIFIED = ...
CONTENT_IDENTITY_VERIFIED = ...
CONFLICTS = ...
UNKNOWNS = ...
BLOCKERS = ...
NOTEBOOK_UPLOADS = ...
DERIVED_MARKDOWN_CREATED = ...
ZIP_OR_ARTIFACT_CREATED = NO unless explicitly requested
TEMPORARY_HELPERS_REMAINING = 0 if helpers were used and cleanup completed
LEGAL_CONCLUSION = NOT_ATTEMPTED unless the bounded unit expressly authorizes a reviewed conclusion
NEXT_BOUNDED_CANDIDATE = ...
AUTO_ADVANCE = NO
STOP = YES
```

## 6. Continuity invariant

```text
CURRENT_GITHUB_STATE > CURRENT_HANDOFF > CHAT_EXPORT > MODEL_MEMORY
SEARCH_FAILURE != NEGATIVE_LEGAL_FINDING
SUPPORTING_RESEARCH != LEGAL_AUTHORITY
AUTO_ADVANCE = NO
```
