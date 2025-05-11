import math
import matplotlib.pyplot as plt

def gaussian(x):
    return (1.0 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x * x)


def main():
    a, b = -4.0, 4.0
    n = 100
    h = (b - a) / (n - 1)

    x_values = [a + i * h for i in range(n)]
    y_values = [gaussian(x) for x in x_values]

    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('g(x)')
    plt.title('Gaussian function on [-4, 4]')
    plt.show()

if __name__ == "__main__":
    main()