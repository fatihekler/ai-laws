AI-LAWS / HSA — SINGLE SOURCE V2.1

`CANONICAL=FALSE | AUTO_ADVANCE=NO | SELECTED_ONLY=TRUE`

Yalnız seçili kaynağı kullan. Hafıza/internet/seçilmemiş kaynak kullanma. Destek yoksa `UNKNOWN/NOT_STATED`.

ID:

* mevcut `SOURCE_ID` aynen korunur;
* `PACK_ID` AI-LAWS upload planındaki exact pack'tir (örn. EU-001=NB02);
* `RUN_ID=RUN-YYYYMMDD-NNN`;
* threat/control/test/source ID uydurma.

YALNIZ 2 DOSYA:

`AILAWS__<PACK_ID>__<SOURCE_ID>__<SHORT>__<RUN_ID>.xlsx`

`AILAWS__<PACK_ID>__<SOURCE_ID>__<SHORT>__<RUN_ID>.md`

XLSX sekmeleri EXACT:

`00_MANIFEST`
`01_SOURCE_IDENTITY`
`02_ACTOR_DUTY`
`03_HSA_THREATS`
`04_EVIDENCE`
`05_UNKNOWN_CONFLICT`
`06_ENGINEERING`
`07_LOCATOR_INDEX`

00: run, pack, source, title, jurisdiction, authority, binding, currentness, canonical=false, promotion, recheck, destination, reviewer, limitations.

01: issuer, document no, type, publication/effective dates, version, territorial scope, limitations. `publication!=application`; `EEA relevance!=automatic EEA applicability`.

02: actor, right/interest, duty/safeguard, condition, locator, exception, remedy/enforcement, binding, limits. `principle/recommendation!=mandatory duty`.

03: threat_id/name/relation/summary/locator/limits. **HSA taxonomy seçili kaynak değilse `THREAT_ID=UNKNOWN`; hiçbir `THR-NNN` üretme.** Relation yalnız:
`DIRECT_EXPLICIT|ANALOGICAL|CONTEXT_ONLY|NO_EXPLICIT_SUPPORT_FOUND`.

04: duty/question, evidence type/holder, `SOURCE_REQUIRED|RESEARCH_USEFUL`, integrity, locator, limits. **SOURCE_REQUIRED yalnız seçili kaynak açıkça zorunlu kılıyorsa; diğerlerini RESEARCH_USEFUL yaz.**

05: `KNOWN|UNKNOWN|CONFLICT|CURRENTNESS_LIMIT|TRANSLATION_LIMIT|SCOPE_LIMIT|EVIDENCE_GAP` + description/materiality/locator/resolution/next research.

06: duty/safeguard, control candidate, test candidate, evidence artifact, destination, reviewer, promotion, limits. ID uydurma; implemented/tested/effective deme.

07: claim summary, source_id, exact locator, locator type, limitations. Her material claim locator içersin.

MD aynı RUN/PACK/SOURCE ile kısa S1–S7 analiz:
identity/authority; scope/actors; rights/duties; HSA relevance; evidence/accountability; unknown/conflict/currentness; engineering relevance. XLSX/source dışı iddia ekleme.

CONTROL:
`DESTINATION_REPO=fatihekler/ai-laws`
`REVIEW_OWNER=AI-LAWS`
Default promotion=`SUPPORTING_RESEARCH`
Allowed=`QUESTION|SUPPORTING_RESEARCH|FINDING_CANDIDATE|HOLD`
`PRIMARY_SOURCE_RECHECK_REQUIRED=TRUE` unless selected AI-LAWS control record explicitly supports FALSE; uncertain=>TRUE.

Never:
`VERIFIED_FINDING|ACCEPTED_REQUIREMENT|PASS|LEGAL_VIOLATION|LIABILITY_ESTABLISHED`

VALIDATE BEFORE EXPORT:

* invented `THR-NNN`?
* RUN/PACK/SOURCE mismatch?
* required metadata missing?
* unsupported `SOURCE_REQUIRED`?
* material locator missing?

YES ise önce düzelt, sonra export et.

SPECIAL:
`CL-002` official fulltext yoksa HOLD.
`INT-004` current UNESCO certified copy.
`TR-*` material result=>live currentness recheck.
`INC-*` fact/attribution/corroboration/hypothesis ayrı; `INCIDENT!=LIABILITY`.
`INC-004` context only.
`STD-*` licensed fulltext yoksa metadata only.
`EU-004`: Article 51 scope'u kesin koru; private actor'a genel doğrudan Charter duty'si uydurma; taxonomy seçili değilse `THREAT_ID=UNKNOWN`.

XLSX yoksa ONE multi-tab Google Sheet. Ayrı CSV yalnız ikisi de mümkün değilse.

FINAL CHAT ONLY:

`RUN_ID | PACK_ID | SOURCE_ID | XLSX filename/state | MD filename/state | RECHECK | PROMOTION | STOP`
