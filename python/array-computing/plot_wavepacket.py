import math
import matplotlib.pyplot as plt

def wavepacket(x, t, alpha, f_param, k, omega):
    return math.exp(-(alpha * x - f_param * t) ** 2) * math.sin(k * x - omega * t)

def main():
    t0 = 0.0
    f0 = 3.0
    k = 3.0 * math.pi
    omega = 3.0 * math.pi
    alphas = [0.5, 1.0, 2.0]
    x_min, x_max = -4.0, 4.0
    n_points = 400
    dx = (x_max - x_min) / (n_points - 1)
    x_values = [x_min + i * dx for i in range(n_points)]
    plt.figure()
    for alpha in alphas:
        y_values = [wavepacket(x, t0, alpha, f0, k, omega) for x in x_values]
        plt.plot(x_values, y_values, label=f"α = {alpha}")

    plt.xlabel("x")
    plt.ylabel("f(x, t=0)")
    plt.title("Wave Packet at t = 0 for Different α")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()