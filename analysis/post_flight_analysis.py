import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 🚀 POST-FLIGHT ANALYSIS TOOL
# Bu script, uçuş bilgisayarından (Black Box) alınan CSV verilerini analiz eder.

def analyze_flight_data(file_path):
    print(f"📂 Veri Yükleniyor: {file_path}")
    
    # Gerçek uçuş verisi yoksa, dummy veri oluştur
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print("⚠️ Dosya bulunamadı! Simülasyon verisi oluşturuluyor...")
        time = np.linspace(0, 100, 1000)
        altitude = 3000 * np.sin(np.pi * time / 100)  # Dummy parabola
        # Gürültü ekle (Sensör verisi asla mükemmel değildir)
        altitude += np.random.normal(0, 10, 1000)
        df = pd.DataFrame({'Time': time, 'Altitude_AGL': altitude})

    # 1. Apogee Tespiti
    max_alt = df['Altitude_AGL'].max()
    apogee_time = df.loc[df['Altitude_AGL'].idxmax(), 'Time']
    
    print(f"🏆 APOGEE DETECTED: {max_alt:.2f} ft @ T+{apogee_time:.2f}s")

    # 2. Grafik Çizimi
    plt.figure(figsize=(10, 6))
    plt.plot(df['Time'], df['Altitude_AGL'], label='Barometric Altitude', color='blue')
    plt.axvline(x=apogee_time, color='red', linestyle='--', label='Apogee')
    
    plt.title(f"Flight Profile | Max Alt: {max_alt:.0f} ft")
    plt.xlabel("Time (s)")
    plt.ylabel("Altitude AGL (ft)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    
    # Grafik kaydet
    output_img = "flight_profile.png"
    plt.savefig(output_img)
    print(f"📊 Grafik kaydedildi: {output_img}")

if __name__ == "__main__":
    # Örnek kullanım: 'flight_data.csv' dosyasını analiz et
    analyze_flight_data("flight_data.csv")
