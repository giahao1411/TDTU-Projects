#bai 12 

import numpy as np

A = np.array([
    [6, 0, 0, 5],
    [1, 7, 2, -5],
    [2, 0, 0, 0],
    [8, 3, 1, 8]
])

B = np.array([
    [1, -2, 5, 2],
    [0, 0, 3, 0],
    [2, -6, -7, 5],
    [5, 0, 4, 4]
])

C = np.array([
    [3, 5, -8, 4],
    [0, -2, 3, -7],
    [0, 0, 1, 5],
    [0, 0, 0, 2]
])

D = np.array([
    [4, 0, 0, 0],
    [7, -1, 0, 0],
    [2, 6, 3, 0],
    [5, -8, 3, 0],
    [5, -8, 4, -3]
])

E = np.array([
    [4, 0, -7, 3, -5],
    [0, 0, 2, 0, 0],
    [7, 3, -6, 4, -8],
    [5, 0, 5, 2, -3],
    [0, 0, 9, -1, 2]
])

F = np.array([
    [6, 3, 2, 4, 0],
    [9, 0, -4, 1, 0],
    [8, -5, 6, 7, 1],
    [3, 0, 0, 0, 0],
    [4, 2, 3, 2, 0]
])

print("a: ", np.linalg.det(A))
print("b: ", np.linalg.det(B))
print("c: ", np.linalg.det(C))
print("d: D khong la ma tran vuong nen khong thuc dinh thuc")
print("e: ", np.linalg.det(E))
print("f: ", np.linalg.det(F))