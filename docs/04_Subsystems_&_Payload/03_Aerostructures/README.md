# 🏗️ Yapısal Tasarım (Aerostructures) & Aerodinamik

![Banner](../../../assets/banner.png)

## 1. Aerodinamik Analiz

### 1.1. Stabilite Merkezi (Center of Pressure - CP)
CP yerini hesaplamak için **Barrowman Denklemleri** kullanılır.
$$ X_{cp} = \frac{ \sum (C_{N\alpha})_i X_i }{ \sum (C_{N\alpha})_i } $$
*   **Önemli:** CP roket uçtukça (Hücum açısı arttıkça) öne doğru kayabilir. OpenRocket simülasyonlarında "CP Shift"e dikkat edin.
*   **Mach Etkisi:** Ses hızına (Mach 1) yaklaştıkça CP ciddi şekilde değişir. Transonic bölgede stabilite kaybı yaşamamak için marjini **2.0 calibre** civarında tutun.

### 1.2. Fin Flutter (Kanatçık Çırpınması)
Kanatçıkların kendi doğal frekansı ile hava akımının rezonansa girmesi. **Yıkıcıdır.**
*   **Hesap:** NACA Technical Report 685 (Theordorsen Teorisi).
*   **G etkili parametreler:**
    *   **Shear Modulus (G):** Malzemenin kayma modülü. Karbon fiberde bu değer yüksektir (~3-5 GPa), fiberglasta düşüktür.
    *   **Kanat Açıklığı (Span):** Kısa kanatçıklar daha rijit olur.
    *   **Kalınlık (Thickness):** En kritik faktördür. $T^3$ ile orantılı sertlik artışı sağlar.

---

## 2. Kompozit Malzeme Üretimi

### 2.1. Hand Lay-up vs Vacuum Infusion
*   **Hand Lay-up:** Elle reçine sürme. Ucuz ama ağır. Reçine/Fiber oranı %60/%40 gibidir (Kötü).
*   **Vacuum Infusion:** Vakum torbalama. Fazla reçineyi emer. Reçine/Fiber oranı %30/%70 (Mükemmel mukavemet).
*   **Pre-preg:** Reçinesi önceden emdirilmiş kumaş. Fırınlama (Curing) gerektirir. IREC için en profesyonel yöntemdir.

### 2.2. Gövde Boruları (Airframe)
*   **Fiberglass Filament Winding:** Makine ile sarım. En optimize üretimdir.
*   **Blue Tube 2.0:** Vulkanize selüloz. Plastik gibi davranır, kırılmaz (yamulur). RF geçirgendir.
*   **Alüminyum 6061-T6:** Motor bloğu (thrust plate) ve aviyonik coupler (bağlantı) parçaları için standarttır. 7075-T6 (Uçak alüminyumu) daha hafiftir ama daha pahalıdır.

---

## 3. Yapısal Entegrasyon
### 3.1. Boat-tail (Kuyruk Koni)
Roket motorunun arkasına takılan daralan koni.
*   **Amaç:** Base Drag (Taban sürüklemesini) azaltır. %10-15 irtifa kazancı sağlayabilir.
*   **Dezavantaj:** Motor ateşlemesinde ısınır. Isıya dayanıklı epoksi kullanılmalıdır.

### 3.2. Rail Buttons (Rampa Butonları)
Roketi rampada tutan parçalar.
*   **Tasarım:** Genellikle Delrin veya Teflon malzemeden yapılır (Sürtünme az).
*   **ADAMANT:** Rail butonlarını ana gövdeye (Load bearing bulkheads) vidalayın. Sadece ince fiberglass gövdeye yapıştırmayın, kalkışta (10G) koparlar.
