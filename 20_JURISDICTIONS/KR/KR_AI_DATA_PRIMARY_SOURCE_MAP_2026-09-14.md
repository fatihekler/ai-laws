# AI-LAWS — Republic of Korea AI / Data Primary-Source Map

**WORK_ITEM:** `AI-LAWS-R010`
**RESEARCH_DATE:** 2026-09-14
**LEVEL:** L1/L2 current-source and binding-state baseline
**LEGAL_ADVICE:** NO
**AUTO_ADVANCE:** NO

## Controlled source set

R010 admits three official current `law.go.kr` sources:

- `KR-001` — `인공지능 발전과 신뢰 기반 조성 등에 관한 기본법`;
- `KR-002` — `인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 시행령`;
- `KR-003` — `개인정보 보호법`.

All three current detail pages exposed `nwYn=Y`. Exact current identifiers/date selectors are preserved in `KR_PRIMARY_SOURCE_INVENTORY_2026-09-14.csv`.

## Current-state controls

```text
KR001_LSID = 014820
KR001_LSISEQ = 282791
KR001_CURRENT_WRAPPER_SELECTOR = 2026-07-21
KR001_CURRENT_REVISION_ANCNO = 21311
KR001_CURRENT_REVISION_ANCYD = 2026-01-20
KR001_BODY_BASE_EFFECT_SIGNAL = 2026-01-22
KR001_AMENDMENT_CHAIN_NORMALIZED = NO
KR002_LSISEQ = 288781
KR002_CURRENT_SELECTOR = 2026-08-20
KR003_LSISEQ = 283839
KR003_CURRENT_SELECTOR = 2026-09-11
```

The 2026-07-21 selector and 2026-01-22 body signal for `KR-001` are not collapsed into one universal commencement date. `ancNo=21311` is recorded as current-revision metadata and is not represented as the original enactment number.

## Binding / policy boundary

`KR-001..KR-003` are binding-law sources. R010 did not pin a separate current Korean national AI policy-plan source to the same verification standard.

```text
KOREA_CURRENT_AI_POLICY_PLAN_SOURCE = NOT_PINNED_R010
BINDING_LAW_SOURCE_VERIFIED != POLICY_PLAN_SOURCE_VERIFIED
```

This open policy-source lane does not reduce the verified identity of the three binding sources and does not establish that no current Korean AI policy exists.

## Translation and legal-conclusion boundary

Authentic Korean text controls. R010 did not admit an authoritative English translation as primary legal authority.

```text
TRANSLATION_CONTROL = AUTHENTIC_KOREAN_PRIMARY_TEXT
SOURCE_IDENTITY != DUTY_APPLICATION
DUTY_APPLICATION != BREACH
BREACH != CAUSATION
CASE_LAW = NOT_ATTEMPTED
LIABILITY_CONCLUSION = NOT_ATTEMPTED
NOTEBOOK_UPLOADS = 0
NEW_BINARY_DOWNLOADS = 0
AUTO_ADVANCE = NO
```
