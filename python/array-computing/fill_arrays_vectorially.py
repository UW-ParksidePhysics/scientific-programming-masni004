import numpy as np

def gaussian(x):
    return (1.0 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

def main():
    n = 41
    a, b = -4.0, 4.0

    x_values = np.linspace(a, b, n)
    y_values = gaussian(x_values)
    print("x_values =", x_values)
    print("y_values =", y_values)

if __name__ == "__main__":
    main()