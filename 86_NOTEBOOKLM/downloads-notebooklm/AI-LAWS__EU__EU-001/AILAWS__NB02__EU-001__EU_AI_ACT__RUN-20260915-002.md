# AI-LAWS Single Source Analysis: EU AI Act Consolidated Text (EU-001)

**RUN_ID**: RUN-20260915-002  
**PACK_ID**: NB02  
**SOURCE_ID**: EU-001  
**DESTINATION_REPO**: fatihekler/ai-laws  
**REVIEW_OWNER**: AI-LAWS  
**PROMOTION_STATE**: SUPPORTING_RESEARCH  
**PRIMARY_SOURCE_RECHECK_REQUIRED**: TRUE  

---

### S1 — IDENTITY / AUTHORITY
* **Belge Kimliği**: Regulation (EU) 2024/1689 of the European Parliament and of the Council (Artificial Intelligence Act), consolidated version dated 27.07.2026 including Regulation (EU) 2026/1744 amendment.
* **Kaynak Türü**: Binding EU Regulation / Primary Legislative Act.
* **Hukuki Bağlayıcılık**: Directly applicable and binding in all EU Member States.
* **Yayın ve Yürürlük / Uygulama Tarihleri**: 
  * Published: 12.07.2024 (OJ L 1689); M1 amendment 24.07.2026 (OJ L 1744).
  * Entry into Force: 01.08.2024.
  * Application: General application from 02.08.2026. Staged application: Chapters I & II apply from 02.02.2025; Chapter III Sec 4, V, VII, XII apply from 02.08.2025; Annex III high-risk applies from 02.02.2027 / 02.12.2027; Annex I high-risk applies from 02.08.2028. *Publication date != application date.*
* **Territorial & Scope Limits**: EEA relevance noted (requires EEA Joint Committee incorporation for EFTA states). Excludes military, defence, national security, and pure R&D uses prior to market entry [Article 2(3), (6)].

---

### S2 — SCOPE / ACTORS
* **Regüle Edilen Aktörler**: Providers [Article 3(3)], Deployers [Article 3(4)], Authorised Representatives [Article 3(5)], Importers [Article 3(6)], Distributors [Article 3(7)], and Downstream Providers [Article 3(68)].
* **Kapsam**: Machine-based AI systems operating with varying autonomy levels [Article 3(1)], General-Purpose AI (GPAI) models [Article 3(63)], and High-Risk AI systems (Annex I & Annex III) [Article 6].
* **İstisnalar**: Purely personal non-professional deployments [Article 2(10)], military/defence systems [Article 2(3)], and research/development prior to placing on market [Article 2(6)].

---

### S3 — RIGHTS / DUTIES / SAFEGUARDS
* **Sağlayıcı Yükümlülükleri**: Risk Yönetim Sistemi [Article 9], Veri Yönetişimi [Article 10], Teknik Dokümantasyon [Article 11, Annex IV], Otomatik Loglama [Article 12], Şeffaflık [Article 13], İnsan Gözetimi [Article 14], Doğruluk/Siber Güvenlik [Article 15].
* **Kullanıcı (Deployer) Yükümlülükleri**: Talimatlara uygun kullanım [Article 26(1)], İnsan gözetimi ataması [Article 26(2)], Temel Haklar Etki Değerlendirmesi (FRIA) [Article 27].
* **Genel Amaçlı YZ (GPAI) Yükümlülükleri**: Model dokümantasyonu ve telif özeti [Article 53]; sistemik riskli GPAI modelleri için (>=10^25 FLOPs) model değerlendirmesi, kitle riski analizi ve siber güvenlik [Article 55].

---

### S4 — HSA THREAT RELEVANCE
* **DIRECT_EXPLICIT**:
  * Subliminal Manipulation & Cognitive Control [Article 5(1)(a)]
  * Vulnerability Exploitation [Article 5(1)(b)]
  * Social Scoring & Discrimination [Article 5(1)(c)]
  * Biometric Mass Surveillance & Scraping [Article 5(1)(e), (h)]
  * Workplace/Educational Emotion Recognition [Article 5(1)(f)]
  * Sensitive Biometric Categorisation [Article 5(1)(g)]
  * Deepfakes & Synthetic Media Unlabelled Generation [Article 50(2), (4)]
  * Adversarial Attacks, Data Poisoning & Evasion [Article 15(5), Article 55(1)(d)]
  * Feedback Loops & Bias Propagation [Article 15(4)]
  * Automation Bias & Loss of Human Control [Article 14(4)(b), (e)]

---

### S5 — EVIDENCE / ACCOUNTABILITY
* **Zorunlu Uyum Kanıtları (SOURCE_REQUIRED)**:
  * Technical Documentation [Article 11, Annex IV]
  * EU Declaration of Conformity [Article 47, Annex V]
  * Automatically Generated System Logs (Min 6 months) [Article 12, Article 19, Article 26(6)]
  * Fundamental Rights Impact Assessment (FRIA) Report [Article 27]
  * EU Database Registration Record [Article 49]
  * Serious Incident Reports [Article 73]
  * GPAI Copyright Compliance & Training Summary [Article 53(1)(c)-(d)]
* **Araştırma/Denetim Kanıtları (RESEARCH_USEFUL)**:
  * Model Source Code & Architecture Details [Article 74(13)]

---

### S6 — UNKNOWN / CONFLICT
* **KNOWN**: Risk-based classification framework, explicit obligations for high-risk AI providers/deployers, administrative fine structure up to 35M EUR / 7% turnover [Article 99].
* **UNKNOWN**: Practical guidelines for Article 6(3) derogations [Article 6(5)]; finalized CEN/CENELEC Harmonised Standards [Article 40].
* **CONFLICT**: Tension between EU internal market harmonization and national security derogations retained by Member States [Article 2(3), Article 5(2)].
* **CURRENTNESS_LIMIT**: Consolidated text dated 27.07.2026.
* **EVIDENCE_GAP**: Inspection challenges for proprietary closed-source GPAI models without full source code access.

---

### S7 — ENGINEERING RELEVANCE
* **CONTROL_CANDIDATE**: Immutable Audit Logging Module [Article 12], Human Oversight Emergency Stop Controls [Article 14], Automated Data Bias Pipeline [Article 10], C2PA Watermarking Injector [Article 50], Adversarial Guardrails [Article 15].
* **TEST_CANDIDATE**: Log Integrity Test, Automation Bias Override Latency Test, Demographic Parity Benchmark, Watermark Detection Robustness Test, Prompt Injection Red-Teaming Suite.
* **EVIDENCE_ARTIFACT**: `audit_log_archive.json`, `human_oversight_spec.pdf`, `data_provenance_log.csv`, `synthetic_media_record.json`, `threat_model_pen_test.pdf`.
*(Note: Engineering candidates are candidates only; not implemented, tested, or verified).*
