''''
DANIEL NEKLUDOV 321984619
GAL RABINOVICH 209064500
ILYA KARAZHYA 323221846
DAVID ARONOV  318359411
'''
# git link: https://github.com/BlackOut42/NumericalAnalysis

import numpy
import numpy as np


def richardson(f, x, n, h):
    d = numpy.array([[0] * (n + 1)] * (n + 1), float)

    for i in range(n + 1):
        d[i, 0] = (f(x + h) - f(x - h)) / (2 * h)

        power_of_2 = 1  # 2^j
        for j in range(1, i + 1):
            power_of_2 = 2 * power_of_2
            d[i, j] = d[i, j - 1] + (d[i, j - 1] - d[i - 1, j - 1]) / (power_of_2 - 1)

        h = 0.5 * h

    return d


function = lambda x: np.sin(x)
x = np.pi / 4
extrapolation_levels = 2
step_size = 0.1

d = richardson(function, x, extrapolation_levels, step_size)
print(d)
print(f'\nFirst function: f`({x}) = {d[extrapolation_levels, extrapolation_levels]}\n')

function = lambda x: 5 * x * np.exp(-2 * x)
x = 0.35
extrapolation_levels = 2
step_size = 0.35

d = richardson(function, x, extrapolation_levels, step_size)
print(d)
print(f'\nSecond function: f`({x}) = {d[extrapolation_levels, extrapolation_levels]}\n')
