#bai 1

import numpy as np 

A1 = np.array([[1, -7], [-2, -3]])
A2 = np.array([[-2, 8], [3, 1]])
A3 = np.array([[2, -8], [3, 1]])
A4 = np.array([[2, 3], [1, 1]])
A5 = np.array([
    [5, -4, 2],
    [-1, 2, 3],
    [-2, 1, 0]
])

#norm 1 - cong cac phan tu o cot voi nhau va so sanh phan tu o cot nao max thi chon phan tu do

norm1_A1 = np.linalg.norm(A1, 1)
norm1_A2 = np.linalg.norm(A2, 1)
norm1_A3 = np.linalg.norm(A3, 1)
norm1_A4 = np.linalg.norm(A4, 1)
norm1_A5 = np.linalg.norm(A5, 1)

print("norm1_A1 = ", norm1_A1)
print("norm1_A2 = ", norm1_A2)
print("norm1_A3 = ", norm1_A3)
print("norm1_A4 = ", norm1_A4)
print("norm1_A5 = ", norm1_A5)