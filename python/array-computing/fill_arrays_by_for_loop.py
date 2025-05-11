import math

def gaussian(position):
    return (1.0 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * position ** 2)

def main():
    n = 41
    a, b = -4.0, 4.0
    h = (b - a) / (n - 1)

    x_values = []
    y_values = []

    for i in range(n):
        x = a + i * h
        x_values.append(x)
        y_values.append(gaussian(x))

    print("x_values =", x_values)
    print("y_values =", y_values)

if __name__ == "__main__":
    main()