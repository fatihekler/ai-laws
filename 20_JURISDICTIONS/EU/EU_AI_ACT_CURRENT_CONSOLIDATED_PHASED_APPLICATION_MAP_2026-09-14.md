# AI-LAWS — European Union AI Act Current Consolidated / Phased-Application Map

**WORK_ITEM:** `AI-LAWS-R003`
**RESEARCH_DATE:** 2026-09-14
**JURISDICTION:** European Union
**LEVEL:** L1/L2 current-law baseline
**CANONICAL:** controlled AI-LAWS research baseline, subject to refresh
**LEGAL_ADVICE:** NO
**AUTO_ADVANCE:** NO

## 1. Controlled source state

The controlling AI-LAWS primary-source baseline for this unit is:

```text
EU-001 = Regulation (EU) 2024/1689, consolidated snapshot CELEX:02024R1689-20260727
EU-002 = Regulation (EU) 2026/1744, amending Regulation (EU) 2024/1689
EU-001_REPOSITORY_SHA256 = 1ccd38d1c78482cf2053b70110115adcc5080700acc8bd7bead8cb3579143ccf
EU-002_REPOSITORY_SHA256 = 0bea4d808256b08275777949ba9cb3c70b7d02e4ebb3ac9b205671b1f552d386
R030_EU001_EXACT_OFFICIAL_EUR_LEX_BYTE_MATCH = YES
R030_EU002_EXACT_OFFICIAL_EUR_LEX_BYTE_MATCH = YES
R030_EU001_CURRENT_CONSOLIDATION_STATE = 2026-07-27 VERIFIED
R003_LIVE_EUR_LEX_RECHECK = PARTIAL_HTTP_202_EMPTY_BODY
```

R003's GitHub runner received HTTP 202 responses without substantive bodies from the live EUR-Lex ELI/PDF endpoints. That access result does not prove a source change and does not invalidate the same-day R030 exact-official/currentness verification. No newer consolidation is admitted into the controlled corpus by R003.

```text
LIVE_FETCH_FAILURE != SOURCE_CHANGE
SAME_DAY_VERIFIED_SNAPSHOT != PERMANENT_CURRENTNESS
CONSOLIDATED_TEXT != NEW_LEGISLATIVE_ACT
```

Material future use must still refresh EUR-Lex currentness.

## 2. Instrument status

Regulation (EU) 2024/1689 is a binding EU regulation. Article 113 states that it is binding in its entirety and directly applicable in all Member States. Direct applicability does not eliminate national-law dependencies where the Regulation itself assigns tasks, penalties, authorisations, procedural rules or institutional choices to Member States.

The Regulation entered into force on 1 August 2024. Its rules do not share one application date. Regulation (EU) 2026/1744 materially altered the phased-application architecture, especially for high-risk AI systems.

## 3. Scope and actor map

Under Article 2, subject to its exclusions and qualifications, the Regulation reaches:

- providers placing AI systems on the Union market or putting them into service, and providers placing general-purpose AI models on the Union market, including providers established outside the Union;
- deployers established or located in the Union;
- third-country providers and deployers where AI-system output is used in the Union;
- importers and distributors;
- product manufacturers placing or putting into service an AI system with their product under their own name or trademark;
- authorised representatives of non-EU providers; and
- affected persons located in the Union.

Important Article 2 boundaries include national-security/military/defence exclusions, research/development qualifications, personal non-professional deployer use, and free/open-source qualifications.

```text
THIRD_COUNTRY_PROVIDER != OUTSIDE_SCOPE_AUTOMATICALLY
AI_ACT_SCOPE != ALL_AI_ACTIVITY
DIRECT_APPLICABILITY != NO_NATIONAL_DEPENDENCIES
```

## 4. Current application state on 2026-09-14

### 4.1 Already applicable

As of the research date, the controlled text establishes the following principal states:

- Chapters I and II have applied since 2 February 2025, except the newly inserted Article 5(1) points (ba) and (bb) and Article 5(1a) and (1b), which do not apply until 2 December 2026.
- Article 4 AI-literacy duties are therefore already applicable. Providers and deployers must take context-sensitive measures supporting AI literacy of staff and other persons operating/using AI systems on their behalf; the provision does not require guaranteeing a specified literacy level for each individual.
- Most Article 5 prohibited-practice rules are already applicable. The new 2026/1744 intimate/sexually-explicit synthetic-content and child-sexual-abuse-material-related additions identified above are a future tranche as of 2026-09-14.
- Chapter III Section 4, Chapter V, Chapter VII, Chapter XII and Article 78 have applied since 2 August 2025, except Article 101.
- The general application date is 2 August 2026 for provisions not assigned a special date.
- Articles 102 to 110 have applied since 27 July 2026.
- Article 50's general transparency architecture is within the post-2-August-2026 applicable layer, subject to the specific Article 111(4) transition for Article 50(2) described below.

### 4.2 High-risk core delayed by Regulation (EU) 2026/1744

The most important current-date correction is Article 113(c). Chapter III Sections 1, 2 and 3, except Article 6(5), apply from:

```text
2027-12-02 = Article 6(2) / Annex III high-risk pathway
2028-08-02 = Article 6(1) / Annex I product/safety-component high-risk pathway
```

Accordingly, a statement that the AI Act's high-risk compliance core generally became applicable on 2 August 2026 is not correct under the 27 July 2026 consolidated text.

Article 6(5) is expressly excepted from that deferral and follows the otherwise applicable timetable. It required Commission practical-implementation guidelines by 2 February 2026.

```text
GENERAL_APPLICATION_DATE != EVERY_PROVISION_APPLICATION_DATE
HIGH_RISK_CLASSIFICATION_PATH != SAME_APPLICATION_DATE_FOR_ALL_HIGH_RISK_SYSTEMS
2026_OMNIBUS_AMENDMENT != COSMETIC_CHANGE
```

## 5. Article 111 legacy/transitional map

The current consolidated Article 111 creates important legacy-system/model transitions:

- Annex X large-scale IT-system components placed on the market or put into service before 2 August 2027 must be brought into compliance by 31 December 2030, without prejudice to the earlier Article 5 application rule.
- Other high-risk systems placed on the market or put into service before the relevant Chapter III application date are subject to the Regulation under Article 111(2) only if, from that date, they undergo significant design changes; high-risk systems intended for use by public authorities have a 2 August 2030 compliance deadline stated in the provision.
- GPAI models placed on the market before 2 August 2025 must take the necessary steps to comply by 2 August 2027.
- Providers of AI systems, including GPAI systems, generating synthetic audio/image/video/text and placed on the market before 2 August 2026 must comply with Article 50(2) by 2 December 2026.

Regulation (EU) 2026/1744 recital 39 explains the type/model logic behind the Article 111(2) grace period and links significant design changes to full high-risk compliance. Recitals are interpretive context; the operative consolidated text controls the legal rule.

## 6. General-purpose AI

Chapter V has applied since 2 August 2025, subject to Article 111(3)'s legacy-model transition.

Article 51 classifies GPAI models with systemic risk. Article 53 includes provider obligations concerning model technical documentation, information for downstream AI-system providers, a Union copyright-law compliance policy, and a public summary of training content. The limited free/open-source exception in Article 53(2) does not apply to GPAI models with systemic risk.

Article 55 adds obligations for systemic-risk GPAI providers, including model evaluation/adversarial testing, systemic-risk assessment and mitigation, serious-incident tracking/reporting and cybersecurity protection.

```text
GPAI_OBLIGATION_APPLICABLE != EVERY_LEGACY_MODEL_IMMEDIATELY_COMPLIANT
SYSTEMIC_RISK_CLASSIFICATION != CIVIL_LIABILITY_FINDING
SERIOUS_INCIDENT_REPORTING_DUTY != PROOF_OF_CAUSATION
```

## 7. Transparency

Article 50 addresses, among other matters:

- disclosure to persons interacting directly with certain AI systems;
- machine-readable marking/detectability of synthetic outputs under Article 50(2);
- notification for emotion-recognition and biometric-categorisation systems;
- disclosure for deep fakes and certain AI-generated/manipulated public-interest text; and
- clear/distinguishable timing and accessibility of required information.

As of 2026-09-14, Article 50 is in the generally applicable layer. However, Article 111(4) gives systems within its legacy synthetic-content category, placed before 2 August 2026, until 2 December 2026 specifically for Article 50(2).

## 8. Prohibited practices

Most Article 5 prohibitions have applied since 2 February 2025. The current text includes restrictions/prohibitions concerning, among other categories, manipulative/deceptive techniques causing or likely to cause significant harm, exploitation of vulnerabilities, social scoring, specified criminal-risk assessment, untargeted facial-image scraping, specified workplace/education emotion inference, specified sensitive biometric categorisation, and restricted real-time remote biometric identification for law enforcement.

The 2026/1744 additions in Article 5(1)(ba), (bb), (1a) and (1b) apply from 2 December 2026 and therefore remain future-applicable as of the research date.

For real-time remote biometric identification, Article 5 itself relies on national-law authorisation and detailed rules within the EU-law limits. Member-State-specific legality cannot be resolved from the EU Regulation alone.

## 9. Enforcement and penalties

Article 99 requires Member States to establish penalties and other enforcement measures and sets EU-level maximum fine architecture. The consolidated text includes, among other ceilings:

- Article 5 infringements: up to EUR 35 million or, for undertakings, up to 7% of preceding-year worldwide annual turnover, whichever is higher;
- specified operator/notified-body infringements: up to EUR 15 million or 3%, whichever is higher;
- supplying incorrect/incomplete/misleading information in specified circumstances: up to EUR 7.5 million or 1%, whichever is higher;
- special lower-ceiling treatment for SMEs and an SMC rule added by Regulation (EU) 2026/1744.

Penalty architecture being applicable does not make a not-yet-applicable underlying substantive obligation enforceable early. National penalty procedures, public-authority fine treatment and procedural mechanisms remain Member-State dependent where Article 99 leaves those matters to national systems.

```text
AI_ACT_VIOLATION != PRIVATE_RIGHT_OF_ACTION
REGULATORY_FINE_ARCHITECTURE != CIVIL_DAMAGES_RULE
PENALTY_CEILING != AUTOMATIC_FINE
```

## 10. Interaction with other EU law

Article 2 itself preserves several legal interfaces:

- Article 2(5): the AI Act does not affect intermediary-service provider liability rules in Chapter II of the Digital Services Act (`EU-006`).
- Article 2(7): EU personal-data/privacy/confidentiality law continues to apply; the AI Act does not displace GDPR (`EU-005`) and the other listed data-protection instruments, subject to the AI Act's own specified provisions.
- Article 2(9): the AI Act is without prejudice to other Union acts on consumer protection and product safety.
- Article 2(11): Member States may maintain or introduce more worker-favourable protections and permit more favourable collective agreements.
- Article 2(13), added by Regulation (EU) 2026/1744, creates a controlled possibility to limit specified AI Act requirements for Article 6(1) systems where Section A Annex I legislation provides equivalent or higher protection and overall protection is not reduced; Commission delegated acts are required to specify that mechanism by 2 August 2027.

The separate interaction inventory for R003 records `EU-003` Product Liability Directive, `EU-004` Charter, `EU-005` GDPR, `EU-006` DSA, `EU-007` Data Act, `EU-008` DGA, `EU-009` NIS2 and `EU-010` CRA. Inclusion in that inventory does not itself decide conflict, lex-specialis priority, national transposition, private remedies or causation.

## 11. Fundamental-rights baseline

Article 1 states an internal-market and innovation purpose alongside a high level of protection of health, safety and fundamental rights enshrined in the Charter, including democracy, rule of law and environmental protection. The Charter (`EU-004`) is binding within its scope of application, but Charter applicability to a concrete actor/scenario requires a separate scope analysis.

```text
CHARTER_REFERENCE != AUTOMATIC_STANDALONE_CLAIM
AI_ACT_COMPLIANCE != GDPR_COMPLIANCE
AI_ACT_COMPLIANCE != PRODUCT_LIABILITY_DEFENCE
```

## 12. R003 stop boundary / unresolved dependencies

R003 does not attempt to resolve:

- every delegated or implementing act adopted under the AI Act;
- current national competent-authority designations and national penalty legislation in every Member State;
- Member-State laws authorising real-time remote biometric identification;
- national transposition of `EU-003` Product Liability Directive or `EU-009` NIS2;
- Member-State-specific labour, consumer, procedural or public-law overlays;
- CJEU or national case law applying the AI Act;
- private-law breach, causation, damages, insurance or remedy conclusions for a concrete incident;
- whether any particular AI system/model is legally within a classification without facts and actor/use-case analysis.

These are separate research units or fact-specific legal questions.

```text
R003_L1_L2_BASELINE = COMPLETE
MEMBER_STATE_IMPLEMENTATION_MAP = NOT_ATTEMPTED
CASE_LAW_MAP = NOT_ATTEMPTED
LIABILITY_CONCLUSION = NOT_ATTEMPTED
NOTEBOOK_UPLOADS = 0
DERIVED_MARKDOWN_CREATED = 0
ZIP_OR_ARTIFACT_CREATED = NO
AUTO_ADVANCE = NO
```
