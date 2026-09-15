# AI-LAWS / HSA — APPROVED SINGLE-SOURCE NOTEBOOKLM FORMAT

**DATE:** 2026-09-15  
**STATE:** APPROVED WORKING FORMAT / NONCANONICAL UNTIL PR ACCEPTANCE  
**PILOT:** `86_NOTEBOOKLM/downloads-notebooklm/AI-LAWS__EU__EU-001 v2/`  
**MODE:** SINGLE_SOURCE  
**CANONICAL:** FALSE  
**AUTO_ADVANCE:** NO

## 1. APPROVED DELIVERY MODEL

Each selected source should normally produce exactly **two deliverables**:

1. one multi-tab `.xlsx` workbook;
2. one `.md` source-analysis report.

Separate CSV files are fallback-only when neither XLSX nor a multi-tab Google Sheet can be produced.

Approved filename pattern:

```text
AILAWS__<PACK_ID>__<SOURCE_ID>__<SHORT_TITLE>__<RUN_ID>.xlsx
AILAWS__<PACK_ID>__<SOURCE_ID>__<SHORT_TITLE>__<RUN_ID>.md
```

Required XLSX tabs:

```text
00_MANIFEST
01_SOURCE_IDENTITY
02_ACTOR_DUTY
03_HSA_THREATS
04_EVIDENCE
05_UNKNOWN_CONFLICT
06_ENGINEERING
07_LOCATOR_INDEX
```

## 2. PILOT VALIDATION RESULT

The EU-001 V2 pilot established the intended operating pattern:

- exactly one XLSX plus one MD deliverable;
- filename contains `NB02`, `EU-001`, and `RUN-20260915-002`;
- Markdown metadata preserves `PACK_ID=NB02`, `SOURCE_ID=EU-001`, `DESTINATION_REPO=fatihekler/ai-laws`, `REVIEW_OWNER=AI-LAWS`, `PROMOTION_STATE=SUPPORTING_RESEARCH`, and `PRIMARY_SOURCE_RECHECK_REQUIRED=TRUE`;
- XLSX binary package contains eight worksheet parts;
- Markdown contains S1-S7 source analysis;
- HSA threat IDs are not invented when the HSA taxonomy itself is not selected;
- engineering outputs remain candidates rather than implemented/tested/effective claims.

This validates the **format**. It does not independently verify every legal proposition in the pilot source extraction.

## 3. CONTROL RULES

```text
SELECTED_SOURCES_ONLY = TRUE
NOTEBOOK_OUTPUT != VERIFIED_FACT
SOURCE_ID = OWNER-NATIVE; DO NOT RENUMBER
PACK_ID = AI-LAWS NOTEBOOK PACK ID; DO NOT INFER FROM JURISDICTION
UNKNOWN != SAFE
INCIDENT != LIABILITY
RECOMMENDATION/PRINCIPLE != MANDATORY_DUTY
IMPLEMENTED != TESTED != EFFECTIVE
```

NotebookLM must not invent HSA threat/control/test/source IDs. If the selected source set does not contain the HSA taxonomy, use `THREAT_ID=UNKNOWN` and describe the threat textually.

Default promotion state is `SUPPORTING_RESEARCH`.

Allowed promotion values:

```text
QUESTION
SUPPORTING_RESEARCH
FINDING_CANDIDATE
HOLD
```

Forbidden direct outputs/promotions:

```text
VERIFIED_FINDING
ACCEPTED_REQUIREMENT
PASS
LEGAL_VIOLATION
LIABILITY_ESTABLISHED
```

## 4. APPROVED COMPACT RUNTIME PROMPT

```text
AI-LAWS / HSA — SINGLE SOURCE V2

CANONICAL=FALSE | AUTO_ADVANCE=NO | SELECTED_ONLY=TRUE

Yalnız seçili kaynağı kullan. Hafıza/internet/seçilmemiş kaynak kullanma. Destek yoksa UNKNOWN/NOT_STATED.

ID: mevcut SOURCE_ID aynen korunur. PACK_ID AI-LAWS upload planındaki exact pack'tir (örn EU-001=NB02). RUN_ID=RUN-YYYYMMDD-NNN. Threat/control/test/source ID uydurma.

YALNIZ 2 DOSYA:
AILAWS__<PACK_ID>__<SOURCE_ID>__<SHORT>__<RUN_ID>.xlsx
AILAWS__<PACK_ID>__<SOURCE_ID>__<SHORT>__<RUN_ID>.md

XLSX sekmeleri EXACT:
00_MANIFEST | 01_SOURCE_IDENTITY | 02_ACTOR_DUTY | 03_HSA_THREATS | 04_EVIDENCE | 05_UNKNOWN_CONFLICT | 06_ENGINEERING | 07_LOCATOR_INDEX

00: run/pack/source/title/jurisdiction/authority/binding/currentness/canonical=false/promotion/recheck/destination/reviewer/limits.
01: issuer/document no/type/publication+effective dates/version/scope/limits. publication!=application; EEA relevance!=automatic EEA applicability.
02: actor/right/duty/condition/locator/exception/remedy/binding/limits. principle/recommendation!=mandatory duty.
03: threat_id/name/relation/summary/locator/limits. Taxonomy seçili değilse THREAT_ID=UNKNOWN; ID uydurma. Relation only DIRECT_EXPLICIT|ANALOGICAL|CONTEXT_ONLY|NO_EXPLICIT_SUPPORT_FOUND.
04: duty/question/evidence type+holder/SOURCE_REQUIRED|RESEARCH_USEFUL/integrity/locator/limits.
05: KNOWN|UNKNOWN|CONFLICT|CURRENTNESS_LIMIT|TRANSLATION_LIMIT|SCOPE_LIMIT|EVIDENCE_GAP + description/materiality/locator/resolution/next research.
06: duty/control candidate/test candidate/evidence artifact/destination/reviewer/promotion/limits. ID uydurma; implemented/tested/effective deme.
07: claim summary/source_id/exact locator/type/limits. Her material claim locator içersin.

MD aynı RUN/PACK/SOURCE ile S1-S7: identity/authority; scope/actors; rights/duties; HSA relevance; evidence/accountability; unknown/conflict/currentness; engineering relevance. XLSX/source dışı iddia ekleme.

CONTROL: DESTINATION_REPO=fatihekler/ai-laws veya REPO-LAW. REVIEW_OWNER=AI-LAWS; gerekirse HUMAN_REVIEW_REQUIRED. Promotion default=SUPPORTING_RESEARCH; allowed QUESTION|SUPPORTING_RESEARCH|FINDING_CANDIDATE|HOLD. PRIMARY_SOURCE_RECHECK_REQUIRED=TRUE unless selected AI-LAWS control record explicitly supports FALSE; uncertain=>TRUE.

Never: VERIFIED_FINDING|ACCEPTED_REQUIREMENT|PASS|LEGAL_VIOLATION|LIABILITY_ESTABLISHED.

Special: CL-002 no official fulltext=>HOLD; INT-004 current UNESCO certified copy; TR-* material result=>live currentness recheck; INC-* fact/attribution/corroboration/hypothesis separate and INCIDENT!=LIABILITY; INC-004 context only; STD-* metadata only without licensed full text.

XLSX unavailable=>ONE multi-tab Google Sheet. Ayrı CSV üretme unless both unavailable.

FINAL CHAT ONLY:
RUN_ID | PACK_ID | SOURCE_ID | XLSX filename/state | MD filename/state | RECHECK | PROMOTION | STOP
```

## 5. CONTINUATION RULE

Use this exact working format for subsequent single-source NotebookLM runs unless:

- a source-specific override requires `HOLD` or a different extraction mode;
- the source is metadata-only;
- a court/case source lacks verified official full text;
- the AI-LAWS source-selection/control state changes.

Every downloaded pair should be stored under a deterministic source folder, for example:

```text
86_NOTEBOOKLM/downloads-notebooklm/AI-LAWS__EU__EU-002/
```

Do not treat the folder output as canonical legal findings merely because the workbook/report was produced.
