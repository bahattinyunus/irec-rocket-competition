# 📂 02_Technical_Report (Teknik Rapor)

## 🏆 Kutsal Kase (Holy Grail)
Bu rapor, yarışmadaki başarımızın **%50'sini** oluşturur. Roketimiz ne kadar iyi uçarsa uçsun, bu rapor kötüyse kazanamayız.

## 📝 Bölüm Bölüm Yazım Rehberi

### 1. Abstract (Özet)
*   **Amaç:** Hakemlere 2 dakikada projenin ne olduğunu anlatmak.
*   **İçerik:** Hedef irtifa, motor tipi, takım yapısı, en önemli inovasyon.

### 2. Introduction (Giriş)
*   Takım vizyonu, tasarım felsefesi (Basitlik mi? Yüksek Teknoloji mi?).

### 3. System Architecture (Sistem Mimarisi)
*   Roketin genel şeması.
*   Neden bu çap? Neden bu uzunluk? (Trade-off analizleri).

### 4. Propulsion (İtki Sistemi)
*   **COTS:** Motor seçimi neden yapıldı? Thrust curve analizi.
*   **SRAD:** Yakıt formülü, yanma testleri, nozzle tasarımı.

### 5. Aerostructures (Yapısal)
*   Malzeme testleri (Çekme/Eğme testleri).
*   Kanatçık (Fin) flutter hızı analizi (Çok Kritik!).

### 6. Recovery (Kurtarma)
*   Paraşüt boyutlandırma hesapları.
*   Sürüklenme (Drift) analizi: Rüzgarlı havada roket nereye düşecek?
*   Ateşleme mekanizması (Black powder miktarı).

### 7. Avionics (Aviyonik)
*   Güç bütçesi (Piller ne kadar dayanır?).
*   RF Link bütçesi (Telemetri ne kadar uzağa çeker?).

### 8. Payload (Faydalı Yük)
*   Bilimsel değer.
*   Mekanik entegrasyon.

### 9. Conclusion (Sonuç)
*   Test uçuşlarından elde edilen verilerle simülasyonların karşılaştırılması.

## ⚠️ Kritik Uyarılar
*   **Grafikler:** Asla Excel varsayılan grafiği kullanmayın. Python/Matplotlib veya profesyonel araçlar kullanın.
*   **Birimler:** Hem Metric (m, kg) hem Imperial (ft, lbs) birimlerini yan yana yazın. Örn: `3048 m (10,000 ft)`.
