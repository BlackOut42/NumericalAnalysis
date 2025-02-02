import math
import numpy as np
import sympy as sp
from gauss_seidel import gauss_seidel
from simpsons_rule import simpsons_rule
from trapezoidal_rule import trapezoidal_rule
from bisection_method import bisection_method
from newton_raphson import newton_raphson
from secant_method import secant_method
from lagrange_interpolation import lagrange_interpolation
from lu import inverse_matrix, lu_decomposition, solve_lu
from polynomial_approximatio import polynomial_approximation
from d_functions import calculate_d1_d5
import matplotlib.pyplot as plt

x = sp.symbols('x')

if __name__ == '__main__':
    ###### integration #####
    print("\nQuestion 6:")
    n_trapezoid = 100
    n_simpson = 10
    a = 0
    b = 1
    f6 = lambda x: (math.cos((2*x**3) + (5*x**2)-6)) / (2*(math.e**(-2*x)))
    trapezoidal_result = trapezoidal_rule(f6, a, b, n_trapezoid)
    print(f"Trapezoidal ingegral result in range [{a},{b}] is {trapezoidal_result}")

    print(f"Division into n={n_simpson} sections ")
    q6_simpsons_result = simpsons_rule(f6, a, b, n_simpson)
    print(f"Simpson integration result in range [{a},{b}] is {q6_simpsons_result}")

    ##### intersection #####
    print("\nQuestion 7:")
    f7 = lambda x: (math.sin((2 * x ** 3) + (5 * x ** 2) - 6)) / 2 * (math.e ** (-2 * x))

    print("\nRaphson method:")
    q7_raphson_result = newton_raphson(f7, 1.42)  # closest guess to 1.5 that gives an intersection point in range.

    print(f"Intersection point {q7_raphson_result}")
    print("\nSecant method:")
    q7_secant_result = secant_method(f7, -1, 1.5)
    print(f"Intersection point {q7_secant_result}")
    ##### integration #####
    print("\nQuestion 12:")
    f12 = lambda x: (x*math.e**(-x) + math.log(x**2,math.e))*(2*x**3 + 2*x**2 -3*x -5)
    a = 0.5
    b = 1
    n = 10
    q12_trapezoidal_result = trapezoidal_rule(f12, a, b, n)
    q12_simpsons_result = simpsons_rule(f12, a, b, n)
    print("Trapezoidal integral:", q12_trapezoidal_result)
    print(f"Simpson integral in range :  [{a},{b}] is {q12_simpsons_result}")

    ##### intersection #####
    print("\nQuestion 17:")

    def f17(x):
        if x == 0:
            return float('nan')  # Or handle separately
        return (2 * x * math.exp(-x) + math.log(2 * x ** 2, math.e)) * (2 * x ** 2 - 3 * x - 5)

    q17_raphson_result = newton_raphson(f17, 3)
    q17_bisection_result = bisection_method(f17, 0, 3)
    print(q17_raphson_result)
    print(q17_bisection_result)

    ### Calc c
    print("\nQuestion 23: ")

    A = np.array([
        [10, 8, 1],
        [4, 10, -5],
        [5, 1, 10]
    ])
    b = np.array([-7, 2, 1.5])
    guess = np.zeros_like(b, dtype=np.double)

    q23_gauss_result = gauss_seidel(A, b, guess)
    q23_c_gauss = q23_gauss_result[2]
    print(f"\nApproximate solution:{q23_gauss_result}\nC: {q23_c_gauss}")

    ### LU
    A_inv = inverse_matrix(A)
    L,U = lu_decomposition(A)

    q23_LU_result = solve_lu(L, U, b)
    q23_c_LU = q23_LU_result[2]
    print(f"LU Decomposition result {q23_LU_result}\nC: {q23_c_LU}")

    #### interpolation ####
    print("\nQuestion 36: ")
    x_values = [2, 2.25, 2.3, 2.7]
    y_values = [0, 0.112463, 0.167996, 0.222709]
    x_point = 2.4
    q36_polynomial_app_result = polynomial_approximation(x_values, y_values, x_point)
    q36_lagrange_result = lagrange_interpolation(x_values,y_values, x_point)
    print(f"Polynomial Interpolation result at point 2.4: {q36_polynomial_app_result}\n")
    print(f"Lagrange Interpolation result at point 2.4: {q36_lagrange_result}")

    print("Q6")
    Q6_l = q6_simpsons_result * 800
    line1 = calculate_d1_d5(Q6_l)
    print("Q7")
    Q7_l = q7_raphson_result * 1200
    line2 = calculate_d1_d5(Q7_l)
    print("Q12")
    Q12_l = q12_simpsons_result * 850
    line3 = calculate_d1_d5(Q12_l)
    print("Q17")
    Q17_l = q17_raphson_result * 500
    line4 = calculate_d1_d5(Q17_l)
    print("Q23")
    Q23_l = q23_c_LU * 1500
    line5 = calculate_d1_d5(Q23_l)
    print("Q36")
    Q36_l = q36_lagrange_result * 1200
    line6 = calculate_d1_d5(Q36_l)

    l_values = [Q6_l,Q7_l,Q12_l,Q17_l,Q23_l,Q36_l]
    matrix = np.array(
              [
              line1,
              line2,
              line3,
              line4,
              line5,
              line6])

    plt.figure(figsize=(10, 6))

    for col in range(matrix.shape[1]):
        y_values = matrix[:, col]
        plt.plot(l_values, y_values, marker='o', label=f'Formula {col + 1}')

    plt.xlabel("L Values")
    plt.ylabel("D values")

    plt.grid(True)
    plt.legend()
    plt.show()
