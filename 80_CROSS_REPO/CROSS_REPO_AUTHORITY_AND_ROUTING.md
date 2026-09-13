# AI-LAWS — CROSS-REPO AUTHORITY AND ROUTING

## Purpose

AI-LAWS is one layer in a multi-project assurance architecture. It must receive and export evidence without importing another project's authority.

## Project roles

### AI-LAWS
Owns legal research concerning:
- applicable law;
- duties/prohibitions;
- precedent;
- evidence/procedure;
- liability/causation;
- remedies/sanctions;
- financial responsibility;
- legal governance and law-reform proposals.

### OWASP
Primary role:
- technical threats;
- attack/control/test hypotheses;
- vulnerability/security evidence;
- excessive agency/supply-chain/security findings.

### Engineering OS
Primary role:
- system requirements;
- architecture;
- bounded execution;
- verification/validation;
- evidence binding;
- lifecycle and acceptance mechanics.

### Ethical-AI
Primary role:
- human agency;
- dignity;
- accountability;
- appeal;
- reversibility;
- meaningful human control;
- harm and oversight candidates.

### Esmaul Husna
Primary role:
- source-reviewed human-facing moral/theological reminder and questioning layer.

Explicit firewall:

```text
ESMA_REMINDER != LEGAL_RULE
ESMA_MAPPING != LEGAL_LIABILITY
ESMA_MAPPING != TECHNICAL_CONTROL
AI_LAWS != THEOLOGICAL_AUTHORITY
```

### Apesteori
Primary role:
- multidimensional framing;
- psychological/social/technological/epistemological/power/emotional/moral/historical challenges;
- unknown/conflict discovery;
- noncanonical analytical support.

### NotebookLM / Gemini Notebook / Grok / ChatGPT / YargıGPT
Research and synthesis assistance only unless a separate system has explicitly granted a narrower authority.

## Routing grammar

Example incident:

```text
UNAUTHORIZED_AGENT_NETWORK_ACTION
```

Potential routes:

```text
OWASP -> technical threat/control/reproduction
ENGINEERING_OS -> requirement/test/evidence/assurance
ETHICAL_AI -> human agency/accountability impact
AI_LAWS -> duty/knowledge/causation/liability/evidence/remedy
ESMAUL_HUSNA -> human-facing responsibility/reminder candidate only
APESTEORI -> multidimensional challenge/unknown discovery
```

No route automatically imports the source project's conclusion.

## Transfer envelope

Every cross-repo transfer should record:

```text
TRANSFER_ID
SOURCE_PROJECT
SOURCE_REPOSITORY
SOURCE_ARTIFACT
SOURCE_COMMIT_OR_BLOB
TARGET_PROJECT
TRANSFER_TYPE = EVIDENCE | QUESTION | CANDIDATE | PROPOSAL | CONFLICT
CLAIM
EVIDENCE_CLASS
AUTHORITY_NON_TRANSFER = TRUE
REQUIRED_TARGET_REVIEW
UNKNOWNS
CONFLICTS
```

## Legal intake from technical projects

AI-LAWS needs facts/evidence such as:
- exact system identity;
- capability/permission scope;
- logs;
- security findings;
- control/test results;
- incident timeline;
- affected assets/persons;
- warnings and known limitations.

It must not treat a scanner or model output as proof of legal breach.

## Engineering export

Where AI-LAWS verifies an applicable duty, export a requirement candidate in this shape:

```text
LEGAL_SOURCE
JURISDICTION
DUTY_OR_PROHIBITION
TRIGGER_CONDITIONS
RESPONSIBLE_ACTOR
REQUIRED_ACTION_OR_CONSTRAINT
EVIDENCE_REQUIRED
EXCEPTIONS
EFFECTIVE_DATE
LEGAL_REVIEW_STATE
```

Engineering OS may then translate accepted requirements into controls/tests/evidence under its own governance.

## Conflict rule

If projects disagree, preserve both claims and the exact evidence. Do not overwrite one project with another's conclusion.

```text
CROSS_REPO_CONFLICT -> EXPLICIT_CONFLICT_RECORD
NOT -> SILENT_MERGE
```
