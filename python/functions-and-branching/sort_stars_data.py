def main():
    nearby_star_data = [
        ("Alpha Centauri A",   4.3,  0.26,    1.56),
        ("Alpha Centauri B",   4.3,  0.077,   0.45),
        ("Alpha Centauri C",   4.2,  0.00001, 0.00006),
        ("Barnard's Star",     6.0,  0.0004,  0.0005),
        ("Wolf 359",           7.7,  0.000001,0.00002),
        ("BD +36° 2147",       8.2,  0.00003, 0.006),
        ("Luyten 726-8 A",     8.4,  0.000003,0.00006),
        ("Luyten 726-8 B",     8.4,  0.000002,0.00004),
        ("Sirius A",           8.6,  1.000,   23.6),
        ("Sirius B",           8.6,  0.001,   0.003),
        ("Ross 154",           9.4,  0.00002, 0.0005),
    ]

    by_distance = sorted(nearby_star_data, key=lambda star: star[1])
    by_brightness = sorted(nearby_star_data, key=lambda star: star[2])
    by_luminosity = sorted(nearby_star_data, key=lambda star: star[3])

    print("Stars sorted by distance (light years):")
    print(f"{'Star':<20} {'Distance (ly)':>12}")
    print("-" * 34)
    for name, dist, _, _ in by_distance:
        print(f"{name:<20} {dist:12.2f}")
    print()

    print("Stars sorted by apparent brightness (relative to Sirius A):")
    print(f"{'Star':<20} {'Brightness':>12}")
    print("-" * 34)
    for name, _, bright, _ in by_brightness:
        print(f"{name:<20} {bright:12.6f}")
    print()

    print("Stars sorted by luminosity (relative to Sun):")
    print(f"{'Star':<20} {'Luminosity':>12}")
    print("-" * 34)
    for name, _, _, lum in by_luminosity:
        print(f"{name:<20} {lum:12.2f}")
    print()

if __name__ == "__main__":
    main()