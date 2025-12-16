from rocketpy import Environment, SolidMotor, Rocket, Flight

# 1. Ortam Kurulumu (New Mexico, Spaceport America)
env = Environment(
    latitude=32.990254,
    longitude=-106.974998,
    elevation=1400,
)

import datetime
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
env.set_date((tomorrow.year, tomorrow.month, tomorrow.day, 12))  # Yarın öğlen

# 2. Motor Kurulumu (Örnek: Cesaroni Pro98 - 6GXL)
# Not: Gerçek .eng dosyası gereklidir, bu temsili bir tanımlamadır.
Pro98 = SolidMotor(
    thrust_source=6000,  # Ortalama itki (N) - Temsili
    burn_time=5.0,       # Yanma süresi (s)
    grain_number=6,
    grain_density=1815,
    grain_outer_radius=0.098/2,
    grain_initial_inner_radius=0.030/2,
    grain_initial_height=0.15,
    nozzle_radius=0.025,
    throat_radius=0.015,
    interpolation_method="linear",
    coordinate_system_orientation="nozzle_to_combustion_chamber",
)

# 3. Roket Kurulumu (Gökçen-1)
gokcen = Rocket(
    radius=0.1524/2,  # 6 inç çap
    mass=25.0,        # Yakıtsız kütle (kg)
    inertia=(6.321, 6.321, 0.034),
    power_off_drag=0.45,  # Tahmini sürükleme katsayısı (Cd)
    power_on_drag=0.45,
    center_of_mass_without_motor=1.5,
    coordinate_system_orientation="tail_to_nose",
)

gokcen.add_motor(Pro98, position=-1.25)

# Paraşütler
main = gokcen.add_parachute(
    "Main",
    cd_s=10.0,
    trigger=450,  # 450m (1500ft) irtifada açılır
    sampling_rate=105,
    lag=1.5,
    noise=(0, 8.3, 0.5),
)

drogue = gokcen.add_parachute(
    "Drogue",
    cd_s=1.0,
    trigger="apogee",  # Tepe noktasında açılır
    sampling_rate=105,
    lag=1.5,
    noise=(0, 8.3, 0.5),
)

# 4. Uçuş Simülasyonu
print("🚀 Simülasyon Başlatılıyor...")
test_flight = Flight(rocket=gokcen, environment=env, rail_length=5.2, inclination=85, heading=0)

print(f"✅ Simülasyon Tamamlandı!")
print(f"Tepe Noktası (Apogee): {test_flight.apogee:.2f} m AGL")
print(f"Maksimum Hız: {test_flight.max_speed:.2f} m/s")
print(f"Uçuş Süresi: {test_flight.t_final:.2f} s")
