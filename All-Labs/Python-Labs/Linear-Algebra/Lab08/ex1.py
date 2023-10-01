#bai 1

import numpy as np

#example - least square solution

A = np.array([[2, 1, 1], [1, 2, 1]]).T
b = np.array([2, 0, -3])

print("A = \n", A)
print("\nb = ", b)

x1 = np.linalg.lstsq(A, b, rcond = None)

print("x1 = ", x1)

x = x1[0]

print("\nx [by lstsq function] = ", x[0], x[1])
print("- x[1] = ", round(x[0], 5))
print("- x[2] = ", round(x[1], 5))

#ex1
print("----Exercise 1:----")

A1 = np.array([
    [2, 2],
    [2, 3]
])

b1 = np.array([4, 6]).T

print("A = \n", A1)
print("\nb = ", b1)

x2 = np.linalg.lstsq(A1, b1, rcond = None)

print("x2 = ", x2)

s = x2[0]

print("\ns [by lstsq function] = ", s[0], s[1])
print("- s[1] = ", round(s[0], 5))
print("- s[2] = ", s[1])