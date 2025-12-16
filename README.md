# 🚀 PROXIMA GÖREVİ | Spaceport America Cup Reposu

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) ![OpenRocket](https://img.shields.io/badge/OpenRocket-Sim-blueviolet?style=for-the-badge) ![SolidWorks](https://img.shields.io/badge/SolidWorks-CAD-red?style=for-the-badge) ![Altium](https://img.shields.io/badge/Altium-PCB-yellow?style=for-the-badge)

![Banner](https://img.shields.io/badge/Görev-PROXIMA-orange?style=for-the-badge) ![Yarışma](https://img.shields.io/badge/Yarışma-Spaceport_America_Cup-blue?style=for-the-badge) ![Konum](https://img.shields.io/badge/Fırlatma_Sahası-New_Mexico_ABD-red?style=for-the-badge) ![Durum](https://img.shields.io/badge/Durum-Geliştirme_Aşamasında-green?style=for-the-badge)

## 🌌 Görev Tanımı (Mission Statement)
**KTU Gökçen Roket Takımı**, dünyanın en büyük üniversiteler arası roket mühendisliği konferansı ve yarışması olan **Spaceport America Cup**'ta yarışmak üzere yeni nesil sondaj roketleri tasarlamaktadır.

Misyonumuz, bilimsel bir faydalı yükü hedef irtifaya taşıyabilen, itki ve aviyonik alanlarında **SRAD (Öğrenci Araştırması ve Geliştirmesi)** mükemmelliğini sergileyen **yüksek performanslı bir fırlatma aracı** tasarlamak, üretmek ve fırlatmaktır.

---

## 🏆 Kutsal Kase: IREC Teknik Rapor Referansları
*"İyi sanatçılar kopyalar, büyük sanatçılar çalar." - Pablo Picasso*

Aşağıdaki raporlar, Spaceport America Cup standartlarını yakalamamız için **incelenmesi zorunlu** kaynaklardır.

### 🚀 30,000 ft (İleri Kategori)
> *Karmaşık aerodinamik, süpersonik uçuş profilleri ve çok kademeli mimariler.*
*   **[McGill Rocket Team - Stella II (2018)](https://www.mcgillrocketteam.com/)** - *Kompozit Gövde & Aviyonik*
*   **[Waterloo Rocketry - Kraken of the Sky (2022)](https://waterloorocketry.com/)** - *Hibrit Motor & SRAD Sistemler*
*   **[Waterloo Rocketry - Shark of the Sky (2019)](https://waterloorocketry.com/)** - *Yüksek İrtifa Tasarımı*

### 🛸 10,000 ft (Orta Kategori)
> *Hassas iniş, COTS (Hazır) motor ustalığı ve faydalı yük entegrasyonu.*
*   **[McGill Rocket Team - Project Blanche (2018)](https://www.mcgillrocketteam.com/)** - *COTS Entegrasyon & Kurtarma*
*   **[Texas A&M SRT - Telemachus (2024)](https://tamusrt.org/)** - *Sentetik Açıklıklı Radar (SAR) Faydalı Yükü*
*   **[Texas A&M SRT - Daedalus (2017)](https://tamusrt.org/)** - *10k Hibrit Motor Başarısı*
*   **[Waterloo Rocketry - Vidar III (2017)](https://waterloorocketry.com/)** - *SRAD Hibrit Başlangıcı*

### 🧪 Deneysel & SRAD Teknolojiler
> *Özel itki sistemleri ve yenilikçi malzemelerle sınırları zorlamak.*
*   **[Waterloo Rocketry - Unexploded Ordnance (2018)](https://waterloorocketry.com/)** - *Kismet Hibrit Motor Serisi*
*   **[Clemson University - IREC 2024 Raporu](https://cecas.clemson.edu/rocket-engineering/)** - *Süreç Yönetimi ve Mühendislik Disiplini*
*   **[Clemson University Arşivi (2022-2023)](https://cecas.clemson.edu/rocket-engineering/)**

---

## 📂 Repo Yapısı (Repository Structure)

```bash
📦 ktu-rocket-irec
 ┣ 📂 .github
 ┃ ┣ 📂 ISSUE_TEMPLATE (Hata & Özellik Bildirimleri)
 ┃ ┗ 📜 pull_request_template.md
 ┣ 📂 analysis (Simülasyonlar & Analizler)
 ┃ ┣ 📜 example_sim.py
 ┃ ┗ 📜 requirements.txt
 ┣ 📂 docs
 ┃ ┣ 📂 00_Competition_Guide (Yarışma Kuralları & Rehber)
 ┃ ┣ 📂 01_Milestones_&_Updates (PDR, CDR Sunumları)
 ┃ ┣ 📂 02_Technical_Report (Teknik Rapor Taslakları)
 ┃ ┣ 📂 03_Safety_&_SRAD (Güvenlik & Risk Analizleri)
 ┃ ┣ 📂 04_Subsystems_&_Payload (Alt Sistem Tasarımları)
 ┃ ┗ 📂 reference_reports (Örnek Rapor Arşivi)
 ┗ 📜 README.md
```
Irec teslimat takvimine tam uyumlu klasör yapısı.

---

## 🛠️ Teknoloji Yığını & Analiz Araçları

> [!TIP]
> **Önce Simülasyon:** Simüle edemediğimiz hiçbir şeyi uçurmayız.

*   **Yörünge:** [OpenRocket](https://openrocket.info/), [RocketPy](https://github.com/RocketPy-Team/RocketPy)
*   **CAD/CFD:** SolidWorks, Ansys Fluent
*   **PCB Tasarımı:** Altium Designer / KiCad
*   **Yazılım:** Python, C++ (Gömülü)

---

## 📅 Spaceport Yol Haritası

```mermaid
gantt
    title IREC 2026 Kampanya Zaman Çizelges
    dateFormat  YYYY-MM-DD
    axisFormat  %b %Y

    section Planlama
    Konsept Belirleme       :active,    des1, 2025-10-01, 30d
    PDR (Ön Tasarım)        :           des2, after des1, 45d

    section Geliştirme
    Prototip & SRAD Test    :           dev1, after des2, 90d
    CDR (Kritik Tasarım)    :           dev2, after dev1, 30d

    section Test
    Tam Entegrasyon Testi   :           tst1, after dev2, 45d
    Uçuşa Hazırlık Gözden Geçirme :     tst2, after tst1, 15d

    section Fırlatma
    Spaceport America Cup   :crit,      launch, 2026-06-15, 7d
```

## 🤝 Katkıda Bulunma
Değişiklik önerme, hata bildirme ve Pull Request gönderme yönergeleri için `CONTRIBUTING.md` dosyasına bakın. Katı bir **"Özellik Başına Dal (Branch per Feature)"** iş akışı izliyoruz.

---
*KTU Gökçen Roket Takımı tarafından ❤️ ile oluşturuldu*
