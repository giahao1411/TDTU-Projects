#bai 2

import numpy as np

A = np.array([
    [0, 0, 1],
    [0, 1, 1],
    [1, 2, 1],
    [1, 0, 1],
    [4, 1, 1],
    [4, 2, 1]
])

b = np.array([[0.5, 1.6, 2.8, 0.8, 5.1, 5.9]]).T

print("A = \n", A)
print("b = \n", b)

x = np.linalg.lstsq(A, b, rcond = None)

print("x = ", x)

x1 = x[0]

print("\nx [by lstsq function] = ", x1[0], x1[1])
print("- x1[1] = ", x1[0])
print("- x1[2] = ", x1[1])
print("- x1[3] = ", x1[2])