# AI-LAWS-R020 — Destination-Neutral Legal Requirement Candidate Method

**WORK_ITEM:** `AI-LAWS-R020`
**DATE:** 2026-09-14
**REPOSITORY:** `fatihekler/ai-laws`
**BRANCH:** `main`
**LEGAL_ADVICE:** NO
**DESTINATION_MUTATION:** NO
**AUTO_ADVANCE:** NO

## 1. Purpose

R020 translates already-verified legal duties into destination-neutral requirement **candidates** for later review by Engineering OS, OWASP and Ethical-AI. It does not write to, bind, or modify any destination repository.

A candidate is not a new legal rule. It is a controlled implementation proposition traceable to a verified legal duty.

```text
LEGAL_DUTY_VERIFIED != DESTINATION_REQUIREMENT_ACCEPTED
TECHNICAL_CONTROL_CANDIDATE != LEGAL_TEXT
DESTINATION_ACCEPTANCE = NOT_RUN
POLICY_GUIDANCE != BINDING_DUTY
FUTURE_APPLICATION != CURRENT_MANDATORY_DUTY
```

## 2. Admission gate

A row may enter the R020 master matrix only when all of the following are true:

- the source/duty is already verified in an AI-LAWS controlled research unit;
- the authority layer is binding law or a binding regulation/statute within the bounded source state;
- the candidate does not strengthen the source into a broader legal obligation;
- actor and trigger/scope are preserved;
- temporal/application-state limitations are explicit;
- implementation evidence and technical-control fields are labelled as candidates, not statutory wording;
- destination acceptance remains `NOT_RUN`.

Nonbinding NIST guidance, policy briefs, withdrawn proposals, staff reports, model outputs and analogical case law are excluded from the legal-duty candidate rows in this bounded unit.

## 3. Required candidate fields

```text
CANDIDATE_ID
LEGAL_SOURCE_ID
LEGAL_DUTY_ID
JURISDICTION
AUTHORITY_CLASS
APPLICATION_STATE_2026_09_14
DUTY_BEARER
TRIGGER_SCOPE
REQUIREMENT_CANDIDATE
EVIDENCE_REQUIRED
TECHNICAL_CONTROL_CANDIDATE
PRIMARY_DESTINATION
LIMITATIONS
DESTINATION_ACCEPTANCE
SOURCE_RECORD_PATH
VERIFICATION_STATE
```

## 4. Destination meaning

- `ENGINEERING_OS`: architecture, lifecycle, governance, traceability, documentation, retention, auditability and operational evidence review.
- `OWASP`: security, adversarial testing, abuse resistance, cybersecurity, technical logging and control-verification review.
- `ETHICAL_AI`: human-facing transparency, agency, disclosure and literacy review.

These labels route review only. They do not represent acceptance by those repositories.

## 5. Temporal discipline

The matrix preserves the R003 phased-application architecture. In particular, high-risk AI core duties in Chapter III Sections 1–3 are not represented as universally current on 2026-09-14. Candidate controls may be useful before their legal application date, but early implementation usefulness is not a statement of current legal compulsion.

## 6. Exclusions

R020 does not:

- create destination-repository commits, issues, PRs or requirements;
- infer a private right of action;
- infer liability, breach, causation or damages;
- convert PLD disclosure/presumption rules into universal logging duties;
- convert FRCP preservation/discovery rules into universal pre-litigation retention mandates;
- convert Delaware analogical oversight cases into direct AI requirements;
- convert competition, state-systems or cross-border scope maps into universal system controls;
- start R019 incident research.

## 7. Outputs

- `79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_MASTER_REQUIREMENT_CANDIDATE_MATRIX_2026-09-14.csv`
- `79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_ENGINEERING_OS_REVIEW_PACKET_2026-09-14.csv`
- `79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_OWASP_REVIEW_PACKET_2026-09-14.csv`
- `79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_ETHICAL_AI_REVIEW_PACKET_2026-09-14.csv`
- `79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_SOURCE_AND_AUTHORITY_MATRIX_2026-09-14.csv`
- `79_CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_VALIDATION_SUMMARY_2026-09-14.csv`
- `95_RESEARCH/CROSS_REPO_REQUIREMENTS/AI-LAWS-R020_CLOSEOUT_2026-09-14.md`

```text
DESTINATION_ACCEPTANCE = NOT_RUN
DESTINATION_MUTATION = NO
UNKNOWN_PRESERVED = YES
AUTO_ADVANCE = NO
```
