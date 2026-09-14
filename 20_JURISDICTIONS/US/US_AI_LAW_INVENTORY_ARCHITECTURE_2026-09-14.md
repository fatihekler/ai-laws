# AI-LAWS — United States Federal + State AI-Law Inventory Architecture

**WORK_ITEM:** `AI-LAWS-R007`
**RESEARCH_DATE:** 2026-09-14
**LEVEL:** L1 inventory architecture + bounded current-source verification
**LEGAL_ADVICE:** NO
**AUTO_ADVANCE:** NO

## 1. Purpose

R007 establishes a federal/state source architecture without collapsing executive orders, OMB memoranda, voluntary NIST frameworks, enacted statutes, pending bills and unverified search results into one category.

```text
EXECUTIVE_ORDER != ACT_OF_CONGRESS
OMB_MEMORANDUM != GENERALLY_APPLICABLE_FEDERAL_STATUTE
NIST_FRAMEWORK != STATUTE
PROPOSED_BILL != ENACTED_LAW
STATE_PORTAL_REACHABLE != STATE_LAW_CURRENTNESS_VERIFIED
SEARCH_FAILURE != NO_STATE_AI_LAW
```

## 2. Federal controlled-source layer

`US_FEDERAL_AI_SOURCE_CLASSIFICATION_2026-09-14.csv` classifies the existing controlled `US-001..US-008` source set. R007 does not claim that those eight sources exhaust all federal statutes, regulations, agency rules or sector-specific law that may govern AI.

The controlled federal layer contains executive orders, executive policy/guidance, OMB memoranda and voluntary NIST frameworks/profiles. None is relabeled as an Act of Congress. Sectoral statutes and regulations remain separate research work.

## 3. State architecture

`US_STATE_AI_LAW_RESEARCH_REGISTRY.csv` enumerates all 50 States plus the District of Columbia. Enumeration is coverage architecture, not a claim that each jurisdiction has or lacks an AI-specific statute.

As of this bounded unit:

```text
STATE_OR_DC_JURISDICTIONS_ENUMERATED = 51
CURRENT_AI_SPECIFIC_STATUTE_SOURCE_VERIFIED_L1 = 1  # Utah
OFFICIAL_CODE_PORTAL_REACHABLE_CONTENT_UNRESOLVED = 1  # Texas candidate endpoint
RESEARCH_REQUIRED = 49
```

## 4. Utah current-law pin

The Utah Legislature Xcode current wrapper identifies Title 13 Chapter 72. The current-version body for Section 13-72-101 is `C13-72-S101_2026050620260506.html` and states:

- Chapter 72: Artificial Intelligence Policy Act;
- Section 13-72-101: Definitions;
- effective date: 5/6/2026;
- affected by Section 63I-2-213 on 7/1/2027.

R007 therefore resolves the prior `US-009` currentness blocker at the chapter-identity / Section 101 level. It does **not** claim that every section in Chapter 72 was independently re-read and currentness-verified in this unit.

```text
US009_CURRENT_CHAPTER_IDENTITY = VERIFIED
US009_SECTION_101_CURRENT_BODY = VERIFIED
US009_SECTION_101_EFFECTIVE_DATE = 2026-05-06
US009_FUTURE_CHANGE_SIGNAL = 2027-07-01
US009_WHOLE_CHAPTER_SECTION_BY_SECTION_CURRENTNESS = OPEN
```

## 5. Texas boundary

The official Texas statutes endpoint tested by R007 returned a client-rendered shell. R007 therefore does not infer title, content, effective date or enacted/current status from that endpoint. Texas remains `RESEARCH_REQUIRED`.

## 6. Federal-state conflict boundary

R007 records federal executive policy sources but does not decide constitutional preemption, Supremacy Clause questions, validity of state-law restrictions, private rights of action, enforcement authority or litigation outcomes. Those questions require instrument-specific law and facts.

## 7. Stop boundary

R007 stops before:

- an exhaustive 50-state substantive law survey;
- sector-by-sector federal statutory/regulatory analysis;
- pending-bill tracking across every legislature;
- case law;
- preemption conclusions;
- compliance advice, breach, liability, remedies or sanctions.

```text
R007_US_INVENTORY_ARCHITECTURE = COMPLETE_L1
FEDERAL_CONTROLLED_SOURCE_CLASSIFICATION = COMPLETE_FOR_US001_US008
STATE_JURISDICTIONS_ENUMERATED = 51
STATE_CURRENT_LAW_CONTENT = PARTIAL
UTAH_US009_CURRENTNESS = VERIFIED_AT_CHAPTER_IDENTITY_SECTION101_LEVEL
CASE_LAW = NOT_ATTEMPTED
LIABILITY_CONCLUSION = NOT_ATTEMPTED
ZIP_OR_ARTIFACT_CREATED = NO
AUTO_ADVANCE = NO
```
