# AI-LAWS — China AI / Data / Cyber Primary-Source Map

**WORK_ITEM:** `AI-LAWS-R008`
**RESEARCH_DATE:** 2026-09-14
**LEVEL:** L1 central primary-source baseline
**AUTHENTIC_LANGUAGE:** Chinese
**LEGAL_ADVICE:** NO
**AUTO_ADVANCE:** NO

## 1. Method and authority boundary

R008 uses central official Chinese sources only: the Cyberspace Administration of China, the State Council / China Government portal, and the National Laws and Regulations Database of the National People's Congress. Search engines are not legal authority. No unofficial English translation is promoted into authoritative text.

```text
OFFICIAL_CHINESE_PRIMARY_TEXT > UNOFFICIAL_TRANSLATION
SEARCH_RESULT != LEGAL_AUTHORITY
EFFECTIVE_DATE_VERIFIED != REPEAL_CHECK_COMPLETE
ADMINISTRATIVE_RULE != NATIONAL_STATUTE
REGULATORY_LAYER != UNIVERSAL_AI_CODE
```

## 2. Controlled eight-source baseline

The controlled source inventory is `CN_PRIMARY_SOURCE_INVENTORY_2026-09-14.csv`. It covers:

- `CN-001` algorithmic recommendation provisions — effective 2022-03-01;
- `CN-002` deep-synthesis provisions — effective 2023-01-10;
- `CN-003` interim generative-AI service measures — effective 2023-08-15;
- `CN-004` Personal Information Protection Law — NPC database current/effective; effective 2021-11-01;
- `CN-005` Data Security Law — NPC database current/effective; effective 2021-09-01;
- `CN-006` Cybersecurity Law current revised record — published 2025-10-28 and effective 2026-01-01;
- `CN-007` Network Data Security Management Regulation — effective 2025-01-01;
- `CN-008` AI-generated/synthetic-content labeling measure — effective 2025-09-01.

These instruments form a layered regulatory baseline; R008 does not infer a single comprehensive Chinese AI Act.

## 3. Current Cybersecurity Law correction

The NPC official database exact-title search returned a current Cybersecurity Law record with `bbbs=021e7d7684474107b8f3febbb1c4f8b5`, publication date 2025-10-28, effective date 2026-01-01 and status `sxx=3` (effective/current). The 2016 record is returned separately with `sxx=2` (modified). The official amendment decision is `bbbs=621d029681d4457ab5fc56ec7c7464a1`.

```text
CSL_2016_RECORD != CURRENT_2026_TEXT
CURRENT_CSL_BBBS = 021e7d7684474107b8f3febbb1c4f8b5
CURRENT_CSL_EFFECTIVE_DATE = 2026-01-01
```

## 4. Currentness and translation boundary

PIPL, Data Security Law and the current Cybersecurity Law were verified through the NPC database current-status layer. For the CAC/State-Council measures, official identity and commencement were verified, but R008 did not perform a separate exhaustive repeal/supersession search. They therefore remain tagged `CURRENTNESS_RECHECK_REQUIRED` before material future conclusions.

Authentic Chinese text controls. R008 does not create or certify an English legal translation. Any later English-language claim matrix must preserve the Chinese locator and recheck the exact provision.

## 5. Scope / territorial boundary

R008 maps central PRC source layers only. It does not determine Hong Kong or Macao law, cross-border conflicts, extraterritorial reach for a specific actor, sectoral licensing, enforcement practice, private rights of action, administrative penalty outcomes or case law.

## 6. Notebook routing

`CN-001..CN-008` are assigned to `NB05_ASIA_AND_COMPARATIVE` as URL-direct sources. No local binary, OCR, derived Markdown or Notebook upload was created in R008.

```text
NB05_CN_OFFICIAL_URL_SOURCE_SET = READY_8
NEW_BINARY_DOWNLOADS = 0
NOTEBOOK_UPLOADS = 0
DERIVED_MARKDOWN_CREATED = 0
CASE_LAW = NOT_ATTEMPTED
LIABILITY_CONCLUSION = NOT_ATTEMPTED
AUTO_ADVANCE = NO
```
