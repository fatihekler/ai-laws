# AI-LAWS-R018 — Cross-Border Jurisdiction / Applicable Law / Enforcement Baseline

**UNIT_ID:** `AI-LAWS-R018`  
**DATE:** 2026-09-14  
**LEVEL:** bounded L1/L2 baseline  
**LEGAL_ADVICE:** NO  
**AUTO_ADVANCE:** NO

## Purpose

R018 separates the legal questions that are often collapsed in cross-border AI disputes:

```text
REGULATORY_TERRITORIAL_SCOPE
FORUM / PERSONAL_JURISDICTION
SERVICE
VENUE
APPLICABLE_LAW
MERITS / LIABILITY
EVIDENCE_COOPERATION
JUDGMENT
RECOGNITION / ENFORCEMENT
```

None of these answers another automatically.

## Controlling non-equivalences

```text
EXTRATERRITORIAL_SCOPE != FORUM
FORUM != APPLICABLE_LAW
SERVICE != PERSONAL_JURISDICTION_PROVEN
VENUE != PERSONAL_JURISDICTION
APPLICABLE_LAW != LIABILITY
EVIDENCE_ASSISTANCE != JUDGMENT_RECOGNITION
JUDGMENT != AUTOMATIC_FOREIGN_ENFORCEMENT
FOREIGN_ACTOR != OUTSIDE_SCOPE_AUTOMATICALLY
CROSS_BORDER_HARM != UNIVERSAL_FORUM
```

## EU regulatory-scope interface

The controlled GDPR snapshot marker-verifies Article 3 territorial-scope concepts including establishment, offering goods/services and monitoring behaviour. This is a regulatory territorial-scope layer; R018 does not treat GDPR Article 3 as a civil jurisdiction or choice-of-law rule.

R003 previously verified the current consolidated AI Act Article 2 scope map, including third-country provider/deployer circumstances and Union-use/output interfaces. R018 reuses that controlled R003 result; the R018 verifier did not independently re-admit Article 2 text because its exact marker pair did not pass. AI Act scope is therefore not converted into a forum, governing-law or private-remedy rule.

## EU private-international-law source boundary

R018 identified the official EUR-Lex identities for:

- Regulation (EU) No 1215/2012 — jurisdiction and recognition/enforcement in civil and commercial matters (`Brussels I bis`);
- Regulation (EC) No 593/2008 — law applicable to contractual obligations (`Rome I`);
- Regulation (EC) No 864/2007 — law applicable to non-contractual obligations (`Rome II`).

GitHub-hosted runners received `HTTP 202` challenge bodies for all tested EUR-Lex/data.europa.eu/HTML variants. European e-Justice fallback pages returned `HTTP 403`. Therefore R018 does **not** admit article-level propositions from these three instruments in this bounded unit. Their legal-domain identities are recorded, while exact forum, special-jurisdiction, choice-of-law and recognition/enforcement rules remain primary-body verification dependencies.

```text
OFFICIAL_INSTRUMENT_IDENTITY != ARTICLE_TEXT_VERIFIED
RUNNER_ACCESS_FAILURE != SOURCE_ABSENCE
```

## United States federal forum/procedure baseline

The current official Federal Rules of Civil Procedure pamphlet dated 1 December 2025 was freshly downloaded from U.S. Courts and exactly matched the R014 hash `bd8705fc038d87e4fe222a7ea2e4324222c9430e2373fce56826bd2dfa2f8baf`. Rule 4 markers for territorial limits of effective service and service in a foreign country were verified.

For bounded use, Rule 4 supplies a service/personal-jurisdiction procedural interface in federal civil litigation. It does not by itself resolve constitutional due-process limits, state long-arm law, claim-specific federal statutory service, sovereign immunity or merits.

28 U.S.C. §1391 was live marker-verified from the Office of Law Revision Counsel current/preliminary U.S. Code page. It supplies federal venue architecture. Venue is not personal jurisdiction and does not establish applicable law or liability.

28 U.S.C. §1782 was live marker-verified as a statutory assistance mechanism concerning evidence for qualifying foreign/international proceedings. R018 does not determine the full case-law-defined scope of “foreign or international tribunal,” discretionary factors, privilege, discoverability, or entitlement in any concrete proceeding.

## Recognition/enforcement boundary

The bounded U.S. source set does not establish a single federal rule for recognition of foreign-country civil judgments. State law, treaty interfaces and case law remain separate dependencies. R018 therefore records `US_FOREIGN_COUNTRY_JUDGMENT_RECOGNITION = OPEN_STATE_SPECIFIC_RESEARCH` rather than a negative rule.

The EU internal recognition/enforcement architecture is associated with Brussels I bis, but article-level conclusions are withheld in this unit because the official primary body was blocked to the runner.

## Cross-border AI analysis order

For any concrete AI harm, analyze in this order without skipping layers:

1. identify actors and locations;
2. identify regulatory territorial-scope rules;
3. identify a legally competent forum and service basis;
4. distinguish venue from jurisdiction;
5. identify the applicable-law/conflict rule for each cause of action;
6. analyze duty, breach, causation, damage, defence and remedy under the selected law;
7. determine evidence-access/cooperation mechanisms;
8. determine recognition/enforcement rules for the resulting judgment or order.

## Open dependencies

- exact Brussels I bis primary text and current article-level verification;
- exact Rome I and Rome II primary text and current article-level verification;
- EU/Member-State case law on jurisdiction, applicable law and enforcement;
- U.S. constitutional personal-jurisdiction case law and state long-arm statutes;
- U.S. state foreign-country-judgment recognition statutes/common law;
- arbitration/choice-of-court/treaty interfaces;
- HCCH service/evidence/choice-of-court/judgments treaty participation and applicability;
- public-law enforcement cooperation and regulator-to-regulator mechanisms;
- concrete cross-border incident facts.

## Stop

```text
GLOBAL_FORUM_RULE = NOT_INFERRED
GLOBAL_APPLICABLE_LAW_RULE = NOT_INFERRED
GLOBAL_JUDGMENT_ENFORCEMENT_RULE = NOT_INFERRED
LEGAL_CONCLUSION = NOT_ATTEMPTED
UNKNOWN_PRESERVED = YES
AUTO_ADVANCE = NO
STOP = YES
```
