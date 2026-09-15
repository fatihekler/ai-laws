# AI-LAWS Single Source Analysis: EU-004

**RUN_ID**: `RUN-20260915-005`  
**PACK_ID**: `NB02`  
**SOURCE_ID**: `EU-004`  
**TITLE**: Charter of Fundamental Rights of the European Union (2016/C 202/02)  
**CANONICAL**: `FALSE`  
**PROMOTION_STATE**: `SUPPORTING_RESEARCH`  
**PRIMARY_SOURCE_RECHECK_REQUIRED**: `TRUE`  

---

### S1 — IDENTITY / AUTHORITY
* **Full Legal Identity**: Charter of Fundamental Rights of the European Union, proclaimed solemnly by the European Parliament, Council, and Commission. Consolidated text published in OJ C 202, 7.6.2016, p. 389–405 (`2016/C 202/02`).
* **Source Type**: Primary Constitutional Law (Treaty-level value under Article 6(1) TEU).
* **Binding State**: Legally binding in its entirety across the European Union.
* **Dates**:
  * Originally Proclaimed: 7 December 2000.
  * Legally Binding (Effective Date): 1 December 2009 (entry into force of the Treaty of Lisbon).
  * Consolidated Publication Date: 7 June 2016 (OJ C 202).
* **Scope & Amendment**:
  * Addressed to EU institutions, bodies, offices, and agencies in all actions (Art 51(1)).
  * Addressed to Member States **ONLY when they are implementing Union law** (Art 51(1)).
  * Does not extend Union competence beyond Treaties (Art 51(2)).

---

### S2 — SCOPE / ACTORS
* **Regulated Actors**:
  * **EU Institutions, Bodies, Offices, and Agencies**: Bound by all provisions across all activities (Art 51(1)).
  * **Member States**: Bound strictly when implementing EU law (Art 51(1)).
  * **Natural and Legal Persons**: Right-holders under Titles I–VI; data controllers/processors subject to Art 8 duties.
* **Covered Conduct & Data**:
  * Personal data processing (fair processing, specified purpose, consent/statutory basis, access, rectification, independent authority supervision) (Art 8).
  * Administrative procedures adversely affecting individuals (right to be heard, access to file, duty to state reasons) (Art 41).
  * Judicial proceedings enforcing EU rights (effective remedy, fair hearing, legal aid, presumption of innocence) (Art 47–49).
* **Exclusions & Exceptions**:
  * Purely national matters unlinked to EU law implementation fall outside Charter scope (Art 51(1)).
  * Rights limitations must be provided for by law, respect the essence of rights, and satisfy proportionality (Art 52(1)).

---

### S3 — RIGHTS / DUTIES / SAFEGUARDS
* **Key Rights & Safeguards**:
  * **Human Dignity & Integrity**: Inviolable dignity (Art 1); physical/mental integrity and free informed consent (Art 3).
  * **Private Life & Data Protection**: Respect for private/family life, home, communications (Art 7); right to protection of personal data, fair processing, consent/legal basis, access, rectification, independent supervision (Art 8).
  * **Non-Discrimination**: Absolute prohibition of discrimination on any ground including sex, race, genetic features, religion, disability, age, sexual orientation (Art 21).
  * **Good Administration**: Right to impartial handling, right to be heard, access to file, obligation of administration to state reasons for decisions, compensation for damage (Art 41).
  * **Effective Judicial Remedy**: Right to fair/public hearing before independent tribunal, legal aid, presumption of innocence (Art 47–48).
* **Mandatory Actor Duties**:
  * **EU Bodies & Member States (when implementing EU law)**: Duty to respect rights, observe principles, and promote application (Art 51(1)).
  * **Data Processors**: Duty to process data fairly for specified purposes on consent/statutory basis (Art 8(2)).
  * **Public Administrations**: Duty to state reasons for decisions (Art 41(2)(c)).

---

### S4 — HSA THREAT RELEVANCE
* **THR-001 / Privacy & Surveillance Threats**: `ANALOGICAL` — Automated surveillance or unauthorized data exploitation threatens private life (Art 7) and data protection guarantees (Art 8).
* **THR-002 / Algorithmic Discrimination & Bias**: `ANALOGICAL` — AI profiling or algorithmic decision systems generating biased outputs breach the constitutional prohibition of discrimination (Art 21).
* **THR-003 / Human Dignity & Autonomy Impairment**: `ANALOGICAL` — Subliminal manipulation or intrusive neurotechnology subverting human agency violates inviolable dignity (Art 1) and mental integrity (Art 3(1)).
* **THR-004 / Opaque Automated Decision-Making**: `ANALOGICAL` — Black-box AI systems operating in public administration without explainability or statement of reasons breach the right to good administration (Art 41(2)(c)) and effective judicial remedy (Art 47).

---

### S5 — EVIDENCE / ACCOUNTABILITY
* **Mandatory Compliance Evidence**:
  * **Consent / Statutory Basis Records**: Documented proof of explicit consent or legitimate legal basis for personal data processing (Art 8(2)).
  * **Independent Authority Audit Reports**: Official supervision and audit findings from independent data protection authorities (Art 8(3)).
  * **Written Statements of Reasons**: Official documentation stating the exact rationale for administrative decisions (Art 41(2)(c)).
  * **Judicial Review Records**: Court files, public hearing transcripts, and reasoned judgments (Art 47).

---

### S6 — UNKNOWN / CONFLICT / CURRENTNESS
* **KNOWN**: Comprehensive 54-article catalog of EU fundamental rights, freedoms, and principles.
* **UNKNOWN**: Specific technical implementation rules or metrics for AI or digital technologies (deferred to secondary legislation like EU AI Act 2024/1689 or GDPR 2016/679).
* **SCOPE_LIMIT**: Applies to Member States ONLY when implementing Union law (Art 51(1)).
* **CURRENTNESS_LIMIT**: Consolidated text published 07.06.2016 (OJ C 202). Live recheck on EUR-Lex required for any subsequent treaty updates.

---

### S7 — ENGINEERING RELEVANCE
* **CONTROL_CANDIDATE**:
  1. *Consent & Purpose Limitation Enforcement Pipeline* (supporting Art 8).
  2. *Algorithmic Fairness & Bias Mitigation Audit Engine* (supporting Art 21).
  3. *Automated Decision Rationale & Explainability Generator* (supporting Art 41(2)(c)).
* **TEST_CANDIDATE**:
  1. *Consent Verification & Data Minimization Audit Test*.
  2. *Demographic Parity & Disparate Impact Benchmark Test*.
  3. *Decision Rationale Traceability & Explainability Test*.
* **EVIDENCE_ARTIFACT**:
  1. `data_protection_impact_assessment.json`
  2. `algorithmic_bias_audit_report.json`
  3. `decision_explanation_log.json`

---

PRIMARY_SOURCE_RECHECK_REQUIRED: TRUE  
DESTINATION_REPO: fatihekler/ai-laws  
REVIEW_OWNER: AI-LAWS  
PROMOTION_STATE: SUPPORTING_RESEARCH  
