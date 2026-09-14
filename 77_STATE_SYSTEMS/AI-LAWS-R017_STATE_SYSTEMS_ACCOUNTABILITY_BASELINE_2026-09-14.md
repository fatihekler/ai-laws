# AI-LAWS-R017 — State Systems / National-Security Accountability Baseline

**UNIT_ID:** `AI-LAWS-R017`  
**DATE:** 2026-09-14  
**SCOPE:** bounded EU + Council of Europe + U.S. federal baseline for national-security, defence, intelligence, sovereign-immunity, judicial-review and oversight dependencies affecting closed/state AI systems  
**LEGAL_ADVICE:** NO  
**AUTO_ADVANCE:** NO

## 1. Research question

What current public-law sources establish scope exclusions, alternative oversight, judicial-review/remedy routes or immunity limitations for state/national-security AI activity, without inferring classified facts or treating an exemption from one AI instrument as an exemption from all law?

## 2. Controlling integrity rules

```text
EXEMPT_FROM_AI_ACT != EXEMPT_FROM_ALL_LAW
NATIONAL_SECURITY_LABEL != CLASSIFIED_FACT_PROVEN
CLASSIFIED_OR_SECRET != UNREGULATED
SOVEREIGN_IMMUNITY != NO_DUTY
WAIVER_OF_IMMUNITY != AUTOMATIC_REMEDY
APA_702 != REVIEWABILITY_OR_SUCCESS_PROVEN
FTCA_WAIVER != CLAIM_WITHIN_SCOPE_PROVEN
FTCA_EXCEPTION != MERITS_DECISION
INSPECTOR_GENERAL_OVERSIGHT != PRIVATE_RIGHT_OF_ACTION
TREATY_TEXT != TREATY_IN_FORCE
PUBLIC_SOURCE_GAP != ACTUAL_OVERSIGHT_GAP
RUNNER_ACCESS_FAILURE != SOURCE_ABSENCE
```

R017 does not determine the legality of any classified system, intelligence operation, military AI deployment, autonomous weapon, surveillance program or named state actor.

## 3. European Union — AI Act scope boundary

The controlled `EU-STATE-001` source is the exact-official repository snapshot of Regulation (EU) 2024/1689 consolidated to 2026-07-27, already pinned by R003/R030 and re-extracted in R017.

Article 2 preserves Member-State national-security competence and contains scope exclusions for AI systems where and insofar as they are placed on the market, put into service or used exclusively for military, defence or national-security purposes. The exact provision and factual purpose of the system must therefore be established before applying the AI Act.

R017 adopts only the scope consequence:

```text
AI_ACT_ARTICLE_2_EXCLUSION
!= STATE_AI_HAS_NO_OTHER_LEGAL_CONSTRAINT
```

The exclusion does not itself answer whether constitutional, human-rights, criminal, administrative, procurement, secrecy, data-protection, sectoral, international-humanitarian-law or other rules apply. Those routes remain instrument- and fact-specific.

## 4. Council of Europe Framework Convention — future/comparative layer only

The repository CETS 225 treaty text was body/marker verified for Article 3 national-security and national-defence language. Article 3 permits a Party not to apply the Convention to activities related to protection of national-security interests subject to the Convention's stated international-law/human-rights/democratic-institution safeguard, while matters relating to national defence fall outside the Convention's scope.

However R004 remains controlling for current legal status. As of the verified Treaty Office state used by AI-LAWS, the treaty-wide Article 30 entry-into-force threshold had not been met: the European Union had deposited approval, while no Council of Europe member State had deposited a qualifying ratification/acceptance/approval.

Accordingly:

```text
CETS225_NATIONAL_SECURITY_TEXT = VERIFIED_TREATY_TEXT
CETS225_TREATY_WIDE_ENTRY_INTO_FORCE = NO_AS_R004_DATE_STATE
CETS225_TEXT != CURRENT_DOMESTIC_OBLIGATION_INFERRED
```

R017 uses Article 3 only to map the structural national-security/defence boundary, not to create a current enforceable remedy.

## 5. ECHR selected alternative rights/remedy layer

The live official European Convention on Human Rights PDF was acquired and marker-verified. Article 8 protects private and family life while allowing public-authority interference only under the Convention's legality and necessity conditions, including specified interests such as national security. Article 13 supplies a treaty-level effective-remedy guarantee for Convention rights.

R017 records this as a selected regional human-rights layer for Contracting Parties. It does not decide jurisdiction, victim status, exhaustion, admissibility, proportionality, margin-of-appreciation questions, state-secret procedure or the merits of any AI system.

```text
NATIONAL_SECURITY_PURPOSE != AUTOMATIC_ECHR_COMPLIANCE
ECHR_RIGHT != AUTOMATIC_DOMESTIC_DAMAGES_AWARD
```

## 6. United States — current OMB federal AI governance scope

`US-STATE-001` is the repository copy of OMB M-25-21; the live official White House PDF was freshly downloaded in R017 and matched exactly:

```text
SHA256 = 0aab0aa4eaeac969ed93894d3940c5dc9d0b7377048171b164a439e8b9e49813
PAGES = 25
LIVE_OFFICIAL_HTTP = 200
EXACT_REPOSITORY_LIVE_BYTE_IDENTITY = YES
```

The verified scope text states that the memorandum is directed to heads of all Executive Branch departments and agencies, including independent regulatory agencies. The document also frames national security among the objectives of federal AI use and directs agencies to maintain safeguards for civil rights, civil liberties and privacy.

The first R017 marker assumption that M-25-21 necessarily contained a separate `44 U.S.C. §3552 national-security-system exclusion` was not verified and was removed. R017 therefore makes neither an inclusion nor exclusion inference beyond the actual verified memorandum text.

```text
OMB_M2521 = EXECUTIVE_BRANCH_OPERATIONAL_MEMORANDUM
OMB_M2521 != ACT_OF_CONGRESS
UNVERIFIED_NSS_CARVEOUT != ADMITTED_RULE
```

Agency-, mission-, statute- and classified-system-specific authorities remain open.

## 7. United States — statutory national-security-system definition

The current Office of Law Revision Counsel text of 44 U.S.C. §3552 was live acquired and marker-verified. It defines `national security system` through specified functions and information categories, including intelligence/cryptologic activities and other national-security/military characteristics identified in the statute.

This definition can be incorporated by other federal instruments, but it does not itself impose an AI governance duty, waive immunity or create a private remedy.

```text
NATIONAL_SECURITY_SYSTEM_DEFINITION != AI_EXEMPTION_BY_ITSELF
```

## 8. United States — sovereign immunity, judicial review and money damages

### 8.1 APA 5 U.S.C. §702

The current official text was marker-verified. Section 702 provides a federal judicial-review route and addresses sovereign immunity for actions seeking relief other than money damages. Its own text preserves other limitations on judicial review and does not by itself establish that a particular agency action is reviewable, that a plaintiff has a valid cause of action, or that requested relief is available.

R017 therefore records:

```text
APA_702_NONMONEY_RELIEF_WAIVER = VERIFIED_STATUTORY_LAYER
PARTICULAR_NATIONAL_SECURITY_AI_REVIEWABILITY = NOT_DETERMINED
```

### 8.2 FTCA 28 U.S.C. §§1346(b), 2674, 2680

The current official texts were live acquired and marker-verified.

- Section 1346(b) supplies a jurisdictional route for specified money-damages claims against the United States based on negligent or wrongful acts/omissions of federal employees acting within scope, under the law specified by the statute.
- Section 2674 states the United States' liability rule in the same manner and to the same extent as a private individual under like circumstances, subject to statutory qualifications.
- Section 2680 contains exceptions, including the due-care/discretionary-function architecture and the foreign-country exception.

These provisions demonstrate that `sovereign immunity` is not a binary all-or-nothing proposition. They also demonstrate that a waiver route can be narrowed by statutory conditions and exceptions.

R017 does **not** complete the FTCA pathway. Administrative exhaustion, claim accrual, substitution, intentional-tort exceptions, military-specific doctrines, contractor questions, choice of governing state law, classified-evidence procedure and case law remain outside this bounded unit.

```text
FTCA_ROUTE_EXISTS != AI_CLAIM_SUCCEEDS
DISCRETIONARY_FUNCTION_EXCEPTION_POSSIBLE != CLAIM_BARRED_WITHOUT_ANALYSIS
FOREIGN_COUNTRY_EXCEPTION != R018_CROSS_BORDER_ANALYSIS_COMPLETE
```

## 9. United States — intelligence-community oversight layer

The current Office of Law Revision Counsel text of 50 U.S.C. §3033 was live acquired and marker-verified. It establishes the Inspector General of the Intelligence Community and an independent/objective statutory oversight function including investigations and related review responsibilities.

This confirms that a national-security/intelligence context cannot be reduced to `no oversight` merely because public transparency or ordinary AI-regulation routes are limited. At the same time, an Inspector General mechanism is not equivalent to public disclosure, Article III merits review, or a private damages action.

```text
ICIG_OVERSIGHT = VERIFIED_STATUTORY_LAYER
ICIG_OVERSIGHT != PUBLIC_TRANSPARENCY
ICIG_OVERSIGHT != PRIVATE_RIGHT_OF_ACTION
```

## 10. DoD autonomous-weapons source-access boundary

R017 probed the official DoD Directive 3000.09 PDF URL as a candidate department-specific operational layer. The GitHub-hosted runner returned `HTTP 403` with an HTML body, so R017 did not admit body-level findings from that directive.

```text
DOD_3000_09_RUNNER_STATE = HTTP_403
DOD_3000_09_BODY_VERIFIED_R017 = NO
RUNNER_403 != DIRECTIVE_ABSENT
```

The candidate remains suitable for a later source-specific recheck if required. R017 does not infer the directive's current detailed requirements from memory or secondary sources.

## 11. State-accountability dependency map

R017 distinguishes at least five analytically separate questions for a closed/state AI system:

1. **Instrument scope:** Is the activity excluded from the AI-specific instrument being tested?
2. **Alternative positive law:** Which constitutional, human-rights, administrative, tort, secrecy, intelligence, defence, procurement or sector rules still apply?
3. **Oversight forum:** Which court, inspector general, legislative, administrative or internal review body has authority?
4. **Remedy and immunity:** Is the requested form of relief within a valid waiver and outside an exception?
5. **Evidence/publicness:** Are facts publicly verifiable, classified, privileged, state-secret, sealed or otherwise unavailable?

A negative answer in one layer cannot be copied into another.

## 12. Public-evidence and classified-system firewall

R017 researched only public official sources. It did not identify, describe or infer the capabilities, deployments, targets, operational rules, incidents or failures of any classified system.

```text
NO_PUBLIC_RECORD != NO_SYSTEM
NO_PUBLIC_RECORD != NO_OVERSIGHT
NO_PUBLIC_RECORD != UNLAWFUL_CONDUCT
CLASSIFICATION != IMMUNITY
CLASSIFICATION != LIABILITY
```

Any later incident-specific or actor-specific analysis must establish facts from admissible/authorized evidence and apply the relevant secrecy/classification procedures separately.

## 13. Preserved UNKNOWNs / dependencies

- AI Act Article 2 fact-specific classification for any concrete state system: `NOT_ATTEMPTED`.
- EU Member-State constitutional/national-security/procedural remedies: `NOT_ATTEMPTED`.
- ECHR case-law on secret surveillance, national security or AI: `NOT_ATTEMPTED`.
- CETS 225 post-R004 treaty-status refresh beyond the controlled dated status: `NOT_ATTEMPTED_IN_R017`.
- U.S. agency-specific classified/national-security AI directives beyond M-25-21: `NOT_EXHAUSTIVE`.
- FTCA administrative-exhaustion and case-law map: `NOT_ATTEMPTED`.
- APA reviewability doctrines, statutory preclusion and national-security case law: `NOT_ATTEMPTED`.
- State-secrets privilege, classified-information procedures and security-clearance doctrines: `NOT_ATTEMPTED`.
- DoD Directive 3000.09 body/current version: `RUNNER_ACCESS_BLOCKED_R017`.
- Actual classified AI facts: `UNKNOWN_NOT_INFERRED`.
- U.S. state / other-country sovereign-immunity regimes: `NOT_ATTEMPTED`.

## 14. Research state

```text
R017_SCOPE = EU_COE_US_FEDERAL_STATE_SYSTEMS_ACCOUNTABILITY_BASELINE
R017_SOURCE_RECORDS = 12
R017_BODY_MARKER_VERIFIED = 11
R017_DOD300009 = HTTP_403_BODY_NOT_VERIFIED
R017_AI_ACT_NS_DEFENCE_SCOPE_BOUNDARY = VERIFIED_CONTROLLED_TEXT
R017_CETS225_NS_DEFENCE_SCOPE_TEXT = VERIFIED_WITH_R004_ENTRY_INTO_FORCE_GATE
R017_ECHR_ART8_ART13_LAYER = VERIFIED_OFFICIAL_TEXT
R017_OMB_M2521_LIVE_EXACT_REPOSITORY_MATCH = YES
R017_M2521_NSS_CARVEOUT = NOT_ESTABLISHED_BY_CONTROLLED_TEXT
R017_US_NSS_DEFINITION = VERIFIED_44_USC_3552
R017_APA_702_NONMONEY_REVIEW_LAYER = VERIFIED
R017_FTCA_1346B_2674_2680_LAYER = VERIFIED_WITH_UNMAPPED_DEPENDENCIES
R017_ICIG_50_USC_3033 = VERIFIED_OVERSIGHT_LAYER
R017_CLASSIFIED_FACTS = UNKNOWN_NOT_INFERRED
R017_LEGAL_CONCLUSION = NOT_ATTEMPTED
R017_NOTEBOOK_UPLOADS = 0
R017_NEW_THIRD_PARTY_BINARIES_VENDORED = 0
R017_ZIP_OR_WORKFLOW_ARTIFACT_CREATED = NO
AUTO_ADVANCE = NO
```