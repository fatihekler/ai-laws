# AI-LAWS Source Analysis: Regulation (EU) 2024/1689 (EU AI Act Consolidated)

**RUN_ID**: `RUN-20260915-001`  
**SOURCE_ID**: `EU-001`  
**PACK_ID**: `EU`  
**SHORT_TITLE**: `EU_AI_ACT_CONSOLIDATED`  
**CANONICAL**: `FALSE`  
**PROMOTION_STATE**: `FINDING_CANDIDATE`  
**PRIMARY_SOURCE_RECHECK_REQUIRED**: `FALSE`  

---

## S1 — Identity / Authority

* **Full Legal & Institutional Identity**: Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), as amended by Regulation (EU) 2026/1744 (M1) in consolidated text dated 27.07.2026 (`CELEX 02024R1689-20260727`).
* **Source Type**: Binding Union Harmonisation Legislation / Primary Legislative Act (`Article 288 TFEU`).
* **Binding State**: Binding in its entirety and directly applicable in all EU/EEA Member States.
* **Publication & Effective Dates**:
  * **Publication Date**: 12 July 2024 in Official Journal L 1689 (Amended by M1 Regulation 2026/1744 published 24 July 2026).
  * **Entry into Force**: 1 August 2024 (20th day following publication).
  * **General Application Date**: 2 August 2026 (`Article 113`).
  * **Staged Implementation Schedule**:
    * *Chapters I & II (General Provisions & Prohibited Practices)*: 2 February 2025.
    * *Chapter III Sec 4 (Notified Bodies), Chapter V (GPAI Models), Chapter VII (Governance), Chapter XII (Penalties)*: 2 August 2025.
    * *Chapter III Sec 1-3 (High-Risk AI Systems - Annex III)*: 2 December 2027.
    * *Chapter III Sec 1-3 (High-Risk AI Systems - Annex I Product Safety)*: 2 August 2028.
* **Scope Limitations & Exclusions**:
  * **National Security & Defense**: Does not apply to AI systems placed on the market or used exclusively for military, defense, or national security purposes (`Article 2(3)`).
  * **Scientific Research**: Does not apply to AI systems specifically developed and put into service for the sole purpose of scientific research and development (`Article 2(6)`).
  * **Personal Non-Professional Use**: Deployer obligations do not apply to natural persons using AI in the course of a purely personal non-professional activity (`Article 2(10)`).
  * **Open Source License Exception**: Free and open-source AI models are exempt from most requirements unless they present systemic risk or fall under prohibited/high-risk/transparency provisions (`Article 2(12)`, `Article 53(2)`).

---

## S2 — Scope / Definitions / Actors

### 1. Key Actors Defined
* **Provider**: Any natural or legal person, public authority, agency, or other body that develops an AI system or GPAI model, or has it developed, and places it on the market or puts it into service under its own name or trademark (`Article 3(3)`).
* **Deployer**: Any natural or legal person, public authority, agency, or other body using an AI system under its authority, except personal non-professional use (`Article 3(4)`).
* **Authorised Representative**: Any natural or legal person located in the Union who has received a written mandate from a non-EU provider to act on its behalf (`Article 3(5)`).
* **Importer**: Any natural or legal person located in the Union that places on the market an AI system bearing the name or trademark of a third-country person (`Article 3(6)`).
* **Distributor**: Any natural or legal person in the supply chain, other than the provider or importer, that makes an AI system available on the Union market (`Article 3(7)`).
* **Affected Person**: Any natural person located in the Union who is subject to or affected by an AI system (`Article 2(1)(g)`).

### 2. Systems, Products & Conduct Covered
* **AI System**: A machine-based system designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions (`Article 3(1)`).
* **General-Purpose AI Model (GPAI Model)**: An AI model trained with a large amount of data using self-supervision at scale, capable of competently performing a wide range of distinct tasks (`Article 3(63)`).
* **Prohibited AI Practices**: Practices using subliminal manipulation, exploiting vulnerabilities, social scoring, untargeted facial scraping, emotion recognition in workplace/education, and biometric categorisation of sensitive attributes (`Article 5`).
* **High-Risk AI Systems**: Systems listed in Annex III or serving as safety components of regulated products under Annex I (`Article 6`).

---

## S3 — Rights / Duties / Safeguards

### 1. Rights & Protections
* **Right to Explanation**: Affected persons have a right to obtain a clear and meaningful explanation of the role of a high-risk AI system in decisions that produce legal or similarly significant effects (`Article 86`).
* **Right to Lodge a Complaint**: Right to submit complaints to Market Surveillance Authorities regarding non-compliance (`Article 85`).
* **Whistleblower Protection**: Protection for individuals reporting infringements pursuant to Directive (EU) 2019/1397 (`Article 87`).

### 2. Mandatory Duties Matrix
* **Risk Management System (Providers)**: Continuous iterative risk management throughout the lifecycle (`Article 9`).
* **Data Governance (Providers)**: Quality criteria for training, validation, and testing datasets (`Article 10`).
* **Technical Documentation (Providers)**: Mandatory preparation prior to market placement (`Article 11 & Annex IV`).
* **Automated Logging (Providers)**: System capabilities for automatic recording of events (`Article 12`).
* **Transparency (Providers)**: Instructions for use and clear information for deployers (`Article 13`).
* **Human Oversight (Providers)**: Interface design enabling natural persons to oversee, intervene, or stop the AI (`Article 14`).
* **Accuracy, Robustness & Cybersecurity (Providers)**: Technical resilience against errors and adversarial attacks (`Article 15`).
* **Deployer Obligations**: Use according to instructions, assign competent human oversight, monitor operation, and retain automatically generated logs for at least 6 months (`Article 26`).
* **Fundamental Rights Impact Assessment (Deployers)**: Public bodies and private service providers must perform FRIA prior to deploying high-risk AI (`Article 27`).
* **Synthetic Content & Deepfake Transparency**: Labeling of AI-generated synthetic content and deepfakes (`Article 50`).

---

## S4 — HSA Threat Relevance

The source explicitly or analogically supports the following threat classifications:
1. **Subliminal Manipulation & Distortion**: Explicitly prohibited under `Article 5(1)(a)`.
2. **Exploitation of Vulnerabilities**: Explicitly prohibited under `Article 5(1)(b)`.
3. **Social Scoring & Automated Bias**: Explicitly prohibited under `Article 5(1)(c)`.
4. **Untargeted Facial Image Scraping**: Explicitly prohibited under `Article 5(1)(e)`.
5. **Emotion Recognition in Workplace/Education**: Explicitly prohibited under `Article 5(1)(f)`.
6. **Biometric Categorisation on Sensitive Attributes**: Explicitly prohibited under `Article 5(1)(g)`.
7. **Deepfakes & Unlabelled Synthetic Media**: Explicitly regulated under `Article 50(2), (4)`.
8. **Adversarial Attacks & Data Poisoning**: Explicitly mandated mitigation under `Article 15(5)` and `Article 55(1)(d)`.
9. **Automation Bias & Loss of Human Control**: Explicitly mitigated via human oversight tools under `Article 14(4)`.
10. **Critical Infrastructure Disruption**: Explicitly classified as High-Risk under `Annex III(2)` and `Article 3(49)(b)`.
11. **GPAI Systemic Risks & Cascading Failures**: Explicitly regulated under `Article 51` and `Article 55`.
12. **Agentic AI & Emerging Autonomy**: Supported analogically via Annex XIV registration code `AIH 0401`.

---

## S5 — Evidence / Accountability

### 1. Mandatory Compliance Evidence
* **Technical Documentation**: Comprehensive system architecture, risk file, and data governance records (`Article 11, Annex IV`).
* **EU Declaration of Conformity**: Signed attestation retained for 10 years (`Article 47, Annex V`).
* **Automatically Generated System Logs**: Tamper-evident logs retained for at least 6 months (`Article 12, Article 19, Article 26(6)`).
* **FRIA Assessment Report**: Documented Fundamental Rights Impact Assessment (`Article 27`).
* **EU Database Registration Record**: Public registration proof (`Article 49`).
* **Serious Incident Reports**: Mandatory reporting to authorities within statutory deadlines (`Article 73`).

### 2. Investigative & Supporting Evidence
* **Source Code & Data Access**: Accessible by market surveillance authorities upon reasoned request (`Article 74(12)-(13)`).
* **Red-Teaming Evaluation Logs**: Adversarial testing logs for systemic GPAI models (`Article 55(1)(a)`).
* **Regulatory Sandbox Exit Reports**: Proof of compliance learning from sandboxes (`Article 57(7)`).

---

## S6 — Unknown / Conflict / Currentness

* **KNOWN**: Comprehensive legal framework, risk-based classification, provider/deployer duties, and administrative penalties up to 35M EUR / 7% turnover (`Articles 1-113`).
* **UNKNOWN**: Final technical specifications of CEN/CENELEC harmonised standards (`Article 40`) and European AI Office Article 6(5) derogation benchmarks.
* **CONFLICT**: Tension between EU internal market harmonisation and Member States' national security exemptions (`Article 2(3)`).
* **CURRENTNESS_LIMIT**: Based on consolidated text as of 27 July 2026. Future secondary implementing acts remain subject to ongoing tracking.
* **TRANSLATION_LIMIT**: Verified against official English CELEX text (`02024R1689-20260727`).
* **SCOPE_LIMIT**: Excludes military/defense AI and purely non-professional personal use (`Article 2`).
* **EVIDENCE_GAP**: Inspection challenges for proprietary closed-weights GPAI models.

---

## S7 — Engineering Relevance

Candidate engineering controls, tests, and artifacts proposed for compliance architecture:
1. **Automated Logging Engine (`ALE-01`)**: Control candidate for `Article 12` log retention. Tested via Log Continuity & Tamper Tests (`system_runtime_logs.json`).
2. **Human Oversight Interface (`OVERSIGHT-01`)**: Emergency stop button and override UI for `Article 14`. Tested via Operator Override Response Tests (`human_oversight_telemetry.csv`).
3. **Adversarial Attack Shield (`ROBUST-01`)**: Defensive guardrails against prompt injection and data poisoning for `Article 15`. Tested via Adversarial Penetration Test Suite (`adversarial_test_report.pdf`).
4. **C2PA / Watermarking Injector (`WMARK-01`)**: Synthetic content labeling tool for `Article 50`. Tested via Automated Watermark Detection Tests (`watermark_verification_log.json`).
5. **Data Governance Pipeline (`DATA-01`)**: Data quality and bias filtering pipeline for `Article 10`. Tested via Demographic Parity & Bias Benchmarks (`data_quality_audit.json`).

*Note: All controls, tests, and artifacts are candidates (`FINDING_CANDIDATE`) and are not marked as implemented or verified.*

---

**PRIMARY_SOURCE_RECHECK_REQUIRED**: `FALSE`  
**DESTINATION_REPO**: `AI-LAWS / EU-COMPLIANCE-FRAMEWORK`  
**REVIEW_OWNER**: `Legal & AI Safety Engineering Working Group`  
**PROMOTION_STATE**: `FINDING_CANDIDATE`  
