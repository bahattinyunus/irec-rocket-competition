# 🪂 Kurtarma Sistemi (Recovery) & Piroteknik

![Banner](../../../assets/banner.png)

## 1. Paraşüt Aerodinamiği
Sadece "büyük paraşüt" demek yetmez. İniş kinetik enerjisi hesaplanmalıdır.
$$ KE = \frac{1}{2} m V^2 $$
*   **Hedef:** İniş enerjisi < 75 Joule olmalı (İnsan güvenliği ve roket sağlığı için).
*   **Toroidal vs Elliptical:**
    *   **Toroidal (Halka):** Yüksek $C_d$ (~2.2). Çok stabildir, salınım yapmaz.
    *   **Flat Circular:** Basit, ucuz ama çok sallanır (Pendulum effect).

## 2. Şok Kordonu (Shock Cord)
Paraşüt açıldığında oluşan ani yükü (Snatch Force) sönümlemek zorundasınız.
*   **Malzeme:** **Kevlar** (Isıya dayanıklı, esnemez) veya **Tubular Nylon** (Çok esner, şoku emer).
*   **Uzunluk:** Gövde boyunun en az 3-4 katı olmalıdır. Kısa kordonlar, paraşüt açılınca gövdelerin birbirine çarpmasına (Zipper effect) neden olur.
*   **Bağlantı:** Quick link (Maillon) kullanın. Asla kanca (Karabina) kullanmayın, yüksek G'de açılabilirler.

## 3. Piroteknik Sistemler (Ejection)

### 3.1. Karabarut (Black Powder FFFFg)
Standart ayırma patlayıcısıdır.
*   **Hesaplama (İdeal Gaz Yasası Türevi):**
    $$ Grams = \frac{P \times V}{R \times T} $$
    *   NASA'nın basitleştirilmiş formülü pratikte daha güvenlidir.
*   **Yedekleme (Redundancy):** IREC kuralı gereği **2 adet** e-match (fünye) ve **2 ayrı** barut haznesi olmak zorundadır.
    *   **Primary Charge:** Hesaplananın %100'ü. (Apogee'de ateşlenir).
    *   **Backup Charge:** Hesaplananın %125'i. (Apogee + 1 saniye sonra ateşlenir).

### 3.2. CO2 Ejection (Alternatif)
Yüksek irtifada (30k) karabarut oksijensizlikten bazen yanmayabilir veya çok basınçlı tüplerde (vakum etkisi) yetersiz kalabilir.
*   **Sistem:** Sıkıştırılmış CO2 tüpünü mekanik bir iğne ile delerek patlatma.
*   **Avantaj:** Çok temizdir (yanık artığı bırakmaz), irtifadan bağımsızdır.
*   **Dezavantaj:** Pahalıdır ve tek kullanımlıktır.

## 4. Test Prosedürleri (Ground Testing)
*   **Ejection Test:** Roket yerde tam montajlıyken barut patlatılır.
*   **Başarı Kriteri:**
    1.  Burun konisi veya gövde ayrılmalı.
    2.  Şok kordonu tam gerilmeli.
    3.  Paraşüt dışarı çıkmalı.
    4.  shear pins (pimler) temiz bir şekilde kesilmeli.
