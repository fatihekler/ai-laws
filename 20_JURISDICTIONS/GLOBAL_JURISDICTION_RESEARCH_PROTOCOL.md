# AI-LAWS — GLOBAL JURISDICTION RESEARCH PROTOCOL

## Goal

Build a jurisdiction-complete legal map without pretending that unresearched jurisdictions are legally empty.

## Coverage model

The registry must ultimately enumerate:

1. international/global instruments;
2. regional/supranational organizations and unions;
3. every sovereign state in scope;
4. material subnational jurisdictions where law materially differs (for example U.S. states/provinces where applicable);
5. special territories/free zones where AI/data/financial rules materially diverge;
6. sector-specific authorities where regulation is functionally jurisdictional.

The initial registry is a seed, not a completed world inventory.

## Per-jurisdiction minimum profile

Each jurisdiction profile should record:

```text
JURISDICTION_ID
NAME
TYPE
CONSTITUTIONAL/HUMAN_RIGHTS_BASELINE
AI_SPECIFIC_LEGISLATION
DATA_PRIVACY_AND_BIOMETRICS
CYBERSECURITY
PRODUCT_AND_SAFETY_LIABILITY
CIVIL/TORT_CONTRACT
CONSUMER_PROTECTION
CRIMINAL/CYBERCRIME
ADMINISTRATIVE/PUBLIC_SECTOR_AI
EMPLOYMENT
COMPETITION
FINANCIAL/INSURANCE
HEALTH/MEDICAL
CHILDREN/VULNERABLE_PERSONS
EVIDENCE/PROCEDURE
INCIDENT_REPORTING
REMEDIES/SANCTIONS
NATIONAL_SECURITY_EXEMPTIONS
CASE_LAW_STATE
REGULATORY_GUIDANCE
STANDARDS/CODES
PENDING_PROPOSALS
INTERNATIONAL_TREATY_LINKS
OPEN_CONFLICTS
UNKNOWNS
LAST_VERIFIED_DATE
```

## Research order

For each jurisdiction:

1. official legislation database / gazette;
2. official court database;
3. regulator/authority sources;
4. official treaty-status source;
5. recognized standards/public bodies;
6. high-quality legal scholarship/commentary only after primary-source identification.

## Effective-date discipline

Never collapse:

```text
ADOPTED
PUBLISHED
ENTERED_INTO_FORCE
APPLICABLE
PARTIALLY_APPLICABLE
AMENDED
REPEALED
PROPOSED
```

into a single “active” state.

## Subnational rule

If national law is materially supplemented by state/province/canton/emirate/free-zone rules, create sub-jurisdiction records rather than hiding divergence in notes.

## International-instrument rule

For treaties and conventions, separately record:

- signature;
- ratification/approval;
- entry into force for the party;
- reservations/declarations;
- direct effect or implementing legislation if material and verified.

## Translation rule

Record authentic-language status. A convenience translation is evidence of content only to the extent legally appropriate; do not silently treat it as the controlling text.

## Research completion levels

```text
L0_NOT_RESEARCHED
L1_SOURCE_SEEDS_IDENTIFIED
L2_PRIMARY_LAW_INVENTORY
L3_CASE_AND_REGULATOR_INVENTORY
L4_CROSS_DOMAIN_ANALYSIS
L5_HUMAN_LEGAL_REVIEWED
```

No jurisdiction becomes `COMPLETE` merely because an AI-specific law was found.
