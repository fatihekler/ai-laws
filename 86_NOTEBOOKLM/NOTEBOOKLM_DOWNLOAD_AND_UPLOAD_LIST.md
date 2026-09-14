# AI-LAWS — NotebookLM / Gemini Notebook Download and Upload List

**DOCUMENT_ID:** AI-LAWS-R021-NB-DOWNLOAD-LIST-1.1
**STATE:** CONTROLLED_SOURCE_ACQUISITION_LIST / R023_RECONCILED
**UPDATED:** 2026-09-14

This is the human-readable companion to `NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv`.

## IMPORTANT — existing repository binaries

The user manually uploaded PDF files under:

`86_NOTEBOOKLM/downloads/`

These binaries are now indexed by:

- `86_NOTEBOOKLM/downloads/README.md`
- `86_NOTEBOOKLM/downloads/DOWNLOADS_REGISTRY.csv`
- `86_NOTEBOOKLM/downloads/NOTEBOOK_UPLOAD_PLAN.md`
- `86_NOTEBOOKLM/PDF_CONTENT_IDENTITY_AND_DERIVED_TEXT_PROTOCOL.md`

Do not infer legal/source verification merely from binary presence or filename similarity.

```text
REPOSITORY_BINARY_PRESENT != CONTENT_IDENTITY_VERIFIED
PDF_FILENAME_MATCH != CURRENT_LAW_VERIFIED
NOTEBOOK_UPLOAD != LEGAL_VERIFICATION
```

Use `DOWNLOADS_REGISTRY.csv` as the source-by-source labeling/Notebook routing layer for the currently uploaded binaries.

The acquisition list remains divided into:

- **UPLOAD / INGEST AFTER IDENTITY CHECK** — binary or official URL exists but content/currentness/rights/pack checks still apply;
- **OFFICIAL URL PREFERRED** — dynamic/current/copyright-sensitive source should normally be ingested from the official URL;
- **HOLD / REPLACE** — do not use the repository binary as current primary source until the stated issue is resolved;
- **METADATA ONLY** — do not upload unlicensed full text.

## A. NB00 — AI-LAWS control and method

Upload directly from the repository:

1. `README_START_HERE.md`
2. `00_CONTROL/PROJECT_CHARTER.md`
3. `00_CONTROL/SOURCE_OF_TRUTH_AND_AUTHORITY.md`
4. `00_CONTROL/RESEARCH_MUTATION_AND_ACCEPTANCE_GATE.md`
5. `00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md`
6. `10_TAXONOMY/LEGAL_DOMAIN_TAXONOMY.csv`
7. `10_TAXONOMY/CLAIM_EVIDENCE_AND_AUTHORITY_CLASSES.md`
8. `30_CASE_LAW/CASE_LAW_CORPUS_SCHEMA.yaml`
9. `40_LIABILITY/AI_LIABILITY_CAUSATION_AND_REMEDY_TAXONOMY.md`
10. `50_RIGHTS/HUMAN_SOVEREIGNTY_COGNITIVE_LIBERTY_AND_DIGNITY_FRAME.md`
11. `60_INCIDENTS/INCIDENT_TO_LEGAL_ANALYSIS_SCHEMA.yaml`
12. `70_FINANCIAL_RESPONSIBILITY/AI_FINANCIAL_RESPONSIBILITY_RESEARCH_FRAME.md`
13. `80_CROSS_REPO/CROSS_REPO_AUTHORITY_AND_ROUTING.md`
14. `85_RESEARCH_ASSISTANTS/GROK_CHATGPT_COLLABORATION_PROTOCOL.md`
15. `85_RESEARCH_ASSISTANTS/MODEL_HANDOFF_CLAIM_SCHEMA.yaml`
16. `86_NOTEBOOKLM/NOTEBOOKLM_CORPUS_ARCHITECTURE.md`
17. `86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_ACQUISITION_POLICY.md`
18. `86_NOTEBOOKLM/PDF_CONTENT_IDENTITY_AND_DERIVED_TEXT_PROTOCOL.md`

NB00 teaches method. It is not proof of substantive law.

---

## B. NB01 — Global AI governance

R027 repository-binary validation state:

```text
INT-001 = CONTENT_IDENTITY_VERIFIED / TREATY_TEXT_SNAPSHOT / LIVE_STATUS_URL_REQUIRED
INT-002 = CONTENT_IDENTITY_VERIFIED
INT-003 = CONTENT_IDENTITY_VERIFIED
INT-004 = SUPERSEDED_SOURCE / CERTIFIED_COPY_URL_PRIMARY
INT-005 = CONTENT_IDENTITY_VERIFIED / OECD_RECOMMENDATION_PDF
INT-006 = CONTENT_IDENTITY_VERIFIED
INT-007 = CONTENT_IDENTITY_PARTIAL / OUTCOME_DOCUMENT_BUNDLE_NOT_EXACT_A_RES_79_1_FILE
INT-008 = CONTENT_IDENTITY_VERIFIED / OFFICIAL_URL_PREFERRED_DUE_RIGHTS_STATE
```

All eight have native searchable text layers; no Markdown derivative is required.

### Council of Europe

- `INT-001` CETS No.225
  https://www.coe.int/en/web/conventions/full-list?module=treaty-detail&treatynum=225
  **R027 repository file state:** verified 12-page treaty text. Live official URL remains required for current signatures, ratifications, reservations and declarations.

- `INT-002` CETS No.225 Explanatory Report
  https://rm.coe.int/1680afae67
  **Use state:** official URL preferred; PDF fallback after content check.

### UNESCO

- `INT-003` Recommendation on the Ethics of Artificial Intelligence (2021)
  https://unesdoc.unesco.org/ark:/48223/pf0000381137
  **Use state:** PDF eligible after content identity/licence check; nonbinding soft law.

- `INT-004` Recommendation on the Ethics of Neurotechnology
  **Current preferred certified-copy source:**
  https://unesdoc.unesco.org/ark:/48223/pf0000397812_eng
  **Use state:** official certified-copy URL preferred. The repository PDF derived from the 43rd General Conference resolutions source is a legacy source variant and must not be loaded as the current primary source.
  **R032 access state:** GitHub runner returned HTTP 403 on 2026-09-14; prior official certified-copy pin preserved; fresh R032 content-body verification not claimed while blocked.

### OECD

- `INT-005` OECD AI Principles (updated 2024)
  https://www.oecd.org/en/topics/ai-principles.html
  **Use state:** current official URL preferred; nonbinding recommendation.

### United Nations

- `INT-006` A/RES/78/265
  https://digitallibrary.un.org/record/4043244/
  **Use state:** official URL preferred.

- `INT-007` Pact for the Future / Global Digital Compact — A/RES/79/1
  **Official viewer:** https://docs.un.org/en/A/RES/79/1
  **Official PDF:** https://documents.un.org/doc/undoc/gen/n24/272/22/pdf/n2427222.pdf
  **R032 official PDF state:** 56 pages; 649956 bytes; SHA-256 `0c3968d0ce8d55cf107309794adea6879d70f9aea60e6d6d64e3a8da4b028336`; `A/RES/79/1`, Pact for the Future and Global Digital Compact markers verified.
  **Repository file state:** 64-page Summit outcome-document bundle remains `CONTENT_IDENTITY_PARTIAL` relative to the exact resolution and is supporting-only.

- `INT-008` Governing AI for Humanity — UN Advisory Body final report
  https://digitallibrary.un.org/record/4062495
  **Use state:** official URL preferred; do not assume public GitHub/Notebook redistribution rights from public accessibility alone.

### Risk-management reference

- `US-007` NIST AI RMF 1.0
  https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10

- `US-008` NIST GenAI Profile
  https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

These are voluntary framework/profile sources, not statutes.

---

## C. NB02 — European Union AI law

Preferred current-law ingestion: official EUR-Lex URL first; repository PDFs are versioned snapshots after content check.

- `EU-001` Current consolidated AI Act
  https://eur-lex.europa.eu/eli/reg/2024/1689
- `EU-002` Regulation (EU) 2026/1744 — Digital Omnibus on AI
  https://eur-lex.europa.eu/eli/reg/2026/1744/oj
- `EU-003` Directive (EU) 2024/2853 — Product Liability Directive
  https://eur-lex.europa.eu/eli/dir/2024/2853/oj
- `EU-004` Charter of Fundamental Rights
  https://eur-lex.europa.eu/eli/treaty/char_2016/oj/eng
- `EU-005` GDPR
  https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
- `EU-006` Digital Services Act
  https://eur-lex.europa.eu/eli/reg/2022/2065/oj/eng
- `EU-007` Data Act
  https://eur-lex.europa.eu/eli/reg/2023/2854
- `EU-008` Data Governance Act
  https://eur-lex.europa.eu/eli/reg/2022/868/oj/eng
- `EU-009` NIS 2
  https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng
- `EU-010` Cyber Resilience Act
  https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng

Before a current-law conclusion, verify the current consolidated/version/application state in EUR-Lex. A Directive must not be treated as identical domestic implementation in every Member State.

---


### R030 repository-PDF verification state

All ten `EU-001..EU-010` repository PDFs are native-searchable and exact-byte matches to the appropriate official EUR-Lex PDFs as rechecked on 2026-09-14. `EU-001` uses consolidated `CELEX:02024R1689-20260727`; directives and phased-application/currentness labels remain mandatory. No Notebook upload was performed by R030.

## D. NB03 — United States

R028 repository validation state:

```text
US-001 = CONTENT_IDENTITY_PARTIAL / WHITE_HOUSE_WEBPAGE_PRINT / LIVE_URL_PRIMARY
US-002 = CONTENT_IDENTITY_VERIFIED / EXACT_OFFICIAL_PDF
US-003 = CONTENT_IDENTITY_VERIFIED / EXACT_OFFICIAL_PDF
US-004 = CONTENT_IDENTITY_VERIFIED / EXACT_OFFICIAL_PDF
US-005 = CONTENT_IDENTITY_VERIFIED / FEDERAL_REGISTER_PDF_SNAPSHOT / EXACT_BYTE_NOT_RUN
US-006 = CONTENT_IDENTITY_VERIFIED / EXACT_OFFICIAL_PDF
US-007 = CONTENT_IDENTITY_VERIFIED / EXACT_NIST_DOI_PDF / REVISION_RECHECK_REQUIRED
US-008 = CONTENT_IDENTITY_VERIFIED / EXACT_NIST_DOI_PDF
```

All eight repository files have native searchable text layers; no Markdown derivative is required. For current executive-policy status use the live White House/OMB sources. NIST materials remain voluntary/nonbinding. Do not describe executive orders or OMB memoranda as Acts of Congress.

### State law

Do not build a definitive state-law notebook from memory. `AI-LAWS-R007` must pin current enacted/amended text state-by-state. `US-009` remains outside this R028 core-PDF unit and requires current Utah codification handling.

---


### R031 NB03 residual verification state

`US-005` is now an exact byte match to official GovInfo Federal Register document `2025-23092` (SHA-256 `5a557f9a153f1f40c7bd885b660ed81f1b26d55a6363b778943dfaa65565e0cb`). `US-001` remains a White House HTML print snapshot and supporting-only by design; exact-byte comparison is not applicable across HTML/PDF representations. NB03 official exact-byte count is therefore `7/8`, with the eighth source represented by a live official HTML URL plus supporting print snapshot. No Notebook upload was performed by R031.

## E. NB04 — Türkiye

Repository binaries now exist for:

- `TR-001` Constitution — No. 2709
- `TR-002` Law No. 6698 — Personal Data Protection
- `TR-003` Turkish Code of Obligations — No. 6098
- `TR-004` Turkish Civil Code — No. 4721
- `TR-005` Turkish Penal Code — No. 5237
- `TR-006` Consumer Protection Law — No. 6502
- `TR-007` Law No. 5651
- `TR-008` Cybersecurity Law — No. 7545

R026 subsequently verified repository content identity for all eight Türkiye PDFs, including native text layers, title/law-number checks and first/final pages. `TR-008` was confirmed to include Law No. 7590 effects effective 2026-07-31. These remain repository snapshots: live official Mevzuat exact-byte/currentness recheck is still required before material legal conclusions.

Official portals:

- https://www.mevzuat.gov.tr/
- https://www.resmigazete.gov.tr/

The YargıGPT API failure records are not court-law sources and must not be loaded as precedent.

---

## E2. NB05 — Asia and Comparative / China URL source set

R008 established an eight-source China primary-source baseline. Use official URLs directly; no repository binary set exists. Authentic Chinese text controls and translation/currentness caveats remain mandatory.

- `CN-001` https://www.cac.gov.cn/2022-01/04/c_1642894606364259.htm
- `CN-002` https://www.cac.gov.cn/2022-12/11/c_1672221949354811.htm
- `CN-003` https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm
- `CN-004` https://flk.npc.gov.cn/law-search/search/flfgDetails?bbbs=ff8081817b6472a3017b656cc2040044
- `CN-005` https://flk.npc.gov.cn/law-search/search/flfgDetails?bbbs=ff80818179f5e0800179f885c7e70392
- `CN-006` https://flk.npc.gov.cn/law-search/search/flfgDetails?bbbs=021e7d7684474107b8f3febbb1c4f8b5
- `CN-007` https://www.gov.cn/zhengce/content/202409/content_6977766.htm
- `CN-008` https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm

```text
NB05_CN_OFFICIAL_URL_SOURCE_SET = READY_8
REPOSITORY_BINARY_SET = NONE
NOTEBOOK_UPLOAD = NOT_RUN
PRIMARY_SOURCE_RECHECK_REQUIRED_BEFORE_MATERIAL_CLAIM = YES
```

---

## E3. NB05 — Comparative / United Kingdom URL source set

R009 established a 13-source official URL baseline for the United Kingdom. Use URL-direct ingestion. No dedicated repository binary set is created by R009.

- `GB-001` https://www.legislation.gov.uk/eur/2016/679/contents
- `GB-002` https://www.legislation.gov.uk/ukpga/2018/12/contents
- `GB-003` https://www.legislation.gov.uk/ukpga/2025/18/contents
- `GB-004` https://www.legislation.gov.uk/ukpga/2023/50/contents
- `GB-005` https://www.legislation.gov.uk/ukpga/2024/13/contents
- `GB-006` https://www.legislation.gov.uk/ukpga/2015/15/contents
- `GB-007` https://www.legislation.gov.uk/ukpga/1987/43/contents
- `GB-008` https://www.legislation.gov.uk/ukpga/2025/20/contents
- `GB-009` https://www.gov.uk/government/calls-for-evidence/ai-growth-lab
- `GB-010` https://www.gov.uk/government/publications/regulators-strategic-approaches-to-ai
- `GB-011` https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/
- `GB-012` https://www.gov.uk/cma-cases/ai-foundation-models-initial-review
- `GB-013` https://www.gov.uk/government/publications/ai-opportunities-action-plan-government-response

```text
NB05_UK_OFFICIAL_URL_SOURCE_SET = READY_13_WITH_LIMITS
BINDING_LAW_AND_POLICY_SEPARATED = YES
SECTION_LEVEL_CURRENTNESS_RECHECK_REQUIRED = YES
OFCOM_HUB = HTTP_403_GITHUB_RUNNER
REPOSITORY_BINARY_SET = NONE
NOTEBOOK_UPLOAD = NOT_RUN
```

Do not use enactment date as universal commencement. Do not treat AI Growth Lab, ICO/CMA material or government policy papers as statutes. Do not import the EU AI Act as UK domestic law.

---

## F. NB06 — Human sovereignty / neurotechnology

Primary source set:

- `INT-003` UNESCO AI Ethics Recommendation;
- `INT-004` UNESCO Neurotechnology **certified-copy official URL**;
- `EU-004` EU Charter official URL;
- `EU-005` GDPR official URL;
- `CL-001` Chile Ley 21.383 official BCN source after currentness check;
- `CL-002` Girardi/Emotiv only when the case-law full-text gate is satisfied.

Do not generalize Chile neurotechnology law into a universal right governing all AI mental-state inference.

---

## G. NB07 — Liability / evidence / financial responsibility

Start with verified/rechecked versions of:

- `EU-003` Product Liability Directive;
- relevant current AI Act logging/incident provisions from `EU-001`;
- `EU-005` GDPR where material;
- `US-003` / `US-004` OMB governance/procurement memoranda;
- `US-007` / `US-008` NIST sources for nonbinding comparison.

Keep separate:

```text
CURRENT LAW
COMMERCIAL MARKET PRACTICE
REGULATORY GUIDANCE
ACADEMIC PROPOSAL
POLICY PROPOSAL
```

---

## H. NB08 — Frontier AI incident evidence

R029 repository/source validation state:

```text
INC-001 = CONTENT_IDENTITY_PARTIAL / OPENAI_REPOSITORY_TECHNICAL_REPORT / OFFICIAL_URL_403_RECHECK_BLOCKED
INC-002 = CONTENT_IDENTITY_VERIFIED / EXACT_METR_ORIGINAL_PDF / INDEPENDENT_INVESTIGATION
INC-003 = CONTENT_IDENTITY_VERIFIED / EXACT_ANTHROPIC_OFFICIAL_PDF / VENDOR_THREAT_INTELLIGENCE
INC-004 = CONTENT_IDENTITY_PARTIAL / AUTHOR_WEBPAGE_PRINT / POLICY_FORECAST_CONTEXT / NOT_INCIDENT
```

All four PDFs have native searchable text; no Markdown derivative is required. The core evidentiary pair remains `INC-001` + `INC-002`, but they are not equal authority and the OpenAI repository report remains source-partial until its official source can be rechecked. `INC-003` is vendor attribution; `INC-004` is optional policy context only.

---

## I. Documents that should NOT be blindly uploaded

- paid ISO/IEC 42001 full text without valid licence;
- paid ISO/IEC 23894 full text without valid licence;
- Westlaw/Lexis/commercial database exports outside licence terms;
- attorney-client privileged material;
- personal/private incident data;
- security secrets;
- unreleased internal logs;
- classified/export-controlled material;
- model-generated reports disguised as primary sources.

---

## J. Existing-PDF validation and upload procedure

For every repository PDF:

1. map file to `SOURCE_ID` via `downloads/DOWNLOADS_REGISTRY.csv`;
2. follow `PDF_CONTENT_IDENTITY_AND_DERIVED_TEXT_PROTOCOL.md`;
3. verify official/current source state;
4. choose upload mode from `downloads/NOTEBOOK_UPLOAD_PLAN.md`;
5. use `recommended_notebook_label` when practical;
6. use `recommended_canonical_filename` for a local upload copy if renaming is useful;
7. upload pack-by-pack, not all at once;
8. run Notebook source identity/locator test;
9. run authority-separation test;
10. recheck material claims against primary/official sources.

Do **not** convert every PDF to Markdown. Use direct PDF/official URL ingestion first; create derived Markdown only when extraction quality, diffing or locator requirements justify it.

`AUTO_ADVANCE = NO`

## R033 — TR-009 current Türkiye AI policy source


- `TR-009` — **Türkiye Yapay Zekâ Eylem Planı (2026-2030)**
  Official strategy-document index: https://www.sanayi.gov.tr/plan-program-raporlar-ve-yayinlar/strateji-belgeleri
  Official release announcement (13 June 2026): https://www.sanayi.gov.tr/medya/haber/turkiye-yapay-zek%C3%A2-eylem-plani-aciklandi
  **Authority:** `OFFICIAL_GUIDANCE` / national policy-action plan.
  **Binding state:** nonbinding policy source; **not statute**.
  **Ingest:** `URL_DIRECT_PREFERRED`.
  **R033 binary state:** exact official PDF body was not exposed to the GitHub runner; SHA-256/byte size remain `UNKNOWN`; no repository binary was vendored.
  **Historical boundary:** 2021-2025 strategy and 2024-2025 action-plan sources remain historical context and must not replace the current 2026-2030 plan.

### R010 — NB05 Republic of Korea + Japan official URL source set

R010 adds URL-direct sources only; no binary download is required for this bounded unit.

- `KR-001` Korea AI Basic Act current official law.go.kr state
- `KR-002` Korea AI Basic Act Enforcement Decree current official law.go.kr state
- `KR-003` Korea PIPA current official law.go.kr state
- `JP-001` Japan AI Act current e-Gov law
- `JP-002` Japan APPI current e-Gov law
- `JP-003` Japan AI Basic Plan Phase II, Cabinet decision 2026-07-14
- `JP-004` Japan AI appropriateness guideline, Headquarters decision 2025-12-19
- `JP-005` Japan AI Guidelines for Business Ver.1.2, current MIC page 2026-03-31

```text
NB05_R010_OFFICIAL_URL_SOURCE_SET = READY_8_WITH_LIMITS
KR_BINDING_SOURCES = 3
KR_SEPARATE_CURRENT_POLICY_PLAN_SOURCE = NOT_PINNED_R010
JP_BINDING_SOURCES = 2
JP_POLICY_GUIDANCE_SOURCES = 3
BINDING_LAW_AND_POLICY_GUIDANCE_SEPARATED = YES
NEW_BINARY_DOWNLOADS = 0
NOTEBOOK_UPLOADS = 0
AUTO_ADVANCE = NO
```
