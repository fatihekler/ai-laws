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

### OECD

- `INT-005` OECD AI Principles (updated 2024)  
  https://www.oecd.org/en/topics/ai-principles.html  
  **Use state:** current official URL preferred; nonbinding recommendation.

### United Nations

- `INT-006` A/RES/78/265  
  https://digitallibrary.un.org/record/4043244/  
  **Use state:** official URL preferred.

- `INT-007` Pact for the Future / Global Digital Compact — A/RES/79/1 source family  
  https://www.un.org/pact-for-the-future/en  
  **R027 repository file state:** 64-page Summit of the Future outcome-document bundle verified; exact `A/RES/79/1` identifier is absent from the PDF, so use the adopted official source for primary resolution identity.

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
