# AI-LAWS / HSA — NotebookLM Investigation Master Instruction

**DOCUMENT_ID:** AI-LAWS-HSA-NBLM-MASTER-2026-09-15
**STATE:** PROPOSAL / SUPPORTING RESEARCH CONTROL
**CANONICAL:** NO
**PRIMARY OWNER:** AI-LAWS for legal-source verification; Engineering OS for cross-repo reconciliation
**AUTO_ADVANCE:** NO

NotebookLM is a source-grounded synthesis workspace. It is not legal authority, a court, a regulator, an engineering acceptance system, or a replacement for destination-repository review.

## 1. Mandatory source routing

Use `86_NOTEBOOKLM/NOTEBOOK_UPLOAD_SELECTION.csv` as the source-selection/routing authority for Notebook packs.

Never treat the entire `downloads/` directory as automatically authoritative.

Required boundaries include:
- `CL-002` = HOLD; official full text unavailable; do not admit as verified case law;
- `INT-004` legacy 43GC PDF = not current primary; use certified-copy URL;
- `INC-004` = policy/context only; not incident evidence;
- Türkiye snapshots = usable for research with live official currentness recheck before material legal conclusions;
- `INC-001` = official company incident statement / verified exact-byte report; incident != liability;
- ISO/technical-standard full text = metadata/citation only unless lawfully available/licensed.

## 2. Notebook packs

```text
NB00 = Method / Authority / Research Rules
NB01 = Global AI Governance / Treaties / International Instruments
NB02 = European Union AI Law
NB03 = United States AI Law
NB04 = Türkiye AI Law
NB05 = China / UK / Japan / Korea Comparative Law
NB06 = Human Sovereignty / Neurodata / Cognitive Liberty / Dignity
NB07 = Liability / Evidence / Financial Responsibility
NB08 = Frontier AI Incidents
NB09 = Cross-Repo Standards / Requirement Inputs
```

Do not collapse packs into a single undifferentiated corpus if source selection can be controlled.

## 3. Non-equivalence firewall

```text
NOTEBOOK_OUTPUT != VERIFIED_FACT
NOTEBOOK_OUTPUT != LEGAL_AUTHORITY
MODEL_AGREEMENT != INDEPENDENT_VERIFICATION
QUESTION != FINDING
FINDING != REQUIREMENT
ETHICAL_CONCERN != LEGAL_VIOLATION
INCIDENT != LIABILITY
PUBLIC_WARNING != ACTOR_SPECIFIC_LEGAL_KNOWLEDGE
SOFT_LAW != BINDING_LAW
GUIDANCE != STATUTE
POLICY_PROPOSAL != CURRENT_LAW
SEARCH_FAILURE != NO_CASE
UNKNOWN != SAFE
```

## 4. Per-source execution protocol

When NotebookLM lets the operator select one source/file, interrogate that source by itself before cross-source synthesis.

For each source create one `RUN-YYYYMMDD-###` execution record and answer the following stages.

### S1 — Identity / authority
1. What exact document is this? Give title, issuing institution, document/law/case number, publication/adoption date and visible version date.
2. What is the source's authority class: constitution, statute/regulation, treaty, binding decision, regulatory guidance, soft law, official framework, company statement, independent reporting, policy proposal, technical standard, or other?
3. Is the source itself binding? If binding only in a limited scope, state exactly what limits are visible in the source.
4. Does the source itself show an effective/application/commencement date? Do not infer one from publication date.
5. Identify visible amendment, repeal, supersession, transition, territorial, actor or sector limits.
6. Return exact source locators: article/section/page/paragraph/table/heading.

### S2 — Definitions / scope / actors
1. Which actors are defined or addressed?
2. Which systems, products, services, data or conduct are in scope?
3. What exclusions, exceptions, thresholds or territorial rules apply?
4. What terms are explicitly defined and which concepts are NOT defined by the source?

### S3 — Rights / duties / safeguards
1. Which rights, protections, duties, prohibitions, governance obligations, documentation duties, human-oversight duties, transparency duties, cybersecurity duties or redress mechanisms are stated?
2. For each duty, identify exact actor + exact locator + conditions.
3. Do not convert recommendations or principles into mandatory duties.

### S4 — HSA threat relevance
For each relevant threat family, return only source-supported links:
`THR-001..THR-024`.
State `NO_EXPLICIT_SUPPORT_FOUND_IN_SELECTED_SOURCE` when the source does not support the mapping.

### S5 — Evidence / accountability
1. What records, logs, notices, assessments, documentation, audit material, incident reports or proof would be relevant to evaluating compliance or breach under this source?
2. What elements remain missing before any liability or violation conclusion?
3. What defences, exceptions, immunities, limitations or safe harbours are visible?

### S6 — Unknown / conflict
Return:
- explicit ambiguity;
- translation limitation;
- currentness limitation;
- scope limitation;
- conflict with another loaded source if visible;
- information the source does not establish.

### S7 — Engineering relevance
Only as a candidate, state which technical/organizational control or test might operationalize a source-supported duty.
Mark every such item `CONTROL_CANDIDATE` / `TEST_CANDIDATE`; never claim implementation/effectiveness.

## 5. Source-type-specific overlays

Apply the common S1–S7 protocol plus the matching overlay in `HSA_NOTEBOOKLM_SOURCE_TYPE_QUESTION_MATRIX_2026_09_15.csv`.

Special priorities:
- Constitution/rights text: scope-of-application, state-action/implementation boundary, remedies and balancing limits.
- Statute/regulation: actor, duty, exact article, dates, exemptions, delegated/secondary rules, enforcement.
- Treaty/international instrument: signature/ratification/entry-into-force/declarations/reservations/territorial effect.
- Court decision: court, docket, procedural posture, facts, issue, holding, reasoning, remedy, binding/precedential scope; no corpus admission without official full text.
- Guidance/soft law/framework: recommendation vs duty; intended audience; relationship to binding law.
- Incident statement/report: observed fact vs attribution vs hypothesis; access limits; causation/damage/liability not inferred.
- Policy proposal: current policy proposal vs enacted law; forecast/opinion separated from fact.
- Standard: metadata/scope/conformity claim limits; standard compliance != legal compliance.

## 6. Pack-level synthesis

After per-source interrogation, run the questions in `HSA_NOTEBOOKLM_PACK_QUESTION_MATRIX_2026_09_15.csv` with the entire pack selected.

Pack synthesis MUST compare sources rather than average them.

Every material statement must identify one or more source IDs and locators.

## 7. Cross-pack synthesis

Only after pack outputs exist, compare packs for:
- actor-role differences;
- jurisdiction/date-state differences;
- human-sovereignty protections;
- liability/evidence differences;
- incident-to-duty gaps;
- current-law vs proposal gaps;
- missing remedies;
- missing technical assurance obligations;
- source conflicts and open unknowns.

Cross-pack synthesis is supporting research only.

## 8. Mandatory output record schema

Each normalized Notebook record must contain:

```text
record_id
run_id
notebook_pack
qualified_source_id
source_id
question_id
question
answer
source_locators
jurisdiction
authority_class
binding_state
date_state
actor
right_or_interest
duty_or_prohibition
evidence_state
known
unknown
conflict
limitations
primary_source_recheck_required
threat_ids
control_candidate
test_candidate
destination_repo
promotion_state
review_owner
notes
```

For admitted AI-LAWS sources use qualified IDs such as `REPO-LAW::EU-001`.
Do not invent an HSA legal `SOURCE_ID`.

## 9. Required output artifacts

Notebook work should produce/export the following files, preferably CSV for row data and MD for narrative synthesis:

```text
NBLM_RUN_MANIFEST.csv
NBLM_SOURCE_IDENTITY_AND_AUTHORITY_MATRIX.csv
NBLM_ACTOR_DUTY_RIGHTS_MATRIX.csv
NBLM_HSA_THREAT_SOURCE_CROSSWALK.csv
NBLM_EVIDENCE_REQUIREMENT_MATRIX.csv
NBLM_EXCEPTION_DEFENCE_MATRIX.csv
NBLM_CONFLICT_UNKNOWN_REGISTER.csv
NBLM_CASE_CANDIDATE_MATRIX.csv
NBLM_CONTROL_TEST_CANDIDATES.csv
NBLM_PACK_SYNTHESIS_NB01.md ... NBLM_PACK_SYNTHESIS_NB09.md
NBLM_CROSS_PACK_GAP_SYNTHESIS.md
```

If NotebookLM cannot directly export the required schema, copy the answer into a raw MD/TXT export and let ChatGPT Work normalize it; preserve the raw output unchanged.

## 10. Promotion states

Notebook outputs begin only as:

```text
QUESTION
SUPPORTING_RESEARCH
FINDING_CANDIDATE
```

NotebookLM may never assign:

```text
VERIFIED_FINDING
ACCEPTED_REQUIREMENT
PASS
LEGAL_VIOLATION
LIABILITY_ESTABLISHED
```

Those require downstream verification/authorization.

## 11. Stop conditions

STOP/mark HOLD when:
- selected source identity is uncertain;
- source locator cannot be produced;
- currentness materially affects the answer;
- translation/authentic-language gap is material;
- court full text is not official/authorized;
- pack contains conflicting versions that cannot be distinguished;
- the question requires evidence not in the selected sources;
- the requested conclusion would exceed the source.

`AUTO_ADVANCE = NO`
