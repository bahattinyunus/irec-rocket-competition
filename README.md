<div align="center">
  <img src="assets/project_banner.png" alt="Gökçen Roket Takımı Banner" width="100%" />
  <br><br>
  <img src="assets/university_logo.png" alt="Üniversite Logosu" width="80" />
  <img src="assets/irec_logo.png" alt="IREC Logosu" width="80" />

  # 📋 Spaceport America Cup (IREC) 2026 - Proje Dokümantasyonu
  ### Karadeniz Teknik Üniversitesi - Gökçen Roket Takımı

  [![](https://img.shields.io/badge/Yarışma-IREC%202026-blue?style=for-the-badge&logo=rocket)](https://www.soundingrocket.org/)
  [![](https://img.shields.io/github/actions/workflow/status/bahattinyunus/ktu-rocket-irec/lint.yml?style=for-the-badge&label=Derleme&logo=github)](https://github.com/bahattinyunus/ktu-rocket-irec/actions)
  [![](https://img.shields.io/badge/Durum-Aktif%20Geliştirme-green?style=for-the-badge)](https://www.soundingrocket.org/)
  [![](https://img.shields.io/badge/Lisans-MIT-green?style=for-the-badge)](LICENSE)

  <br>

  **"Geleceği mühendislikle inşa ediyoruz, New Mexico çöllerinde yıldızları hedefliyoruz."**

</div>

---

## 📚 Kaynaklar ve Referanslar

| 🇹🇷 Yerel Kaynaklar | 🌍 IREC & Uluslararası Kaynaklar |
| :--- | :--- |
| • [Gökçen Geçmiş Raporlar](pass_reports/)<br>• [Teknofest Arşivi](https://teknofest.org/tr/) | • **[ESRA (Exp. Sounding Rocket Assoc.)](https://www.soundingrocket.org/)**<br>• [RocketPy](https://github.com/RocketPy-Team/RocketPy)<br>• [OpenRocket](https://github.com/openrocket/openrocket)<br>• [Nakka Rocketry](https://www.nakka-rocketry.net/)<br>• [Apogee Rockets](https://www.apogeerockets.com/) |

---

> [!IMPORTANT]
> **📢 Takım Duyurusu**
>
> 1.  **Erişim:** Katkıda bulunmak için "Collaborator" yetkisi isteyin veya Pull Request açın.
> 2.  **Rapor Analizi:** Lütfen `pass_reports` klasöründeki eski IREC teknik makalelerini inceleyin.
> 3.  **Dil:** Yarışma gereği ana raporlama dili **İngilizce**'dir, ancak bu repo içindeki çalışma notları ve kılavuzlar **Türkçe** olabilir.

---

## 🛠️ Teknoloji Yığını
<div align="center">

![OpenRocket](https://img.shields.io/badge/OpenRocket-Tasarım-blue?style=for-the-badge&logo=rocket)
![Ansys](https://img.shields.io/badge/Ansys-CFD-yellow?style=for-the-badge&logo=ansys)
![SolidWorks](https://img.shields.io/badge/SolidWorks-CAD-red?style=for-the-badge&logo=dassaultsystèmes)
![STM32](https://img.shields.io/badge/STM32-Aviyonik-green?style=for-the-badge&logo=stmicroelectronics)
![Python](https://img.shields.io/badge/Python-Scripting-blue?style=for-the-badge&logo=python)
![GitHub](https://img.shields.io/badge/GitHub-İşbirliği-181717?style=for-the-badge&logo=github)

</div>

---

## 📌 Depo Amacı
Bu repo, **KTÜ Gökçen Roket Takımı**'nın **2026 Spaceport America Cup (IREC)** katılımı için merkezi çalışma alanıdır. Tüm tasarım belgeleri, analiz raporları, uçuş simülasyonları ve aviyonik yazılımları burada barındırılır.

---

## 🚀 Spaceport America Cup (IREC) Hakkında

**Spaceport America Cup**, her yıl New Mexico, ABD'de düzenlenen dünyanın en büyük üniversiteler arası roket mühendisliği konferansı ve yarışmasıdır.

### 🏆 Kategoriler
Takımımız şu kategoriyi hedeflemektedir:
*   **Hedef İrtifa:** 10,000 ft (AGL) veya 30,000 ft (AGL)
*   **İtki Tipi:** COTS (Hazır Ticari Motor) veya SRAD (Öğrenci Araştırma ve Geliştirme)
*   **Mevcut Hedef:** **10,000 ft - COTS Katı Yakıtlı Motor** (Ön Karar)

### 📝 Zaman Çizelgesi (IREC 2026)
Yarışma, ESRA takvimine sıkı sıkıya bağlılık gerektirir:

```mermaid
timeline
    title IREC 2026 Sezonu
    2025 Ekim : Başvuru & Öneri
    2025 Aralık : 1. İlerleme Raporu (PDR)
    2026 Şubat : 2. İlerleme Raporu (CDR)
    2026 Mart : Teknik Rapor Girişi
    2026 Mayıs : Uçuş Hazırlık İncelemesi (FRR)
    2026 Haziran : SPACEPORT AMERICA CUP (Fırlatma Haftası) 🚀
```

### 🎯 Puanlama Kriterleri
*   **Proje Teknik Raporu:** 500 Puan (Tasarım doğruluğu, analiz, güvenlik).
*   **Uçuş Performansı:** 500 Puan (İrtifa doğruluğu, kurtarma başarısı, faydalı yük görevi).
*   **Bonus:** Sportiflik, Takım Ruhu, SRAD bileşenler.

---

## 📂 Dokümantasyon Yapısı (IREC Standardı)

```plaintext
├── 📂 assets              # Görseller, bannerlar, logolar
├── 📂 docs                # 🧠 Teknik Dokümantasyon
│   ├── 📂 00_admin                  # 📅 Bütçe, Takım Listesi, ESRA İletişimleri
│   ├── 📂 01_progress_updates       # 📝 PDR, CDR, Uçuş Hazırlık İncelemeleri
│   ├── 📂 02_technical_report       # 📄 Final Proje Teknik Raporu
│   ├── 📂 03_safety_and_operations  # ⚠️ Tehlike Analizi & Fırlatma Kontrol Listeleri
│   └── 📂 04_subsystems             # 🛠️ Tasarım & Analiz (İtki, Aviyonik...)
├── 📂 flight_data         # 📡 Telemetry logları & Simülasyon dosyaları (OpenRocket/RasAero)
├── 📜 CITATION.cff        # Akademik atıf
├── 📜 README.md           # Ana proje dosyası
└── 📜 LICENSE             # MIT Lisansı
```

### 📋 Önemli Belgeler
*   [🚀 Fırlatma Operasyon Kontrol Listesi](docs/03_safety_and_operations/launch_checklist.md)
*   [⚠️ Risk Değerlendirmesi](docs/03_safety_and_operations/risk_assessment.md)
*   [📄 Teknik Rapor Taslağı](docs/02_technical_report/README.md)

---

## 🤝 Katkıda Bulunma & İş Akışı
1.  **Haftalık Toplantılar:** Pazar günleri saat 20:00.
2.  **Belgeleme:** Tüm mühendislik kararları gerekçeleriyle birlikte `docs/` altında belgelenmelidir.
3.  **Birimler:** Tüm belgeler **Imperial & Metric** birimlerini (IREC gereksinimi) kullanmalıdır.

---

## 📞 İletişim
*   **Takım Kaptanı:** [İsim Soyisim] (email@ktu.edu.tr)
*   **Akademik Danışman:** [Ünvan İsim Soyisim]

<div align="center">
  <p>© 2026 Karadeniz Teknik Üniversitesi - Gökçen Roket Takımı</p>
</div>
