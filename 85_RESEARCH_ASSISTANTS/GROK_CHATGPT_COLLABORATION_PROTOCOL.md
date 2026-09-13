# AI-LAWS — GROK ↔ CHATGPT COLLABORATION PROTOCOL

**DOCUMENT_ID:** AI-LAWS-R021-GROK-CHATGPT-PROTOCOL-1.0  
**STATE:** RESEARCH_COORDINATION_PROTOCOL  
**DATE:** 2026-09-13  
**CANONICAL_LEGAL_AUTHORITY:** NO  
**AUTO_ADVANCE:** NO

## 1. Purpose

This protocol allows Grok and ChatGPT to contribute to `fatihekler/ai-laws` without creating circular model authority, duplicate legal conclusions, or cross-project state contamination.

- **Grok**: adversarial horizon scanner, public-source challenger, current-events and public-statement researcher, counter-hypothesis generator.
- **ChatGPT**: repository steward for the current bounded AI-LAWS task, source-classification/reconciliation layer, GitHub evidence writer when explicitly authorized.
- **Gemini Notebook / NotebookLM**: closed/source-grounded synthesis workspace over an explicitly curated source pack.
- **YargıGPT or other specialist legal search tools**: specialist source-discovery tools only; their outputs require source verification.
- **Human legal reviewer**: required before project-level legal advice-like conclusions, litigation/regulatory submissions, or material jurisdiction-specific action recommendations.

None of these roles has judicial, legislative, regulatory, or automatic canonical authority.

## 2. Non-equivalence rules

```text
GROK_OUTPUT != LEGAL_AUTHORITY
CHATGPT_OUTPUT != LEGAL_AUTHORITY
NOTEBOOK_OUTPUT != LEGAL_AUTHORITY
YARGIGPT_OUTPUT != COURT_DECISION
MODEL_A_CONFIRMS_MODEL_B != INDEPENDENT_VERIFICATION
MULTIPLE_MODELS_AGREE != FACT_PROVEN
PUBLIC_STATEMENT != LAW
INCIDENT != LIABILITY
ALLEGATION != VIOLATION
POLICY_PROPOSAL != CURRENT_LAW
UNKNOWN != NO_RISK
```

## 3. Circular-citation firewall

A model may not cite another model's synthesis as proof of the underlying claim.

Valid chain:

```text
MODEL_OUTPUT
→ SOURCE_POINTERS
→ PRIMARY/OFFICIAL/INDEPENDENT_SOURCE
→ VERIFIED CLAIM RECORD
```

Invalid chain:

```text
GROK says X
→ ChatGPT summarizes Grok
→ Notebook cites ChatGPT summary
→ Grok cites Notebook
→ "three systems confirmed X"
```

If a model-generated artifact is loaded into Notebook for critique, label it:

```text
SOURCE_CLASS = MODEL_GENERATED_SUPPORTING_RESEARCH
CANONICAL = FALSE
MAY_NOT_PROVE_UNDERLYING_FACT = TRUE
```

## 4. Claim-first workflow

Every material claim should receive a stable research claim ID before reconciliation.

Minimum claim fields:

```text
CLAIM_ID
TASK_ID
CLAIM_TEXT
JURISDICTION
ACTOR
EVENT_DATE_OR_LEGAL_DATE
CLAIM_TYPE
PROPOSED_AUTHORITY_CLASS
SOURCE_URLS
SOURCE_DATE
CURRENTNESS_DATE
KNOWN
UNKNOWN
CONFLICT
GROK_POSITION
CHATGPT_VERIFICATION_STATE
NOTEBOOK_SUPPORT_STATE
HUMAN_REVIEW_STATE
CANONICAL = FALSE
```

## 5. Grok task rules

Grok should be asked to:

1. challenge the claim rather than confirm it;
2. find the strongest primary/official source first;
3. find a credible contradictory or limiting source where available;
4. separate current law, court decision, official guidance, company statement, reporting, scholarly analysis, policy proposal, allegation and inference;
5. identify exact effective/application dates;
6. identify jurisdiction and actor-role limitations;
7. identify national-security/defence/state exemptions where material;
8. identify unresolved causation and evidence gaps;
9. preserve denials and competing factual accounts;
10. report when a prior Grok statement was wrong, overstated, stale or unsupported.

Grok must not be asked to make repository mutations, legal filings, accusations of crime/cartel conduct, or definitive liability findings from incomplete facts.

## 6. ChatGPT reconciliation rules

When receiving Grok output, ChatGPT should:

- fresh-read the current AI-LAWS GitHub state before a mutation task;
- decompose the output into claim-level records;
- independently retrieve material current sources when feasible;
- prefer official/authentic current legal text over model summaries;
- distinguish source fact from model inference;
- register material conflicts instead of silently choosing a preferred narrative;
- create append-only research first;
- update current pointers/queues only when the bounded unit explicitly allows it;
- stop before guilt, breach, liability, criminal responsibility, regulatory violation or legal-advice conclusions unless a separate human-review gate authorizes them.

## 7. Notebook/Gemini Notebook role

Notebook is for source-grounded comparison and synthesis.

Primary-law notebooks should contain primary/official sources plus AI-LAWS control/method documents. Model-generated answers should not be included by default.

Recommended Notebook output classes:

- source concordance;
- disagreement/conflict table;
- duty/actor matrix;
- date/effective-state timeline;
- jurisdiction comparison;
- evidence-gap list;
- research-question list;
- claim-to-source locator table.

Notebook output is imported to AI-LAWS only as supporting research until separately verified.

## 8. Handoff packet: ChatGPT → Grok

Each request should contain:

```text
TASK_ID
AI_LAWS_BASE_HEAD
SCOPE
JURISDICTIONS
DATE_CUTOFF
CLAIM_IDS
SOURCE_POLICY
KNOWN_SOURCES
QUESTIONS
REQUIRED_COUNTEREVIDENCE
OUTPUT_SCHEMA
FORBIDDEN_INFERENCES
STOP_CONDITION
```

Do not send secrets, privileged legal material, personal data, closed incident evidence or unrelated repository state.

## 9. Handoff packet: Grok → ChatGPT

Required sections:

```text
A. CORRECTIONS_TO_PRIOR_OUTPUT
B. WELL_ESTABLISHED
C. PLAUSIBLE_NOT_PROVEN
D. POLICY_PROPOSALS
E. DISPUTED_OR_CONFLICTING
F. UNKNOWN
G. CLAIM_ROWS
H. PRIMARY_SOURCE_POINTERS
I. CONTRARY_OR_LIMITING_SOURCES
J. REQUIRED_EXPERTISE
K. NEXT_VERIFICATION
```

Each claim row should include:

```text
CLAIM_ID
SOURCE_URL
SOURCE_TYPE
AUTHORITY_CLASS
EVIDENCE_CLASS
DATE
JURISDICTION
KNOWN
UNKNOWN
CONFLICT
CURRENT_LAW_OR_PROPOSAL
CONFIDENCE
```

## 10. News/social-source discipline

```text
SOCIAL_POST = STATEMENT_EVIDENCE, NOT LEGAL_TRUTH
NEWS_REPORT = REPORTING_EVIDENCE, NOT COURT_FINDING
COMPANY_BLOG = OFFICIAL_COMPANY_STATEMENT, NOT INDEPENDENT_PROOF
```

For material legal claims, route from reporting to primary/official law or official docket/decision where possible.

## 11. Cross-repo routing

AI-LAWS owns legal/accountability research only.

- OWASP: technical threat/control/test evidence.
- Engineering OS: requirement/control/test/evidence and V&V.
- Ethical-AI: dignity, agency, appeal, reversibility, meaningful human control.
- Esmaul Husna: source-reviewed human-facing moral/theological reminders only.
- Apesteori: multidimensional challenge, conflict/unknown discovery.

```text
TRANSFER = EVIDENCE_OR_PROPOSAL
TRANSFER != AUTHORITY
```

## 12. Stop rules

Stop and preserve `UNKNOWN` when:

- current legal text cannot be verified;
- material effective dates are unclear;
- official case full text is unavailable;
- actor identity is disputed;
- allegations are not independently corroborated;
- the same failed search is being repeated without new information;
- the requested conclusion would require facts not in evidence.

## 13. Exact protocol state

```text
GROK_ROLE = ADVERSARIAL_SUPPORTING_RESEARCHER
CHATGPT_ROLE = REPOSITORY_STEWARD_AND_RECONCILER_WHEN_AUTHORIZED
NOTEBOOK_ROLE = SOURCE_GROUNDED_SYNTHESIS
MODEL_OUTPUT_CANONICAL = NO
CIRCULAR_MODEL_CITATION = PROHIBITED
LEGAL_ADVICE = NO
AUTO_ADVANCE = NO
```
