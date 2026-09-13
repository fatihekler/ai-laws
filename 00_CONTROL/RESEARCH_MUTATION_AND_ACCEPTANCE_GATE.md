# AI-LAWS — RESEARCH, MUTATION AND ACCEPTANCE GATE

## Core rule

AI-LAWS separates research, evidence capture, legal analysis, human review and canonical project decisions.

```text
RESEARCH != LEGAL_CONCLUSION
EVIDENCE_CAPTURE != ACCEPTANCE
CROSS_REPO_TRANSFER != AUTHORITY_TRANSFER
LLM_SYNTHESIS != CANONICAL_STATE
AUTO_ADVANCE = NO
```

## Bounded-unit rule

One explicit “continue / next / research and proceed” instruction authorizes at most one bounded unit unless the current control file explicitly grants more.

Each bounded unit records:

```text
UNIT_ID
ROLE
BASE_HEAD
BASE_TREE
SCOPE
ALLOWED_PATHS
FORBIDDEN_ACTIONS
SOURCE_POLICY
STOP_CONDITION
NEXT_ITEM
AUTO_ADVANCE = NO
```

## Allowed roles

- `OBSERVER`
- `RESEARCHER`
- `LEGAL_ANALYST`
- `CASE_LAW_RESEARCHER`
- `COMPARATIVE_LAW_RESEARCHER`
- `POLICY_ANALYST`
- `REVIEWER`
- `RECONCILER`
- `HUMAN_LEGAL_REVIEWER`

No role may claim judicial/regulatory authority.

## Mutation classes

### A. Append-only research

May create new evidence/research records. It must not rewrite a verified historical source record to erase conflicts.

### B. Controlled reconciliation

May update indexes, registries or current synthesis only after enumerating consumed evidence and preserving conflicts/unknowns.

### C. Human legal review

Required for material claims that will be labeled as project-level legal conclusions, legal advice-like recommendations, jurisdiction-specific action plans, or litigation/regulatory submissions.

## Fail-closed rules

Stop or preserve UNKNOWN when:

- official source unavailable;
- currentness/effective date cannot be confirmed;
- authentic text/translation status is unclear and material;
- conflicting authorities are unresolved;
- court full text cannot be verified;
- jurisdiction or actor role is ambiguous;
- factual incident identity is disputed;
- legal conclusion would require facts not in evidence;
- branch drift overlaps the bounded task.

## Case-law admission gate

A case may enter the verified case corpus only if:

```text
OFFICIAL_OR_ACCEPTED_AUTHORITATIVE_SOURCE = VERIFIED
DECISION_IDENTITY = VERIFIED
FULL_TEXT = VERIFIED
RELEVANCE_CLASS = ASSIGNED
ANALOGY_LIMIT = RECORDED_IF_ANALOGICAL
SOURCE_DATE = RECORDED
CANONICAL = FALSE_UNTIL_REVIEW
```

## Policy-proposal gate

Catastrophe funds, mandatory insurance, special strict-liability regimes, new neurorights, new criminal offences or new regulator powers must be labeled `POLICY_PROPOSAL` unless current binding law is verified.

## External systems

No external scraper, API client, agent, model, skill or automation receives repository mutation authority merely because it is useful for research.

## Current execution policy

At initialization, research/documentation mutations are permitted when explicitly requested by the user. Automated legal conclusions, filing, litigation actions, regulator submissions and external runtime actions are not authorized.
