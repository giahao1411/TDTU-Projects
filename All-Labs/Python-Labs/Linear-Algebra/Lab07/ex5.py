#bai 5

import numpy as np

#cau a
print("Cau a:")
w = np.array([1, 1, -1, -3]).reshape(-1, 1)
A = np.array([
    [7, 6, -4, 1],
    [-5, -1, 0, -2],
    [9, -11, 7, -3],
    [19, -9, 7, 1]
])

U, s, V = np.linalg.svd(A)
CS = U.dot(U.T.dot(w))

NS = V.T[:, s < 1e-10]

count = 0
if np.allclose(w, CS):
    print("w is in the column space of A")
    count = count + 1
else:
    print("w is not in the column space of A")

Aw = A.dot(w)
if np.allclose(Aw, np.zeros((A.shape[0], 1))):
    print("w is in the null space of A")
    count = count + 1
else:
    print("w is not in the null space of A")

if (count ==2):
    print("w is both the column space and null space of A")
else:
    print("w is not both the column space and null space of A")

#cau b
print("Cau b:")
w = np.array([1, 2, 1, 0]).reshape(-1, 1)

A = np.array([
    [-8, 5, -2, 0],
    [-5, 2, 1, -2],
    [10, -8, 6, -3],
    [3, -2, 1, 0]
])

U, s, V = np.linalg.svd(A)
CS = U.dot(U.T.dot(w))

NS = V.T[:, s < 1e-10]

count = 0
if np.allclose(w, CS):
    print("w is in the column space of A")
    count = count + 1
else:
    print("w is not in the column space of A")

Aw = A.dot(w)
if np.allclose(Aw, np.zeros((A.shape[0], 1))):
    print("w is in the null space of A")
    count = count + 1
else:
    print("w is not in the null space of A")

if (count== 2):
    print("w is both the column space and null space of A")
else:
    print("w is not both the column space and null space of A")