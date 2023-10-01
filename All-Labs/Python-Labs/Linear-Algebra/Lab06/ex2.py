#bai 2

import numpy as np

B1 = np.array([[1, 7], [-2, -3]])
B2 = np.array([[3, 6], [1, 0]])
B3 = np.array([[5, 4, 2], [-1, 2, 3], [2, 1, 0]])
B4 = np.array([[3, 6, -1], [3, 1, 0], [-2, 4, -7]])
B5 = np.array([[3, 0, 0], [0, 4, 0], [0, 0, 2]])

#infinity norm - cong cac phan tu trong hang voi nhau roi so sanh phan tu o hang nao max thi chon phan tu do

norm_infB1 = np.linalg.norm(B1, np.inf)
norm_infB2 = np.linalg.norm(B2, np.inf)
norm_infB3 = np.linalg.norm(B3, np.inf)
norm_infB4 = np.linalg.norm(B4, np.inf)
norm_infB5 = np.linalg.norm(B5, np.inf)

print("infinity norm B1 = ", norm_infB1)
print("infinity norm B2 = ", norm_infB2)
print("infinity norm B3 = ", norm_infB3)
print("infinity norm B4 = ", norm_infB4)
print("infinity norm B5 = ", norm_infB5)