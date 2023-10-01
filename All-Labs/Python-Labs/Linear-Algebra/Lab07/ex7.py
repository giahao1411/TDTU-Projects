#bai 7

import numpy as np

A = np.array([
    [1, 0, 2],
    [0, 1, 4],
    [2, -2, -4]
]).T

dim_span = np.linalg.matrix_rank(A)

rref, _ = np.linalg.qr(A)
basis = rref[:, :dim_span]

print("Dimension of span =", dim_span)
print("Basis of span = \n", basis)