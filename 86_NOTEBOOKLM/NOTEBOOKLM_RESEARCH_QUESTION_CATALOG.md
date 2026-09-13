# AI-LAWS — NotebookLM / Gemini Notebook Research Question Catalog

**DOCUMENT_ID:** AI-LAWS-R021-NB-QUESTION-CATALOG-1.0  
**STATE:** ACTIVE_RESEARCH_QUESTION_LIBRARY  
**DATE:** 2026-09-13

Use these questions with the exact relevant source subset selected. Do not ask a global notebook to answer a jurisdiction-specific legal question when the applicable sources are not loaded.

## 1. Authority and currentness

1. Which sources in this pack are binding law, treaty obligations, court decisions, regulatory decisions, guidance, soft law, technical frameworks, scholarship, company statements or reporting?
2. For each binding source, what is the exact adoption/publication/entry-into-force/application date?
3. Which source has been amended, corrected, superseded or consolidated?
4. Which provisions are not yet applicable even though the instrument is in force?
5. Which source is only a policy proposal or implementation plan?
6. Which legal conclusions would require checking a national transposition measure or local case law?
7. Which sources contain internal disclaimers that the consolidated text is not itself the authentic legal text?
8. Which claims in our current synthesis are stale as of the pack date?

Output columns:

```text
SOURCE_ID | AUTHORITY_CLASS | BINDING_STATE | CURRENT_VERSION_DATE | APPLICATION_DATE | LIMITATION | NEXT_VERIFICATION
```

## 2. Actor and role allocation

For the selected jurisdiction, identify how the sources distinguish:

- model developer;
- provider;
- deployer;
- importer/distributor;
- user/operator;
- employer;
- public authority;
- tool/harness provider;
- data controller/processor;
- product manufacturer/component supplier;
- auditor/conformity assessor;
- affected person.

Questions:

1. Which actor receives which duty?
2. Can an actor become subject to a different role because of modification/rebranding/integration?
3. Which duties are nondelegable?
4. Which duties depend on system class or use context?
5. Where is actor classification uncertain for agentic AI/harness systems?

## 3. Human sovereignty and rights

Using only selected rights/legal sources:

1. What legally recognized protections relate to dignity, privacy, mental integrity, autonomy, data protection, non-discrimination and due process?
2. Which source expressly covers neurodata, biometric data or inferred characteristics?
3. Which rights require a decision by a human, explanation, appeal or contestability?
4. Which rights are only scholarly proposals such as a generalized "cognitive liberty" right?
5. What is the legal difference between direct neural measurement and inference about mental/emotional state from ordinary behavioral data?
6. Which legal protections apply to children or vulnerable persons?
7. What opt-out, consent, objection or deletion mechanisms exist?
8. Which rights cannot safely be generalized across jurisdictions?

Required output:

```text
RIGHT_OR_INTEREST | SOURCE_ID | LEGAL_STATUS | SUBJECT | DUTY_BEARER | REMEDY_OR_PROCESS | SCOPE_LIMIT | UNKNOWN
```

## 4. Automated and agentic decision systems

1. Which sources address automated decision-making directly?
2. Which duties apply when an AI recommendation is nominally advisory but is followed routinely by humans?
3. What changes when AI has tool/network/file/process authority?
4. Are irreversible automated actions treated differently?
5. Which obligations relate to human oversight and intervention?
6. What logging/traceability is required or recommended?
7. Do any sources address delegation to sub-agents or chained services?
8. Where does existing law become ambiguous for autonomous continuation after the original user command?

## 5. Liability structure

For each jurisdiction/source set, separate:

```text
DUTY
BREACH
CAUSATION
DAMAGE
REMEDY
DEFENCE
```

Questions:

1. What legal duty might apply to a developer/provider/deployer/operator?
2. Is the regime fault-based, strict, regulatory, contractual, product-liability based or mixed?
3. What factual evidence would be needed to prove breach?
4. What causation problems arise when multiple models/tools/people contribute?
5. What kinds of damage are legally recognized?
6. Are pure economic, dignitary, privacy, psychological or probabilistic harms recoverable?
7. How are third-party attacks or misuse treated?
8. Does compliance with a technical standard create a defence, presumption, or merely evidence of care?
9. Does failure to preserve logs affect proof?
10. What remains unknown without case law?

## 6. Evidence, logging and procedure

1. Which sources require or incentivize logs, records, technical documentation or incident reports?
2. Who controls the evidence after an AI incident?
3. What preservation period applies?
4. What happens if records are missing?
5. Is there a disclosure/discovery mechanism available to affected persons?
6. Who bears the burden of proof?
7. Are evidentiary presumptions available in product liability or data cases?
8. What must an external auditor be allowed to see?
9. What evidence would be necessary to distinguish model defect, harness defect, configuration error and operator error?
10. Which evidence obligations continue after model/version replacement?

## 7. Incident analysis

When NB08 is selected:

1. What facts are admitted by the system/provider itself?
2. What facts are independently corroborated?
3. Which facts are disputed?
4. Which claims are only vendor attribution?
5. What was the exact environment: evaluation, training, staging or production?
6. What was the original authorized task?
7. What capability/authority was granted?
8. What unauthorized action occurred?
9. What containment/control failed?
10. What third-party harm is documented rather than hypothesized?
11. What legal elements remain unproven?
12. What evidence should be preserved for later liability analysis?

Never answer "who is liable" from incident sources alone.

## 8. National security / state systems

1. Which AI rules exclude or limit national-security/defence/intelligence activities?
2. What alternative oversight applies when the general AI regulation does not?
3. Is judicial review available?
4. Are procurement, constitutional, human-rights or data rules still applicable?
5. What transparency/reporting exemptions exist?
6. Which claims about classified systems cannot be verified from public sources?
7. Does the source create a complete exemption or only an exemption from one instrument?
8. How does sovereign immunity affect remedy?

Required invariant:

```text
EXEMPT_FROM_AI_ACT != EXEMPT_FROM_ALL_LAW
```

## 9. Competition / concentration / coordination

1. What evidence exists of public coordination among AI companies?
2. Does any source establish an agreement with legally relevant commitments?
3. Which facts would be needed for antitrust/cartel analysis?
4. Can safety standards create barriers to entry?
5. Can interoperability/data portability reduce lock-in?
6. What procurement rules discourage single-vendor dependency?
7. How should safety coordination be designed to avoid competitive abuse?
8. Which claims are merely market-structure hypotheses?

Required invariant:

```text
PUBLIC_ALIGNMENT != SECRET_COLLUSION
```

## 10. Financial responsibility / insurance

1. What existing insurance products or financial-assurance duties actually apply?
2. Is any AI-specific mandatory insurance currently binding in the selected jurisdiction?
3. What exclusions or coverage limits matter for cyber/AI/autonomous-agent losses?
4. Are catastrophe bonds, industry pools, developer reserves or victim funds existing mechanisms or only proposals?
5. What is the judgment-proofness problem?
6. Who pays first-dollar losses under proposed models?
7. What moral-hazard problems arise?
8. Which analogies from nuclear/environmental/financial regulation are legally transferable and which are not?

Output categories:

```text
CURRENT_BINDING_LAW
CURRENT_MARKET_PRACTICE
SCHOLARLY_PROPOSAL
POLICY_PROPOSAL
UNKNOWN
```

## 11. Cross-border conflict of laws

1. Where did development, deployment, decision, harm and data processing occur?
2. Which jurisdiction claims territorial/extraterritorial reach?
3. What connecting factors determine applicable law?
4. What forum/jurisdiction rules may apply?
5. Can a judgment/order be enforced cross-border?
6. Which data-transfer/localization rules matter?
7. Does the provider's location change legal exposure?
8. Which claims require local counsel?

## 12. Case-law research support

For verified court sources only:

1. What exactly did the court hold?
2. Which facts were decisive?
3. What legal provisions were applied?
4. What was not decided?
5. Is the case directly about AI or merely analogical?
6. What is the analogy target?
7. What is the analogy limit?
8. Is the decision final/binding/persuasive in the relevant system?
9. Has later authority limited or reversed it?
10. Which AI proposition would be unsafe to infer from the case?

## 13. Temporal / "we did not know" analysis

Build a timeline without converting public awareness into automatic legal notice.

For each risk:

```text
EARLY_PUBLIC_WARNING
DEVELOPER_ACKNOWLEDGEMENT
DOCUMENTED_INCIDENT
REGULATOR_ACKNOWLEDGEMENT
ACTOR_SPECIFIC_KNOWLEDGE_EVIDENCE
CURRENT_DUTY
```

Required invariant:

```text
PUBLIC_KNOWLEDGE_EXISTS != LEGAL_KNOWLEDGE_ELEMENT_SATISFIED
```

## 14. APES / multidimensional challenge interface

When Apesteori material is intentionally selected, ask separately:

- psychological effects;
- sociological effects;
- technological control surface;
- epistemological uncertainty;
- power concentration;
- emotional dependency/manipulation;
- moral/theological human-reminder questions;
- historical analogies and failure patterns.

Do not collapse these into a legal score.

Route only legally relevant claims into AI-LAWS legal analysis.

## 15. Cross-repo requirement candidate generation

Only after a legal duty is verified, ask:

1. What destination-neutral requirement candidate follows?
2. Who is the duty bearer?
3. What evidence would demonstrate compliance?
4. What technical control candidate may support it?
5. What does the legal source **not** require?
6. Which destination repo should review the candidate?

Output:

```text
LEGAL_SOURCE_ID
LEGAL_DUTY_ID
REQUIREMENT_CANDIDATE
DUTY_BEARER
EVIDENCE_REQUIRED
TECHNICAL_CONTROL_CANDIDATE
PRIMARY_DESTINATION
LIMITATIONS
DESTINATION_ACCEPTANCE = NOT_RUN
```

## 16. Mandatory Notebook answer footer

Ask Notebook to end material research answers with:

```text
SOURCE_SET_USED = [...]
DATE_CUTOFF = ...
BINDING_LAW_SEPARATED_FROM_GUIDANCE = YES/NO
CONFLICTS_PRESERVED = YES/NO
UNKNOWNS_PRESERVED = YES/NO
MODEL_OUTPUT_USED_AS_PRIMARY_AUTHORITY = NO
LEGAL_ADVICE = NO
CANONICAL_STATE_CHANGED = NO
```
