from numpy.linalg import norm
import numpy as np

def gauss_seidel(a_matrix, b_vector, initial_guess, tolerance=1e-16, max_iterations=200):
    n = len(a_matrix)
    k = 1

    if not is_diagonally_dominant(a_matrix):
        raise ValueError("The matrix is not diagonally dominant.")

    x = np.zeros(n, dtype=np.double)
    while k <= max_iterations:

        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += a_matrix[i][j] * x[j]
            x[i] = (b_vector[i] - sigma) / a_matrix[i][i]

        if norm(x - initial_guess, np.inf) < tolerance:
            return tuple(x)

        k += 1
        initial_guess = x.copy()

    print("Maximum number of iterations exceeded")
    return tuple(x)


def is_diagonally_dominant(matrix):
    for i in range(len(matrix)):
        sum_row = sum(abs(matrix[i][j]) for j in range(len(matrix)) if j != i)
        if abs(matrix[i][i]) <= sum_row:
            return False
    return True