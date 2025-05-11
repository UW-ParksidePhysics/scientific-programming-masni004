densities = {
    "iron": 7.87,
    "air": 0.0012,
    "gasoline": 0.75,
    "ice": 0.92,
    "human_body": 1.1 ,
    "silver": 10.5,
    "platinum": 21.5
}
volume = 1000
for substance, density in densities.items():
    mass = density * volume
    print(f"{substance}: {mass:.2f} g")