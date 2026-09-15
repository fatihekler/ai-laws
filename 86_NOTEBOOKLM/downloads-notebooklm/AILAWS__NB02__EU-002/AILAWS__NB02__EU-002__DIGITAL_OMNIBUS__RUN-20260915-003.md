# AI-LAWS Source Analysis: Regulation (EU) 2026/1744 (Digital Omnibus on AI)

**RUN_ID**: RUN-20260915-003  
**PACK_ID**: NB02  
**SOURCE_ID**: EU-002  
**SHORT_TITLE**: DIGITAL_OMNIBUS  
**PRIMARY_SOURCE_RECHECK_REQUIRED**: TRUE  
**PROMOTION_STATE**: SUPPORTING_RESEARCH  
**DESTINATION_REPO**: fatihekler/ai-laws  
**REVIEW_OWNER**: AI-LAWS  

---

## S1 — Identity / Authority

* **Full Legal Title**: Regulation (EU) 2026/1744 of the European Parliament and of the Council of 8 July 2026 amending Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230 as regards the simplification of the implementation of harmonised rules on artificial intelligence (Digital Omnibus on AI) `[Title; Recital 1; Art. 1]`.
* **Authority Class & Legal Nature**: Binding EU Regulation (Amending Primary Legislative Act) adopted under the Ordinary Legislative Procedure pursuant to Article 114 of the Treaty on the Functioning of the European Union (TFEU) `[Title; Preamble; Recital 1]`.
* **Publication & Entry into Force**:
  * **Published**: Official Journal of the European Union, OJ L series 2026/1744 on 24 July 2026 `[OJ L Header]`.
  * **Entry into Force**: 27 July 2026 (the third day following publication in accordance with Article 4 and Recital 46) `[Recital 46; Art. 4]`.
* **Staggered Application Timetable**:
  * **27 July 2026**: Immediate application of Articles 102 to 110 amendments `[Art. 1(40)(c)]`.
  * **2 December 2026**: Application of explicit prohibitions on AI systems generating/manipulating non-consensual intimate material (NCII) and child sexual abuse material (CSAM) `[Art. 1(7), Art. 1(40)(a)]`; end of 4-month transitional period for generative AI marking under Art. 50(2) `[Art. 1(39)(b)]`.
  * **2 August 2027**: Deadline for national AI regulatory sandboxes operationalization `[Art. 1(22)(a)]`; Commission delegated acts on sectoral equivalence `[Art. 1(3)]`; Commission post-market monitoring guidance `[Art. 1(30)]`.
  * **2 December 2027**: Deferred application date for Chapter III Sections 1, 2, 3 high-risk AI obligations under Annex III `[Recital 40; Art. 1(40)(b)(i)]`.
  * **2 August 2028**: Deferred application date for Chapter III Sections 1, 2, 3 high-risk AI obligations under Annex I `[Recital 40; Art. 1(40)(b)(ii)]`; application of Machinery Regulation (EU) 2023/1230 delegated acts `[Art. 3(1)]`.
* **Territorial Scope & EEA Relevance**: Text marked with EEA relevance. However, EEA relevance does not constitute automatic application in EFTA EEA states (Iceland, Liechtenstein, Norway) without formal incorporation into Annex XI of the EEA Agreement by decision of the EEA Joint Committee `[Title; Scope Limitations]`.

---

## S2 — Scope / Actors

### 1. Key Actors Regulated
* **Providers**: Entities developing or placing AI systems or GPAI models on the market `[Reg (EU) 2024/1689 Art. 3(3)]`. Amending regulation simplifies technical documentation (Annex IV) and QMS (Art. 17) for SMEs, start-ups, and Small Mid-cap Enterprises (SMCs) `[Art. 1(10), (11), (26)]`.
* **Deployers**: Entities using AI systems under their authority. Prohibited from using AI for the purpose of generating/manipulating NCII or CSAM `[Art. 1(7) amending Art. 5(1a)(b)]`. Granted DPIA cross-referencing stream in FRIA `[Art. 1(13)]`.
* **Small Mid-cap Enterprises (SMCs)**: Defined under Commission Recommendation (EU) 2025/1099 as enterprises outgrowing SMEs but requiring proportionate compliance support `[Recital 6; Art. 1(4)(b) inserting Art. 3(14b)]`. Fines capped at lower of percentage or fixed amount `[Art. 1(38)(c)]`.
* **European AI Office**: Granted exclusive supervisory and enforcement competence over GPAI-based AI systems (within same undertaking) and AI systems integrated into VLOPs/VLOSEs under DSA Regulation (EU) 2022/2065 `[Recitals 31-34; Art. 1(31) amending Art. 75; Art. 1(32) inserting Arts. 75a-75d]`.
* **Initial & Succeeded Providers**: Succeeded providers assume provider status upon substantial modification; initial providers must provide technical documentation and access unless clearly specifying non-conversion `[Art. 1(12)(a) amending Art. 25(2)]`.

### 2. Systems & Conduct Covered
* **Safety Components**: Redefined to focus strictly on components fulfilling a safety function (preventing/mitigating health/safety risks). Non-safety functions (user assistance, performance optimization, service efficiency, automation, convenience, quality control) do not qualify `[Recital 7; Art. 1(4)(a) amending Art. 3(14); Art. 1(8) amending Art. 6(1a)-(1c)]`.
* **Prohibited AI Practices (Art. 5)**:
  * **NCII Generation/Manipulation**: Placing on market, putting into service, or use of AI generating/manipulating realistic intimate parts or sexually explicit depictions without explicit consent `[Art. 1(7) amending Art. 5(1)(ba)]`.
  * **CSAM Generation/Manipulation**: Placing on market, putting into service, or use of AI generating/manipulating CSAM, except under law enforcement 'without right' defence `[Art. 1(7) amending Art. 5(1)(bb)]`.
* **Annex XIV Typology & Codes**: Introduces AIP codes (product safety), AIB codes (biometric AI), and AIH codes (horizontal tech), explicitly including **AIH 0401 Agentic AI** `[Recital 43; Art. 1(43) adding Annex XIV]`.

---

## S3 — Rights / Duties / Safeguards

### 1. Explicit Rights & Safeguards
* **Fundamental Rights Protection**: Explicit prohibition of NCII/CSAM safeguards human dignity, personal autonomy, private life, and rights of the child under Articles 1, 3, 4, 7, 8, 21, 23, 24 of the Charter of Fundamental Rights `[Recital 14]`.
* **Processing of Special Categories of Personal Data (Art. 4a)**: Provides explicit legal basis under Art 9(2)(g) GDPR for processing special categories of data strictly for bias detection and correction for high-risk AI and other AI systems, subject to strict safeguards (pseudonymization, strict access, deletion upon correction, ROPA docs) `[Recital 9; Art. 1(6) inserting Art. 4a]`.
* **Procedural Rights & CJEU Review**: Operators subject to AI Office investigations enjoy full rights of defence, access to file via negotiated disclosure, and CJEU review over decisions and fines `[Art. 1(32) inserting Arts. 75c(6), 75d]`.

### 2. Core Mandatory Duties
* **AI Literacy Measures**: Providers and deployers must take measures to support staff AI literacy considering context and technical background. Does NOT require guaranteeing individual literacy levels `[Art. 1(5) replacing Art. 4]`.
* **NCII/CSAM Technical Safety Controls**: Providers must deploy reasonable and adequate state-of-the-art preventive safeguards (refusal training, prompt guardrails, output controls, content filtering) where generation is a reasonably foreseeable outcome `[Recital 17; Art. 1(7) amending Art. 5(1a)(a)(ii)]`.
* **Generative AI Marking**: Providers of generative AI must mark synthetic content under Art. 50(2), with a 4-month transitional period until 2 December 2026 for existing systems `[Art. 1(39)(b) adding Art. 111(4)]`.
* **Upstream Supply Chain Written Agreements**: High-risk AI providers and third-party suppliers must execute written agreements specifying technical access, documentation, and capabilities `[Art. 1(12)(b) amending Art. 25(4)]`.

---

## S4 — HSA Threat Relevance

The source explicitly supports and addresses key threats within the AI-LAWS taxonomy:
* **Generation & Proliferation of Non-Consensual Intimate Material (NCII / Deepfake Nudity)**: `DIRECT_EXPLICIT` — Specifically prohibited under amended Art. 5(1)(ba) due to severe harms to human dignity, privacy, and health safety `[Recitals 10-12; Art. 1(7)]`.
* **Generation & Proliferation of Child Sexual Abuse Material (CSAM)**: `DIRECT_EXPLICIT` — Specifically prohibited under amended Art. 5(1)(bb) due to grave threats to child safety and human dignity `[Recitals 10, 11, 13; Art. 1(7)]`.
* **Algorithmic Bias, Discrimination & Demographic Disparities**: `DIRECT_EXPLICIT` — Addressed by establishing Art. 4a legal basis allowing processing of special data categories for bias detection/correction `[Recital 9; Art. 1(6)]`.
* **Inadequate Technical Safeguards & Control Circumvention**: `DIRECT_EXPLICIT` — Addressed by mandating state-of-the-art technical preventive and corrective safeguards `[Recital 17; Art. 1(7)]`.
* **Complex Societal Harms from VLOP / VLOSE Integrated AI**: `DIRECT_EXPLICIT` — Addressed by establishing exclusive EU AI Office supervision over VLOP/VLOSE integrated AI `[Recital 32; Art. 1(31)]`.
* **Emerging Autonomous Behaviours & Agentic AI Security Risks**: `DIRECT_EXPLICIT` — Explicitly codified under Annex XIV Code **AIH 0401 Agentic AI** `[Recital 43; Art. 1(43)]`.

---

## S5 — Evidence / Accountability

### 1. Mandatory Compliance Evidence
* **Explicit Consent Records**: Required for providers/deployers of systems intended for intimate material generation `[Recital 20; Art. 1(7)]`.
* **ROPA Bias Documentation**: Required under Art. 4a(1)(f) documenting why processing special data was strictly necessary for bias detection/correction `[Art. 1(6)]`.
* **Technical Safeguard Documentation**: Evidence of refusal training, prompt guardrails, and filtering mechanisms for generative AI `[Recital 17; Art. 1(7)]`.
* **Commission Simplified Technical Form**: Simplified Annex IV technical documentation for SMEs and SMCs `[Art. 1(10)]`.
* **FRIA & DPIA Cross-Reference Docs**: Completed FRIA questionnaire utilizing AI Office template `[Art. 1(13)]`.
* **Upstream Written Agreements**: Written contracts between high-risk providers and component suppliers `[Art. 1(12)(b)]`.

### 2. Regulatory & Investigative Evidence
* **AI Office Investigation & Inspection Records**: Business records, data copies, oral/written explanations, binding commitments, and formal decisions `[Art. 1(32) inserting Arts. 75a-75d]`.
* **Real-World Testing Framework Notifications**: Member State frameworks and real-world testing plans submitted to Commission `[Art. 1(25) inserting Art. 60a]`.

---

## S6 — Unknown / Conflict / Currentness

* **KNOWN**: Clear statutory amendments expanding Art. 5 prohibitions to NCII/CSAM; legal basis for bias processing under Art. 4a; AI Office exclusive jurisdiction over GPAI and VLOPs; deferred application dates (Dec 2027 / Aug 2028).
* **UNKNOWN**: Specific product categories where AI Act requirements may be limited via Commission delegated acts under Art. 2(13) (by Aug 2027); specific guidance and template for post-market monitoring plans (by Sept 2027).
* **CURRENTNESS_LIMIT**: Regulation (EU) 2026/1744 published on 24 July 2026. Entry into force on 27 July 2026. Staggered application dates extend through 2 August 2028.
* **SCOPE_LIMIT**: Analysis strictly limited to Regulation (EU) 2026/1744 (EU-002). No unselected notebook sources or external knowledge used.

---

## S7 — Engineering Relevance

### Candidate Engineering Controls & Artifacts
* **NCII / CSAM Generation Prevention Pipeline**: `CONTROL_CANDIDATE` — Multimodal content moderation, refusal fine-tuning, runtime prompt guardrails, output classification/filtering, and image/video hashing. `EVIDENCE_ARTIFACT`: Guardrail Configuration Log, Content Filtering Audit Report, Red-Teaming Test Report. `[Recital 17; Art. 1(7)]`.
* **Explicit Consent Verification Protocol**: `CONTROL_CANDIDATE` — Authenticated consent capture and distribution mechanism for legitimate intimate material generation. `EVIDENCE_ARTIFACT`: Signed Consent Record / Cryptographic Token Audit Log. `[Recital 20; Art. 1(7)]`.
* **Bias Audit Pipeline with Automated Deletion**: `CONTROL_CANDIDATE` — Isolated bias detection workflow utilizing pseudonymized special data with strict access controls and auto-deletion trigger upon bias correction. `EVIDENCE_ARTIFACT`: ROPA Bias Log, Access Control Log, Automated Deletion Certificate. `[Art. 1(6) inserting Art. 4a]`.
* **Generative AI C2PA Watermarking Engine**: `CONTROL_CANDIDATE` — Digital watermarking and metadata injection engine for synthetic audio/image/video/text content. `EVIDENCE_ARTIFACT`: Watermark Verification Log, C2PA Manifest. `[Art. 1(39)(b)]`.
* **SME/SMC Simplified Documentation Engine**: `CONTROL_CANDIDATE` — Automated documentation generator conforming to Commission simplified form for SMEs/SMCs. `EVIDENCE_ARTIFACT`: Simplified Technical Documentation Package (Annex IV JSON/PDF). `[Art. 1(10)]`.

*(Note: All engineering items are candidate controls/artifacts; none are certified as implemented, tested, or effective.)*
