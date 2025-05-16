import numpy as np


def calculate_quadratic_fit(data: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    """
    Accepts (2, M) arrays once again, however M >= 3 due to quadratic requirements.
    Rounds digits so the final answer remains accurate. Used AI assistant, Gemini 2.0 Flash,
    for help with the float rounding. Prompt: picture + "find out why my program's
    output is incorrect."
    """
    if data.ndim != 2 or data.shape[0] != 2 or data.shape[1] < 3:
        raise IndexError(
            f"Change format to (2, M) with M >= 3; got {data.shape}"
        )

    x = data[0]
    y = data[1]
    p = np.polyfit(x, y, 2)
    coeffs = p[::-1]
    small = np.isclose(coeffs, 0.0, atol=tol)
    coeffs[small] = 0.0

    return coeffs


if __name__ == "__main__":
    # Tests over interval [-1, 1]
    x = np.linspace(-1, 1, 50)
    y = x**2
    data = np.vstack([x, y])

    coeffs = calculate_quadratic_fit(data)
    print("Quadratic coefficients (c0, c1, c2) respectively:")
    print(coeffs)