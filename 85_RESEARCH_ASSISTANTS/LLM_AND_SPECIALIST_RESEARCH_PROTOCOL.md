# AI-LAWS — LLM AND SPECIALIST RESEARCH ASSISTANT PROTOCOL

## Purpose

Define how ChatGPT, Grok, YargıGPT, Gemini Notebook/NotebookLM and other specialist tools may contribute without becoming legal authority.

## Universal rule

```text
ASSISTANT_OUTPUT = SUPPORTING_RESEARCH
CANONICAL = FALSE
LEGAL_AUTHORITY_ASSUMED = FALSE
DESTINATION_PROJECT_ACCEPTANCE_ASSUMED = FALSE
```

## Required metadata for every imported assistant output

```text
ASSISTANT_NAME
MODEL_OR_SERVICE_IF_KNOWN
GENERATION_DATE
PROMPT_ID_OR_SCOPE
SOURCE_SET_IDENTITY
LIVE_WEB_OR_DATABASE_USED
PRIMARY_SOURCE_VERIFICATION_STATE
OUTPUT_TYPE
CLAIM_COUNT
CONFLICT_COUNT
UNKNOWN_COUNT
HUMAN_REVIEW_STATE
CANONICAL = FALSE
```

## ChatGPT role

Best suited for:
- structured legal-research planning;
- official-source web verification;
- comparative synthesis;
- corpus/schema design;
- cross-repo routing;
- contradiction and gap analysis.

Must not:
- invent cases or statutes;
- give definitive liability conclusions from incomplete facts;
- silently substitute model knowledge for current primary law.

## Grok role

Preferred role: `ADVERSARIAL_EXTERNAL_RESEARCHER / CHALLENGER`.

Ask Grok to:
- challenge assumptions;
- reconstruct public timelines;
- distinguish company statements from independent evidence;
- investigate competition/regulatory-capture/market-power counterarguments;
- test financial-responsibility proposals against economic feasibility;
- identify claims that are plausible but not proved;
- source-verify its own earlier statements.

Do not ask Grok merely to agree with the project thesis.

Imported Grok claims should be classified as:

```text
WELL_ESTABLISHED
PLAUSIBLE_NOT_PROVEN
POLICY_PROPOSAL
UNKNOWN
```

before source verification.

## YargıGPT role

Preferred role: `TURKISH_CASE_LAW_SOURCE_DISCOVERY_ASSISTANT`.

Rules:
- official source/full-text verification required;
- API unavailable => interruption evidence only;
- no remembered-case reconstruction;
- no `NONE_FOUND` from failed search;
- analogical precedents require `ANALOGY_LIMIT`;
- batch size should remain small and reviewable.

Current preserved evidence:
- TR-LAW-01-B001 = official source unavailable;
- TR-LAW-01-B002 = official source unavailable.

If a later independent-time retry produces the same failure with no new information, prefer `BLOCKED_BY_OFFICIAL_SOURCE_AVAILABILITY` and reroute rather than infinite retry.

## Gemini Notebook / NotebookLM role

Preferred role: source-grounded synthesis and matrix generation.

Require exact source locators and explicit UNKNOWN/conflict fields.

Do not treat notebook citation as authority transfer.

Recommended matrix fields:

```text
ROW_ID
JURISDICTION
SOURCE
SOURCE_LOCATOR
CLAIM
AUTHORITY_CLASS
BINDING_STATE
LEGAL_DOMAIN
ACTOR
RIGHT_OR_INTEREST
DUTY_OR_PROHIBITION
EVIDENCE_REQUIRED
CURRENT_LAW_OR_PROPOSAL
CONFLICT
UNKNOWN
CROSS_REPO_TARGET
CANONICAL = FALSE
```

## Cross-model disagreement

When assistants disagree:

```text
DO_NOT_AVERAGE
DO_NOT_PICK_BY_CONFIDENCE_TONE
VERIFY_ORIGINAL_SOURCES
PRESERVE_CONFLICT_IF_UNRESOLVED
```

## Weapon/exploit/biological boundary

AI-LAWS researches legal categories, duties, prohibitions, incidents and governance. Do not turn legal research into operational harmful instructions.

## Final import rule

Assistant output enters the project through:

```text
ASSISTANT OUTPUT
-> APPEND-ONLY RESEARCH RECORD
-> ORIGINAL-SOURCE VERIFICATION
-> LEGAL CLASSIFICATION
-> HUMAN REVIEW WHERE MATERIAL
-> RECONCILIATION
-> CURRENT PROJECT SYNTHESIS
```
