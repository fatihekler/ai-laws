# AI-LAWS — Japan AI / Policy / Data Primary-Source Map

**WORK_ITEM:** `AI-LAWS-R010`
**RESEARCH_DATE:** 2026-09-14
**LEVEL:** L1/L2 current-source and binding-state baseline
**LEGAL_ADVICE:** NO
**AUTO_ADVANCE:** NO

## Controlled source set

R010 admits five official Japanese sources:

- `JP-001` — AI Act, `人工知能関連技術の研究開発及び活用の推進に関する法律`;
- `JP-002` — APPI, `個人情報の保護に関する法律`;
- `JP-003` — `人工知能基本計画（第Ⅱ期）`;
- `JP-004` — AI R&D/use appropriateness guideline;
- `JP-005` — `AI事業者ガイドライン Ver.1.2`.

## Binding-law layer

Official e-Gov structured data verified:

```text
JP001_LAW_ID = 507AC0000000053
JP001_LAW_NUMBER = 令和七年法律第五十三号
JP001_PROMULGATED = 2025-06-04
JP001_CURRENT_REVISION_EFFECTIVE = 2025-09-01
JP001_CURRENT_REVISION_STATUS = CurrentEnforced
JP001_FULL_EFFECTIVE = 2025-09-01
JP002_LAW_ID = 415AC0000000057
JP002_ORIGINAL_LAW_NUMBER = 平成十五年法律第五十七号
JP002_CURRENT_REVISION_EFFECTIVE = 2026-07-17
JP002_CURRENT_REVISION_STATUS = CurrentEnforced
```

Cabinet Office independently states the AI Act was partially effective from 2025-06-04 and fully effective from 2025-09-01.

## Policy and guidance layer

```text
JP003_AI_BASIC_PLAN_PHASE_II_CABINET_DECISION = 2026-07-14
JP004_APPROPRIATENESS_GUIDELINE_HEADQUARTERS_DECISION = 2025-12-19
JP005_AI_GUIDELINES_FOR_BUSINESS_VERSION = 1.2
JP005_CURRENT_PAGE_DATE = 2026-03-31
JP005_MIC_ACCESS = HTTP_200
JP005_METI_COUNTERPART_ACCESS = HTTP_403_GITHUB_RUNNER
```

`JP-003..JP-005` are not statutes. The Cabinet Office current hub distinguishes the Act, the Phase II Basic Plan and guideline layers. The MIC page for Business Guidelines Ver.1.2 was reachable; the METI counterpart returned 403 from the runner, which is an access state rather than source absence.

## Translation and legal-conclusion boundary

Authentic Japanese text controls for legal meaning. Official English titles/links do not replace Japanese primary text unless a source is expressly authoritative for that purpose.

```text
POLICY_PLAN != STATUTE
OFFICIAL_GUIDANCE != STATUTE
RUNNER_HTTP_403 != SOURCE_ABSENCE
SOURCE_IDENTITY != DUTY_APPLICATION
CASE_LAW = NOT_ATTEMPTED
LIABILITY_CONCLUSION = NOT_ATTEMPTED
NOTEBOOK_UPLOADS = 0
NEW_BINARY_DOWNLOADS = 0
AUTO_ADVANCE = NO
```
