# AI-LAWS-R012 — Comparative Liability Baseline

**UNIT_ID:** `AI-LAWS-R012`  
**RESEARCH_DATE:** 2026-09-14  
**STATE:** `COMPLETE_RESEARCH_BASELINE_L1_L2_LIABILITY_MODEL_JURISDICTION_DEPENDENCIES_OPEN`  
**ROLE:** `COMPARATIVE_LAW_RESEARCHER`  
**LEGAL_ADVICE:** NO  
**MODEL_OUTPUT_CANONICAL:** NO  
**NOTEBOOK_OUTPUT_CANONICAL:** NO  
**AUTO_ADVANCE:** NO

## 1. Bounded scope

R012 creates a source-backed comparative liability grammar without inventing a global AI-liability rule. The bounded positive-law comparison uses:

- EU: controlled `EU-001` AI Act, `EU-003` Directive (EU) 2024/2853 Product Liability Directive, and `EU-005` GDPR;
- US: the controlled federal executive/OMB/NIST layer plus the already pinned Utah Chapter 72 Section 101 anchor, mainly to identify what the current controlled source set does and does not establish about private civil liability.

R005/R006 are not reopened. R019 is not started. Notebook ingestion is not performed.

## 2. Currentness and source identity

The repository copies of `EU-001`, `EU-003`, and `EU-005` are previously verified exact official EUR-Lex byte matches. R012 extracted liability-relevant text from those verified snapshots.

Fresh GitHub-runner probes on 2026-09-14 returned `HTTP 202` with empty bodies for the tested EUR-Lex PDF endpoints. This repeats the known live-access limitation and does not prove amendment, repeal, or staleness.

Fresh probes returned accessible official endpoints for `US-003`, `US-004`, `US-007`, `US-008`, and Utah `US-009` Section 101. The OMB PDF hashes matched the already verified repository copies; NIST publication pages were live; Utah Section 101 returned the previously pinned current PDF.

```text
LIVE_FETCH_FAILURE != SOURCE_CHANGE
EXACT_SNAPSHOT_IDENTITY != PERMANENT_CURRENTNESS
DIRECTIVE_TEXT_VERIFIED != MEMBER_STATE_TRANSPOSITION_VERIFIED
CONTROLLED_SOURCE_GAP != NO_LIABILITY_LAW
```

## 3. Actor translation firewall

AI Act roles such as provider, deployer, importer, distributor, authorised representative, product manufacturer, and operator are regulatory roles. They do not automatically determine the civil-liability defendant.

The Product Liability Directive uses a different chain: manufacturer of product/component, provider of a related service, authorised representative, importer, fulfilment service provider, distributor, specified online-platform provider, and qualifying substantial modifier. GDPR uses controller and processor roles.

```text
AI_ACT_PROVIDER != AUTOMATIC_PLD_MANUFACTURER
AI_ACT_DEPLOYER != AUTOMATIC_TORT_DEFENDANT
TOOL_PROVIDER != AUTOMATIC_COMPONENT_MANUFACTURER
AGENT_OPERATOR != AUTOMATIC_CONTROLLER_OR_PROCESSOR
ROLE_MAPPING_REQUIRES_FACTS_AND_APPLICABLE_LAW
```

## 4. EU Product Liability Directive architecture

### Software and manufacturer control

`EU-003` Article 4 includes software within the definition of product. Its manufacturer-control concept addresses integration/supply of components, software updates/upgrades, modification, and the ability to supply updates/upgrades. That makes software lifecycle control relevant within this regime; it does not make every AI service defective or every model developer liable.

### Defectiveness

Article 7 uses the safety a person is entitled to expect or that Union/national law requires, taking all circumstances into account. The controlled text expressly includes reasonably foreseeable use, continued learning/acquisition of features after market placement/service, foreseeable interconnection effects, timing/control, safety-relevant cybersecurity requirements, recalls/interventions, and specific user-group needs.

```text
AI_OUTPUT_ERROR != DEFECT_AUTOMATICALLY
REGULATORY_NONCOMPLIANCE != CIVIL_LIABILITY_AUTOMATICALLY
BETTER_MODEL_EXISTS != DEFECT_AUTOMATICALLY
```

### Liable economic-operator routes

Article 8 establishes product-chain routes that may include the defective-product manufacturer, a causally relevant defective-component manufacturer, defined Union-side operators for third-country manufacturers, qualifying substantial modifiers, and conditional distributor/platform routes. Concrete actor classification remains fact-specific.

### Evidence and causation

Article 9 provides controlled evidence-disclosure mechanisms subject to plausibility, necessity, proportionality, confidentiality/trade-secret protection, and national procedure.

Article 10 keeps the claimant's baseline burden to prove defectiveness, damage, and causal link, while establishing rebuttable presumptions in specified circumstances, including defined non-disclosure, qualifying product-safety noncompliance, obvious malfunction, typical consistency of damage with defect, and technically/scientifically complex proof situations meeting the Directive's likelihood threshold.

R012 records this architecture but does not replace R014's dedicated evidence/procedure work.

### Damage, remedy, defences, and allocation

Articles 5–6 establish the Directive compensation route for defined damage caused by a defective product, including death/personal injury, medically recognised psychological injury, specified property loss, and destruction/corruption of non-professional data, with national-law dependencies preserved.

Article 11 contains defined exemptions and specific limits concerning related services, software/updates/upgrades, missing safety updates/upgrades, and substantial modification within manufacturer control. Articles 12–15 address multiple liable economic operators, contribution/recourse, injured-person fault, and non-excludability against the injured person.

Article 8(5) permits Member States, in specified non-recovery/insolvency circumstances, to use existing or establish national compensation schemes. It does **not** create a mandatory EU-wide AI catastrophe fund.

## 5. PLD date-state gate

Article 22 requires Member States to transpose Directive (EU) 2024/2853 by **2026-12-09**. Article 21 repeals Directive 85/374/EEC from that date while preserving the earlier Directive for products placed on the market or put into service before then.

On 2026-09-14:

```text
PLD_2024_TEXT = VERIFIED_PRIMARY_SOURCE
TRANSPOSITION_DEADLINE = FUTURE_2026-12-09
MEMBER_STATE_TRANSPOSITION_MAP = NOT_ATTEMPTED
UNIFORM_CURRENT_NATIONAL_IMPLEMENTATION = NOT_INFERRED
```

The Directive therefore supports the Union legislative liability architecture, but R012 does not state that every Member State already applies the new rules identically.

## 6. GDPR Article 82 route

`EU-005` Article 82 provides a distinct compensation/liability route for material or non-material damage resulting from GDPR infringement. Controllers and processors have different liability triggers; the provision also contains a responsibility-based exemption, whole-damage protection where multiple responsible actors are involved, and recourse allocation.

```text
GDPR_INFRINGEMENT != PRODUCT_DEFECT
GDPR_ART82_ROUTE != AI_ACT_FINE_ARCHITECTURE
MULTIPLE_RESPONSIBLE_CONTROLLERS != EVERY_AI_SUPPLY_CHAIN_ACTOR
```

## 7. AI Act interface

`EU-001` supplies actor definitions and regulatory duties, but R003's firewall remains controlling:

```text
AI_ACT_VIOLATION != PRIVATE_RIGHT_OF_ACTION
REGULATORY_FINE_ARCHITECTURE != CIVIL_DAMAGES_RULE
AI_ACT_COMPLIANCE != PRODUCT_LIABILITY_DEFENCE
```

A mandatory AI/product-safety rule may matter to a private-law analysis only after the exact system, actor, applicable provision/date, protected risk, and liability route are established. R012 does not infer that bridge generically.

## 8. United States controlled-source result

The controlled federal `US-001..US-008` layer is executive-order, policy-plan, OMB, and NIST centered. R007 did not establish an exhaustive federal/state tort, product-liability, consumer, privacy, or private-right-of-action corpus.

Fresh R012 probes confirm selected OMB/NIST source availability, but availability does not convert those instruments into generally applicable civil-liability statutes. Utah Section 101 remains a current source anchor only; whole-chapter liability/remedy analysis is open.

```text
US_GENERAL_AI_TORT_RULE = NOT_ESTABLISHED_BY_CONTROLLED_R012_SET
NIST_FRAMEWORK != STATUTE
OMB_MEMORANDUM != GENERAL_PRIVATE_TORT_DUTY
EXECUTIVE_POLICY != PRIVATE_RIGHT_OF_ACTION
UTAH_SECTION101_CURRENT != WHOLE_CHAPTER_LIABILITY_ANALYSIS_COMPLETE
```

This is a controlled-source insufficiency result, not a finding that U.S. tort/product/privacy/consumer law cannot apply to AI harms.

## 9. Required liability chain

Every later concrete liability record must keep separate:

```text
ACTOR
DUTY
BREACH
CAUSATION
DAMAGE
REMEDY
DEFENCE
EVIDENCE
JURISDICTION
DATE_STATE
```

No missing element is borrowed from another regime.

## 10. Open dependencies

R012 does not resolve:

- EU Member-State PLD transposition or national procedural/damages details;
- CJEU or national case law applying the new PLD to AI/software;
- exhaustive U.S. federal/50-state private liability law and case law;
- concrete role, breach/defect, causation, damage, defence, evidence, or remedy;
- Türkiye R005/R006 blockers;
- R019 incident-specific work;
- R013 insurance/financial-responsibility research;
- R014 evidence/procedure crosswalk;
- other jurisdictions.

## 11. Close state

```text
CONTROLLED_SOURCE_RECORDS = 8
EU_PRIMARY_LIABILITY_SOURCES = 3
EU_PLD_SOFTWARE_AS_PRODUCT = VERIFIED
EU_PLD_TRANSPOSITION_DEADLINE = 2026-12-09
EU_PLD_MEMBER_STATE_TRANSPOSITION_MAP = NOT_ATTEMPTED
GDPR_ARTICLE_82_ROUTE = VERIFIED_PRIMARY_TEXT
US_GENERAL_AI_TORT_RULE = NOT_ESTABLISHED_BY_CONTROLLED_SET
EURLEX_LIVE_RECHECK = HTTP_202_EMPTY_BODY
NOTEBOOK_UPLOADS = 0
NEW_SOURCE_BINARIES = 0
DERIVED_MARKDOWN_CREATED = 0
GLOBAL_LIABILITY_RULE = NOT_INFERRED
LEGAL_CONCLUSION = NOT_ATTEMPTED
UNKNOWN_PRESERVED = YES
AUTO_ADVANCE = NO
STOP = YES
```
