import numpy as np


def max_steps(a, b, tol):
    return int(np.ceil(np.log2((b - a) / tol)))  # Calculate max steps


def bisection_method(f, a, b, tol=1e-6):
    if np.sign(f(a)) == np.sign(f(b)):  # Ensure root is bounded
        return f'BISECTION METHOD: The scalars {a} and {b} do not bound a root'

    c, k = 0, 0
    steps = max_steps(a, b, tol)  # Calculate max possible steps

    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
        "Iteration", "a", "b", "f(a)", "f(b)", "c", "f(c)"))

    while abs(b - a) > tol and k < steps:
        c = (a + b) / 2  # Midpoint

        if abs(f(c)) < tol:  # Stop early if function value is close to zero
            return c

        prev_a, prev_b = a, b  # Store previous values
        prev_fa, prev_fb = f(prev_a), f(prev_b)  # Function values

        if f(c) * f(a) < 0:
            b = c  # Move left
        else:
            a = c  # Move right

        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f}".format(
            k, prev_a, prev_b, prev_fa, prev_fb, c, f(c)))

        k += 1

    return c  # Return the root approximation