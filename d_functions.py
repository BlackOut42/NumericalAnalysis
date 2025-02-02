import numpy as np


def d1(L):
    A = 4.86
    B = 0.018
    return A + B * L


def d2(L):
    A = 3000
    return L / A


def d3(L):
    A0 = 0.0047
    A1 = 0.0023
    A2 = 0.000043
    return (A0 + A1 * np.log(L) + A2 * np.log(L) ** 2) * L


def d4(L):
    A = 4.2
    B = 0.0015
    C = 4 / 3
    return A + B * L ** C


def d5(L):
    A = 0.069
    B = 0.00156
    C = 0.00000047
    return A + B * L + C * (L ** 2)


def calculate_d1_d5(num):
    arr = [d1(num), d2(num), d3(num), d4(num), d5(num)]

    print("D1: " + str(arr[0]))
    print("D2: " + str(arr[1]))
    print("D3: " + str(arr[2]))
    print("D4: " + str(arr[3]))
    print("D5: " + str(arr[4]))
    print("\n")
    return arr