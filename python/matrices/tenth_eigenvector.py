import numpy as np
import matplotlib.pyplot as plt


# Matrix dimension
matrix_dimension = 10

# Matrix scalar multiplied with H
scalar = 1 / (2 * (1 / (matrix_dimension + 1))**2)

# 10x10 Matrix constructed with diagflat function
T = (
    np.diagflat(2 * np.ones(matrix_dimension))
    - np.diagflat(np.ones(matrix_dimension - 1), 1)
    - np.diagflat(np.ones(matrix_dimension - 1), -1)
)
H = scalar * T

# Computes and sorts the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(H)
idx = np.argsort(eigenvalues)
eigenvectors = eigenvectors[:, idx]

# Eigenvector ten
tenth_ev = eigenvectors[:, matrix_dimension - 1]

# Positions for all ten eigenvectors
x_values = np.linspace(
    1 / (matrix_dimension + 1),
    matrix_dimension / (matrix_dimension + 1),
    matrix_dimension,
)

# Interval for plot
x_cont = np.linspace(0, 1, 500)
func = np.sqrt(2) * np.sin(np.pi * x_cont)

# Comparison of final result
plt.figure()
plt.plot(
    x_values,
    tenth_ev,
    marker='o',
    linestyle='-',
    label='10th eigenvector',
)
plt.plot(
    x_cont,
    func,
    linestyle='--',
    label=r'$\sqrt{2}\sin(\pi x)$',
)
plt.xlabel('x')
plt.ylabel('y')
plt.title('10th Eigenvector vs. $\\sqrt{2}\\sin(\\pi x)$')
plt.legend()
plt.grid(True)
plt.show()
