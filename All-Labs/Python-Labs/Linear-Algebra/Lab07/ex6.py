#bai 6

import numpy as np

A = np.array([
    [5, 1, 2, 2, 0],
    [3, 3, 2, -1, -12],
    [8, 4, 4, -5, 12],
    [2, 1, 1, 0, -2]
])

B = A[:, [0, 1, 3]]

rank_B = np.linalg.matrix_rank(B)
U, s, V = np.linalg.svd(B)
CS_B = U[:, :rank_B]

a3 = A[:, 2]
a5 = A[:, 4]

proj_a3 = CS_B.dot(np.linalg.inv(CS_B.T.dot(CS_B))).dot(CS_B.T).dot(a3)
proj_a5 = CS_B.dot(np.linalg.inv(CS_B.T.dot(CS_B))).dot(CS_B.T).dot(a5)

if np.allclose(proj_a3, a3):
    print("a3 is in the column space of B")
else:
    print("a3 is not in the column space of B")

if np.allclose(proj_a5, a5):
    print("a5 is in the column space of B")
else:
    print("a5 is not in the column space of B")