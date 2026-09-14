# AI-LAWS-R015 — Corporate Governance Baseline

**UNIT_ID:** `AI-LAWS-R015`  
**DATE:** 2026-09-14  
**SCOPE:** bounded EU + U.S./Delaware corporate-governance and issuer-disclosure baseline for frontier/high-risk AI  
**LEGAL_ADVICE:** NO  
**AUTO_ADVANCE:** NO

## 1. Research question

What currently verified legal or official-source rules bear on organizational AI governance, board/officer oversight, risk disclosure and internal controls, without collapsing entity obligations into personal fiduciary liability?

## 2. Integrity rule

```text
ENTITY_OR_PROVIDER_DUTY
!= BOARD_OVERSIGHT_DUTY
!= OFFICER_OVERSIGHT_DUTY
!= SECURITIES_DISCLOSURE_DUTY
!= PERSONAL_LIABILITY
```

A regulatory obligation imposed on an AI provider does not by itself establish that a director or officer personally breached a fiduciary duty. A risk-management framework does not itself create law. A pleaded oversight claim that survives dismissal does not establish final liability.

## 3. EU AI Act organizational-governance layer

The controlled current AI Act snapshot is the existing repository binary `86_NOTEBOOKLM/downloads/Current consolidated AI Act.pdf`, previously verified by R030 as an exact official EUR-Lex PDF snapshot. R015 reverified its Article 17 and Article 55 markers.

- Article 16 requires providers of high-risk AI systems, among other things, to have the Article 17 quality-management system in place and to maintain required documentation/logging and conformity processes.
- Article 17 requires providers of high-risk AI systems to establish a documented quality-management system designed to ensure compliance, including written policies, procedures and instructions across regulatory compliance, design/development controls, testing/validation, data management, risk management, post-market monitoring, incident handling and accountability-related processes.
- Article 55 imposes additional obligations on providers of general-purpose AI models with systemic risk, including model evaluation/adversarial testing, assessment and mitigation of Union-level systemic risks, serious-incident tracking/documentation/reporting and adequate cybersecurity protection.

**Boundary:** these provisions establish obligations of regulated provider actors/entities. This bounded unit does not identify a general Article 17 or Article 55 rule making every corporate director/officer personally liable, nor a universal requirement that a board create a dedicated AI committee.

## 4. Delaware board-management and oversight layer

The current official Delaware Code source for Title 8 §§ 141–142 was live-verified. Section 141 supplies the corporate-law baseline that the corporation's business and affairs are managed by or under the direction of the board, subject to statutory/certificate exceptions; § 142 addresses corporate officers. The full current Title 8 PDF was also transiently verified but intentionally not vendored because the current official code URL is the preferred dynamic source.

### Marchand v. Barnhill

Official Delaware Supreme Court full text was separately verified. The corrected opinion is dated June 19, 2019; the judgment reversed and remanded the Court of Chancery dismissal. The court explains that directors must make a good-faith effort to implement a reasonable board-level monitoring/reporting system and then monitor it, while retaining substantial discretion to design context- and industry-specific approaches.

The Blue Bell facts involved food safety as a central operational/compliance issue for a single-product food company. R015 therefore records **mission-critical relevance as fact-specific**, not a rule that AI is automatically mission-critical for every corporation. The case is admitted only as `ANALOGICAL_PRECEDENT` for AI governance.

### In re McDonald's — officer oversight opinion

The Delaware Court of Chancery opinion dated January 26, 2023 clarifies that corporate officers owe a duty of oversight. The opinion describes the application as context-driven: a CEO may have a company-wide remit, while other officers generally have oversight/reporting duties within their areas of responsibility. Establishing a breach requires bad-faith/disloyal conduct, not merely a poor outcome.

The court denied Fairhurst's Rule 12(b)(6) motion as to pleaded claims. **That procedural result is not a final adjudication of personal liability.** R015 admits the decision only as `ANALOGICAL_PRECEDENT`.

### In re McDonald's — director dismissal opinion

The companion Court of Chancery opinion dated March 1, 2023 provides an important counterweight. It explains that a red-flags oversight theory requires facts supporting an inference that directors knew of a problem and consciously ignored it; weak, inadequate or even grossly negligent response is not enough to plead the required bad faith. On the pleaded facts, the directors' response prevented a reasonable bad-faith inference, and their motion to dismiss was granted.

**R015 inference rule:** the existence of an AI risk, incident, model failure or regulator concern does not itself prove a Caremark-style breach. Governance-system design, information flow, actual red flags, response, officer remit, state of mind, procedural posture and company-specific centrality all matter.

## 5. U.S. securities-disclosure layer

### Regulation S-K Item 105

The current official eCFR URL for 17 CFR § 229.105 is retained as the controlling current-source pointer. Official current text was independently verified for the material-risk-factor requirement. The GitHub-hosted runner's HTTP-200 body was **not** accepted as section identity and the acquisition ledger was corrected accordingly.

R015 does not infer that every AI risk is material or separately disclosable. Materiality, issuer facts, existing disclosures and the applicable filing context remain necessary.

### Regulation S-K Item 407(h)

The SEC's official 2009 adopting release for Proxy Disclosure Enhancements was independently verified. It adopted disclosure concerning board leadership structure and the board's role in risk oversight. The current eCFR § 229.407 URL is retained, but the GitHub-runner body was not admitted as verified current section text.

This is a disclosure rule about board risk-oversight architecture; it is not by itself a substantive rule requiring a particular AI governance committee or prescribing the merits of a board's AI-risk response.

### SEC AI-washing statements

The official SEC page could not be acquired from the GitHub runner (`HTTP 403`). Public SEC statements warning against unsupported or materially misleading AI claims are treated only as `OFFICIAL_GUIDANCE / ENFORCEMENT_SIGNAL`, not as a new AI-specific regulation or standalone private-liability rule.

## 6. NIST AI RMF layer

The existing repository `NIST AI RMF 1.0.pdf` was reverified; the official NIST publication page returned HTTP 200. NIST states that AI RMF 1.0 is voluntary and that a revised version is in progress. Its GOVERN function is useful as an operational governance/control vocabulary, but it does not itself create Delaware fiduciary duties, SEC disclosure duties or EU AI Act obligations.

## 7. Governance-duty crosswalk

| Layer | Actor | Verified proposition | What is not inferred |
|---|---|---|---|
| EU AI Act Art. 17 | high-risk AI provider | documented quality-management system | automatic director/officer personal liability |
| EU AI Act Art. 55 | systemic-risk GPAI provider | evaluation, systemic-risk mitigation, serious-incident reporting, cybersecurity | universal board committee mandate |
| DGCL §141 | Delaware corporation/board | business and affairs managed by or under board direction | AI-specific duty by statutory text alone |
| Marchand | Delaware directors | good-faith effort to establish and monitor reasonable board-level system | AI always mission-critical; strict liability |
| McDonald's officer opinion | Delaware corporate officers | context/remit-specific oversight; bad faith required | every officer responsible for every AI risk; final liability from pleading survival |
| McDonald's director opinion | Delaware directors | conscious disregard/bad-faith threshold; responsive conduct matters | negligent/inadequate response automatically equals breach |
| Reg. S-K Item 105 | SEC registrant | material risk-factor disclosure framework | every AI risk is material |
| Reg. S-K Item 407(h) | SEC registrant | board leadership/risk-oversight disclosure | mandated AI committee or governance design |
| NIST AI RMF 1.0 | voluntary users | governance/risk-management framework | binding fiduciary or regulatory duty |

## 8. Preserved UNKNOWNs / next research dependencies

- No exhaustive 50-state U.S. corporate-governance map was attempted.
- No EU Member-State company-law/director-duty implementation map was attempted.
- No sector-specific board duty map for banks, insurers, healthcare, critical infrastructure or public bodies was attempted.
- No concrete company, director or officer liability conclusion was attempted.
- No general rule that AI is a corporation's `mission-critical` risk was inferred.
- No general legal requirement for a dedicated board AI committee was established.
- Current exact eCFR body identity for §§ 229.303 and 229.407 remains unresolved in the GitHub-runner lane; official URLs and fixed SEC adoption materials are retained with that limitation.
- Delaware official opinion URLs returned short HTML bodies to GitHub-hosted runners. Official full text was independently verified, but repository PDF snapshots were not fabricated or falsely pinned.
- Later appellate treatment, case-specific subsequent history and post-2023 doctrinal developments are not exhaustively mapped by this bounded unit.
- Whether any AI-related fact is material for securities-law disclosure remains issuer- and fact-specific.

## 9. Research state

```text
EU_AI_ACT_ORGANIZATIONAL_DUTIES = VERIFIED_BOUNDED
DELAWARE_BOARD_STATUTORY_BASELINE = VERIFIED_CURRENT_OFFICIAL_SOURCE
DELAWARE_ANALOGICAL_CASES_FULL_TEXT = VERIFIED_OFFICIAL_SOURCE
DELAWARE_CASE_PDF_REPOSITORY_SNAPSHOTS = NOT_PINNED_GITHUB_RUNNER_BODY_NOT_PDF
SEC_ITEM_105_CURRENT_SOURCE = VERIFIED_BOUNDED
SEC_ITEM_407H_ADOPTION = VERIFIED_OFFICIAL_SEC_FINAL_RULE
NIST_AI_RMF_BINDING_LAW = NO
PERSONAL_LIABILITY_FINDING = NOT_ATTEMPTED
GLOBAL_AI_BOARD_DUTY = NOT_INFERRED
AUTO_ADVANCE = NO
```
