# SOURCE ANALYSIS: EU-001 (EU_AI_ACT_CONSOLIDATED)

## S1 — IDENTITY / AUTHORITY
* **Belge Kimliği**: Avrupa Parlamentosu ve Konseyi'nin (AB) 2024/1689 sayılı Yapay Zekâ Tüzüğü (Artificial Intelligence Act), 27 Temmuz 2026 tarihli konsolide sürümü (M1 Düzenlemesi (AB) 2026/1744 işlenmiş hali).
* **Kaynak Türü**: Bağlayıcı Birlik Uyum Mevzuatı (Binding EU Regulation / Primary Legislative Act).
* **Bağlayıcılık Durumu**: Tüm Üye Devletlerde bütün hükümleriyle doğrudan bağlayıcı ve uygulanabilirdir.
* **Yayın ve Yürürlük Takvimi**:
  * Yayın Tarihi: 12 Temmuz 2024 (OJ L 1689); M1 Değişikliği: 24 Temmuz 2026 (OJ L 1744).
  * Yürürlüğe Giriş: 1 Ağustos 2024 (Yayımı takip eden 20. gün).
  * Genel Uygulama: 2 Ağustos 2026.
  * Aşamalı Uygulama:
    * Bölüm I & II (Genel Hükümler ve Yasaklı Uygulamalar): 2 Şubat 2025 (Madde 5(1)(ba), (bb) hariç - 2 Aralık 2026).
    * Bölüm III Kısım 4, Bölüm V, VII, XII, Madde 78: 2 Ağustos 2025.
    * Bölüm III Kısım 1-3 (Ek III Yüksek Risk): 2 Aralık 2027.
    * Bölüm III Kısım 1-3 (Ek I Yüksek Risk Ürün Güvenliği): 2 Ağustos 2028.
    * Madde 102-110: 27 Temmuz 2026.
* **Kapsam İstisnaları**: Milli güvenlik, askeri/savunma amaçlı YZ kullanımı, saf bilimsel R&D, pazara sunulma öncesi R&D testleri (gerçek dünya koşullarında testler hariç), kişisel mesleki olmayan kullanım, serbest ve açık kaynak kodlu lisanslı modeller (yüksek riskli veya yasaklı olmadıkça) [Art. 2(3), 2(6), 2(8), 2(10), 2(12)].

## S2 — DEFINITIONS / SCOPE / ACTORS
* **Aktörler**: Provider [Art. 3(3)], Deployer [Art. 3(4)], Authorised Representative [Art. 3(5)], Importer [Art. 3(6)], Distributor [Art. 3(7)], Operator [Art. 3(8)], Downstream Provider [Art. 3(68)], Affected Person [Art. 2(1)(g)], National Competent Authority [Art. 3(48)], AI Office [Art. 3(47)].
* **Kapsamdaki Varlıklar**: AI System [Art. 3(1)], General-Purpose AI Model (GPAI) [Art. 3(63)], High-Risk AI System [Art. 6, Annex I, Annex III], Prohibited AI Practices [Art. 5], Deep Fake [Art. 3(60)], Emotion Recognition System [Art. 3(29)], Biometric Categorisation System [Art. 3(40)].
* **Eşikler**: GPAI modellerinde sistemik risk eşiği kumülatif eğitim hesaplama gücü > $10^{25}$ FLOP [Art. 51(2)].

## S3 — RIGHTS / DUTIES / SAFEGUARDS
* **Haklar**: Açıklama alma hakkı [Art. 86], Şikâyet etme hakkı [Art. 85], İhbarcı koruması [Art. 87].
* **Önemli Görevler**: Risk yönetim sistemi [Art. 9], Veri yönetişimi [Art. 10], Teknik dokümantasyon [Art. 11, Annex IV], Otomatik loglama [Art. 12, 19, 26(6)], Şeffaflık [Art. 13, 50], İnsan gözetimi [Art. 14], Doğruluk, dayanıklılık ve siber güvenlik [Art. 15], Kalite yönetim sistemi [Art. 17], FRIA etki değerlendirmesi [Art. 27], GPAI yükümlülükleri [Art. 53, 55].

## S4 — HSA THREAT RELEVANCE
* **THR-001 (Autonomous Impairment / Subliminal Manipulation)**: `DIRECT_EXPLICIT` [Art. 5(1)(a)]
* **THR-002 (Vulnerability Exploitation)**: `DIRECT_EXPLICIT` [Art. 5(1)(b)]
* **THR-003 (Biometric Mass Surveillance & Untargeted Scraping)**: `DIRECT_EXPLICIT` [Art. 5(1)(e), 5(1)(h)]
* **THR-004 (Social Scoring & Discrimination)**: `DIRECT_EXPLICIT` [Art. 5(1)(c)]
* **THR-005 (Emotion Recognition in Workplace/Education)**: `DIRECT_EXPLICIT` [Art. 5(1)(f)]
* **THR-006 (Biometric Categorisation on Sensitive Attributes)**: `DIRECT_EXPLICIT` [Art. 5(1)(g)]
* **THR-007 (Deepfake / Synthetic Content Impersonation & NCII)**: `DIRECT_EXPLICIT` [Art. 5(1)(ba), Art. 50(2), (4)]
* **THR-008 (Adversarial Attacks & Data/Model Poisoning)**: `DIRECT_EXPLICIT` [Art. 15(5), Art. 55(1)(d)]
* **THR-009 (Feedback Loops & Automated Bias Propagation)**: `DIRECT_EXPLICIT` [Art. 15(4)]
* **THR-010 (Automation Bias & Loss of Human Control)**: `DIRECT_EXPLICIT` [Art. 14(4)(b), (e)]
* **THR-011 (Critical Infrastructure Disruption)**: `DIRECT_EXPLICIT` [Annex III(2), Art. 3(49)(b)]
* **THR-012 (GPAI Systemic Risks & High-Impact Cascading Failures)**: `DIRECT_EXPLICIT` [Art. 3(65), Art. 51, Art. 55]
* **THR-013 (Agentic AI & Emerging Autonomous Behaviours)**: `ANALOGICAL` [Annex XIV]

## S5 — EVIDENCE / ACCOUNTABILITY
* **Zorunlu Uyum Kanıtları**: Teknik Dokümantasyon [Art. 11, Annex IV], AB Uygunluk Beyanı [Art. 47, Annex V], Otomatik Kayıt Günlükleri (en az 6 ay) [Art. 12, 19, 26(6)], Temel Haklar Etki Değerlendirmesi (FRIA) Raporu [Art. 27], AB Veritabanı Kaydı [Art. 49], Kalite Yönetim Sistemi Dokümanları [Art. 17], Ciddi Olay Bildirim Raporları [Art. 73], GPAI Telif Hakkı ve Eğitim Özeti [Art. 53(1)(c)-(d)].
* **Soruşturma / Araştırma Kanıtları**: Veri Seti Erişim ve API Kayıtları [Art. 74(12)], Kaynak Kodu [Art. 74(13)], Kırmızı Takım (Red-Teaming) Test Raporları [Art. 55(1)(a)], Bilgilendirilmiş Rıza Belgeleri [Art. 60(4)(i), 61], Regulatory Sandbox Çıkış Raporu [Art. 57(7)].

## S6 — UNKNOWN / CONFLICT
* **KNOWN**: Risk temelli derecelendirme mimarisi, yüksek riskli YZ yükümlülükleri, GPAI kuralları, idari para cezası rejimleri (35M EUR / %7 ciro; 15M EUR / %3 ciro; 7.5M EUR / %1 ciro).
* **UNKNOWN**: Uyumlaştırılmış standartların henüz tamamlanmamış teknik standart detayları; Madde 6(5) uygulama rehberinin nihai detayları.
* **CONFLICT**: İç pazar harmonizasyonu ile Üye Devletlerin kamu düzeni/kolluk acil durum istisnaları arasındaki yetki dengesi.
* **CURRENTNESS_LIMIT**: 27 Temmuz 2026 konsolide metnidir.
* **TRANSLATION_LIMIT**: İngilizce konsolide resmi metindir.
* **SCOPE_LIMIT**: Sadece AB pazarına sunulan veya çıktıları AB'de kullanılan YZ sistemlerini kapsar; askeri/savunma sistemleri hariçtir.
* **EVIDENCE_GAP**: Ticari kapalı GPAI modellerinde fikri mülkiyet gerekçesiyle tam şeffaflık denetimi zorlukları.

## S7 — ENGINEERING RELEVANCE
* **CONTROL_CANDIDATE**: Otomatik loglama motoru (en az 6 ay saklama) [Art. 12, 19]; İnsan Gözetim Durdurma Düğmesi (Stop Button) [Art. 14(4)(e)]; Dijital Filigranlama & C2PA Metadoküman Modülü [Art. 50(2)]; Veri Önyargısı Temizleme Hattı [Art. 10(2)(f)-(g)].
* **TEST_CANDIDATE**: Hasmane Kırmızı Takım (Jailbreak / Data Poisoning) Test Seti [Art. 15(5), Art. 55(1)(a)]; Demografik Eşitlik & Yanlılık Test Benchmarkları [Art. 10(3), 15(3)]; Otomasyon Önyargısı İnsan-Makine Etkileşim Testi [Art. 14(4)(b)].
* **EVIDENCE_ARTIFACT**: `technical_documentation_vX.json`, `data_governance_provenance_log.csv`, `fria_assessment_report.pdf`, `eu_declaration_of_conformity.pdf`.

---
PRIMARY_SOURCE_RECHECK_REQUIRED: FALSE
DESTINATION_REPO: AI-LAWS / EU-COMPLIANCE-FRAMEWORK
REVIEW_OWNER: Legal & AI Safety Engineering Working Group
PROMOTION_STATE: FINDING_CANDIDATE
