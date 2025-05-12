
import numpy as np
from numpy.polynomial import Polynomial


def fit_curve_array(
    quadratic_coefficients: np.ndarray,
    minimum_x: float,
    maximum_x: float,
    number_of_points: int = 100
) -> np.ndarray:
    """
    Inputs a quadratic function.
    Outputs a 2×N (N =number of function evaluation points)
    array of (x, y) points for the quadratic in format
    c0 + c1*x + c2*x^2.


    """
    if maximum_x < minimum_x:
        raise ArithmeticError(
            "maximum_x must be >= minimum_x "
            f"(got minimum_x={minimum_x}, maximum_x={maximum_x})"
        )
    if number_of_points <= 2:
        raise IndexError(
            "number_of_points must be > 2 "
            f"(got {number_of_points})"
        )

    #  Uses value for N to determine the x value spacing
    x_values = np.linspace(minimum_x, maximum_x, number_of_points)

    # Evaluates the polynomial
    poly = Polynomial(quadratic_coefficients)
    y_values = poly(x_values)

    # Returns 2xN array
    return np.vstack([x_values, y_values])


if __name__ == "__main__":
    # Tests on [-2, 2]
    coeffs = np.array([0.0, 0.0, 1.0])
    fit = fit_curve_array(coeffs, -2.0, 2.0)

    print(f"fit_curve shape: {fit.shape}\n")
    print("First 5 (x, y) pairs:")
    for x, y in zip(fit[0, :5], fit[1, :5]):
        print(f"  x = {x:.2f}, y = {y:.2f}")

    # Verify that y == x^2
    if np.allclose(fit[1], fit[0]**2):
        print("\nSuccess, y matches x^2 for all points.")
    else:
        print("\nFailure, y doesn't match x^2.")