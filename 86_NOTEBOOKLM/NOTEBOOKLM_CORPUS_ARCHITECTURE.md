# AI-LAWS — NotebookLM / Gemini Notebook Corpus Architecture

**DOCUMENT_ID:** AI-LAWS-R021-NB-CORPUS-ARCH-1.0  
**STATE:** RESEARCH_SUPPORT_ARCHITECTURE  
**DATE:** 2026-09-13  
**AUTO_ADVANCE:** NO

## 1. Objective

Use NotebookLM / Gemini Notebook as a controlled, source-grounded synthesis layer for AI law research without converting model output into legal authority.

The architecture separates:

```text
LEGAL_SOURCE
INCIDENT_EVIDENCE
MODEL_SYNTHESIS
CROSS_REPO_ANALYSIS
```

because mixing these classes in one unstructured notebook creates false equivalence.

## 2. Notebook families

### NB00 — AI-LAWS CONTROL AND METHOD

Purpose: teach the notebook the project taxonomy and evidence rules.

Recommended sources:

- `README_START_HERE.md`
- `00_CONTROL/PROJECT_CHARTER.md`
- `00_CONTROL/SOURCE_OF_TRUTH_AND_AUTHORITY.md`
- `00_CONTROL/RESEARCH_MUTATION_AND_ACCEPTANCE_GATE.md`
- `10_TAXONOMY/CLAIM_EVIDENCE_AND_AUTHORITY_CLASSES.md`
- `10_TAXONOMY/LEGAL_DOMAIN_TAXONOMY.csv`
- `30_CASE_LAW/CASE_LAW_CORPUS_SCHEMA.yaml`
- `40_LIABILITY/AI_LIABILITY_CAUSATION_AND_REMEDY_TAXONOMY.md`
- `50_RIGHTS/HUMAN_SOVEREIGNTY_COGNITIVE_LIBERTY_AND_DIGNITY_FRAME.md`
- `60_INCIDENTS/INCIDENT_TO_LEGAL_ANALYSIS_SCHEMA.yaml`
- `70_FINANCIAL_RESPONSIBILITY/AI_FINANCIAL_RESPONSIBILITY_RESEARCH_FRAME.md`
- `80_CROSS_REPO/CROSS_REPO_AUTHORITY_AND_ROUTING.md`
- `85_RESEARCH_ASSISTANTS/GROK_CHATGPT_COLLABORATION_PROTOCOL.md`
- `85_RESEARCH_ASSISTANTS/MODEL_HANDOFF_CLAIM_SCHEMA.yaml`

NB00 is methodology-only. It should not be used to prove substantive legal claims.

### NB01 — GLOBAL AI GOVERNANCE

Purpose: international/treaty/soft-law and global governance comparison.

Priority sources:

- Council of Europe CETS No. 225 and Explanatory Report;
- current signatures/ratifications/reservations/declarations;
- UNESCO Recommendation on the Ethics of AI (2021);
- UNESCO Recommendation on the Ethics of Neurotechnology (2025);
- OECD AI Principles (updated 2024);
- UN GA A/RES/78/265;
- Pact for the Future / Global Digital Compact (A/RES/79/1);
- UN Advisory Body `Governing AI for Humanity`;
- NIST AI RMF and GenAI Profile as nonbinding technical/risk frameworks.

### NB02 — EUROPEAN UNION AI LAW

Purpose: binding EU AI/data/cyber/product-liability law plus carefully separated implementation/guidance.

Core sources:

- current consolidated EU AI Act;
- Regulation (EU) 2026/1744 Digital Omnibus on AI;
- Directive (EU) 2024/2853 Product Liability;
- Charter of Fundamental Rights;
- GDPR;
- Digital Services Act;
- Data Act;
- Data Governance Act;
- NIS 2;
- Cyber Resilience Act;
- Commission/AI Office implementation material only when separately labeled `GUIDANCE/IMPLEMENTATION`.

Do not assume a Directive has identical domestic effect in every Member State without transposition research.

### NB03 — UNITED STATES AI LAW

Purpose: federal/state split, agency authority, procurement/government AI, consumer/civil-rights/product/tort overlays.

Initial federal core:

- Executive Order 14179 (2025);
- America’s AI Action Plan (2025);
- OMB M-25-21;
- OMB M-25-22;
- Executive Order 14365 (2025);
- NIST AI RMF / GenAI Profile;
- relevant FTC/agency material once R007 verifies currentness and legal effect.

State sources such as Utah/Colorado/Texas/California must enter only after current official-law verification under R007.

### NB04 — TÜRKİYE AI LAW

Purpose: primary Turkish law baseline and later verified case law.

Initial source families to be verified under R005:

- Constitution;
- Law No. 6698 (KVKK);
- Turkish Code of Obligations No. 6098;
- Turkish Civil Code No. 4721;
- Turkish Penal Code No. 5237;
- Consumer Protection Law No. 6502;
- Law No. 5651;
- Cybersecurity legislation including Law No. 7545 if current official text is verified;
- relevant KVKK Board decisions/guidance;
- current AI strategy/action-plan documents as `POLICY`, not statute;
- verified case-law records only after case-law admission gate.

YargıGPT interruption records are research-history evidence and should not be treated as case-law sources.

### NB05 — ASIA AND COMPARATIVE

Separate sub-notebooks are preferred if source count grows.

Candidate jurisdictions:

- China;
- Republic of Korea;
- Japan;
- Singapore;
- India;
- UAE;
- Saudi Arabia.

Only upload primary/current sources after the relevant jurisdiction research item verifies source identity, translation status and binding state.

### NB06 — HUMAN SOVEREIGNTY / NEUROTECH / DIGNITY

Purpose: cognitive liberty, mental privacy, neurodata, biometric/emotion inference, dignity, autonomy, appeal, opt-out and reversibility.

Core source families:

- UNESCO Neurotechnology Recommendation;
- UNESCO AI Ethics Recommendation;
- Chile neurorights constitutional/legal material and verified decisions;
- relevant international human-rights instruments;
- EU Charter/GDPR where applicable;
- verified scholarship as a separate lower-authority layer.

Do not invent a universal named right merely because scholarship uses a term.

### NB07 — LIABILITY / EVIDENCE / FINANCIAL RESPONSIBILITY

Purpose: actor allocation, duty/breach/causation/damage/remedy, evidence preservation, insurance and compensation architecture.

Sources:

- EU Product Liability Directive;
- national tort/product/consumer rules when verified;
- procedural/evidence rules;
- insurance/financial-assurance sources;
- catastrophe-fund/CAT-bond proposals clearly marked `POLICY_PROPOSAL`.

### NB08 — FRONTIER AI INCIDENTS

Purpose: factual incident chronology and evidence-gap analysis.

Source classes may include:

- official company incident disclosures;
- independent security/evaluation investigations;
- regulator/law-enforcement records;
- credible reporting;
- denials and competing accounts.

Do not use an incident notebook to declare legal liability.

### NB09 — CROSS-REPO REQUIREMENTS

Purpose: translate verified legal duties into destination-neutral candidate requirements.

Inputs:

- verified AI-LAWS source records;
- Engineering OS interface/control vocabulary;
- OWASP threat/control vocabulary;
- Ethical-AI human-agency vocabulary;
- Esmaul Husna reminder interface only where source-reviewed and human-facing;
- Apesteori challenge vocabulary.

Output remains `CANDIDATE` until each destination repository accepts it under its own governance.

## 3. Source-count discipline

Google's current standard/free limit is 50 sources per notebook. Design for 35–40 routine sources, leaving 10–15 slots for amendments, cases and challenge sources.

If a pack approaches the limit:

- split by jurisdiction or legal domain;
- do not concatenate unrelated laws merely to save slots;
- avoid duplicate language copies unless comparison requires them;
- keep current and superseded versions distinct when temporal analysis matters.

## 4. Primary-source preference

Preferred order:

```text
AUTHENTIC_CURRENT_PRIMARY_LEGAL_TEXT
> OFFICIAL_CONSOLIDATED_TEXT
> OFFICIAL COURT / REGULATOR MATERIAL
> OFFICIAL GUIDANCE
> VERIFIED SCHOLARSHIP / SECONDARY SOURCE
> REPORTING
> MODEL SYNTHESIS
```

A consolidated legal text may include a disclaimer that the authentic OJ version controls. Record that distinction.

## 5. Temporal model

Every legal notebook should answer two time questions:

- **business/legal time**: when did the rule/event apply?
- **research/system time**: when did AI-LAWS retrieve and verify it?

Minimum source metadata:

```text
SOURCE_ID
DOCUMENT_ID
JURISDICTION
AUTHORITY_CLASS
ADOPTION_DATE
PUBLICATION_DATE
ENTRY_INTO_FORCE_DATE
APPLICATION_DATE
AMENDMENT_STATE
CONSOLIDATED_VERSION_DATE
RETRIEVAL_DATE
SOURCE_URL
LANGUAGE
AUTHENTIC_LANGUAGE_STATE
```

## 6. No circular model evidence

Primary-law notebooks should not contain Grok/ChatGPT/Notebook outputs as evidence sources.

If model outputs are uploaded for critique, use a separate notebook or clearly isolated source group and prefix filenames:

`MODEL_SUPPORTING_ONLY__...`

## 7. Notebook output schema

Ask Notebook to return:

```text
NB_FINDING_ID
SOURCE_IDS
CLAIM
SOURCE_LOCATORS
AUTHORITY_CLASS
JURISDICTION
DATE_STATE
AGREEMENT
CONFLICT
UNKNOWN
LIMITATION
POSSIBLE_AI_LAWS_DESTINATION
CANONICAL = FALSE
```

## 8. Refresh triggers

Re-import or re-verify a source when:

- an amendment/corrigendum is published;
- a new consolidated version appears;
- a Directive reaches/changes transposition state;
- treaty ratification/reservation/declaration changes;
- court/regulator interpretation changes a material claim;
- the notebook source is more than the assigned freshness window old;
- a material Grok/ChatGPT challenge identifies possible staleness.

## 9. Stop rule

Notebook answers may identify candidate legal conclusions but may not close AI-LAWS legal gates.

```text
NOTEBOOK_SYNTHESIS = SUPPORTING_RESEARCH
HUMAN_LEGAL_REVIEW = REQUIRED_WHEN_MATERIAL
AUTO_ADVANCE = NO
```
