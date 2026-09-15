# AI-LAWS / HSA Single Source Analysis: EU-004 (Charter of Fundamental Rights)

**RUN_ID**: `RUN-20260915-012`  
**PACK_ID**: `NB02`  
**SOURCE_ID**: `EU-004`  
**DESTINATION_REPO**: `fatihekler/ai-laws`  
**REVIEW_OWNER**: `AI-LAWS`  
**PRIMARY_SOURCE_RECHECK_REQUIRED**: `TRUE`  
**PROMOTION_STATE**: `SUPPORTING_RESEARCH`  

---

### S1 — IDENTITY / AUTHORITY
* **Document Identity**: Charter of Fundamental Rights of the European Union (2016/C 202/02; CELEX 32012P/TXT). Published in OJ C 202, 7.6.2016, p. 389–405 [Title Page].
* **Source Type & Authority Class**: Primary Law / EU Constitutional Law [Art. 51]. Solemnly proclaimed by the European Parliament, Council, and Commission on 7 December 2000 and 12 December 2007; rendered legally binding with the entry into force of the Treaty of Lisbon on 1 December 2009 (Art. 6(1) TEU) [Art. 51]. Publication date (2016-06-07) != effective date (2009-12-01).
* **Scope & Territorial Limits**: Applies to EU institutions, bodies, offices, and agencies, and to EU Member States **only when implementing Union law** [Art. 51(1)]. EEA relevance does not imply automatic EEA applicability unless incorporated into the EEA Agreement.

---

### S2 — SCOPE / ACTORS
* **Regulated Actors**:
  1. **EU Institutions, Bodies, Offices, and Agencies**: Bound at all times to respect rights, observe principles, and promote fundamental rights [Art. 51(1)].
  2. **EU Member States**: Bound **only when implementing Union law** [Art. 51(1)].
  3. **Individuals / Right Holders**: Everyone within the jurisdiction of EU law [Art. 1, Art. 8, Art. 21, Art. 41, Art. 47].
* **Exclusions & Scope Limitations**:
  * **No Direct Private Actor Duty**: Article 51(1) strictly limits Charter duties to public EU/Member State entities. The Charter does not create direct, general constitutional duties for private commercial entities or AI developers in the text itself.
  * **No Competence Extension**: The Charter does not extend the field of application of Union law beyond the powers of the Union or establish any new power or task for the Union [Art. 51(2)].
  * **Unmentioned Technical Concepts**: Terms such as *data minimization*, *DPIA*, *DPO*, or *algorithmic transparency* are `OUTSIDE_SELECTED_SOURCE` and belong to secondary law (GDPR/EU-005, AI Act/EU-001).

---

### S3 — RIGHTS / DUTIES / SAFEGUARDS
* **Right to Protection of Personal Data [Art. 8(1)-(3)]**:
  * **Rights**: Everyone has the right to protection of personal data concerning him or her [Art. 8(1)], right of access to collected data, and right of rectification [Art. 8(2)].
  * **Processing Condition**: Data must be processed fairly for specified purposes and on the basis of consent or another legitimate basis laid down by law [Art. 8(2)].
  * **Mandatory Safeguard**: Compliance shall be subject to control by an independent authority [Art. 8(3)].
* **Right to Good Administration [Art. 41(1)-(3)]**:
  * **Rights**: Right to have affairs handled impartially, fairly, and within a reasonable time [Art. 41(1)]. Includes right to be heard, right of access to file, and mandatory **obligation of the administration to give reasons for its decisions** [Art. 41(2)].
* **Non-Discrimination & Equality [Art. 20, Art. 21(1)]**:
  * **Prohibition**: Prohibition of discrimination based on sex, race, colour, ethnic/social origin, genetic features, language, religion/belief, political opinion, disability, age, sexual orientation [Art. 21(1)].
* **Right to an Effective Remedy & Fair Trial [Art. 47]**:
  * **Safeguards**: Right to effective remedy before a tribunal, fair and public hearing within a reasonable time by an independent tribunal, legal advice, defence, and legal aid [Art. 47].

---

### S4 — HSA THREAT RELEVANCE
*Note*: HSA taxonomy is not present in the selected source text. All Threat IDs are categorized as `UNKNOWN` with `ANALOGICAL` relationship class. No `THR-NNN` identifiers are invented.
1. **THREAT_ID=UNKNOWN | Automated Bias & Discriminatory Output Risk** (`ANALOGICAL`): Violation of non-discrimination principles [Art. 21(1)] through biased automated processing.
2. **THREAT_ID=UNKNOWN | Unlawful Data Processing & Data Exploitation** (`ANALOGICAL`): Infringement of data protection principles [Art. 8(1)-(3)] via unverified processing.
3. **THREAT_ID=UNKNOWN | Opacification & Unreasoned Automated Decisions** (`ANALOGICAL`): Breach of administrative duty to give reasons [Art. 41(2)(c)] when using black-box automated systems.
4. **THREAT_ID=UNKNOWN | Deprivation of Judicial Review** (`ANALOGICAL`): Compromising the right to effective remedy and fair trial [Art. 47] through unreviewable automated decisions.

---

### S5 — EVIDENCE / ACCOUNTABILITY
* **Mandatory Source-Required Evidence (`SOURCE_REQUIRED`)**:
  1. **Independent Authority Control**: Official audit reports or decision notices demonstrating independent supervisory oversight [Art. 8(3)].
  2. **Statement of Reasons**: Written, explicit legal and factual reasons accompanying administrative decisions [Art. 41(2)(c)].
* **Research-Useful Evidence (`RESEARCH_USEFUL`)**:
  1. **Lawful Basis & Consent Documentation**: Verifiable consent records or legal basis documentation [Art. 8(2)].
  2. **Technical Logging & Model Reasoning Logs**: Immutable decision logs and prompt trails supporting administrative explanation and judicial review [Art. 41(2)(c), Art. 47] (engineering best-practice, not explicitly named in Charter text).

---

### S6 — UNKNOWN / CONFLICT / CURRENTNESS
* **Scope Limit [Art. 51(1)]**: Article 51(1) strictly limits Charter applicability to EU institutions and Member States implementing EU law. Direct legal duties for private commercial entities cannot be inferred directly from the Charter text without secondary legislation.
* **Evidence Gap**: Technical data protection mechanisms (*data minimization*, *DPIA*, *DPO*) are absent from Charter text and flagged as `OUTSIDE_SELECTED_SOURCE`.
* **Currentness**: Based on 2016 consolidated text (OJ C 202). Effective since 2009-12-01. Primary source recheck required before final legal finding (`PRIMARY_SOURCE_RECHECK_REQUIRED=TRUE`).

---

### S7 — ENGINEERING RELEVANCE
*Candidate controls and tests (not implemented/tested/effective in source text)*:
1. **Algorithmic Fairness Guardrail (`CONTROL_CANDIDATE`)**: Bias detection pipeline enforcing non-discrimination [Art. 21(1)]. Test candidate: Disparate impact testing across protected attributes. Artifact: `bias_evaluation_report.json`.
2. **Data Rights Processing Pipeline (`CONTROL_CANDIDATE`)**: Purpose-bound processing with consent logging and access/rectification workflows [Art. 8(1)-(3)]. Artifact: `data_access_rectification_audit.log`.
3. **Decision Explainability Module (`CONTROL_CANDIDATE`)**: Automated reasoning generator satisfying administrative reason-giving duties [Art. 41(2)(c)]. Artifact: `decision_rationale_artifact.pdf`.

---
