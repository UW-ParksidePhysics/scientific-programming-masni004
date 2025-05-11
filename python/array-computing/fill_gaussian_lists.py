import math

def gaussian(position):
    return (1.0 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * position**2)

def main():
    n = 41
    a, b = -4.0, 4.0

    h = (b - a) / (n - 1)

    positions = []
    gaussian_values = []
    for i in range(n):
        x = a + i * h
        positions.append(x)
        gaussian_values.append(gaussian(x))

    print("positions =", positions)
    print("gaussian_values =", gaussian_values)

if __name__ == "__main__":
    main()

