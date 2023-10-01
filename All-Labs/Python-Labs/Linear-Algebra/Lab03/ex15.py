#bai 15

import numpy as np

A = np.array([
    [2, 4, 5/2],
    [-3/4, 2, 1/4],
    [1/4, 1/2, 2]
])

B = np.array([
    [1, -1/2, 3/4],
    [3/2, 1/2, -2],
    [1/4, 1, 1/2]
])

print("- Cau a:");
print("A.T x B.T = \n", np.matmul(A.T, B.T))
print("(A x B).T = A.T x B.T = \n", np.matmul(A.T, B.T))
print("(B x A).T = B.T x A.T = \n", np.matmul(B.T, A.T))
print("- Cau b:");
print("(A^-1).T = A = \n", A)
print("(A.T)^-1 = A = \n", A)