# AI-LAWS — R005 Türkiye Primary Source Pin

**UNIT_ID:** AI-LAWS-R005-PIN-20260913-001  
**DATE:** 2026-09-13  
**STATE:** PARTIAL_SOURCE_PIN / OFFICIAL_PORTAL_ACCESS_BLOCKED  
**CANONICAL:** FALSE  
**LEGAL_ADVICE:** NO

## Scope

This bounded unit identifies and pins the official source family and document identity for the first Türkiye primary-law baseline used by NB04. It does not create substantive legal conclusions and does not treat inaccessible official consolidated text as verified current text.

## Source handling rule

```text
OFFICIAL_SOURCE_IDENTITY != CURRENTNESS_VERIFIED
OFFICIAL_URL_PINNED != FILE_DOWNLOADED
SECONDARY_CROSS_REFERENCE != PRIMARY_SOURCE
SEARCH_FAILURE != NO_LAW
```

The current execution environment could not retrieve `www.mevzuat.gov.tr` PDF/HTML bytes; attempts returned timeout/502 or local DNS failure. Therefore no Mevzuat binary, SHA-256, byte size, or content-identity assertion is created in this unit.

## Rights/use state

For Turkish legislation, FSEK No. 5846 Article 31 provides that officially published/announced legislation and judicial decisions may be reproduced, disseminated, processed, or otherwise used. This establishes a legal-text reuse basis, but does not cure source-currentness or byte-identity uncertainty.

## Pinned primary-law families

| Source ID | Document | Official identity / target | Currentness state | Acquisition state |
|---|---|---|---|---|
| TR-001 | Türkiye Cumhuriyeti Anayasası — No. 2709 | `https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=2709&MevzuatTur=1&MevzuatTertip=5` | OFFICIAL_SOURCE_FAMILY_PINNED / CONSOLIDATED_TEXT_ACCESS_FAILED | MANUAL_DOWNLOAD_REQUIRED |
| TR-002 | Kişisel Verilerin Korunması Kanunu — No. 6698 | `https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6698&MevzuatTur=1&MevzuatTertip=5` | OFFICIAL_SOURCE_FAMILY_PINNED / CONSOLIDATED_TEXT_ACCESS_FAILED | MANUAL_DOWNLOAD_REQUIRED |
| TR-003 | Türk Borçlar Kanunu — No. 6098 | `https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6098&MevzuatTur=1&MevzuatTertip=5` | OFFICIAL_SOURCE_FAMILY_PINNED / CONSOLIDATED_TEXT_ACCESS_FAILED | MANUAL_DOWNLOAD_REQUIRED |
| TR-004 | Türk Medeni Kanunu — No. 4721 | `https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=4721&MevzuatTur=1&MevzuatTertip=5` | OFFICIAL_SOURCE_FAMILY_PINNED / CONSOLIDATED_TEXT_ACCESS_FAILED | MANUAL_DOWNLOAD_REQUIRED |
| TR-005 | Türk Ceza Kanunu — No. 5237 | `https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=5237&MevzuatTur=1&MevzuatTertip=5` | OFFICIAL_SOURCE_FAMILY_PINNED / CONSOLIDATED_TEXT_ACCESS_FAILED | MANUAL_DOWNLOAD_REQUIRED |
| TR-006 | Tüketicinin Korunması Hakkında Kanun — No. 6502 | `https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6502&MevzuatTur=1&MevzuatTertip=5` | OFFICIAL_SOURCE_FAMILY_PINNED / CONSOLIDATED_TEXT_ACCESS_FAILED | MANUAL_DOWNLOAD_REQUIRED |
| TR-007 | İnternet Ortamında Yapılan Yayınların Düzenlenmesi... — No. 5651 | `https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=5651&MevzuatTur=1&MevzuatTertip=5` | OFFICIAL_SOURCE_FAMILY_PINNED / CONSOLIDATED_TEXT_ACCESS_FAILED | MANUAL_DOWNLOAD_REQUIRED |
| TR-008 | Siber Güvenlik Kanunu — No. 7545 | TBMM law record for 7545 + Resmî Gazete 19/03/2025 No. 32846 + amending Law No. 7590, RG 31/07/2026 No. 33326; current consolidated Mevzuat target by law number 7545 | PARTIAL_CURRENTNESS_VERIFIED; 7590 amendments effective 31/07/2026; consolidated official bytes unavailable | MANUAL_DOWNLOAD_REQUIRED |

## TR-008 currentness finding

The original Siber Güvenlik Kanunu No. 7545 was accepted on 12 March 2025 and published in Resmî Gazete on 19 March 2025, No. 32846. It was materially amended by Law No. 7590, accepted 24 July 2026 and published in Resmî Gazete on 31 July 2026, No. 33326. The amendment changes provisions including Article 6, Article 16, adds Temporary Article 2 and an attached list. Accordingly:

```text
7545_ORIGINAL_2025 != CURRENT_CONSOLIDATED_7545
CURRENT_7545_REQUIRES_7590_EFFECTS
```

Do not use only the 19 March 2025 original text for current-law analysis.

## Acquisition result

```text
SOURCE_IDS_TOUCHED = TR-001..TR-008
OFFICIAL_SOURCE_FAMILIES_PINNED = 8
CURRENT_CONSOLIDATED_BINARIES_DOWNLOADED = 0
SHA256_RECORDED = 0
REPOSITORY_LEGAL_TEXT_BINARIES_CREATED = 0
REASON = OFFICIAL_MEVZUAT_PORTAL_UNAVAILABLE_TO_CURRENT_EXECUTION_ENVIRONMENT
```

## Next requirement

When the official Mevzuat portal becomes reachable from an execution channel capable of binary transfer:

1. open each exact law-number record;
2. verify the current consolidated version/date state;
3. download the official PDF from the official host;
4. verify expected title/law number and opening text;
5. compute SHA-256, byte size, MIME type;
6. store under `86_NOTEBOOKLM/SOURCES/NB04/` using the controlled naming convention;
7. append/update the central acquisition ledger;
8. only then mark the source `S8_CONTENT_IDENTITY_CHECKED`.

`AUTO_ADVANCE = NO`
