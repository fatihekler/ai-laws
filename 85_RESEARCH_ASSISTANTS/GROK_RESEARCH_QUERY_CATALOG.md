# AI-LAWS — Grok Adversarial Research Query Catalog

**DOCUMENT_ID:** AI-LAWS-R021-GROK-QUERY-CATALOG-1.0  
**STATE:** ACTIVE_RESEARCH_QUERY_LIBRARY  
**DATE:** 2026-09-13

This catalog is for bounded Grok research tasks. Select one task family at a time. Grok output remains supporting research.

## 1. Current-law verification

Prompt pattern:

> For `[JURISDICTION]`, identify the current primary legal instruments governing `[TOPIC]` as of `[DATE]`. Use official legal sources first. For each source give exact document number, effective/application dates, amendment/consolidation state, actor scope, and what the source does **not** establish. Find any later amendment/corrigendum that makes an older summary stale.

Topics:

- AI provider/deployer duties;
- high-risk/impact AI;
- GPAI/frontier systems;
- automated decision-making;
- transparency/disclosure;
- human oversight;
- incident reporting;
- cybersecurity;
- product liability;
- data/biometric/neurodata;
- consumer protection;
- public-sector AI;
- procurement.

## 2. Source contradiction search

> Take claim `[CLAIM_ID]`. Find the strongest primary/official source supporting it and the strongest credible source limiting or contradicting it. If the sources address different scopes, explain the scope mismatch instead of declaring a contradiction.

Required output:

```text
SUPPORTING_SOURCE
LIMITING_SOURCE
SCOPE_DIFFERENCE
DATE_DIFFERENCE
JURISDICTION_DIFFERENCE
UNRESOLVED
```

## 3. Amendment/currentness challenge

> Search for amendments, corrigenda, consolidation changes, implementation delays, repeal/supersession, new guidance or court/regulator interpretation affecting `[DOCUMENT_ID]` after `[LAST_VERIFIED_DATE]`.

This task should be run before major legal conclusions from fast-moving AI law.

## 4. Frontier AI incident challenge

> For incident `[INCIDENT_ID]`, separate provider-admitted facts, independently corroborated facts, disputed facts, allegations, forecasts and legal inferences. Identify environment, authorized task, granted authorities, unauthorized actions, failed controls, documented third-party harm, and evidence that remains unavailable.

Do not answer liability.

## 5. Company public alignment / antitrust watch

> For public statements by `[ACTORS]` on AI safety/pacing/standards, build a dated public-evidence timeline. Identify any actual written agreement, common standard, governance body or contractual commitment. Separate public alignment from evidence of coordinated conduct. Identify what additional facts would be required for competition-law analysis.

Required invariant:

```text
PUBLIC_ALIGNMENT != SECRET_COLLUSION
```

## 6. Human sovereignty / mental autonomy

> Across `[JURISDICTIONS]`, identify binding and nonbinding sources concerning dignity, mental integrity, cognitive liberty, mental privacy, neurodata, biometric/emotion inference, manipulation, automated decision appeal, opt-out and reversibility. Do not universalize scholarly labels. Separate direct neural measurement from inference using ordinary behavioral data.

## 7. Agent/harness legal role

> Research how current law might classify an AI harness/tool provider that gives models file, network, process, secret and external-tool authority. Compare possible roles under product, software, cybersecurity, procurement, data and negligence frameworks. Mark every classification that lacks authoritative precedent as UNKNOWN or analogy only.

## 8. Multi-agent causation

> Identify legal doctrines relevant when harm results from model developer + deployer + harness + tool + third-party software + human approval. Research causation, contribution, joint liability, intervening acts, organizational negligence and evidence-preservation issues. Do not infer a global rule.

## 9. Evidence/logging obligations

> For `[JURISDICTION]`, find current binding rules and cases addressing logging, technical documentation, records preservation, disclosure/discovery, burden of proof and missing evidence in AI/software/data/cyber incidents. Identify exact actor, retention, access and sanction/remedy where supported.

## 10. Product liability

> Map whether software/AI is treated as a product/component/service for product-liability purposes in `[JURISDICTION]`. Separate current binding law from proposed reform. Identify damage categories, defect tests, disclosure/evidence mechanisms, presumptions and transposition/application dates.

## 11. “We did not know” / foreseeability

> Build a dated public-risk timeline for `[RISK_CLASS]`, but separately identify evidence of actor-specific knowledge, foreseeable misuse, prior incidents, internal acknowledgement if public, regulator notice and current duty. Do not convert public knowledge into automatic legal notice.

## 12. National-security/state carve-outs

> For `[JURISDICTION]`, identify exact exemptions/carve-outs for military, defence, intelligence and national security in AI/data/cyber law. Then identify what constitutional, human-rights, procurement, oversight, audit or administrative-law mechanisms may still apply. Do not infer classified operational facts.

Required invariant:

```text
EXEMPT_FROM_ONE_AI_INSTRUMENT != EXEMPT_FROM_ALL_LAW
```

## 13. Financial responsibility

> Identify existing mandatory insurance, financial assurance, reserves, compensation funds or guarantee schemes that could apply to AI-related harms in `[JURISDICTION]`. Then separately identify academic/policy proposals for AI catastrophe insurance, CAT bonds, industry pools or developer reserves. Distinguish actual market products from catastrophic-tail coverage.

## 14. Judgment-proofness

> Research whether AI/frontier developers could externalize catastrophic losses because liabilities exceed firm assets/insurance. Find legal/economic literature, existing analogous regimes and counterarguments. Label this as scholarship/policy analysis unless binding law exists.

## 15. Cross-border harm

> For a scenario where developer, cloud, deployer, affected person and harmful action are in different jurisdictions, identify the conflict-of-laws questions that must be answered. Do not choose a governing law without facts. List connecting factors, forum issues, enforcement and data-transfer complications.

## 16. State-by-state / province-by-province inventory

> For `[COUNTRY_WITH_SUBNATIONAL_LAW]`, enumerate enacted AI-specific laws/rules at the subnational level as of `[DATE]`. Exclude bills that are not enacted. Record effective dates, amendments, enforcement body, private right of action if any, preemption/conflict questions and official source URL.

## 17. Court-case discovery

> Find official case law directly involving AI/automated decision systems or analogical software/data/cyber issues for `[JURISDICTION/TOPIC]`. Do not summarize a case unless full official text or accepted authoritative text is available. Record docket, date, court, holding, legal basis, direct/analogical classification and analogy limit.

## 18. Regulator enforcement

> Identify regulator enforcement decisions involving AI, algorithmic discrimination, biometric inference, dark patterns, automated profiling, data misuse or deceptive AI claims. Separate enforcement settlement/decision from guidance and press release.

## 19. Children / vulnerable persons

> Map binding duties and regulator guidance for AI affecting children, older persons, disabled persons, patients or other vulnerable groups. Identify consent, profiling, manipulation, safety and human-review rules.

## 20. Employment / labour

> Map current rules for AI in recruitment, worker monitoring, performance scoring and termination. Identify transparency, discrimination, works council/collective, privacy and appeal obligations.

## 21. Health / medical AI

> Map medical-device, clinical-decision, data, liability and professional-duty rules for AI-supported healthcare. Separate device approval from malpractice/professional responsibility.

## 22. Election/information integrity

> Map current law governing synthetic media, political advertising, automated influence, platform duties and foreign interference. Separate political speech protections from deceptive/manipulative conduct rules.

## 23. Competition and standards-as-moat

> Research whether mandatory/voluntary AI safety standards can create entry barriers, exclusion, interoperability problems or information-sharing antitrust risks. Identify existing competition-law principles and actual enforcement/guidance rather than assuming abuse.

## 24. Auditor independence

> Research legal/professional rules governing independence of AI auditors/conformity assessors/evaluators. What conflicts arise if the developer selects/pays the evaluator? Which regimes require accreditation, independence, access or reporting rights?

## 25. Model distillation / extraction

> Map possible legal categories for model extraction/distillation: contract, trade secret, cybersecurity/unauthorized access, copyright/database, export controls and competition. Separate vendor attribution from adjudicated facts. Identify what evidence is required to prove protected information or unauthorized acquisition.

## 26. Neurotechnology and inferred mental state

> Compare direct neural-data rules with rules for mental/emotional inference from voice, face, text, behavior or biometrics. Identify where law explicitly covers inference and where analogy is speculative.

## 27. AI dependency/manipulation

> Search binding consumer, platform, child-safety, mental-health, advertising and unfair-practices law that could apply to AI systems encouraging dependency, exclusivity, compulsive use or manipulative persuasion. Separate ethical concern from legally defined violation.

## 28. Remedies

> For `[RIGHT/DUTY]`, identify available remedies: injunction, deletion, correction, human review, administrative fine, compensation, contract remedy, product-liability damages, criminal sanction, judicial review or collective action. Do not infer remedy where statute/case does not provide it.

## 29. Cross-repo requirement extraction

> Given verified legal source `[SOURCE_ID]`, extract only destination-neutral requirement candidates. Each candidate must include duty bearer, trigger, prohibited/required conduct, evidence needed, legal limitation and destination repo. Do not translate a policy recommendation into a legal requirement.

## 30. Required Grok footer

Every bounded task should end:

```text
PRIMARY_SOURCES_FOUND = <N>
OFFICIAL_SOURCES_FOUND = <N>
CONTRARY_OR_LIMITING_SOURCES_FOUND = <N>
MATERIAL_UNKNOWNS = <N>
LEGAL_AUTHORITY_ASSUMED = FALSE
MODEL_OUTPUT_CANONICAL = FALSE
REPOSITORY_STATE_CHANGED = FALSE
AUTO_ADVANCE = NO
```
