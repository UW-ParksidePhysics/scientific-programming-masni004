def convert_fahrenheit_to_celsius(fahrenheit):
    return (5.0 / 9) * (fahrenheit - 32)

def main():
    temp_f_str = input("Enter a temperature in Fahrenheit: ")
    try:
        temp_f = float(temp_f_str)
    except ValueError:
        print("Try again.")
        return

    temp_c = convert_fahrenheit_to_celsius(temp_f)
    print(f"{temp_f:.2f} °F is equivalent to {temp_c:.2f} °C.")
100
if __name__ == "__main__":
    main()