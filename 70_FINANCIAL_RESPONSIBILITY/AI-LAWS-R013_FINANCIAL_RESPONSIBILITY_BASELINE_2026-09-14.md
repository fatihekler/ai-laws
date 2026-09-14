# AI-LAWS-R013 — Financial Responsibility Baseline

**UNIT_ID:** `AI-LAWS-R013`
**RESEARCH_DATE:** 2026-09-14
**STATE:** `COMPLETE_RESEARCH_BASELINE_L1_L2_FINANCIAL_RESPONSIBILITY_CURRENT_LAW_MARKET_PROPOSAL_LIMITS_OPEN`
**ROLE:** `COMPARATIVE_LAW_RESEARCHER`
**LEGAL_ADVICE:** NO
**MODEL_OUTPUT_CANONICAL:** NO
**NOTEBOOK_OUTPUT_CANONICAL:** NO
**AUTO_ADVANCE:** NO

## 1. Bounded scope

R013 separates three categories that must not be collapsed:

```text
CURRENT_BINDING_LAW_OR_DIRECTIVE_ARCHITECTURE
!=
CURRENT_COMMERCIAL_MARKET_OFFERING
!=
LEGISLATIVE_OR_POLICY_PROPOSAL
```

The bounded unit uses the controlled EU source snapshots already verified in the repository, a fresh official European Parliament procedure record, and fresh live commercial-source identity probes. It does not attempt an exhaustive global insurance-market survey, national insurance-law analysis, actuarial pricing study, or catastrophe-capacity model.

Türkiye R005/R006 blockers are not reopened. R019 is not started. No Notebook ingestion is performed.

## 2. Current-law financial-responsibility signals

### 2.1 EU AI Act — notified-body liability insurance

The controlled current AI Act text contains a specific financial-responsibility requirement for notified bodies: they must take out appropriate liability insurance for conformity-assessment activities unless liability is assumed by the Member State in accordance with national law or that Member State is itself directly responsible for the conformity assessment.

This is a narrow institutional requirement. R013 does not transform it into a general insurance mandate for AI providers, GPAI providers, deployers, model developers, tool providers, agent operators or users.

```text
NOTIFIED_BODY_INSURANCE_DUTY = VERIFIED_CURRENT_CONTROLLED_TEXT
NOTIFIED_BODY_INSURANCE_DUTY != GENERAL_AI_PROVIDER_INSURANCE_DUTY
NOTIFIED_BODY_INSURANCE_DUTY != GENERAL_AI_DEPLOYER_INSURANCE_DUTY
```

### 2.2 Product Liability Directive — compensation schemes and insurance availability

Directive (EU) 2024/2853 supplies three relevant financial-responsibility signals.

First, its recitals preserve compensation schemes outside the Directive's liability regime, including insurance schemes. Second, Article 8(5) permits Member States, where victims cannot obtain compensation because none of the specified persons can be held liable under the Directive or because liable persons are insolvent or have ceased to exist, to use existing national sectoral compensation schemes or establish new ones under national law, preferably not funded by public revenue. Third, Article 20 requires the Commission's future evaluation to include information about the availability of product-liability insurance.

These provisions do not themselves create a single EU-wide AI catastrophe fund or establish that any particular Member State currently operates an AI-specific compensation scheme.

The Directive's transposition deadline remains 9 December 2026. R013 does not infer national implementation before source-specific Member-State research.

```text
PLD_ARTICLE_8_5_COMPENSATION_SCHEME_OPTION = VERIFIED_PRIMARY_TEXT
PLD_ARTICLE_20_INSURANCE_EVALUATION_SIGNAL = VERIFIED_PRIMARY_TEXT
PLD_TRANSPOSITION_DEADLINE = 2026-12-09
PLD_MEMBER_STATE_COMPENSATION_SCHEME_MAP = NOT_ATTEMPTED
EU_WIDE_AI_CATASTROPHE_FUND_CREATED_BY_PLD = NO
```

### 2.3 GDPR bounded result

A targeted search of the controlled GDPR snapshot returned insurance references associated with health-insurance/data-processing contexts, not an AI financial-assurance duty. R013 therefore records only a bounded source-set result:

```text
GDPR_AI_FINANCIAL_ASSURANCE_DUTY = NOT_ESTABLISHED_BY_TARGETED_R013_SEARCH
```

This is not a universal negative finding about insurance, indemnification, contractual risk transfer or sector regulation under Member-State law.

## 3. Current commercial market layer

Fresh GitHub-runner probes on 2026-09-14 confirmed live Armilla pages:

- `https://www.armilla.ai/` — HTTP 200; page title identified the site as `Armilla: AI Insurance`;
- `https://www.armilla.ai/ai-insurance` — HTTP 200; page title identified `AI Insurance – Lloyd’s Coverholder | Armilla AI`;
- `https://www.armilla.ai/become-an-armilla-broker-ai-insurance-warranty` — HTTP 200; page title identified an AI insurance/warranty broker page.

This establishes a current commercial-source identity and disproves any claim that R013 can assume AI-related insurance products do not exist. The `Lloyd’s Coverholder` description is the commercial source's own page title and was not independently verified against a Lloyd's register in this bounded unit.

R013 did not acquire policy wording, declarations, endorsements, exclusions, limits, deductibles, underwriting rules, territorial scope, licensing records, solvency information or claims-payment evidence. No coverage conclusion is therefore admitted.

Two guessed Munich Re candidate paths returned HTTP 404. That result is treated only as unresolved routing for those candidate URLs.

```text
ARMILLA_CURRENT_AI_INSURANCE_MARKET_IDENTITY = VERIFIED_COMMERCIAL_SOURCE_HTTP_200
ARMILLA_POLICY_WORDING = UNKNOWN_NOT_ACQUIRED
ARMILLA_LIMITS_EXCLUSIONS_UNDERWRITING = UNKNOWN_NOT_ACQUIRED
MUNICH_RE_CANDIDATE_URLS = HTTP_404
HTTP_404_CANDIDATE_URL != NO_MARKET_PRODUCT
COMMERCIAL_PRODUCT_EXISTS != LEGAL_MANDATE
COMMERCIAL_PAGE_TITLE != POLICY_COVERAGE_PROVEN
```

## 4. Proposal and withdrawn-procedure layer

The European Parliament Legislative Observatory current procedure record for `2022/0303(COD)`, the proposed AI Liability Directive, was fetched successfully on 2026-09-14. It records:

```text
TITLE = Adapting non-contractual civil liability rules to artificial intelligence (AI Liability Directive)
PROCEDURE = 2022/0303(COD)
STATUS = Procedure lapsed or withdrawn
WITHDRAWAL_EVENT = 2025-10-06 — Proposal withdrawn by Commission
```

Accordingly, the AI Liability Directive proposal is not represented in AI-LAWS as current law or as an active legislative proposal on the R013 research date.

The 2020 European Parliament resolution often cited in AI liability/insurance policy discussions was probed through Parliament HTML, PDF and XML variants and EUR-Lex. The tested endpoints returned `HTTP 202` with empty bodies in the GitHub-runner environment. R013 therefore does not admit an exact substantive mandatory-insurance proposition from that primary text. R001 supporting research remains proposal-space only and cannot substitute for inaccessible primary text.

Catastrophe bonds, mutual pools, developer reserves, mandatory sector-wide AI insurance, public-private reinsurance and AI catastrophe funds remain research/proposal classes unless an applicable binding instrument is separately verified.

```text
AILD_2022_0303_COD = LAPSED_OR_WITHDRAWN
AILD_COMMISSION_WITHDRAWAL_DATE = 2025-10-06
AILD_CURRENT_LAW = NO
AILD_ACTIVE_PROPOSAL_R013_DATE = NO
EP_2020_RESOLUTION_PRIMARY_BODY = ACCESS_BLOCKED_HTTP_202_EMPTY_BODY
EP_2020_EXACT_MANDATORY_INSURANCE_TEXT = NOT_ADMITTED_R013
GLOBAL_FRONTIER_AI_CATASTROPHE_FUND_RULE = NOT_ESTABLISHED_BY_R013
GENERAL_AI_PROVIDER_DEPLOYER_MANDATORY_INSURANCE_RULE = NOT_ESTABLISHED_BY_R013
```

## 5. Financial-responsibility classification

| Layer | R013 status | What can be said | What cannot be said |
|---|---|---|---|
| AI Act notified-body insurance | current binding controlled text | a scoped notified-body liability-insurance requirement exists, subject to Member-State-liability substitute | all AI actors must buy liability insurance |
| PLD compensation schemes | binding EU Directive; national implementation open | Article 8(5) permits specified national compensation schemes; Article 20 tracks product-liability-insurance availability | an EU-wide AI fund already exists; Member States have identical schemes |
| GDPR | current binding controlled text | targeted R013 search did not establish an AI financial-assurance duty | GDPR contains no relevant financial responsibility in every context |
| Armilla | current commercial source | a live AI-insurance commercial offering identity is observable | policy wording, coverage, enforceability, licensing or claims performance is established |
| AI Liability Directive | withdrawn procedure | the 2022 proposal was withdrawn on 2025-10-06 | it is current law or an active proposal in September 2026 |
| catastrophe fund/bond/reserve concepts | proposal/research layer | design options may be researched | any proposal is an existing legal right or duty |

## 6. Open questions preserved

R013 intentionally leaves open:

- exhaustive current AI insurance products and insurers;
- actual policy language, limits, exclusions, sublimits, waiting periods, warranties and claims triggers;
- whether particular conventional cyber, technology E&O, professional indemnity, product liability, D&O or general-liability forms respond to a defined AI loss;
- EU Member-State PLD transposition and compensation-scheme implementation;
- jurisdiction-specific mandatory insurance, bonding, reserve, capital or guarantee duties beyond the bounded sources;
- insurance-market capacity for correlated or catastrophic frontier-AI loss;
- catastrophe-bond, mutual-pool, government-backstop or victim-fund feasibility and legal design;
- insolvency priority, parent/subsidiary responsibility and judgment-proof risk;
- exact primary text of the inaccessible 2020 Parliament resolution;
- independent verification of commercial-source regulatory/market claims.

## 7. Controlling firewalls

```text
INSURANCE_AVAILABLE != LIABILITY_EXISTS
INSURANCE_UNAVAILABLE != NO_LIABILITY
COVERAGE != INDEMNITY_CERTAINTY
POLICY_LIMIT != MAXIMUM_HARM
COMMERCIAL_MARKET_OFFERING != LEGAL_REQUIREMENT
PROPOSAL != CURRENT_LAW
WITHDRAWN_PROPOSAL != ACTIVE_PROPOSAL
COMPENSATION_SCHEME_OPTION != EXISTING_AI_FUND
SOURCE_ACCESS_FAILURE != SOURCE_ABSENCE
TARGETED_SEARCH_NO_HIT != UNIVERSAL_NEGATIVE_FINDING
```

## 8. Bounded close

R013 completes only a current-law / market / proposal classification baseline. It does not establish a global AI financial-responsibility rule, universal mandatory insurance, actuarial pricing, insurer capacity, or a current frontier-AI catastrophe fund.

```text
LEGAL_CONCLUSION = NOT_ATTEMPTED
NOTEBOOK_UPLOADS = 0
DERIVED_MARKDOWN_CREATED = 0
NEW_SOURCE_BINARIES = 0
ZIP_OR_ARTIFACT_CREATED = NO
UNKNOWN_PRESERVED = YES
AUTO_ADVANCE = NO
STOP = YES
```
