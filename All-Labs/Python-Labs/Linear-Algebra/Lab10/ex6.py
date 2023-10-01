#bai 6

import numpy as np

A = np.array([
    [1, 2, 2],
    [0, 3, 2],
    [0, 0, 1]
])

w, P = np.linalg.eig(A)
print("w = ", w)
print("\nP = \n", P)
P_1 = np.linalg.inv(P)
print("\nP^-1 = \n", P_1)

res = np.matmul(np.matmul(P_1, A), P)
print("\nP^-1 * A * P = \n", res)