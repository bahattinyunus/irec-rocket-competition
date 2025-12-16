# 📟 Aviyonik & Yazılım (Avionics & Software) Bilgi Bankası

![Banner](../../../assets/banner.png)

> [!WARNING]
> **Güvenlik Kritik Sistem:** Aviyonik sistemlerdeki bir yazılım hatası, motorun rampada ateşlenmesine veya roketin balistik (paraşütsüz) düşmesine neden olabilir. Şaka değildir.

## 1. Donanım Mimarisi & PCB Tasarımı

### 1.1. Merkezi Uçuş Bilgisayarı (Flight Computer)
**SRAD (Öğrenci Yapımı)** bilgisayarlarda genellikle şu işlemci aileleri tercih edilir:
*   **STM32F4/F7/H7 Serisi:** Endüstri standardı. Yüksek işlem gücü (Floating Point Unit - FPU) sayesinde Kalman filtresi rahatlıkla çalışır.
*   **Teensy 4.1 (NXP i.MX RT1062):** 600 MHz hız. Prototipleme için mükemmel ama IREC'te "Breadboard" kullanımı yasaktır. Özel PCB şart.

### 1.2. PCB Tasarım Kuralları (Mission Critical)
Roketler titrer. Hem de çok titrer.
1.  **Dört Katmanlı PCB (4-Layer):** Sinyal bütünlüğü için *Signal - Ground - Power - Signal* yapısı zorunludur.
2.  **Vidalı Konnektörler:** Asla *Dupont* veya *Pin Header* kullanmayın. **Molex**, **JST-XH** veya vidalı klemensler (Screw Terminals) kullanın.
3.  **Tantalum Kapasitörler:** Titreşimde seramik kapasitörler çatlayabilir. Kritik güç hatlarında Tantalum veya Polimer kapasitör kullanın.
4.  **Conformal Coating:** PCB üretildikten sonra üzerine koruyucu vernik (Silikon veya Akrilik) sıkın. Nem ve metal tozundan (karbon fiber tozu iletkendir!) korur.

---

## 2. Gömülü Yazılım Mimarisi (Embedded Software)

### 2.1. RTOS mu Bare Metal mi?
IREC seviyesindeki komplex görevler için **RTOS (Real-Time Operating System)** şiddetle önerilir.
*   **Neden?** Sensör okuma (1000Hz), veri kaydı (SD Kart) ve telemetri (LoRa) işlemleri birbirini beklememelidir.
*   **Önerilenler:** FreeRTOS, ChibiOS.
*   **Task Öncelikleri:**
    1.  `CRITICAL_TASK`: Apogee algılama ve Pyro ateşleme. (En yüksek öncelik)
    2.  `SENSOR_TASK`: IMU ve Barometre okuma.
    3.  `LOGGING_TASK`: SD karta yazma.
    4.  `TELEM_TASK`: Yer istasyonuna veri gönderme.

### 2.2. Durum Makineleri (Finite State Machines - FSM)
Roketin davranışı kesinlikle bir `switch-case` yapısı (Durum Makinesi) ile yönetilmelidir.
*   `STATE_IDLE`: Rampada bekleme. (Gyro kalibrasyonu burada yapılır).
*   `STATE_ARMED`: Güvenlik pimi çekildi. Ateşleme komutu bekleniyor.
*   `STATE_ASCENT`: İvme algılandı (>3G). Veri kaydı başladı.
*   `STATE_APOGEE`: Tepe noktası. **Drogue paraşüt** ateşlemesi.
*   `STATE_DESCENT`: İniş.
*   `STATE_MAIN`: Belirli irtifada (örn. 1500ft). **Ana paraşüt** ateşlemesi.
*   `STATE_LANDED`: Hareket durdu. Buzzer ötüyor, GPS konumu yollanıyor.

### 2.3. Algoritmalar: Kalman Filtresi
Ham sensör verisi gürültülüdür. Özellikle ses hızını (Transonic) geçerken basınç sensörleri sapıtır.
*   **Lider Filtre (Predictor-Corrector):** İvmeölçer verisini entegre ederek hızı bulur, barometre verisiyle bu tahmini düzeltir.
*   **Apogee Tespiti:** Sadece "Yükseklik azaldı" demek yetmez.
    *   `if (velocity < 0 && altitude > min_altitude)` mantığı daha güvenlidir.
    *   **Timer Lockout:** Kalkıştan sonraki ilk 5-10 saniye (motor yanarken) piroteknik kanalları yazılımsal olarak kilitleyin.

---

## 3. Yer İstasyonu Yazılımı (Ground Station)

Yer kontrol yazılımı (GUI), roketin sağlığını anlık izlemelidir.
*   **Teknolojiler:** C# (WPF), Python (PyQt/PySide), veya Elektron (Web tabanlı).
*   **Kritik Veriler:**
    *   Anlık İrtifa (Grafiksel)
    *   GPS Konumu (Harita üzerinde)
    *   Pil Voltajı (Kırmızı alarm sınırı: 3.7V/hücre)
    *   RSSI (Sinyal Gücü)
*   **Link Bütçesi & Protokol:**
    *   Veri paketlerini küçük tutun (Struct packing).
    *   Örnek Paket: `[HEADER][TIMESTAMP][ALT][VEL][ACC_Z][GPS_LAT][GPS_LON][CRC]`

---

## 4. Sensör ve Bileşen Seçimi (BOM Guide)

| Bileşen | Önerilen Model | Neden? |
| :--- | :--- | :--- |
| **MCU** | STM32H743 | 480MHz, çift çekirdek, bol UART/SPI. |
| **IMU** | ISM330DHCX | Endüstriyel sınıf, yüksek vibrasyon dayanımı. |
| **Barometre** | MS5611 / DPS310 | BMP280'den çok daha hassas (10cm çözünürlük). |
| **GPS** | uBlox NEO-M9N | Yüksek irtifa limiti (COCOM limitlerine dikkat!), hızlı fix. |
| **LoRa** | RFM95W / SX1276 | 915 MHz (ABD) veya 433 MHz (Avrupa) seçeneği. |
| **Piro Sürücü** | N-Channel MOSFET | Yüksek akım (min 10A anlık) verebilmeli. Flyback diyot eklemeyi unutmayın! |

---

> [!TIP]
> **Yazılım Testi (HIL - Hardware in the Loop):**
> Yazılımınızı gerçek uçuş verisiyle test edin. Geçmiş uçuşların `CSV` dosyalarını işlemciye "sanki sensörden okuyormuş gibi" verin ve paraşütlerin doğru zamanda tetiklenip tetiklenmediğini görün.
