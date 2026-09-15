# AI-LAWS Single Source Analysis: EU-005 (GDPR)

**RUN_ID**: RUN-20260915-006  
**PACK_ID**: NB02  
**SOURCE_ID**: EU-005  
**TITLE**: Regulation (EU) 2016/679 (General Data Protection Regulation - GDPR)  
**PROMOTION_STATE**: SUPPORTING_RESEARCH  
**PRIMARY_SOURCE_RECHECK_REQUIRED**: TRUE  

---

### S1 — Identity / Authority
* **Full Title**: Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation) [Title Preamble].
* **Issuer**: European Parliament and Council of the European Union.
* **Jurisdiction**: European Union / European Economic Area.
* **Document Number**: Regulation (EU) 2016/679 / CELEX 32016R0679.
* **Authority Class**: Binding EU Regulation / Primary Legislative Act.
* **Binding State**: Directly applicable in all EU Member States [Art. 99(2)].
* **Dates**: Publication: 04.05.2016 (OJ L 119); Entry into Force: 24.05.2016 [Art. 99(1)]; Application Date: 25.05.2018 [Art. 99(2)].

### S2 — Scope / Actors
* **Actors**: Data Controller [Art. 4(7)], Data Processor [Art. 4(8)], Data Subject [Art. 4(1)], Supervisory Authority [Art. 4(22), Art. 51], Data Protection Officer (DPO) [Art. 37].
* **System / Data Scope**: Processing of personal data wholly or partly by automated means, or non-automated processing forming part of a filing system [Art. 2(1)].
* **Exclusions**: Processing outside EU law scope, purely personal or household activity [Art. 2(2)(c)], or law enforcement/national security processing by competent authorities [Art. 2(2)(d)].

### S3 — Rights / Duties / Safeguards
* **Core Principles**: Lawfulness, fairness, transparency, purpose limitation, data minimisation, accuracy, storage limitation, integrity/confidentiality, and accountability [Art. 5(1)-(2)].
* **Data Subject Rights**: Right of access [Art. 15], rectification [Art. 16], erasure/to be forgotten [Art. 17], restriction [Art. 18], data portability [Art. 20], objection [Art. 21], and protection against solely automated decision-making/profiling [Art. 22].
* **Key Controller Duties**: Data protection by design & default [Art. 25], security of processing [Art. 32], breach notification within 72h [Art. 33], DPIA execution for high-risk processing [Art. 35], and ROPA maintenance [Art. 30].
* **Enforcement & Penalties**: Administrative fines up to 20M EUR or 4% of global annual turnover [Art. 83(5)].

### S4 — HSA Threat Relevance
* **Automated Decision-Making & Profiling Risk**: Directly regulated with strict prohibitions and mandatory human intervention pathways [Art. 22, Recital 71].
* **Biometric & Sensitive Data Exploitation Risk**: Special category data processing prohibited unless explicit legal exception applies [Art. 9].
* **Data Breach & Unauthorized Access Risk**: Mandatory technical security, encryption, and 72-hour breach reporting [Art. 32, Art. 33].
* **Opacity of AI Logic**: Addressed via mandatory transparency and 'meaningful information about the logic involved' [Art. 13(2)(f), Art. 15(1)(h)].

### S5 — Evidence / Accountability
* **Required Evidence**: Records of Processing Activities (ROPA) [Art. 30], DPIA Reports [Art. 35], Data Breach Documentation [Art. 33(5)], Data Processing Agreements (DPA) [Art. 28(3)], and Consent Logs [Art. 7(1)].

### S6 — Unknown / Conflict / Currentness
* **Unknowns**: GDPR does not explicitly use the term 'Artificial Intelligence', applying functionally to all 'automated processing'.
* **Currentness Limit**: Adopted 2016, applicable 2018. Subsequent EDPB guidelines and CJEU jurisprudence provide practical operational interpretations.

### S7 — Engineering Relevance
* **Control Candidates**: Human-in-the-loop override interface [Art. 22], automated privacy-by-default schema filters [Art. 25], and continuous data pipeline encryption [Art. 32].
* **Test Candidates**: Automated decision pipeline human-review test, API payload data minimisation test, and breach alert latency test.
* **Evidence Artifacts**: `human_override_audit_trail.log`, `privacy_by_default_schema_test.json`, `security_audit_report.pdf`.
