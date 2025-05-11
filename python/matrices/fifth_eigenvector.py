import numpy as np
import matplotlib.pyplot as plt

# Number of interior points
n = 5

# Matrix scalar multiplied with H
scalar = 1 / (2 * (1 / (n + 1))**2)

# 5x5 Matrix constructed with diagflat function
T = (
    np.diagflat(2 * np.ones(n))
    - np.diagflat(np.ones(n - 1), 1)
    - np.diagflat(np.ones(n - 1), -1)
)
H = scalar * T

# Computes and sorts the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(H)
idx = np.argsort(eigenvalues)
eigenvectors = eigenvectors[:, idx]

# Eigenvector 5
fifth_ev = eigenvectors[:, 4]

# Positions for 5 eigenvectors
x_values = np.linspace(1 / (n + 1), n / (n + 1), n)

# Interval for plot
x_cont = np.linspace(0, 1, 500)
func = np.sqrt(2) * np.sin(np.pi * x_cont)

# Comparison of final result displayed on the graph
plt.figure()
plt.plot(
    x_values,
    fifth_ev,
    marker='o',
    linestyle='-',
    label='5th eigenvector',
)
plt.plot(
    x_cont,
    func,
    linestyle='--',
    label=r'$\sqrt{2}\sin(\pi x)$',
)
plt.xlabel('x')
plt.ylabel('y')
plt.title(
    '5th Eigenvector vs. '
    r'$\sqrt{2}\sin(\pi x)$'
)
plt.legend()
plt.grid(True)
plt.show()