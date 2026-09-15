# AI-LAWS Single Source Analysis: EU-004 (Charter of Fundamental Rights)

**RUN_ID**: `RUN-20260915-011`  
**PACK_ID**: `NB02`  
**SOURCE_ID**: `EU-004`  
**TITLE**: Charter of Fundamental Rights of the European Union (2016/C 202/02)  
**PROMOTION_STATE**: `SUPPORTING_RESEARCH`  
**RECHECK_REQUIRED**: `TRUE`  

---

### S1 — IDENTITY / AUTHORITY
* **Document Identity**: Charter of Fundamental Rights of the European Union, consolidated text published in Official Journal 2016/C 202/02.
* **Authority Class**: Primary EU Constitutional Law. Under Article 6(1) TEU (as amended by the Treaty of Lisbon), the Charter has the same legal status as the EU Treaties.
* **Binding State**: Legally binding upon EU Institutions, bodies, offices, and agencies, and upon EU Member States when implementing Union law.
* **Publication vs Application Date**: Solemnly proclaimed on 18.12.2000; revised text 12.12.2007; became legally binding on 01.12.2009 (entry into force of Treaty of Lisbon). Consolidated version published 07.06.2016 (OJ C 202/02).

---

### S2 — SCOPE / ACTORS
* **Regulated Actors**: 
  * EU Institutions, Bodies, Offices, Agencies (bound directly in all actions) [Article 51(1)].
  * EU Member States (bound strictly when implementing Union law) [Article 51(1)].
* **Scope Limits & Private Actors**: Under Article 51(1), the Charter does not directly create general horizontal obligations for private AI developers or deployers. Private actors are bound through secondary EU legislation (e.g., EU AI Act, GDPR, Digital Services Act) and national transposing laws.
* **Limitations on Rights**: Any limitation on Charter rights must be provided for by law, respect the essence of those rights, and satisfy the proportionality principle [Article 52(1)].

---

### S3 — RIGHTS / DUTIES / SAFEGUARDS
* **Human Dignity (Article 1)**: Inviolable constitutional baseline; human dignity must be respected and protected in all AI policy and regulation.
* **Private Life & Data Protection (Articles 7 & 8)**: Guarantees protection of private and family life, home, and communications [Article 7], and protection of personal data processed fairly for specified purposes, subject to access, rectification, and independent authority control [Article 8(1)-(3)].
* **Non-Discrimination (Article 21)**: Prohibits any discrimination based on sex, race, colour, ethnic/social origin, genetic features, language, religion, disability, age, or sexual orientation [Article 21(1)].
* **High Level of Consumer Protection (Article 38)**: Guarantees a high level of consumer protection in Union policies.
* **Effective Remedy & Fair Trial (Article 47)**: Guarantees an effective remedy before an independent tribunal for anyone whose EU-guaranteed rights are violated, underpinning explainability and transparency requirements in automated decision-making.

---

### S4 — HSA THREAT RELEVANCE
* **Taxonomy Note**: Source is the EU Charter of Fundamental Rights. Because an HSA threat taxonomy is not selected in this single source, `THREAT_ID` is strictly `UNKNOWN`. No `THR-NNN` identifiers are invented.
* **Threat Analogies**:
  * *Cognitive Manipulation & Autonomy*: Analagously guarded by Article 1 (Dignity) & Article 3(1) (Integrity of person).
  * *Biometric Surveillance*: Analogously guarded by Article 7 (Private Life) & Article 8 (Data Protection).
  * *Algorithmic Discrimination*: Analogously guarded by Article 21(1) (Non-discrimination).
  * *Black-Box Decision-Making*: Analogously guarded by Article 47 (Effective Remedy & Fair Trial).

---

### S5 — EVIDENCE / ACCOUNTABILITY
* **Requirement Classification**: The Charter sets out constitutional rights and principles rather than technical logging specifications. All evidence candidates are classified as `RESEARCH_USEFUL` unless explicitly mandated by secondary legislation.
* **Key Research Artifacts**:
  * *Legality & Proportionality*: Legislative Impact Assessments and Explanatory Memoranda demonstrating Article 52(1) compliance.
  * *Data Protection*: Data Protection Impact Assessments (DPIAs) and DPA oversight records supporting Article 8 compliance.
  * *Non-Discrimination*: Algorithmic disparate impact audits and bias evaluation reports supporting Article 21 compliance.
  * *Effective Remedy*: Decision rationale notices and explanation records supporting Article 47 compliance.

---

### S6 — UNKNOWN / CONFLICT / CURRENTNESS
* **Scope Limit**: Article 51(1) explicitly limits direct Charter obligations to EU entities and Member States (when implementing Union law). Extending direct horizontal Charter duties to private actors without secondary law is an unsupported assumption (`SCOPE_LIMIT`).
* **Currentness**: Text is the 2016 consolidation (OJ C 202/02). The primary legal status is established by Article 6(1) TEU (2009). Case law from the CJEU continuously interprets Charter rights in the context of emerging AI technologies (`CURRENTNESS_LIMIT`).

---

### S7 — ENGINEERING RELEVANCE
* **Control Candidates**: Data minimization engines (Art 8), algorithmic bias mitigation filters (Art 21), and XAI rationale logging modules (Art 47).
* **Test Candidates**: Protected characteristic disparate impact testing, re-identification risk testing, and counterfactual rationale verification.
* **Evidence Artifacts**: `dpia_and_privacy_audit_report.pdf`, `algorithmic_bias_audit_results.json`, `xai_decision_rationale_log.csv`.
* **Status**: All engineering items are proposed as candidates (`SUPPORTING_RESEARCH`) for repository `fatihekler/ai-laws` under review of `AI-LAWS`. None are marked as implemented, tested, or effective.

---
