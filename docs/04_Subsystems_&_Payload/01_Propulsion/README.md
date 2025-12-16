# 🚀 İtki Sistemi (Propulsion) Derinlemesine Teknik Rehber

![Banner](../../../assets/banner.png)

## 1. Hibrit Motor Teorisi (SRAD - Hybrid)
IREC 30k kategorisinde "Kutsal Kase" hibrit motorlardır.
*   **Yakıt (Fuel):** Genellikle **Paraffin Wax** (Mum) veya **HTPB**. Parafinin yanma hızı (regression rate) yüksektir.
*   **Oksitleyici (Oxidizer):** **Nitrous Oxide ($N_2O$)**. Kendinden basınçlıdır (Vapor Pressure @ 20°C $\approx$ 50 bar).

### 1.1. Enjektör Tasarımı (Injector)
Motorun kalbidir. $N_2O$'nun sıvı fazda yanma odasına püskürtülmesi gerekir.
*   **Discharge Coefficient ($C_d$):** Enjektör deliklerinin verimi. Genellikle 0.6 - 0.7 arası alınır.
*   **Atomizasyon:** Oksitleyici ne kadar iyi parçalanırsa yanma o kadar verimli olur. (Showerhead vs Impinging jet).

### 1.2. Yanma Kararsızlığı (Instability)
Hibrit motorların baş belasıdır. "Chugging" (Düşük frekans) ve "Screaming" (Yüksek frekans) olarak ikiye ayrılır.
*   **Önlem:** Pre-combustion chamber (Ön yanma odası) hacmini doğru ayarlamak.

---

## 2. Katı Yakıt Motorları (COTS & SRAD)

### 2.1. COTS Motor Seçimi
Cesaroni (CTI) veya Aerotech motorları standarttır.
*   **Motor Kodu Okuma:** `L2200G-P`
    *   **L:** Total Impulse sınıfı (2560-5120 Ns).
    *   **2200:** Ortalama itki (Newton).
    *   **G:** Yakıt tipi (Green / Blue vs).
*   **Seçim Kriteri:** Roketinizi 5G - 10G arası bir ivmeyle rampadan çıkarmalıdır (**Thrust-to-Weight Ratio > 5**).

### 2.2. Grain Geometrisi (SRAD)
Yanma yüzey alanı ($A_b$), itki profilini belirler.
*   **Bates Grain:** İstikrarlı, düz bir itki profili verir. (En yaygın).
*   **Star Grain (Yıldız):** Başlangıçta çok yüksek itki, sonra düşüş. Hızlı kalkış için ideal.
*   **Moonburner:** Uzun yanma süresi (Sustainer motorlar için).

---

## 3. Üretim & Test Standartları

### 3.1. Hidrostatik Test (Proof Pressure Test)
Yanma odası (Combustion Chamber) üretildikten sonra mutlaka su ile basınç testine sokulmalıdır.
*   **Yöntem:** Çalışma basıncının (MEOP) **1.5 katı** basınçla 10 dakika test edilir.
*   **Güvenlik:** Asla hava/gaz ile test yapmayın! Su sıkışmaz, patlarsa sadece ıslanırsınız. Gaz patlarsa şarapnel saçar.

### 3.2. Statik Ateşleme (Static Fire)
Uçmadan önce motoru yerde ateşlemek zorundasınız.
*   **Load Cell:** İtki verisini (Thrust Curve) kaydetmek için.
*   **Basınç Transducer:** Yanma odası basıncını ölçmek için.
*   **Güvenlik Mesafesi:** IREC kurallarına göre en az 50 metre.

---

## 4. Referans Kaynaklar
*   **Rocket Propulsion Elements (Sutton):** Bölüm 12 (Solid), Bölüm 13 (Hybrid).
*   **AspireSpace:** Hibrit motor tasarım araçları.
