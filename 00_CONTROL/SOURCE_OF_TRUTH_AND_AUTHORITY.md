# AI-LAWS — SOURCE OF TRUTH AND AUTHORITY

## 1. Authority hierarchy

AI-LAWS stores many evidence classes. They do not have equal legal authority.

Default precedence for a concrete legal claim:

```text
AUTHENTIC_CURRENT_PRIMARY_LEGAL_TEXT_OR_OFFICIAL_COURT_DECISION
>
OFFICIAL_CONSOLIDATED_OR_REGULATORY_SOURCE
>
OFFICIAL_GUIDANCE / EXPLANATORY MATERIAL
>
VERIFIED_SECONDARY_LEGAL_SOURCE / SCHOLARLY ANALYSIS
>
REPUTABLE FACTUAL REPORTING / INCIDENT DISCLOSURE
>
CROSS_REPO EVIDENCE OR PROPOSAL
>
LLM / NOTEBOOK / SEARCH SYNTHESIS
>
CHAT MEMORY
```

This is not a universal jurisprudential hierarchy; local law may assign authority differently. The exact jurisdiction controls.

## 2. Mandatory authority classes

Every material record must use one or more of:

- `CONSTITUTIONAL_TEXT`
- `STATUTE_OR_REGULATION`
- `TREATY_OR_INTERNATIONAL_INSTRUMENT`
- `BINDING_COURT_DECISION`
- `NONBINDING_OR_PERSUASIVE_CASE_LAW`
- `REGULATORY_DECISION`
- `REGULATORY_GUIDANCE`
- `OFFICIAL_STANDARD_OR_FRAMEWORK`
- `TECHNICAL_STANDARD`
- `SOFT_LAW_RECOMMENDATION`
- `SCHOLARLY_ANALYSIS`
- `OFFICIAL_COMPANY_STATEMENT`
- `INDEPENDENT_REPORTING`
- `FACTUAL_INCIDENT_RECORD`
- `ALLEGATION`
- `POLICY_PROPOSAL`
- `MODEL_GENERATED_RESEARCH`
- `UNKNOWN`

## 3. Mandatory state fields

For legal instruments where applicable:

```text
JURISDICTION
ISSUING_BODY
DOCUMENT_ID
ADOPTION_DATE
PUBLICATION_DATE
ENTRY_INTO_FORCE_DATE
APPLICATION_DATE
AMENDMENT_STATE
CONSOLIDATED_VERSION_DATE
BINDING_STATE
OFFICIAL_SOURCE
RETRIEVAL_DATE
LANGUAGE
AUTHENTIC_LANGUAGE_STATE
```

If not verified, use `UNKNOWN`, not inference.

## 4. Claim-state vocabulary

Use:

- `VERIFIED_PRIMARY`
- `VERIFIED_OFFICIAL_SECONDARY`
- `VERIFIED_REPUTABLE_SECONDARY`
- `SUPPORTED_INFERENCE`
- `POLICY_PROPOSAL`
- `DISPUTED`
- `UNKNOWN`
- `SOURCE_UNAVAILABLE`
- `SUPERSEDED`
- `NOT_APPLICABLE`

## 5. Legal conclusion firewall

No single record automatically proves:

```text
DUTY
BREACH
CAUSATION
DAMAGE
LIABILITY
CRIMINAL_RESPONSIBILITY
REGULATORY_VIOLATION
REMedy entitlement
```

Those elements depend on jurisdiction-specific law and verified facts.

## 6. Cross-project authority

Information may be transferred as evidence or proposals, never as automatic authority.

- OWASP supplies threat/control/test evidence.
- Engineering OS supplies requirements/V&V/runtime evidence.
- Ethical-AI supplies human-agency/accountability/rights candidates.
- Esmaul Husna supplies source-reviewed human-facing moral/theological reminders only.
- Apesteori supplies noncanonical multidimensional analysis/challenges.
- AI-LAWS performs legal research and legal-engineering analysis.

Destination review remains mandatory.

## 7. Assistant-output rule

Outputs from ChatGPT, Grok, YargıGPT, Gemini Notebook/NotebookLM or other assistants must record:

```text
GENERATOR
GENERATION_DATE
PROMPT_SCOPE
SOURCE_SET
SOURCE_VERIFICATION_STATE
CONFLICTS
UNKNOWNS
CANONICAL = FALSE
```

until separately reviewed.
