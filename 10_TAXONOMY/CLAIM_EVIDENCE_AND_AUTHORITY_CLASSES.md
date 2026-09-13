# AI-LAWS — CLAIM, EVIDENCE AND AUTHORITY CLASSES

## Purpose

This taxonomy prevents factual, legal, policy and model-generated statements from collapsing into one undifferentiated corpus.

## Evidence classes

### E0 — UNKNOWN
No reliable source or insufficiently verified state.

### E1 — MODEL / NOTEBOOK GENERATED
Output produced by an AI assistant or synthesis system. Useful for candidate discovery only.

### E2 — SECONDARY REPORTING / COMMENTARY
Journalism, commentary, practitioner analysis or non-official summaries.

### E3 — SCHOLARLY / PROFESSIONAL ANALYSIS
Peer-reviewed or otherwise identifiable academic/professional work. Persuasive, not primary law by itself.

### E4 — OFFICIAL NONBINDING
Government/regulator/standards-body guidance, official explanatory material, voluntary framework, recommendation or policy document.

### E5 — OFFICIAL PRIMARY LEGAL SOURCE
Authentic statute, regulation, treaty text, official gazette, binding regulatory decision, verified court decision or other primary source under the applicable legal system.

## Claim classes

Every material proposition should be identified as one of:

- `FACTUAL_EVENT`
- `LEGAL_TEXT_CONTENT`
- `COURT_HOLDING`
- `REGULATORY_POSITION`
- `LEGAL_INTERPRETATION`
- `ANALOGY`
- `CAUSATION_HYPOTHESIS`
- `LIABILITY_HYPOTHESIS`
- `RISK_HYPOTHESIS`
- `POLICY_PROPOSAL`
- `ETHICAL_ARGUMENT`
- `THEOLOGICAL_REMINDER`
- `TECHNICAL_FINDING`
- `ECONOMIC_PROJECTION`
- `UNKNOWN`

## Binding-state values

```text
BINDING
CONDITIONALLY_BINDING
PERSUASIVE
VOLUNTARY
SOFT_LAW
PROPOSAL
NOT_LAW
UNKNOWN
```

The exact meaning is jurisdiction-specific.

## Factual-state values

```text
VERIFIED
PARTIALLY_VERIFIED
DISPUTED
ALLEGED
RETRACTED_OR_CORRECTED
UNKNOWN
```

## Legal-relevance classes for precedents

```text
DIRECTLY_RELEVANT
ANALOGICAL_PRECEDENT
NOT_RELEVANT
UNKNOWN
```

For `ANALOGICAL_PRECEDENT`, both must be recorded:

```text
ANALOGOUS_ELEMENT
ANALOGY_LIMIT
```

## Current-law versus reform separation

Every legal recommendation must identify:

```text
CURRENT_LAW
CURRENT_NONBINDING_GUIDANCE
LEGAL_AMBIGUITY
POLICY_PROPOSAL
RESEARCH_HYPOTHESIS
```

No proposal is promoted by rhetorical urgency.

## Knowledge/notice separation

The following are distinct:

```text
PUBLIC_INFORMATION_EXISTED
ACTOR_ACTUALLY_KNEW
ACTOR_SHOULD_HAVE_KNOWN
RISK_WAS_LEGALLY_FORESEEABLE
DUTY_REQUIRED_ACTION
BREACH_OCCURRED
```

Evidence for one does not automatically prove another.

## Technology/legal non-equivalence

```text
SCANNER_FINDING != LEGAL_BREACH
MODEL_CAPABILITY != LEGAL_DUTY
SECURITY_INCIDENT != AUTOMATIC_TORT
SAFETY_STANDARD_COMPLIANCE != AUTOMATIC_NO_LIABILITY
TECHNICAL_FAILURE != AUTOMATIC_CAUSATION
```

## Human-review trigger

Require qualified human legal review before a record is used for:

- filing or threatening litigation;
- regulator submissions;
- jurisdiction-specific compliance instructions;
- claims of criminal conduct;
- definitive liability conclusions;
- interpretation of materially conflicting authorities;
- significant policy advocacy presented as settled law.
