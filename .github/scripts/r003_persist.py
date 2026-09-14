from pathlib import Path
import csv
import io

DATE = "2026-09-14"


def write(path, text):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.rstrip() + "\n", encoding="utf-8")


profile = r'''# AI-LAWS — European Union AI Act Current Consolidated / Phased-Application Map

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
'''

matrix = '''claim_id,topic,provision,application_state_2026_09_14,application_or_deadline_date,source_id,authority_state,dependency_or_limit,claim_state
R003-EU-001,Entry into force,Article 113,IN_FORCE,2024-08-01,EU-001,BINDING_EU_REGULATION,Currentness refresh required,VERIFIED_BASELINE
R003-EU-002,Chapters I and II general tranche,Article 113(a),APPLICABLE,2025-02-02,EU-001,BINDING_EU_REGULATION,New Article 5 ba/bb and 1a/1b excluded until 2026-12-02,VERIFIED_BASELINE
R003-EU-003,AI literacy,Article 4,APPLICABLE,2025-02-02,EU-001,BINDING_EU_REGULATION,Context-sensitive measures; no guaranteed individual literacy level,VERIFIED_BASELINE
R003-EU-004,Most prohibited practices,Article 5 and Article 113(a),APPLICABLE,2025-02-02,EU-001,BINDING_EU_REGULATION,National-law dependencies remain for specified real-time RBI authorisation,VERIFIED_BASELINE
R003-EU-005,New intimate/sexually-explicit and CSAM-related prohibited-practice additions,Article 5(1)(ba)/(bb) and 1a/1b,FUTURE_APPLICATION,2026-12-02,EU-001;EU-002,BINDING_EU_REGULATION,Not yet applicable on 2026-09-14,VERIFIED_BASELINE
R003-EU-006,Chapter III Section 4 + Chapter V + Chapter VII + Chapter XII + Article 78,Article 113(b),APPLICABLE,2025-08-02,EU-001,BINDING_EU_REGULATION,Article 101 excluded from this tranche,VERIFIED_BASELINE
R003-EU-007,General application date,Article 113,APPLICABLE,2026-08-02,EU-001,BINDING_EU_REGULATION,Does not override provision-specific dates,VERIFIED_BASELINE
R003-EU-008,Articles 102 to 110,Article 113(d),APPLICABLE,2026-07-27,EU-001;EU-002,BINDING_EU_REGULATION,Current consolidated text controls,VERIFIED_BASELINE
R003-EU-009,Annex III high-risk core,Chapter III Sections 1-3 / Article 6(2),FUTURE_APPLICATION,2027-12-02,EU-001;EU-002,BINDING_EU_REGULATION,Article 6(5) excluded from deferral,VERIFIED_BASELINE
R003-EU-010,Annex I product high-risk core,Chapter III Sections 1-3 / Article 6(1),FUTURE_APPLICATION,2028-08-02,EU-001;EU-002,BINDING_EU_REGULATION,Article 6(5) excluded from deferral; sectoral legislation interactions,VERIFIED_BASELINE
R003-EU-011,Transparency architecture,Article 50,APPLICABLE,2026-08-02,EU-001,BINDING_EU_REGULATION,Article 111(4) creates legacy transition specifically for Article 50(2),VERIFIED_BASELINE
R003-EU-012,Legacy synthetic-content systems Article 50(2),Article 111(4),TRANSITION_ACTIVE,2026-12-02,EU-001;EU-002,BINDING_EU_REGULATION,For systems in scope placed before 2026-08-02,VERIFIED_BASELINE
R003-EU-013,GPAI Chapter V,Chapter V / Article 113(b),APPLICABLE,2025-08-02,EU-001,BINDING_EU_REGULATION,Pre-2025-08-02 GPAI models have Article 111(3) transition,VERIFIED_BASELINE
R003-EU-014,Legacy GPAI models,Article 111(3),TRANSITION_ACTIVE,2027-08-02,EU-001,BINDING_EU_REGULATION,Applies to GPAI models placed before 2025-08-02,VERIFIED_BASELINE
R003-EU-015,Legacy high-risk systems for public-authority use,Article 111(2),FUTURE_COMPLIANCE_DEADLINE,2030-08-02,EU-001;EU-002,BINDING_EU_REGULATION,Article 111 conditions and significant-design-change rule must be applied,VERIFIED_BASELINE
R003-EU-016,Annex X large-scale IT-system components,Article 111(1),FUTURE_COMPLIANCE_DEADLINE,2030-12-31,EU-001,BINDING_EU_REGULATION,Article 5 earlier application remains without prejudice,VERIFIED_BASELINE
R003-EU-017,National AI regulatory sandbox minimum,Amended Article 57 context,FUTURE_OPERATIONAL_DEADLINE,2027-08-02,EU-002,BINDING_EU_REGULATION,National implementation details not mapped in R003,VERIFIED_BASELINE
R003-EU-018,Article 2(13) high-risk Annex I limitation mechanism,Article 2(13),DELEGATED_ACT_DEPENDENCY,2027-08-02,EU-001;EU-002,BINDING_EU_REGULATION,Commission delegated acts required to specify systems/requirements/conditions/scope,VERIFIED_BASELINE
'''

interactions = '''source_id,instrument,authority_class,interaction_with_ai_act,current_state_2026_09_14,r003_limit
EU-002,Regulation (EU) 2026/1744,STATUTE_OR_REGULATION,Direct amendment to AI Act including phased-application and high-risk architecture,IN_FORCE_AND_REFLECTED_IN_2026_07_27_CONSOLIDATION,R003 maps operative amendments but not every amendment in the omnibus package
EU-003,Directive (EU) 2024/2853 Product Liability Directive,STATUTE_OR_REGULATION,Separate product-liability architecture potentially relevant to defective AI-enabled products,TRANSPOSITION_DEPENDENT,Directive text verified does not establish Member-State transposition or liability in a concrete case
EU-004,Charter of Fundamental Rights of the European Union,CONSTITUTIONAL_TEXT,Article 1 fundamental-rights baseline and broader EU-law rights context,BINDING_WITHIN_SCOPE_OF_EU_LAW,Concrete Charter applicability requires scope analysis
EU-005,Regulation (EU) 2016/679 GDPR,STATUTE_OR_REGULATION,Article 2(7) preserves EU data-protection/privacy law; AI Act does not displace GDPR,APPLICABLE,AI Act compliance is not GDPR compliance and lawful-basis/data-rights questions remain separate
EU-006,Regulation (EU) 2022/2065 Digital Services Act,STATUTE_OR_REGULATION,Article 2(5) preserves Chapter II intermediary-service liability rules,APPLICABLE,No conflict/priority conclusion beyond the explicit non-displacement clause
EU-007,Regulation (EU) 2023/2854 Data Act,STATUTE_OR_REGULATION,Data access/use and connected-product context potentially overlaps AI systems and products,APPLICABLE_GENERAL_2025_09_12_ART3_1_DATE_2026_09_12_PASSED,R003 does not decide provision-specific overlap or priority
EU-008,Regulation (EU) 2022/868 Data Governance Act,STATUTE_OR_REGULATION,Data-governance/reuse/intermediation context,APPLICABLE,R003 records context only; no automatic AI Act duty inference
EU-009,Directive (EU) 2022/2555 NIS2,STATUTE_OR_REGULATION,Cybersecurity risk-management/incident context may overlap AI operators/entities,EU_DIRECTIVE_NATIONAL_TRANSPOSITION_REQUIRED,Member-State implementation must be checked separately
EU-010,Regulation (EU) 2024/2847 Cyber Resilience Act,STATUTE_OR_REGULATION,Product cybersecurity interaction for products with digital elements including AI-enabled products where in scope,CHAPTER_IV_APPLICABLE_2026_06_11_ARTICLE_14_APPLICABLE_2026_09_11_GENERAL_2027_12_11,R003 does not resolve product-scope or lex-specialis questions
INT-001,CETS No.225 Council of Europe Framework Convention,TREATY_OR_INTERNATIONAL_INSTRUMENT,Related European human-rights/democracy/rule-of-law treaty layer but not EU secondary law,PARTY_SPECIFIC_STATUS_REQUIRES_LIVE_TREATY_CHECK,Do not treat treaty status or domestic effect as resolved by R003
'''

closeout = r'''# AI-LAWS — R003 Closeout

**WORK_ITEM:** `AI-LAWS-R003`  
**DATE:** 2026-09-14  
**SCOPE:** EU AI Act current consolidated / phased-application L1/L2 legal map plus interaction-source inventory  
**EXECUTION_CHANNEL:** GitHub / GitHub Actions  
**AUTO_ADVANCE:** NO

## Result

R003 establishes a controlled European Union AI Act baseline using the already validated `EU-001` and `EU-002` exact-official repository snapshots and the same-day R030 currentness state.

Principal correction:

```text
AI_ACT_GENERAL_APPLICATION = 2026-08-02
BUT
CHAPTER_III_SECTIONS_1_2_3_ART6_2_ANNEX_III = 2027-12-02
CHAPTER_III_SECTIONS_1_2_3_ART6_1_ANNEX_I = 2028-08-02
```

Regulation (EU) 2026/1744 therefore prevents use of the obsolete assumption that the entire high-risk AI compliance core became generally applicable on 2 August 2026.

Other controlled date states include:

```text
CHAPTERS_I_II = 2025-02-02
NEW_ARTICLE_5_BA_BB_1A_1B = 2026-12-02
CHAPTER_III_SECTION_4 = 2025-08-02
CHAPTER_V_GPAI = 2025-08-02 subject to Article 111 legacy transition
CHAPTER_VII = 2025-08-02
CHAPTER_XII = 2025-08-02 except Article 101
ARTICLES_102_110 = 2026-07-27
ARTICLE_50_GENERAL_LAYER = 2026-08-02 subject to Article 111(4) legacy Article 50(2) transition
```

## Currentness boundary

The R003 GitHub verification run attempted fresh live EUR-Lex ELI/PDF reads. Those calls returned HTTP 202 with no substantive PDF body in that runner session. The result is classified as an access/currentness-recheck limitation, not a source mismatch.

The R030 same-day state remains authoritative inside the project:

```text
EU001_OFFICIAL_CURRENT_CONSOLIDATED_2026_07_27 = VERIFIED
EU001_REPOSITORY_EXACT_OFFICIAL_BYTE_MATCH = YES
EU002_REPOSITORY_EXACT_OFFICIAL_BYTE_MATCH = YES
R003_LIVE_FETCH = PARTIAL_HTTP_202_EMPTY_BODY
NEWER_CONSOLIDATION_PROVED_BY_R003 = NO
```

## Durable outputs

- `20_JURISDICTIONS/EU/EU_AI_ACT_CURRENT_CONSOLIDATED_PHASED_APPLICATION_MAP_2026-09-14.md`
- `20_JURISDICTIONS/EU/EU_AI_ACT_PHASED_APPLICATION_MATRIX.csv`
- `20_JURISDICTIONS/EU/EU_AI_ACT_INTERACTION_SOURCE_INVENTORY.csv`
- this closeout
- updated jurisdiction registry, research queue and current context

## Stop boundary

R003 does not establish Member-State-specific implementation, national penalty procedure, real-time biometric authorisation law, PLD/NIS2 transposition, case law, concrete-system classification, breach, causation, damages or remedies.

```text
R003_STATE = COMPLETE_RESEARCH_BASELINE_L1_L2
MEMBER_STATE_IMPLEMENTATION = NOT_ATTEMPTED
CASE_LAW = NOT_ATTEMPTED
LIABILITY_CONCLUSION = NOT_ATTEMPTED
NOTEBOOK_UPLOADS = 0
NEW_SOURCE_DOWNLOADS_COMMITTED = 0
DERIVED_MARKDOWN_CREATED = 0
ZIP_OR_ARTIFACT_CREATED = NO
UNKNOWN_PRESERVED = YES
AUTO_ADVANCE = NO
```
'''

write('20_JURISDICTIONS/EU/EU_AI_ACT_CURRENT_CONSOLIDATED_PHASED_APPLICATION_MAP_2026-09-14.md', profile)
write('20_JURISDICTIONS/EU/EU_AI_ACT_PHASED_APPLICATION_MATRIX.csv', matrix)
write('20_JURISDICTIONS/EU/EU_AI_ACT_INTERACTION_SOURCE_INVENTORY.csv', interactions)
write('95_RESEARCH/EU/AI-LAWS-R003_CLOSEOUT_2026-09-14.md', closeout)

# Update jurisdiction registry deterministically.
reg_path = Path('20_JURISDICTIONS/JURISDICTION_RESEARCH_REGISTRY.csv')
rows = list(csv.DictReader(reg_path.read_text(encoding='utf-8').splitlines()))
found = False
for r in rows:
    if r['jurisdiction_id'] == 'REG-EU':
        r['research_state'] = 'AI_ACT_L1_L2_BASELINE_COMPLETE_MEMBER_STATE_DEPENDENCIES_OPEN'
        r['initial_focus'] = 'AI Act current consolidated/phased application; data protection; product safety/liability; consumer; cyber; competition'
        r['notes'] = ('R003 completed EU AI Act L1/L2 current baseline on 2026-09-14 using the verified 2026-07-27 consolidated text and Regulation (EU) 2026/1744. '
                      'High-risk Chapter III Sections 1-3 are phased to 2027-12-02 for Article 6(2)/Annex III and 2028-08-02 for Article 6(1)/Annex I. '
                      'Member-State implementation, national procedures, delegated/implementing acts refresh and case law remain separate research dependencies.')
        found = True
if not found:
    raise SystemExit('REG-EU registry row missing')
out = io.StringIO(newline='')
w = csv.DictWriter(out, fieldnames=rows[0].keys(), lineterminator='\n')
w.writeheader(); w.writerows(rows)
reg_path.write_text(out.getvalue(), encoding='utf-8')

# Update research queue deterministically.
q_path = Path('90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv')
qrows = list(csv.DictReader(q_path.read_text(encoding='utf-8').splitlines()))
found = False
for r in qrows:
    if r['work_item_id'] == 'AI-LAWS-R003':
        r['state'] = 'COMPLETE_RESEARCH_BASELINE_L1_L2'
        r['expected_output'] = ('20_JURISDICTIONS/EU/EU_AI_ACT_CURRENT_CONSOLIDATED_PHASED_APPLICATION_MAP_2026-09-14.md; '
                                '20_JURISDICTIONS/EU/EU_AI_ACT_PHASED_APPLICATION_MATRIX.csv; '
                                '20_JURISDICTIONS/EU/EU_AI_ACT_INTERACTION_SOURCE_INVENTORY.csv; '
                                '95_RESEARCH/EU/AI-LAWS-R003_CLOSEOUT_2026-09-14.md')
        r['stop_condition'] = ('L1/L2 current AI Act phased-application baseline complete; stop before Member-State implementation/transposition, case law, concrete classification or liability conclusions')
        found = True
if not found:
    raise SystemExit('R003 queue row missing')
out = io.StringIO(newline='')
w = csv.DictWriter(out, fieldnames=qrows[0].keys(), lineterminator='\n')
w.writeheader(); w.writerows(qrows)
q_path.write_text(out.getvalue(), encoding='utf-8')

# Update current context with exact controlled replacements.
ctx_path = Path('00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md')
ctx = ctx_path.read_text(encoding='utf-8')
if 'R003_EU_AI_ACT_L1_L2_COMPLETE' not in ctx:
    old = '**STATE:** R001_COMPLETE / '
    if old not in ctx:
        raise SystemExit('context STATE anchor missing')
    ctx = ctx.replace(old, '**STATE:** R001_COMPLETE / R003_EU_AI_ACT_L1_L2_COMPLETE / ', 1)

if 'AI-LAWS-R003 = COMPLETE_RESEARCH_BASELINE_L1_L2' not in ctx:
    anchor = 'AI-LAWS-R001 = COMPLETE_SUPPORTING_RESEARCH_IMPORT\n'
    if anchor not in ctx:
        raise SystemExit('completed-units anchor missing')
    ctx = ctx.replace(anchor, anchor + 'AI-LAWS-R003 = COMPLETE_RESEARCH_BASELINE_L1_L2\n', 1)

section = r'''### R003 — EU AI Act current consolidated / phased-application legal map

R003 created the EU L1/L2 current-law baseline from the controlled `EU-001` 2026-07-27 consolidated snapshot and `EU-002` Regulation (EU) 2026/1744.

```text
AI_ACT_GENERAL_APPLICATION = 2026-08-02
CHAPTERS_I_II = APPLICABLE_FROM_2025-02-02
NEW_ARTICLE_5_BA_BB_1A_1B = FUTURE_2026-12-02
CHAPTER_V_GPAI = APPLICABLE_FROM_2025-08-02_WITH_ARTICLE_111_LEGACY_TRANSITION
HIGH_RISK_ART6_2_ANNEX_III_CORE = FUTURE_2027-12-02
HIGH_RISK_ART6_1_ANNEX_I_CORE = FUTURE_2028-08-02
ARTICLES_102_110 = APPLICABLE_FROM_2026-07-27
R003_LIVE_EURLEX_RECHECK = PARTIAL_HTTP_202_EMPTY_BODY
R030_SAME_DAY_CURRENTNESS_PIN = PRESERVED
MEMBER_STATE_IMPLEMENTATION = NOT_ATTEMPTED
CASE_LAW = NOT_ATTEMPTED
LIABILITY_CONCLUSION = NOT_ATTEMPTED
```

Durable outputs are under `20_JURISDICTIONS/EU/` plus `95_RESEARCH/EU/AI-LAWS-R003_CLOSEOUT_2026-09-14.md`.

'''
if '### R003 — EU AI Act current consolidated / phased-application legal map' not in ctx:
    anchor = '### R021\n'
    if anchor not in ctx:
        raise SystemExit('R021 section anchor missing')
    ctx = ctx.replace(anchor, section + anchor, 1)

old_next = '''### Preferred substantive legal-research unit\n\n```text\nAI-LAWS-R003 — EU AI ACT CURRENT CONSOLIDATED / PHASED-APPLICATION LEGAL MAP\nSTATE = READY FOR EXPLICIT AUTHORIZATION\n```\n\nR003 remains unstarted. R025 source validation does not constitute R003 substantive legal analysis.\n'''
new_next = '''### Completed preferred substantive legal-research unit\n\n```text\nAI-LAWS-R003 — EU AI ACT CURRENT CONSOLIDATED / PHASED-APPLICATION LEGAL MAP\nSTATE = COMPLETE_RESEARCH_BASELINE_L1_L2\n```\n\nR003 is complete at L1/L2 baseline level. No subsequent substantive research unit is auto-started. Member-State implementation/transposition, case law, delegated/implementing-act refresh and concrete liability/classification questions remain separate bounded work.\n'''
if old_next in ctx:
    ctx = ctx.replace(old_next, new_next, 1)
elif 'STATE = COMPLETE_RESEARCH_BASELINE_L1_L2' not in ctx:
    raise SystemExit('preferred R003 next-unit block not found')

if 'R003_EU_AI_ACT_HIGH_RISK_ANNEX_III_CORE_DATE' not in ctx:
    anchor = 'NOTEBOOK_UPLOAD_COUNT = 0\n'
    if anchor not in ctx:
        raise SystemExit('integrity anchor missing')
    additions = '''R003_EU_AI_ACT_BASELINE = COMPLETE_L1_L2\nR003_EU_AI_ACT_CONSOLIDATED_SNAPSHOT = 2026-07-27\nR003_EU_AI_ACT_HIGH_RISK_ANNEX_III_CORE_DATE = 2027-12-02\nR003_EU_AI_ACT_HIGH_RISK_ANNEX_I_CORE_DATE = 2028-08-02\nR003_LIVE_EURLEX_RECHECK = PARTIAL_HTTP_202_EMPTY_BODY\nR003_MEMBER_STATE_IMPLEMENTATION = NOT_ATTEMPTED\nR003_CASE_LAW = NOT_ATTEMPTED\nR003_LIABILITY_CONCLUSION = NOT_ATTEMPTED\n'''
    ctx = ctx.replace(anchor, additions + anchor, 1)

if '**AUTO_ADVANCE:** NO' not in ctx:
    raise SystemExit('AUTO_ADVANCE control missing')
ctx_path.write_text(ctx, encoding='utf-8')

# Final controlled assertions.
assert Path('20_JURISDICTIONS/EU/EU_AI_ACT_CURRENT_CONSOLIDATED_PHASED_APPLICATION_MAP_2026-09-14.md').exists()
assert Path('20_JURISDICTIONS/EU/EU_AI_ACT_PHASED_APPLICATION_MATRIX.csv').exists()
assert '2027-12-02' in Path('20_JURISDICTIONS/EU/EU_AI_ACT_PHASED_APPLICATION_MATRIX.csv').read_text(encoding='utf-8')
assert '2028-08-02' in Path('20_JURISDICTIONS/EU/EU_AI_ACT_PHASED_APPLICATION_MATRIX.csv').read_text(encoding='utf-8')
assert 'COMPLETE_RESEARCH_BASELINE_L1_L2' in q_path.read_text(encoding='utf-8')
assert 'AI_ACT_L1_L2_BASELINE_COMPLETE_MEMBER_STATE_DEPENDENCIES_OPEN' in reg_path.read_text(encoding='utf-8')
assert 'R003_EU_AI_ACT_L1_L2_COMPLETE' in ctx_path.read_text(encoding='utf-8')

print('R003_PERSIST_ASSERTIONS=PASS')
print('R003_STATE=COMPLETE_RESEARCH_BASELINE_L1_L2')
print('ANNEX_III_HIGH_RISK_CORE_DATE=2027-12-02')
print('ANNEX_I_HIGH_RISK_CORE_DATE=2028-08-02')
print('LIVE_EURLEX_RECHECK=PARTIAL_HTTP_202_EMPTY_BODY')
print('MEMBER_STATE_IMPLEMENTATION=NOT_ATTEMPTED')
print('CASE_LAW=NOT_ATTEMPTED')
print('LIABILITY_CONCLUSION=NOT_ATTEMPTED')
print('NOTEBOOK_UPLOADS=0')
print('DERIVED_MARKDOWN_CREATED=0')
print('ZIP_OR_ARTIFACT_CREATED=NO')
print('AUTO_ADVANCE=NO')
