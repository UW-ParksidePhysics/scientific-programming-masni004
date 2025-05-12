import numpy as np


def calculate_bivariate_statistics(data: np.ndarray) -> np.ndarray:
    """
Verifies that the array is in the correct format, then calculates the bivariate statistics.
    """
    # Check dimensions: must be 2 rows and at least 2 columns
    if data.ndim != 2 or data.shape[0] != 2 or data.shape[1] < 2:
        raise IndexError(
            "Must enter array with format (2,M) "
            f"{data.shape}"
        )

    # Split into x and y arrays
    x_values = data[0]
    y_values = data[1]

    # Computes necessary statistics
    mean_y = np.mean(y_values)
    std_y = np.std(y_values)
    min_x = np.min(x_values)
    max_x = np.max(x_values)
    min_y = np.min(y_values)
    max_y = np.max(y_values)

    # 4) Returns array for graph
    return np.array([mean_y, std_y, min_x, max_x, min_y, max_y])


if __name__ == "__main__":
    """
    Calls the above function, as well as printing and organizing the data.
    """
    x = np.linspace(-10, 10, 101)
    y = x ** 2
    test_data = np.vstack([x, y])
    results = calculate_bivariate_statistics(test_data)

    labels = [
        "Mean of y      ",
        "Std. dev. of y ",
        "Min of x       ",
        "Max of x       ",
        "Min of y       ",
        "Max of y       ",
    ]

    print("Results for y = x² over x ∈ [-10, 10]:\n")
    for label, value in zip(labels, results):
        print(f"  {label}: {value:.4f}")