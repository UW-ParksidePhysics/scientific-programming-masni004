import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from typing import List


def plot_data_with_fit(
    data: np.ndarray,
    fit_curve: np.ndarray,
    data_format: str = 'o',
    fit_format: str = ''
) -> List[Line2D]:
    """
   Accepts a (2,M) array, checks it, and returns a Line2D plot
    """
    if data.ndim != 2 or data.shape[0] != 2:
        raise IndexError(f"data must be shape (2, M), got {data.shape}")
    if fit_curve.ndim != 2 or fit_curve.shape[0] != 2:
        raise IndexError(f"fit_curve must be shape (2, N), got {fit_curve.shape}")

    x_data, y_data = data
    x_fit, y_fit = fit_curve

    # Plots the graph
    line_data, = plt.plot(x_data, y_data, data_format, label='data')
    line_fit, = plt.plot(x_fit, y_fit, fit_format, label='fit')

    # Details the graph
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Data with Fit')

    return [line_data, line_fit]


if __name__ == "__main__":
   """
   Tests using [[-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]
    and the fit_curve = [np.linspace(-2, 2),  np.linspace(-2, 2)**2]
   """

data = np.array([[-2, -1, 0, 1, 2],
                     [ 4,  1, 0, 1, 4]])
xs = np.linspace(-2, 2, 100)
fit = np.vstack([xs, xs**2])
lines = plot_data_with_fit(data, fit, data_format='x', fit_format='--')
plt.show()