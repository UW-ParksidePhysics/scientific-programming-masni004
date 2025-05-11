import math

p = 1.038        # g/cm³
c = 3.7          # J/(g*K)
k = 5.4e-3       #  W/(cm*K)
Tw = 100         #  Celsius
Ty = 70          # Celsius

egg_data = {
    "small": 47,   # g
    "large": 67    # g
}

initial_temps = {
    "fridge": 4,
    "room": 20
}

def calculate_cook_time(mass, T0):
    mass = mass / 1.0
    numerator = (mass ** (2/3)) * (c * p ** (1/3))
    denominator = k * (math.pi ** 2) * ((4 * math.pi / 3) ** (2/3))
    log_argument = 0.76 * (T0 - Tw) / (Ty - Tw)
    time_seconds = (numerator / denominator) * math.log(log_argument)
    return abs(time_seconds)

for size, mass in egg_data.items():
    for temp_label, T0 in initial_temps.items():
        cook_time_sec = calculate_cook_time(mass, T0)
        cook_time_min = cook_time_sec / 60
        print(f"{size.capitalize()} egg from {temp_label} (T₀ = {T0}°C):")
        print(f"  Cook time: {cook_time_sec:.1f} seconds ({cook_time_min:.1f} minutes)\n")