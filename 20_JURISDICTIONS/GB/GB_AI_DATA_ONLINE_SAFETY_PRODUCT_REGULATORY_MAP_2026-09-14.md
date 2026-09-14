# AI-LAWS — United Kingdom Sectoral AI / Data / Online Safety / Product Regulatory Map

**WORK_ITEM:** `AI-LAWS-R009`
**RESEARCH_DATE:** 2026-09-14
**LEVEL:** L1/L2 sectoral source architecture baseline
**JURISDICTION_ID:** `GB` (repository identifier for United Kingdom)
**LEGAL_ADVICE:** NO
**AUTO_ADVANCE:** NO

## 1. Authority and method

R009 uses official UK sources only for the controlled baseline: `legislation.gov.uk`, GOV.UK, the Information Commissioner's Office and the Competition and Markets Authority. Ofcom's online-safety hub was probed but returned HTTP 403 to the GitHub runner; this is an access blocker, not evidence that the source or duties do not exist.

```text
EU_AI_ACT != UK_DOMESTIC_AI_STATUTE
POLICY_PROPOSAL != CURRENT_LAW
REGULATOR_GUIDANCE != STATUTE
ENACTMENT_DATE != UNIVERSAL_COMMENCEMENT_DATE
LATEST_AVAILABLE_REVISED != EVERY_PROVISION_CURRENTLY_IN_FORCE
SEARCH_FAILURE != NO_RULE
```

## 2. Controlled source baseline

The controlled inventory is `GB_PRIMARY_SOURCE_INVENTORY_2026-09-14.csv` and contains 13 official URL sources:

- `GB-001` UK GDPR;
- `GB-002` Data Protection Act 2018;
- `GB-003` Data (Use and Access) Act 2025;
- `GB-004` Online Safety Act 2023;
- `GB-005` Digital Markets, Competition and Consumers Act 2024;
- `GB-006` Consumer Rights Act 2015;
- `GB-007` Consumer Protection Act 1987;
- `GB-008` Product Regulation and Metrology Act 2025;
- `GB-009` AI Growth Lab call for evidence;
- `GB-010` Regulators' strategic approaches to AI;
- `GB-011` ICO Artificial Intelligence guidance hub;
- `GB-012` CMA AI Foundation Models initial review;
- `GB-013` AI Opportunities Action Plan: government response.

The first eight are binding-law source records. `GB-009..GB-013` are policy/regulator sources and must not be converted into statutory duties.

## 3. Binding-law layer

Official `legislation.gov.uk` identity and the `Latest available (Revised)` representation were verified for `GB-001..GB-008`. XML enactment-date attributes were separately verified:

```text
GB-001 = 2016-04-27
GB-002 = 2018-05-23
GB-003 = 2025-06-19
GB-004 = 2023-10-26
GB-005 = 2024-05-24
GB-006 = 2015-03-26
GB-007 = 1987-05-15
GB-008 = 2025-07-21
```

R009 does **not** infer commencement/application of every provision from these enactment dates. The official legislation pages expose changes/currentness/commencement material; exact section-level date state remains a later gate.

## 4. AI-governance policy and regulator layer

`GB-009` is a closed call for evidence for the proposed AI Growth Lab. Its official text describes targeted regulatory modifications under safeguards and monitoring. It is a **proposal/policy-development source**, not enacted law.

`GB-010` records strategic AI approaches requested from key regulators and is useful for mapping the sectoral regulator architecture, but it is not itself a statute.

`GB-011` is the ICO's official AI hub. It is regulator guidance and points to AI/decision-explanation/data-protection materials. The underlying UK GDPR/DPA provisions remain the legal authority.

`GB-012` is the CMA's official Foundation Models review page. It is regulatory/competition context, not a court holding or standalone binding AI law.

`GB-013` is a government AI policy paper. Later 2025/2026 regulation-policy materials also exist, so R009 does not freeze the 2025 Action Plan response as the sole current AI-regulation policy.

A 2026 GOV.UK page titled `Response to the AI Growth Lab call for evidence` was inspected and **not** promoted into the government-policy baseline: its body identifies it as the Biometrics and Surveillance Camera Commissioner's response to the call for evidence, not the government's own adoption decision.

## 5. Online safety and Ofcom limitation

The Online Safety Act source identity is verified. The Ofcom online-safety hub returned HTTP 403 from the GitHub Actions runner during R009. Therefore:

```text
OFCOM_HUB_ACCESS_STATE = HTTP_403_GITHUB_RUNNER
OFCOM_GUIDANCE_CURRENTNESS = NOT_VERIFIED_R009
OFCOM_ACCESS_FAILURE != NO_OFCOM_RULES
```

Provision-specific Online Safety Act duties, Ofcom codes/guidance, commencement regulations and enforcement procedure require a separate current-source recheck.

## 6. Product / consumer limitation

The Consumer Rights Act 2015, Consumer Protection Act 1987 and Product Regulation and Metrology Act 2025 establish relevant source layers. R009 does not decide whether any AI model, software, service or output is a product, digital content, service, unsafe product or defective product, and does not infer liability.

## 7. Territorial and devolution boundary

Repository jurisdiction ID `GB` labels the United Kingdom profile, but R009 does not assume every provision has identical territorial extent or effect across England and Wales, Scotland and Northern Ireland. Provision-specific extent, devolved competence and Northern-Ireland interfaces remain open where material.

## 8. Negative-findings boundary

R009 did not add a comprehensive UK AI statute to the controlled source set. This is **not** a definitive negative-law finding that no such law, bill, sector rule or later instrument exists.

```text
BOUNDED_SOURCE_MAP != EXHAUSTIVE_NEGATIVE_LEGAL_FINDING
NO_CONTROLLED_GENERAL_AI_ACT_SOURCE != NO_AI_LAW
```

## 9. Notebook routing

`GB-001..GB-013` are routed to `NB05_ASIA_AND_COMPARATIVE` for URL-direct ingestion. No repository binary, OCR derivative or Notebook upload is created by R009.

```text
NB05_UK_OFFICIAL_URL_SOURCE_SET = READY_13_WITH_LIMITS
NEW_BINARY_DOWNLOADS = 0
DERIVED_MARKDOWN_CREATED = 0
NOTEBOOK_UPLOADS = 0
CASE_LAW = NOT_ATTEMPTED
LIABILITY_CONCLUSION = NOT_ATTEMPTED
AUTO_ADVANCE = NO
```
