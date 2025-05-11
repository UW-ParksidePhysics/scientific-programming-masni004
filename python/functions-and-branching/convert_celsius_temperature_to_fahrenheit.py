def convert_celsius_temperature_to_fahrenheit(celsius_temperature):
    return (9.0 / 5) * celsius_temperature + 32

def convert_fahrenheit_temperature_to_celsius(fahrenheit_temperature):
    return (5.0 / 9) * (fahrenheit_temperature - 32)

def main():
    test_celsius = [0.0, 21.0, 100.0]

    print(f"{'°C':>7} {'°F':>10} {'°C (round-trip)':>17}")
    print("-" * 36)

    for c in test_celsius:
        f = convert_celsius_temperature_to_fahrenheit(c)
        c_back = convert_fahrenheit_temperature_to_celsius(f)
        print(f"{c:7.2f} {f:10.2f} {c_back:17.2f}")

if __name__ == "__main__":
    main()
