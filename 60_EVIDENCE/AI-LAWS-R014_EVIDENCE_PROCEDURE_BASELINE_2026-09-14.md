# AI-LAWS-R014 — Evidence and Procedure Baseline

**UNIT_ID:** `AI-LAWS-R014`  
**RESEARCH_DATE:** 2026-09-14  
**STATE:** `COMPLETE_RESEARCH_BASELINE_L1_L2_EVIDENCE_PROCEDURE_EU_US_FEDERAL_SCOPE_LIMITS_OPEN`  
**ROLE:** `COMPARATIVE_LAW_RESEARCHER`  
**LEGAL_ADVICE:** NO  
**AUTO_ADVANCE:** NO

## 1. Bounded scope

R014 establishes a bounded evidence/procedure crosswalk for:

- EU regulatory record creation/retention under the controlled AI Act;
- EU Product Liability Directive disclosure and burden/presumption architecture;
- GDPR accountability, access and processing-record duties relevant to evidence generation and access;
- U.S. federal civil discovery, ESI production/preservation and missing-ESI consequences under the current Federal Rules of Civil Procedure.

It does **not** establish Member-State civil procedure, U.S. state procedure, a universal AI evidence rule, case-specific sanctions, or an automatic bridge from regulatory noncompliance to civil liability.

R005/R006 are not reopened. R019 is not started. Notebook ingestion is not performed.

## 2. Source/currentness baseline

The EU analysis uses repository PDFs previously verified as exact official EUR-Lex byte matches:

- `EU-001` — current consolidated AI Act, snapshot `2026-07-27`, SHA-256 `1ccd38d1c78482cf2053b70110115adcc5080700acc8bd7bead8cb3579143ccf`;
- `EU-003` — Directive (EU) 2024/2853 Product Liability Directive, SHA-256 `86982bf66ec10cce529fa5030096422a35cb9c88beb855c3129389dcb4562057`;
- `EU-005` — GDPR, SHA-256 `bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499`.

For the United States, R014 freshly resolved the Administrative Office of the U.S. Courts current FRCP page. The page states that the Civil Rules were last amended in 2025 and exposes the official **Federal Rules of Civil Procedure Pamphlet, Dec. 1, 2025**. The exact official PDF returned HTTP 200, `application/pdf`, 415707 bytes and SHA-256 `bd8705fc038d87e4fe222a7ea2e4324222c9430e2373fce56826bd2dfa2f8baf`.

```text
CURRENT_RULES_PAGE_VERIFIED != EVERY_RULE_AMENDED_IN_2025
REGULATORY_RETENTION != LITIGATION_PRESERVATION
DATA_SUBJECT_ACCESS != CIVIL_DISCOVERY
DISCLOSURE_DUTY != AUTOMATIC_ADVERSE_INFERENCE
MISSING_RECORD != AUTOMATIC_LIABILITY
```

## 3. Evidence/procedure grammar

R014 keeps the following mechanisms separate:

```text
RECORD_CREATION
RECORD_RETENTION
LITIGATION_PRESERVATION
ACCESS
DISCLOSURE
DISCOVERY_SCOPE
PRODUCTION_FORMAT
BURDEN_OF_PROOF
REBUTTABLE_PRESUMPTION
MISSING_RECORD_CONSEQUENCE
PRIVILEGE_CONFIDENTIALITY
CASE_LAW_DEPENDENCY
```

A duty in one category is not silently converted into another.

## 4. EU AI Act — logging and retention

### Article 12 — record-keeping capability

The controlled consolidated text requires high-risk AI systems to technically allow automatic recording of events (logs) over the system lifetime. Logging capabilities must support traceability appropriate to the intended purpose, including identifying risk/substantial-modification situations, post-market monitoring, and monitoring operation under the relevant deployer provision.

This is a **regulatory system-design and traceability requirement**, not a civil discovery rule.

### Article 19 — provider retention

Providers of high-risk AI systems must keep automatically generated Article 12 logs to the extent they are under the provider's control. The controlled text sets a period appropriate to the intended purpose and **at least six months**, unless applicable Union or national law provides otherwise, including data-protection law.

### Article 26(6) — deployer retention

Deployers of high-risk AI systems likewise must keep automatically generated logs under their control for an appropriate period of **at least six months**, unless applicable Union or national law provides otherwise.

### Phased-application gate

R003 remains controlling for date-state. The high-risk core for Article 6(2)/Annex III is future `2027-12-02`, and the Article 6(1)/Annex I core is future `2028-08-02` in the controlled consolidated state.

```text
CURRENT_PROVISION_TEXT_VERIFIED != UNIVERSAL_CURRENT_APPLICABILITY
SIX_MONTH_REGULATORY_MINIMUM != MAXIMUM_RETENTION_PERIOD
SIX_MONTH_REGULATORY_MINIMUM != FRCP_LITIGATION_HOLD
```

## 5. EU Product Liability Directive — disclosure and proof

### Article 9 — disclosure of evidence

Directive (EU) 2024/2853 requires Member States to provide a disclosure mechanism in qualifying product-liability proceedings. A claimant who presents facts/evidence sufficient to support plausibility may obtain relevant evidence at the defendant's disposal, subject to Article 9 conditions. A defendant may also seek relevant evidence at the claimant's disposal under the Directive's conditions and national law.

Disclosure must be limited to what is **necessary and proportionate**. National courts must account for legitimate interests, confidentiality and trade secrets, and can require disclosed material to be presented in an accessible and understandable form where proportionate. Article 9 expressly leaves national pre-trial disclosure rules unaffected.

### Article 10 — burden and rebuttable presumptions

The claimant retains the baseline burden to prove defectiveness, damage and causal link. The Directive then creates specified rebuttable presumptions, including:

- defectiveness where the defendant fails to disclose relevant evidence under Article 9(1);
- defectiveness for qualifying noncompliance with mandatory product-safety requirements intended to protect against the relevant risk;
- defectiveness for qualifying obvious malfunction;
- causal link where established defectiveness and the type of damage are typically consistent;
- defectiveness and/or causal link in qualifying technically or scientifically complex cases where the claimant meets the Directive's likelihood threshold.

All Article 10 presumptions are rebuttable.

### Transposition gate

The transposition deadline remains **2026-12-09**. R014 therefore treats Articles 9–10 as verified Union legislative architecture, not as proof that every Member State already applies an identical national procedure on 2026-09-14.

```text
PLD_DISCLOSURE_RULE_VERIFIED != MEMBER_STATE_PROCEDURE_VERIFIED
PLD_PRESUMPTION != AUTOMATIC_LIABILITY
FAILURE_TO_DISCLOSE_UNDER_ART9 != EVERY_FORM_OF_MISSING_LOG
TECHNICAL_COMPLEXITY != BURDEN_REVERSAL_WITHOUT_ART10_CONDITIONS
```

## 6. GDPR — accountability/access/records interface

The controlled GDPR text supplies several evidence-relevant duties but not a general civil-discovery code:

- Article 5(2): the controller is responsible for and must be able to demonstrate compliance with the Article 5(1) principles;
- Article 15: a data subject has a right of access to personal data concerning them and specified information about processing;
- Article 28(3)(h): processors must make available to controllers information necessary to demonstrate compliance with Article 28 and allow/contribute to audits under the provision;
- Article 30: controllers and processors within scope must maintain records of processing activities and make them available to the supervisory authority on request.

These mechanisms can generate or expose records, but they are not treated as a substitute for civil discovery, litigation preservation, evidentiary admissibility or an adverse-inference doctrine.

```text
GDPR_ACCOUNTABILITY != FRCP_DISCOVERY
GDPR_ART15_ACCESS != PARTY_DISCOVERY_REQUEST
GDPR_ART30_RECORD != AI_LOG_AUTOMATICALLY
GDPR_RECORD_DUTY != PERMANENT_RETENTION
```

## 7. U.S. Federal Rules of Civil Procedure — discovery and ESI

### Scope boundary

The current official U.S. Courts page states that the Federal Rules of Civil Procedure govern civil proceedings in United States district courts. R014 does not generalize them to state courts, criminal proceedings, administrative proceedings, arbitration, or foreign litigation.

### Rule 16 — scheduling and ESI preservation

The current pamphlet provides that a scheduling order may address disclosure, discovery, or preservation of electronically stored information. This confirms that ESI preservation can be an express case-management subject in federal civil litigation.

### Rule 26 — disclosure, proportional discovery, preservation planning

Rule 26 includes required disclosures and provides that discovery generally reaches nonprivileged matter relevant to a party's claim or defense and **proportional to the needs of the case**, considering the rule's listed factors. Rule 26(f) discovery planning expressly includes issues about disclosure, discovery, or preservation of ESI and production form.

### Rule 34 — production of ESI

Rule 34 permits requests for designated documents and ESI within Rule 26(b)'s scope that are in the responding party's possession, custody, or control. The rule addresses requested production forms and, absent specification, requires ESI production in the form in which it is ordinarily maintained or in a reasonably usable form.

### Rule 37(e) — failure to preserve ESI

Rule 37(e) addresses ESI that should have been preserved in anticipation or conduct of litigation, is lost because a party failed to take reasonable steps to preserve it, and cannot be restored or replaced through additional discovery.

The current text separates consequences:

- upon finding prejudice, a court may order measures no greater than necessary to cure the prejudice;
- only upon finding **intent to deprive** another party of the information's use in the litigation may the court presume the lost information was unfavorable, instruct the jury that it may or must so presume, or dismiss the action / enter default judgment.

```text
RULE37E_TRIGGER != ORDINARY_DATA_DELETION_AUTOMATICALLY
PREJUDICE != INTENT_TO_DEPRIVE
ADVERSE_PRESUMPTION_REQUIRES_RULE37E_2_FINDING
AI_ACT_LOG_RETENTION_BREACH != RULE37E_SANCTION_AUTOMATICALLY
```

## 8. Cross-regime missing-record analysis

R014 establishes three different consequence models:

| Layer | Missing/withheld record condition | Potential consequence | Automatic? |
|---|---|---|---|
| AI Act | regulated actor/system fails applicable logging/retention duty | regulatory noncompliance consequences depend on applicable AI Act enforcement regime | No civil inference established here |
| PLD Article 10(2)(a) | defendant fails to disclose relevant evidence pursuant to Article 9(1) | rebuttable presumption of product defectiveness | Only within Article 10 conditions |
| FRCP Rule 37(e) | qualifying ESI should have been preserved, is lost through failure of reasonable steps, and cannot be restored/replaced | curative measures; harsher adverse-presumption/dismissal/default only with intent-to-deprive finding | No |

No rule is imported across jurisdictions or causes of action.

## 9. What R014 does not establish

R014 does not establish:

- EU Member-State implementation of PLD Articles 9–10;
- national procedural sanctions for failure to disclose beyond the Directive text;
- CJEU/national case law interpreting PLD technical-complexity presumptions;
- U.S. state discovery or spoliation law;
- case law defining anticipation of litigation, reasonable steps, prejudice or intent to deprive under Rule 37(e);
- whether a specific AI provider/deployer's logs are within a litigant's possession, custody or control;
- privilege, work-product, trade-secret or confidentiality outcomes in a concrete dispute;
- admissibility/authentication of AI logs;
- a universal legal duty to preserve every AI interaction indefinitely;
- liability, breach or sanctions in any actual incident.

## 10. Close state

```text
R014_EU_CONTROLLED_SOURCES = 3
R014_AI_ACT_ART12_LOGGING = VERIFIED_CURRENT_CONTROLLED_TEXT
R014_AI_ACT_ART19_PROVIDER_LOG_RETENTION = VERIFIED_CURRENT_CONTROLLED_TEXT
R014_AI_ACT_ART26_6_DEPLOYER_LOG_RETENTION = VERIFIED_CURRENT_CONTROLLED_TEXT
R014_AI_ACT_MINIMUM_LOG_RETENTION = AT_LEAST_6_MONTHS_SUBJECT_TO_OTHER_LAW
R014_PLD_ART9_DISCLOSURE = VERIFIED_PRIMARY_TEXT
R014_PLD_ART10_BURDEN_PRESUMPTIONS = VERIFIED_PRIMARY_TEXT
R014_PLD_TRANSPOSITION_DEADLINE = 2026-12-09
R014_PLD_MEMBER_STATE_PROCEDURE_MAP = NOT_ATTEMPTED
R014_GDPR_ACCOUNTABILITY_ACCESS_RECORDS = VERIFIED_PRIMARY_TEXT
R014_USCOURTS_CURRENT_FRCP_PAGE = VERIFIED_HTTP_200
R014_FRCP_CURRENT_PAMPHLET_DATE = 2025-12-01
R014_FRCP_PDF_SHA256 = bd8705fc038d87e4fe222a7ea2e4324222c9430e2373fce56826bd2dfa2f8baf
R014_FRCP_RULE26_DISCOVERY_PROPORTIONALITY_ESI_PLANNING = VERIFIED
R014_FRCP_RULE34_ESI_PRODUCTION = VERIFIED
R014_FRCP_RULE37E_ESI_PRESERVATION_CONSEQUENCES = VERIFIED
R014_US_STATE_PROCEDURE = NOT_ATTEMPTED
R014_CASE_LAW = NOT_ATTEMPTED
R014_NOTEBOOK_UPLOADS = 0
R014_NEW_REPOSITORY_BINARIES = 0
R014_DERIVED_MARKDOWN_CREATED = 0
R014_GLOBAL_AI_EVIDENCE_RULE = NOT_INFERRED
R014_LEGAL_CONCLUSION = NOT_ATTEMPTED
UNKNOWN_PRESERVED = YES
AUTO_ADVANCE = NO
STOP = YES
```
