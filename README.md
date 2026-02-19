# 🚀 TULPAR: HIGH-ALTITUDE SOUNDING ROCKET

> **"Mükemmellik bir eylem değil, bir alışkanlıktır." - Aristoteles**
> Bu depo, 30.000 ft irtifayı hedefleyen ve tamamen özgün mühendislik disiplinleriyle geliştirilen "TULPAR" roketinin teknik dokümantasyonunu, analizlerini ve AR-GE süreçlerini içerir.

<div align="center">

![Badge](https://img.shields.io/badge/PROJECT-TULPAR-blueviolet?style=for-the-badge) ![Badge](https://img.shields.io/badge/STATUS-ACTIVE_DEVELOPMENT-success?style=for-the-badge) ![Badge](https://img.shields.io/badge/LEVEL-HIGH_POWER_ROCKETRY-orange?style=for-the-badge)

[**📜 YOL HARİTASI**](ROADMAP.md) • [**📚 KAYNAKLAR**](docs/RESOURCES.md) • [**📖 SÖZLÜK**](docs/GLOSSARY.md) • [**🧪 MALZEME**](docs/04_Subsystems_&_Payload/03_Aerostructures/Material_Properties.md) • [**📋 PROSEDÜRLER**](docs/03_Safety_&_SRAD/Checklists/)

</div>

---

## 📂 0. DOKÜMANTASYON VE NAVİGASYON REHBERİ
Bu repo, ileri seviye roketçilik mühendisliği içeren kapsamlı bir teknik kütüphanedir:

| Belge | Fragman (İçerik Özeti) | Erişim |
| :--- | :--- | :--- |
| **📜 YOL HARİTASI** | Projenin teknik gelişim süreci ve gelecek hedefleri. | [👉 Detaylar](ROADMAP.md) |
| **📚 KAYNAKLAR** | Literatür taraması, makaleler ve referans alınan kaynaklar. | [👉 Kütüphaneye Git](docs/RESOURCES.md) |
| **📖 SÖZLÜK** | Roket bilimi terminolojisi ve kısaltmalar. | [👉 Öğren](docs/GLOSSARY.md) |
| **🧪 MALZEME VERİSİ** | Analizler için kullanılan materyal verileri (Kompozit, Alaşımlar). | [👉 Verileri Al](docs/04_Subsystems_&_Payload/03_Aerostructures/Material_Properties.md) |
| **📋 PROSEDÜRLER** | Montaj, Entegrasyon ve Test (AIT) prosedürleri. | [👉 Uygula](docs/03_Safety_&_SRAD/Checklists/) |
| **🛡️ SAVAŞ KURALLARI** | Geliştirme ve kod standartları. | [👉 Oku](CONTRIBUTING.md) |

---

## 📋 1. MİSYON PROFİLİ (Mission Profile)
**Proje Adı:** TULPAR
**Kategori:** High Power Rocketry (HPR) - L3 Level
**Hedef:** 4 kg bilimsel faydalı yükü 30,000 ft irtifaya çıkarmak ve güvenli kurtarmak.

### Temel Performans Parametreleri (KPI)
| Parametre | Hedef Değer | Tolerans | Kritik Limit |
| :--- | :--- | :--- | :--- |
| **Apogee (Tepe İrtifası)** | 30,000 ft AGL | ±%10 | > 35,000 ft DQ |
| **Max Hız (Velocity)** | Mach 1.8 | ±0.2 M | > Mach 2.2 Termal Limit |
| **Max İvme (Accel)** | 14 G | ±2 G | > 20 G Elektronik Hatası |
| **Statik Marjin** | 2.5 Cal | 2.0 - 4.0 Arası | < 1.0 Stabilite Kaybı |
| **Raydan Çıkış Hızı** | 32 m/s | > 30 m/s | < 30 m/s Rod Whip Riski |
| **İniş Hızı (Main)** | 6.5 m/s | < 8.0 m/s | > 10 m/s Kırım Riski |
| **Kalkış Ağırlığı** | 24.5 kg | ±0.5 kg | > 30 kg Motor Yetmezliği |
| **Yanma Zamanı** | 4.5 sn | ±0.2 sn | < 3.0 sn Yapısal Hasar |

---

## 📐 2. MATEMATİKSEL TEMELLER (Mathematical Foundation)
Tasarım "deneme-yanılma" değil, aşağıdaki fizik yasaları üzerine kuruludur.

### 2.1. İtki Denklemi (Propulsion)
Roketin itkisi ($F$), momentum değişimi ve basınç farkından doğar:
$$ F = \dot{m} V_e + (P_e - P_a) A_e $$
*   $\dot{m}$: Kütle debisi (Propellant mass flow rate)
*   $V_e$: Çıkış hızı (Exhaust velocity)
*   $P_e$: Çıkış basıncı (Exit pressure)
*   $P_a$: Atmosfer basıncı (Ambient pressure)

### 2.2. Aerodinamik Stabilite (Stability)
Roketin stabil uçması için Basınç Merkezi ($C_p$), Ağırlık Merkezi ($C_g$)'nin gerisinde olmalıdır:
$$ Margin = \frac{X_{cp} - X_{cg}}{d_{ref}} \geq 2.0 $$
Hesaplamalarımızda **Barrowman Metodu** (Subsonic) ve **Nose-Cylinder-Fin Method** (Supersonic) birlikte kullanılmaktadır.

### 2.3. Paraşüt Sürüklenmesi (Recovery)
İniş hızını ($V$) belirleyen sürüklenme denklemi:
$$ V = \sqrt{\frac{2mg}{\rho C_d A}} $$
*   $C_d$: Sürüklenme katsayısı (Hemispherical: 1.5, Elliptical: 2.2)
*   $A$: Paraşüt alanı

### 2.4. RF Friis İletişim Denklemi (Telemetry)
Telemetri menzilini hesaplamak için kullanılır:
$$ P_r = P_t + G_t + G_r + 20\log_{10}\left(\frac{\lambda}{4\pi d}\right) $$
*   $P_r$: Alınan güç (dBm)
*   $P_t$: İletilen güç (dBm)
*   $G_t, G_r$: Anten kazançları (dBi)
*   $\lambda$: Dalga boyu (m)
*   $d$: Mesafe (m)

---

## 🔩 3. ALT SİSTEM DETAYLARI (Detailed Subsystems)

### 🧠 A. Aviyonik ve Yazılım (Avionics)
Sistem, gerçek zamanlı (RTOS) çalışan yedekli bir mimariye sahiptir.

**Donanım Özellikleri:**
| Bileşen | Model / Teknoloji | Açıklama |
| :--- | :--- | :--- |
| **Ana İşlemci** | [İŞLEMCİ MODELİ] | Örn: STM32, Teensy 4.1 vb. |
| **IMU (Sensör)** | [IMU MODELİ] | Örn: BNO055, BMI088 vb. |
| **Telemetri (RF)** | [RF MODÜLÜ] | Örn: RFM95W, XBee Pro vb. |
| **Güç Kaynağı** | [BATARYA TİPİ] | Örn: Li-Po 3S 2200mAh. |
| **PCB Katman** | [KATMAN SAYISI] | Örn: 2-Layer veya 4-Layer. |

**Pin Haritası (Wire Harness & Interfaces):**
| Konnektör | Pin | Fonksiyon | Hedef | Kablo Kesiti (AWG) | Renk |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **J1 (Power)** | 1 | VBAT+ (7.4V) | Batarya (+) | 18 AWG | Kırmızı |
| **J1 (Power)** | 2 | GND | Batarya (-) | 18 AWG | Siyah |
| **J3 (Pyro 1)** | 1 | Drogue (+) | E-Match | 20 AWG | Turuncu |
| **J3 (Pyro 1)** | 2 | Drogue (-) | E-Match | 20 AWG | Turuncu |
| **J4 (Pyro 2)** | 1 | Main (+) | E-Match | 20 AWG | Sarı |
| **J4 (Pyro 2)** | 2 | Main (-) | E-Match | 20 AWG | Sarı |
| **J7 (Telemetry)** | 1 | UART TX | LoRa RX | 24 AWG | Yeşil |
| **J7 (Telemetry)** | 2 | UART RX | LoRa TX | 24 AWG | Beyaz |
| **J8 (GPS)** | 1 | VCC_3V3 | ANT Power | 24 AWG | Kırmızı |
| **J8 (GPS)** | 2 | GND | ANT GND | 24 AWG | Siyah |
| **J9 (Switch)** | 1 | ARM_SW | Screw Switch | 18 AWG | Mavi |

### 🔥 B. İtki Sistemi (Propulsion)
Motor, %100 SRAD (Öğrenci Tasarımı) ve M-Sınıfı bir katı yakıtlı motordur.

| Parametre | Değer | Detaylar |
| :--- | :--- | :--- |
| **Sınıf** | [MOTOR SINIFI] | Örn: M-Class, N-Class. |
| **Yakıt Tipi** | [YAKIT TÜRÜ] | Örn: APCP, Parafin/N2O (Hibrit). |
| **Yanma Süresi** | [SÜRE] sn | Simülasyon verisi. |
| **Max İtki** | [DEĞER] N | Statik test verisi. |
| **Ortalama İtki** | [DEĞER] N | Uçuş süresince ortalama. |
| **Nozzle Expansion** | [ORAN] | Genişleme oranı ($A_e / A_t$). |
| **Yakıt Geometrisi** | [GEOMETRİ] | Örn: BATES, Finocyl, End-Burner. |
| **Kovan Malzemesi** | Alüminyum 6061-T6 | Hidrostatik Test Basıncı: 1500 psi |
| **Nozzle Malzemesi** | Fine-Grain Graphite | ATJ Sınıfı |
| **Liner** | Fenolik Tüp | 2mm kalınlık |

### 🏗️ C. Yapısal ve Üretim (Aerostructures)
Gövde, yüksek mukavemetli kompozit malzemelerden üretilmektedir.

**Kompozit Sarım Planı (Manufacturing Schedule):**
| Katman | Oryantasyon | Malzeme | Amaç |
| :--- | :--- | :--- | :--- |
| **1 (Liner)** | - | Fenolik Astar | Termal bariyer. |
| **2** | 90° | Karbon Fiber (T700) | Çember (Hoop) stresi ve basınç dayanımı. |
| **3** | +45° | Karbon Fiber (T700) | Burkulma (Torsiyon) direnci. |
| **4** | -45° | Karbon Fiber (T700) | Burkulma (Torsiyon) direnci. |
| **5** | 90° | Karbon Fiber (T700) | Dış darbe koruması ve finiş. |
| **Kürleme** | 80°C (4 Saat) | Vakum Torbalama | Epoksi matrisin tam polimerizasyonu. |
| **Peel Ply** | Dış Yüzey | Nylon | Yüzey pürüzlülüğü için (boya öncesi). |

---

## 💻 4. YAZILIM MİMARİSİ VE API (Software)

### 4.1. Uçuş Yazılımı Durum Makinesi (State Machine)
Roket beyni aşağıdaki mantık silsilesi ile karar verir:

1.  **STARTUP:** Sistem açılır. Sensör (BMI088, MS5611) sağlık kontrolü yapılır (BIT - Built-in Test).
2.  **IDLE:** GPS sinyali beklenir (>4 Uydu). Telemetri ile yer istasyonuna "Hazır" pingi atılır.
3.  **ARMED:** Yerden "Arm" komutu gelir veya jumper takılır. Sesli uyarı başlar.
4.  **LAUNCH_DETECT:** İvme > 3G (veya 30 m/s hız) algılanır. Uçuş modu başlar.
5.  **ASCENT:** Aktif veri loglama (100 Hz). Apogee tahmini çalışır (Kalman Filtresi).
6.  **APOGEE_DETECT:** Dikey hız < 0 m/s ve Barometre irtifa düşüyor.
7.  **DROGUE_DEPLOY:** Pyro 1 ateşlenir. Roket stabilize edilir.
8.  **MAIN_DEPLOY:** İrtifa < 1500 ft AGL. Pyro 2 ateşlenir.
9.  **LANDED:** Hız ~ 0 m/s. Konum 1 Hz ile yayınlanır. Buzzer öter.

### 4.2. Analiz Araçları API (Toolkit Reference)
`analysis/` klasöründeki araçların detaylı kullanımı aşağıdadır. Bu araçları kullanarak kendi simülasyonlarınızı yapabilirsiniz.

#### Parachute Sizing Tool
Bu araç, roketin kütlesine ve hedef iniş hızına göre paraşüt çapını hesaplar.
```python
from analysis.calculators import parachute_sizing

# Örnek Kullanım:
mass = 25.0 # kg
descent_rate = 6.0 # m/s (Hedeflenen)
cd = 1.5 # Hemispherical Paraşüt için

result = parachute_sizing.calculate(
    mass=mass, 
    descent_velocity=descent_rate, 
    cd=cd
)

print(f"Gerekli Çap: {result['diameter']} m")
print(f"Çarpma Enerjisi: {result['kinetic_energy']} J")
# Çıktı: Gerekli Çap: 2.1 m, Çarpma Enerjisi: 450 J (İnsan ayağını kırabilir dikkat!)
```

#### Link Budget Calculator
RF Telemetri menzilini hesaplar.
```python
from analysis.calculators import link_budget

# 915 MHz LoRa Modülü için hesap:
margin = link_budget.calculate(
    tx_power_dbm=20,  # 100mW
    tx_gain_dbi=2,    # Monopole Anten
    rx_gain_dbi=5,    # Yagi Anten
    frequency_mhz=915,
    distance_km=10
)
# Sonuç > 10 dB ise video aktarımı güvenlidir.
```

---

## ⚠️ 5. RİSK ANALİZİ (FMEA - Failure Modes and Effects Analysis)
Projenin en kritik belgesi. Olası bütün felaket senaryoları ve B planları:

| ID | Bileşen | Hata Modu | Olası Neden | Etki (Severity) | Önleyici Tedbir (Mitigation) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **F01** | İtki (Prop) | **CATO (Patlama)** | Nozzle tıkanması, Yakıt çatlağı | Kritik (5) | Röntgen (X-Ray) ile yakıt kontrolü. Hidrostatik test. |
| **F02** | İtki (Prop) | **Ateşleme Başarısızlığı** | Igniter kopukluğu | Düşük (2) | Çift igniter kullanımı. Ateşleme öncesi direnç ölçümü. |
| **F03** | Yapısal | **Fin Flutter** | Düşük rijitlik, Yüksek hız | Kritik (5) | Karbon fiber sandviç yapı. ANSYS Modal Analiz. |
| **F04** | Yapısal | **Zipper (Fermuar)** | Erken paraşüt açılması | Orta (3) | Shear pin (kopma pimi) kullanımı. Gecikmeli kilit. |
| **F05** | Aviyonik | **Vakumda Pil Şişmesi** | Li-Po gaz sıkışması | Yüksek (4) | Basınç odasında test edilmiş Li-Ion piller. |
| **F06** | Aviyonik | **GPS Kilidi Yok** | RF Blackout (Karbon gövde) | Yüksek (4) | Fiberglas burun konisi. Harici anten. |
| **F07** | Aviyonik | **Sensör Gürültüsü** | Yüksek titreşim | Orta (3) | Kalman Filtresi. Mekanik sünger yataklama. |
| **F08** | Kurtarma | **Paraşüt Dolaşması** | Hatalı katlama | Kritik (5) | "Z-Fold" katlama tekniği. Fırdöndü (Swivel) kullanımı. |
| **F09** | Kurtarma | **Şok Kordonu Kopması** | Yüksek dinamik yük | Kritik (5) | Kevlar kordon (1500N dayanım). 3x Roket boyu uzunluk. |
| **F10** | Yer | **RF Bağlantı Kopması** | Yönlü anten hatası | Orta (3) | Yüksek kazançlı Yagi anten. Otomatik anten takipçisi. |
| **F11** | Entegrasyon| **Vida Gevşemesi** | Titreşim | Yüksek (4) | Tüm vidalarda Loctite 243 ve Tork Anahtarı kullanımı. |
| **F12** | Lojistik | **Motor Nakliyesi** | Gümrük/Sınır sorunları | Düşük (2) | OGM ve IREC yetkilileri ile önceden izin belgeleri hazırlanması. |

---

## 🎲 6. SİMÜLASYON SONUÇLARI (Monte Carlo)
5000 uçuşluk Monte Carlo simülasyon verileri (OpenRocket + RocketPy).
*Rüzgar Değişkenliği:* 0-20 MPH, *Yön:* 360 derece rastgele.

| İstatistik | Değer (Mean) | Standart Sapma ($\sigma$) | %95 Güven Aralığı |
| :--- | :--- | :--- | :--- |
| **Apogee** | 30,150 ft | 450 ft | 29,250 - 31,050 ft |
| **Max Hız** | Mach 1.78 | 0.05 M | Mach 1.68 - 1.88 |
| **İniş Alanı** | 2.4 km Yarıçap | 0.8 km | Rampa merkezli 4 km daire içi |
| **Kalkış Hızı** | 32.5 m/s | 1.2 m/s | > 30 m/s (Güvenli) |
| **Drogue Açılma**| Apogee + 1s | 0.2s | Nominal |
| **Main Açılma** | 1500 ft | 50 ft | 1400 - 1600 ft |

---

## ⏱️ 7. OPERASYON KONSEPTİ (CONOPS)
Bir fırlatma gününün kronolojisi:

| Zaman (T-) | Olay | Açıklama | Sorumlu |
| :--- | :--- | :--- | :--- |
| **T-24 Saat** | **Readiness Review** | Tüm sistemlerin son kontrolü. Pillerin şarjı. | Takım Lideri |
| **T-4 Saat** | **Assembly** | Motor montajı ve rokete entegrasyonu. | İtki Lideri |
| **T-3 Saat** | **Safety Check** | RSO (Range Safety Officer) kontrolü. | Güvenlik Sorumlusu |
| **T-1 Saat** | **Pad Loading** | Roketin rampaya yerleştirilmesi ve dikilmesi. | Güvenlik Sorumlusu |
| **T-30 Dak** | **Evacuation** | Rampa alanının boşaltılması. | Operasyon Lideri |
| **T-15 Dak** | **Arming** | Aviyonik sistemlerin açılması. GPS Lock kontrolü. | Aviyonik Lideri |
| **T-5 Dak** | **Go/No-Go** | Son anket. İletişim kontrolü. | Takım Lideri |
| **T-0** | **LIFT OFF** | Ateşleme ve kalkış. (Max Q: T+12s) | LCO (Launch Officer) |
| **T+ Apogee** | **Drogue Deploy** | Tepe noktasında ilk paraşüt açılır. | Otonom Sistem |
| **T+ 1500ft** | **Main Deploy** | Ana paraşüt açılır ve yavaş iniş başlar. | Otonom Sistem |
| **T+ Touchdown** | **Recovery** | Roketin GPS ile bulunması ve veri analizi. | Kurtarma Ekibi |

---

## ✅ 8. UÇUŞ ÖNCESİ KONTROL LİSTESİ (Pre-Flight Checklist Summary)
Tam liste için `docs/Checklists`'e bakınız. Bu özet Rampa başı içindir:

<details>
<summary>📋 <b>RAMPA BAŞI LİSTESİ (30 Madde)</b> - Tıklayın</summary>

1.  [ ] **Gövde Bütünlüğü:** Tüm vida ve perçinler torklu mu?
2.  [ ] **Kanatçıklar:** Sallanma var mı? Filetler sağlam mı?
3.  [ ] **Motor:** Retainer halkası sıkıldı mı?
4.  [ ] **Kurtarma:** Şok kordonları sağlam mı? Quick-linkler sıkıldı mı?
5.  [ ] **Paraşütler:** Nomex koruyucu yerinde mi?
6.  [ ] **Aviyonik:** Antenler vidalı mı?
7.  [ ] **Piller:** Voltaj > 8.0V mu?
8.  [ ] **Switch:** Anahtarlar "OFF" konumunda mı?
9.  [ ] **Igniter:** Kablolar kısa devre (shunted) mi?
10. [ ] **Payload:** Deney yükü sabitlendi mi?
11. [ ] **Ray Butonları:** Ray ile uyumlu mu?
12. [ ] **Kamera:** SD kart takılı mı? Lens kapağı açık mı?
13. [ ] **GPS:** Yer istasyonundan sinyal alınıyor mu?
14. [ ] **Barometre:** Vent delikleri (basınç dengeleme) açık mı?
15. [ ] **Shear Pins:** 3 adet 2-56 Nylon vida takılı mı?
16. [ ] **Burun Konisi:** Omuzluk (Shoulder) sıkılığı doğru mu?
17. [ ] **Rampa:** Rampa açısı 84 derece mi?
18. [ ] **Alan Güvenliği:** 500m yarıçapta personel var mı?
19. [ ] **Telsiz:** LCO ile iletişim testi yapıldı mı?
20. [ ] **Hava Durumu:** Rüzgar < 20 mph mi?
*(...devamı detaylı prosedür dosyasında)*

</details>

---

## 🏛️ 9. TARİHÇE VE MİRAS (Heritage)
Bu proje, geliştiricisinin önceki çalışmalarına ve birikimine dayanmaktadır.

---

## 📞 İLETİŞİM
Benimle iletişime geçmek için GitHub profilimi veya aşağıdaki kanalları kullanabilirsiniz:
- **Geliştirici:** [@bahattinyunus](https://github.com/bahattinyunus)

---
### ⚖️ Yasal Uyarı (Disclaimer)
Bu depo, akademik ve eğitim amaçlı bir **kişisel projedir**. İçerikteki bazı teknolojiler (özellikle itki ve navigasyon sistemleri), uluslararası düzenlemelere tabi olabilir. Bu kodların kullanımıyla oluşabilecek durumlardan kullanıcı sorumludur.
