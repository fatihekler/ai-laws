# AI-LAWS — MASTER RESEARCH, SOURCE ACQUISITION AND NOTEBOOK ORCHESTRATION

**DOCUMENT_ID:** AI-LAWS-MASTER-ORCHESTRATION-1.0  
**DATE:** 2026-09-13  
**REPOSITORY:** `fatihekler/ai-laws`  
**BRANCH:** `main`  
**STATE:** MASTER_CONTROL_INSTRUCTION  
**LEGAL_ADVICE:** NO  
**MODEL_OUTPUT_CANONICAL:** NO  
**AUTO_ADVANCE:** NO

## 1. Mission

AI-LAWS exists to build a source-verifiable, jurisdiction-aware, temporally current corpus for AI-related law, rights, duties, prohibitions, evidence, case law, liability, remedies, sanctions, financial responsibility, national-security exceptions and unresolved legal gaps.

The system must preserve the difference between:

```text
LAW
CASE LAW
TREATY
REGULATORY GUIDANCE
SOFT LAW
STANDARD
POLICY
SCHOLARSHIP
INCIDENT EVIDENCE
ALLEGATION
MODEL SYNTHESIS
UNKNOWN
```

AI-LAWS is not a court, regulator, law firm or substitute for licensed legal counsel.

## 2. Non-negotiable rules

```text
MODEL_OUTPUT != LEGAL_AUTHORITY
NOTEBOOK_OUTPUT != LEGAL_AUTHORITY
GROK_OUTPUT != LEGAL_AUTHORITY
YARGIGPT_OUTPUT != COURT_DECISION
MULTIPLE_MODELS_AGREE != FACT_PROVEN
SEARCH_FAILURE != NO_CASE
ALLEGATION != VIOLATION
INCIDENT != LIABILITY
HARM != AUTOMATIC_CAUSATION
PUBLIC_KNOWLEDGE != ACTOR_SPECIFIC_LEGAL_KNOWLEDGE
ANALOGICAL_PRECEDENT != DIRECT_AI_PRECEDENT
POLICY_PROPOSAL != CURRENT_LAW
SOFT_LAW != BINDING_LAW
STANDARD != STATUTE
UNKNOWN != NO_RISK
```

## 3. Source-of-truth order

```text
CURRENT_AUTHENTIC_PRIMARY_LEGAL_SOURCE / COURT / TREATY / REGULATOR
>
CURRENT_AI_LAWS_GITHUB_STATE_AND_VERIFIED_SOURCE_RECORDS
>
CURRENT_VERIFIED_SECONDARY_LEGAL_SOURCE
>
CURRENT_VERIFIED_INCIDENT_EVIDENCE
>
CURRENT_CROSS_REPO_EVIDENCE_OR_PROPOSAL
>
GROK / CHATGPT / NOTEBOOKLM / YARGIGPT OUTPUT
>
CHAT MEMORY
```

No lower layer may silently override a higher layer.

## 4. Mandatory continuity sequence for every new AI-LAWS chat

Before research or mutation:

1. Fresh-read `main` HEAD and TREE.
2. Read `README_START_HERE.md`.
3. Read `00_CONTROL/NEW_CHAT_BOOTSTRAP.md`.
4. Read this MASTER file.
5. Read `00_CONTROL/PROJECT_CHARTER.md`.
6. Read `00_CONTROL/SOURCE_OF_TRUTH_AND_AUTHORITY.md`.
7. Read `00_CONTROL/RESEARCH_MUTATION_AND_ACCEPTANCE_GATE.md`.
8. Read `00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md`.
9. Read `10_TAXONOMY/LEGAL_DOMAIN_TAXONOMY.csv`.
10. Read `10_TAXONOMY/CLAIM_EVIDENCE_AND_AUTHORITY_CLASSES.md`.
11. Read `20_JURISDICTIONS/JURISDICTION_RESEARCH_REGISTRY.csv`.
12. Read `20_JURISDICTIONS/GLOBAL_JURISDICTION_RESEARCH_PROTOCOL.md`.
13. Read `85_RESEARCH_ASSISTANTS/GROK_CHATGPT_COLLABORATION_PROTOCOL.md` if Grok is involved.
14. Read `86_NOTEBOOKLM/NOTEBOOKLM_CORPUS_ARCHITECTURE.md` if NotebookLM/Gemini Notebook is involved.
15. Read `86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_ACQUISITION_POLICY.md` before downloading/uploading any external source.
16. Read `86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv`.
17. Read `86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_PACK_ASSIGNMENTS.csv`.
18. Read `90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv`.
19. Read the exact jurisdiction/domain/case-law/incident files relevant to the bounded unit.
20. Fresh-read HEAD/TREE again before mutation; unexplained overlapping drift is a blocker.

## 5. Bounded-unit rule

One user command authorizes at most one registered bounded unit unless the gate explicitly states otherwise.

```text
USER_SAYS_CONTINUE != UNLIMITED_AUTO_ADVANCE
BROAD_RESEARCH != AUTOMATIC_CANONICALIZATION
AUTO_ADVANCE = NO
```

## 6. Global coverage objective

The long-term target is not a single static list of laws. It is an enumerated and refreshable legal coverage graph across:

- sovereign states;
- supranational unions;
- treaty systems;
- territories and special regions when legally material;
- federal/state/provincial/subnational systems when legally material;
- sector regulators;
- courts and tribunals;
- data protection, competition, consumer, cyber, product, civil, criminal, administrative, labour, health, children, election/information-integrity, national-security and financial-responsibility layers.

A jurisdiction is not considered researched merely because its country name appears in a registry.

Each jurisdiction must progress through the state machine below.

## 7. Jurisdiction state machine

```text
J0_DISCOVERED
→ J1_OFFICIAL_AUTHORITY_MAP
→ J2_PRIMARY_SOURCE_PINNED
→ J3_CURRENTNESS_VERIFIED
→ J4_SOURCE_ACQUIRED_OR_URL_INGEST_READY
→ J5_NOTEBOOK_PACK_LOADED
→ J6_NOTEBOOK_SOURCE_LOCATORS_TESTED
→ J7_CLAIM_MATRIX_EXTRACTED
→ J8_INDEPENDENT_RECHECKED
→ J9_HUMAN_REVIEW_READY
→ J10_ACCEPTED_RESEARCH_BASELINE
→ J11_REFRESH_MONITORED
```

No jurisdiction may skip directly from `J0` to `J10`.

## 8. Source-acquisition state machine

Every material document receives a `SOURCE_ID` and moves through:

```text
S0_CANDIDATE
→ S1_OFFICIAL_IDENTITY_VERIFIED
→ S2_AUTHORITY_CLASSIFIED
→ S3_CURRENTNESS_AND_DATE_STATE_VERIFIED
→ S4_RIGHTS_AND_USE_STATE_VERIFIED
→ S5_ACQUISITION_METHOD_SELECTED
→ S6_DOWNLOADED_OR_URL_INGEST_READY
→ S7_HASHED_IF_LOCAL_FILE
→ S8_CONTENT_IDENTITY_CHECKED
→ S9_NOTEBOOK_ASSIGNED
→ S10_NOTEBOOK_LOADED
→ S11_NOTEBOOK_LOCATOR_TESTED
→ S12_ANALYSIS_ELIGIBLE
→ S13_REFRESH_DUE / CURRENT
```

### Required source metadata

```text
SOURCE_ID
TITLE
DOCUMENT_ID
JURISDICTION
ISSUING_AUTHORITY
AUTHORITY_CLASS
BINDING_STATE
ADOPTION_DATE
PUBLICATION_DATE
ENTRY_INTO_FORCE_DATE
APPLICATION_DATE
CONSOLIDATED_VERSION_DATE
AMENDMENT_STATE
AUTHENTIC_LANGUAGE
TRANSLATION_STATE
OFFICIAL_URL
RETRIEVAL_DATE
PREFERRED_INGEST
RIGHTS_OR_USE_STATE
LOCAL_FILENAME
SHA256
BYTE_SIZE
CONTENT_TYPE
NOTEBOOK_PACK
VERIFICATION_STATE
REFRESH_TRIGGER
NOTES
```

## 9. Authority classes

At minimum use:

```text
CONSTITUTIONAL_TEXT
STATUTE_OR_REGULATION
DIRECTIVE_OR_FRAMEWORK_LAW
TREATY_OR_INTERNATIONAL_INSTRUMENT
BINDING_COURT_DECISION
REGULATORY_DECISION
REGULATORY_GUIDANCE
OFFICIAL_STANDARD_OR_FRAMEWORK
SOFT_LAW_RECOMMENDATION
OFFICIAL_COMPANY_STATEMENT
INDEPENDENT_REPORTING
SCHOLARLY_ANALYSIS
POLICY_PROPOSAL
ALLEGATION
MODEL_GENERATED_SUPPORTING_RESEARCH
UNKNOWN
```

If a source does not fit confidently, preserve `UNKNOWN` and create a clarification task.

## 10. Acquisition-method selection

Permitted acquisition states:

- `URL_DIRECT_PREFERRED` — use current official URL in Notebook when stable and accessible.
- `PDF_DOWNLOAD_ALLOWED` — public official PDF may be downloaded for controlled research use.
- `MANUAL_DOWNLOAD_REQUIRED` — portal/session/manual retrieval needed; record exact source identity afterward.
- `OFFICIAL_SOURCE_NEEDS_VERIFICATION` — do not ingest until exact official source/currentness is pinned.
- `PAYWALLED_DO_NOT_VENDOR` — metadata/reference only unless a valid license authorizes full-text use.

Never bypass access controls, paywalls, copyright restrictions, robots restrictions, authentication or technical protections.

## 11. Download procedure

For every `PDF_DOWNLOAD_ALLOWED` or lawfully downloadable local file:

1. Open the official source page first.
2. Confirm document ID/title/issuing authority.
3. Confirm date/version/currentness.
4. Confirm rights/use state.
5. Download from the official host.
6. Preserve meaningful original filename or rename as:
   `SOURCE_ID__JURISDICTION__DOCUMENT_ID__VERSIONDATE.ext`.
7. Compute SHA-256.
8. Record byte size and content type.
9. Open the file and confirm it contains the expected document.
10. Record retrieval timestamp and final URL.
11. If the source is amended/consolidated dynamically, record that the local copy is a snapshot.
12. Add/update the acquisition manifest/ledger.
13. Only then mark `S8_CONTENT_IDENTITY_CHECKED`.

A file hash proves file identity, not legal authenticity.

## 12. URL-direct procedure

For `URL_DIRECT_PREFERRED`:

1. Confirm the official host.
2. Confirm current document identity.
3. Confirm the page is stable enough for Notebook ingestion.
4. Record currentness/retrieval date.
5. Add to the correct Notebook source pack.
6. After ingestion, ask Notebook to return exact title/document ID/source locator.
7. Compare Notebook's returned identity to the manifest.
8. If mismatch or partial ingestion occurs, mark `NOTEBOOK_SOURCE_MISMATCH` and do not analyze the source until corrected.

## 13. NotebookLM / Gemini Notebook architecture

Use separate source packs, not one giant notebook:

```text
NB00 = AI-LAWS CONTROL AND METHOD
NB01 = GLOBAL AI GOVERNANCE
NB02 = EUROPEAN UNION AI LAW
NB03 = UNITED STATES AI LAW
NB04 = TÜRKİYE AI LAW
NB05 = ASIA AND COMPARATIVE
NB06 = HUMAN SOVEREIGNTY / NEUROTECH / DIGNITY
NB07 = LIABILITY / EVIDENCE / FINANCIAL RESPONSIBILITY
NB08 = FRONTIER AI INCIDENTS
NB09 = CROSS-REPO REQUIREMENTS
```

Use `86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_PACK_ASSIGNMENTS.csv` as the routing table.

## 14. Notebook capacity and source hygiene

Notebook/Gemini limits are product-dependent and changeable. Before a large batch, verify current Google documentation.

At the 2026-09-13 verification point, standard access supports up to 50 sources per notebook; individual sources may contain up to 500,000 words, and local uploaded files may be up to 200 MB. Keep working packs below the hard limit to reserve slots for amendments, cases and challenge sources.

Do not upload a document if you do not have the rights required for the intended use.

## 15. Notebook upload sequence

For each notebook pack:

### Phase N1 — Pack preparation

- read the pack assignment table;
- select only `S8_CONTENT_IDENTITY_CHECKED` or verified URL-direct sources;
- remove superseded duplicate versions unless temporal comparison requires them;
- keep binding law and lower-authority materials visibly labeled;
- exclude secrets, privileged material, personal/private incident data, classified/export-controlled material and unlicensed commercial full text.

### Phase N2 — Upload/ingest

- upload files or add official URLs;
- preserve `SOURCE_ID` in the source title where practical;
- record Notebook name, upload date and source count;
- do not exceed current product limits.

### Phase N3 — Source-identity verification

Before asking substantive legal questions, ask Notebook to produce:

```text
SOURCE_ID
SOURCE_TITLE
DOCUMENT_ID
JURISDICTION
AUTHORITY_CLASS
DATE_VISIBLE_IN_SOURCE
LOCATOR_OR_SECTION
INGESTION_LIMITATION
```

Compare this output to the GitHub manifest.

Any mismatch => `NOTEBOOK_SOURCE_MISMATCH` and STOP substantive use of that source.

### Phase N4 — Authority separation test

Ask Notebook to separate:

```text
BINDING LAW
COURT/REGULATOR DECISION
GUIDANCE
SOFT LAW
STANDARD
POLICY
SCHOLARSHIP
INCIDENT EVIDENCE
ALLEGATION
```

If it collapses these categories, refine source labels/prompts before continuing.

### Phase N5 — Substantive extraction

Use the question catalog and produce claim-level records with:

```text
NB_FINDING_ID
SOURCE_IDS
CLAIM
SOURCE_LOCATORS
AUTHORITY_CLASS
JURISDICTION
LEGAL_DATE_STATE
ACTOR_ROLE
DUTY_OR_RIGHT
LIMITATION
CONFLICT
UNKNOWN
POSSIBLE_DESTINATION
CANONICAL = FALSE
```

### Phase N6 — Independent recheck

Notebook citations are pointers, not final verification.

For every material claim:

- reopen the primary/official source;
- verify the quoted/relied-on provision or holding;
- check currentness/effective date;
- check whether Notebook omitted a limitation, exception or scope condition;
- check authentic-language/translation issues;
- record `VERIFIED / PARTIAL / CONFLICT / UNKNOWN`.

Only rechecked claims may enter AI-LAWS verified research records.

## 16. Notebook output import to GitHub

Notebook output enters GitHub as supporting research, never as primary authority.

Required import header:

```text
NOTEBOOK_OUTPUT_CLASS = SUPPORTING_RESEARCH
NOTEBOOK_NAME
NOTEBOOK_RUN_DATE
SOURCE_PACK_VERSION
SOURCE_IDS_USED
MODEL_OUTPUT_CANONICAL = NO
PRIMARY_SOURCE_RECHECK_REQUIRED = YES
```

Material claims that pass independent recheck may then be represented in the jurisdiction/domain evidence matrix with source pointers.

## 17. Grok collaboration sequence

Use Grok for adversarial challenge, horizon scanning and counterevidence, not canonicalization.

Sequence:

```text
AI-LAWS CLAIM / QUESTION
→ GROK CHALLENGE
→ GROK SOURCE POINTERS
→ CHATGPT / HUMAN SOURCE VERIFICATION
→ NOTEBOOK SOURCE-GROUNDED COMPARISON IF USEFUL
→ PRIMARY-SOURCE RECHECK
→ AI-LAWS EVIDENCE RECORD
```

Never use Grok to prove its own prior claim.

For every Grok task use:

- `85_RESEARCH_ASSISTANTS/GROK_READY_TO_PASTE_MASTER_INSTRUCTION.txt`
- `85_RESEARCH_ASSISTANTS/GROK_RESEARCH_QUERY_CATALOG.md`
- `85_RESEARCH_ASSISTANTS/MODEL_HANDOFF_CLAIM_SCHEMA.yaml`

## 18. Case-law protocol

No case enters the case corpus without verified full text from an official court/authorized source when the project policy requires official verification.

Required states:

```text
DIRECTLY_RELEVANT
ANALOGICAL_PRECEDENT
NOT_RELEVANT
UNKNOWN
```

For analogical cases, `ANALOGOUS_ELEMENT` and `ANALOGY_LIMIT` are mandatory.

Repeated official API failure without new information must become a blocker/reroute, not an infinite retry loop.

## 19. Legal-claim chain

For liability-related analysis, keep separate:

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

No missing element may be silently inferred.

## 20. Incident-to-law protocol

```text
INCIDENT FACT
→ SOURCE CLASS
→ TECHNICAL EVENT
→ AFFECTED ACTORS
→ POSSIBLE LEGAL DOMAINS
→ POSSIBLE DUTIES
→ EVIDENCE REQUIRED
→ CAUSATION QUESTIONS
→ DAMAGE QUESTIONS
→ REMEDY QUESTIONS
```

`POSSIBLE` is not a legal finding.

## 21. Human sovereignty / cognitive liberty protocol

Research terms such as dignity, autonomy, cognitive liberty, mental privacy, neurodata, emotion inference, manipulation, appeal, opt-out and reversibility must be tied to specific jurisdictions and sources.

Do not invent a universal named right because scholarship or model outputs use a term.

## 22. Financial responsibility protocol

Keep separate:

```text
CURRENT MANDATORY LAW
CURRENT COMMERCIAL INSURANCE PRACTICE
REGULATORY GUIDANCE
ACADEMIC PROPOSAL
POLICY PROPOSAL
INDUSTRY PROPOSAL
UNKNOWN MARKET CAPACITY
```

Do not represent catastrophe funds, mandatory insurance, CAT bonds, pools or developer reserves as existing legal requirements unless verified for the jurisdiction.

## 23. Cross-repo routing

AI-LAWS owns legal/accountability research only.

- OWASP: technical threats/controls/tests.
- Engineering OS: requirements/V&V/evidence.
- Ethical-AI: dignity/agency/appeal/reversibility/meaningful human control.
- Esmaul Husna: source-reviewed human-facing moral/theological reminders only.
- Apesteori: multidimensional challenge, conflict and unknown discovery.

```text
TRANSFER = EVIDENCE_OR_PROPOSAL
TRANSFER != AUTHORITY
```

## 24. Human legal-review gate

Human legal review is required before:

- legal advice-like conclusions;
- litigation/regulatory filing language;
- accusations of legal breach/crime/cartel conduct;
- material jurisdiction-specific action recommendations;
- final liability allocation;
- relying on unsettled case-law analogies for consequential decisions.

## 25. Refresh and expiry controls

A source becomes `REFRESH_DUE` when:

- a law/regulation is amended or corrected;
- a new consolidated version appears;
- an application/effective date passes;
- a directive reaches transposition deadline;
- treaty signatures/ratifications/reservations/declarations change;
- court/regulator interpretation changes a material claim;
- an official page moves or is replaced;
- a material challenge suggests staleness;
- the assigned freshness window expires.

Never assume a Notebook copy is current merely because it remains accessible.

## 26. Required status ledger after every bounded unit

Record:

```text
UNIT_ID
BASE_HEAD
FINAL_HEAD
JURISDICTION
SOURCE_IDS_TOUCHED
NEW_SOURCES
UPDATED_SOURCES
DOWNLOADS_COMPLETED
HASHES_RECORDED
NOTEBOOK_PACK
NOTEBOOK_UPLOADS
NOTEBOOK_SOURCE_CHECKS
CLAIMS_EXTRACTED
CLAIMS_RECHECKED
CONFLICTS
UNKNOWNS
HUMAN_REVIEW_REQUIRED
NEXT_BOUNDED_UNIT
AUTO_ADVANCE = NO
```

## 27. Stop conditions

STOP if:

- official source/currentness cannot be verified;
- rights/use state is unclear;
- authentic text is unavailable and translation is material;
- Notebook source identity mismatches;
- case full text cannot be verified;
- actor identity is disputed;
- legal effective/application date is unresolved;
- the same failed search is repeating without information gain;
- a requested conclusion requires facts not in evidence;
- overlapping GitHub drift is unexplained;
- a new bounded unit would be required.

## 28. Completion definition

A legal source pack is not complete merely because files were uploaded.

Minimum completion requires:

```text
SOURCE_IDENTITIES_VERIFIED = YES
AUTHORITY_CLASSES_VERIFIED = YES
CURRENTNESS_VERIFIED = YES
RIGHTS_STATE_VERIFIED = YES
ACQUISITION_LOGGED = YES
NOTEBOOK_SOURCE_IDENTITY_TESTED = YES
NOTEBOOK_AUTHORITY_SEPARATION_TESTED = YES
MATERIAL_CLAIMS_PRIMARY_SOURCE_RECHECKED = YES
UNKNOWNS_PRESERVED = YES
LEGAL_ADVICE = NO
```

## 29. Final invariants

```text
LEGAL_ADVICE = NO
MODEL_OUTPUT_CANONICAL = NO
NOTEBOOK_OUTPUT_CANONICAL = NO
GROK_OUTPUT_CANONICAL = NO
UNKNOWN_PRESERVED = YES
SOURCE_CURRENTNESS_REQUIRED = YES
COPYRIGHT_AND_LICENSE_RESPECTED = YES
AUTO_ADVANCE = NO
```
