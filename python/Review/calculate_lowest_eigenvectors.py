import numpy as np


def calculate_lowest_eigenvectors(
    square_matrix: np.ndarray,
    number_of_eigenvectors: int = 3
) -> tuple[np.ndarray, np.ndarray]:
    """
    Takes an MxM matrix and outputs the smallest eigenvectors and their eigenvalues.
    """
    # Check that the matrix is MxM
    if square_matrix.ndim != 2 or square_matrix.shape[0] != square_matrix.shape[1]:
        raise IndexError(
            f"Only accepts square matrices {square_matrix.shape}"
        )

    M = square_matrix.shape[0]
    K = number_of_eigenvectors
    if not isinstance(K, int) or K < 1 or K > M:
        raise IndexError(
            f"number_of_eigenvectors must be 1 ≤ K ≤ {M}; got {K}"
        )

    vals, vecs = np.linalg.eig(square_matrix)
    selected = np.argsort(vals)[:K]
    lowest_vals = vals[selected]
    lowest_vecs = vecs[:, selected].T

    return lowest_vals, lowest_vecs


if __name__ == "__main__":
    # Tests  np.array([2, -1], [-1, 2]) and number_of_eigenvectors = 2
    mat = np.array([[2, -1],
                    [-1, 2]])
    k = 2
    eigvals, eigvecs = calculate_lowest_eigenvectors(mat, k)

    print(f"Eigenvalues (lowest {k}): {eigvals}")
    print("Eigenvectors (rows correspond to above eigenvalues):")
    for vec in eigvecs:
        print(f"  {vec}")