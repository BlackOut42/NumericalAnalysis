import numpy as np


def polynomial_approximation(x_data, y_data, x):
    """
    Polynomial Approximation Interpolation

    Parameters:
    x_data (list): List of x-values for data points.
    y_data (list): List of y-values for data points.
    x (float): The x-value where you want to evaluate the interpolated polynomial.

    Returns:
    float: The interpolated y-value at the given x.
    """
    # Create a Vandermonde matrix
    A = np.vander(x_data, increasing=True)
    # Solve the linear system to find the polynomial coefficients
    coeffs = np.linalg.solve(A, y_data)
    # Evaluate the polynomial at x
    return sum([coeffs[i] * (x ** i) for i in range(len(coeffs))])