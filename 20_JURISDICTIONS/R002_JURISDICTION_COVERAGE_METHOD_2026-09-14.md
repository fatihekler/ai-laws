# AI-LAWS-R002 — Global Jurisdiction Registry Coverage Method

**UNIT_ID:** `AI-LAWS-R002`
**DATE:** 2026-09-14
**ROLE:** jurisdiction-registry / coverage-control infrastructure
**LEGAL_ADVICE:** NO
**AUTO_ADVANCE:** NO

## 1. Purpose

R002 turns the seed jurisdiction registry into an explicit global coverage baseline without treating an unresearched jurisdiction as legally empty.

The registry is a research-routing instrument. A row means the jurisdiction/area is in scope; it does **not** mean substantive AI law, private law, public law, case law, treaty effect, enforcement or remedies have been researched.

```text
REGISTRY_PRESENCE != SUBSTANTIVE_LAW_RESEARCHED
REGISTRY_ABSENCE_OF_A_RULE != NO_RULE
UN_M49_ENUMERATION != SOVEREIGNTY_DETERMINATION
CENSUS_ENUMERATION != LEGAL_STATUS_EQUIVALENCE
SUBNATIONAL_MATERIALITY != INDEPENDENT_SOVEREIGNTY
```

## 2. Global country/area enumeration layer

The live official United Nations Statistics Division M49 overview is the deterministic enumeration source for the global country/area universe used by R002.

R002 parsed 247 rows carrying ISO alpha-2 codes from the live table. Existing AI-LAWS rows such as Türkiye, United States, China, United Kingdom, Republic of Korea, Japan, Canada, Australia, Brazil and others retain their pre-existing research state/priority/focus; the M49 pass adds only dated enumeration confirmation metadata.

Newly enumerated rows default to:

```text
JURISDICTION_TYPE = UN_M49_COUNTRY_OR_AREA
RESEARCH_STATE = REGISTRY_ENUMERATED_RESEARCH_NOT_STARTED
PRIORITY = P2
SUBSTANTIVE_LAW_FINDING = NONE
```

M49 uses "country or area" terminology. R002 therefore does not convert that list into a determination of sovereignty, recognition, independence, treaty personality, applicable law or domestic legislative competence.

## 3. U.S. subnational layer

The live official U.S. Census Bureau state/statistical-equivalent list is the deterministic enumeration source for the U.S. subnational baseline.

The retrieved list contains 57 rows. Existing R007 state/DC rows retain their legal-research state. R002 adds/normalizes non-state territory/statistical-equivalent routing, including:

```text
US-AS
US-GU
US-MP
US-PR
US-UM
US-VI
```

`US-UM` is expressly classified as `SUBNATIONAL_US_TERRITORY_OR_STATISTICAL_EQUIVALENT`, not as a state or district.

Enumeration does not imply that states, District of Columbia, inhabited territories and U.S. Minor Outlying Islands have identical constitutional, legislative, judicial or regulatory status.

## 4. Material-subnational admission rule

AI-LAWS does not attempt to enumerate every municipality, province, canton, emirate, autonomous area, special administrative region or free zone on Earth before legal research begins. Instead, a subnational/special jurisdiction is added when at least one source-backed materiality trigger is met.

Materiality triggers are recorded in `R002_MATERIAL_SUBNATIONAL_TRIGGER_MATRIX_2026-09-14.csv` and include:

- constitutionally or statutorily separate legislative competence relevant to an AI-LAWS domain;
- materially separate court/legal system;
- enacted AI, data, privacy, biometric, consumer, product, employment, cyber or public-sector rules that materially diverge from the parent baseline;
- separate regulator/enforcement authority with legally material powers;
- separate conflict-of-laws, forum, recognition or enforcement relevance;
- special territory/free-zone regime with materially divergent applicable law;
- treaty/constitutional status that changes the applicable source hierarchy.

Unlisted subnational jurisdictions remain **in scope** and may be admitted when a trigger is verified.

## 5. ID and merge discipline

- Existing controlled AI-LAWS IDs are preserved where possible.
- ISO alpha-2 is used for new M49 country/area rows.
- U.S. Census abbreviations are represented as `US-XX`.
- International/regional organization rows retain controlled prefixes such as `INT-` and `REG-`.
- Duplicate `jurisdiction_id` is fail-closed and must remain zero.
- Existing research state may not be downgraded by an enumeration refresh.

## 6. Refresh discipline

R002 source bodies are live and dated. Future refreshes must re-fetch the official UN M49 and U.S. Census layers, record body hash/count changes, and review additions/removals before changing the registry.

```text
SAME_HASH_TODAY != PERMANENT_CURRENTNESS
SOURCE_LIST_CHANGE != AUTOMATIC_LEGAL_STATUS_CHANGE
NAME_CHANGE != SUBSTANTIVE_LAW_CHANGE
TERRITORIAL_STATUS_CHANGE != INFERRED_FROM_LABEL_ALONE
```

## 7. Stop boundary

R002 stops at registry and coverage-method infrastructure.

It does not perform substantive legal research for the 247 M49 rows, does not decide disputed territorial status, does not determine applicable law for a cross-border fact pattern, and does not complete R018.

```text
SUBSTANTIVE_LAW_FINDINGS_FOR_NEW_ROWS = 0
CROSS_BORDER_FORUM_CONCLUSION = NOT_ATTEMPTED
APPLICABLE_LAW_CONCLUSION = NOT_ATTEMPTED
AUTO_ADVANCE = NO
```
