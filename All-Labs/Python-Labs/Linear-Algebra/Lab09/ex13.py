#bai 13

import numpy as np

A = np.array([
    [1, 2],
    [0, -3],
    [2, 6]
])

b = np.array([1, 1, 0])

print("A = \n", A)
print("\nb = \n", b)

res = np.linalg.lstsq(A, b, rcond=None)[0]

res_vector = A.dot(res)

print("\nResult = ", res_vector)